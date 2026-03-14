# iot_sim/alarm_bridge.py
"""
Simülasyondaki sensör verileri ile CALCULATOR.py'deki alarm sistemini
birbirine bağlayan köprü modülü.

Kurallar:
  - Her sensör sadece aktif modları için limiter hakkı tüketir
    (örn: sadece TEMP açıksa tick başına 1 hak)
  - Her sensör kendi RateLimiter'ına sahip
  - Alarm hem terminale hem uygulama içi log buffer'a yazılır
"""

import datetime
import sys
import os

_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from CALCULATOR import (
    Logger,
    RateLimiter,
    Sensor as CalcSensor,
    CalibratedSensor,
    SensorKind,
    EventEngine,
    InMemoryStage,
    ConsoleNotifier,
    EventType,
    Event,
)

from .models import (
    Entity, Kind, GasMode, SensorMode,
    GAS_CRITICAL_PPM, TEMP_CRITICAL_C,
)


# ── Renk kodlu konsol çıktısı ──────────────────────────────────

_UNIT_MAP = {"TEMP": "°C", "CO": "ppm", "CO2": "ppm", "H2": "ppm"}


class PrettyNotifier(ConsoleNotifier):
    """CALCULATOR'ün ConsoleNotifier'ını override eder. Güzel konsol + log buffer."""

    def __init__(self):
        super().__init__()
        self.log_lines: list[str] = []
        self._max_lines = 200
        self.entity_names: dict[int, str] = {}  # entity_id -> display_name

    def notify(self, event: Event) -> None:
        ts = event.Ets.strftime("%H:%M:%S")
        name = event.detected_from
        parts = name.split("_", 1)
        kind_tag = parts[1] if len(parts) > 1 else event.Ekind.value
        unit = _UNIT_MAP.get(kind_tag, "")
        val = event.Evalue

        # Entity adını bul
        try:
            eid = int(parts[0].replace("S", ""))
            sensor_name = self.entity_names.get(eid, parts[0])
        except (ValueError, IndexError):
            sensor_name = parts[0]

        if event.Etype == EventType.ALERT:
            icon = "\033[91m⚠ ALERT\033[0m"
            plain_icon = "⚠ ALERT"
        else:
            icon = "\033[92m✓ CALM \033[0m"
            plain_icon = "✓ CALM"

        # Terminal: saat | durum | sensör adı | parametre | değer
        print(f"  {icon}  [{ts}]  {sensor_name}  {kind_tag}  {val:.1f} {unit}")

        # Uygulama içi log: [saat] sensör adı | parametre tipi | değer
        line = f"[{ts}] {plain_icon} {sensor_name} | {kind_tag} | {val:.1f} {unit}"
        self.log_lines.append(line)
        if len(self.log_lines) > self._max_lines:
            self.log_lines = self.log_lines[-self._max_lines:]


# ── Sensör slotu ────────────────────────────────────────────────

_MODE_TO_SLOT = {
    SensorMode.TEMP: "temp",
    SensorMode.CO:   "co",
    SensorMode.CO2:  "co2",
    SensorMode.H2:   "h2",
}


