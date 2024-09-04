import json
import io
import os
import sys

"""
修视频？
"""
err_count = 0
argv = ["XXXX", "", "", ""]
if len(sys.argv) < 3:
    if len(sys.argv) == 2:
        argv[1] = sys.argv[1]
        argv[2] = sys.argv[2]
        if argv[-4:] == ".aac":
            argv[3] = "A"
        elif argv[-4:] == ".264":
            argv[3] = "V"
        # elif argv[-4:] == ".265": argv[3] = "V"
        else:
            print("Error")
            err_count += 100
    else:
        argv[1] = input("file 1 : ").lstrip('"').rstrip('"')
        argv[2] = input("file 2 : ").lstrip('"').rstrip('"')
        argv[3] = input("suffix : ")
elif len(sys.argv) == 3:
    argv[1] = sys.argv[1]
    argv[2] = sys.argv[2]
    argv[3] = sys.argv[3]
else:
    print(sys.argv)
if argv[3].__eq__("A"):
    SUFFIX = ".aac"
elif argv[3].__eq__("V"):
    SUFFIX = ".264"
IN_INFO_1 = argv[1].rsplit(".", 1)[-2] + argv[3] + ".json"
IN_INFO_2 = argv[2].rsplit(".", 1)[-2] + argv[3] + ".json"
IN_FILE_1 = argv[1].rsplit(".", 1)[-2] + SUFFIX
IN_FILE_2 = argv[2].rsplit(".", 1)[-2] + SUFFIX

OUT__FILE = "NUL"
OUT__FILE = IN_FILE_1.rsplit(".")[-2] + "_OUT." + IN_FILE_1.rsplit(".")[-1]

with open(IN_INFO_1, "r") as HASH_1, open(IN_INFO_2, "r") as HASH_2, io.open(IN_FILE_1, "rb") as FILE_1, io.open(IN_FILE_2, "rb") as FILE_2, io.open(OUT__FILE, "wb") as OUT_FI:
    print_control = 0
    output_frames = 0
    output_file_size = 0
    PKT_1 = json.load(HASH_1)["packets"]
    PKT_2 = json.load(HASH_2)["packets"]
    HASH_1.close()
    HASH_2.close()
    OUT_L = "========        "  # 输出文件1
    OUT_R = "        ========"  # 输出文件2
    OUT_A = "================"  # 文件1和文件2的帧内容相同，输出
    OUT_S = "++++++SKIP++++++"  # 跳过
    LEN_P1 = len(PKT_1)
    LEN_P2 = len(PKT_2)
    i = 0
    j = 0
    k = "A"
    skip_count = 0
    print(f"XXXXXXXXXXXXXXXX\tOutput\tSkip\tPOS_L\tPOS_R\tSize", end="")
    while True:
        if i == LEN_P1 and j == LEN_P2:
            print("\n__END__")
            break
        pktL = PKT_1[i]
        if j < LEN_P2:
            pktR = PKT_2[j]

        if err_count >= 100:
            print("too many Error")
            break

        if pktL["data_hash"] == pktR["data_hash"] and i != LEN_P1 - 1:
            FILE_1.seek(int(pktL["pos"]))
            OUT_FI.write(FILE_1.read(int(pktL["size"])))
            if print_control != 1:
                print()
            print_control = 1
            output_frames += 1
            output_file_size += int(pktL["size"])
            k = "A"
            i += 1
            j += 1
            print(f"{OUT_A}\t{output_frames}\t{skip_count}\t{i+1}\t{j+1}\t{output_file_size}", end="\r")
        else:
            if (k.__contains__("L") and i <= LEN_P1 - 1) or (i < LEN_P1 and j == LEN_P2):
                if k.__contains__("S"):
                    skip_count += 1
                    print(f"{OUT_S}\t{output_frames}\t{skip_count}\t{i+1}\t{j+1}\t{output_file_size}", end="\r")
                else:
                    FILE_1.seek(int(pktL["pos"]))
                    OUT_FI.write(FILE_1.read(int(pktL["size"])))
                    if print_control != 0:
                        print()
                    print_control = 0
                    output_frames += 1
                    output_file_size += int(pktL["size"])
                    print(
                        f"{OUT_L}\t{output_frames}\t{skip_count}\t{i+1}\t{j+1}\t{output_file_size}",
                        end="\r"
                    )
                i += 1
            elif k.__contains__("R"):
                if k.__contains__("S"):
                    skip_count += 1
                    print(f"{OUT_S}\t{output_frames}\t{skip_count}\t{i+1}\t{j+1}\t{output_file_size}", end="\r")
                else:
                    FILE_2.seek(int(pktR["pos"]))
                    OUT_FI.write(FILE_2.read(int(pktR["size"])))
                    print_control = 2
                    output_frames += 1
                    output_file_size += int(pktR["size"])
                    if print_control != 2:
                        print()
                    print(f"{OUT_R}\t{output_frames}\t{skip_count}\t{i+1}\t{j+1}\t{output_file_size}", end="\r")
                j += 1
            elif k == "A":
                k = input("\nNext:")
            elif i == LEN_P1 and j == LEN_P2:
                break
            elif skip_count > LEN_P1 + LEN_P2:
                print("too many skip")
                break
            else:
                err_count += 1
                print("Error")
    OUT_FI.close()
    print()
    print("#\tFrames\t\tSize")
    print(f"A\t{LEN_P1}\t\t{os.stat(IN_FILE_1).st_size}")
    print(f"B\t{LEN_P2}\t\t{os.stat(IN_FILE_2).st_size}")
    print(f"Sum\t{LEN_P1+LEN_P2}\t\t{os.stat(IN_FILE_1).st_size+os.stat(IN_FILE_2).st_size}")
    print(f"F\t{output_frames}\t\t{output_file_size}")
