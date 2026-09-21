"""Sürümlü başlangıç sahnesi; tam doğrulama sonrası nesne üretimi."""
import json
import math
import os
import tempfile
from dataclasses import asdict
from pathlib import Path
from .models import Entity, Kind, SensorProps, SourceProps, SourceType, SensorMode, GasMode, UavProps, RouteMode

SCHEMA_VERSION = 1
MODEL_VERSION = "education-2.0"
CHANNELS = ("TEMP", "CO", "CO2", "H2")
SENSOR_FIELDS = ("range_tiles", "efficiency", "battery", "enabled", "sample_interval", "noise_percent",
                 "offsets", "thresholds", "clear_thresholds", "modes", "limit", "max_limit", "repeat_seconds")
SOURCE_FIELDS = tuple(SourceProps.__dataclass_fields__)


def encode(value):
    """Enum, küme ve koordinatları standart JSON türlerine çevir."""
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (set, list, tuple)):
        items = sorted(value, key=str) if isinstance(value, set) else value
        return [encode(v) for v in items]
    return value.value if hasattr(value, "value") else value


def to_scene(entities, seed=42, width=200, height=200, lesson=0):
    """Canlı okumaları dışarıda bırakıp mevcut düzeni yeni başlangıç olarak kodla."""
    items = []
    for e in entities:
        row = {k: getattr(e, k) for k in ("id", "kind", "tx", "ty", "name", "show_effect", "carried_by",
                                          "icon_override", "flammable", "ignition_temp", "ignition_seconds")}
        if e.sensor:
            row["sensor"] = {k: getattr(e.sensor, k) for k in SENSOR_FIELDS}
        if e.source:
            row["source"] = asdict(e.source)
        if e.uav:
            row["uav"] = {k: getattr(e.uav, k) for k in ("speed", "route", "route_mode", "carrying_ids", "show_route")}
        items.append(encode(row))
    return dict(schema_version=SCHEMA_VERSION, model_version=MODEL_VERSION, seed=seed,
                width=width, height=height, lesson=lesson, entities=items)


def number(value, low, high, label, integer=False):
    """Boolean/NaN/sonsuz dahil bozuk sayıları reddet."""
    if type(value) not in (int, float) or not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{label}: {low}–{high} aralığında sayı gerekli.")
    if integer and type(value) is not int:
        raise ValueError(f"{label}: tam sayı gerekli.")
    return value


def boolean(value, label):
    if type(value) is not bool:
        raise ValueError(f"{label}: doğru/yanlış değeri gerekli.")
    return value


def object_fields(value, allowed, label):
    if not isinstance(value, dict) or set(value) - set(allowed):
        raise ValueError(f"{label}: bilinmeyen alan veya bozuk nesne.")
    return value


