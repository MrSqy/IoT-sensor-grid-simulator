"""Başlangıç davranışları değil, onaylı kuralları doğrulayan regresyonlar."""
import copy
import csv
import json
import math
from pathlib import Path
import tempfile
import unittest
from iot_sim.models import *
from iot_sim.simulation import Simulation
from iot_sim.scene import to_scene, parse_scene, load_scene, save_scene
from iot_sim.lessons import lesson_scene
from iot_sim.sensors import field_at, simulate_tick, invalidate
from iot_sim.alarm_bridge import AlarmBridge
from iot_sim.engine import route_is_valid
from iot_sim.uav import update_uavs
from iot_sim import operations
from iot_sim.exporter import Exporter
from iot_sim.fire import spread_fire


class MeasurementTests(unittest.TestCase):
    def test_point_measurement_has_no_distance_cutoff(self):
        s=Entity(1,Kind.SENSOR,0,0,sensor=SensorProps(noise_percent=0,range_tiles=1))
        src=Entity(2,Kind.SOURCE,16,0,source=SourceProps(range_tiles=80))
        simulate_tick([s,src],1)
        self.assertAlmostEqual(s.sensor.last_temp,field_at(0,0,[src])["TEMP"])
        self.assertGreater(s.sensor.last_temp,22)
        before=s.sensor.last_temp
        s.sensor.range_tiles=50
        src.source.power=10
        simulate_tick([s,src],1)
        self.assertEqual(before,s.sensor.last_temp)

    def test_channels_and_calibration(self):
        e=Entity(1,Kind.SENSOR,0,0,sensor=SensorProps(noise_percent=0,modes={SensorMode.TEMP}))
        e.sensor.offsets["TEMP"]=7
        simulate_tick([e],1)
        self.assertEqual(e.sensor.last_temp,29)
        self.assertIsNone(e.sensor.last_co)

    def test_energy_frequency_and_channels(self):
        results=[]
        for channels,interval in [({SensorMode.TEMP},1), (set(SensorMode),1), ({SensorMode.TEMP},.5)]:
            s=SensorProps(modes=channels,sample_interval=interval)
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=s)]))
            sim.advance(10)
            results.append(sim.entities[0].sensor.battery)
        self.assertGreater(results[0],results[1])
        self.assertGreater(results[0],results[2])

    def test_empty_and_off_are_not_zero_normal(self):
        for props,state in [(SensorProps(battery=0),"EMPTY"),(SensorProps(enabled=False),"OFF"),(SensorProps(modes=set()),"OFF")]:
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=props)]))
            sim.advance(1)
            s=sim.entities[0].sensor
            self.assertEqual(s.status,state)
            self.assertIsNone(s.last_temp)
            self.assertFalse(s.valid)

    def test_carried_sensor_is_logged_and_alerts(self):
        sim=Simulation(lesson_scene(5))
        sim.advance(4)
        self.assertGreater(len(sim.history[2]),0)
        self.assertIn(2,sim.alarm.active_alerts)
        self.assertGreater(sim.entities[1].sensor.last_temp,60)


class AlarmTests(unittest.TestCase):
    def make(self,channel,value,limit=40):
        s=SensorProps(modes={SensorMode(channel)},valid=True,limit=limit,max_limit=40)
        setattr(s,{"TEMP":"last_temp","CO":"last_co","CO2":"last_co2","H2":"last_h2"}[channel],value)
        return Entity(1,Kind.SENSOR,0,0,sensor=s)

    def test_all_threshold_boundaries_agree(self):
        thresholds={"TEMP":60,"CO":35,"CO2":5000,"H2":4000}
        for channel,threshold in thresholds.items():
            for value,alarm in [(threshold-.01,False),(threshold,True),(threshold+.01,True)]:
                with self.subTest(channel=channel,value=value):
                    e=self.make(channel,value)
                    b=AlarmBridge()
                    b.update([e],0)
                    self.assertEqual(e.sensor.status=="ALERT",alarm)
                    self.assertEqual(any(ev["kind"]=="ALERT" for ev in b.events),alarm)

    def test_hysteresis_and_transition_only(self):
        e=self.make("TEMP",60)
        b=AlarmBridge()
        b.update([e],0)
        n=b.total_events
        e.sensor.last_temp=57
        b.update([e],1)
        self.assertEqual(n,b.total_events)
        self.assertEqual(e.sensor.status,"ALERT")
        e.sensor.last_temp=54.9
        b.update([e],2)
        self.assertEqual(e.sensor.status,"NORMAL")
        self.assertEqual(sum(ev["kind"]=="CALM" for ev in b.events),1)

    def test_zero_repeat_quota_preserves_measurements_events(self):
        e=self.make("TEMP",70,limit=0)
        e.sensor.repeat_seconds=1
        b=AlarmBridge()
        b.update([e],0)
        b.update([e],1)
        self.assertEqual(e.sensor.limit,0)
        self.assertEqual(e.sensor.status,"ALERT")
        self.assertEqual(len(b.notifications),1)  # ilk geçiş sınırlanmaz
        e.sensor.last_temp=40
        b.update([e],2)
        self.assertTrue(any(ev["kind"]=="CALM" for ev in b.events))
        b.update([e],60)
        self.assertEqual(e.sensor.limit,40)

    def test_removed_sensor_state_is_pruned(self):
        e=self.make("TEMP",80)
        b=AlarmBridge()
        b.update([e],0)
        b.update([],1)
        self.assertEqual(b.alert_count,0)
        self.assertFalse(b.slots)


