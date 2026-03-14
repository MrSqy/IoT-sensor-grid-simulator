from .constants import *
from .engine import clamp


class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.zoom = 1.0

    def clamp_zoom_for_map(self, tile_px: float, map_w: int, map_h: int):
        view_w = SCREEN_W - PANEL_W
        view_h = SCREEN_H

        min_zoom_x = view_w / (tile_px * max(1, map_w))
        min_zoom_y = view_h / (tile_px * max(1, map_h))

        min_zoom = max(min_zoom_x, min_zoom_y, MIN_ZOOM_FLOOR)
        self.zoom = clamp(self.zoom, min_zoom, MAX_ZOOM)

    def zoom_at(self, zoom_factor: float, tile_px: float, map_w: int, map_h: int):
        self.zoom *= zoom_factor
        self.clamp_zoom_for_map(tile_px, map_w, map_h)

    def screen_to_world(self, screen_pos: tuple[int, int], tile_px: float) -> tuple[float, float]:
        sx, sy = screen_pos

        cx = (SCREEN_W - PANEL_W) / 2
        cy = SCREEN_H / 2

        dx = sx - cx
        dy = sy - cy

        wx = dx / (tile_px * self.zoom) + self.x
        wy = dy / (tile_px * self.zoom) + self.y

        return wx, wy

