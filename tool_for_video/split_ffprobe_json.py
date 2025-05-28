import json
import sys

try:
    import simdjson
except ImportError:
    simdjson = json

file_name = sys.argv[1]
with open(file_name, encoding="utf-8") as f:
    data: dict = simdjson.load(f)  # type: ignore


def get_file_name_base(file_name: str) -> str:
    try:
        file_name_base = file_name.rsplit(".", 1)[-2]
        return file_name_base if file_name_base != file_name else file_name + "_"
    except IndexError:
        return file_name + "_"


file_name_base = get_file_name_base(file_name)
packets = [i for i in data.get("packets_and_frames", []) if i["type"] == "packet"]
frames = [i for i in data.get("packets_and_frames", []) if i["type"] == "frame"]


if not data:
    sys.exit()


def write_json_file(file_name: str, data_dict: dict) -> None:
    with open(file_name, "w", encoding="utf-8") as fp:
        json_string = json.dumps(data_dict, indent="\t", separators=(",", ":"))
        fp.write(json_string.replace("\n\t\t\t", "").replace("\n\t\t}", "}"))


write_json_file(file_name_base + "packets.json", {"packets": packets})
write_json_file(file_name_base + "frames.json", {"frames": frames})
