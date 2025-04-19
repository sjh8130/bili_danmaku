import io
import json
import os
import sys

try:
    import simdjson
except ImportError:
    simdjson = json

if sys.argv[3].__eq__("A"):
    SUFFIX = ".aac"
elif sys.argv[3].__eq__("V"):
    SUFFIX = ".264"
else:
    SUFFIX = ".XXX"
IN_INFO_1 = sys.argv[1].rsplit(".", 1)[-2] + sys.argv[3] + ".json"
IN_INFO_2 = sys.argv[2].rsplit(".", 1)[-2] + sys.argv[3] + ".json"
IN_FILE_1 = sys.argv[1].rsplit(".", 1)[-2] + SUFFIX
IN_FILE_2 = sys.argv[2].rsplit(".", 1)[-2] + SUFFIX

OUT__FILE = "NUL"
OUT__FILE = IN_FILE_1.rsplit(".")[-2] + "_OUT." + IN_FILE_1.rsplit(".")[-1]

with (
    open(IN_INFO_1, "r") as HASH_L,
    open(IN_INFO_2, "r") as HASH_R,
    io.open(IN_FILE_1, "rb", buffering=256 * 1024 * 1024) as FILE_1,
    io.open(IN_FILE_2, "rb", buffering=256 * 1024 * 1024) as FILE_2,
    io.open(OUT__FILE, "wb", buffering=256 * 1024 * 1024) as OUT_FI,
):
    print_control = 0
    output_frames = 0
    output_F_size = 0
    PKT_L = simdjson.load(HASH_L)["packets"]
    PKT_R = simdjson.load(HASH_R)["packets"]
    HASH_L.close()
    HASH_R.close()
    OUT_L = "========        "  # 输出文件1
    OUT_R = "        ========"  # 输出文件2
    OUT_A = "================"  # 文件1和文件2的帧内容相同，输出
    LEN_L = len(PKT_L)
    LEN_R = len(PKT_R)
    pos_L = 0
    pos_R = 0
    left = PKT_L[pos_L]
    right = PKT_R[pos_R]
    while True:
        if left["data_hash"] != right["data_hash"] and pos_L != LEN_L - 1:
            FILE_1.seek(int(left["pos"]))
            OUT_FI.write(FILE_1.read(int(left["size"])))
            if print_control != 0:
                print()
            print_control = 0
            output_frames += 1
            output_F_size += int(left["size"])
            print(OUT_L, output_frames, end="\r")
            pos_L += 1
        elif left["data_hash"] == right["data_hash"] and pos_L != LEN_L - 1:
            FILE_1.seek(int(left["pos"]))
            OUT_FI.write(FILE_1.read(int(left["size"])))
            if print_control != 1:
                print()
            print_control = 1
            output_frames += 1
            output_F_size += int(left["size"])
            print(OUT_A, output_frames, end="\r")
            pos_L += 1
            pos_R += 1
        elif pos_L == LEN_L - 1 and pos_R != LEN_R - 1:
            FILE_2.seek(int(right["pos"]))
            OUT_FI.write(FILE_2.read(int(right["size"])))
            output_frames += 1
            output_F_size += int(right["size"])
            if print_control != 2:
                print()
            print_control = 2
            print(OUT_R, output_frames, end="\r")
            pos_R += 1
        elif pos_L == LEN_L - 1 and pos_R == LEN_R - 1:
            FILE_2.seek(int(right["pos"]))
            OUT_FI.write(FILE_2.read(int(right["size"])))
            output_frames += 1
            output_F_size += int(right["size"])
            print(OUT_R, output_frames, end="\r")
            break
        else:
            print("ERR")
            print(f"i={pos_L}\tj={pos_R}")
            break
        left = PKT_L[pos_L]
        right = PKT_R[pos_R]
    OUT_FI.close()
    print()
    print("#\tFrames\t\tSize")
    print(f"A\t{LEN_L}\t\t{os.stat(IN_FILE_1).st_size}")
    print(f"B\t{LEN_R}\t\t{os.stat(IN_FILE_2).st_size}")
    print(f"S\t{LEN_L+LEN_R}\t\t{os.stat(IN_FILE_1).st_size+os.stat(IN_FILE_2).st_size}")
    print(f"F\t{output_frames}\t\t{output_F_size}")