class _SensorSlot:
    """Bir sim sensörü için CALCULATOR tarafındaki tüm bileşenler."""

    def __init__(self, entity_id: int, rate_limit: int, window_seconds: int):
        self.entity_id = entity_id
        self._window_seconds = window_seconds
        self.limiter = RateLimiter(rate_limit)
        self.limiter.window_seconds = window_seconds

        # TEMP
        t_raw = CalcSensor(raw=0.0, name=f"S{entity_id}_TEMP",
                           kind=SensorKind.TEMP, min_deger=0, max_deger=1000)
        t_cal = CalibratedSensor(t_raw, offset=0, min_deger=-50, max_deger=50)
        self.temp = (t_raw, t_cal)

        # CO
        co_raw = CalcSensor(raw=0.0, name=f"S{entity_id}_CO",
                            kind=SensorKind.GAS, min_deger=0, max_deger=10000)
        co_cal = CalibratedSensor(co_raw, offset=0, min_deger=-100, max_deger=100)
        self.co = (co_raw, co_cal)

        # CO2
        co2_raw = CalcSensor(raw=0.0, name=f"S{entity_id}_CO2",
                             kind=SensorKind.GAS, min_deger=0, max_deger=100000)
        co2_cal = CalibratedSensor(co2_raw, offset=0, min_deger=-500, max_deger=500)
        self.co2 = (co2_raw, co2_cal)

        # H2
        h2_raw = CalcSensor(raw=0.0, name=f"S{entity_id}_H2",
                            kind=SensorKind.GAS, min_deger=0, max_deger=100000)
        h2_cal = CalibratedSensor(h2_raw, offset=0, min_deger=-500, max_deger=500)
        self.h2 = (h2_raw, h2_cal)

    def get_active_calibrated(self, modes: set[SensorMode]) -> list[CalibratedSensor]:
        """Sadece aktif modlara ait CalibratedSensor listesi döndürür."""
        result = []
        for mode in sorted(modes, key=lambda m: m.value):
            slot_name = _MODE_TO_SLOT.get(mode)
            if slot_name:
                pair = getattr(self, slot_name, None)
                if pair:
                    result.append(pair[1])
        return result

    def sync_limiter(self, sensor_props):
        """max_limit her zaman senkronize edilir. remaining sadece panel değiştirdiyse."""
        new_max = getattr(sensor_props, 'max_limit', 40)
        if new_max != self.limiter.max_remaining:
            self.limiter.max_remaining = new_max
            self.limiter.remaining = min(self.limiter.remaining, new_max)

        # Panel'den gelen limit, write_back'ten farklıysa kullanıcı elle değiştirmiş demektir
        panel_limit = getattr(sensor_props, 'limit', new_max)
        if hasattr(self, '_last_written_limit') and panel_limit != self._last_written_limit:
            self.limiter.remaining = min(panel_limit, new_max)

    def write_back_limit(self, sensor_props):
        sensor_props.limit = self.limiter.remaining
        sensor_props.max_limit = self.limiter.max_remaining
        self._last_written_limit = self.limiter.remaining


# ── Ana köprü sınıfı ───────────────────────────────────────────

