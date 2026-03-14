import pygame
from .constants import PANEL_W, PAD


def draw_button(screen, rect, text, font, active=False):
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(
        screen,
        (225, 225, 225) if active else (90, 90, 100),
        rect,
        2 if active else 1,
        border_radius=10,
    )
    label = font.render(text, True, (235, 235, 235))
    screen.blit(label, (rect.x + 12, rect.y + 9))


def draw_small_btn(screen, rect, text, font):
    pygame.draw.rect(screen, (50, 50, 55), rect, border_radius=6)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=6)
    label = font.render(text, True, (240, 240, 240))
    lw, lh = label.get_size()
    screen.blit(label, (rect.centerx - lw // 2, rect.centery - lh // 2))


def draw_switch(screen, rect, on: bool):
    bg = (50, 50, 55)
    border = (120, 120, 130)
    on_col = (120, 210, 150)

    pygame.draw.rect(screen, bg, rect, border_radius=999)
    pygame.draw.rect(screen, border, rect, 1, border_radius=999)

    inner = rect.inflate(-4, -4)
    pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)

    knob_r = inner.height // 2 - 1
    kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
    ky = inner.centery
    pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)


def draw_section_title(screen, x, y, title, font, small):
    screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
    pygame.draw.line(
        screen,
        (45, 45, 55),
        (x, y + 26),
        (x + PANEL_W - 2 * PAD, y + 26),
        1,
    )


def draw_segmented(screen, rect, options: list[str], selected_idx: int, font_small):
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=10)

    n = len(options)
    seg_w = rect.width // n
    seg_rects = []
    for i in range(n):
        r = pygame.Rect(rect.x + i * seg_w, rect.y, seg_w, rect.height)
        seg_rects.append(r)

        if i == selected_idx:
            pygame.draw.rect(screen, (70, 70, 78), r.inflate(-2, -2), border_radius=8)

        txt = font_small.render(options[i], True, (235, 235, 235))
        screen.blit(txt, (r.centerx - txt.get_width() // 2, r.centery - txt.get_height() // 2))

    return seg_rects

