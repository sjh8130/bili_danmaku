import json
from google.protobuf.json_format import MessageToJson
from base64 import b64decode
import Live_dm_v2_pb2 as live_dm
import sys

infile = sys.argv[1]
outfile= "B:\\test.json"
proc = {"default": []}
with open(infile, "r", 1048576, encoding="utf-8") as file:
	for item in file.readlines():
		if item.find("DANMU_MSG") == -1 :
			continue
		for i in range(len(item)):
			try:
				temp_json = json.loads(item[i:])
			except json.decoder.JSONDecodeError:
				continue
			else:
				break
		if temp_json["cmd"] != "DANMU_MSG":
			continue
		try:
			decoded_B64 = b64decode(temp_json["dm_v2"])
		except KeyError:
			continue
		temp_proto = live_dm.dm_V2()
		temp_proto.ParseFromString(decoded_B64)
		proc["default"].append(json.loads(MessageToJson(temp_proto, indent=0, including_default_value_fields=False)))
final_file = json.dumps(proc, ensure_ascii=False, indent=None, separators=(",", ":")).replace("},{\"dmid\"","},\n{\"dmid\"")
open(outfile, "w", encoding="utf-8").write(final_file)
