import pygame

from .constants import *
from .models import Entity, Kind, SourceType, RouteMode, GasMode, SensorMode, GAS_CRITICAL_PPM, TEMP_CRITICAL_C
from .engine import clamp, find_entity_by_id
from .ui_widgets import draw_button, draw_switch, draw_section_title, draw_small_btn, draw_segmented


def build_panel_layout(
    entities,
    selected_tool,
    selected_entity_idx,
    panel_x,
    small,
    font,
    show_effect_global: bool,
    uav_focus_cargo_id: int | None,
    collapsed_cargo_ids: set[int],
    alarm_bridge=None,
    show_log_view=False,
):
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

    # Global switch row
    attr_y = PANEL_Y_GLOBAL_SWITCH
    sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
    global_rows.append(("switch", sw, "Etki yarıçaplarını göster", show_effect_global))
    clickables.append((sw, None))  # placeholder (app.py bağlayacak)

    # Panel alt sınırı
    content_bottom = 360
    for _, rect, _ in tool_buttons:
        content_bottom = max(content_bottom, rect.bottom)
    content_bottom = max(content_bottom, sw.bottom)

    # ── LOG VIEW MODU ──
    if show_log_view:
        y = PANEL_SCROLL_Y0

        # Özet: entity sayıları
        n_sensor = sum(1 for e in entities if e.kind == Kind.SENSOR)
        n_source = sum(1 for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED))
        n_uav    = sum(1 for e in entities if e.kind == Kind.UAV)
        n_obs    = sum(1 for e in entities if e.kind == Kind.OBSTACLE)
        entity_rows.append(("text", y, f"Sensör: {n_sensor}  Kaynak: {n_source}  İHA: {n_uav}  Engel: {n_obs}"))
        y += 24

        # Sensörler listesi
        sensors = [e for e in entities if e.kind == Kind.SENSOR and e.sensor]
        if sensors:
            entity_rows.append(("text", y, "── Sensörler ──"))
            y += 20
            for e in sensors:
                s = e.sensor
                modes_str = ",".join(sorted(m.value for m in s.modes)) if s.modes else "-"
                status = ""
                lim_tag = ""
                if alarm_bridge:
                    st = alarm_bridge.get_sensor_status(e.id)
                    if "ALERT" in st:
                        status = " ⚠"
                    if e.id in alarm_bridge.limiter_exhausted:
                        lim_tag = " ⏳"
                loc = f"({e.tx},{e.ty})"
                carried = f" [İHA #{e.carried_by}]" if e.carried_by else ""
                label = f"{e.display_name}  {loc}{carried}{status}{lim_tag}"
                is_alert = "⚠" in status
                entity_rows.append(("log_line", y, label, is_alert))
                y += 16
                # Ölçümler + limiter (kompakt)
                vals = []
                if SensorMode.TEMP in s.modes and s.last_temp > 0:
                    vals.append(f"T:{s.last_temp:.0f}°C")
                if SensorMode.CO in s.modes and s.last_co > 0:
                    vals.append(f"CO:{s.last_co:.0f}")
                if SensorMode.CO2 in s.modes and s.last_co2 > 0:
                    vals.append(f"CO2:{s.last_co2:.0f}")
                if SensorMode.H2 in s.modes and s.last_h2 > 0:
                    vals.append(f"H2:{s.last_h2:.0f}")
                vals.append(f"L:{s.limit}/{s.max_limit}")
                if vals:
                    entity_rows.append(("log_line", y, "  " + "  ".join(vals), False))
                    y += 14
            y += 6

        # Kaynaklar listesi
        sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source]
        if sources:
            entity_rows.append(("text", y, "── Kaynaklar ──"))
            y += 20
            for e in sources:
                sp = e.source
                loc = f"({e.tx},{e.ty})"
                carried = f" [İHA #{e.carried_by}]" if e.carried_by else ""
                if sp.stype == SourceType.TEMP:
                    detail = f"TEMP {sp.temp_celcius:.0f}°C  r={sp.range_tiles}"
                else:
                    gm = ",".join(sorted(m.value for m in sp.gas_modes)) if sp.gas_modes else "-"
                    detail = f"GAS [{gm}]"
                label = f"{e.display_name}  {loc}{carried}  {detail}"
                entity_rows.append(("log_line", y, label, False))
                y += 16
            y += 6

        # İHA'lar listesi
        uavs = [e for e in entities if e.kind == Kind.UAV and e.uav]
        if uavs:
            entity_rows.append(("text", y, "── İHA'lar ──"))
            y += 20
            for e in uavs:
                up = e.uav
                loc = f"({e.tx},{e.ty})"
                cargo_n = len(up.carrying_ids)
                wp_n = len(up.route)
                label = f"{e.display_name}  {loc}  hız={up.speed:.1f}  wp={wp_n}  yük={cargo_n}"
                entity_rows.append(("log_line", y, label, False))
                y += 16
            y += 6

        # Son olaylar
        if alarm_bridge and alarm_bridge.log_lines:
            entity_rows.append(("text", y, "── Son Olaylar ──"))
            y += 20
            recent = alarm_bridge.log_lines[-20:]
            for line in recent:
                is_alert = "ALERT" in line
                entity_rows.append(("log_line", y, line, is_alert))
                y += 16

        for row in entity_rows:
            if row[0] in ("text", "log_line"):
                content_bottom = max(content_bottom, row[1] + 28)
        content_bottom = max(content_bottom, PANEL_Y_SELECTED_LABEL + 40)
        return tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom

    if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
        # Entity seçili olmasa da log göster
        y = PANEL_SCROLL_Y0
        if alarm_bridge is not None and alarm_bridge.log_lines:
            entity_rows.append(("text", y, "── Olay Logu ──"))
            y += 20
            recent = alarm_bridge.log_lines[-15:]
            for line in recent:
                is_alert = "ALERT" in line
                entity_rows.append(("log_line", y, line, is_alert))
                y += 16

        for row in global_rows + entity_rows:
            if row[0] == "switch":
                content_bottom = max(content_bottom, row[1].bottom)
            elif row[0] in ("text", "log_line"):
                content_bottom = max(content_bottom, row[1] + 28)
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

    # İsim gösterimi ve düzenleme butonu
    display = e.display_name
    entity_rows.append(("text", y, f"İsim: {display}"))
    y += 20
    name_btn = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 28)
    entity_rows.append(("button", name_btn, "İsmi Değiştir"))
    clickables.append((name_btn, ("start_rename", e.id)))
    y += 38

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

        # Sensör modları — çoklu seçim
        entity_rows.append(("text", y, "Ölçüm Modları:"))
        y += 20
        btn_w = (PANEL_W - 2 * PAD - 15) // 4
        for mi, sm in enumerate([SensorMode.TEMP, SensorMode.CO, SensorMode.CO2, SensorMode.H2]):
            bx = panel_x + PAD + mi * (btn_w + 5)
            btn_rect = pygame.Rect(bx, y, btn_w, 28)
            is_on = sm in s.modes

            def _toggle_mode(mode=sm):
                if mode in s.modes:
                    s.modes.discard(mode)
                else:
                    s.modes.add(mode)

            entity_rows.append(("gas_toggle", btn_rect, sm.value, is_on))
            clickables.append((btn_rect, _toggle_mode))
        y += 38

        if not s.modes:
            entity_rows.append(("text", y, "Mod seçilmedi — ölçüm yapılmıyor"))
            y += 20

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

        add_numeric_row("Menzil", str(s.range_tiles), dec_fn=lambda: set_range(-1), inc_fn=lambda: set_range(+1))
        add_numeric_row("Verimlilik", str(s.efficiency), dec_fn=lambda: set_eff(-5), inc_fn=lambda: set_eff(+5), step_hint="(±5)")
        add_numeric_row("Pil", str(int(s.battery)), dec_fn=lambda: set_batt(-250), inc_fn=lambda: set_batt(+250), step_hint="(±250)")

        # Limit / Max Limit
        def set_max_limit(d):
            s.max_limit = clamp(s.max_limit + d, 5, 200)
            s.limit = min(s.limit, s.max_limit)

        def set_limit(d):
            s.limit = clamp(s.limit + d, 0, s.max_limit)

        add_numeric_row("Max Limit", str(s.max_limit),
                        dec_fn=lambda: set_max_limit(-5), inc_fn=lambda: set_max_limit(+5), step_hint="(±5)")
        add_numeric_row("Limit (kalan)", f"{s.limit}/{s.max_limit}",
                        dec_fn=lambda: set_limit(-5), inc_fn=lambda: set_limit(+5), step_hint="(±5)")

        # Ölçüm değerleri — sadece aktif modlar gösterilir
        if SensorMode.TEMP in s.modes:
            t_warn = s.last_temp >= TEMP_CRITICAL_C
            entity_rows.append(("sensor_val", y, f"Sıcaklık: {s.last_temp:.1f} °C", t_warn))
            y += 20

        if SensorMode.CO in s.modes:
            co_warn = s.last_co >= GAS_CRITICAL_PPM[GasMode.CO]
            entity_rows.append(("sensor_val", y, f"CO:  {s.last_co:.1f} ppm  (eşik {GAS_CRITICAL_PPM[GasMode.CO]:.0f})", co_warn))
            y += 18

        if SensorMode.CO2 in s.modes:
            co2_warn = s.last_co2 >= GAS_CRITICAL_PPM[GasMode.CO2]
            entity_rows.append(("sensor_val", y, f"CO2: {s.last_co2:.0f} ppm  (eşik {GAS_CRITICAL_PPM[GasMode.CO2]:.0f})", co2_warn))
            y += 18

        if SensorMode.H2 in s.modes:
            h2_warn = s.last_h2 >= GAS_CRITICAL_PPM[GasMode.H2]
            entity_rows.append(("sensor_val", y, f"H2:  {s.last_h2:.0f} ppm  (eşik {GAS_CRITICAL_PPM[GasMode.H2]:.0f})", h2_warn))
            y += 18

        y += 6

        # Alarm durumu (CALCULATOR entegrasyonu)
        if alarm_bridge is not None:
            status = alarm_bridge.get_sensor_status(e.id)
            if "ALERT" in status:
                entity_rows.append(("alarm_text", y, status))
            else:
                entity_rows.append(("text", y, f"Durum: {status}"))
            y += 22

            lim_info = alarm_bridge.get_limiter_info(e.id)
            if lim_info:
                entity_rows.append(("text", y, lim_info))
                y += 20

            # Limiter hakkı bitmiş uyarısı
            if e.id in alarm_bridge.limiter_exhausted:
                entity_rows.append(("alarm_text", y, "⏳ LİMİTER HAKKI BİTTİ"))
                y += 24

    elif e.kind == Kind.SOURCE and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip:"))
        y += 18
        seg_rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 32)
        entity_rows.append(("segmented", seg_rect, ["TEMP", "GAS"], 0 if src.stype == SourceType.TEMP else 1))
        y += 44

        if src.stype == SourceType.TEMP:
            # Sıcaklık kaynağı: merkez sıcaklık (°C)
            def set_temp_c(d):
                src.temp_celcius = max(50.0, min(1500.0, src.temp_celcius + d))

            add_numeric_row("Sıcaklık (°C)", f"{src.temp_celcius:.0f}",
                            dec_fn=lambda: set_temp_c(-50), inc_fn=lambda: set_temp_c(+50), step_hint="(±50)")

            def set_power(d):
                src.power = clamp(src.power + d, 1, 10)

            def set_srange(d):
                src.range_tiles = clamp(src.range_tiles + d, 1, 80)

            add_numeric_row("Güç", str(src.power), dec_fn=lambda: set_power(-1), inc_fn=lambda: set_power(+1))
            add_numeric_row("Menzil", str(src.range_tiles), dec_fn=lambda: set_srange(-1), inc_fn=lambda: set_srange(+1))

        elif src.stype == SourceType.GAS:
            # Gaz modları — çoklu seçim butonları
            entity_rows.append(("text", y, "Gaz Modları (çoklu seçim):"))
            y += 20

            btn_w = (PANEL_W - 2 * PAD - 10) // 3
            for gi, gm in enumerate([GasMode.CO, GasMode.CO2, GasMode.H2]):
                bx = panel_x + PAD + gi * (btn_w + 5)
                btn_rect = pygame.Rect(bx, y, btn_w, 30)
                is_on = gm in src.gas_modes

                def _toggle_gas(mode=gm):
                    if mode in src.gas_modes:
                        src.gas_modes.discard(mode)
                    else:
                        src.gas_modes.add(mode)

                entity_rows.append(("gas_toggle", btn_rect, gm.value, is_on))
                clickables.append((btn_rect, _toggle_gas))

            y += 42

            if not src.gas_modes:
                entity_rows.append(("text", y, "Gaz modu seçilmedi — yayılım yok"))
                y += 20

            def set_power(d):
                src.power = clamp(src.power + d, 1, 10)

            add_numeric_row("Güç", str(src.power), dec_fn=lambda: set_power(-1), inc_fn=lambda: set_power(+1))

            # Her aktif gaz için ayrı ppm ve menzil kontrolü
            if GasMode.CO in src.gas_modes:
                entity_rows.append(("text", y, "── CO (Karbonmonoksit) ──"))
                y += 20

                def set_co_ppm(d):
                    src.co_ppm = max(10.0, min(10000.0, src.co_ppm + d))
                def set_co_range(d):
                    src.co_range = clamp(src.co_range + d, 1, 80)

                add_numeric_row("CO ppm", f"{src.co_ppm:.0f}",
                                dec_fn=lambda: set_co_ppm(-50), inc_fn=lambda: set_co_ppm(+50), step_hint="(±50)")
                add_numeric_row("CO Menzil", str(src.co_range),
                                dec_fn=lambda: set_co_range(-1), inc_fn=lambda: set_co_range(+1))

            if GasMode.CO2 in src.gas_modes:
                entity_rows.append(("text", y, "── CO2 (Karbondioksit) ──"))
                y += 20

                def set_co2_ppm(d):
                    src.co2_ppm = max(100.0, min(100000.0, src.co2_ppm + d))
                def set_co2_range(d):
                    src.co2_range = clamp(src.co2_range + d, 1, 80)

                add_numeric_row("CO2 ppm", f"{src.co2_ppm:.0f}",
                                dec_fn=lambda: set_co2_ppm(-500), inc_fn=lambda: set_co2_ppm(+500), step_hint="(±500)")
                add_numeric_row("CO2 Menzil", str(src.co2_range),
                                dec_fn=lambda: set_co2_range(-1), inc_fn=lambda: set_co2_range(+1))

            if GasMode.H2 in src.gas_modes:
                entity_rows.append(("text", y, "── H2 (Hidrojen) ──"))
                y += 20

                def set_h2_ppm(d):
                    src.h2_ppm = max(100.0, min(100000.0, src.h2_ppm + d))
                def set_h2_range(d):
                    src.h2_range = clamp(src.h2_range + d, 1, 80)

                add_numeric_row("H2 ppm", f"{src.h2_ppm:.0f}",
                                dec_fn=lambda: set_h2_ppm(-500), inc_fn=lambda: set_h2_ppm(+500), step_hint="(±500)")
                add_numeric_row("H2 Menzil", str(src.h2_range),
                                dec_fn=lambda: set_h2_range(-1), inc_fn=lambda: set_h2_range(+1))

    elif e.kind == Kind.BURNED and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip: TEMP (burned)"))
        y += 22

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power), dec_fn=lambda: set_power(-1), inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles), dec_fn=lambda: set_srange(-1), inc_fn=lambda: set_srange(+1))

    elif e.kind == Kind.UAV and e.uav:
        up = e.uav

        entity_rows.append(("text", y, "Rota: K ile düzenle (İHA seçiliyken)"))
        y += 18
        entity_rows.append(("text", y, f"Waypoint sayısı: {len(up.route)}"))
        y += 22

        def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)

        add_numeric_row("Hız (tile/s)", f"{up.speed:.1f}", dec_fn=lambda: set_speed(-0.5), inc_fn=lambda: set_speed(+0.5), step_hint="(±0.5)")

        route_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("switch", route_sw, "Rotayı göster (mavi başlangıç)", up.show_route))

        def toggle_route():
            up.show_route = not up.show_route

        clickables.append((route_sw, toggle_route))
        y += 40

        mode_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("mode_switch", mode_sw, "Tersine takip (PingPong)", up.route_mode == RouteMode.PINGPONG))

        def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1

        clickables.append((mode_sw, toggle_mode))
        y += 40

        entity_rows.append(("text", y, "Taşınanlar (sürükle-bırak):"))
        y += 18

        slot_w = (PANEL_W - 2 * PAD - 10) // 3
        slots = []
        for i in range(3):
            r = pygame.Rect(panel_x + PAD + i * (slot_w + 5), y, slot_w, 42)
            slots.append(r)
        entity_rows.append(("cargo_slots", slots))
        y += 54

        clr = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", clr, "Taşınanları Temizle"))

        def clear_cargo():
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()

        clickables.append((clr, clear_cargo))
        y += 42

        if up.carrying_ids:
            entity_rows.append(("text", y, "── Taşınan Nesneler ──"))
            y += 22
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce is None:
                    continue

                # Güzel etiket: isim varsa göster, yoksa tip+id
                ce_label = ce.display_name
                if ce.kind == Kind.SENSOR and ce.sensor:
                    modes_str = ",".join(sorted(m.value for m in ce.sensor.modes)) if ce.sensor.modes else "yok"
                    ce_label += f"  [{modes_str}]"
                elif ce.kind in (Kind.SOURCE, Kind.BURNED) and ce.source:
                    if ce.source.stype == SourceType.TEMP:
                        ce_label += f"  [{ce.source.temp_celcius:.0f}°C]"
                    else:
                        gm_str = ",".join(sorted(m.value for m in ce.source.gas_modes)) if ce.source.gas_modes else "yok"
                        ce_label += f"  [{gm_str}]"

                rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
                entity_rows.append(("carry_edit_btn", rect, ce_label, cid))
                clickables.append((rect, ("uav_focus_cargo", cid)))
                y += 38

        if uav_focus_cargo_id is not None and uav_focus_cargo_id in list(up.carrying_ids):
            ce = find_entity_by_id(entities, uav_focus_cargo_id)
            if ce is not None:
                y += 4
                entity_rows.append(("text", y, f"▸ {ce.display_name} özellikleri:"))
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
                        if src2.stype == SourceType.TEMP:
                            entity_rows.append(("text", y, f"Tip: TEMP  ({src2.temp_celcius:.0f}°C)"))
                        else:
                            gm_str = ", ".join(sorted(m.value for m in src2.gas_modes)) if src2.gas_modes else "yok"
                            entity_rows.append(("text", y, f"Tip: GAS  modlar: {gm_str}"))
                        y += 18

                        def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)

                        def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

                        add_numeric_row("Güç", str(src2.power), dec_fn=lambda: set_power2(-1), inc_fn=lambda: set_power2(+1))
                        add_numeric_row("Menzil", str(src2.range_tiles), dec_fn=lambda: set_srange2(-1), inc_fn=lambda: set_srange2(+1))

                    elif ce.kind == Kind.SENSOR and ce.sensor:
                        s2 = ce.sensor
                        modes_str = ", ".join(sorted(m.value for m in s2.modes)) if s2.modes else "yok"
                        entity_rows.append(("text", y, f"Modlar: {modes_str}"))
                        y += 18
                        entity_rows.append(("text", y, f"Pil: {int(s2.battery)} | Menzil: {s2.range_tiles}"))
                        y += 18

                        def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True

                        def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)

                        add_numeric_row("Menzil", str(s2.range_tiles), dec_fn=lambda: set_range2(-1), inc_fn=lambda: set_range2(+1))
                        add_numeric_row("Verimlilik", str(s2.efficiency), dec_fn=lambda: set_eff2(-5), inc_fn=lambda: set_eff2(+5), step_hint="(±5)")

    elif e.kind == Kind.OBSTACLE:
        entity_rows.append(("text", y, "Engel: şimdilik sadece blok objesi."))
        y += 18
        entity_rows.append(("text", y, "Sonraki adım: LOS ile zayıflatma."))
        y += 22

    # ── Olay Logu (tüm entity tipleri için, alarm_bridge varsa) ──
    if alarm_bridge is not None and alarm_bridge.log_lines:
        y += 10
        entity_rows.append(("text", y, "── Olay Logu ──"))
        y += 20
        # Son N log satırı (en yeniler altta)
        recent = alarm_bridge.log_lines[-15:]
        for line in recent:
            is_alert = "ALERT" in line
            entity_rows.append(("log_line", y, line, is_alert))
            y += 16
        y += 4

    # Content bottom: global + entity + sabit UI (full scroll)
    for row in global_rows + entity_rows:
        if row[0] in ("switch", "mode_switch"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] in ("text", "log_line"):
            content_bottom = max(content_bottom, row[1] + 28)
        elif row[0] == "alarm_text":
            content_bottom = max(content_bottom, row[1] + 28)
        elif row[0] == "sensor_val":
            content_bottom = max(content_bottom, row[1] + 22)
        elif row[0] == "gas_toggle":
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "numeric":
            content_bottom = max(content_bottom, row[1] + 60)
        elif row[0] in ("button", "carry_edit_btn", "segmented", "cargo_toggle"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "cargo_slots":
            for r in row[1]:
                content_bottom = max(content_bottom, r.bottom)

    # Seçili bölüm başlığı/etiket gibi sabit y'leri de dahil et (scroll artık tüm panel)
    content_bottom = max(content_bottom, PANEL_Y_SELECTED_LABEL + 40)

    return tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom


def draw_panel(
    screen,
    panel_x: int,
    font,
    small,
    tool_buttons,
    global_rows,
    entity_rows,
    selected_tool,
    selected_entity,
    panel_scroll: int = 0,
    sim_running: bool = False,
    sim_time: float = 0.0,
    alarm_bridge=None,
    show_log_view=False,
):
    # Full-panel scroll: her şeyi y_offset ile çiz
    y_offset = -panel_scroll

    # clip: panel dışına taşan çizimler görünmesin
    prev_clip = screen.get_clip()
    screen.set_clip(pygame.Rect(panel_x, 0, PANEL_W, SCREEN_H))

    # Panel background
    pygame.draw.rect(screen, (12, 12, 14), pygame.Rect(panel_x, 0, PANEL_W, SCREEN_H))

    # Header
    screen.blit(font.render("Araçlar", True, (245, 245, 245)), (panel_x + PAD, 24 + y_offset))

    # Tool buttons
    for kind, rect, label in tool_buttons:
        rr = rect.move(0, y_offset)
        draw_button(screen, rr, label, small, active=(selected_tool == kind))

    # Sim status
    screen.blit(
        small.render(f"Sim: {'RUNNING' if sim_running else 'PAUSED'}  (Space)", True, (200, 200, 200)),
        (panel_x + PAD, 320 + y_offset),
    )
    screen.blit(
        small.render(f"Zaman: {sim_time:.0f}s", True, (200, 200, 200)),
        (panel_x + PAD, 340 + y_offset),
    )

    # Alarm özet satırı
    if alarm_bridge is not None:
        ac = alarm_bridge.alert_count
        te = alarm_bridge.total_events
        color = (255, 90, 90) if ac > 0 else (120, 210, 150)
        screen.blit(
            small.render(f"Alarm: {ac} aktif | Toplam olay: {te}", True, color),
            (panel_x + PAD, 358 + y_offset),
        )

    # Global section
    draw_section_title(screen, panel_x + PAD, PANEL_Y_APPEAR + y_offset, "Görünüm", font, small)
    for row in global_rows:
        if row[0] == "switch":
            _, sw_rect, label, on = row
            rr = sw_rect.move(0, y_offset)
            screen.blit(small.render(label, True, (220, 220, 220)), (rr.right + 10, rr.y + 3))
            draw_switch(screen, rr, on)

    # Selected / Log section
    section_title = "Log Görünümü" if show_log_view else "Seçili"
    draw_section_title(screen, panel_x + PAD, PANEL_Y_SELECTED_TITLE + y_offset, section_title, font, small)

    if show_log_view:
        # Log view modunda entity_rows zaten log içeriğini barındırıyor
        # Doğrudan entity_rows çizimine atla
        pass
    elif selected_entity is None:
        screen.blit(
            small.render("Yok (haritadan bir entity seç)", True, (180, 180, 180)),
            (panel_x + PAD, PANEL_Y_SELECTED_LABEL + y_offset),
        )
        # Entity seçili değilken de entity_rows'ta log olabilir, çizime devam
    else:
        # Selected entity title
        screen.blit(
            small.render(selected_entity.display_name, True, (230, 230, 230)),
            (panel_x + PAD, PANEL_Y_SELECTED_LABEL + y_offset),
        )

    # Entity rows
    for row in entity_rows:
        typ = row[0]

        if typ == "text":
            _, y, text = row
            yy = y + y_offset
            if -40 <= yy <= SCREEN_H - 10:
                screen.blit(small.render(text, True, (200, 200, 200)), (panel_x + PAD, yy))

        elif typ == "alarm_text":
            _, y, text = row
            yy = y + y_offset
            if -40 <= yy <= SCREEN_H - 10:
                # Kırmızı arka planlı alarm göstergesi
                txt_surf = small.render(text, True, (255, 255, 255))
                tw, th = txt_surf.get_size()
                bg_rect = pygame.Rect(panel_x + PAD - 4, yy - 2, min(tw + 8, PANEL_W - 2 * PAD), th + 4)
                pygame.draw.rect(screen, (180, 50, 50), bg_rect, border_radius=4)
                screen.blit(txt_surf, (panel_x + PAD, yy))

        elif typ == "sensor_val":
            _, y, text, is_warn = row
            yy = y + y_offset
            if -40 <= yy <= SCREEN_H - 10:
                color = (255, 100, 100) if is_warn else (200, 200, 200)
                screen.blit(small.render(text, True, color), (panel_x + PAD, yy))

        elif typ == "gas_toggle":
            _, rect, label, is_on = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            bg = (60, 140, 90) if is_on else (50, 50, 55)
            border = (120, 210, 150) if is_on else (90, 90, 100)
            pygame.draw.rect(screen, bg, rr, border_radius=6)
            pygame.draw.rect(screen, border, rr, 1, border_radius=6)
            lbl = small.render(label, True, (240, 240, 240))
            screen.blit(lbl, (rr.centerx - lbl.get_width() // 2, rr.centery - lbl.get_height() // 2))

        elif typ == "log_line":
            _, y, text, is_alert = row
            yy = y + y_offset
            if -40 <= yy <= SCREEN_H - 10:
                color = (255, 120, 120) if is_alert else (160, 160, 160)
                # Küçük font ile sığdır
                screen.blit(small.render(text, True, color), (panel_x + PAD, yy))

        elif typ in ("switch", "mode_switch"):
            _, rect, label, on = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            screen.blit(small.render(label, True, (220, 220, 220)), (rr.right + 10, rr.y + 3))
            draw_switch(screen, rr, on)

        elif typ == "button":
            _, rect, label = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            draw_button(screen, rr, label, small, active=False)

        elif typ == "carry_edit_btn":
            _, rect, label, _cid = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            draw_button(screen, rr, label, small, active=False)

        elif typ == "cargo_toggle":
            _, rect, label = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            draw_small_btn(screen, rr, label, small)

        elif typ == "numeric":
            _, y, label, minus_rect, plus_rect, step_hint = row
            yy = y + y_offset
            if yy > SCREEN_H or yy < -120:
                continue
            screen.blit(small.render(label, True, (220, 220, 220)), (panel_x + PAD, yy))
            mr = minus_rect.move(0, y_offset)
            pr = plus_rect.move(0, y_offset)
            draw_small_btn(screen, mr, "-", small)
            draw_small_btn(screen, pr, "+", small)
            if step_hint:
                screen.blit(small.render(step_hint, True, (150, 150, 150)), (panel_x + PAD + 80, mr.y + 4))

        elif typ == "segmented":
            _, rect, opts, sel = row
            rr = rect.move(0, y_offset)
            if rr.bottom < 0 or rr.top > SCREEN_H:
                continue
            draw_segmented(screen, rr, opts, sel, small)

        elif typ == "cargo_slots":
            slots = row[1]
            for r in slots:
                rr = r.move(0, y_offset)
                pygame.draw.rect(screen, (35, 35, 40), rr, border_radius=10)
                pygame.draw.rect(screen, (90, 90, 100), rr, 1, border_radius=10)

    # restore clip
    screen.set_clip(prev_clip)