import json
import sys
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json

file_name = Path(sys.argv[1]).resolve()
with file_name.open(encoding="utf-8") as f:
    data: dict = simdjson.load(f)  # type: ignore

if not data:
    sys.exit()

file_name_base = file_name.stem
packets = [i for i in data.get("packets_and_frames", []) if i["type"] == "packet"]
frames = [i for i in data.get("packets_and_frames", []) if i["type"] == "frame"]


def write_json_file(file_name: Path, data_dict: dict) -> None:
    with file_name.open("w", encoding="utf-8") as fp:
        json_string = json.dumps(data_dict, indent="\t", separators=(",", ":"))
        fp.write(json_string.replace("\n\t\t\t", "").replace("\n\t\t}", "}"))


write_json_file(file_name.with_name(file_name_base + "packets.json"), {"packets": packets})
write_json_file(file_name.with_name(file_name_base + "frames.json"), {"frames": frames})
