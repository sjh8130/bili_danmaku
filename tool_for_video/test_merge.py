import json
import io
import os
import sys

"""
修视频？
使用ffmpeg的hash来修复视频文件
for %a in (*.flv) do ffmpeg -v warning -hide_banner -i "%~na.flv" -c copy "%~na.aac" -c copy "%~na.264"

for %a in (*.flv) do ffmpeg -v warning -hide_banner -i "%~na.flv" -vn -c copy "%~na.aac"
for %a in (*.flv) do ffmpeg -v warning -hide_banner -i "%~na.flv" -an -c copy "%~na.264"

for %a in (*.aac) do ffprobe -v warning -hide_banner -show_data_hash SHA256 -show_packets "%~na.aac"|find "data_hash=SHA256:" >"%~naA.txt"
for %a in (*.aac) do ffprobe -v warning -hide_banner -show_data_hash SHA256 -show_packets -print_format json=compact=1 "%~na.aac" > "%~naA.json"

for %a in (*.264) do ffprobe -v warning -hide_banner -show_data_hash SHA256 -show_packets "%~na.264"|find "data_hash=SHA256:" >"%~naV.txt"
for %a in (*.264) do ffprobe -v warning -hide_banner -show_data_hash SHA256 -show_packets -print_format json=compact=1 "%~na.264" > "%~naV.json"
"""

if sys.argv[3].__eq__("A"):
	SUFFIX = ".aac"
elif sys.argv[3].__eq__("V"):
	SUFFIX = ".264"
IN_INFO_1 = sys.argv[1].rsplit(".",1)[-2]+sys.argv[3]+".json"
IN_INFO_2 = sys.argv[2].rsplit(".",1)[-2]+sys.argv[3]+".json"
IN_FILE_1 = sys.argv[1].rsplit(".",1)[-2]+SUFFIX
IN_FILE_2 = sys.argv[2].rsplit(".",1)[-2]+SUFFIX

OUT__FILE = "NUL"
OUT__FILE = IN_FILE_1.rsplit(".")[-2]+"_OUT."+IN_FILE_1.rsplit(".")[-1]

with open(IN_INFO_1, "r") as HASH_1, \
	open(IN_INFO_2, "r") as HASH_2, \
	io.open(IN_FILE_1, "rb", buffering=256*1024*1024) as FILE_1, \
	io.open(IN_FILE_2, "rb") as FILE_2, \
	io.open(OUT__FILE, "wb") as OUT_FI:
	print_control = 0
	output_frames = 0
	output_F_size = 0
	PKT_1 = json.load(HASH_1)["packets"]
	PKT_2 = json.load(HASH_2)["packets"]
	HASH_1.close()
	HASH_2.close()
	OUT_L = "========        "	# 输出文件1
	OUT_R = "        ========"	# 输出文件2
	OUT_A = "================"	# 文件1和文件2的帧内容相同，输出
	LEN_P1 = len(PKT_1)
	LEN_P2 = len(PKT_2)
	i = 0
	j = 0
	print(f"{LEN_P1}+{LEN_P2} = {LEN_P1+LEN_P2}")
	print(f"{os.stat(IN_FILE_1).st_size}+{os.stat(IN_FILE_2).st_size} = {os.stat(IN_FILE_1).st_size+os.stat(IN_FILE_2).st_size}")
	while True:
		a = PKT_1[i]
		b = PKT_2[j]
		if a["data_hash"] != b["data_hash"] and i != LEN_P1-1:
			FILE_1.seek(int(a["pos"]))
			OUT_FI.write(FILE_1.read(int(a["size"])))
			if print_control != 0: print()
			print_control = 0
			output_frames += 1
			output_F_size += int(a["size"])
			print(OUT_L,output_frames,end="\r")
			i += 1
		elif a["data_hash"] == b["data_hash"] and i != LEN_P1-1:
			FILE_1.seek(int(a["pos"]))
			OUT_FI.write(FILE_1.read(int(a["size"])))
			if print_control != 1: print()
			print_control = 1
			output_frames += 1
			output_F_size += int(a["size"])
			print(OUT_A,output_frames,end="\r")
			i += 1
			j += 1
		elif i == LEN_P1-1 and j != LEN_P2-1:
			FILE_2.seek(int(b["pos"]))
			OUT_FI.write(FILE_2.read(int(b["size"])))
			output_frames += 1
			output_F_size += int(b["size"])
			if print_control != 2: print()
			print_control = 2
			print(OUT_R,output_frames,end="\r")
			j += 1
		elif i == LEN_P1-1 and j == LEN_P2-1:
			FILE_2.seek(int(b["pos"]))
			OUT_FI.write(FILE_2.read(int(b["size"])))
			output_frames += 1
			output_F_size += int(b["size"])
			print(OUT_R,output_frames,end="\r")
			break
		else:
			print("ERR")
			print(f"i={i}\tj={j}")
			break
	OUT_FI.close()
	print()
	print(output_frames, output_F_size)
