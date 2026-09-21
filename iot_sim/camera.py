"""Boyutu değişen görünümde dünya/ekran koordinat dönüşümü."""
import pygame
from .engine import clamp


class Camera:
    def __init__(self):
        self.x, self.y, self.zoom = 12.0, 12.0, 1.4
        self.viewport = pygame.Rect(0, 100, 800, 600)

    def world_to_screen(self, x, y, tile_px=24):
        return (round(self.viewport.centerx + (x-self.x)*tile_px*self.zoom),
                round(self.viewport.centery + (y-self.y)*tile_px*self.zoom))

    def screen_to_world(self, pos, tile_px=24):
        return ((pos[0]-self.viewport.centerx)/(tile_px*self.zoom)+self.x,
                (pos[1]-self.viewport.centery)/(tile_px*self.zoom)+self.y)

    def zoom_at(self, factor, tile_px=24, map_w=200, map_h=200):
        self.zoom = clamp(self.zoom * factor, .35, 3.5)

    def clamp_zoom_for_map(self, tile_px, map_w, map_h):
        self.zoom = clamp(self.zoom, .35, 3.5)
