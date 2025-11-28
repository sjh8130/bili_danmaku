import dataclasses
import json
import os
import sys
from decimal import Decimal
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json


@dataclasses.dataclass
class FFProbeFilePackets:
    codec_type: str = ""
    data_hash: str = ""
    dts_time: Decimal = Decimal(0)
    dts: int = 0
    duration_time: Decimal = Decimal(0)
    duration: int = 0
    flags: str = ""
    pos: int = 0
    pts_time: Decimal = Decimal(0)
    pts: int = 0
    size: int = 0
    stream_index: int = 0


@dataclasses.dataclass
class FFProbeFile:
    packets: list[FFProbeFilePackets]

    def __init__(self, packet_list: list[dict]):
        if self.packets is None:
            self.packets = []
        self.packets = [FFProbeFilePackets(**pl) for pl in packet_list]

    def __len__(self) -> int:
        return len(self.packets)

    def __getitem__(self, *k, **kw) -> FFProbeFilePackets:
        return self.packets.__getitem__(*k, **kw)


OL = "========        "  # 输出文件1
OR = "        ========"  # 输出文件2
OA = "================"  # 文件1和文件2的帧内容相同
OS = "++++++SKIP++++++"  # 跳过


def _main():
    """修视频?"""
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
                err_count = 100
        else:
            argv[1] = input("file 1 : ").strip('"')
            argv[2] = input("file 2 : ").strip('"')
            argv[3] = input("suffix : ").strip()
    elif len(sys.argv) == 4:
        argv = sys.argv
    else:
        print(sys.argv)
    if argv[3] == "A":
        SUFFIX = ".aac"
    elif argv[3] == "V":
        SUFFIX = ".264"
    else:
        SUFFIX = ".XXX"
    TYP = argv[3]
    IN_FILE_1 = Path(argv[1]).resolve()
    IN_FILE_2 = Path(argv[2]).resolve()
    IN_INFO_1 = IN_FILE_1.with_name(IN_FILE_1.stem + TYP + ".json")
    IN_INFO_2 = IN_FILE_2.with_name(IN_FILE_2.stem + TYP + ".json")

    out_path = "NUL"
    out_path = IN_FILE_1.with_name(IN_FILE_1.stem + "_OUT" + SUFFIX)

    with IN_INFO_1.open(encoding="utf-8") as HASH_1, IN_INFO_2.open(encoding="utf-8") as HASH_2:
        PACKETS_1 = FFProbeFile(simdjson.load(HASH_1)["packets"])
        PACKETS_2 = FFProbeFile(simdjson.load(HASH_2)["packets"])
        LEN_1 = len(PACKETS_1)
        LEN_2 = len(PACKETS_2)
    with IN_FILE_1.open("rb") as FILE_1, IN_FILE_2.open("rb") as FILE_2, out_path.open("wb") as OUT_FI:
        print_control = 0
        w_f = 0
        w_f_s = 0
        idx_1 = 0
        idx_2 = 0
        k = "A"
        skips = 0
        print("XXXXXXXXXXXXXXXX\tOutput\tSkip\tPOS_L\tPOS_R\tSize", end="")
        while True:
            if idx_1 == LEN_1 and idx_2 == LEN_2:
                print("\n__END__")
                break
            if err_count >= 100:
                print("too many Error")
                break
            pktL = PACKETS_1[idx_1]
            pktR = PACKETS_2[idx_2] if idx_2 < LEN_2 else PACKETS_2[-1]

            if pktL.data_hash == pktR.data_hash and idx_1 != LEN_1 - 1:
                FILE_1.seek(pktL.pos)
                OUT_FI.write(FILE_1.read(pktL.size))
                if print_control != 1:
                    print()
                print_control = 1
                w_f += 1
                w_f_s += pktL.size
                k = "A"
                idx_1 += 1
                idx_2 += 1
                print(f"{OA}\t{w_f}\t{skips}\t{idx_1 + 1}\t{idx_2 + 1}\t{w_f_s}", end="\r")
                continue
            if (("L" in k) and idx_1 <= LEN_1 - 1) or (idx_1 < LEN_1 and idx_2 == LEN_2):
                if "S" in k:
                    skips += 1
                    print(f"{OS}\t{w_f}\t{skips}\t{idx_1 + 1}\t{idx_2 + 1}\t{w_f_s}", end="\r")
                else:
                    FILE_1.seek(pktL.pos)
                    OUT_FI.write(FILE_1.read(pktL.size))
                    if print_control != 0:
                        print()
                    print_control = 0
                    w_f += 1
                    w_f_s += pktL.size
                    print(f"{OL}\t{w_f}\t{skips}\t{idx_1 + 1}\t{idx_2 + 1}\t{w_f_s}", end="\r")
                idx_1 += 1
            elif "R" in k:
                if "S" in k:
                    skips += 1
                    print(f"{OS}\t{w_f}\t{skips}\t{idx_1 + 1}\t{idx_2 + 1}\t{w_f_s}", end="\r")
                else:
                    FILE_2.seek(pktR.pos)
                    OUT_FI.write(FILE_2.read(pktR.size))
                    print_control = 2
                    w_f += 1
                    w_f_s += pktR.size
                    if print_control != 2:
                        print()
                    print(f"{OR}\t{w_f}\t{skips}\t{idx_1 + 1}\t{idx_2 + 1}\t{w_f_s}", end="\r")
                idx_2 += 1
            elif k == "A":
                k = input("\nNext:")
            elif idx_1 == LEN_1 and idx_2 == LEN_2:
                break
            elif skips > LEN_1 + LEN_2:
                print("too many skip")
                break
            else:
                err_count += 1
                print("Error")
        OUT_FI.close()
        print()
        print("#\tFrames\t\tSize")
        print(f"A\t{LEN_1}\t\t{os.stat(IN_FILE_1).st_size}")
        print(f"B\t{LEN_2}\t\t{os.stat(IN_FILE_2).st_size}")
        print(f"Sum\t{LEN_1 + LEN_2}\t\t{os.stat(IN_FILE_1).st_size + os.stat(IN_FILE_2).st_size}")
        print(f"F\t{w_f}\t\t{w_f_s}")


if __name__ == "__main__":
    _main()
