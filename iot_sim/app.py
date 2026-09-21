"""Pygame deney uygulaması: girdi, sabit saatli model ve responsive görünüm."""
import argparse
import math
from pathlib import Path
import pygame
from .models import Kind, SensorMode, GasMode, SourceType, RouteMode
from .simulation import Simulation
from .scene import load_scene, save_scene, to_scene, parse_scene
from .lessons import lesson_scene, LESSONS
from .exporter import Exporter, ROOT
from .engine import find_entity_at, find_entity_by_id, clamp
from . import operations
from .camera import Camera
from .panel import Inspector
from .render import draw_world
from .graphs import draw_graph
from .assets import load_icon
from .ui_widgets import button, text_block, BG, TEXT, MUTED, ACCENT

SPEEDS=(.25,1,2,5)


class App:
    """Ekran ve olay sahipliği; model kuralları Simulation/operations içindedir."""
    def __init__(self, scene=None, out_dir=None, size=(1360,900)):
        pygame.init()
        self.screen=pygame.display.set_mode(size,pygame.RESIZABLE)
        pygame.display.set_caption("IoT Deney Atölyesi")
        self.font=pygame.font.SysFont("DejaVu Sans",19)
        self.small=pygame.font.SysFont("DejaVu Sans",14)
        self.tiny=pygame.font.SysFont("DejaVu Sans",12)
        self.title_font=pygame.font.SysFont("DejaVu Sans",25,bold=True)
        self.clock=pygame.time.Clock()
        self.sim=Simulation(scene if scene is not None else lesson_scene(1))
        self.out_dir=out_dir
        self.exporter=None
        self.last_output=None
        self.running=True
        self.playing=False
        self.speed=1
        self.selected_id=None
        self.tool=None
        self.tab="lesson"
        self.inspector=Inspector()
        self.cam=Camera()
        self.buttons={}
        self.channel="TEMP"
        self.show_theory=True
        self.show_field=False
        self.show_grid=True
        self.filter_selected=False
        self.filter_kind="Tümü"
        self.mode=None
        self.mode_id=None
        self.route_points=[]
        self.drag_origin=None
        self.pan_anchor=None
        self.modal=None
        self.input_text=""
        self.toast="Bir deney seç veya Başlat ile uzaklık deneyini çalıştır."
        self.toast_until=pygame.time.get_ticks()+6000
        self.icons={key:load_icon(str(ROOT/"assets"/(key+".png")))
                    for key in ("sensor","source_temp","source_gas","obstacle","burned","drone")}
        self.focus_scene()

    @property
    def selected(self):
        return find_entity_by_id(self.sim.entities,self.selected_id)

    def focus_scene(self):
        visible=[e for e in self.sim.entities if e.carried_by is None]
        self.cam.x=sum(e.tx+.5 for e in visible)/len(visible) if visible else 100
        self.cam.y=sum(e.ty+.5 for e in visible)/len(visible) if visible else 100

    def message(self,text):
        self.toast=str(text)
        self.toast_until=pygame.time.get_ticks()+6000

    def btn(self,key,rect,label,action,active=False,clip=None):
        button(self.screen,rect,label,self.small,active)
        hit=rect.clip(clip) if clip else rect
        if hit.width and hit.height:
            self.buttons[key]=(hit,action)

    def layout(self):
        width,height=self.screen.get_size()
        panel_w=360 if width>=1200 else 320
        self.panel_rect=pygame.Rect(width-panel_w-16,154,panel_w,height-180)
        map_w=self.panel_rect.x-34
        graph_h=218
        self.cam.viewport=pygame.Rect(18,154,map_w,max(100,height-154-graph_h-40))
        self.graph_rect=pygame.Rect(18,self.cam.viewport.bottom+12,map_w,graph_h)
        self.graph_rect.height=min(graph_h,height-self.graph_rect.y-22)

    def draw(self):
        self.layout()
        self.buttons={}
        screen=self.screen
        screen.fill(BG)
        width,height=screen.get_size()
        screen.blit(self.title_font.render("IoT Deney Atölyesi",True,TEXT),(18,15))
        caption=f"{'ÇALIŞIYOR' if self.playing else 'DURAKLATILDI'}   •   {self.sim.time:.2f} s   •   {self.sim.alarm.alert_count} alarm"
        label=self.small.render(caption,True,ACCENT)
        screen.blit(label,(width-label.get_width()-18,24))
        actions=[
            ("play","Duraklat" if self.playing else "Başlat",("play",),98),
            ("step","Tek adım",("step",),90),("reset","Başa dön",("reset",),94),
            ("speed",f"Hız {self.speed:g}×",("speed",),82),
            ("seed",f"Tohum {self.sim.seed}",("seed",),112),
            ("new","Yeni",("new",),64),("save","Kaydet",("save",),78),
            ("load","Yükle",("load",),78),("lessons","Deneyler",("tab","lesson"),96)]
        x=18
        for key,label,action,w in actions:
            self.btn(key,pygame.Rect(x,62,w,34),label,action,self.playing if key=="play" else False)
            x+=w+7
        tools=[("select","Seç",None),("sensor","Sensör",Kind.SENSOR),("source","Kaynak",Kind.SOURCE),
               ("obstacle","Engel / Ağaç",Kind.OBSTACLE),("drone","Drone",Kind.UAV)]
        x=18
        for key,label,kind in tools:
            w=112 if key=="obstacle" else 85
            self.btn("tool_"+key,pygame.Rect(x,108,w,30),label,("tool",kind),self.tool==kind)
            x+=w+6
        self.btn("field",pygame.Rect(x+4,108,150,30),"Teorik alan "+("Açık" if self.show_field else "Kapalı"),("field",),self.show_field)
        self.btn("center",pygame.Rect(x+162,108,90,30),"Ortala",("center",))
        draw_world(screen,self.cam,self.sim,self.selected_id,self.icons,self.tiny,
                   layer=self.channel if self.channel!="BATTERY" else "TEMP",
                   show_field=self.show_field,route_preview=self.route_points,show_grid=self.show_grid)
        if self.mode:
            description={"move":"TAŞI • Hedef kareye tıkla. Esc: iptal",
                         "route":"ROTA • Durak ekle; K: kaydet; Esc: iptal",
                         "attach":"YÜKLE • Sensör veya kaynağa tıkla; Esc: iptal"}[self.mode]
            text_block(screen,description,self.cam.viewport.x+12,self.cam.viewport.y+12,
                       self.cam.viewport.width-24,self.small,(255,215,130))
        graph=self.graph_rect
        gap=6
        bw=min(89,(graph.width-140)//5)
        for i,key in enumerate(("TEMP","CO","CO2","H2","BATTERY")):
            self.btn("channel_"+key,pygame.Rect(graph.x+i*(bw+gap),graph.y,bw,29),
                     "Pil" if key=="BATTERY" else key,("channel",key),self.channel==key)
        self.btn("theory",pygame.Rect(graph.right-130,graph.y,130,29),"Teorik çizgi",("theory",),self.show_theory)
        sensor=self.selected
        if sensor and sensor.uav:
            sensor=next((find_entity_by_id(self.sim.entities,cid) for cid in sensor.uav.carrying_ids
                         if find_entity_by_id(self.sim.entities,cid).sensor),None)
        if not sensor or not sensor.sensor:
            sensor=next((e for e in self.sim.entities if e.sensor),None)
        history=self.sim.history.get(sensor.id,[]) if sensor else []
        draw_graph(screen,pygame.Rect(graph.x,graph.y+36,graph.width,graph.height-36),
                   history,self.channel,self.tiny,self.show_theory)
        if sensor:
            tag=self.tiny.render(sensor.display_name,True,MUTED)
            screen.blit(tag,(graph.right-tag.get_width()-12,graph.y+46))
        self.inspector.draw(self,self.panel_rect)
        footer="Space: çalıştır  •  N: adım  •  M: taşı  •  K: rota  •  Orta tuş: kaydır  •  Tekerlek: zoom"
        screen.blit(self.tiny.render(footer,True,MUTED),(18,height-17))
        if self.toast and pygame.time.get_ticks()<self.toast_until:
            box=pygame.Rect(self.cam.viewport.x+8,self.cam.viewport.bottom-90,self.cam.viewport.width-16,80)
            pygame.draw.rect(screen,(28,44,58),box,border_radius=8)
            text_block(screen,self.toast,box.x+12,box.y+10,box.width-24,self.small)
        if self.modal:
            shade=pygame.Surface(screen.get_size(),pygame.SRCALPHA)
            shade.fill((0,0,0,180))
            screen.blit(shade,(0,0))
            box=pygame.Rect(0,0,min(780,width-60),220)
            box.center=screen.get_rect().center
            pygame.draw.rect(screen,(30,44,60),box,border_radius=14)
            labels={"save":"Başlangıç sahnesini kaydet (.json)","load":"Sahne yükle (.json)",
                    "seed":"Yeni deney tohumu (0–4294967295)","rename":"Nesne adı"}
            text_block(screen,labels[self.modal],box.x+20,box.y+20,box.width-40,self.font)
            # Son karakterler görünür; tam yol input_text içinde korunur.
            display=self.input_text
            while self.small.size(display+"|")[0]>box.width-40: display=display[1:]
            text_block(screen,display+"|",box.x+20,box.y+85,box.width-40,self.small,ACCENT)
            text_block(screen,"Enter: uygula   •   Esc: iptal",box.x+20,box.bottom-48,box.width-40,self.small,MUTED)
        pygame.display.flip()

    def begin_recording(self):
        if self.exporter is None:
            if self.sim.time==0:
                self.sim.baseline=self.sim.snapshot()
            self.exporter=Exporter(self.out_dir,scene=self.sim.snapshot())
            self.sim.start_recording(self.exporter)
            self.last_output=self.exporter.directory

    def close_recording(self):
        if self.exporter:
            self.last_output=self.exporter.close()
            self.exporter=None
            self.sim.exporter=None

    def change(self,description):
        """Editör değişikliklerini deney çıktısında zamanıyla kaydet."""
        self.sim.revision += 1
        if self.sim.time==0:
            self.sim.baseline=self.sim.snapshot()
        if self.exporter:
            self.exporter.log_change(self.sim.time,description,self.sim.snapshot())

    def replace_sim(self,scene):
        """Yeni sahne önce tamamen doğrulanır; sonra eski oturum kapatılır."""
        candidate=Simulation(scene)
        self.close_recording()
        self.sim=candidate
        self.playing=False
        self.selected_id=None
        self.mode=None
        self.mode_id=None
        self.route_points=[]
        self.inspector.scroll=0
        self.focus_scene()

    def prompt(self,kind):
        self.playing=False
        self.modal=kind
        self.input_text=str(ROOT/"scenes"/"deney.json") if kind in ("load","save") else str(self.sim.seed) if kind=="seed" else self.selected.name

    def submit(self):
        kind=self.modal
        value=self.input_text.strip()
        if kind=="save":
            path=Path(value).expanduser()
            if path.suffix.lower()!=".json": raise ValueError("Dosya uzantısı .json olmalı.")
            save_scene(path,self.sim.snapshot())
            self.message(f"Sahne kaydedildi: {path}")
        elif kind=="load":
            self.replace_sim(load_scene(Path(value).expanduser()))
            self.message("Sahne doğrulandı ve yüklendi.")
        elif kind=="seed":
            seed=int(value)
            scene=self.sim.snapshot()
            scene["seed"]=seed
            self.replace_sim(scene)
            self.message("Tohum değişti; yeni başlangıç oluşturuldu.")
        elif kind=="rename" and self.selected:
            if len(value)>80: raise ValueError("İsim en fazla 80 karakter olabilir.")
            self.selected.name=value
            self.change("rename")
        self.modal=None

    def action(self,action):
        """Buton ve kısayolları aynı işlem yoluna yönlendir."""
        name,*args=action
        e=self.selected
        if name=="play":
            if not self.playing: self.begin_recording()
            self.playing=not self.playing
        elif name=="step":
            self.playing=False
            self.begin_recording()
            interval=e.sensor.sample_interval if e and e.sensor else 1
            self.sim.advance(interval)
        elif name=="reset":
            baseline=self.sim.baseline
            self.replace_sim(baseline)
            self.message("Aynı başlangıç ve tohum yeniden kuruldu.")
        elif name=="speed":
            self.speed=SPEEDS[(SPEEDS.index(self.speed)+1)%len(SPEEDS)]
        elif name=="new":
            self.replace_sim(to_scene([],seed=self.sim.seed))
            self.tab="properties"
            self.message("Boş deney; araç seçip nesne ekle.")
        elif name in ("save","load","seed","rename"):
            if name!="rename" or e: self.prompt(name)
        elif name=="lesson":
            self.replace_sim(lesson_scene(args[0]))
            self.tab="lesson"
            self.message(LESSONS[args[0]-1]["goal"])
        elif name=="tab":
            self.tab=args[0]
            self.inspector.scroll=0
        elif name=="tool":
            self.tool=args[0]
            self.mode=None
            self.route_points=[]
            self.tab="properties"
        elif name=="field": self.show_field=not self.show_field
        elif name=="theory": self.show_theory=not self.show_theory
        elif name=="center": self.focus_scene()
        elif name=="channel": self.channel=args[0]
        elif name=="filter_sensor": self.filter_selected=not self.filter_selected
        elif name=="filter_kind":
            values=("Tümü","ALERT","CALM","STATUS","UNAVAILABLE","FIRE")
            self.filter_kind=values[(values.index(self.filter_kind)+1)%len(values)]
        elif name=="select":
            self.selected_id=args[0]
            self.tool=None
            self.inspector.scroll=0
        elif e:
            self.playing=False
            if name=="move":
                if e.carried_by: raise ValueError("Önce yükü indir.")
                self.mode,self.mode_id="move",e.id
            elif name=="delete":
                operations.delete_entity(self.sim,e.id)
                self.selected_id=None
                self.mode=None
                self.route_points=[]
                self.change("delete")
            elif name=="route" and e.uav:
                if self.mode=="route" and self.mode_id==e.id:
                    operations.set_route(self.sim,e,self.route_points)
                    self.mode=None
                    self.route_points=[]
                    self.change("route")
                else:
                    self.mode,self.mode_id="route",e.id
                    self.route_points=[]
            elif name=="attach" and e.uav:
                self.mode,self.mode_id="attach",e.id
            elif name=="release" and e.uav:
                operations.release_cargo(self.sim,e)
                self.change("release")
            elif name=="route_mode" and e.uav:
                e.uav.route_mode=RouteMode.PINGPONG if e.uav.route_mode==RouteMode.LOOP else RouteMode.LOOP
                e.uav.route_dir=1
                self.change(name)
            elif name=="route_clear" and e.uav:
                e.uav.route=[]
                e.uav.blocked_reason=""
                self.change(name)
            elif name=="sensor_mode":
                mode=args[0]
                e.sensor.modes.symmetric_difference_update({mode})
                # Kanal kapatınca geçmiş okumayı geçerli tutma.
                from .sensors import invalidate
                invalidate(e.sensor,"WAITING" if e.sensor.modes else "OFF")
                self.sim.alarm.update(self.sim.entities,self.sim.time)
                self.change(name)
            elif name=="gas_mode":
                e.source.gas_modes.symmetric_difference_update({args[0]})
                self.change(name)
            elif name=="source_type":
                e.source.stype=SourceType.GAS if e.source.stype==SourceType.TEMP else SourceType.TEMP
                self.change(name)
            elif name=="toggle":
                target=e.sensor or e.uav
                setattr(target,args[0],not getattr(target,args[0]))
                if e.sensor:
                    from .sensors import invalidate
                    invalidate(e.sensor,"WAITING" if e.sensor.enabled else "OFF")
                    self.sim.alarm.update(self.sim.entities,self.sim.time)
                self.change(name)
            elif name=="entity_toggle":
                setattr(e,args[0],not getattr(e,args[0]))
                self.change(name)
            elif name=="adjust":
                key,delta,low,high=args
                target=e.sensor or e.source or e.uav or e
                if "." in key:
                    attribute,channel=key.split(".")
                    values=getattr(target,attribute)
                    values[channel]=round(clamp(values[channel]+delta,low,high),6)
                    if attribute in ("thresholds","clear_thresholds"):
                        target.clear_thresholds[channel]=min(target.clear_thresholds[channel],target.thresholds[channel])
                else:
                    value=round(clamp(getattr(target,key)+delta,low,high),6)
                    if type(getattr(target,key)) is int: value=int(value)
                    setattr(target,key,value)
                    if key=="max_limit": target.limit=min(target.limit,target.max_limit)
                self.change(key)
                self.message("Ayar güncellendi. Devam et veya Tek adım ile etkisini gözle.")

    def map_click(self,pos):
        wx,wy=self.cam.screen_to_world(pos)
        x,y=math.floor(wx),math.floor(wy)
        if not (0<=x<self.sim.width and 0<=y<self.sim.height): return
        index=find_entity_at(self.sim.entities,x,y)
        hit=self.sim.entities[index] if index is not None else None
        if self.mode=="move":
            operations.move_entity(self.sim,self.mode_id,x,y)
            self.mode=None
            self.change("move")
        elif self.mode=="attach":
            if hit is None: raise ValueError("Bir sensör veya kaynak seç.")
            operations.attach(self.sim,self.mode_id,hit.id)
            self.mode=None
            self.change("attach")
        elif self.mode=="route":
            if self.route_points and self.route_points[-1]==(x,y):
                raise ValueError("Aynı durağı arka arkaya ekleme.")
            self.route_points.append((x,y))
        elif self.tool is not None and hit is None:
            e=operations.add_entity(self.sim,self.tool,x,y)
            self.selected_id=e.id
            self.change("add")
        else:
            self.selected_id=hit.id if hit else None
            self.tool=None
            self.tab="properties"
        self.inspector.scroll=0

    def process_event(self,event):
        """Gerçek event.pos kullan; aynı karedeki olaylar birbirinin koordinatını almaz."""
        try:
            if event.type==pygame.QUIT:
                self.running=False
            elif event.type==pygame.VIDEORESIZE:
                self.screen=pygame.display.set_mode((max(1024,event.w),max(720,event.h)),pygame.RESIZABLE)
            elif self.modal:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: self.modal=None
                    elif event.key==pygame.K_RETURN: self.submit()
                    elif event.key==pygame.K_BACKSPACE: self.input_text=self.input_text[:-1]
                    elif event.unicode and event.unicode.isprintable() and len(self.input_text)<4096:
                        self.input_text+=event.unicode
            elif event.type==pygame.KEYDOWN:
                mods=getattr(event,"mod",pygame.key.get_mods())
                mapping={pygame.K_SPACE:("play",),pygame.K_n:("step",),pygame.K_m:("move",),
                         pygame.K_k:("route",),pygame.K_DELETE:("delete",),pygame.K_BACKSPACE:("delete",)}
                if event.key==pygame.K_ESCAPE:
                    self.mode=None
                    self.mode_id=None
                    self.route_points=[]
                    self.tool=None
                elif mods & pygame.KMOD_CTRL and event.key in (pygame.K_s,pygame.K_o):
                    self.action(("save" if event.key==pygame.K_s else "load",))
                elif event.key==pygame.K_g: self.show_grid=not self.show_grid
                elif event.key in mapping: self.action(mapping[event.key])
            elif event.type==pygame.MOUSEWHEEL:
                pos=pygame.mouse.get_pos()
                if self.panel_rect.collidepoint(pos):
                    self.inspector.scroll=clamp(self.inspector.scroll-event.y*60,0,self.inspector.bottom)
                elif self.cam.viewport.collidepoint(pos): self.cam.zoom_at(1.12**event.y)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                if event.button==1:
                    for rect,action in reversed(list(self.buttons.values())):
                        if rect.collidepoint(pos):
                            self.action(action)
                            return
                    if self.cam.viewport.collidepoint(pos):
                        # Seçili drone korunurken nesneyi panel üstüne sürükleme.
                        wx,wy=self.cam.screen_to_world(pos)
                        idx=find_entity_at(self.sim.entities,math.floor(wx),math.floor(wy))
                        hit=self.sim.entities[idx] if idx is not None else None
                        if not self.mode and self.selected and self.selected.uav and hit and (hit.sensor or hit.source):
                            self.drag_origin=(self.selected_id,hit.id,pos)
                        else: self.map_click(pos)
                elif event.button==3 and self.cam.viewport.collidepoint(pos):
                    wx,wy=self.cam.screen_to_world(pos)
                    idx=find_entity_at(self.sim.entities,math.floor(wx),math.floor(wy))
                    if idx is not None:
                        self.selected_id=self.sim.entities[idx].id
                        self.action(("delete",))
                elif event.button==2 and self.cam.viewport.collidepoint(pos):
                    self.pan_anchor=pos
                elif event.button in (4,5):
                    delta=1 if event.button==4 else -1
                    if self.panel_rect.collidepoint(pos): self.inspector.scroll=clamp(self.inspector.scroll-delta*60,0,self.inspector.bottom)
                    elif self.cam.viewport.collidepoint(pos): self.cam.zoom_at(1.12**delta)
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==2: self.pan_anchor=None
                if event.button==1 and self.drag_origin:
                    drone,cargo,start=self.drag_origin
                    self.drag_origin=None
                    if self.panel_rect.collidepoint(event.pos):
                        operations.attach(self.sim,drone,cargo)
                        self.change("attach")
                    else: self.map_click(event.pos)
            elif event.type==pygame.MOUSEMOTION and self.pan_anchor:
                dx,dy=event.pos[0]-self.pan_anchor[0],event.pos[1]-self.pan_anchor[1]
                self.cam.x=clamp(self.cam.x-dx/(24*self.cam.zoom),0,self.sim.width)
                self.cam.y=clamp(self.cam.y-dy/(24*self.cam.zoom),0,self.sim.height)
                self.pan_anchor=event.pos
        except (ValueError,OSError) as exc:
            self.message(str(exc))

    def run(self,max_frames=None):
        frames=0
        try:
            while self.running and (max_frames is None or frames<max_frames):
                dt=self.clock.tick(60)/1000
                self.draw()
                for event in pygame.event.get(): self.process_event(event)
                if self.playing: self.sim.advance(min(dt,.25)*self.speed)
                frames+=1
        finally:
            self.close_recording()
            pygame.quit()


def main(argv=None):
    parser=argparse.ArgumentParser(description="Öğretici IoT deney ortamı")
    parser.add_argument("--lesson",type=int,choices=range(1,7),default=1)
    parser.add_argument("--scene",type=Path)
    parser.add_argument("--seed",type=int)
    parser.add_argument("--out-dir",type=Path)
    parser.add_argument("--seconds",type=float,help="Pencere açmadan belirtilen simülasyon süresini çalıştır.")
    parser.add_argument("--smoke-frames",type=int,help=argparse.SUPPRESS)
    args=parser.parse_args(argv)
    scene=load_scene(args.scene) if args.scene else lesson_scene(args.lesson)
    if args.seed is not None: scene["seed"]=args.seed
    if args.seconds is not None:
        sim=Simulation(scene)
        with Exporter(args.out_dir,scene=scene) as exporter:
            sim.start_recording(exporter)
            sim.advance(args.seconds)
            print(f"{sim.time:.2f} simülasyon saniyesi • {sim.alarm.total_events} olay • {exporter.directory}")
    else:
        App(scene,args.out_dir).run(args.smoke_frames)


if __name__=="__main__":
    main()
