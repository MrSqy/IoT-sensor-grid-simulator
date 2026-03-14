# iot_sim/exporter.py
import os, csv, time, json

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def timestamp_tag():
    return time.strftime("%Y%m%d_%H%M%S")

class Exporter:
    def __init__(self, out_dir="exports", tag=None):
        ensure_dir(out_dir)
        if tag is None:
            tag = timestamp_tag()

        self.csv_path = os.path.join(out_dir, f"sensor_log_{tag}.csv")
        self.poly_path = os.path.join(out_dir, f"threat_polygons_{tag}.jsonl")
        self.alarm_path = os.path.join(out_dir, f"alarm_log_{tag}.csv")

        self._csv_f = open(self.csv_path, "w", newline="", encoding="utf-8")
        self._csv_w = csv.DictWriter(self._csv_f, fieldnames=[
            "t", "sensor_id", "sensor_name", "sx", "sy",
            "modes",
            "temp_c", "co_ppm", "co2_ppm", "h2_ppm", "gas_total_ppm",
            "battery", "active", "efficiency", "range_tiles",
            "limit", "max_limit",
            "threat_active", "threat_area", "threat_points_count"
        ])
        self._csv_w.writeheader()

        self._poly_f = open(self.poly_path, "w", encoding="utf-8")

        self._alarm_f = open(self.alarm_path, "w", newline="", encoding="utf-8")
        self._alarm_w = csv.DictWriter(self._alarm_f, fieldnames=[
            "t", "sensor_id", "sensor_name", "alert_type", "details"
        ])
        self._alarm_w.writeheader()

    def log_sensor(self, sim_time: float, sensor_entity):
        s = sensor_entity.sensor
        threat_points = getattr(s, "threat_points", []) or []
        threat_area = float(getattr(s, "threat_area", 0.0))
        threat_active = bool(getattr(s, "threat_active", False))

        modes = getattr(s, "modes", set())
        modes_str = ",".join(sorted(m.value for m in modes)) if modes else ""

        self._csv_w.writerow({
            "t": round(sim_time, 3),
            "sensor_id": sensor_entity.id,
            "sensor_name": getattr(sensor_entity, "name", ""),
            "sx": sensor_entity.tx,
            "sy": sensor_entity.ty,
            "modes": modes_str,
            "temp_c": round(float(getattr(s, "last_temp", 0.0)), 2),
            "co_ppm": round(float(getattr(s, "last_co", 0.0)), 2),
            "co2_ppm": round(float(getattr(s, "last_co2", 0.0)), 2),
            "h2_ppm": round(float(getattr(s, "last_h2", 0.0)), 2),
            "gas_total_ppm": round(float(getattr(s, "last_gas", 0.0)), 2),
            "battery": round(float(getattr(s, "battery", 0.0)), 1),
            "active": int(bool(getattr(s, "active", True))),
            "efficiency": int(getattr(s, "efficiency", 100)),
            "range_tiles": int(getattr(s, "range_tiles", 0)),
            "limit": int(getattr(s, "limit", 0)),
            "max_limit": int(getattr(s, "max_limit", 40)),
            "threat_active": int(threat_active),
            "threat_area": round(threat_area, 6),
            "threat_points_count": len(threat_points),
        })

        if threat_active and len(threat_points) >= 3:
            rec = {
                "t": round(sim_time, 3),
                "sensor_id": sensor_entity.id,
                "sensor_pos": [sensor_entity.tx, sensor_entity.ty],
                "vertices": [[float(x), float(y)] for (x, y) in threat_points],
                "area": threat_area,
            }
            self._poly_f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def log_alarm(self, sim_time: float, sensor_entity, alert_type: str, details: str):
        """Alarm olaylarını ayrı CSV'ye kaydet."""
        self._alarm_w.writerow({
            "t": round(sim_time, 3),
            "sensor_id": sensor_entity.id,
            "sensor_name": getattr(sensor_entity, "name", ""),
            "alert_type": alert_type,
            "details": details,
        })

    def close(self):
        self._csv_f.close()
        self._poly_f.close()
        self._alarm_f.close()
        return self.csv_path, self.poly_path, self.alarm_path