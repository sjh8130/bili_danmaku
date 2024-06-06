#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import json
import sys
import time

try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2

from my_lib.file_writer import FileWriter

if __name__ == "__main__":
	is_live_recording = False
	time1 = time.time()
	print("read")
	danmaku_binary = open(sys.argv[1], "rb").read()

	time2 = time.time()
	print("proto")
	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(danmaku_binary)

	if len(Temp_Binary.elems) == 0:
		print("No Data")
		sys.exit()
	time3 = time.time()
	print("json")
	j1 = json.loads(MessageToJson(Temp_Binary, indent=0))
	# for this in Temp_Binary.elems:
	# 	if this.attr == 2:
	# 		is_live_recording = True
	# 		break
	itm_len = len(j1["elems"])
	i = 0
	while True:
		itm_len = len(j1["elems"])
		if i == itm_len:
			break

		try:
			if j1["elems"][i]["test20"] == "0":
				del j1["elems"][i]["test20"]
		except KeyError:
			pass

		try:
			if j1["elems"][i]["test21"] == "0":
				del j1["elems"][i]["test21"]
		except KeyError:
			pass

		try:
			del j1["elems"][i]["weight"]
		except KeyError:
			pass

		try:
			del j1["elems"][i]["likes"]
		except KeyError:
			pass

		try:
			del j1["elems"][i]["oid"]
		except KeyError:
			pass
		try:
			del j1["elems"][i]["xxxx"]
		except KeyError:
			pass

		try:
			if j1["elems"][i]["pool"] == 3:
				try:
					del j1["elems"][i]
				except KeyError:
					pass
				continue
		except KeyError:
			pass
		i += 1

	# j1["commandDms"] = []
	# j1["info"] = {}
	# j1["info"]["Ver"] = "V6_20230601_P2J"
	# j1["info"]["dmk_Ver"] = 4
	# j1["info"]["owner"] = {"mid":0, "name":"Fake_Username", "face":"http://[::]/a.jpg"}
	# j1["info"]["bvid"] = "Fake_BVID"
	# j1["info"]["avid"] = 0
	# j1["info"]["V_Name"] = "Fake_MainTitle"
	# j1["info"]["pubdate"] = 0
	# j1["info"]["ctime"] = 0
	# j1["info"]["P_Name"] = "Fake_P_Title"
	# j1["info"]["cid"] = 0
	# j1["info"]["duration"] = 0
	# j1["info"]["segment_count"] = 0
	# j1["info"]["danmaku_count"] = len(j1["elems"])
	# j1["info"]["danmaku_web_reported"] = 0
	# j1["info"]["danmaku_proto_reported"] = 0
	# j1["info"]["File_Create_Time"] = int(os.stat(sys.argv[1]).st_ctime)
	# j1["info"]["File_Create_Time_Start"] = int(os.stat(sys.argv[1]).st_ctime)
	# j1["info"]["is_live_record"] = is_live_recording
	Write_Data = json.dumps(j1, ensure_ascii=False, separators=(",", ":"))

	Temp_Binary = None
	time4 = time.time()
	print("write")
	FileWriter(f"{sys.argv[1]}.json", Write_Data.replace(
		"},{\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", ""))
	# writeER(f"{sys.argv[1]}.json", Write_Data.replace("}, {\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", ""), True)
	time5 = time.time()

	print(f"ALL:{time5-time1}, Write: {time5-time4}, Json: {time4-time3}, Proto: {time3-time2}, Read: {time2-time1}")
