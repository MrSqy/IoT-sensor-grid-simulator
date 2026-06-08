import math
import random
from typing import List, Tuple

from .models import (
    Entity, Kind, SourceType, GasMode, SensorMode,
    SensorProps, SourceProps,
    GAS_CRITICAL_PPM, TEMP_CRITICAL_C,
)
from .engine import clamp, accuracy_for_dist


Point = Tuple[float, float]

# Ortam sabitleri
AMBIENT_TEMP_C = 22.0   # °C — ortam sıcaklığı

# Threat polygon ray sayısı
THREAT_RAYS = 16


def _shoelace_area(poly: List[Point]) -> float:
    n = len(poly)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - y1 * x2
    return abs(s) * 0.5


# ------------------------------------------------------------------ #
#  Gerçekçi kaynak katkısı hesabı                                     #
# ------------------------------------------------------------------ #

def _temp_at_distance(src: SourceProps, d: float) -> float:
    """
    TEMP kaynağından d tile uzaklıktaki sıcaklık (°C).

    Model: T(d) = T_ambient + (T_source - T_ambient) * attenuation
    attenuation = max(0, 1 - d / range)^1.5   (1/r^2'ye yakın düşüş)
    """
    if d > max(0.001, float(src.range_tiles)):
        return AMBIENT_TEMP_C

    att = max(0.0, 1.0 - d / max(0.001, float(src.range_tiles)))
    att = att ** 1.5   # doğrusal değil, daha hızlı düşer

    delta = (src.temp_celcius - AMBIENT_TEMP_C) * att
    return AMBIENT_TEMP_C + delta


def _gas_ppm_at_distance(src: SourceProps, d: float, gas: GasMode) -> float:
    """
    GAS kaynağından d tile uzaklıktaki belirli gazın ppm değeri.

    Her gazın kendi ppm ve menzil değeri var.
    Kaynak sadece gas_modes'unda aktif olan gazları yayar.
    """
    if gas not in src.gas_modes:
        return 0.0

    # Gaz bazlı ppm ve menzil
    if gas == GasMode.CO:
        ppm, rng = src.co_ppm, src.co_range
    elif gas == GasMode.CO2:
        ppm, rng = src.co2_ppm, src.co2_range
    else:  # H2
        ppm, rng = src.h2_ppm, src.h2_range

    rng_f = max(0.001, float(rng))
    if d > rng_f:
        return 0.0

    att = max(0.0, 1.0 - d / rng_f)
    att = att ** 1.3

    return ppm * att


# ------------------------------------------------------------------ #
#  Sensörün algıladığı değerler (doğruluk düşüşü dahil)             #
# ------------------------------------------------------------------ #

def _source_contrib_at_point(
    px: float, py: float,
    src: Entity,
) -> Tuple[float, float, float, float]:
    """
    Bir noktadaki kaynak katkısı: (temp_C, co_ppm, co2_ppm, h2_ppm)
    Sensör doğruluğu UYGULANMAZ — sadece fizik modeli.
    """
    sp = src.source
    if sp is None:
        return 0.0, 0.0, 0.0, 0.0

    d = math.hypot(px - src.tx, py - src.ty)

    temp_c = 0.0
    co_ppm = 0.0
    co2_ppm = 0.0
    h2_ppm = 0.0

    if sp.stype == SourceType.TEMP:
        temp_c = _temp_at_distance(sp, d) - AMBIENT_TEMP_C  # delta olarak
    elif sp.stype == SourceType.GAS:
        co_ppm  = _gas_ppm_at_distance(sp, d, GasMode.CO)
        co2_ppm = _gas_ppm_at_distance(sp, d, GasMode.CO2)
        h2_ppm  = _gas_ppm_at_distance(sp, d, GasMode.H2)

    return temp_c, co_ppm, co2_ppm, h2_ppm


def _perceived_field_at(
    px: float, py: float,
    sx: int, sy: int,
    sources: List[Entity],
) -> Tuple[float, float, float, float]:
    """
    Sensörün (sx,sy) konumundan (px,py) noktasını algılaması.
    Doğruluk düşüşü mesafeye göre uygulanır.
    Döndürür: (temp_C, co_ppm, co2_ppm, h2_ppm)
    """
    t_total = 0.0
    co_total = 0.0
    co2_total = 0.0
    h2_total = 0.0

    for src in sources:
        dt, dco, dco2, dh2 = _source_contrib_at_point(px, py, src)
        t_total += dt
        co_total += dco
        co2_total += dco2
        h2_total += dh2

    # Sensör doğruluğu (sensör -> nokta mesafesi)
    ds = int(round(math.hypot(px - sx, py - sy)))
    acc = accuracy_for_dist(ds) / 100.0
    if acc <= 0:
        return 0.0, 0.0, 0.0, 0.0

    return t_total * acc, co_total * acc, co2_total * acc, h2_total * acc


# ------------------------------------------------------------------ #
#  Threat polygon                                                     #
# ------------------------------------------------------------------ #

