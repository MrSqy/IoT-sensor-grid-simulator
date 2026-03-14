import pygame


def load_icon(path: str):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        return None


def get_scaled_icon(cache: dict, key: str, surf, size: tuple[int, int]):
    if surf is None:
        return None

    k = (key, size[0], size[1])
    if k in cache:
        return cache[k]

    cache[k] = pygame.transform.smoothscale(surf, size)
    return cache[k]

