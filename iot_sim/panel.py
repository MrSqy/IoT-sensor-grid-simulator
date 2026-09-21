"""Özellik, deney ve olay panelleri; eylemleri App'e veri olarak döndürür."""
import pygame
from .models import Kind, SensorMode, GasMode, SourceType
from .alarm_bridge import STATUS_LABELS
from .sensors import VALUE_ATTR
from .lessons import LESSONS
from .ui_widgets import text_block,button,TEXT,MUTED,ACCENT,PANEL,BORDER


class Inspector:
    """Yalnız panel içeriği kayar; sekmeler ve deney kontrolleri sabittir."""
    def __init__(self):
        self.scroll=0
        self.bottom=0

    def draw(self, app, rect):
        screen,font,small=app.screen,app.font,app.small
        pygame.draw.rect(screen,PANEL,rect,border_radius=12)
        tabs=[("properties","Nesne"),("lesson","Deney"),("log","Olaylar")]
        tabw=(rect.width-24)//3
        for i,(key,label) in enumerate(tabs):
            app.btn("tab_"+key,pygame.Rect(rect.x+10+i*tabw,rect.y+10,tabw-4,32),label,("tab",key),app.tab==key)
        clip=pygame.Rect(rect.x+10,rect.y+52,rect.width-20,rect.height-62)
        old=screen.get_clip()
        screen.set_clip(clip)
        x,width,y=clip.x+5,clip.width-10,clip.y-self.scroll
        def text(value,color=TEXT):
            nonlocal y
            y=text_block(screen,value,x,y,width,small,color)+7
        def heading(value):
            nonlocal y
            y=text_block(screen,value,x,y,width,font,ACCENT)+12
        def btn(key,label,action,active=False):
            nonlocal y
            r=pygame.Rect(x,y,width,32)
            app.btn(key,r,label,action,active,clip=clip)
            y+=40
        def numeric(key,label,value,action,step,low,high,hint=""):
            nonlocal y
            text(f"{label}: {value:g}")
            w=(width-8)//2
            app.btn(key+"_minus",pygame.Rect(x,y,w,28),f"− {step:g}",("adjust",action,-step,low,high),clip=clip)
            app.btn(key+"_plus",pygame.Rect(x+w+8,y,w,28),f"+ {step:g}",("adjust",action,step,low,high),clip=clip)
            y+=36
            if hint: text(hint,MUTED)
        if app.tab=="lesson":
            heading("Deney defteri")
            text("Hazır bir sahne seç. Her seçim yeni bir deney başlatır; sonuç dosyaları korunur.",MUTED)
            for i,lesson in enumerate(LESSONS,1):
                btn(f"lesson_{i}",f"{i}. {lesson['title']}",("lesson",i),app.sim.lesson==i)
            if app.sim.lesson:
                lesson=LESSONS[app.sim.lesson-1]
                heading(lesson["goal"])
                for i,step in enumerate(lesson["steps"],1): text(f"{i}. {step}")
                heading("Neden?")
                text(lesson["why"])
            text("Serbest sahne: Yeni düğmesi. Haritada seç; özellikleri değiştir; grafiği izle.",MUTED)
        elif app.tab=="log":
            heading(f"Olay geçmişi • {app.sim.alarm.total_events}")
            btn("filter_sensor",f"Sensör: {'Seçili' if app.filter_selected else 'Tümü'}",("filter_sensor",),app.filter_selected)
            btn("filter_kind",f"Tür: {app.filter_kind}",("filter_kind",))
            text("Alarm geçişleri kotadan bağımsız kaydedilir. Son 1000 olay burada; tam geçmiş sonuç dosyasında.",MUTED)
            notifications=[ev for ev in app.sim.alarm.notifications
                           if (not app.filter_selected or ev["sensor_id"]==app.selected_id)
                           and ev["kind"]=="REPEAT"]
            if notifications:
                heading("Son tekrar bildirimleri")
                for ev in list(reversed(notifications))[:5]:
                    text(f"{ev['t']:.2f}s  #{ev['sensor_id']}  {ev['channel']} • {ev['details']}",(255,188,106))
                heading("Durum geçişleri")
            events=[ev for ev in app.sim.alarm.events
                    if (not app.filter_selected or ev["sensor_id"]==app.selected_id)
                    and (app.filter_kind=="Tümü" or ev["kind"]==app.filter_kind)]
            for ev in reversed(events):
                value="" if ev["value"] is None else f" • {ev['value']:.2f}"
                text(f"{ev['t']:.2f}s  #{ev['sensor_id']}  {ev['channel']}  {ev['kind']}{value}\n{ev['details']}",
                     (255,149,151) if ev["kind"]=="ALERT" else TEXT)
            if not events: text("Filtreye uyan olay yok.",MUTED)
        else:
            e=app.selected
            if e is None:
                heading("Bir nesne seç")
                text("Üstte bir araç seçip haritaya tıklayarak ekle. Seç aracıyla mevcut nesneyi incele.")
                heading("Kısayollar")
                text("Space: başlat/duraklat\nN: tek örnekleme adımı\nM: seçiliyi taşı\nK: drone rotası\nDelete / sağ tık: sil\nCtrl+S / Ctrl+O: sahne kaydet/yükle\nTekerlek: yakınlaş\nOrta tuş sürükle: haritayı kaydır\nEsc: geçici işlemi iptal")
                text("Renkli alan, sensörün okuması değil simülatörün teorik alanıdır.",MUTED)
            else:
                heading(e.display_name)
                text(f"{e.kind.value} • ({e.tx}, {e.ty})"+(f" • Drone #{e.carried_by} üzerinde" if e.carried_by else ""),MUTED)
                btn("rename","İsmi değiştir",("rename",))
                if e.carried_by is None: btn("move","Haritada taşı (M)",("move",))
                if e.sensor:
                    s=e.sensor
                    heading(STATUS_LABELS.get(s.status,s.status))
                    btn("enabled","Sensör: "+("Açık" if s.enabled else "Kapalı"),("toggle","enabled"),s.enabled)
                    for mode in SensorMode:
                        btn("sensor_"+mode.value,mode.value+(" • ölçüyor" if mode in s.modes else " • kapalı"),("sensor_mode",mode),mode in s.modes)
                    numeric("interval","Örnek aralığı (s)",s.sample_interval,"sample_interval",.1,.1,60,"Kısa aralık: daha çok örnek, daha çok enerji.")
                    numeric("battery","Pil (eğitim birimi)",s.battery,"battery",25,0,1000000)
                    numeric("efficiency","Verimlilik (%)",s.efficiency,"efficiency",5,1,100)
                    numeric("noise","Gürültü (%)",s.noise_percent,"noise_percent",1,0,50)
                    channel=app.channel if app.channel!="BATTERY" else "TEMP"
                    heading(f"Kanal ayarı: {channel}")
                    text("Grafik kanal düğmeleriyle ayarlanacak kanalı seç.",MUTED)
                    numeric("offset","Kalibrasyon sapması",s.offsets[channel],"offsets."+channel,1 if channel=="TEMP" else 10,-100000,100000)
                    step=5 if channel in ("TEMP","CO") else 500
                    numeric("threshold","Alarm açılış eşiği",s.thresholds[channel],"thresholds."+channel,step,0,100000)
                    numeric("clear","Alarm kapanış eşiği",s.clear_thresholds[channel],"clear_thresholds."+channel,step,0,100000)
                    numeric("repeat","Tekrar bildirimi (s; 0=kapalı)",s.repeat_seconds,"repeat_seconds",1,0,300)
                    numeric("quota","60 s tekrar kotası",s.max_limit,"max_limit",5,0,200)
                    numeric("remaining","Kalan tekrar hakkı",s.limit,"limit",5,0,s.max_limit)
                    text(app.sim.alarm.get_limiter_info(e.id),MUTED)
                    if e.id in app.sim.alarm.limiter_exhausted: text("Tekrar bildirimi bastırılıyor; ölçüm ve alarm kaydı sürüyor.",(255,188,106))
                    for key,attr in VALUE_ATTR.items():
                        value=getattr(s,attr)
                        if value is not None: text(f"{key}: ölçüm {value:.2f} / teorik {s.theoretical.get(key,0):.2f}")
                elif e.source:
                    s=e.source
                    btn("source_type","Kaynak: "+s.stype.value,("source_type",))
                    if s.stype==SourceType.TEMP:
                        numeric("temperature","Kaynak sıcaklığı (°C)",s.temp_celcius,"temp_celcius",25,22,1500)
                        numeric("source_range","Yayılım yarıçapı (kare)",s.range_tiles,"range_tiles",1,1,80)
                    else:
                        if not s.gas_modes:
                            text("Yayılım için aşağıdan en az bir gaz kanalı aç.",MUTED)
                        for mode in GasMode:
                            key=mode.value.lower()
                            btn("gas_"+key,mode.value+(" • açık" if mode in s.gas_modes else " • kapalı"),("gas_mode",mode),mode in s.gas_modes)
                            if mode in s.gas_modes:
                                numeric(key+"_ppm",mode.value+" yoğunluğu (ppm)",getattr(s,key+"_ppm"),key+"_ppm",50 if key=="co" else 500,0,100000)
                                numeric(key+"_range",mode.value+" yarıçapı",getattr(s,key+"_range"),key+"_range",1,1,80)
                    numeric("visibility","Görsel görünürlük",s.power,"power",1,1,10,"Görsel ayar ölçümü değiştirmez.")
                    btn("effect","Kaynak görseli: "+("Açık" if e.show_effect else "Kapalı"),("entity_toggle","show_effect"),e.show_effect)
                elif e.uav:
                    u=e.uav
                    numeric("speed","Hız (kare/s)",u.speed,"speed",.5,1,10)
                    btn("route","Rota çiz / bitir (K)",("route",))
                    btn("route_mode","Rota: "+u.route_mode.value,("route_mode",))
                    btn("route_clear","Rotayı temizle",("route_clear",))
                    btn("route_visible","Rota görünümü",("toggle","show_route"),u.show_route)
                    text(f"{len(u.route)} durak • {len(u.carrying_ids)} yük",MUTED)
                    if u.blocked_reason: text(u.blocked_reason,(255,188,106))
                    btn("attach","Haritadan yük seç",("attach",))
                    btn("release","Tüm yükleri indir",("release",))
                    for cid in u.carrying_ids: btn(f"cargo_{cid}",f"Yük #{cid} özellikleri",("select",cid))
                else:
                    btn("flammable","Yanabilir: "+("Evet" if e.flammable else "Hayır"),("entity_toggle","flammable"),e.flammable)
                    numeric("ignition","Tutuşma sıcaklığı (°C)",e.ignition_temp,"ignition_temp",10,25,1500)
                    numeric("exposure","Gerekli maruz kalma (s)",e.ignition_seconds,"ignition_seconds",.5,.1,300)
                    text(f"Eşik üstünde geçen süre: {e.heat_seconds:.2f}s")
                btn("delete","Nesneyi sil",("delete",))
                text("Ölçüm ve yangın kuralları eğitim amaçlıdır. Değişiklikler sonuç klasörüne kaydedilir.",MUTED)
        self.bottom=max(0,y+self.scroll-clip.bottom+16)
        self.scroll=max(0,min(self.scroll,self.bottom))
        screen.set_clip(old)
        if self.bottom:
            bar=pygame.Rect(rect.right-7,clip.top,3,max(20,clip.height*clip.height/(clip.height+self.bottom)))
            bar.y+=round((clip.height-bar.height)*self.scroll/self.bottom)
            pygame.draw.rect(screen,ACCENT,bar,border_radius=2)
