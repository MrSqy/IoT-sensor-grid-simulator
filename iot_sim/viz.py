import math
import pygame

from .constants import FIELD_STEP_PX
from .engine import clamp


def draw_dashed_circle(
    surface: pygame.Surface,
    center: tuple[int, int],
    radius: int,
    color: tuple[int, int, int, int],
    dash_deg: int = 12,
    gap_deg: int = 10,
    width: int = 2,
):
    if radius <= 0:
        return

    cx, cy = center
    step = dash_deg + gap_deg
    for a0 in range(0, 360, step):
        a1 = a0 + dash_deg
        pts = []
        samples = max(4, dash_deg // 2)
        for i in range(samples + 1):
            t = i / samples
            ang = math.radians(a0 + (a1 - a0) * t)
            x = cx + int(round(math.cos(ang) * radius))
            y = cy + int(round(math.sin(ang) * radius))
            pts.append((x, y))
        if len(pts) >= 2:
            pygame.draw.lines(surface, color, False, pts, width)


def make_gauss_field_surface(cache: dict, key: tuple, radius_px: int, rgba: tuple[int, int, int, int]):
    if radius_px <= 0:
        return None
    if key in cache:
        return cache[key]

    size = radius_px * 2 + 1
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = cy = radius_px

    max_a = rgba[3]
    r_col, g_col, b_col, _ = rgba

    sigma = radius_px / 2.2
    if sigma < 1:
        sigma = 1.0

    for r in range(radius_px, 0, -FIELD_STEP_PX):
        a = int(max_a * math.exp(- (r * r) / (2.0 * sigma * sigma)))
        if a <= 0:
            continue
        pygame.draw.circle(surf, (r_col, g_col, b_col, a), (cx, cy), r)

    core_a = min(255, max_a)
    pygame.draw.circle(surf, (r_col, g_col, b_col, core_a), (cx, cy), max(1, radius_px // 10))

    cache[key] = surf
    return surf

