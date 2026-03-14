# iot_sim/geom.py
import math
from typing import List, Tuple

Point = Tuple[float, float]

def order_polygon_points(points: List[Point]) -> List[Point]:
    """Centroid'e göre açı sıralaması (CW/CCW)."""
    if len(points) < 3:
        return points[:]
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    return sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

def polygon_area(points: List[Point]) -> float:
    """Shoelace formula. points ordered olmalı (order_polygon_points ile sırala)."""
    n = len(points)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - y1 * x2
    return abs(s) * 0.5