class ClockRegressionTests(unittest.TestCase):
    def test_fire_timestamp_without_sensor_samples(self):
        source=Entity(1,Kind.SOURCE,1,1,source=SourceProps())
        tree=Entity(2,Kind.OBSTACLE,2,1,ignition_seconds=.15)
        sim=Simulation(to_scene([source,tree]))
        sim.advance(.15)
        fire=next(ev for ev in sim.alarm.events if ev["kind"]=="FIRE")
        self.assertEqual(fire["t"],.15)

    def test_repeats_follow_clock_between_measurements(self):
        sensor=SensorProps(modes={SensorMode.TEMP},noise_percent=0,sample_interval=10,
                           repeat_seconds=1,limit=5,max_limit=5)
        sensor.thresholds["TEMP"]=sensor.clear_thresholds["TEMP"]=0
        sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=sensor)]))
        sim.advance(13)
        repeats=[ev["t"] for ev in sim.alarm.notifications if ev["kind"]=="REPEAT"]
        self.assertEqual(repeats,[11,12,13])
        self.assertEqual(len(sim.history[1]),1)
        self.assertEqual(sim.entities[0].sensor.limit,2)


class DroneTests(unittest.TestCase):
    def sim(self):
        return Simulation(lesson_scene(5))

    def test_degenerate_route_returns(self):
        for mode in RouteMode:
            u=Entity(1,Kind.UAV,2,2,uav=UavProps(x=2,y=2,route=[(2,2),(2,2)],route_mode=mode))
            update_uavs([u],.05,200,200)
            self.assertTrue(u.uav.blocked_reason)

    def test_loop_closure_and_approach(self):
        self.assertFalse(route_is_valid([(2,2),(2,4),(4,4)],{(3,3)}))
        sim=self.sim()
        sim.entities.append(Entity(9,Kind.OBSTACLE,8,12))
        with self.assertRaises(ValueError):
            operations.set_route(sim,sim.entities[0],[(9,12),(12,12)])
        old=(sim.entities[0].uav.x,sim.entities[0].uav.y)
        sim.advance(1)
        self.assertEqual(old,(sim.entities[0].uav.x,sim.entities[0].uav.y))
        self.assertTrue(sim.entities[0].uav.blocked_reason)

    def test_move_and_delete_keep_cargo_consistent(self):
        sim=self.sim()
        drone,sensor=sim.entities[:2]
        drone.uav.route=[]
        operations.move_entity(sim,drone.id,2,2)
        self.assertEqual((sensor.tx,sensor.ty),(2,2))
        operations.delete_entity(sim,drone.id)
        self.assertIsNone(sensor.carried_by)
        self.assertNotEqual((sensor.tx,sensor.ty),(sim.entities[-1].tx,sim.entities[-1].ty))
        parse_scene(sim.snapshot())

    def test_release_is_atomic_when_full(self):
        s=Entity(2,Kind.SENSOR,0,0,sensor=SensorProps(),carried_by=1)
        u=Entity(1,Kind.UAV,0,0,uav=UavProps(x=0,y=0,carrying_ids=[2]))
        entities=[u,s]+[Entity(3+i,Kind.OBSTACLE,x,y) for i,(x,y) in enumerate([(0,1),(1,0),(1,1)])]
        sim=Simulation(to_scene(entities,width=2,height=2))
        before=sim.snapshot()
        with self.assertRaises(ValueError): operations.release_cargo(sim,sim.entities[0])
        self.assertEqual(before,sim.snapshot())

    def test_capacity_and_mixed_load(self):
        sim=Simulation(to_scene([]))
        drone=operations.add_entity(sim,Kind.UAV,0,0)
        s=operations.add_entity(sim,Kind.SENSOR,1,0)
        source=operations.add_entity(sim,Kind.SOURCE,2,0)
        operations.attach(sim,drone.id,s.id)
        with self.assertRaises(ValueError): operations.attach(sim,drone.id,source.id)


