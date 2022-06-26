import json
import sys
import re
import time

Start_Time = time.time()
jsonData = ""
input_file = sys.argv[1]
outputFile = input_file.rstrip(".json")+".xml"
Split_SIZE = 2500

with open(input_file, "r", encoding="utf-8")as f:
	jsonData = f.read()

try: jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
	print("\033[41m==============================ERROR=============================\033[0m")
	if len(jsonData) <= 2:	print("\033[41m Empty File\033[0m")
	print("总计用时:", time.time()-Start_Time)
	sys.exit(1)

cid = re.split("_", input_file)[3]
XML_item = ""

danmu_count = len(jsonData["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = ""

for i in range(danmu_count):
	try: content = jsonData["elems"][i]["content"]
	except KeyError:
		# print("\n\033[43m content   ERROR", jsonData["elems"][i]["id"], "\033[0m")
		continue
		# content = "_CONTENT_ERROR_"
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

	try: progress = jsonData["elems"][i]["progress"]
	except KeyError: progress = 0.0
	progress = format(progress/1000, ".5f")
	mode = jsonData["elems"][i]["mode"]
	fontsize = jsonData["elems"][i]["fontsize"]
	try: color = jsonData["elems"][i]["color"]
	except KeyError: color = 0
	midHash = jsonData["elems"][i]["midHash"]
	ctime = jsonData["elems"][i]["ctime"]
	weight = jsonData["elems"][i]["weight"]
	# try: idstr = jsonData["elems"][i]["idstr"]
	# except KeyError: idstr = "0"# ,print("\n idstr    ERROR", 1)
	id = jsonData["elems"][i]["id"]
	# if id != idstr:print("\n id idstr mismatch:", id, idstr)
	try: pool = jsonData["elems"][i]["pool"]
	except KeyError: pool = 0

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id, weight - 1, content)
	XML_Data_2nd_Cache += XML_item
	if i % Split_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
		print(f"\r进度：{i}/{danmu_count}，用时：",format(time.time()-Start_Time,".5f"),end="")

XML_Data_1st_Cache += XML_Data_2nd_Cache
XML_Data_1st_Cache += "</i>"
with open(outputFile, "w", encoding="utf-8")as Final_Write:
	Final_Write.write(XML_Data_1st_Cache)
	Final_Write.close()
End_Time = time.time()
print(f"\r总计用时: {End_Time-Start_Time}          ")
