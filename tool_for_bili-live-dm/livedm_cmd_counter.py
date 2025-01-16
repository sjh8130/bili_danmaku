import json
import sys
import time

from tqdm import tqdm


def main(in_paths, out_path):
    left_pos = 0
    l_line = {}
    if in_paths == []:
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
            raise e
    pbar = tqdm(total=len(in_paths))
    for in_path in in_paths:
        # print(in_path)
        if in_path == out_path:
            continue
        pbar.set_description(in_path)
        is_err = False
        lineno = 1
        with open(in_path, "r", encoding="utf-8") as file_in:
            for line in file_in:
                lineno += 1
                left_pos = line.find("{")
                try:
                    l_line = json.loads(line[left_pos:])
                except json.JSONDecodeError:
                    print(lineno)
                    if not is_err:
                        print(in_path)
                        is_err = True
                finally:
                    pass
                cmd = l_line["cmd"]
                try:
                    final_write[cmd] += 1
                except KeyError:
                    final_write[cmd] = 1
        pbar.update()
    pbar.close()
    with open(out_path, "w", encoding="utf-8") as file_io:
        json.dump(final_write, file_io, ensure_ascii=False, indent="\t")


if __name__ == "__main__":
    in_path = sys.argv[1:]
    out_path = "Z:\\CMD_count.json"
    start_time = time.time()
    main(in_path, out_path)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(5)