class AlarmBridge:
    """
    Sim sensörlerini CALCULATOR alarm motoruna bağlar.
    Her sensör entity'si kendi RateLimiter'ına sahiptir.
    Sadece aktif modlar limiter hakkı tüketir.
    """

    def __init__(self, rate_limit: int = 40, window_seconds: int = 60):
        self._rate_limit = rate_limit
        self._window_seconds = window_seconds

        # Ortak bileşenler
        self.logger = Logger()
        self.logger.Clog = self._console_log
        self.storage = InMemoryStage()
        self.notifier = PrettyNotifier()

        # entity id -> _SensorSlot
        self._slots: dict[int, _SensorSlot] = {}

        # Panelde gösterilecek bilgiler
        self.active_alerts: dict[int, list[str]] = {}
        self.limiter_exhausted: dict[int, bool] = {}  # entity_id -> True (hakkı bitmiş)
        self.recent_alerts: list[dict] = []
        self._max_recent = 50

    @staticmethod
    def _console_log(msg: str):
        """Limiter mesajlarını konsola bas, geri kalanını sustur (PrettyNotifier zaten basıyor)."""
        if "Limiter" in msg:
            print(f"  ⏳ {msg}")

    def _ensure_slot(self, entity_id: int):
        if entity_id not in self._slots:
            self._slots[entity_id] = _SensorSlot(
                entity_id, self._rate_limit, self._window_seconds
            )

    def _remove_stale(self, active_ids: set[int]):
        stale = [eid for eid in self._slots if eid not in active_ids]
        for eid in stale:
            del self._slots[eid]
            self.active_alerts.pop(eid, None)

    def update(self, entities: list[Entity], sim_time: float):
        sim_sensors = [
            e for e in entities
            if e.kind == Kind.SENSOR
            and e.sensor is not None
            and e.carried_by is None
        ]
        active_ids = {e.id for e in sim_sensors}
        self._remove_stale(active_ids)

        # Entity isimlerini notifier'a aktar
        for e in sim_sensors:
            self.notifier.entity_names[e.id] = e.display_name

        for e in sim_sensors:
            s = e.sensor
            if s is None:
                continue

            modes = s.modes if hasattr(s, 'modes') and s.modes else set()
            if not modes:
                continue

            self._ensure_slot(e.id)
            slot = self._slots[e.id]

            # Limiter'ı sensör ayarlarıyla senkronize et
            slot.sync_limiter(s)

            # Raw değerleri aktar (sadece aktif modlar)
            if SensorMode.TEMP in modes:
                slot.temp[0].raw = max(0.0, min(1000.0, float(s.last_temp)))
            if SensorMode.CO in modes:
                slot.co[0].raw = max(0.0, min(10000.0, float(s.last_co)))
            if SensorMode.CO2 in modes:
                slot.co2[0].raw = max(0.0, min(100000.0, float(s.last_co2)))
            if SensorMode.H2 in modes:
                slot.h2[0].raw = max(0.0, min(100000.0, float(s.last_h2)))

            # Sadece aktif modların CalibratedSensor'larını EventEngine'e ver
            # Bu sayede her mod tick başına 1 limiter hakkı tüketir
            active_cals = slot.get_active_calibrated(modes)
            if not active_cals:
                continue

            engine = EventEngine(
                Csensors=active_cals,
                logger=self.logger,
                storage=self.storage,
                notifier=self.notifier,
                limiter=slot.limiter,
            )
            engine.tick()

            # Limiter'ın güncel durumunu SensorProps'a geri yaz
            slot.write_back_limit(s)

            # Limiter hakkı bittiyse kaydet ve log'a yaz
            if slot.limiter.remaining <= 0:
                self.limiter_exhausted[e.id] = True
                exhaust_line = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ⏳ LİMİT {e.display_name} | hak bitti ({s.max_limit}/{s.max_limit} tüketildi)"
                if not self.notifier.log_lines or self.notifier.log_lines[-1] != exhaust_line:
                    self.notifier.log_lines.append(exhaust_line)
                    if len(self.notifier.log_lines) > self.notifier._max_lines:
                        self.notifier.log_lines = self.notifier.log_lines[-self.notifier._max_lines:]
            else:
                self.limiter_exhausted.pop(e.id, None)

        # Gerçekçi eşik kontrolü (sadece aktif modlara göre)
        self.active_alerts.clear()
        for e in sim_sensors:
            eid = e.id
            s = e.sensor
            if s is None or eid not in self._slots:
                continue

            modes = s.modes if hasattr(s, 'modes') and s.modes else set()
            alerts = []

            if SensorMode.TEMP in modes and s.last_temp >= TEMP_CRITICAL_C:
                alerts.append(f"TEMP ({s.last_temp:.0f}°C)")
            if SensorMode.CO in modes and s.last_co >= GAS_CRITICAL_PPM[GasMode.CO]:
                alerts.append(f"CO ({s.last_co:.0f} ppm)")
            if SensorMode.CO2 in modes and s.last_co2 >= GAS_CRITICAL_PPM[GasMode.CO2]:
                alerts.append(f"CO2 ({s.last_co2:.0f} ppm)")
            if SensorMode.H2 in modes and s.last_h2 >= GAS_CRITICAL_PPM[GasMode.H2]:
                alerts.append(f"H2 ({s.last_h2:.0f} ppm)")

            if alerts:
                self.active_alerts[eid] = alerts

        all_events = self.storage.events
        self.recent_alerts = all_events[-self._max_recent:]

    # ── Sorgu metodları ─────────────────────────────────────────

    @property
    def alert_count(self) -> int:
        return len(self.active_alerts)

    @property
    def total_events(self) -> int:
        return len(self.storage.events)

    @property
    def log_lines(self) -> list[str]:
        """Uygulama içi log satırları (PrettyNotifier'dan)."""
        return self.notifier.log_lines

    def get_sensor_status(self, entity_id: int) -> str:
        if entity_id in self.active_alerts:
            kinds = self.active_alerts[entity_id]
            return "ALERT: " + " | ".join(kinds)
        if entity_id in self._slots:
            return "CALM"
        return "N/A"

    def get_limiter_info(self, entity_id: int) -> str:
        if entity_id not in self._slots:
            return ""
        lim = self._slots[entity_id].limiter
        return f"Limiter: {lim.remaining}/{lim.max_remaining}"

    def get_recent_alerts_text(self, n: int = 5) -> list[str]:
        result = []
        alerts_only = [
            ev for ev in self.recent_alerts
            if ev.get("emergency") == "ALERT"
        ]
        for ev in alerts_only[-n:]:
            ts = ev.get("timestamp", "")
            if isinstance(ts, datetime.datetime):
                ts = ts.strftime("%H:%M:%S")
            kind = ev.get("type", "?")
            sensor = ev.get("detected_from", "?")
            value = ev.get("value", 0)
            result.append(f"{ts} {kind} {sensor} val={value:.1f}")
        return result