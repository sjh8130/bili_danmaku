import json
import time
from google.protobuf.json_format import MessageToJson
from base64 import b64decode
# import Live_dm_v2_pb2 as live_dm
import Live_dm_v2_2023_03_23_pb2 as live_dm
import sys

st = time.time()
infile = sys.argv[1]
outfile= "B:\\test.json"
proc = {"default": []}
i = 0
temp_proto = live_dm.dm_V2()
with open(infile, "r", 1048576, encoding="utf-8") as file:
	for item in file.readlines():
		if item.find("dm_v2") == -1:
			continue
		for i in range(len(item)):
			try:
				temp_json = json.loads(item[i:])
			except json.decoder.JSONDecodeError as err:
				if err.msg == "Extra data": i = err.pos
				# if err.msg == "Expecting value": i = err.pos
				continue
			else:
				break
		if temp_json["cmd"] != "DANMU_MSG":
			continue
		try:
			decoded_B64 = b64decode(temp_json["dm_v2"])
		except KeyError:
			continue
		temp_proto.ParseFromString(decoded_B64)
		proc["default"].append(json.loads(MessageToJson(temp_proto, indent=0, including_default_value_fields=False)))
for this in proc["default"]:
	break
	del this["mode"]
	del this["fontsize"]
	del this["color"]
	del this["midHash"]
	del this["content"]
	del this["ctime"]
	try:del this["dmid"]
	except:pass
	del this["chatBubble"]
	try:del this["emots"]
	except:pass
	del this["validation"]
	del this["fanMedalExt"]
final_file = json.dumps(proc, ensure_ascii=False, indent=None, separators=(",", ":")).replace("},{\"idStr\"","},\n{\"idStr\"").replace(",\"unknown17\":[\"\"]","").replace(",\"unknownUserinfo14\":[\"\"]","").replace(",\"title\":{}","").replace(",\"chatBubble\":{}","").replace(",\"lottery\":{}","")
open(outfile, "w", encoding="utf-8").write(final_file)
et = time.time()
print(et-st)
