import math

from .models import Entity, Kind
from .engine import clamp, find_entity_by_id


def update_uavs(entities: list[Entity], dt: float, map_w: int, map_h: int):
    for u in entities:
        if u.kind != Kind.UAV or u.uav is None:
            continue

        up = u.uav
        if not up.route or len(up.route) < 2:
            continue

        speed = clamp(up.speed, 1.0, 10.0)
        remaining = speed * dt  # tiles to move this frame

        while remaining > 1e-6:
            # Clamp waypoint index
            up.route_i = int(clamp(up.route_i, 0, len(up.route) - 1))
            target_i = up.route_i
            tx, ty = up.route[target_i]

            dx = tx - up.x
            dy = ty - up.y
            d = math.hypot(dx, dy)

            if d < 1e-6:
                # reached this waypoint, choose next
                next_i = target_i + up.route_dir

                if up.route_mode.value == "LOOP":
                    if next_i >= len(up.route):
                        next_i = 0
                    if next_i < 0:
                        next_i = len(up.route) - 1
                    up.route_i = next_i

                else:  # PINGPONG
                    if next_i >= len(up.route) or next_i < 0:
                        up.route_dir *= -1
                        next_i = target_i + up.route_dir
                        next_i = int(clamp(next_i, 0, len(up.route) - 1))
                    up.route_i = next_i

                continue

            step = min(remaining, d)
            up.x += (dx / d) * step
            up.y += (dy / d) * step
            remaining -= step

        # Keep inside map bounds
        up.x = clamp(up.x, 0.0, map_w - 1.0)
        up.y = clamp(up.y, 0.0, map_h - 1.0)

        # Update tile coords for rendering/selection
        u.tx = int(round(up.x))
        u.ty = int(round(up.y))
        u.tx = int(clamp(u.tx, 0, map_w - 1))
        u.ty = int(clamp(u.ty, 0, map_h - 1))

        # Move carried items with UAV
        for cid in up.carrying_ids:
            ce = find_entity_by_id(entities, cid)
            if ce is None:
                continue
            ce.tx = u.tx
            ce.ty = u.ty