def _build_threat_polygon(sensor_ent: Entity, sources: List[Entity]) -> List[Point]:
    s = sensor_ent.sensor
    if s is None:
        return []

    sx, sy = float(sensor_ent.tx), float(sensor_ent.ty)
    rng = max(1, int(s.range_tiles))

    # Herhangi bir kritik eşik aşılıyor mu?
    threat_temp = s.last_temp >= TEMP_CRITICAL_C
    threat_co   = s.last_co  >= GAS_CRITICAL_PPM[GasMode.CO]
    threat_co2  = s.last_co2 >= GAS_CRITICAL_PPM[GasMode.CO2]
    threat_h2   = s.last_h2  >= GAS_CRITICAL_PPM[GasMode.H2]

    if not (threat_temp or threat_co or threat_co2 or threat_h2):
        return []

    pts: List[Point] = []
    rays = max(8, THREAT_RAYS)

    for i in range(rays):
        ang = 2.0 * math.pi * (i / rays)
        dx = math.cos(ang)
        dy = math.sin(ang)
        hit: Point | None = None

        for step in range(1, rng + 1):
            px = sx + dx * step
            py = sy + dy * step
            pt, pco, pco2, ph2 = _perceived_field_at(px, py, int(sx), int(sy), sources)

            ok = False
            if threat_temp and (AMBIENT_TEMP_C + pt) >= TEMP_CRITICAL_C:
                ok = True
            if threat_co and pco >= GAS_CRITICAL_PPM[GasMode.CO]:
                ok = True
            if threat_co2 and pco2 >= GAS_CRITICAL_PPM[GasMode.CO2]:
                ok = True
            if threat_h2 and ph2 >= GAS_CRITICAL_PPM[GasMode.H2]:
                ok = True

            if ok:
                hit = (px, py)
            else:
                if hit is not None:
                    break

        if hit is not None:
            pts.append(hit)

    return pts


# ------------------------------------------------------------------ #
#  Ana simülasyon tick'i                                              #
# ------------------------------------------------------------------ #

def simulate_tick(entities: List[Entity], dt_seconds: float):
    """
    Her tick'te:
    - Sensör pil tüketimi
    - Sıcaklık ölçümü (°C)
    - Gaz ölçümleri (CO, CO2, H2 ppm — bağımsız)
    - Threat polygon hesabı
    """
    sources = [
        e for e in entities
        if e.kind in (Kind.SOURCE, Kind.BURNED)
        and e.source is not None
    ]

    for e in entities:
        if e.kind != Kind.SENSOR or e.sensor is None:
            continue

        s = e.sensor

        # --- Pil tüketimi ---
        rng = max(1, int(s.range_tiles))
        eff = clamp(int(s.efficiency), 1, 100)
        base = float(rng * rng)
        mult = 1.0 + (100 - eff) / 100.0
        drain = base * mult * float(dt_seconds)

        if s.battery <= 0.0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_co = 0.0
            s.last_co2 = 0.0
            s.last_h2 = 0.0
            s.last_gas = 0.0
            s.threat_active = False
            s.threat_points = []
            s.threat_area = 0.0
            continue

        s.battery = s.battery - drain
        if s.battery <= 0.0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_co = 0.0
            s.last_co2 = 0.0
            s.last_h2 = 0.0
            s.last_gas = 0.0
            s.threat_active = False
            s.threat_points = []
            s.threat_area = 0.0
            continue

        s.active = True

        # Sensör modları
        modes = s.modes if hasattr(s, 'modes') and s.modes else set()

        # --- Ölçümler (sadece aktif modlar) ---
        temp_delta = 0.0
        co_ppm = 0.0
        co2_ppm = 0.0
        h2_ppm = 0.0

        for src in sources:
            sp = src.source
            if sp is None:
                continue

            d = math.hypot(float(e.tx - src.tx), float(e.ty - src.ty))

            # Gaz kaynağı için en büyük gaz menzilini kontrol et
            max_src_range = float(sp.range_tiles)
            if sp.stype == SourceType.GAS:
                max_src_range = max(float(sp.co_range), float(sp.co2_range), float(sp.h2_range))

            if d > max_src_range + float(rng):
                continue

            acc = accuracy_for_dist(int(round(d))) / 100.0
            if acc <= 0:
                continue

            if sp.stype == SourceType.TEMP and SensorMode.TEMP in modes:
                if d <= max(0.001, float(sp.range_tiles)):
                    measured_temp = _temp_at_distance(sp, d)
                    temp_delta += (measured_temp - AMBIENT_TEMP_C) * acc

            elif sp.stype == SourceType.GAS:
                if SensorMode.CO in modes:
                    co_ppm  += _gas_ppm_at_distance(sp, d, GasMode.CO)  * acc
                if SensorMode.CO2 in modes:
                    co2_ppm += _gas_ppm_at_distance(sp, d, GasMode.CO2) * acc
                if SensorMode.H2 in modes:
                    h2_ppm  += _gas_ppm_at_distance(sp, d, GasMode.H2)  * acc

        # Sonuçları yaz (±%5 ölçüm gürültüsü, sadece aktif modlar)
        noise = lambda v: v * (1.0 + random.uniform(-0.05, 0.05)) if abs(v) > 0.01 else v

        s.last_temp = noise(AMBIENT_TEMP_C + temp_delta) if SensorMode.TEMP in modes else 0.0
        s.last_co   = max(0.0, noise(co_ppm))  if SensorMode.CO  in modes else 0.0
        s.last_co2  = max(0.0, noise(co2_ppm)) if SensorMode.CO2 in modes else 0.0
        s.last_h2   = max(0.0, noise(h2_ppm))  if SensorMode.H2  in modes else 0.0
        s.last_gas  = s.last_co + s.last_co2 + s.last_h2

        # --- Threat polygon ---
        poly = _build_threat_polygon(e, sources)

        if len(poly) >= 3:
            s.threat_active = True
            s.threat_points = poly
            s.threat_area = _shoelace_area(poly)
        else:
            s.threat_active = False
            s.threat_points = []
            s.threat_area = 0.0