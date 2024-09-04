import json
import time
import sys


def main(in_paths, out_path):
    line: str
    left_pos = 0
    l_line: dict
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
    for in_path in in_paths:
        print(in_path)
        if in_path == out_path:
            continue
        with open(in_path, "r", encoding="utf-8") as file_in:
            for line in file_in.readlines():
                left_pos = line.find("{")
                l_line = json.loads(line[left_pos:-1])
                cmd = l_line["cmd"]
                try:
                    final_write[cmd] += 1
                except KeyError:
                    final_write[cmd] = 1
    with open(out_path, "w", encoding="utf-8") as file_io:
        json.dump(final_write, file_io, ensure_ascii=False, indent="\t")


if __name__ == "__main__":
    in_path = sys.argv[1:]
    out_path = "Z:\\test.json"
    start_time = time.time()
    main(in_path, out_path)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(5)
