"""Sabit zaman adımıyla, Pygame olmadan çalıştırılabilen deney."""
from collections import defaultdict, deque
from copy import deepcopy
import random
from .alarm_bridge import AlarmBridge
from .sensors import simulate_tick, invalidate, VALUE_ATTR
from .fire import spread_fire
from .uav import update_uavs
from .scene import to_scene, parse_scene

STEP = 0.05


class Simulation:
    def __init__(self, scene=None):
        if scene is None:
            scene = to_scene([])
        self.entities, self.seed, self.width, self.height, self.lesson = parse_scene(scene)
        self.baseline = deepcopy(scene)
        self.rng = random.Random(self.seed)
        self.steps = 0
        self.pending = 0.0
        self.revision = 0
        self.cache_token = object()
        self.next_id = max((e.id for e in self.entities), default=0) + 1
        self.history = defaultdict(lambda: deque(maxlen=600))
        self.exporter = None
        self.alarm = AlarmBridge(on_event=self._event)
        self.alarm.update(self.entities, 0)

    @property
    def time(self):
        return round(self.steps * STEP, 6)

    def snapshot(self):
        return to_scene(self.entities, self.seed, self.width, self.height, self.lesson)

    def _event(self, event):
        if self.exporter:
            self.exporter.log_event(event)

    def start_recording(self, exporter):
        self.exporter = exporter
        for event in self.alarm.events:
            exporter.log_event(event)

    def _record_sensor(self, e):
        """Ölçüm veya geçersizlik geçişini aynı anda grafiğe ve dosyaya yaz."""
        s = e.sensor
        self.history[e.id].append(dict(t=self.time, measured={k: getattr(s, attr) for k, attr in VALUE_ATTR.items()},
            theoretical=dict(s.theoretical), battery=s.battery, status=s.status,
            thresholds=dict(s.thresholds), alarms=sorted(self.alarm.flags.get(e.id, set()))))
        if self.exporter:
            self.exporter.log_sensor(self.time, e, self.entities)

    def invalidate_sensor(self, e):
        """Editörden kapatılan/değişen sensörün eski okumasını geçersiz kıl."""
        s = e.sensor
        status = "OFF" if not s.enabled or not s.modes else "EMPTY" if s.battery <= 0 else "WAITING"
        invalidate(s, status)
        self.alarm.update(self.entities, self.time)
        self._record_sensor(e)

    def advance(self, seconds):
        """Süre biriktir; hareket, enerji ve yangını aynı sabit sırada yürüt."""
        if not 0 <= seconds <= 3600:
            raise ValueError("İlerleme süresi 0–3600 saniye olmalı.")
        self.pending += seconds
        count = int((self.pending + 1e-9) / STEP)
        self.pending = max(0.0, self.pending - count * STEP)
        for _ in range(count):
            update_uavs(self.entities, STEP, self.width, self.height)
            burning = spread_fire(self.entities, STEP)
            self.steps += 1
            changed = simulate_tick(self.entities, STEP, self.rng)
            # Bildirim ve olay saatleri örnekleme aralığını beklemez.
            self.alarm.update(self.entities, self.time)
            for e in changed:
                self._record_sensor(e)
            for e in burning:
                self.alarm._emit(e, "TEMP", "FIRE", e.source.temp_celcius, "Tutuşma sıcaklığı ve süresi sağlandı")
        return count

    def reset(self):
        """Başlangıç sahnesi ve RNG aynı olacak şekilde yeni deney üret."""
        return Simulation(deepcopy(self.baseline))
