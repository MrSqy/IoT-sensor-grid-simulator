"""Sonlu rota takibi ve tüm durumlarda yük konumu eşitleme."""
import math
from .models import Kind, RouteMode
from .engine import clamp, route_is_valid, find_entity_by_id, bresenham_tiles


def sync_cargo(entities, drone):
    """Rotasız/duraklatılmış araçta da yük koordinatlarını eşitle."""
    for cid in drone.uav.carrying_ids:
        cargo = find_entity_by_id(entities, cid)
        if cargo:
            cargo.tx, cargo.ty = drone.tx, drone.ty


def update_uavs(entities, dt, map_w, map_h):
    """Geçerli rotada süre kadar ilerle; kapalı yolu aşmadan dur."""
    obstacles = {(e.tx, e.ty) for e in entities if e.kind == Kind.OBSTACLE}
    for e in entities:
        up = e.uav
        if e.kind != Kind.UAV or up is None:
            continue
        up.blocked_reason = ""
        if up.route:
            target = int(clamp(up.route_i, 0, len(up.route) - 1))
            if not route_is_valid(up.route, obstacles, up.route_mode):
                up.blocked_reason = "Rota geçersiz: iki farklı durak ve açık yol gerekli."
            elif any(p in obstacles for p in bresenham_tiles(e.tx, e.ty, *up.route[target])):
                up.blocked_reason = "Sıradaki durağa giden yol kapalı."
            if not up.blocked_reason:
                remaining = max(0, dt) * clamp(up.speed, 1, 10)
                zero_hops = 0
                while remaining > 1e-9:
                    up.route_i = int(clamp(up.route_i, 0, len(up.route) - 1))
                    tx, ty = up.route[up.route_i]
                    dx, dy = tx - up.x, ty - up.y
                    distance = math.hypot(dx, dy)
                    if distance < 1e-9:
                        zero_hops += 1
                        if zero_hops > len(up.route) * 2:
                            up.blocked_reason = "Rotada ilerlenemiyor."
                            break
                        nxt = up.route_i + up.route_dir
                        if up.route_mode == RouteMode.LOOP:
                            nxt %= len(up.route)
                        elif not 0 <= nxt < len(up.route):
                            up.route_dir *= -1
                            nxt = up.route_i + up.route_dir
                        up.route_i = nxt
                        continue
                    zero_hops = 0
                    step = min(remaining, distance)
                    up.x += dx / distance * step
                    up.y += dy / distance * step
                    remaining -= step
        up.x, up.y = clamp(up.x, 0, map_w - 1), clamp(up.y, 0, map_h - 1)
        e.tx, e.ty = int(round(up.x)), int(round(up.y))
        sync_cargo(entities, e)
