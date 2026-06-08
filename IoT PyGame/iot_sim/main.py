import math
import os
import random
import pygame
from dataclasses import dataclass, field
from enum import Enum

# =============================
# CONFIG
# =============================
SCREEN_W, SCREEN_H = 1200, 800
PANEL_W = 320
FPS = 60

DEFAULT_TILE = 16
MAX_ZOOM = 4.0
MIN_ZOOM_FLOOR = 0.15

TICK_SECONDS = 1.0

# Accuracy drops with distance (0..7). 8+ => no measurement.
ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55]  # d=0..6, d=7 uses last

# Left-drag pan
PAN_SPEED = 1.0
PAN_DRAG_THRESHOLD_PX = 4  # treat as drag after moving this much

# Visualization
FIELD_STEP_PX = 6  # lower = smoother, higher = faster

# Panel layout
PAD = 20
SECTION_GAP = 18

# Panel layout (y positions)
PANEL_Y_APPEAR = 370
PANEL_Y_GLOBAL_SWITCH = 406
PANEL_Y_SELECTED_TITLE = 450
PANEL_Y_SELECTED_LABEL = 490
PANEL_SCROLL_Y0 = 520

# Drag & drop
DRAG_THRESHOLD_PX = 6

# =============================
# DOMAIN
# =============================
class Kind(str, Enum):
    SENSOR = "SENSOR"
    SOURCE = "SOURCE"
    OBSTACLE = "OBSTACLE"
    BURNED = "BURNED"
    UAV = "UAV"


class SourceType(str, Enum):
    TEMP = "TEMP"
    GAS = "GAS"


class RouteMode(str, Enum):
    LOOP = "LOOP"
    PINGPONG = "PINGPONG"


@dataclass
class SensorProps:
    range_tiles: int = 6
    efficiency: int = 80
    battery: float = 5000.0
    active: bool = True
    last_temp: float = 0.0
    last_gas: float = 0.0


@dataclass
class SourceProps:
    stype: SourceType = SourceType.TEMP
    power: int = 5
    range_tiles: int = 8


@dataclass
class UavProps:
    speed: float = 3.0  # tiles/sec (1..10)
    route: list[tuple[int, int]] = field(default_factory=list)
    route_mode: RouteMode = RouteMode.LOOP
    route_dir: int = 1              # +1 or -1 for pingpong
    route_i: int = 0                # current waypoint index
    x: float = 0.0                  # continuous position
    y: float = 0.0
    carrying_ids: list[int] = field(default_factory=list)  # entity ids (sources/sensor)
    show_route: bool = True  # draw route overlay (start point in blue)


@dataclass
class Entity:
    id: int
    kind: Kind
    tx: int
    ty: int
    sensor: SensorProps | None = None
    source: SourceProps | None = None
    uav: UavProps | None = None
    show_effect: bool = True  # per-entity effect visibility
    carried_by: int | None = None  # uav id if being carried
    icon_override: str | None = None  # custom icon key (e.g., 'burned')


# =============================
# HELPERS
# =============================
def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def accuracy_for_dist(d: int) -> int:
    if d >= 8:
        return 0
    if d <= 6:
        return ACCURACY_BY_DIST[d]
    return ACCURACY_BY_DIST[-1]  # d==7


def tile_occupied(entities: list[Entity], tx: int, ty: int) -> bool:
    for e in entities:
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return True
    return False


def find_entity_at(entities: list[Entity], tx: int, ty: int):
    # Prefer non-carried things for selection
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return i
    return None


def find_entity_by_id(entities: list[Entity], eid: int) -> Entity | None:
    for e in entities:
        if e.id == eid:
            return e
    return None


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])



# Bresenham line over tiles (inclusive)
def bresenham_tiles(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def route_is_valid(route_points: list[tuple[int, int]], obstacle_tiles: set[tuple[int, int]]) -> bool:
    """Returns False if any segment intersects an obstacle tile."""
    if len(route_points) < 2:
        return True
    for i in range(1, len(route_points)):
        x0, y0 = route_points[i - 1]
        x1, y1 = route_points[i]
        for (x, y) in bresenham_tiles(x0, y0, x1, y1):
            # allow the starting tile; everything else must be free
            if (x, y) == (x0, y0):
                continue
            if (x, y) in obstacle_tiles:
                return False
    return True


def spread_fire(entities: list["Entity"]):
    """Every call (expected every 2s), some obstacles may ignite into TEMP sources."""
    temp_sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source and e.source.stype == SourceType.TEMP]
    if not temp_sources:
        return

    obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
    if not obstacles:
        return

    for tree in obstacles:
        # nearest temp source that can reach this tree
        best_d = None
        best_src = None
        for src in temp_sources:
            sp = src.source
            if sp is None:
                continue
            d = math.hypot(tree.tx - src.tx, tree.ty - src.ty)
            if d <= max(1, int(sp.range_tiles)):
                if best_d is None or d < best_d:
                    best_d = d
                    best_src = src

        if best_d is None or best_d <= 0:
            continue

        n = max(1.0, float(best_d))
        p = 1.0 / (n * n)

        if random.random() < p:
            # convert this obstacle into a burned TEMP source
            tree.kind = Kind.SOURCE
            tree.source = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=6)
            tree.icon_override = "burned"



# =============================
# CAMERA (NO ROTATE)
# =============================
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


