"""SDL pencere denemesi, altı ekran ve sınırlı eğitim sahnesi performansı."""
import argparse
import hashlib
import json
import os
import platform
import resource
import statistics
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
os.environ.setdefault("SDL_AUDIODRIVER","dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT","1")
import pygame
from iot_sim.app import App
from iot_sim.models import *
from iot_sim.scene import to_scene
from iot_sim.lessons import lesson_scene
from iot_sim.render import FIELD_CACHE


def benchmark_scene():
    """30 sensör, 10 kaynak, 3 drone; öğretici ölçekte tekrarlanabilir yük."""
    entities=[]
    for i in range(30):
        entities.append(Entity(i+1,Kind.SENSOR,5+2*(i%10),6+2*(i//10),
                               sensor=SensorProps(),name=f"S{i+1}"))
    for i in range(10):
        entities.append(Entity(31+i,Kind.SOURCE,5+2*i,18,source=SourceProps()))
    for i in range(3):
        x=5+6*i
        entities.append(Entity(41+i,Kind.UAV,x,22,
            uav=UavProps(x=x,y=22,route=[(x,22),(x,26)])))
    return to_scene(entities)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    app=App(out_dir=args.output/"exports",size=(1280,800))
    app.toast=""
    report={"python":platform.python_version(),"pygame":pygame.version.ver,"platform":platform.platform(),
            "display_driver":pygame.display.get_driver(),"interactive_human_test":False}
    report["source_sha256"]={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted([*ROOT.glob("iot_sim/*.py"),ROOT/"CALCULATOR.py",ROOT/"main.py",Path(__file__).resolve()])}
    try:
        captures=[]
        for number in range(1,7):
            app.replace_sim(lesson_scene(number))
            app.tab="lesson"
            app.begin_recording()
            app.sim.advance(10)
            app.show_field=True
            app.toast=""
            app.draw()
            path=args.output/f"deney-{number}.png"
            pygame.image.save(app.screen,path)
            captures.append(dict(lesson=number,seconds=app.sim.time,events=app.sim.alarm.total_events,
                                 samples=sum(len(h) for h in app.sim.history.values()),image=path.name))
        report["lessons"]=captures
        app.replace_sim(benchmark_scene())
        app.tab="properties"
        app.show_field=True
        app.focus_scene()
        durations=[]
        for _ in range(150):
            start=time.perf_counter()
            app.sim.advance(1/30)
            app.draw()
            pygame.event.pump()
            durations.append((time.perf_counter()-start)*1000)
        report["benchmark"]={"sensors":30,"sources":10,"drones":3,"frames":150,
            "includes_model_and_drawing":True,"theoretical_layer":True,
            "median_ms":statistics.median(durations),"p95_ms":sorted(durations)[int(len(durations)*.95)],
            "max_ms":max(durations),"cache_bytes":FIELD_CACHE.bytes,"cache_limit_bytes":FIELD_CACHE.limit}
        for e in app.sim.entities:
            if e.source: e.source.range_tiles=80
        app.sim.revision+=1
        app.cam.zoom=3.5
        start=time.perf_counter()
        app.draw()
        report["maximum_radius"]={"source_range":80,"zoom":3.5,"frame_ms":(time.perf_counter()-start)*1000,
                                 "cache_bytes":FIELD_CACHE.bytes}
        assert FIELD_CACHE.bytes<=FIELD_CACHE.limit
        report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
        pygame.image.save(app.screen,args.output/"kalabalik-sahne.png")
    finally:
        app.close_recording()
        pygame.quit()
    (args.output/"runtime.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
