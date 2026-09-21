"""Yeniden boyutlandırılabilir harita; gerçek ölçüm ile teorik katman ayrıdır."""
import math
import pygame
from .models import Kind, SourceType, RouteMode
from .sensors import field_at, position
from .viz import EffectCache

COLORS = {Kind.SENSOR:(91,211,194), Kind.SOURCE:(255,184,96),
          Kind.UAV:(119,163,255), Kind.OBSTACLE:(103,154,109), Kind.BURNED:(244,114,96)}
FIELD_CACHE = EffectCache()

GAS_COLORS = {"CO":(244,114,114),"CO2":(106,215,161),"H2":(117,170,255)}


def draw_world(screen, cam, sim, selected_id, icons, font, layer="TEMP", show_field=False, route_preview=None, show_grid=True):
    """Görünür karoları çiz; alan örnekleri en fazla 35×25 hücredir."""
    viewport = cam.viewport
    previous = screen.get_clip()
    screen.set_clip(viewport)
    screen.fill((18,26,35), viewport)
    tile = 24 * cam.zoom
    wx0, wy0 = cam.screen_to_world(viewport.topleft)
    wx1, wy1 = cam.screen_to_world(viewport.bottomright)
    if show_field and sim.entities:
        key=(sim.cache_token, sim.revision, int(sim.time*2), viewport.size, cam.x, cam.y, cam.zoom, layer)
        def build_overlay():
            cell = max(28, math.ceil(max(viewport.width/35, viewport.height/25)))
            overlay = pygame.Surface(viewport.size, pygame.SRCALPHA)
            for sy in range(0, viewport.height, cell):
                for sx in range(0, viewport.width, cell):
                    wx, wy = cam.screen_to_world((viewport.x+sx+cell/2, viewport.y+sy+cell/2))
                    if not (0 <= wx < sim.width and 0 <= wy < sim.height):
                        continue
                    values = field_at(wx-.5, wy-.5, sim.entities)
                    base, scale = (22,200) if layer=="TEMP" else (0, {"CO":200,"CO2":15000,"H2":12000}[layer])
                    alpha = round(min(135,max(0,(values[layer]-base)/scale*135)))
                    color = (255,160,80) if layer=="TEMP" else GAS_COLORS[layer]
                    pygame.draw.rect(overlay, (*color,alpha), (sx,sy,cell,cell))
            return overlay
        screen.blit(FIELD_CACHE.get(key, build_overlay), viewport.topleft)
    visual = pygame.Surface(viewport.size, pygame.SRCALPHA)
    for e in sim.entities:
        if e.source and e.show_effect:
            px,py=position(e,sim.entities)
            sx,sy=cam.world_to_screen(px+.5,py+.5)
            source=e.source
            ranges=[(source.range_tiles,(255,184,96))] if source.stype==SourceType.TEMP else [
                (getattr(source,m.value.lower()+"_range"),GAS_COLORS[m.value]) for m in source.gas_modes]
            for radius,color in ranges:
                pygame.draw.circle(visual,(*color,20+source.power*10),
                    (sx-viewport.x,sy-viewport.y),max(1,round(radius*tile)),1)
    screen.blit(visual,viewport.topleft)
    if show_grid:
        for x in range(max(0,math.floor(wx0)),min(sim.width,math.ceil(wx1))+1):
            sx,_=cam.world_to_screen(x,0)
            pygame.draw.line(screen,(31,43,55),(sx,viewport.top),(sx,viewport.bottom))
        for y in range(max(0,math.floor(wy0)),min(sim.height,math.ceil(wy1))+1):
            _,sy=cam.world_to_screen(0,y)
            pygame.draw.line(screen,(31,43,55),(viewport.left,sy),(viewport.right,sy))
    for e in sim.entities:
        if e.uav and e.uav.show_route and e.uav.route:
            points=[cam.world_to_screen(x+.5,y+.5) for x,y in e.uav.route]
            if len(points)>1:
                pygame.draw.lines(screen,(83,126,185),e.uav.route_mode==RouteMode.LOOP,points,2)
            for p in points: pygame.draw.circle(screen,(130,172,240),p,4)
    if route_preview:
        points=[cam.world_to_screen(x+.5,y+.5) for x,y in route_preview]
        if len(points)>1: pygame.draw.lines(screen,(255,215,119),False,points,3)
        for p in points: pygame.draw.circle(screen,(255,215,119),p,5)
    for e in sim.entities:
        if e.carried_by is not None:
            continue
        px,py=position(e,sim.entities)
        sx,sy=cam.world_to_screen(px+.5,py+.5)
        radius=max(5,min(25,round(tile*.35)))
        if not viewport.inflate(60,60).collidepoint(sx,sy):
            continue
        color=COLORS[e.kind]
        if e.kind==Kind.OBSTACLE and not e.flammable: color=(131,147,165)
        pygame.draw.circle(screen,color,(sx,sy),radius)
        icon_key="drone" if e.uav else "sensor" if e.sensor else "burned" if e.kind==Kind.BURNED else "obstacle" if e.kind==Kind.OBSTACLE else "source_gas" if e.source.stype==SourceType.GAS else "source_temp"
        icon=icons.get(icon_key)
        if icon:
            # En fazla altı ikon × mevcut tek ölçek; ara kopya cache büyütmez.
            image=pygame.transform.smoothscale(icon,(radius*2,radius*2))
            screen.blit(image,(sx-radius,sy-radius))
        if selected_id==e.id: pygame.draw.circle(screen,(234,243,255),(sx,sy),radius+5,2)
        if e.id in sim.alarm.active_alerts: pygame.draw.circle(screen,(255,101,114),(sx,sy),radius+9,2)
        if e.uav and e.uav.carrying_ids:
            pygame.draw.circle(screen,(91,211,194),(sx+radius,sy+radius),5)
        if e.kind==Kind.OBSTACLE and e.heat_seconds:
            rect=pygame.Rect(sx-radius,sy+radius+7,radius*2,4)
            pygame.draw.rect(screen,(80,60,50),rect)
            pygame.draw.rect(screen,(255,180,90),(rect.x,rect.y,rect.width*min(1,e.heat_seconds/e.ignition_seconds),4))
        label=font.render(e.name or f"#{e.id}",True,(196,211,226))
        screen.blit(label,(sx-label.get_width()/2,sy-radius-20))
    screen.set_clip(previous)
