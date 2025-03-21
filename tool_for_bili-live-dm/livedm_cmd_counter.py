import json
import os
import sys
import time
from typing import Any

from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json

_cmd_count: dict[str, int] = {}


def _p1():
    try:
        with open(_out_path, "r", encoding="utf-8") as file_io:
            _cmd_count.update(simdjson.load(file_io))
    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        if e.args[0] == "Expecting value: line 1 column 1 (char 0)":
            pass
        else:
            raise e


def _p2():
    with open(_out_path, "w", encoding="utf-8") as file_io:
        json.dump(_cmd_count, file_io, ensure_ascii=False, indent="\t", sort_keys=True)


def _main(in_paths):
    if in_paths == []:
        return
    for in_path in in_paths:
        # print(in_path)
        if in_path == _out_path:
            continue
        is_err = False
        lineno = 1
        with open(in_path, "r", encoding="utf-8") as file_in:
            for line in tqdm(file_in.readlines(), leave=False, desc=f"{os.path.basename(in_path)}"):
                lineno += 1
                left_pos = line.find("{")
                try:
                    l_line: dict[str, Any] = json.loads(line[left_pos:])
                except json.JSONDecodeError as e:
                    print(lineno)
                    print(e)
                    if not is_err:
                        print(in_path)
                        is_err = True
                    continue
                cmd = l_line["cmd"]
                _cmd_count[cmd] = _cmd_count.get(cmd, 0) + 1


if __name__ == "__main__":
    _in_path = sys.argv[1:]
    _out_path = "Z:\\CMD_count.json"
    _st = time.time()
    _p1()
    _main(_in_path)
    _p2()
    _et = time.time() - _st
    print(f"处理完成，耗时：{_et:.3f}秒")
    time.sleep(5)
