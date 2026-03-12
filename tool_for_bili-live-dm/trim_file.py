import json
import sys
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json


def _trim_file(in_path: str) -> None:
    with Path(in_path).open(encoding="utf-8") as input_file, Path(in_path).with_suffix(".TRIM.jsonl").open("a", 1048576, "utf-8") as out_file:
        for line in input_file:
            # if any(keyword in line for keyword in _SKIP_KEYWORDS):
            #     continue
            ls = line.find("{")
            date_raw = line[:ls]
            date = ((date_raw.replace(".", "") + "0000000000000")[:13] if ls else "") if "." in date_raw else date_raw[:13] if ls else ""
            x = simdjson.loads(line[ls:])
            out_file.write(date + json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    files_to_process = sys.argv[1:]
    for file in files_to_process:
        _trim_file(file)
