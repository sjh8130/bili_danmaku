import io
import json
import time
from google.protobuf.json_format import MessageToJson
from base64 import b64decode
# import Live_dm_v2_pb2 as live_dm
import Live_dm_v2_2023_03_23_pb2 as live_dm
import sys
from filters import FILTER_WORDS

st = time.time()
in_path = sys.argv[1]
outPath = "Z:\\test.json"
L_pos = 0
dm_proto = live_dm.Dm()
with open(in_path, "r", 1048576, encoding="utf-8") as F_in, io.open(outPath, "w", encoding="utf-8") as F_out:
	for item in F_in.readlines():
		if item.find("dm_v2") == -1:
			continue
		R_pos = len(item)
		for L_pos in range(len(item)):
			try:
				dm_proto.ParseFromString(b64decode(json.loads(item[L_pos:R_pos])["dm_v2"]))
			except json.decoder.JSONDecodeError as err:
				if err.msg == "Extra data": L_pos = err.pos
				if err.msg == "Expecting value": R_pos -= 1
				continue
			else:
				break
		if dm_proto.text.lstrip(" ").rstrip(" ").lstrip("　").rstrip("　") in FILTER_WORDS or dm_proto.text.find("【")>0 or dm_proto.text.find("】")>0:
			continue
		temp_json2 = json.loads(MessageToJson(dm_proto, indent=0, including_default_value_fields=False))
		temp_json2["text"] = temp_json2["text"].lstrip(" ").rstrip(" ").lstrip("　").rstrip("　")
		if 1:
			del temp_json2["dmid"]	# 1
			del temp_json2["mode"]	# 2
			del temp_json2["size"]	# 3
			del temp_json2["color"]	# 4
			del temp_json2["uhash"]	# 5
			del temp_json2["date"]	# 6
			del temp_json2["ctime"]	# 7

			try: del temp_json2["dmType"]	# 8
			except: pass

			try: del temp_json2["rnd"]	# 9
			except: pass

			# # try: del temp_json2["type"]	# 11
			# # except: pass

			try: del temp_json2["bizScene"]	#11
			except: pass

			del temp_json2["bubble"]	# 12

			try: del temp_json2["emoticons"]	# 14
			except: pass

			del temp_json2["aggregation"]	# 17

			del temp_json2["check"]	# 19
			del temp_json2["room"]	# 21

			try: del temp_json2["icon"]		# 22
			except: pass

			del temp_json2["user"]["uid"]
			del temp_json2["user"]["name"]
			try: del temp_json2["user"]["nameColor"]
			except: pass
			try: del temp_json2["user"]["face"]
			except: pass
			del temp_json2["user"]["level"]["rank"]
			del temp_json2["user"]["mobileVerify"]
			del temp_json2["user"]["rank"]
			try: del temp_json2["user"]["medal"]["name"]
			except: pass
			try: del temp_json2["user"]["medal"]["level"]
			except: pass
			try: del temp_json2["user"]["medal"]["light"]
			except: pass
			try: del temp_json2["user"]["medal"]["color"]
			except: pass
			try: del temp_json2["user"]["medal"]["borderColor"]
			except: pass
			try: del temp_json2["user"]["medal"]["gradientStartColor"]
			except: pass
			try: del temp_json2["user"]["medal"]["gradientEndColor"]
			except: pass
			del temp_json2["user"]["medal"]

			try: del temp_json2["user"]["level"]["level"]
			except: pass
			try: del temp_json2["user"]["level"]["attr"]
			except: pass
			try: del temp_json2["user"]["level"]["onlineRank"]
			except: pass
			del temp_json2["user"]["level"]["color"]
			del temp_json2["user"]["level"]

			del temp_json2["user"]["title"]
			del temp_json2["user"]["identify"]
			try: del temp_json2["user"]["wealth"]
			except: pass
			del temp_json2["user"]
		F_out.write(json.dumps(temp_json2, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
	F_in.close()
	F_out.close()
et = time.time()
print(et-st)
time.sleep(5)
