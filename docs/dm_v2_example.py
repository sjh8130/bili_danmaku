import json
from google.protobuf.json_format import MessageToJson
from base64 import b64decode
import Live_dm_v2_pb2 as live_dm

infile = "path\\to\\file"
outfile= "path\\to\\file.json"
proc = {"default": []}
with open(infile, "r", 1048576, encoding="utf-8") as file:
	for item in file.readlines():
		temp_json = json.loads(item[14:])
		if temp_json["cmd"] != "DANMU_MSG": continue
		decoded_B64 = b64decode(temp_json["dm_v2"])
		temp_proto = live_dm.dm_V2()
		temp_proto.ParseFromString(decoded_B64)
		proc["default"].append(json.loads(MessageToJson(temp_proto, indent=0, including_default_value_fields=False)))
final_file = json.dumps(proc, ensure_ascii=False, indent=None, separators=(",", ":")).replace("},{\"dmid\"","},\n{\"dmid\"")
open(outfile, "w", encoding="utf-8").write(final_file)
