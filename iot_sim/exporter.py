"""Her deney için ayrı, üzerine yazılmayan sonuç klasörü."""
import csv
import json
import tempfile
from contextlib import ExitStack
from datetime import datetime
from pathlib import Path
from .sensors import VALUE_ATTR, position
from .scene import MODEL_VERSION

ROOT = Path(__file__).resolve().parent.parent


class Exporter:
    def __init__(self, out_dir=None, tag=None, scene=None):
        root = Path(out_dir) if out_dir is not None else ROOT / "exports"
        root.mkdir(parents=True, exist_ok=True)
        self.directory = Path(tempfile.mkdtemp(prefix=datetime.now().strftime("%Y%m%d_%H%M%S_"), dir=root))
        self.stack = ExitStack()
        self.streams = []
        self.closed = False
        self.rows = 0
        try:
            self.csv_path = self.directory / "sensor_log.csv"
            self.alarm_path = self.directory / "alarm_log.csv"
            self.actions_path = self.directory / "changes.jsonl"
            self._sensor = self._writer(self.csv_path, ["t", "sensor_id", "sensor_name", "x", "y", "carried_by",
                "channel", "valid", "status", "measured", "theoretical", "battery", "threshold", "clear_threshold"])
            self._alarm = self._writer(self.alarm_path, ["t", "sensor_id", "sensor_name", "channel", "kind", "value", "details"])
            self._actions = self.stack.enter_context(self.actions_path.open("x", encoding="utf-8"))
            self.streams.append(self._actions)
            metadata = {"schema_version": 2, "model_version": MODEL_VERSION, "scene": scene,
                        "units": {"TEMP": "°C", "CO": "ppm", "CO2": "ppm", "H2": "ppm", "battery": "eğitim enerji birimi"}}
            (self.directory / "experiment.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False))
        except Exception:
            self.stack.close()
            raise

    def _writer(self, path, fields):
        f = self.stack.enter_context(path.open("x", newline="", encoding="utf-8"))
        self.streams.append(f)
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        return writer

    def log_sensor(self, sim_time, entity, entities=None):
        s = entity.sensor
        x, y = position(entity, entities or [entity])
        for channel, attr in VALUE_ATTR.items():
            value = getattr(s, attr)
            valid = s.valid and value is not None
            self._sensor.writerow(dict(t=round(sim_time, 6), sensor_id=entity.id, sensor_name=entity.name,
                x=x, y=y, carried_by=entity.carried_by, channel=channel, valid=int(valid), status=s.status,
                measured=value if valid else "", theoretical=s.theoretical.get(channel) if valid else "",
                battery=s.battery, threshold=s.thresholds[channel], clear_threshold=s.clear_thresholds[channel]))
        self.rows += 1
        if self.rows % 20 == 0:
            self.flush()

    def log_event(self, event):
        self._alarm.writerow(event)
        self.flush()

    def log_change(self, sim_time, action, scene):
        self._actions.write(json.dumps(dict(t=round(sim_time, 6), action=action, scene=scene),
                                       ensure_ascii=False, allow_nan=False) + "\n")
        self.flush()

    def flush(self):
        for stream in self.streams:
            if not stream.closed:
                stream.flush()

    def close(self):
        if not self.closed:
            self.stack.close()
            self.closed = True
        return self.directory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()
