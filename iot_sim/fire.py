import math
import random

from .models import Entity, Kind, SourceProps, SourceType


def spread_fire(entities: list[Entity]):
    """Every call (expected every 2s), some obstacles may ignite into TEMP sources."""
    temp_sources = [
        e for e in entities
        if e.kind in (Kind.SOURCE, Kind.BURNED)
        and e.source is not None
        and e.source.stype == SourceType.TEMP
    ]
    if not temp_sources:
        return

    obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
    if not obstacles:
        return

    for tree in obstacles:
        best_d = None

        for src in temp_sources:
            sp = src.source
            if sp is None:
                continue

            d = math.hypot(tree.tx - src.tx, tree.ty - src.ty)
            if d <= max(1, int(sp.range_tiles)):
                if best_d is None or d < best_d:
                    best_d = d

        if best_d is None or best_d <= 0:
            continue

        n = max(1.0, float(best_d))
        p = 1.0 / (n * n)

        if random.random() < p:
            # convert this obstacle into a burned TEMP source
            tree.kind = Kind.SOURCE
            tree.source = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=6)
            tree.icon_override = "burned"

