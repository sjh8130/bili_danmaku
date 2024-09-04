import json
import sys

file_name = sys.argv[1]
try:
    file_name_base = file_name.rsplit(".", 1)[-2]
    if file_name_base == file_name:
        file_name_base = file_name + "_"
except IndexError:
    file_name_base = file_name + "_"

a = json.loads(open(file_name, "r", encoding="utf-8").read())
if a == {}:
    exit()

packets = []
frames = []
if a["packets_and_frames"]:
    for i in a["packets_and_frames"]:
        if i["type"] == "packet":
            packets.append(i)
        elif i["type"] == "frame":
            frames.append(i)
    with open(file_name_base + "packets.json", "w", encoding="utf-8") as fp:
        str = json.dumps({"packets": packets}, indent="\t", separators=(",", ":"))
        fp.write(str.replace("\n\t\t\t", "").replace("\n\t\t}", "}"))
    with open(file_name_base + "frames.json", "w", encoding="utf-8") as fp:
        str = json.dumps({"frames": frames}, indent="\t", separators=(",", ":"))
        fp.write(str.replace("\n\t\t\t", "").replace("\n\t\t}", "}"))
