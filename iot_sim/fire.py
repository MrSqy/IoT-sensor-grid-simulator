"""Sıcaklık ve kesintisiz maruz kalma süresine bağlı eğitim modeli."""
from .models import Kind, SourceProps, SourceType
from .sensors import field_at


def spread_fire(entities, dt=2.0):
    """Önce tüm sıcaklıkları hesapla; sonra tutuşanları birlikte dönüştür."""
    burning = []
    for e in entities:
        if e.kind != Kind.OBSTACLE or not e.flammable:
            continue
        temperature = field_at(e.tx, e.ty, entities)["TEMP"]
        e.heat_seconds = e.heat_seconds + dt if temperature >= e.ignition_temp else 0.0
        if e.heat_seconds + 1e-9 >= e.ignition_seconds:
            burning.append(e)
    for e in burning:
        e.kind = Kind.BURNED
        e.source = SourceProps(stype=SourceType.TEMP, temp_celcius=300, range_tiles=6)
        e.icon_override = "burned"
    return burning
