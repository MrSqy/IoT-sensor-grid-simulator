from dataclasses import dataclass, field
from enum import Enum


class Kind(str, Enum):
    SENSOR = "SENSOR"
    SOURCE = "SOURCE"
    OBSTACLE = "OBSTACLE"
    BURNED = "BURNED"
    UAV = "UAV"


class SourceType(str, Enum):
    TEMP = "TEMP"
    GAS = "GAS"


class GasMode(str, Enum):
    CO  = "CO"
    CO2 = "CO2"
    H2  = "H2"


class SensorMode(str, Enum):
    TEMP = "TEMP"
    CO   = "CO"
    CO2  = "CO2"
    H2   = "H2"


class RouteMode(str, Enum):
    LOOP = "LOOP"
    PINGPONG = "PINGPONG"


# Eğitim varsayılanlarıdır; maruziyet/güvenlik standardı değildir.
GAS_CRITICAL_PPM: dict[GasMode, float] = {
    GasMode.CO:   35.0,
    GasMode.CO2:  5000.0,
    GasMode.H2:   4000.0,
}

GAS_DANGER_PPM: dict[GasMode, float] = {
    GasMode.CO:   200.0,
    GasMode.CO2:  40000.0,
    GasMode.H2:   40000.0,
}

TEMP_CRITICAL_C = 60.0
TEMP_DANGER_C   = 100.0


@dataclass
class SensorProps:
    threat_active: bool = False
    threat_points: list[tuple[float, float]] = field(default_factory=list)
    threat_area: float = 0.0

    range_tiles: int = 6
    efficiency: int = 80
    battery: float = 5000.0
    active: bool = True
    enabled: bool = True
    status: str = "WAITING"
    sample_interval: float = 1.0
    noise_percent: float = 5.0
    offsets: dict[str, float] = field(default_factory=lambda: {m.value: 0.0 for m in SensorMode})
    thresholds: dict[str, float] = field(default_factory=lambda: {"TEMP": 60.0, "CO": 35.0, "CO2": 5000.0, "H2": 4000.0})
    clear_thresholds: dict[str, float] = field(default_factory=lambda: {"TEMP": 55.0, "CO": 30.0, "CO2": 4500.0, "H2": 3500.0})
    theoretical: dict[str, float] = field(default_factory=dict)
    elapsed: float = 0.0
    repeat_seconds: float = 0.0
    valid: bool = False

    # Sensör modları — sadece seçili olanlar ölçülür
    # Varsayılan: hepsi açık
    modes: set[SensorMode] = field(default_factory=lambda: {
        SensorMode.TEMP, SensorMode.CO, SensorMode.CO2, SensorMode.H2
    })

    # Limiter ayarları (sensör bazlı)
    limit: int = 40        # mevcut penceredeki kalan işlem hakkı
    max_limit: int = 40    # pencere başına maksimum işlem hakkı

    # Ölçüm değerleri
    last_temp: float | None = None
    last_co:  float | None = None
    last_co2: float | None = None
    last_h2:  float | None = None
    last_gas: float = 0.0


@dataclass
class SourceProps:
    stype: SourceType = SourceType.TEMP

    temp_celcius: float = 300.0

    gas_modes: set[GasMode] = field(default_factory=set)

    co_ppm: float = 200.0
    co_range: int = 8

    co2_ppm: float = 15000.0
    co2_range: int = 10

    h2_ppm: float = 12000.0
    h2_range: int = 6

    power: int = 5
    range_tiles: int = 8


@dataclass
class UavProps:
    speed: float = 3.0
    route: list[tuple[int, int]] = field(default_factory=list)
    route_mode: RouteMode = RouteMode.LOOP
    route_dir: int = 1
    route_i: int = 0
    x: float = 0.0
    y: float = 0.0
    carrying_ids: list[int] = field(default_factory=list)
    show_route: bool = True
    blocked_reason: str = ""


@dataclass
class Entity:
    id: int
    kind: Kind
    tx: int
    ty: int
    name: str = ""          # kullanıcının vereceği özel isim
    sensor: SensorProps | None = None
    source: SourceProps | None = None
    uav: UavProps | None = None
    show_effect: bool = True
    carried_by: int | None = None
    icon_override: str | None = None
    flammable: bool = True
    ignition_temp: float = 120.0
    ignition_seconds: float = 3.0
    heat_seconds: float = 0.0

    @property
    def display_name(self) -> str:
        if self.name:
            return f"{self.name} (#{self.id})"
        return f"{self.kind.value} #{self.id}"
