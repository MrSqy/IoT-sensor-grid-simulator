import math
import random
from .models import *
from .constants import *
from .constants import ACCURACY_BY_DIST
from .models import Entity

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def accuracy_for_dist(d: int) -> int:
    if d < 0:
        return 0
    if d < len(ACCURACY_BY_DIST):
        return ACCURACY_BY_DIST[d]
    return 0

def tile_occupied(entities: list[Entity], tx: int, ty: int) -> bool:
    for e in entities:
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return True
    return False

def find_entity_at(entities: list[Entity], tx: int, ty: int):
    # Prefer non-carried things for selection
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return i
    return None

def find_entity_by_id(entities: list[Entity], eid: int):
    for e in entities:
        if e.id == eid:
            return e
    return None

def build_entity_index(entities: list[Entity]) -> dict[int, Entity]:
    """O(1) lookup için entity id -> Entity dict'i oluşturur."""
    return {e.id: e for e in entities}

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# Bresenham line over tiles (inclusive)
def bresenham_tiles(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def route_is_valid(route_points, obstacle_tiles, mode=RouteMode.LOOP, start=None) -> bool:
    """Başlangıç, tüm parçalar ve LOOP dönüşünü kapsayan rota kontrolü."""
    if len(set(route_points)) < 2:
        return False
    points = list(route_points)
    if mode == RouteMode.LOOP:
        points.append(points[0])
    if start is not None:
        points.insert(0, tuple(int(round(v)) for v in start))
    return all(not any(p in obstacle_tiles for p in bresenham_tiles(*a, *b))
               for a, b in zip(points, points[1:]))
