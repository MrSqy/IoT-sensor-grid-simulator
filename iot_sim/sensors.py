"""Noktasal alan, cihaz hatası ve örnek başına enerji: ekran bağımsız model."""
import math
import random
from .models import Entity, Kind, SourceType, SensorMode

AMBIENT_TEMP_C = 22.0
VALUE_ATTR = {"TEMP": "last_temp", "CO": "last_co", "CO2": "last_co2", "H2": "last_h2"}


def position(entity: Entity, entities: list[Entity]) -> tuple[float, float]:
    """Taşınan cihaz ve kaynak için drone'un kesintisiz konumunu kullan."""
    target = entity
    if entity.carried_by is not None:
        target = next((e for e in entities if e.id == entity.carried_by), entity)
    return (target.uav.x, target.uav.y) if target.uav else (target.tx, target.ty)


def field_at(x: float, y: float, entities: list[Entity]) -> dict[str, float]:
    """Kaynakların katkısını topla; duvar/rüzgâr ve zamanla difüzyon modeli yok."""
    result = {"TEMP": AMBIENT_TEMP_C, "CO": 0.0, "CO2": 0.0, "H2": 0.0}
    for e in entities:
        s = e.source
        if s is None or e.kind not in (Kind.SOURCE, Kind.BURNED):
            continue
        px, py = position(e, entities)
        distance = math.hypot(x - px, y - py)
        if s.stype == SourceType.TEMP:
            attenuation = max(0.0, 1 - distance / max(1, s.range_tiles)) ** 1.5
            result["TEMP"] += (s.temp_celcius - AMBIENT_TEMP_C) * attenuation
        else:
            for mode in s.gas_modes:
                key = mode.value.lower()
                attenuation = max(0.0, 1 - distance / max(1, getattr(s, key + "_range"))) ** 1.3
                result[mode.value] += getattr(s, key + "_ppm") * attenuation
    return result


def invalidate(sensor, status: str):
    """Veri yokluğunu sıfır ölçümden ayır; eski okumaları temizle."""
    sensor.status = status
    sensor.active = sensor.valid = False
    sensor.theoretical = {}
    for attr in VALUE_ATTR.values():
        setattr(sensor, attr, None)
    sensor.last_gas = 0.0


def simulate_tick(entities: list[Entity], dt_seconds: float, rng=None) -> list[Entity]:
    """Enerjiyi ilerlet; zamanı gelen sensörleri örnekle ve değişenleri döndür."""
    rng = rng or random
    changed = []
    for e in sorted(entities, key=lambda item: item.id):
        s = e.sensor
        if e.kind != Kind.SENSOR or s is None:
            continue
        unavailable = "OFF" if not s.enabled or not s.modes else "EMPTY" if s.battery <= 0 else None
        if unavailable:
            if s.status != unavailable or s.valid:
                invalidate(s, unavailable)
                changed.append(e)
            continue
        if not s.active:
            s.status, s.elapsed = "WAITING", 0.0
        s.active = True
        s.battery = max(0.0, s.battery - 0.02 * dt_seconds)
        s.elapsed += dt_seconds
        if s.battery <= 0:
            invalidate(s, "EMPTY")
            changed.append(e)
            continue
        if s.elapsed + 1e-9 < s.sample_interval:
            continue
        s.elapsed = max(0.0, s.elapsed - s.sample_interval)
        energy = 0.6 * len(s.modes) * 100 / max(1, s.efficiency)
        s.battery = max(0.0, s.battery - energy)
        if s.battery <= 0:
            invalidate(s, "EMPTY")
        else:
            s.theoretical = field_at(*position(e, entities), entities)
            for mode in SensorMode:
                value = None
                if mode in s.modes:
                    truth = s.theoretical[mode.value]
                    value = truth * (1 + rng.uniform(-s.noise_percent, s.noise_percent) / 100) + s.offsets[mode.value]
                    if mode != SensorMode.TEMP:
                        value = max(0.0, value)
                setattr(s, VALUE_ATTR[mode.value], value)
            s.last_gas = sum(getattr(s, a) or 0 for a in ("last_co", "last_co2", "last_h2"))
            s.valid = True
        changed.append(e)
    return changed
