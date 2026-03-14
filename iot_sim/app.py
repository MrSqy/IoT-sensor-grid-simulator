import os
import math
import pygame

from .constants import *
from .models import *
from .camera import Camera
from .engine import clamp, find_entity_at, find_entity_by_id, route_is_valid
from .sensors import simulate_tick
from .uav import update_uavs
from .fire import spread_fire
from .assets import load_icon
from .panel import build_panel_layout, draw_panel
from .render import draw_world
from .cargo import attach_to_uav
from .exporter import Exporter
from .alarm_bridge import AlarmBridge


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("IoT Grid Sim")
    clock = pygame.time.Clock()
    exporter = Exporter(out_dir="exports")

    font = pygame.font.SysFont("DejaVu Sans", 18)
    small = pygame.font.SysFont("DejaVu Sans", 14)

    # --------- state ----------
    exporter = Exporter(out_dir="exports")
    alarm_bridge = AlarmBridge(rate_limit=40)
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

    # UAV panel focus for carried item editing
    uav_focus_cargo_id: int | None = None
    collapsed_cargo_ids: set[int] = set()

    sim_running = False
    sim_time = 0.0
    tick_accum = 0.0
    spread_accum = 0.0

    panel_x = SCREEN_W - PANEL_W
    panel_scroll = 0
    last_selected_entity_id = None

    # route edit state
    route_editing = False
    route_edit_points: list[tuple[int, int]] = []
    route_backup: list[tuple[int, int]] = []
    route_edit_uav_id: int | None = None
    route_preview_invalid = False

    # drag state
    left_down = False
    dragging_entity_idx: int | None = None
    dragging_active = False
    dragging_start = (0, 0)

    # move mode state (M tuşu)
    move_mode = False

    # text input state (isim değiştirme)
    text_input_active = False
    text_input_buffer = ""
    text_input_entity_id: int | None = None

    # log view state
    show_log_view = False

    # UI toast
    ui_msg_text = ""
    ui_msg_timer = 0.0

    def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs

    # assets
    icons = {
        "sensor": load_icon(os.path.join("assets", "sensor.png")),
        "source_temp": load_icon(os.path.join("assets", "source_temp.png")),
        "source_gas": load_icon(os.path.join("assets", "source_gas.png")),
        "obstacle": load_icon(os.path.join("assets", "obstacle.png")),
        "burned": load_icon(os.path.join("assets", "burned.png")),
        "drone": load_icon(os.path.join("assets", "drone.png")),
    }
    icon_cache: dict = {}
    field_cache: dict = {}

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        mx, my = pygame.mouse.get_pos()

        # timers
        if ui_msg_timer > 0:
            ui_msg_timer = max(0.0, ui_msg_timer - dt)

        # hover tile
        hover_tx = hover_ty = None
        if mx < panel_x:
            wx, wy = cam.screen_to_world((mx, my), tile_px)
            ht = int(math.floor(wx + 1e-6))
            hy = int(math.floor(wy + 1e-6))
            if 0 <= ht < MAP_W and 0 <= hy < MAP_H:
                hover_tx, hover_ty = ht, hy

        # sim updates
        if sim_running:
            update_uavs(entities, dt, MAP_W, MAP_H)

            tick_accum += dt
            while tick_accum >= TICK_SECONDS:
                tick_accum -= TICK_SECONDS
                sim_time += TICK_SECONDS

                simulate_tick(entities, TICK_SECONDS)

                # CALCULATOR alarm değerlendirmesi
                alarm_bridge.update(entities, sim_time)

                # sensör ölçümlerini logla
                for ent in entities:
                    if ent.kind == Kind.SENSOR and ent.sensor is not None and ent.carried_by is None:
                        exporter.log_sensor(sim_time, ent)

                # alarm olaylarını logla
                for eid, alerts in alarm_bridge.active_alerts.items():
                    for ent in entities:
                        if ent.id == eid:
                            exporter.log_alarm(sim_time, ent, "ALERT", " | ".join(alerts))
                            break

                spread_accum += TICK_SECONDS
                while spread_accum >= 2.0:
                    spread_accum -= 2.0
                    spread_fire(entities)

        # build panel layout
        tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom = build_panel_layout(
            entities, selected_tool, selected_entity_idx, panel_x,
            small, font, show_effect_global, uav_focus_cargo_id, collapsed_cargo_ids,
            alarm_bridge=alarm_bridge, show_log_view=show_log_view
        )

        # wire global switch callback (panel.py puts placeholder None)
        for idx, (r, action) in enumerate(panel_clickables):
            if r == global_sw_rect:
                def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
                panel_clickables[idx] = (r, _toggle_global)
                break

        # reset scroll / focus when selection changes
        cur_sel_id = entities[selected_entity_idx].id if (selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities)) else None
        if cur_sel_id != last_selected_entity_id:
            panel_scroll = 0
            uav_focus_cargo_id = None
            last_selected_entity_id = cur_sel_id

        # cargo slots for drop detection
        cargo_slots: list[pygame.Rect] = []
        for row in entity_rows:
            if row[0] == "cargo_slots":
                cargo_slots = row[1]
                break

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Text input aktifken tüm tuşları yakala
                if text_input_active:
                    if event.key == pygame.K_RETURN:
                        # Kaydet
                        if text_input_entity_id is not None:
                            for ent in entities:
                                if ent.id == text_input_entity_id:
                                    ent.name = text_input_buffer.strip()
                                    push_msg(f"İsim güncellendi: {ent.display_name}")
                                    break
                        text_input_active = False
                        text_input_buffer = ""
                        text_input_entity_id = None
                    elif event.key == pygame.K_ESCAPE:
                        text_input_active = False
                        text_input_buffer = ""
                        text_input_entity_id = None
                        push_msg("İsim değiştirme iptal edildi.")
                    elif event.key == pygame.K_BACKSPACE:
                        text_input_buffer = text_input_buffer[:-1]
                    else:
                        if event.unicode and len(text_input_buffer) < 30:
                            text_input_buffer += event.unicode
                    continue

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
                    move_mode = False
                    text_input_active = False
                    text_input_buffer = ""
                    text_input_entity_id = None

                elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        dying = entities[selected_entity_idx]

                        # deleting a carried entity -> unlink
                        if dying.carried_by is not None:
                            parent = find_entity_by_id(entities, dying.carried_by)
                            if parent and parent.kind == Kind.UAV and parent.uav:
                                if dying.id in parent.uav.carrying_ids:
                                    parent.uav.carrying_ids.remove(dying.id)
                            dying.carried_by = None

                        # deleting UAV -> detach cargo
                        if dying.kind == Kind.UAV and dying.uav:
                            for cid in list(dying.uav.carrying_ids):
                                ce = find_entity_by_id(entities, cid)
                                if ce:
                                    ce.carried_by = None
                            dying.uav.carrying_ids.clear()

                        entities.pop(selected_entity_idx)
                        selected_entity_idx = None

                elif event.key == pygame.K_k:
                    # UAV route edit toggle
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        e = entities[selected_entity_idx]
                        if e.kind == Kind.UAV and e.uav is not None:
                            if not route_editing:
                                route_editing = True
                                route_edit_points = []
                                route_preview_invalid = False
                                route_backup = list(e.uav.route)
                                route_edit_uav_id = e.id
                            else:
                                if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and (not route_preview_invalid):
                                    e.uav.route = list(route_edit_points)
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
                            if route_editing:
                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None

                elif event.key == pygame.K_m:
                    # Nesne taşıma modu toggle
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        e = entities[selected_entity_idx]
                        if e.carried_by is None:
                            move_mode = not move_mode
                            if move_mode:
                                push_msg(f"{e.kind.value} #{e.id} taşınıyor — haritada tıkla yerleştir | M/ESC: İptal")
                            else:
                                push_msg("Taşıma iptal edildi.")
                    else:
                        move_mode = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # wheel
                if event.button in (4, 5):
                    if mx >= panel_x:
                        # FULL panel scroll (seçili olmasa bile)
                        scroll_step = 50
                        if event.button == 4:
                            panel_scroll = max(0, panel_scroll - scroll_step)
                        else:
                            max_scroll = max(0, panel_content_bottom - SCREEN_H + 20)
                            panel_scroll = min(max_scroll, panel_scroll + scroll_step)
                    else:
                        mods = pygame.key.get_mods()
                        ctrl = (mods & pygame.KMOD_CTRL) != 0
                        shift = (mods & pygame.KMOD_SHIFT) != 0

                        if ctrl:
                            # zoom
                            if event.button == 4:
                                cam.zoom_at(1.12, tile_px, MAP_W, MAP_H)
                            else:
                                cam.zoom_at(1 / 1.12, tile_px, MAP_W, MAP_H)
                            icon_cache.clear()
                            field_cache.clear()
                        else:
                            # pan
                            pan_tiles = 6.0 / max(0.2, cam.zoom)
                            if shift:
                                cam.x += (-pan_tiles if event.button == 4 else pan_tiles)
                            else:
                                cam.y += (-pan_tiles if event.button == 4 else pan_tiles)

                            cam.x = clamp(cam.x, 0.0, MAP_W - 1.0)
                            cam.y = clamp(cam.y, 0.0, MAP_H - 1.0)

                elif event.button == 1:
                    left_down = True

                    # potential entity drag start (only map)
                    if mx < panel_x and hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        dragging_entity_idx = idx
                        dragging_start = (mx, my)
                        dragging_active = False

                elif event.button == 3 and mx < panel_x:
                    # right click delete on map
                    if hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        if idx is not None:
                            entities.pop(idx)
                            if selected_entity_idx == idx:
                                selected_entity_idx = None
                            elif selected_entity_idx is not None and selected_entity_idx > idx:
                                selected_entity_idx -= 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and left_down:
                    # drop dragged entity to UAV cargo slots
                    if dragging_entity_idx is not None and dragging_active:
                        if mx >= panel_x and cargo_slots and selected_entity_idx is not None:
                            uav_ent = entities[selected_entity_idx]
                            cand = entities[dragging_entity_idx]
                            # slots are panel-space; panel scroll affects hit test
                            if any(r.move(0, -panel_scroll).collidepoint(mx, my) for r in cargo_slots):
                                if uav_ent.kind == Kind.UAV:
                                    attach_to_uav(entities, uav_ent, cand)

                    else:
                        # Log butonu tıklama kontrolü (harita üstü top-bar)
                        log_btn_w, log_btn_h = 90, 30
                        _log_btn = pygame.Rect(panel_x - log_btn_w - 12, 8, log_btn_w, log_btn_h)
                        if _log_btn.collidepoint(mx, my):
                            show_log_view = not show_log_view
                            panel_scroll = 0
                            left_down = False
                            dragging_entity_idx = None
                            dragging_active = False
                            continue

                        # click (panel vs map)
                        if mx >= panel_x:
                            clicked = False

                            # tool buttons (scroll applies to ALL panel now)
                            for k, r, _label in tool_buttons:
                                rr = r.move(0, -panel_scroll)
                                if rr.collidepoint(mx, my):
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

                            # panel clickables (scroll applies to ALL)
                            for r, action in panel_clickables:
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
                                        elif action[0] == "start_rename":
                                            text_input_active = True
                                            text_input_entity_id = action[1]
                                            for ent in entities:
                                                if ent.id == action[1]:
                                                    text_input_buffer = ent.name
                                                    break
                                        elif action[0] == "toggle_log_view":
                                            show_log_view = not show_log_view
                                            panel_scroll = 0
                                    clicked = True
                                    break

                            # segmented control (source type) (scroll applies)
                            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                e = entities[selected_entity_idx]
                                if e.kind == Kind.SOURCE and e.source:
                                    for row in entity_rows:
                                        if row[0] == "segmented":
                                            seg_rect = row[1].move(0, -panel_scroll)
                                            if seg_rect.collidepoint(mx, my):
                                                half = seg_rect.width // 2
                                                e.source.stype = SourceType.TEMP if mx < seg_rect.x + half else SourceType.GAS
                                            break

                        else:
                            # map click
                            if hover_tx is not None:
                                tx, ty = hover_tx, hover_ty

                                if move_mode and selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                    # Nesne taşıma: seçili entity'yi tıklanan tile'a taşı
                                    e = entities[selected_entity_idx]
                                    e.tx = tx
                                    e.ty = ty
                                    if e.kind == Kind.UAV and e.uav:
                                        e.uav.x = float(tx)
                                        e.uav.y = float(ty)
                                    move_mode = False
                                    push_msg(f"{e.kind.value} #{e.id} taşındı → ({tx}, {ty})")

                                elif route_editing:
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
                                                entities.append(Entity(id=next_id, kind=Kind.BURNED, tx=tx, ty=ty, source=bp, icon_override="burned"))
                                                next_id += 1
                                    else:
                                        selected_entity_idx = find_entity_at(entities, tx, ty)

                    left_down = False
                    dragging_entity_idx = None
                    dragging_active = False

            elif event.type == pygame.MOUSEMOTION:
                if left_down:
                    # drag detect (entity -> UAV cargo)
                    if dragging_entity_idx is not None and not dragging_active:
                        if abs(mx - dragging_start[0]) >= DRAG_THRESHOLD_PX or abs(my - dragging_start[1]) >= DRAG_THRESHOLD_PX:
                            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                if uav_ent.kind == Kind.UAV and cand is not None and cand.kind in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED) and cand.carried_by is None:
                                    dragging_active = True

        # draw
        screen.fill((18, 18, 22))
        draw_world(
            screen, cam, tile_px, show_grid,
            entities, hover_tx, hover_ty, selected_entity_idx,
            MAP_W, MAP_H, icons, icon_cache,
            show_effect_global, field_cache,
            route_preview=(route_edit_points if route_editing else None),
            route_preview_invalid=route_preview_invalid,
            alarm_bridge=alarm_bridge
        )

        # route edit banner + toast
        if route_editing:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((0, 0, 0, 120))
            screen.blit(banner, (0, 0))
            msg = "ROTA DÜZENLEME: Haritaya tıkla waypoint ekle | K: Bitir/İptal"
            screen.blit(small.render(msg, True, (245, 245, 245)), (12, 9))

        elif move_mode:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((40, 0, 80, 140))
            screen.blit(banner, (0, 0))
            sel_label = ""
            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                e = entities[selected_entity_idx]
                sel_label = f" ({e.kind.value} #{e.id})"
            msg = f"TAŞIMA MODU{sel_label}: Haritaya tıkla yerleştir | M/ESC: İptal"
            screen.blit(small.render(msg, True, (220, 180, 255)), (12, 9))

        elif text_input_active:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((0, 40, 80, 160))
            screen.blit(banner, (0, 0))
            cursor = "|" if int(pygame.time.get_ticks() / 500) % 2 == 0 else " "
            msg = f"İSİM: {text_input_buffer}{cursor}   (Enter: Kaydet | ESC: İptal)"
            screen.blit(small.render(msg, True, (180, 220, 255)), (12, 9))

        if ui_msg_timer > 0.0 and ui_msg_text:
            y_off = 38 if (route_editing or move_mode or text_input_active) else 8
            box_w = min(720, SCREEN_W - PANEL_W - 24)
            box = pygame.Surface((box_w, 30), pygame.SRCALPHA)
            box.fill((0, 0, 0, 160))
            screen.blit(box, (12, y_off))
            screen.blit(small.render(ui_msg_text, True, (245, 245, 245)), (20, y_off + 8))

        # Top-bar Log butonu (harita alanının sağ üstü)
        log_btn_w, log_btn_h = 90, 30
        log_btn_rect = pygame.Rect(panel_x - log_btn_w - 12, 8, log_btn_w, log_btn_h)
        if show_log_view:
            pygame.draw.rect(screen, (80, 50, 120), log_btn_rect, border_radius=8)
            pygame.draw.rect(screen, (180, 140, 255), log_btn_rect, 2, border_radius=8)
            lbl = small.render("< Geri", True, (220, 200, 255))
        else:
            pygame.draw.rect(screen, (40, 40, 50, 200), log_btn_rect, border_radius=8)
            pygame.draw.rect(screen, (120, 120, 140), log_btn_rect, 1, border_radius=8)
            lbl = small.render("Log", True, (220, 220, 230))
        screen.blit(lbl, (log_btn_rect.centerx - lbl.get_width() // 2, log_btn_rect.centery - lbl.get_height() // 2))

        # sol alt talimatlar + stats
        stats = f"Map: {MAP_W}x{MAP_H} | Zoom: {cam.zoom:.2f} | Entities: {len(entities)}"
        screen.blit(small.render(stats, True, (180, 180, 180)), (20, SCREEN_H - 26))

        hint_lines = [
            "Sol tık: Seç / (Araç seçiliyken) Ekle | Sağ tık: Sil | DEL/BKSP: Seçiliyi sil",
            "Wheel: Haritayı kaydır | Shift+Wheel: Yatay | Ctrl+Wheel: Zoom",
            "G: Izgara | Space: Sim (RUN/PAUSE) | M: Seçili nesneyi taşı",
            "İHA seçiliyken: K rota edit (tıkla waypoint ekle, K ile bitir)",
            "Kaynak/Sensör: Haritadan sürükle -> İHA panelindeki slotlara bırak",
        ]
        hint_y0 = SCREEN_H - 26 - 8 - 18 * len(hint_lines)
        for i, line in enumerate(hint_lines):
            screen.blit(small.render(line, True, (170, 170, 170)), (20, hint_y0 + 18 * i))

        # panel
        draw_panel(
            screen=screen,
            panel_x=panel_x,
            font=font,
            small=small,
            tool_buttons=tool_buttons,
            global_rows=global_rows,
            entity_rows=entity_rows,
            selected_tool=selected_tool,
            selected_entity=selected_entity,
            panel_scroll=panel_scroll,
            sim_running=sim_running,
            sim_time=sim_time,
            alarm_bridge=alarm_bridge,
            show_log_view=show_log_view,
        )

        pygame.display.flip()
    csv_path, poly_path, alarm_path = exporter.close()
    print("Export:", csv_path, poly_path, alarm_path)
    

    pygame.quit()


if __name__ == "__main__":
    main()