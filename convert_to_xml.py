import json
import sys
import re
from tqdm import tqdm
import time

Start_Time = time.time()
jsonData = ""
input_file = sys.argv[1]
outputFile = input_file.rstrip(".json")+".xml"
# HDD_Write_Count = 0		# 分段写入计数
# write_split = 20000		# 磁盘IO <<----小----  分块大小 ----大---->> 处理时间 # 分段写入计数

with open(input_file, "r", encoding="utf-8")as f:
	jsonData = f.read()

try:
	jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
	print("\033[41m==============================ERROR=============================\033[0m")
	if len(jsonData) <= 2:
		print("\033[41m Empty File\033[0m")
	print("总计用时:", time.time()-Start_Time)
	sys.exit(1)

cid = re.split("_", input_file)[3]
XML_item = ""

with open(outputFile, "w", encoding="utf-8")as first_clear:
	first_clear.write("")
	# HDD_Write_Count += 1	# 分段写入计数
	first_clear.close()

# counter = 0				# 性能分析
# Time_Array = {}			# 性能分析
# time2 = time.time()		# 性能分析
danmu_count = len(jsonData["elems"])
XML_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"

if danmu_count >= 85000:print("提示：弹幕数量大于 85,000 会导致程序运行缓慢")

Progress_Bar = tqdm(total=danmu_count, leave=False)
for i in range(danmu_count):
	# ================================ content ================================
	try:
		content = jsonData["elems"][i]["content"]
	except KeyError:
		# print("\n\033[43m content   ERROR", jsonData["elems"][i]["id"], "\033[0m")
		continue
		# content = "_CONTENT_ERROR_"

	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
	# ================================ progress ================================
	try:
		progress = jsonData["elems"][i]["progress"]
	except KeyError:
		# print("\n progress ERROR", i)
		progress = 0.0

	progress = format(progress/1000, ".5f")
	# ================================ mode ================================
	mode = jsonData["elems"][i]["mode"]
	# ================================ fontsize ================================
	fontsize = jsonData["elems"][i]["fontsize"]
	# ================================ color ================================
	try:
		color = jsonData["elems"][i]["color"]
	except KeyError:
		# print("\n color    ERROR", i)
		color = 0
	# ================================ midHash ================================
	midHash = jsonData["elems"][i]["midHash"]
	# ================================ ctime ================================
	ctime = jsonData["elems"][i]["ctime"]
	# ================================ weight ================================
	weight = jsonData["elems"][i]["weight"]

	# ================================ idStr ================================
	# try:
	# 	idstr = jsonData["elems"][i]["idstr"]
	# except KeyError:
	# 	# print("\n idstr    ERROR", 1)
	# 	idstr = "0"

	# ================================ id ================================
	id = jsonData["elems"][i]["id"]

	# ================================ id|idStr ================================
	# if id != idstr:
	# 	print("\n id idstr mismatch:", id, idstr)

	# ================================ pool ================================
	try:
		pool = jsonData["elems"][i]["pool"]
	except KeyError:
		pool = 0

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id, weight - 1, content)
	XML_Data += XML_item
	# if i % write_split == 0:
	# 	with open(outputFile, "a", encoding="utf-8")as split_write:
	# 		split_write.write(XML_Data)
	# 		HDD_Write_Count += 1									# 分段写入计数
	# 		XML_Data = ""

	# if i % 1000 == 0:												#性能分析
	# 	time1 = time.time()											#性能分析
	# 	Time_Array[counter] = time1-time2							#性能分析
	# 	counter += 1												#性能分析
	# 	time2 = time.time()											#性能分析
	Progress_Bar.update(1)
Progress_Bar.close()

XML_Data += "</i>"

with open(outputFile, "a", encoding="utf-8")as Final_Write:
	Final_Write.write(XML_Data)
	# HDD_Write_Count += 1											# 分段写入计数
	Final_Write.close()
End_Time = time.time()
# print("Time_Array:",Time_Array)									#性能分析
# print(f"写入分块大小: {write_split}\t磁盘写入计数: {HDD_Write_Count}\t总计用时: {End_Time-Start_Time}")
print(f"总计用时: {End_Time-Start_Time}")
