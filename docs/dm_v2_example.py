import json
import time
from google.protobuf.json_format import MessageToJson
from base64 import b64decode
# import Live_dm_v2_pb2 as live_dm
import Live_dm_v2_2023_03_23_pb2 as live_dm
import sys

st = time.time()
infile = sys.argv[1]
outfile = "Z:\\test.json"
final_file = ""
L_pos = 0
temp_proto = live_dm.Dm()
with open(infile, "r", 1048576, encoding="utf-8") as file, open(outfile, "w", encoding="utf-8") as final_file:
	for item in file.readlines():
		if item.find("dm_v2") == -1:
			continue
		R_pos = len(item)
		for L_pos in range(len(item)):
			try:
				temp_json = json.loads(item[L_pos:R_pos])
			except json.decoder.JSONDecodeError as err:
				if err.msg == "Extra data": L_pos = err.pos
				if err.msg == "Expecting value": R_pos -= 1
				continue
			else:
				break
		# if temp_json["cmd"] != "DANMU_MSG":
		# 	continue
		decoded_B64 = b64decode(temp_json["dm_v2"])
		# try:
		# 	decoded_B64 = b64decode(temp_json["dm_v2"])
		# except KeyError:
		# 	continue
		temp_proto.ParseFromString(decoded_B64)
		temp_json2 = json.loads(MessageToJson(temp_proto, indent=0, including_default_value_fields=False))
		if temp_json["info"][0][12] == 1 and 0:
			print(temp_json["info"][0][13]["bulge_display"] == temp_json2["emots"][0]["detail"]["bulgeDisplay"], "\t", \
				temp_json["info"][0][13]["in_player_area"] == temp_json2["emots"][0]["detail"]["inPlayerArea"], "\t", \
				temp_json["info"][0][13]["is_dynamic"] == temp_json2["emots"][0]["detail"]["isDynamic"])
		if 0:
			del temp_json2["idStr"]	# 1
			del temp_json2["mode"]	# 2
			del temp_json2["fontsize"]	# 3
			del temp_json2["color"]	# 4
			del temp_json2["midHash"]	# 5
			del temp_json2["content"]	# 6
			del temp_json2["ctime"]	# 7
			del temp_json2["bubble"]	# 12
			try: del temp_json2["rnd"]	# 9
			except: pass
			try:del temp_json2["aggregation"]	#17
			except:pass
			try: del temp_json2["DmType"]	# 8
			except: pass
			# try: del temp_json2["type"]	# 11
			# except: pass
			try: del temp_json2["emoticons"]	# 14
			except:pass
			del temp_json2["check"]	# 19
			del temp_json2["user"]["uid"]
			del temp_json2["user"]["name"]
			try: del temp_json2["user"]["usernameColor"]
			except: pass
			del temp_json2["user"]["face"]
			del temp_json2["user"]["rank"]
			del temp_json2["user"]["medal"]
			del temp_json2["user"]["level"]
			del temp_json2["user"]["title"]
			del temp_json2["user"]["unknownUserinfo08"]
			del temp_json2["user"]["unknownUserinfo14"]
			del temp_json2["room"]	# 21
		final_file.write(json.dumps(temp_json2, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
	file.close()
	final_file.close()
et = time.time()
print(et-st)
time.sleep(5)