# =============================
# SIMULATION
# =============================
def simulate_tick(entities: list[Entity], dt_seconds: float):
    sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source is not None]

    for e in entities:
        if e.kind != Kind.SENSOR or e.sensor is None:
            continue

        s = e.sensor
        rng = max(1, int(s.range_tiles))
        eff = clamp(int(s.efficiency), 1, 100)

        # Battery drain: n^2 per second, multiplied by inefficiency
        base = rng * rng
        mult = 1.0 + (100 - eff) / 100.0
        drain = base * mult * dt_seconds

        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.battery -= drain
        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.active = True

        temp_val = 0.0
        gas_val = 0.0

        for src_ent in sources:
            sp = src_ent.source
            if sp is None:
                continue

            d = math.hypot(e.tx - src_ent.tx, e.ty - src_ent.ty)
            src_rng = max(1, int(sp.range_tiles))

            # Effective distance from sensor to nearest point of source influence:
            d_eff = max(0.0, d - src_rng)
            if d_eff > rng:
                continue

            d_eff_i = int(math.floor(d_eff + 1e-6))
            acc = accuracy_for_dist(d_eff_i)
            if acc <= 0:
                continue

            power = clamp(int(sp.power), 1, 10)

            att = 1.0 - (d_eff / src_rng)
            if att < 0:
                att = 0.0

            contrib = power * att * (acc / 100.0)

            if sp.stype == SourceType.TEMP:
                temp_val += contrib
            else:
                gas_val += contrib

        s.last_temp = temp_val
        s.last_gas = gas_val


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

                if up.route_mode == RouteMode.LOOP:
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

        # Move carried items with UAV (and effects center becomes UAV center because tx/ty follow)
        for cid in up.carrying_ids:
            ce = find_entity_by_id(entities, cid)
            if ce is None:
                continue
            ce.tx = u.tx
            ce.ty = u.ty


# =============================
# UI drawing
# =============================
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
    # pill
    bg = (50, 50, 55)
    border = (120, 120, 130)
    on_col = (120, 210, 150)
    pygame.draw.rect(screen, bg, rect, border_radius=999)
    pygame.draw.rect(screen, border, rect, 1, border_radius=999)
    inner = rect.inflate(-4, -4)
    pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)

    # knob
    knob_r = inner.height // 2 - 1
    kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
    ky = inner.centery
    pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)


def draw_section_title(screen, x, y, title, font, small):
    screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
    pygame.draw.line(screen, (45, 45, 55), (x, y + 26), (x + PANEL_W - 2 * PAD, y + 26), 1)


def draw_segmented(screen, rect, options: list[str], selected_idx: int, font_small):
    # background
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


