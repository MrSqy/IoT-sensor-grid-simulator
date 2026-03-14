import pygame

from .constants import SCREEN_W, SCREEN_H, PANEL_W
from .models import Entity, Kind, SourceType, GasMode
from .engine import clamp, find_entity_by_id
from .assets import get_scaled_icon
from .viz import draw_dashed_circle, make_gauss_field_surface
from .camera import Camera


def draw_route_overlay(
    screen,
    cam: Camera,
    tile_px: float,
    route_points: list[tuple[int, int]],
    map_w: int,
    map_h: int,
    panel_x: int,
    line_color: tuple[int, int, int] = (220, 220, 230),
    point_color: tuple[int, int, int] = (240, 240, 240),
    start_color: tuple[int, int, int] = (80, 170, 255),
):
    if not route_points:
        return

    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    pts = []
    for (tx, ty) in route_points:
        sx, sy = world_to_screen(tx + 0.5, ty + 0.5)
        pts.append((sx, sy))

    if len(pts) >= 2:
        pygame.draw.lines(screen, line_color, False, pts, 2)

    for i, p in enumerate(pts):
        if i == 0:
            pygame.draw.circle(screen, start_color, p, 6)
            pygame.draw.circle(screen, (10, 10, 12), p, 6, 2)
        else:
            pygame.draw.circle(screen, point_color, p, 4)


