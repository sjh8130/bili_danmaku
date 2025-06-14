import json
import sys

try:
    import simdjson
except ImportError:
    simdjson = json  # type:ignore


def _main() -> None:
    """FFprobe json[data-hash] to txt."""
    in_path = sys.argv[1]
    with open(in_path, encoding="utf-8") as fp:
        d = simdjson.load(fp)  # type:ignore
    if not d:
        sys.exit()
    switch = False
    for preload, i in enumerate(d["packets"]):
        if preload >= 150:
            break
        if i["stream_index"] > 0:
            switch = True
    if switch:
        with (
            open(in_path.rsplit(".", 1)[-2] + "V.txt", "w", encoding="utf-8") as f1,
            open(in_path.rsplit(".", 1)[-2] + "A.txt", "w", encoding="utf-8") as f2,
        ):
            for i in d["packets"]:
                if i["stream_index"] == 0:
                    f1.write(i["data_hash"] + "\n")
                elif i["stream_index"] == 1:
                    f2.write(i["data_hash"] + "\n")
    else:
        with open(in_path.rsplit(".", 1)[-2] + ".txt", "w", encoding="utf-8") as f:
            for i in d["packets"]:
                f.write(i["data_hash"] + "\n")


if __name__ == "__main__":
    _main()
