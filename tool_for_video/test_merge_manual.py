import json
import io
import sys

"""
修视频？
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
	io.open(IN_FILE_1, "rb") as FILE_1, \
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
	k = "A"
	while True:
		if i == LEN_P1 and j == LEN_P2:
			print("\n!!!!!!")
			break
		a = PKT_1[i]
		if j<LEN_P2:
			b = PKT_2[j]

		if a["data_hash"] == b["data_hash"] and i != LEN_P1-1:
			FILE_1.seek(int(a["pos"]))
			OUT_FI.write(FILE_1.read(int(a["size"])))
			if print_control != 1: print()
			print_control = 1
			output_frames += 1
			output_F_size += int(a["size"])
			k = "A"
			i += 1
			j += 1
			print(OUT_A,output_frames,end="\r")
		else:
			if (k == "L" and i <= LEN_P1-1) or (i< LEN_P1 and j==LEN_P2):
				FILE_1.seek(int(a["pos"]))
				OUT_FI.write(FILE_1.read(int(a["size"])))
				if print_control != 0: print()
				print_control = 0
				output_frames += 1
				output_F_size += int(a["size"])
				i += 1
				print(OUT_L,output_frames,end="\r")
			elif k == "R":
				FILE_2.seek(int(b["pos"]))
				OUT_FI.write(FILE_2.read(int(b["size"])))
				print_control = 2
				output_frames += 1
				output_F_size += int(b["size"])
				if print_control != 2: print()
				j += 1
				print(OUT_R,output_frames,end="\r")
			elif k == "A":
				k = input("\nNext:")
			elif i == LEN_P1 and j == LEN_P2:
				break
			else:
				print("Error")
	OUT_FI.close()
	print()
	print(output_frames, output_F_size)
