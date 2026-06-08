from .models import Entity, Kind
from .engine import find_entity_by_id


def can_attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if uav.kind != Kind.UAV or uav.uav is None:
        return False
    if candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED):
        return False
    if candidate.carried_by is not None:
        return False

    up = uav.uav
    carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
    carried = [c for c in carried if c is not None]

    have_sensor = any(c.kind == Kind.SENSOR for c in carried)
    have_source = any(c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried)

    if candidate.kind == Kind.SENSOR:
        if have_source:
            return False
        if have_sensor:
            return False
        return True

    if have_sensor:
        return False

    nsrc = sum(1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED))
    return nsrc < 3


def attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if not can_attach_to_uav(entities, uav, candidate):
        return False
    up = uav.uav
    if up is None:
        return False

    up.carrying_ids.append(candidate.id)
    candidate.carried_by = uav.id
    candidate.tx = uav.tx
    candidate.ty = uav.ty
    return True

