import json
import sys
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json


def get_file_name_base(file_name: Path) -> Path:
    file_name_base = file_name.parent / (file_name.stem.split(".", 1)[-2])
    return file_name_base if file_name_base != file_name else file_name / "_"


def write_json_file(file_name: Path, data_dict: dict) -> None:
    with file_name.open("w", encoding="utf-8") as fp:
        json_string = json.dumps(data_dict, indent="\t", separators=(",", ":"))
        fp.write(json_string.replace("\n\t\t\t", "").replace("\n\t\t}", "}"))


def main(d: dict) -> None:
    p_stream_index = []
    file_name_base = get_file_name_base(file_name)
    for stream in d.get("packets", []):
        stream_index = stream["stream_index"]
        stream_type = stream["codec_type"]
        if stream_index in p_stream_index:
            continue
        p_stream_index.append(stream_index)
        packets = [i for i in d.get("packets", []) if i["stream_index"] == stream_index]
        if packets:
            file_name_suffix = f"_{stream_type}_{stream_index}"
            write_json_file(file_name_base / (file_name_suffix + ".json"), {"packets": packets})
    p_stream_index.clear()

    for stream in d.get("frames", []):
        stream_index = stream["stream_index"]
        stream_type = stream["codec_type"]
        if stream_index in p_stream_index:
            continue
        p_stream_index.append(stream_index)
        frames = [i for i in d.get("frames", []) if i["stream_index"] == stream_index]
        if frames:
            file_name_suffix = f"_{stream_type}_{stream_index}"
            write_json_file(file_name_base / (file_name_suffix + ".json"), {"frames": frames})
    p_stream_index.clear()

    for stream in d.get("packets_and_frames", []):
        stream_index = stream["stream_index"]
        stream_type = stream["codec_type"]
        if stream_index in p_stream_index:
            continue
        p_stream_index.append(stream_index)
        packets_and_frames = [i for i in d.get("packets_and_frames", []) if i["stream_index"] == stream_index]
        if packets_and_frames:
            file_name_suffix = f"_{stream_type}_{stream_index}"
            write_json_file(file_name_base / (file_name_suffix + ".json"), {"packets_and_frames": packets_and_frames})


if __name__ == "__main__":
    file_name = Path(sys.argv[1]).resolve()
    with file_name.open(encoding="utf-8") as f:
        data: dict = simdjson.load(f)
    if not data:
        sys.exit()
    main(data)
