import json
import sys
import time
from pathlib import Path
from typing import Any

from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json  # type:ignore

_cmd_count: dict[str, int] = {}


def _p1() -> None:
    try:
        with _out_path.open(encoding="utf-8") as file_io:
            _cmd_count.update(simdjson.load(file_io))  # type:ignore
    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        if e.args[0] == "Expecting value: line 1 column 1 (char 0)":
            pass
        else:
            raise e


def _p2() -> None:
    with _out_path.open("w", encoding="utf-8") as file_io:
        json.dump(_cmd_count, file_io, ensure_ascii=False, indent="\t", sort_keys=True)


def _main(in_paths: list[str]) -> None:
    if in_paths == []:
        return
    for in_path_s in in_paths:
        in_path = Path(in_path_s)
        # print(in_path)
        if in_path == _out_path:
            continue
        is_err = False
        lineno = 1
        with in_path.open(encoding="utf-8") as file_in:
            for line in tqdm(file_in.readlines(), leave=False, desc=in_path.name):
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
    _out_path = Path("Z:\\CMD_count.json")
    _st = time.time()
    _p1()
    _main(_in_path)
    _p2()
    _et = time.time() - _st
    print(f"处理完成，耗时：{_et:.3f}秒")
    time.sleep(5)