def parse_scene(data):
    """Bütün yapı ve çapraz referanslar geçerliyse yeni nesne listesi döndür."""
    try:
        object_fields(data, ("schema_version", "model_version", "seed", "width", "height", "lesson", "entities"), "Sahne")
        if type(data["schema_version"]) is not int or data["schema_version"] != SCHEMA_VERSION or data["model_version"] != MODEL_VERSION:
            raise ValueError("Desteklenmeyen sahne/model sürümü.")
        width = number(data["width"], 2, 200, "Genişlik", True)
        height = number(data["height"], 2, 200, "Yükseklik", True)
        seed = number(data["seed"], 0, 2**32 - 1, "Tohum", True)
        lesson = number(data.get("lesson", 0), 0, 6, "Deney", True)
        rows = data["entities"]
        if not isinstance(rows, list) or len(rows) > 500:
            raise ValueError("Sahne en fazla 500 nesne içerebilir.")
        entities, ids, occupied = [], set(), set()
        for row in rows:
            object_fields(row, ("id", "kind", "tx", "ty", "name", "show_effect", "carried_by", "icon_override",
                                "flammable", "ignition_temp", "ignition_seconds", "sensor", "source", "uav"), "Nesne")
            eid = number(row["id"], 1, 10**9, "Kimlik", True)
            if eid in ids:
                raise ValueError("Tekrarlanan nesne kimliği.")
            ids.add(eid)
            kind = Kind(row["kind"])
            x = number(row["tx"], 0, width - 1, "X", True)
            y = number(row["ty"], 0, height - 1, "Y", True)
            name = row.get("name", "")
            if not isinstance(name, str) or len(name) > 80:
                raise ValueError("İsim en fazla 80 karakter olmalı.")
            e = Entity(eid, kind, x, y, name=name)
            e.show_effect = boolean(row.get("show_effect", True), "Görünürlük")
            e.flammable = boolean(row.get("flammable", True), "Yanabilirlik")
            e.ignition_temp = number(row.get("ignition_temp", 120), 25, 1500, "Tutuşma sıcaklığı")
            e.ignition_seconds = number(row.get("ignition_seconds", 3), .1, 300, "Tutuşma süresi")
            e.carried_by = row.get("carried_by")
            if e.carried_by is not None:
                number(e.carried_by, 1, 10**9, "Taşıyıcı kimliği", True)
            elif kind != Kind.UAV and (x, y) in occupied:
                raise ValueError("Bağımsız nesneler aynı karede olamaz.")
            elif kind != Kind.UAV:
                occupied.add((x, y))
            icon = row.get("icon_override")
            if icon not in (None, "burned"):
                raise ValueError("Bilinmeyen ikon.")
            e.icon_override = icon
            expected = "sensor" if kind == Kind.SENSOR else "uav" if kind == Kind.UAV else "source" if kind in (Kind.SOURCE, Kind.BURNED) else None
            for key in ("sensor", "source", "uav"):
                if (key in row) != (key == expected):
                    raise ValueError("Nesne türü ile özellikleri uyuşmuyor.")
            if kind == Kind.SENSOR:
                p = object_fields(row["sensor"], SENSOR_FIELDS, "Sensör")
                s = SensorProps()
                bounds = {"range_tiles": (1, 50, True), "efficiency": (1, 100, True), "battery": (0, 1000000, False),
                          "sample_interval": (.1, 60, False), "noise_percent": (0, 50, False),
                          "limit": (0, 200, True), "max_limit": (0, 200, True), "repeat_seconds": (0, 300, False)}
                for key, (low, high, integer) in bounds.items():
                    setattr(s, key, number(p.get(key, getattr(s, key)), low, high, key, integer))
                if abs(s.sample_interval / .05 - round(s.sample_interval / .05)) > 1e-6:
                    raise ValueError("Örnekleme aralığı 0,05 saniyenin katı olmalı.")
                if s.limit > s.max_limit:
                    raise ValueError("Kalan bildirim hakkı maksimumu aşamaz.")
                s.enabled = boolean(p.get("enabled", True), "Sensör açık")
                modes = p.get("modes", list(CHANNELS))
                if not isinstance(modes, list) or len(modes) != len(set(modes)):
                    raise ValueError("Ölçüm kanalları tekrarsız liste olmalı.")
                s.modes = {SensorMode(m) for m in modes}
                for key in ("offsets", "thresholds", "clear_thresholds"):
                    values = p.get(key, getattr(s, key))
                    if not isinstance(values, dict) or set(values) != set(CHANNELS):
                        raise ValueError("Her kanalın ayarı gerekli.")
                    setattr(s, key, {k: number(v, -100000 if key == "offsets" else 0, 100000, key) for k, v in values.items()})
                if any(s.clear_thresholds[k] > s.thresholds[k] for k in CHANNELS):
                    raise ValueError("Alarm kapanış eşiği açılış eşiğini aşamaz.")
                e.sensor = s
            elif expected == "source":
                p = object_fields(row["source"], SOURCE_FIELDS, "Kaynak")
                s = SourceProps()
                s.stype = SourceType(p.get("stype", "TEMP"))
                modes = p.get("gas_modes", [])
                if not isinstance(modes, list) or len(modes) != len(set(modes)):
                    raise ValueError("Gaz kanalları tekrarsız liste olmalı.")
                s.gas_modes = {GasMode(m) for m in modes}
                for key in ("range_tiles", "co_range", "co2_range", "h2_range", "power"):
                    setattr(s, key, number(p.get(key, getattr(s, key)), 1, 10 if key == "power" else 80, key, True))
                s.temp_celcius = number(p.get("temp_celcius", 300), 22, 1500, "Sıcaklık")
                for key in ("co_ppm", "co2_ppm", "h2_ppm"):
                    setattr(s, key, number(p.get(key, getattr(s, key)), 0, 100000, key))
                e.source = s
            elif kind == Kind.UAV:
                p = object_fields(row["uav"], ("speed", "route", "route_mode", "carrying_ids", "show_route"), "Drone")
                u = UavProps(x=float(x), y=float(y))
                u.speed = number(p.get("speed", 3), 1, 10, "Hız")
                u.route_mode = RouteMode(p.get("route_mode", "LOOP"))
                route = p.get("route", [])
                if not isinstance(route, list) or len(route) > 500:
                    raise ValueError("Rota en fazla 500 durak içerebilir.")
                u.route = []
                for point in route:
                    if not isinstance(point, list) or len(point) != 2:
                        raise ValueError("Rota noktası [x,y] olmalı.")
                    u.route.append((number(point[0], 0, width-1, "Durak X", True), number(point[1], 0, height-1, "Durak Y", True)))
                if u.route and len(set(u.route)) < 2:
                    raise ValueError("Rota en az iki farklı durak içermeli.")
                u.carrying_ids = p.get("carrying_ids", [])
                if not isinstance(u.carrying_ids, list) or len(u.carrying_ids) > 3:
                    raise ValueError("Yük listesi geçersiz.")
                for cid in u.carrying_ids:
                    number(cid, 1, 10**9, "Yük kimliği", True)
                if len(set(u.carrying_ids)) != len(u.carrying_ids):
                    raise ValueError("Tekrarlanan yük.")
                u.show_route = boolean(p.get("show_route", True), "Rota görünürlüğü")
                e.uav = u
            entities.append(e)
        index = {e.id: e for e in entities}
        for e in entities:
            if e.carried_by is not None:
                parent = index.get(e.carried_by)
                if not parent or not parent.uav or e.id not in parent.uav.carrying_ids or (e.tx, e.ty) != (parent.tx, parent.ty):
                    raise ValueError("Taşıyıcı bağlantısı/konumu geçersiz.")
            if e.uav:
                children = [index.get(cid) for cid in e.uav.carrying_ids]
                if any(c is None or c.carried_by != e.id or c.kind not in (Kind.SENSOR, Kind.SOURCE, Kind.BURNED) for c in children):
                    raise ValueError("Drone yük bağlantısı geçersiz.")
                if any(c.sensor for c in children) and len(children) != 1:
                    raise ValueError("Sensör yalnız taşınabilir.")
        return entities, seed, width, height, lesson
    except (KeyError, TypeError, OverflowError) as exc:
        raise ValueError("Eksik veya bozuk sahne alanı.") from exc


def load_scene(path):
    path = Path(path)
    if path.stat().st_size > 2_000_000:
        raise ValueError("Sahne dosyası 2 MB sınırını aşıyor.")
    data = json.loads(path.read_text(encoding="utf-8"))
    parse_scene(data)
    return data


def save_scene(path, data):
    """Önce doğrula; yarım dosya bırakmadan atomik değiştir."""
    parse_scene(data)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as f:
            temporary = f.name
            json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and Path(temporary).exists():
            Path(temporary).unlink()