def draw_world(
    screen,
    cam: Camera,
    tile_px: float,
    show_grid: bool,
    entities: list[Entity],
    hover_tx,
    hover_ty,
    selected_entity_idx,
    map_w: int,
    map_h: int,
    icons: dict,
    icon_cache: dict,
    show_effect_global: bool,
    field_cache: dict,
    route_preview: list[tuple[int, int]] | None = None,
    route_preview_invalid: bool = False,
    alarm_bridge=None,
):
    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    tw = max(1, int(tile_px * cam.zoom))
    th = max(1, int(tile_px * cam.zoom))

    tiles_x = int(view_w / (tile_px * cam.zoom)) + 4
    tiles_y = int(view_h / (tile_px * cam.zoom)) + 4

    x0 = clamp(int(cam.x) - tiles_x // 2, 0, map_w - 1)
    x1 = clamp(int(cam.x) + tiles_x // 2, 0, map_w - 1)
    y0 = clamp(int(cam.y) - tiles_y // 2, 0, map_h - 1)
    y1 = clamp(int(cam.y) + tiles_y // 2, 0, map_h - 1)

    # Tiles + grid
    for ty in range(y0, y1 + 1):
        for tx in range(x0, x1 + 1):
            sx, sy = world_to_screen(tx, ty)
            rect = pygame.Rect(sx, sy, tw, th)

            pygame.draw.rect(screen, (24, 24, 28) if (tx + ty) % 2 == 0 else (22, 22, 26), rect)
            if show_grid:
                pygame.draw.rect(screen, (35, 35, 40), rect, 1)

    # Effects (behind entities)
    if show_effect_global:
        for e in entities:
            if not e.show_effect:
                continue

            if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source is not None:
                sp = e.source
                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)

                if sp.stype == SourceType.TEMP:
                    # Sıcaklık: tek turuncu blob
                    radius_px = int(round(sp.range_tiles * tile_px * cam.zoom))
                    if radius_px <= 0:
                        continue
                    alpha = int(clamp(40 + sp.power * 16, 40, 220))
                    blob = make_gauss_field_surface(
                        field_cache,
                        key=("blob", "TEMP", e.id, radius_px, alpha),
                        radius_px=radius_px,
                        rgba=(255, 170, 60, alpha),
                    )
                    if blob:
                        screen.blit(blob, blob.get_rect(center=(cx_s, cy_s)))

                elif sp.stype == SourceType.GAS:
                    if not sp.gas_modes:
                        continue

                    # Her aktif gaz için ayrı blob — kendi rengi, kendi menzili
                    # CO=kırmızı, CO2=yeşil, H2=mavi
                    gas_colors = {
                        GasMode.CO:  (220, 80, 80),
                        GasMode.CO2: (90, 220, 120),
                        GasMode.H2:  (80, 160, 255),
                    }
                    gas_ranges = {
                        GasMode.CO:  sp.co_range,
                        GasMode.CO2: sp.co2_range,
                        GasMode.H2:  sp.h2_range,
                    }

                    for gm in sp.gas_modes:
                        grng = gas_ranges.get(gm, 8)
                        radius_px = int(round(grng * tile_px * cam.zoom))
                        if radius_px <= 0:
                            continue
                        rgb = gas_colors.get(gm, (200, 200, 200))
                        alpha = int(clamp(30 + sp.power * 12, 30, 160))
                        blob = make_gauss_field_surface(
                            field_cache,
                            key=("blob", gm.value, e.id, radius_px, alpha),
                            radius_px=radius_px,
                            rgba=(rgb[0], rgb[1], rgb[2], alpha),
                        )
                        if blob:
                            screen.blit(blob, blob.get_rect(center=(cx_s, cy_s)))

        for e in entities:
            if not e.show_effect:
                continue
            if e.kind == Kind.SENSOR and e.sensor is not None and e.sensor.active:
                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                max_r = max(1, int(e.sensor.range_tiles))
                outer_px = int(round(max_r * tile_px * cam.zoom))

                # Dış menzil çemberi — ince, yarı saydam
                if outer_px > 2:
                    ring = pygame.Surface((outer_px * 2 + 2, outer_px * 2 + 2), pygame.SRCALPHA)
                    pygame.draw.circle(ring, (180, 200, 255, 35), (outer_px + 1, outer_px + 1), outer_px)
                    pygame.draw.circle(ring, (180, 200, 255, 70), (outer_px + 1, outer_px + 1), outer_px, 1)
                    screen.blit(ring, (cx_s - outer_px - 1, cy_s - outer_px - 1))

    # UAV route overlays (per-UAV toggle)
    for ent in entities:
        if ent.kind == Kind.UAV and ent.uav is not None:
            up = ent.uav
            if up.show_route and up.route and len(up.route) >= 1:
                draw_route_overlay(screen, cam, tile_px, up.route, map_w, map_h, SCREEN_W - PANEL_W)

    # Route preview overlay
    if route_preview:
        col = (220, 60, 60) if route_preview_invalid else (220, 220, 230)
        draw_route_overlay(screen, cam, tile_px, route_preview, map_w, map_h, SCREEN_W - PANEL_W, line_color=col)

    # Hover highlight
    if hover_tx is not None and hover_ty is not None:
        hsx, hsy = world_to_screen(hover_tx, hover_ty)
        pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(hsx, hsy, tw, th), 2)

    # Entities
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue

        if not (0 <= e.tx < map_w and 0 <= e.ty < map_h):
            continue

        sx, sy = world_to_screen(e.tx, e.ty)
        r = pygame.Rect(sx, sy, tw, th)

        icon_key = None
        icon_src = None

        if e.kind == Kind.SENSOR:
            icon_key = "sensor"
            icon_src = icons.get("sensor")
        elif e.kind == Kind.OBSTACLE:
            icon_key = "obstacle"
            icon_src = icons.get("obstacle")
        elif e.kind == Kind.SOURCE and e.source:
            if e.source.stype == SourceType.TEMP:
                if e.icon_override == "burned":
                    icon_key = "burned"
                    icon_src = icons.get("burned")
                else:
                    icon_key = "source_temp"
                    icon_src = icons.get("source_temp")
            else:
                icon_key = "source_gas"
                icon_src = icons.get("source_gas")
        elif e.kind == Kind.BURNED and e.source:
            icon_key = "burned"
            icon_src = icons.get("burned")
        elif e.kind == Kind.UAV:
            icon_key = "drone"
            icon_src = icons.get("drone")

        scaled = get_scaled_icon(icon_cache, icon_key or "none", icon_src, (tw, th))

        if scaled is not None:
            screen.blit(scaled, (r.x, r.y))
        else:
            if e.kind == Kind.OBSTACLE:
                pygame.draw.rect(screen, (40, 90, 45), r)
            elif e.kind == Kind.SOURCE:
                pygame.draw.rect(
                    screen,
                    (150, 70, 70) if e.source and e.source.stype == SourceType.TEMP else (150, 120, 70),
                    r,
                )
            elif e.kind == Kind.BURNED:
                pygame.draw.rect(screen, (150, 70, 70), r)
            elif e.kind == Kind.SENSOR:
                pygame.draw.rect(screen, (70, 70, 90) if e.sensor and not e.sensor.active else (60, 120, 170), r)
            elif e.kind == Kind.UAV:
                pygame.draw.rect(screen, (160, 160, 180), r)

        # Draw carried items on UAV
        if e.kind == Kind.UAV and e.uav:
            up = e.uav
            pad = int(0.4 * min(tw, th))
            cs = max(8, int(min(tw, th) * 0.45))

            slots_pos_1 = [(r.centerx, r.y + pad)]
            slots_pos_2 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad)]
            slots_pos_3 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad), (r.centerx, r.bottom - pad)]

            carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
            carried = [c for c in carried if c is not None]

            sensor_carried = [c for c in carried if c.kind == Kind.SENSOR]
            source_carried = [c for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED)]

            nsrc = len(source_carried)
            if nsrc == 1:
                slots_pos = slots_pos_1
            elif nsrc == 2:
                slots_pos = slots_pos_2
            else:
                slots_pos = slots_pos_3

            for idx_s, c in enumerate(source_carried[:3]):
                px, py = slots_pos[idx_s]
                icon_key2 = (
                    "burned"
                    if (c.kind == Kind.BURNED or c.icon_override == "burned")
                    else ("source_temp" if c.source and c.source.stype == SourceType.TEMP else "source_gas")
                )
                icon_src2 = icons.get(icon_key2)
                sc = get_scaled_icon(icon_cache, f"carry_{icon_key2}", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(px, py)))

            if sensor_carried:
                icon_src2 = icons.get("sensor")
                sc = get_scaled_icon(icon_cache, "carry_sensor", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(r.centerx, r.bottom + cs // 3)))

        if selected_entity_idx == i:
            pygame.draw.rect(screen, (240, 240, 240), r, 2)

        # Alarm göstergesi: ALERT durumundaki sensörlere kırmızı çerçeve
        if alarm_bridge is not None and e.kind == Kind.SENSOR:
            if e.id in alarm_bridge.active_alerts:
                alert_r = r.inflate(6, 6)
                pygame.draw.rect(screen, (255, 60, 60), alert_r, 2)

            # Limiter hakkı bitmiş sensörlere sarı yanıp sönen çerçeve
            if e.id in alarm_bridge.limiter_exhausted:
                blink = (pygame.time.get_ticks() // 400) % 2 == 0
                if blink:
                    lim_r = r.inflate(10, 10)
                    pygame.draw.rect(screen, (255, 200, 40), lim_r, 2)