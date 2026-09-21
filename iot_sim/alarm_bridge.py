"""Tek alarm kararı; geçiş kaydı kotadan bağımsız, yalnız tekrarlar sınırlı."""
from collections import deque
from CALCULATOR import RateLimiter
from .sensors import VALUE_ATTR

STATUS_LABELS = {"WAITING": "İlk ölçüm bekleniyor", "OFF": "Kapalı", "EMPTY": "Pil bitti",
                 "NORMAL": "Normal", "ALERT": "Alarm"}


class AlarmBridge:
    """Sensör durumlarını, sınırlı olay geçmişini ve bildirim kotasını yönetir."""
    def __init__(self, rate_limit=40, window_seconds=60, on_event=None):
        self.now = 0.0
        self.window_seconds = window_seconds
        self.on_event = on_event
        self.events = deque(maxlen=1000)
        self.notifications = deque(maxlen=200)
        self.active_alerts = {}
        self.limiter_exhausted = {}
        self.states = {}
        self.flags = {}
        self.slots = {}
        self.last_written = {}
        self.last_repeat = {}
        self.total_events = 0

    def _emit(self, e, channel, kind, value, details):
        event = dict(t=round(self.now, 6), sensor_id=e.id, sensor_name=e.name,
                     channel=channel, kind=kind, value=value, details=details)
        self.events.append(event)
        self.total_events += 1
        if self.on_event:
            self.on_event(event)
        if kind in ("ALERT", "CALM"):
            self.notifications.append(event)
        return event

    def update(self, entities, sim_time):
        """Geçerli örnekleri ortak eşik/histerezis kuralıyla değerlendir."""
        self.now = sim_time
        ids = {e.id for e in entities if e.sensor}
        for mapping in (self.states, self.flags, self.slots, self.last_written,
                        self.last_repeat, self.active_alerts, self.limiter_exhausted):
            for eid in list(mapping):
                if eid not in ids:
                    del mapping[eid]
        for e in entities:
            s = e.sensor
            if s is None:
                continue
            if e.id not in self.slots:
                self.slots[e.id] = RateLimiter(s.max_limit, clock=lambda: self.now)
                self.slots[e.id].window_seconds = self.window_seconds
                self.slots[e.id].remaining = min(s.limit, s.max_limit)
            limiter = self.slots[e.id]
            limiter.max_remaining = s.max_limit
            if e.id in self.last_written and s.limit != self.last_written[e.id]:
                limiter.remaining = min(s.max_limit, max(0, s.limit))
            limiter.remaining = min(limiter.remaining, s.max_limit)
            limiter.refresh()
            previous = self.flags.get(e.id, set())
            current = set()
            if s.valid:
                for mode in sorted(s.modes, key=lambda m: m.value):
                    channel = mode.value
                    value = getattr(s, VALUE_ATTR[channel])
                    if value is None:
                        continue
                    alarm = value >= s.thresholds[channel] if channel not in previous else value >= s.clear_thresholds[channel]
                    if alarm:
                        current.add(channel)
                    if alarm != (channel in previous):
                        self._emit(e, channel, "ALERT" if alarm else "CALM", value,
                                   "Alarm başladı" if alarm else "Alarm sona erdi")
                for removed in previous - {m.value for m in s.modes}:
                    self._emit(e, removed, "UNAVAILABLE", None, "Kanal kapatıldı")
                s.status = "ALERT" if current else "NORMAL"
            elif previous:
                self._emit(e, "", "UNAVAILABLE", None, STATUS_LABELS.get(s.status, s.status))
            if self.states.get(e.id) != s.status:
                self._emit(e, "", "STATUS", None, STATUS_LABELS.get(s.status, s.status))
            if current:
                self.active_alerts[e.id] = sorted(current)
                last = self.last_repeat.get(e.id, self.now)
                if current != previous:
                    last = self.now
                if s.repeat_seconds > 0 and self.now - last + 1e-9 >= s.repeat_seconds:
                    if limiter.allow():
                        self.notifications.append(dict(t=self.now, sensor_id=e.id, channel=",".join(sorted(current)),
                                                       kind="REPEAT", details="Alarm devam ediyor", value=None))
                    last = self.now
                self.last_repeat[e.id] = last
            else:
                self.active_alerts.pop(e.id, None)
                self.last_repeat.pop(e.id, None)
            self.flags[e.id], self.states[e.id] = current, s.status
            s.limit = self.last_written[e.id] = limiter.remaining
            if limiter.remaining == 0:
                self.limiter_exhausted[e.id] = True
            else:
                self.limiter_exhausted.pop(e.id, None)

    @property
    def alert_count(self):
        return len(self.active_alerts)

    @property
    def log_lines(self):
        return [f"{e['t']:.1f}s #{e['sensor_id']} {e['channel']} {e['kind']} {e['details']}"
                for e in self.events]

    def get_sensor_status(self, entity_id):
        return self.states.get(entity_id, "WAITING")

    def get_limiter_info(self, entity_id):
        limiter = self.slots.get(entity_id)
        return f"Tekrar bildirimi: {limiter.remaining}/{limiter.max_remaining}" if limiter else ""
