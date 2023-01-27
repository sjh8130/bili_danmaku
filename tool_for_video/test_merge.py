import json
import io
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

input_file_1 = sys.argv[1]
input_info_1 = sys.argv[1].rsplit(".",1)[-2]+sys.argv[3]+".json"
input_file_2 = sys.argv[2]
input_info_2 = sys.argv[2].rsplit(".",1)[-2]+sys.argv[3]+".json"
output_file = "NUL"
output_file = input_file_1.rsplit(".")[-2]+"_OUT."+input_file_1.rsplit(".")[-1]

with open(input_info_1, "r") as hash_1, \
	open(input_info_2, "r") as hash_2, \
	io.open(input_file_1, "rb") as input_1, \
	io.open(input_file_2, "rb") as input_2, \
	io.open(output_file, "wb") as out:
	print_control = 0
	output_frames = 0
	packets1 = json.load(hash_1)["packets"]
	packets2 = json.load(hash_2)["packets"]
	x = "========        "	# 输出文件1
	y = "        ========"	# 输出文件2
	z = "================"	# 文件1和文件2的帧内容相同，输出
	i = 0
	j = 0
	while True:
		a = packets1[i]
		b = packets2[j]
		if a["data_hash"] != b["data_hash"] and i != len(packets1)-1:
			input_1.seek(int(a["pos"]))
			out.write(input_1.read(int(a["size"])))
			if print_control == 0:...
			else: print()
			print_control = 0
			output_frames += 1
			print(x,output_frames,end="\r")
			i += 1
		elif a["data_hash"] == b["data_hash"] and i != len(packets1)-1:
			input_1.seek(int(a["pos"]))
			out.write(input_1.read(int(a["size"])))
			if print_control == 1:...
			else: print()
			print_control = 1
			output_frames += 1
			print(z,output_frames,end="\r")
			i += 1
			j += 1
		elif i == len(packets1)-1 and j != len(packets2)-1:
			input_2.seek(int(b["pos"]))
			out.write(input_2.read(int(b["size"])))
			output_frames += 1
			if print_control == 2:...
			else: print()
			print_control = 2
			print(y,output_frames,end="\r")
			j += 1
		elif i == len(packets1)-1 and j == len(packets2)-1:
			input_2.seek(int(b["pos"]))
			out.write(input_2.read(int(b["size"])))
			output_frames += 1
			print(y,output_frames,end="\r")
			break
		else:
			print("ERR")
			print(f"i={i}\tj={j}")
			break
	print()
	print(output_frames)
