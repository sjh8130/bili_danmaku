import io
import json
import time
from google.protobuf.json_format import MessageToDict
from base64 import b64decode

# import Live_dm_v2_pb2 as live_dm
import Live_dm_v2_2023_03_23_pb2 as live_dm
import sys
from filters import FILTER_WORDS


st = time.time()
in_path = sys.argv[1]
outPath = "Z:\\test.json"
left_pos_cache = 0
right_pos_cache = 0
dm_proto = live_dm.Dm()
with open(in_path, "r", 1048576, encoding="utf-8") as F_in, io.open(outPath, "w", encoding="utf-8") as F_out:
    for this_line in F_in.readlines():
        if this_line.find("dm_v2") == -1:
            continue
        right_pos_cache = len(this_line)
        for left_pos_cache in range(len(this_line)):
            try:
                dm_proto.ParseFromString(b64decode(json.loads(this_line[left_pos_cache:right_pos_cache])["dm_v2"]))
            except json.decoder.JSONDecodeError as err:
                if err.msg == "Extra data":
                    left_pos_cache = err.pos
                if err.msg == "Expecting value":
                    right_pos_cache -= 1
                continue
            else:
                break
        if dm_proto.text.lstrip(" ").rstrip(" ").lstrip("　").rstrip("　").lower() in FILTER_WORDS or dm_proto.text.find("【") > 0 or dm_proto.text.find("】") > 0 or dm_proto.dm_type != live_dm.DmTypeNormal:
            continue
        temp_json2 = MessageToDict(dm_proto)
        temp_json2["text"] = temp_json2["text"].lstrip(" ").rstrip(" ").lstrip("　").rstrip("　")
        if 1:
            del temp_json2["dmid"]  # 1
            del temp_json2["mode"]  # 2
            del temp_json2["size"]  # 3
            del temp_json2["color"]  # 4
            del temp_json2["uhash"]  # 5
            del temp_json2["date"]  # 6
            try:
                del temp_json2["ctime"]  # 7
            except:
                pass

            try:
                del temp_json2["dmType"]  # 8
            except:
                pass

            try:
                del temp_json2["rnd"]  # 9
            except:
                pass

            # # try: del temp_json2["type"]	# 11
            # # except: pass

            try:
                del temp_json2["bizScene"]  # 11
            except:
                pass

            del temp_json2["bubble"]  # 12

            try:
                del temp_json2["emoticons"]  # 14
            except:
                pass

            del temp_json2["aggregation"]  # 17

            del temp_json2["check"]  # 19
            del temp_json2["room"]  # 21

            try:
                del temp_json2["icon"]  # 22
            except:
                pass

            del temp_json2["user"]["uid"]
            del temp_json2["user"]["name"]
            try:
                del temp_json2["user"]["nameColor"]
            except:
                pass
            try:
                del temp_json2["user"]["face"]
            except:
                pass
            del temp_json2["user"]["level"]["rank"]
            del temp_json2["user"]["mobileVerify"]
            del temp_json2["user"]["rank"]
            try:
                del temp_json2["user"]["medal"]["name"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["level"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["light"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["color"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["borderColor"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["gradientStartColor"]
            except:
                pass
            try:
                del temp_json2["user"]["medal"]["gradientEndColor"]
            except:
                pass
            del temp_json2["user"]["medal"]

            try:
                del temp_json2["user"]["level"]["level"]
            except:
                pass
            try:
                del temp_json2["user"]["level"]["attr"]
            except:
                pass
            try:
                del temp_json2["user"]["level"]["onlineRank"]
            except:
                pass
            del temp_json2["user"]["level"]["color"]
            del temp_json2["user"]["level"]

            del temp_json2["user"]["title"]
            del temp_json2["user"]["identify"]
            try:
                del temp_json2["user"]["wealth"]
            except:
                pass
            del temp_json2["user"]

            try:
                del temp_json2["reply"]
            except:
                pass
        F_out.write(json.dumps(temp_json2, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
    F_in.close()
    F_out.close()
et = time.time()
print(et - st)
time.sleep(5)
