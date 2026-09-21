"""Pencere boyutunu aşmayan, ortak anahtarlı ve sınırlı görsel önbellek."""
from collections import OrderedDict
import pygame


class EffectCache:
    def __init__(self, limit_bytes=16*1024*1024):
        self.limit = limit_bytes
        self.bytes = 0
        self.items = OrderedDict()

    def get(self, key, factory):
        if key in self.items:
            self.items.move_to_end(key)
            return self.items[key]
        surface = factory()
        size = surface.get_pitch() * surface.get_height()
        if size <= self.limit:
            while self.items and self.bytes + size > self.limit:
                _, old = self.items.popitem(last=False)
                self.bytes -= old.get_pitch() * old.get_height()
            self.items[key] = surface
            self.bytes += size
        return surface


def field_overlay(cache, size, sources):
    """Görünür alanda çiz; menzil büyüse de tam dünya boyutunda yüzey üretme."""
    surface = pygame.Surface(size, pygame.SRCALPHA)
    for cx, cy, radius, color, alpha in sources:
        # Yalnız pencere boyutundaki hedefe çizim; dev ara sprite yok.
        for fraction in (1, .8, .6, .4, .2):
            pygame.draw.circle(surface, (*color, int(alpha*(1-fraction*.7))),
                               (cx, cy), max(1, round(radius*fraction)))
    return surface