# =============================
# PANEL LAYOUT
# =============================
def build_panel_layout(entities, selected_tool, selected_entity_idx, panel_x, small, font,
                       show_effect_global: bool, uav_focus_cargo_id: int | None,
                       collapsed_cargo_ids: set[int]):
    tool_buttons = [
        (Kind.SENSOR, pygame.Rect(panel_x + PAD, 70, PANEL_W - 2 * PAD, 40), "Ekle: IoT Sensör"),
        (Kind.SOURCE, pygame.Rect(panel_x + PAD, 120, PANEL_W - 2 * PAD, 40), "Ekle: Kaynak"),
        (Kind.OBSTACLE, pygame.Rect(panel_x + PAD, 170, PANEL_W - 2 * PAD, 40), "Ekle: Engel (Ağaç)"),
        (Kind.BURNED, pygame.Rect(panel_x + PAD, 220, PANEL_W - 2 * PAD, 40), "Ekle: Burned (Yanık)"),
        (Kind.UAV, pygame.Rect(panel_x + PAD, 270, PANEL_W - 2 * PAD, 40), "Ekle: İHA (Drone)"),
    ]

    clickables: list[tuple[pygame.Rect, callable]] = []
    global_rows = []
    entity_rows = []
    global_sw_rect = None

    # Global switch row
    attr_y = PANEL_Y_GLOBAL_SWITCH
    sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
    global_rows.append(("switch", sw, "Etki yarıçaplarını göster", show_effect_global))
    clickables.append((sw, None))  # placeholder

    if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
        # content bottom for scrolling
        content_bottom = 0
        for row in global_rows:
            if row[0] == "switch":
                content_bottom = max(content_bottom, row[1].bottom)
        return tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom

    e = entities[selected_entity_idx]

    # Per-entity switch
    ent_sw_y = PANEL_SCROLL_Y0
    ent_sw = pygame.Rect(panel_x + PAD, ent_sw_y, 44, 24)
    entity_rows.append(("switch", ent_sw, "Bu nesnenin etkisini göster", e.show_effect))

    def toggle_entity_effect():
        e.show_effect = not e.show_effect

    clickables.append((ent_sw, toggle_entity_effect))

    y = ent_sw_y + 40

    # If this entity is being carried, offer a quick "back to UAV" button
    if e.carried_by is not None:
        back = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", back, f"İHA'ya dön (#{e.carried_by})"))
        clickables.append((back, ("select_entity_id", e.carried_by)))
        y += 42
        entity_rows.append(("text", y, f"Not: Bu nesne İHA #{e.carried_by} üzerinde taşınıyor."))
        y += 22

    def add_numeric_row(label, value_str, dec_fn, inc_fn, step_hint=None):
        nonlocal y
        text_surf = small.render(f"{label}: {value_str}", True, (220, 220, 220))
        h = text_surf.get_height()
        btn_y = y + h + 6
        minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
        plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
        clickables.append((minus, dec_fn))
        clickables.append((plus, inc_fn))
        entity_rows.append(("numeric", y, f"{label}: {value_str}", minus, plus, step_hint))
        y = btn_y + 26 + 12

    if e.kind == Kind.SENSOR and e.sensor:
        s = e.sensor
        entity_rows.append(("text", y, f"Aktif: {'Evet' if s.active else 'Hayır'}"))
        y += 22

        def set_range(d):
            s.range_tiles = clamp(s.range_tiles + d, 1, 50)
            if s.battery > 0:
                s.active = True

        def set_eff(d):
            s.efficiency = clamp(s.efficiency + d, 1, 100)

        def set_batt(d):
            s.battery = max(0.0, s.battery + float(d))
            if s.battery > 0:
                s.active = True

        add_numeric_row("Menzil", str(s.range_tiles),
                        dec_fn=lambda: set_range(-1),
                        inc_fn=lambda: set_range(+1))
        add_numeric_row("Verimlilik", str(s.efficiency),
                        dec_fn=lambda: set_eff(-5),
                        inc_fn=lambda: set_eff(+5),
                        step_hint="(±5)")
        add_numeric_row("Pil", str(int(s.battery)),
                        dec_fn=lambda: set_batt(-250),
                        inc_fn=lambda: set_batt(+250),
                        step_hint="(±250)")

        entity_rows.append(("text", y, f"Son TEMP: {s.last_temp:.2f}"))
        y += 18
        entity_rows.append(("text", y, f"Son GAS : {s.last_gas:.2f}"))

    elif e.kind == Kind.SOURCE and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip:"))
        y += 18

        seg_rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 32)
        # placeholder rects produced in draw step; click handling uses stored rectangles
        entity_rows.append(("segmented", seg_rect, ["TEMP", "GAS"], 0 if src.stype == SourceType.TEMP else 1))
        y += 44

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))


    elif e.kind == Kind.BURNED and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip: TEMP (burned)"))
        y += 22

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))

    elif e.kind == Kind.UAV and e.uav:
        up = e.uav

        entity_rows.append(("text", y, "Rota: K ile düzenle (İHA seçiliyken)"))
        y += 18
        entity_rows.append(("text", y, f"Waypoint sayısı: {len(up.route)}"))
        y += 22

        def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)

        add_numeric_row("Hız (tile/s)", f"{up.speed:.1f}",
                        dec_fn=lambda: set_speed(-0.5),
                        inc_fn=lambda: set_speed(+0.5),
                        step_hint="(±0.5)")

        # route visibility switch
        route_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("switch", route_sw, "Rotayı göster (mavi başlangıç)", up.show_route))

        def toggle_route():
            up.show_route = not up.show_route

        clickables.append((route_sw, toggle_route))
        y += 40

        # route mode switch
        mode_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("mode_switch", mode_sw, "Tersine takip (PingPong)", up.route_mode == RouteMode.PINGPONG))

        def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1

        clickables.append((mode_sw, toggle_mode))
        y += 40

        # Cargo slots (drag-drop)
        entity_rows.append(("text", y, "Taşınanlar (sürükle-bırak):"))
        y += 18

        slot_w = (PANEL_W - 2 * PAD - 10) // 3
        slots = []
        for i in range(3):
            r = pygame.Rect(panel_x + PAD + i * (slot_w + 5), y, slot_w, 42)
            slots.append(r)
        entity_rows.append(("cargo_slots", slots))
        y += 54

        # Clear button
        clr = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", clr, "Taşınanları Temizle"))

        def clear_cargo():
            # detach carried
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()

        clickables.append((clr, clear_cargo))
        y += 42

        # Quick access buttons for carried items (edit without detaching)
        if up.carrying_ids:
            entity_rows.append(("text", y, "Taşınan nesneler (düzenle):"))
            y += 18
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce is None:
                    continue
                rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
                label = f"Düzenle: {ce.kind.value} #{ce.id}"
                entity_rows.append(("carry_edit_btn", rect, label, cid))
                clickables.append((rect, ("uav_focus_cargo", cid)))
                y += 38

        # Focused cargo details (show under UAV props, without changing selection)
        if uav_focus_cargo_id is not None and uav_focus_cargo_id in list(up.carrying_ids):
            ce = find_entity_by_id(entities, uav_focus_cargo_id)
            if ce is not None:
                y += 4
                entity_rows.append(("text", y, f"{ce.kind.value} özellikleri:"))
                tog = pygame.Rect(panel_x + PAD + 170, y - 2, 90, 22)
                is_collapsed = (ce.id in collapsed_cargo_ids)
                entity_rows.append(("cargo_toggle", tog, "KAPAT" if not is_collapsed else "AÇ"))
                def _toggle_cargo(cid=ce.id):
                    if cid in collapsed_cargo_ids:
                        collapsed_cargo_ids.remove(cid)
                    else:
                        collapsed_cargo_ids.add(cid)
                clickables.append((tog, _toggle_cargo))
                y += 26

                if ce.id not in collapsed_cargo_ids:
                    if ce.kind in (Kind.SOURCE, Kind.BURNED) and ce.source:
                        src2 = ce.source
                        entity_rows.append(("text", y, f"Tip: {src2.stype.value}"))
                        y += 18

                        def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)
                        def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

                        add_numeric_row("Güç", str(src2.power),
                                        dec_fn=lambda: set_power2(-1),
                                        inc_fn=lambda: set_power2(+1))
                        add_numeric_row("Menzil", str(src2.range_tiles),
                                        dec_fn=lambda: set_srange2(-1),
                                        inc_fn=lambda: set_srange2(+1))

                    elif ce.kind == Kind.SENSOR and ce.sensor:
                        s2 = ce.sensor
                        def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True
                        def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)

                        add_numeric_row("Menzil", str(s2.range_tiles),
                                        dec_fn=lambda: set_range2(-1),
                                        inc_fn=lambda: set_range2(+1))
                        add_numeric_row("Verimlilik", str(s2.efficiency),
                                        dec_fn=lambda: set_eff2(-5),
                                        inc_fn=lambda: set_eff2(+5),
                                        step_hint="(±5)")

    elif e.kind == Kind.OBSTACLE:
        entity_rows.append(("text", y, "Engel: şimdilik sadece blok objesi."))
        y += 18
        entity_rows.append(("text", y, "Sonraki adım: LOS ile zayıflatma."))

    # content bottom for scrolling (panel absolute coords)
    content_bottom = 0
    for row in global_rows + entity_rows:
        if row[0] in ("switch", "mode_switch"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "text":
            content_bottom = max(content_bottom, row[1] + 28)
        elif row[0] == "numeric":
            content_bottom = max(content_bottom, row[1] + 60)
        elif row[0] in ("button", "carry_edit_btn", "segmented", "cargo_toggle"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "cargo_slots":
            for r in row[1]:
                content_bottom = max(content_bottom, r.bottom)
    return tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom


# =============================
# ASSETS
# =============================
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


# =============================
# VISUALIZATION HELPERS
# =============================
def draw_dashed_circle(surface: pygame.Surface, center: tuple[int, int], radius: int,
                       color: tuple[int, int, int, int], dash_deg: int = 12, gap_deg: int = 10, width: int = 2):
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


# =============================
# WORLD RENDER
# =============================

def draw_route_overlay(screen, cam: Camera, tile_px: float, route_points: list[tuple[int, int]],
                       map_w: int, map_h: int, panel_x: int,
                       line_color: tuple[int, int, int] = (220, 220, 230),
                       point_color: tuple[int, int, int] = (240, 240, 240),
                       start_color: tuple[int, int, int] = (80, 170, 255)):
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


def draw_world(screen, cam: Camera, tile_px: float, show_grid: bool,
               entities: list[Entity], hover_tx, hover_ty, selected_entity_idx: int | None,
               map_w: int, map_h: int, icons: dict, icon_cache: dict,
               show_effect_global: bool, field_cache: dict,
               route_preview: list[tuple[int, int]] | None = None,
               route_preview_invalid: bool = False):

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
                radius_px = int(round(sp.range_tiles * tile_px * cam.zoom))
                if radius_px <= 0:
                    continue

                base_rgb = (255, 170, 60) if sp.stype == SourceType.TEMP else (90, 220, 120)
                alpha = int(clamp(40 + sp.power * 16, 40, 220))

                blob = make_gauss_field_surface(
                    field_cache,
                    key=("blob", sp.stype.value, radius_px, alpha),
                    radius_px=radius_px,
                    rgba=(base_rgb[0], base_rgb[1], base_rgb[2], alpha),
                )
                if blob is None:
                    continue

                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                screen.blit(blob, blob.get_rect(center=(cx_s, cy_s)))

        for e in entities:
            if not e.show_effect:
                continue
            if e.kind == Kind.SENSOR and e.sensor is not None and e.sensor.active:
                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                max_r = max(1, int(e.sensor.range_tiles))
                for r_tiles in range(1, max_r + 1):
                    radius_px = int(round(r_tiles * tile_px * cam.zoom))
                    draw_dashed_circle(screen, (cx_s, cy_s), radius_px, (255, 255, 255, 90))


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
            continue  # carried items are drawn on UAV

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
                    r
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
            # anchor points relative to UAV rect
            pad = int(0.4 * min(tw, th))
            # small icon size
            cs = max(8, int(min(tw, th) * 0.45))
            # positions
            slots_pos = []
            # 1: top center
            slots_pos_1 = [(r.centerx, r.y + pad)]
            # 2: top-left & top-right
            slots_pos_2 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad)]
            # 3: top-left, top-right, bottom-center
            slots_pos_3 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad), (r.centerx, r.bottom - pad)]

            carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
            carried = [c for c in carried if c is not None]

            # If sensor carried, draw under UAV
            sensor_carried = [c for c in carried if c.kind == Kind.SENSOR]
            source_carried = [c for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED)]

            # Draw sources on top
            nsrc = len(source_carried)
            if nsrc == 1:
                slots_pos = slots_pos_1
            elif nsrc == 2:
                slots_pos = slots_pos_2
            elif nsrc >= 3:
                slots_pos = slots_pos_3

            for idx_s, c in enumerate(source_carried[:3]):
                px, py = slots_pos[idx_s]
                icon_key2 = ("burned" if (c.kind == Kind.BURNED or c.icon_override == "burned") else ("source_temp" if c.source and c.source.stype == SourceType.TEMP else "source_gas"))
                icon_src2 = icons.get(icon_key2)
                sc = get_scaled_icon(icon_cache, f"carry_{icon_key2}", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(px, py)))

            # Draw sensor under UAV (center bottom)
            if sensor_carried:
                c = sensor_carried[0]
                icon_src2 = icons.get("sensor")
                sc = get_scaled_icon(icon_cache, "carry_sensor", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(r.centerx, r.bottom + cs // 3)))

        if selected_entity_idx == i:
            pygame.draw.rect(screen, (240, 240, 240), r, 2)


# =============================
# CARGO RULES
# =============================
def can_attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if uav.kind != Kind.UAV or uav.uav is None:
        return False
    if candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED):
        return False
    if candidate.carried_by is not None:
        return False

    up = uav.uav
    carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
    carried = [c for c in carried if c is not None]

    have_sensor = any(c.kind == Kind.SENSOR for c in carried)
    have_source = any(c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried)

    if candidate.kind == Kind.SENSOR:
        # Must be empty OR already sensor? (only 1 sensor total)
        if have_source:
            return False
        if have_sensor:
            return False
        return True

    # candidate is SOURCE
    if have_sensor:
        return False
    # max 3 sources
    nsrc = sum(1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED))
    return nsrc < 3


def attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if not can_attach_to_uav(entities, uav, candidate):
        return False
    up = uav.uav
    if up is None:
        return False
    up.carrying_ids.append(candidate.id)
    candidate.carried_by = uav.id
    candidate.tx = uav.tx
    candidate.ty = uav.ty
    return True


# =============================
# MAIN
# =============================
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("IoT Grid Sim (NO ROTATE)")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("DejaVu Sans", 18)
    small = pygame.font.SysFont("DejaVu Sans", 14)

    MAP_W, MAP_H = 200, 200
    tile_px = DEFAULT_TILE

    cam = Camera()
    cam.clamp_zoom_for_map(tile_px, MAP_W, MAP_H)
    cam.x = (MAP_W - 1) / 2
    cam.y = (MAP_H - 1) / 2

    show_grid = True
    show_effect_global = True

    entities: list[Entity] = []
    next_id = 1

    selected_tool: Kind | None = None
    selected_entity_idx: int | None = None

    # Panel: when UAV selected, you can click a carried item to show its details below UAV properties
    uav_focus_cargo_id: int | None = None
    collapsed_cargo_ids: set[int] = set()

    sim_running = False
    sim_time = 0.0
    tick_accum = 0.0
    spread_accum = 0.0

    # Left mouse state (click / drag)
    left_down = False
    left_down_pos = (0, 0)

    # Drag state (entity -> panel slots)
    dragging_entity_idx: int | None = None
    dragging_start = (0, 0)
    dragging_active = False

    # Route edit
    route_editing = False
    route_edit_points: list[tuple[int, int]] = []
    route_backup: list[tuple[int, int]] = []
    route_edit_uav_id: int | None = None
    route_preview_invalid = False

    ui_msg_text = ""
    ui_msg_timer = 0.0

    # Assets (optional)
    icons = {
        "sensor": load_icon(os.path.join("assets", "sensor.png")),
        "source_temp": load_icon(os.path.join("assets", "source_temp.png")),
        "source_gas": load_icon(os.path.join("assets", "source_gas.png")),
        "obstacle": load_icon(os.path.join("assets", "obstacle.png")),
        "burned": load_icon(os.path.join("assets", "burned.png")),
        "drone": load_icon(os.path.join("assets", "drone.png")),  # <= senin istediğin
    }
    icon_cache: dict = {}
    field_cache: dict = {}

    panel_x = SCREEN_W - PANEL_W
    SCROLL_Y0 = PANEL_SCROLL_Y0
    
    panel_scroll = 0
    last_selected_entity_id = None

    def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        mx, my = pygame.mouse.get_pos()

        if ui_msg_timer > 0.0:
            ui_msg_timer = max(0.0, ui_msg_timer - dt)

        # Hover tile
        hover_tx = None
        hover_ty = None
        if mx < panel_x:
            wx, wy = cam.screen_to_world((mx, my), tile_px)
            ht = int(math.floor(wx + 1e-6))
            hy = int(math.floor(wy + 1e-6))
            if 0 <= ht < MAP_W and 0 <= hy < MAP_H:
                hover_tx, hover_ty = ht, hy

        # Per-frame UAV motion (only when sim is running)
        if sim_running:
            update_uavs(entities, dt, MAP_W, MAP_H)

        # Simulation tick
        if sim_running:
            tick_accum += dt
            while tick_accum >= TICK_SECONDS:
                tick_accum -= TICK_SECONDS
                sim_time += TICK_SECONDS
                simulate_tick(entities, TICK_SECONDS)
                spread_accum += TICK_SECONDS
                while spread_accum >= 2.0:
                    spread_accum -= 2.0
                    spread_fire(entities)

        tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom = build_panel_layout(
            entities, selected_tool, selected_entity_idx, panel_x, small, font, show_effect_global, uav_focus_cargo_id, collapsed_cargo_ids
        )

        # Wire global switch callback
        for idx, (r, action) in enumerate(panel_clickables):
            if r == global_sw_rect:
                def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
                panel_clickables[idx] = (r, _toggle_global)
                break

        # Reset panel scroll / UAV cargo focus when selection changes
        cur_sel_id = entities[selected_entity_idx].id if (selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities)) else None
        if cur_sel_id != last_selected_entity_id:
            panel_scroll = 0
            uav_focus_cargo_id = None
            last_selected_entity_id = cur_sel_id
        # Identify cargo slot rects for drop detection
        cargo_slots: list[pygame.Rect] = []
        for row in entity_rows:
            if row[0] == "cargo_slots":
                cargo_slots = row[1]
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    show_grid = not show_grid
                elif event.key == pygame.K_SPACE:
                    sim_running = not sim_running
                elif event.key == pygame.K_ESCAPE:
                    selected_tool = None
                    selected_entity_idx = None
                    route_editing = False
                    route_preview_invalid = False
                    route_edit_points.clear()
                    route_backup = []
                    route_edit_uav_id = None
                elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        # detach cargo if deleting UAV
                        dying = entities[selected_entity_idx]
                        # If deleting a carried entity, unlink it from the UAV cargo list
                        if dying.carried_by is not None:
                            parent = find_entity_by_id(entities, dying.carried_by)
                            if parent and parent.kind == Kind.UAV and parent.uav:
                                if dying.id in parent.uav.carrying_ids:
                                    parent.uav.carrying_ids.remove(dying.id)
                            dying.carried_by = None

                        if dying.kind == Kind.UAV and dying.uav:
                            for cid in list(dying.uav.carrying_ids):
                                ce = find_entity_by_id(entities, cid)
                                if ce:
                                    ce.carried_by = None
                            dying.uav.carrying_ids.clear()
                        entities.pop(selected_entity_idx)
                        selected_entity_idx = None
                elif event.key == pygame.K_k:
                    # UAV route edit toggle (only when UAV selected)
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        e = entities[selected_entity_idx]
                        if e.kind == Kind.UAV and e.uav is not None:
                            if not route_editing:
                                # Enter edit mode: start collecting waypoints
                                route_editing = True
                                route_edit_points = []
                                route_preview_invalid = False
                                route_backup = list(e.uav.route)
                                route_edit_uav_id = e.id
                            else:
                                # Exit edit mode:
                                # - If user provided <2 points, treat as cancel (keep old route)
                                # - Otherwise finalize new route for the same UAV
                                if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and (not route_preview_invalid):
                                    e.uav.route = list(route_edit_points)
                                    if e.uav.route and e.uav.route[0] == e.uav.route[-1]:
                                        e.uav.route_mode = RouteMode.LOOP
                                    else:
                                        e.uav.route_mode = RouteMode.PINGPONG
                                    e.uav.route_i = 0
                                    e.uav.route_dir = 1
                                else:
                                    e.uav.route = list(route_backup)
                                    if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and route_preview_invalid:
                                        push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")

                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None
                        else:
                            # If somehow K is pressed while editing but UAV not selected, just cancel edit mode.
                            if route_editing:
                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Wheel: zoom on world, scroll on panel (when an entity is selected)
                if event.button in (4, 5):
                    # Panel scroll (only when an entity is selected)
                    if mx >= panel_x and selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        scroll_step = 40
                        if event.button == 4:
                            panel_scroll = max(0, panel_scroll - scroll_step)
                        else:
                            scroll_bottom_limit = SCREEN_H - 20
                            max_scroll = max(0, panel_content_bottom - scroll_bottom_limit)
                            panel_scroll = min(max_scroll, panel_scroll + scroll_step)
                    else:
                        mods = pygame.key.get_mods()
                        ctrl = (mods & pygame.KMOD_CTRL) != 0
                        shift = (mods & pygame.KMOD_SHIFT) != 0

                        if ctrl:
                            # Ctrl + Wheel => zoom
                            if event.button == 4:
                                cam.zoom_at(1.12, tile_px, MAP_W, MAP_H)
                            else:
                                cam.zoom_at(1 / 1.12, tile_px, MAP_W, MAP_H)
                            icon_cache.clear()
                            field_cache.clear()
                        else:
                            # Wheel => move map (Shift => horizontal)
                            pan_tiles = 6.0 / max(0.2, cam.zoom)
                            if shift:
                                cam.x += (-pan_tiles if event.button == 4 else pan_tiles)
                            else:
                                cam.y += (-pan_tiles if event.button == 4 else pan_tiles)

                            cam.x = clamp(cam.x, 0.0, MAP_W - 1.0)
                            cam.y = clamp(cam.y, 0.0, MAP_H - 1.0)

                # Left press: start possible drag
                elif event.button == 1:
                    left_down = True
                    left_down_pos = (mx, my)

                    # potential entity drag start (only on map)
                    if mx < panel_x and hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        dragging_entity_idx = idx
                        dragging_start = (mx, my)
                        dragging_active = False

                # Right click: delete entity on hovered tile
                elif event.button == 3 and mx < panel_x:
                    if hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        if idx is not None:
                            entities.pop(idx)
                            if selected_entity_idx == idx:
                                selected_entity_idx = None
                            elif selected_entity_idx is not None and selected_entity_idx > idx:
                                selected_entity_idx -= 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if left_down:
                        # If dragging entity to panel
                        if dragging_entity_idx is not None and dragging_active:
                            if mx >= panel_x and cargo_slots and selected_entity_idx is not None:
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                # drop into any slot rect
                                if any(r.move(0, -panel_scroll).collidepoint(mx, my) for r in cargo_slots):
                                    if uav_ent.kind == Kind.UAV:
                                        attach_to_uav(entities, uav_ent, cand)

                        else:
                            if mx >= panel_x:
                                # Panel click
                                clicked = False

                                for k, r, _ in tool_buttons:
                                    if r.collidepoint(mx, my):
                                        selected_tool = k
                                        selected_entity_idx = None
                                        uav_focus_cargo_id = None
                                        panel_scroll = 0
                                        clicked = True
                                        break
                                if clicked:
                                    left_down = False
                                    dragging_entity_idx = None
                                    dragging_active = False
                                    continue

                                # Panel element clicks (with scroll offset for entity section)
                                for r, action in panel_clickables:
                                    rr = r
                                    if selected_entity_idx is not None and rr.y >= SCROLL_Y0:
                                        rr = r.move(0, -panel_scroll)

                                    if rr.collidepoint(mx, my):
                                        if callable(action):
                                            action()
                                        elif isinstance(action, tuple) and len(action) >= 2:
                                            if action[0] == "select_entity_id":
                                                target_id = action[1]
                                                for ii, ee in enumerate(entities):
                                                    if ee.id == target_id:
                                                        selected_entity_idx = ii
                                                        selected_tool = None
                                                        break
                                            elif action[0] == "uav_focus_cargo":
                                                uav_focus_cargo_id = action[1]
                                        clicked = True
                                        break

                                # Source segmented clicks (handled here)
                                if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                    e = entities[selected_entity_idx]
                                    if e.kind == Kind.SOURCE and e.source:
                                        for row in entity_rows:
                                            if row[0] == "segmented":
                                                seg_rect = row[1]
                                                if selected_entity_idx is not None and seg_rect.y >= SCROLL_Y0:
                                                    seg_rect = seg_rect.move(0, -panel_scroll)
                                                if seg_rect.collidepoint(mx, my):
                                                    # determine segment
                                                    half = seg_rect.width // 2
                                                    if mx < seg_rect.x + half:
                                                        e.source.stype = SourceType.TEMP
                                                    else:
                                                        e.source.stype = SourceType.GAS
                                                    clicked = True
                                                break
                            else:
                                # Map click: place/select or route edit point
                                if hover_tx is not None:
                                    tx, ty = hover_tx, hover_ty

                                    if route_editing:
                                        # add waypoint (avoid obstacles)
                                        obstacles_set = {(o.tx, o.ty) for o in entities if o.kind == Kind.OBSTACLE and o.carried_by is None}
                                        if (tx, ty) in obstacles_set:
                                            push_msg("Engelin üstüne waypoint koyamazsın. Tekrar dene.")
                                        else:
                                            route_edit_points.append((tx, ty))
                                            route_preview_invalid = (not route_is_valid(route_edit_points, obstacles_set))
                                            if route_preview_invalid:
                                                push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")
                                    else:
                                        if selected_tool is not None:
                                            # If you click an existing entity while a tool is selected, just select it.
                                            idx_here = find_entity_at(entities, tx, ty)
                                            if idx_here is not None:
                                                selected_entity_idx = idx_here
                                            else:
                                                if selected_tool == Kind.SENSOR:
                                                    entities.append(Entity(id=next_id, kind=Kind.SENSOR, tx=tx, ty=ty, sensor=SensorProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.SOURCE:
                                                    entities.append(Entity(id=next_id, kind=Kind.SOURCE, tx=tx, ty=ty, source=SourceProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.OBSTACLE:
                                                    entities.append(Entity(id=next_id, kind=Kind.OBSTACLE, tx=tx, ty=ty))
                                                    next_id += 1
                                                elif selected_tool == Kind.UAV:
                                                    up = UavProps(speed=3.0, x=float(tx), y=float(ty))
                                                    entities.append(Entity(id=next_id, kind=Kind.UAV, tx=tx, ty=ty, uav=up))
                                                    next_id += 1
                                                elif selected_tool == Kind.BURNED:
                                                    bp = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=3)
                                                    entities.append(Entity(id=next_id, kind=Kind.BURNED, tx=tx, ty=ty, source=bp, icon_override='burned'))
                                                    next_id += 1

                                        else:
                                            selected_entity_idx = find_entity_at(entities, tx, ty)

                    left_down = False
                    dragging_entity_idx = None
                    dragging_active = False

            elif event.type == pygame.MOUSEMOTION:
                if left_down:
                    # Detect entity drag (only for UAV cargo)
                    if dragging_entity_idx is not None and not dragging_active:
                        if abs(mx - dragging_start[0]) >= DRAG_THRESHOLD_PX or abs(my - dragging_start[1]) >= DRAG_THRESHOLD_PX:
                            # Start drag ONLY if selected is UAV and candidate is draggable
                            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                if uav_ent.kind == Kind.UAV and cand.kind in (Kind.SOURCE, Kind.SENSOR) and cand.carried_by is None:
                                    dragging_active = True

        # =============================
        # DRAW
        # =============================
        screen.fill((18, 18, 22))

        # Route preview points (editing) or show selected UAV route (optional)
        preview = route_edit_points if route_editing else None

        draw_world(
            screen, cam, tile_px, show_grid,
            entities, hover_tx, hover_ty, selected_entity_idx,
            MAP_W, MAP_H, icons, icon_cache,
            show_effect_global, field_cache,
            route_preview=preview,
            route_preview_invalid=route_preview_invalid
        )

        # Route edit banner (top-left of world view)
        if route_editing:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((0, 0, 0, 120))
            screen.blit(banner, (0, 0))
            msg = "ROTA DÜZENLEME MODU: Haritaya tıkla waypoint ekle | K: Bitir/İptal"
            screen.blit(small.render(msg, True, (245, 245, 245)), (12, 9))

        # Toast / warning message (top-left)
        if ui_msg_timer > 0.0 and ui_msg_text:
            y_off = 38 if route_editing else 8
            box_w = min(720, SCREEN_W - PANEL_W - 24)
            box = pygame.Surface((box_w, 30), pygame.SRCALPHA)
            box.fill((0, 0, 0, 160))
            screen.blit(box, (12, y_off))
            screen.blit(small.render(ui_msg_text, True, (245, 245, 245)), (20, y_off + 8))

        # Panel background
        pygame.draw.rect(screen, (14, 14, 16), (panel_x, 0, PANEL_W, SCREEN_H))
        pygame.draw.line(screen, (60, 60, 70), (panel_x, 0), (panel_x, SCREEN_H), 2)

        # Tools
        screen.blit(font.render("Araçlar", True, (240, 240, 240)), (panel_x + PAD, 25))
        for k, r, label in tool_buttons:
            draw_button(screen, r, label, font, active=(selected_tool == k))

        # Sim status
        sim_label = "RUNNING" if sim_running else "PAUSED"
        screen.blit(small.render(f"Sim: {sim_label}  (Space)", True, (220, 220, 220)), (panel_x + PAD, 320))
        screen.blit(small.render(f"Zaman: {sim_time:.0f}s", True, (200, 200, 200)), (panel_x + PAD, 340))

                # Appearance section (global)
        draw_section_title(screen, panel_x + PAD, PANEL_Y_APPEAR, "Görünüm", font, small)
        for row in global_rows:
            if row[0] == "switch":
                _, sw_rect, text, on = row
                draw_switch(screen, sw_rect, on)
                screen.blit(small.render(text, True, (200, 200, 200)), (sw_rect.right + 10, sw_rect.y + 4))

        # Selected section
        draw_section_title(screen, panel_x + PAD, PANEL_Y_SELECTED_TITLE, "Seçili", font, small)

        if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
            screen.blit(small.render("Yok (haritadan bir entity seç)", True, (180, 180, 180)),
                        (panel_x + PAD, PANEL_Y_SELECTED_LABEL))
        else:
            e = entities[selected_entity_idx]
            label = f"{e.kind.value} @ ({e.tx},{e.ty})"
            if e.carried_by is not None:
                label += f"  [İHA #{e.carried_by} üzerinde]"
            screen.blit(small.render(label, True, (210, 210, 210)), (panel_x + PAD, PANEL_Y_SELECTED_LABEL))

            # Entity rows (scrollable)
            seg_rects_live = None

            scroll_clip = pygame.Rect(panel_x, SCROLL_Y0, PANEL_W, SCREEN_H - SCROLL_Y0)
            prev_clip = screen.get_clip()
            screen.set_clip(scroll_clip)

            for row in entity_rows:
                rtype = row[0]

                if rtype == "switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "mode_switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "button":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "carry_edit_btn":
                    _, rect, label_text, _cid = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "cargo_toggle":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "numeric":
                    # ("numeric", y, "Label: value", minus_rect, plus_rect, step_hint)
                    _, y, label_text, minus_rect, plus_rect, step_hint = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    m2 = minus_rect.move(0, -panel_scroll) if minus_rect.y >= SCROLL_Y0 else minus_rect
                    p2 = plus_rect.move(0, -panel_scroll) if plus_rect.y >= SCROLL_Y0 else plus_rect

                    screen.blit(small.render(label_text, True, (210, 210, 210)), (panel_x + PAD, ry))
                    draw_small_btn(screen, m2, "-", small)
                    draw_small_btn(screen, p2, "+", small)
                    if step_hint:
                        screen.blit(small.render(str(step_hint), True, (170, 170, 170)), (p2.right + 8, p2.y + 6))

                elif rtype == "segmented":
                    # ("segmented", rect, options, selected_idx)
                    _, rect, options, current = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_segmented(screen, rr, options, current, small)

                elif rtype == "text":
                    _, y, t = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    screen.blit(small.render(t, True, (180, 180, 180)), (panel_x + PAD, ry))

                elif rtype == "cargo_slots":
                    # ("cargo_slots", [rect, rect, rect])
                    slots = []
                    for r in row[1]:
                        slots.append(r.move(0, -panel_scroll) if r.y >= SCROLL_Y0 else r)

                    for i_slot, r in enumerate(slots):
                        pygame.draw.rect(screen, (55, 55, 55), r, border_radius=8)
                        pygame.draw.rect(screen, (90, 90, 90), r, width=2, border_radius=8)
                        idx_txt = small.render(str(i_slot + 1), True, (120, 120, 120))
                        screen.blit(idx_txt, (r.x + 6, r.y + 6))

                    uav_ent = entities[selected_entity_idx]
                    if uav_ent.uav:
                        for i_slot, cid in enumerate(uav_ent.uav.carrying_ids[:3]):
                            if i_slot >= len(slots):
                                break
                            ce = find_entity_by_id(entities, cid)
                            if ce is None:
                                continue

                            icon_key2 = None
                            if ce.kind == Kind.SENSOR:
                                icon_key2 = "sensor"
                            elif ce.kind in (Kind.SOURCE, Kind.BURNED) and ce.source:
                                if ce.icon_override == "burned":
                                    icon_key2 = "burned"
                                else:
                                    icon_key2 = "source_temp" if ce.source.stype == SourceType.TEMP else "source_gas"

                            icon_src2 = icons.get(icon_key2) if icon_key2 else None
                            sc = get_scaled_icon(icon_cache, f"panel_{icon_key2}", icon_src2, (26, 26))

                            if sc is not None:
                                screen.blit(sc, sc.get_rect(center=slots[i_slot].center))
                            else:
                                letter = "S" if ce.kind == Kind.SENSOR else ("T" if (ce.source and ce.source.stype == SourceType.TEMP) else "G")
                                txt = small.render(letter, True, (235, 235, 235))
                                screen.blit(txt, txt.get_rect(center=slots[i_slot].center))

            screen.set_clip(prev_clip)


        # Drag ghost
        if dragging_entity_idx is not None and dragging_active:
            d = entities[dragging_entity_idx]
            # simple ghost circle
            pygame.draw.circle(screen, (240, 240, 240), (mx, my), 10, 2)

        # Footer
        stats = f"Map: {MAP_W}x{MAP_H} | Zoom: {cam.zoom:.2f} | Entities: {len(entities)}"
        screen.blit(small.render(stats, True, (180, 180, 180)), (20, SCREEN_H - 26))

        hint_lines = [
            "Sol tık: Seç / (Araç seçiliyken) Ekle | Sağ tık: Sil | DEL/BKSP: Seçiliyi sil",
            "Wheel: Haritayı kaydır | Shift+Wheel: Yatay | Ctrl+Wheel: Zoom",
            "G: Izgara | Space: Sim (RUN/PAUSE)",
            "İHA seçiliyken: K rota edit (tıkla waypoint ekle, K ile bitir)",
            "Kaynak/Sensör: Haritadan sürükle -> İHA panelindeki slotlara bırak",
        ]
        hint_y0 = SCREEN_H - 26 - 8 - 18 * len(hint_lines)
        for i, line in enumerate(hint_lines):
            screen.blit(small.render(line, True, (170, 170, 170)), (20, hint_y0 + 18 * i))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
