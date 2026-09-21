"""Pygame'in gerçek çizim ve olay işleyicisini kontrollü SDL girdileriyle sınar."""
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
os.environ.setdefault("SDL_VIDEODRIVER","dummy")
os.environ.setdefault("SDL_AUDIODRIVER","dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT","1")
try:
    import pygame
except ImportError:
    raise unittest.SkipTest("Grafik testleri için requirements.txt kurulmalı.")
from iot_sim.app import App
from iot_sim.lessons import lesson_scene
from iot_sim.scene import to_scene,parse_scene
from iot_sim.models import *


class UITests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.app=App(out_dir=self.tmp.name,size=(1024,720))
        self.app.toast=""
        self.app.draw()

    def tearDown(self):
        self.app.close_recording()
        pygame.quit()
        self.tmp.cleanup()

    def click(self,key):
        for _ in range(25):
            self.app.draw()
            if key in self.app.buttons: break
            self.app.inspector.scroll=min(self.app.inspector.bottom,self.app.inspector.scroll+200)
        self.assertIn(key,self.app.buttons)
        rect,_=self.app.buttons[key]
        pos=rect.center
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=1,pos=pos))

    def mapclick(self,x,y,button=1):
        self.app.draw()
        pos=self.app.cam.world_to_screen(x+.5,y+.5)
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=button,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=button,pos=pos))

    def key(self,key):
        self.app.process_event(pygame.event.Event(pygame.KEYDOWN,key=key,unicode="",mod=0))

    def test_all_lessons_graphs_and_resizing(self):
        for n in range(1,7):
            self.app.action(("tab","lesson"))
            self.click("lesson_"+str(n))
            self.assertEqual(self.app.sim.lesson,n)
            self.click("step")
            self.app.sim.advance(9)
            for channel in ("TEMP","CO","CO2","H2","BATTERY"):
                self.click("channel_"+channel)
                self.app.draw()
            self.app.process_event(pygame.event.Event(pygame.VIDEORESIZE,w=1280,h=800))
            self.app.draw()
            self.assertTrue(self.app.screen.get_rect().contains(self.app.panel_rect))
            self.assertTrue(self.app.screen.get_rect().contains(self.app.graph_rect))

    def test_editor_and_actual_event_coordinates(self):
        self.click("new")
        self.click("tool_sensor")
        self.mapclick(100,100)
        self.assertEqual(len(self.app.sim.entities),1)
        sensor=self.app.selected
        self.assertEqual((sensor.tx,sensor.ty),(100,100))
        self.key(pygame.K_m)
        self.mapclick(101,101)
        self.assertEqual((sensor.tx,sensor.ty),(101,101))
        self.click("rename")
        self.app.input_text="Öğretici sensör"
        self.key(pygame.K_RETURN)
        self.assertEqual(sensor.name,"Öğretici sensör")
        self.key(pygame.K_DELETE)
        self.assertFalse(self.app.sim.entities)

    def test_right_click_and_del_both_release(self):
        for key_delete in (False,True):
            self.app.replace_sim(lesson_scene(5))
            drone=self.app.sim.entities[0]
            if key_delete:
                self.app.selected_id=drone.id
                self.key(pygame.K_DELETE)
            else:
                self.mapclick(drone.tx,drone.ty,3)
            sensor=next(e for e in self.app.sim.entities if e.sensor)
            self.assertIsNone(sensor.carried_by)
            self.assertIsNone(next((e for e in self.app.sim.entities if e.uav),None))
            parse_scene(self.app.sim.snapshot())

    def test_drag_drop_sensor_to_drone_panel(self):
        scene=to_scene([Entity(1,Kind.UAV,10,10,uav=UavProps(x=10,y=10)),
                        Entity(2,Kind.SENSOR,12,10,sensor=SensorProps())])
        self.app.replace_sim(scene)
        self.app.selected_id=1
        self.app.draw()
        pos=self.app.cam.world_to_screen(12.5,10.5)
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEMOTION,pos=self.app.panel_rect.center,rel=(50,0),buttons=(1,0,0)))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=1,pos=self.app.panel_rect.center))
        self.assertEqual(self.app.sim.entities[1].carried_by,1)
        self.assertEqual(self.app.sim.entities[0].uav.carrying_ids,[2])

    def test_route_keyboard_and_cancel(self):
        self.app.replace_sim(lesson_scene(5))
        self.app.selected_id=1
        self.key(pygame.K_k)
        self.mapclick(7,10)
        self.mapclick(9,10)
        self.key(pygame.K_k)
        self.assertEqual(self.app.sim.entities[0].uav.route,[(7,10),(9,10)])
        self.key(pygame.K_k)
        self.mapclick(7,10)
        self.mapclick(7,10)
        self.assertEqual(len(self.app.route_points),1)
        self.key(pygame.K_ESCAPE)
        self.assertEqual(self.app.sim.entities[0].uav.route,[(7,10),(9,10)])

    def test_save_load_seed_invalid_load_preserves_scene(self):
        path=Path(self.tmp.name)/"sahne.json"
        self.click("save")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertTrue(path.exists())
        before=self.app.sim.snapshot()
        self.click("new")
        self.click("load")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.snapshot(),before)
        path.write_text('{"schema_version": 999}')
        self.click("load")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.snapshot(),before)
        self.key(pygame.K_ESCAPE)
        self.click("seed")
        self.app.input_text="123"
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.seed,123)

    def test_panel_controls_and_filters(self):
        self.app.selected_id=1
        self.app.tab="properties"
        before=self.app.selected.sensor.battery
        self.click("battery_plus")
        self.assertGreater(self.app.selected.sensor.battery,before)
        self.click("noise_plus")
        self.assertEqual(self.app.selected.sensor.noise_percent,1)
        self.click("step")
        self.click("tab_log")
        self.click("filter_sensor")
        self.click("filter_kind")
        self.assertTrue(self.app.filter_selected)
        self.assertEqual(self.app.filter_kind,"ALERT")
        self.app.draw()

    def test_source_fire_and_alarm_controls(self):
        self.app.replace_sim(lesson_scene(4))
        self.app.selected_id=3;self.app.tab="properties"
        self.click("gas_co2")
        self.assertIn(GasMode.CO2,self.app.selected.source.gas_modes)
        before=self.app.selected.source.co2_ppm
        self.click("co2_ppm_plus")
        self.assertGreater(self.app.selected.source.co2_ppm,before)
        self.app.selected_id=1;self.app.inspector.scroll=0
        self.click("channel_CO2")
        self.click("threshold_minus")
        self.assertEqual(self.app.selected.sensor.thresholds["CO2"],4500)
        self.click("clear_plus")
        self.assertLessEqual(self.app.selected.sensor.clear_thresholds["CO2"],4500)
        self.app.replace_sim(lesson_scene(6))
        self.app.selected_id=1;self.app.tab="properties"
        self.click("flammable")
        self.assertFalse(self.app.selected.flammable)
        self.click("ignition_plus")
        self.assertEqual(self.app.selected.ignition_temp,130)

    def test_exception_path_closes_exporter(self):
        self.app.action(("play",))
        exporter=self.app.exporter
        with patch.object(self.app.sim,"advance",side_effect=RuntimeError("injected")):
            with self.assertRaises(RuntimeError): self.app.run(max_frames=2)
        self.assertTrue(exporter.closed)


if __name__=="__main__":
    unittest.main()
