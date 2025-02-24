import json
import sys

a = json.loads(open(sys.argv[1], "r", encoding="utf-8").read())
if not a:
    exit()
preload = 0
switch = False
for i in a["packets"]:
    if preload >= 150:
        break
    if i["stream_index"] > 0:
        switch = True
    preload += 1
if switch:
    with open(sys.argv[1].rsplit(".", 1)[-2] + "V.txt", "w") as FILE_1, open(
        sys.argv[1].rsplit(".", 1)[-2] + "A.txt", "w"
    ) as FILE_2:
        for i in a["packets"]:
            if i["stream_index"] == 0:
                FILE_1.write(i["data_hash"] + "\n")
            elif i["stream_index"] == 1:
                FILE_2.write(i["data_hash"] + "\n")
else:
    with open(sys.argv[1].rsplit(".", 1)[-2] + ".txt", "w") as f:
        for i in a["packets"]:
            f.write(i["data_hash"] + "\n")
