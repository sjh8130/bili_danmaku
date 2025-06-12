import binascii
import json
import sys
import time
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json
import Live_dm_v2_2023_03_23_pb2 as live_dm
from filters import FILTER_WORDS
from google.protobuf.json_format import MessageToDict

st = time.time()
in_path = Path(sys.argv[1])
out_path = Path("Z:\\test.json")
left_pos_cache = 0
right_pos_cache = 0
dm_proto = live_dm.Dm()
with in_path.open(encoding="utf-8") as F_in, out_path.open("w", encoding="utf-8") as F_out:
    for line in F_in:
        if line.find("dm_v2") == -1:
            continue
        right_pos_cache = len(line)
        try:
            dm_proto.ParseFromString(binascii.a2b_base64(simdjson.loads(line[line.find("{") : right_pos_cache])["dm_v2"]))  # type: ignore
        except json.decoder.JSONDecodeError as err:
            if err.msg == "Extra data":
                left_pos_cache = err.pos
            if err.msg == "Expecting value":
                right_pos_cache -= 1
            continue
        if (
            dm_proto.text.lstrip(" ").rstrip(" ").lstrip("　").rstrip("　").lower() in FILTER_WORDS
            or dm_proto.text.find("【") > 0
            or dm_proto.text.find("】") > 0
            or dm_proto.dm_type != live_dm.DmTypeNormal
        ):
            continue
        itm = MessageToDict(dm_proto)
        itm["text"] = itm["text"].strip()
        F_out.write(json.dumps(itm, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
et = time.time()
print(et - st)
time.sleep(5)
