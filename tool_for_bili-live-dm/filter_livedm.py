import json
import os
import sys
import time

from filters import FILTER_MID, FILTER_MID_HASH_STR_LOWER, FILTER_WORDS
from tqdm import tqdm


def main(in_paths: list[str], out_path: str):
    line: str
    left_pos = 0
    if not in_paths:
        return
    try:
        with open(out_path, "r", encoding="utf-8") as file_io:
            final_write = json.load(file_io)
    except FileNotFoundError:
        final_write = {}
    except json.JSONDecodeError as e:
        if e.args[0] == "Expecting value: line 1 column 1 (char 0)":
            final_write = {}
        else:
            raise
    len_i = len(in_paths)
    p_i = 1
    for in_path in in_paths:
        f_s = f"{p_i}/{len_i}"
        p_i += 1
        is_err = False
        lineno = 1
        if in_path == out_path:
            continue
        with open(in_path, "r", encoding="utf-8") as file_in:
            for line in tqdm(
                file_in.readlines(),
                unit="line",
                bar_format="{desc}{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} ",
                desc=f"{f_s:8} {os.path.basename(in_path)} ",
            ):
                # if "DANMU_MSG" not in line:
                #     continue
                # if line.find("DANMU_MSG:3:7:1:1:1:1") == 1:
                #     continue
                lineno += 1
                left_pos = line.find("{")
                try:
                    cmd: dict = json.loads(line[left_pos:])
                except json.JSONDecodeError:
                    print(lineno)
                    if not is_err:
                        print(in_path)
                        is_err = True
                    continue
                if cmd["cmd"] != "DANMU_MSG":
                    continue
                # if cmd["info"][0][9] != 0:
                #     continue  # 1:节奏风暴 2:天选时刻 9:弹幕互动游戏
                # if cmd["info"][0][12] != 0:
                #     continue  # 0:文本 1:表情包 2:语音
                if cmd["info"][0][7] in FILTER_MID_HASH_STR_LOWER:
                    continue
                if cmd["info"][2][0] in FILTER_MID:
                    continue
                dm_text: str = (
                    cmd["info"][1]
                    .replace("\u007f", "")
                    .replace("\u00a0", "")
                    .replace("\u2006", "")
                    .replace("\u200b", "")
                    .replace("\u200e", "")
                    .replace("\u2060", "")
                    .replace("\u2063", "")
                    .replace("\u3000", "")
                    .replace("\U000e0020", "")
                    .strip()
                )
                if dm_text in FILTER_WORDS or dm_text.lower() in FILTER_WORDS:
                    try:
                        del final_write[dm_text]
                    except KeyError:
                        pass
                    continue
                else:
                    try:
                        if cmd["info"][0][15]["extra"].find('"hit_combo":1') >= 1:
                            continue
                    except KeyError:
                        pass
                    try:
                        final_write[dm_text] += 1
                    except KeyError:
                        final_write[dm_text] = 1
    with open(out_path, "w", encoding="utf-8") as file_io:
        json.dump(final_write, file_io, ensure_ascii=False, indent="\t", sort_keys=True)


if __name__ == "__main__":
    in_path = sys.argv[1:]
    out_path = "Z:\\test.json"
    start_time = time.time()
    main(in_path, out_path)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(5)