class SceneLimitTests(unittest.TestCase):
    def test_entity_limit_rejects_edit_without_mutation(self):
        entities=[Entity(i+1,Kind.OBSTACLE,i%25,i//25) for i in range(500)]
        sim=Simulation(to_scene(entities))
        before=sim.snapshot()
        with self.assertRaises(ValueError): operations.add_entity(sim,Kind.SENSOR,100,100)
        self.assertEqual(sim.snapshot(),before)
        self.assertEqual(sim.next_id,501)

    def test_entity_id_limit_rejects_edit(self):
        sim=Simulation(to_scene([Entity(10**9,Kind.OBSTACLE,0,0)]))
        with self.assertRaises(ValueError): operations.add_entity(sim,Kind.SENSOR,1,0)
        self.assertEqual(len(sim.entities),1)

    def test_route_limit_preserves_old_route(self):
        sim=Simulation(lesson_scene(5))
        drone=sim.entities[0]
        old=list(drone.uav.route)
        with self.assertRaises(ValueError): operations.set_route(sim,drone,[(7,12),(18,12)]*251)
        self.assertEqual(drone.uav.route,old)

    def test_oversized_save_preserves_existing_file(self):
        large=to_scene([Entity(i+1,Kind.UAV,i,1,
                       uav=UavProps(x=i,y=1,route=[(0,0),(1,0)]*250)) for i in range(100)])
        self.assertGreater(len(json.dumps(large,ensure_ascii=False,indent=2).encode("utf-8")),2_000_000)
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"scene.json"
            initial=lesson_scene(1)
            save_scene(path,initial)
            before=path.read_bytes()
            with self.assertRaises(ValueError): save_scene(path,large)
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(load_scene(path),initial)
            self.assertEqual(len(list(Path(tmp).iterdir())),1)


class TimeAndSceneTests(unittest.TestCase):
    def test_lessons_demonstrate_promised_relationships(self):
        distance=Simulation(lesson_scene(1));distance.advance(1)
        self.assertGreater(distance.entities[0].sensor.last_temp,distance.entities[1].sensor.last_temp)
        noisy=Simulation(lesson_scene(2))
        noisy.entities[0].sensor.noise_percent=0
        noisy.advance(1)
        baseline=noisy.entities[0].sensor.last_temp
        noisy.entities[0].sensor.offsets["TEMP"]=10
        noisy.advance(1)
        self.assertAlmostEqual(noisy.entities[0].sensor.last_temp,baseline+10)
        battery=Simulation(lesson_scene(3));battery.advance(10)
        self.assertEqual(battery.entities[1].sensor.status,"EMPTY")
        self.assertEqual(battery.entities[0].sensor.status,"NORMAL")
        gas=Simulation(lesson_scene(4));gas.entities[0].sensor.noise_percent=0;gas.advance(1)
        co=gas.entities[0].sensor.last_co
        self.assertEqual(gas.entities[0].sensor.last_co2,0)
        gas.entities[1].source.gas_modes.add(GasMode.CO2);gas.advance(1)
        self.assertEqual(gas.entities[0].sensor.last_co,co)
        self.assertGreater(gas.entities[0].sensor.last_co2,0)
        moving=Simulation(lesson_scene(5));moving.advance(6)
        self.assertGreater(len({r["measured"]["TEMP"] for r in moving.history[2]}),1)
        fire=Simulation(lesson_scene(6));fire.advance(4)
        self.assertEqual(fire.entities[1].kind,Kind.BURNED)
        self.assertEqual(fire.entities[2].kind,Kind.OBSTACLE)

    def test_scene_can_capture_drone_crossing_ground_sensor(self):
        drone=Entity(1,Kind.UAV,2,2,uav=UavProps(x=2,y=2))
        sensor=Entity(2,Kind.SENSOR,2,2,sensor=SensorProps())
        scene=to_scene([drone,sensor])
        parse_scene(scene)

    def test_frame_partition_and_seed_reproduce_all_history(self):
        a,b=Simulation(lesson_scene(2)),Simulation(lesson_scene(2))
        a.advance(10)
        for _ in range(400): b.advance(.025)
        self.assertEqual(a.time,b.time)
        self.assertEqual(list(a.history[1]),list(b.history[1]))
        self.assertEqual(list(a.alarm.events),list(b.alarm.events))
        c=a.reset();c.advance(10)
        self.assertEqual(list(a.history[1]),list(c.history[1]))

    def test_all_lessons_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            for n in range(1,7):
                scene=lesson_scene(n)
                path=Path(tmp)/f"{n}.json"
                save_scene(path,scene)
                sim=Simulation(load_scene(path))
                self.assertEqual(scene,sim.snapshot())
                sim.advance(10)

    def test_reject_corrupt_scene_without_mutation(self):
        sim=Simulation(lesson_scene(1));before=sim.snapshot()
        changes=[lambda d:d.update(schema_version=999), lambda d:d.update(seed=float("nan")),
                 lambda d:d["entities"].append(copy.deepcopy(d["entities"][0])),
                 lambda d:d["entities"][0]["sensor"].update(sample_interval=0),
                 lambda d:d["entities"][0].update(carried_by=987),
                 lambda d:d["entities"][0]["sensor"]["clear_thresholds"].update(TEMP=900),
                 lambda d:d["entities"][0].update(tx=-1)]
        for change in changes:
            data=copy.deepcopy(before);change(data)
            with self.assertRaises(ValueError): parse_scene(data)
            self.assertEqual(sim.snapshot(),before)

    def test_speed_and_interval_partition(self):
        references=[]
        for speed in (.25,1,2,5):
            sim=Simulation(lesson_scene(5))
            for _ in range(round(4/(.01*speed))): sim.advance(.01*speed)
            references.append((sim.time,list(sim.history[2])))
        self.assertTrue(all(item==references[0] for item in references))


class ExportAndFireTests(unittest.TestCase):
    def test_unique_sessions_complete_data_and_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            scene=lesson_scene(5)
            with Exporter(tmp,tag="same",scene=scene) as a, Exporter(tmp,tag="same",scene=scene) as b:
                self.assertNotEqual(a.directory,b.directory)
                sim=Simulation(scene);sim.start_recording(a);sim.advance(2)
                a.log_change(sim.time,"test",sim.snapshot())
            with a.csv_path.open() as f:
                rows=list(csv.DictReader(f))
            self.assertEqual(len(rows),8)
            self.assertTrue(all(r["carried_by"]=="1" for r in rows))
            self.assertEqual(json.loads((a.directory/"experiment.json").read_text())["scene"],scene)
            self.assertEqual(len(a.actions_path.read_text().splitlines()),1)
            self.assertTrue(a.closed)

    def test_invalid_measurements_are_blank(self):
        with tempfile.TemporaryDirectory() as tmp:
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=SensorProps(battery=0))]))
            with Exporter(tmp,scene=sim.snapshot()) as exporter:
                sim.start_recording(exporter);sim.advance(1)
            with exporter.csv_path.open() as f:
                rows=list(csv.DictReader(f))
            self.assertTrue(all(r["measured"]=="" and r["valid"]=="0" and r["status"]=="EMPTY" for r in rows))

    def test_exception_closes_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            exporter=None
            with self.assertRaises(RuntimeError):
                with Exporter(tmp) as exporter: raise RuntimeError("deneme")
            self.assertTrue(exporter.closed)

    def test_ignition_needs_heat_time_and_flammability(self):
        sim=Simulation(lesson_scene(6))
        sim.advance(2.95)
        self.assertEqual(sim.entities[1].kind,Kind.OBSTACLE)
        sim.advance(.05)
        self.assertEqual(sim.entities[1].kind,Kind.BURNED)
        self.assertEqual(sim.entities[2].kind,Kind.OBSTACLE)

    def test_cool_source_does_not_ignite(self):
        sim=Simulation(lesson_scene(6))
        sim.entities[0].source.temp_celcius=50
        sim.advance(10)
        self.assertTrue(all(e.kind==Kind.OBSTACLE for e in sim.entities[1:3]))


if __name__=="__main__":
    unittest.main()
