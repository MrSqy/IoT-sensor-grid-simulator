"""Sınırlı geçmişten birimleri ayrı canlı kanal ve pil grafiği."""
import pygame
from .ui_widgets import TEXT,MUTED,ACCENT,BORDER


def draw_graph(screen, rect, history, channel, font, theory=True):
    """Boş/kapalı örneklerde çizgiyi kes; olay anları ve eşik geçmişini çiz."""
    pygame.draw.rect(screen,(19,29,41),rect,border_radius=12)
    unit="enerji" if channel=="BATTERY" else "°C" if channel=="TEMP" else "ppm"
    label=f"{channel} • {unit}    Ölçüm / pil"
    if theory and channel!="BATTERY": label+="    Teorik + eşik"
    screen.blit(font.render(label,True,TEXT),(rect.x+14,rect.y+10))
    if not history:
        screen.blit(font.render("Başlat veya Tek adım ile ilk örneği al.",True,MUTED),(rect.x+14,rect.y+48))
        return
    rows=list(history)[-180:]
    values=[]
    for row in rows:
        if channel=="BATTERY": values.append(row["battery"])
        else:
            for key in ("measured","theoretical" if theory else "measured","thresholds"):
                v=row[key].get(channel)
                if v is not None: values.append(v)
    if not values: values=[0,1]
    low,high=min(values),max(values)
    margin=max(1,(high-low)*.12)
    low,high=low-margin,high+margin
    plot=pygame.Rect(rect.x+57,rect.y+39,max(40,rect.width-78),max(30,rect.height-67))
    t0,t1=rows[0]["t"],max(rows[-1]["t"],rows[0]["t"]+1)
    def point(t,value):
        return (round(plot.left+(t-t0)/(t1-t0)*plot.width),round(plot.bottom-(value-low)/(high-low)*plot.height))
    for i in range(3):
        value=low+(high-low)*i/2
        y=point(t0,value)[1]
        pygame.draw.line(screen,BORDER,(plot.left,y),(plot.right,y))
        screen.blit(font.render(f"{value:.0f}",True,MUTED),(rect.x+8,y-7))
    keys=[("battery",ACCENT)] if channel=="BATTERY" else [("measured",ACCENT),("thresholds",(235,182,98))]
    if theory and channel!="BATTERY": keys.append(("theoretical",(129,154,234)))
    for key,color in keys:
        previous=None
        for row in rows:
            value=row["battery"] if key=="battery" else row[key].get(channel)
            if value is None:
                previous=None
                continue
            p=point(row["t"],value)
            if previous: pygame.draw.line(screen,color,previous,p,2 if key=="measured" else 1)
            else: pygame.draw.circle(screen,color,p,2)
            previous=p
    last=False
    for row in rows:
        active=channel in row["alarms"]
        if active!=last:
            x=point(row["t"],low)[0]
            pygame.draw.line(screen,(150,71,87),(x,plot.top),(x,plot.bottom),1)
        last=active
    screen.blit(font.render(f"{t0:.1f}s",True,MUTED),(plot.left,plot.bottom+7))
    end=font.render(f"{rows[-1]['t']:.1f}s",True,MUTED)
    screen.blit(end,(plot.right-end.get_width(),plot.bottom+7))
