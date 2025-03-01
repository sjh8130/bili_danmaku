import json
import sys

try:
    import simdjson
except ImportError:
    simdjson = json

def _main():
    """ffprobe json[data-hash] to txt"""
    in_path = sys.argv[1]
    with open(in_path, "r", encoding="utf-8") as fp:
        d = simdjson.load(fp)
    if not d:
        exit()
    preload = 0
    switch = False
    for i in d["packets"]:
        if preload >= 150:
            break
        if i["stream_index"] > 0:
            switch = True
        preload += 1
    if switch:
        with open(in_path.rsplit(".", 1)[-2] + "V.txt", "w") as f1, open(
            in_path.rsplit(".", 1)[-2] + "A.txt", "w"
        ) as f2:
            for i in d["packets"]:
                if i["stream_index"] == 0:
                    f1.write(i["data_hash"] + "\n")
                elif i["stream_index"] == 1:
                    f2.write(i["data_hash"] + "\n")
    else:
        with open(in_path.rsplit(".", 1)[-2] + ".txt", "w") as f:
            for i in d["packets"]:
                f.write(i["data_hash"] + "\n")


if __name__ == "__main__":
    _main()
