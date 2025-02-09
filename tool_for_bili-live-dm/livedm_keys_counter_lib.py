# cython:language_level=3
import json
import os
from pathlib import Path
from types import NoneType

import json5
from tqdm import tqdm

result: dict[str, dict[str, dict]] = {}
SWITCH_1: bool = False
IGNORE_LIST = set()
SWITCH_2: bool = False
DONT_CARE_INDEX_LIST = set()
STR_LIST = set()
SWITCH_3: bool = False
try:
    with open("livedm_keys_not_interest.json") as fp:
        _D1: dict[str, list[str]] = json5.load(fp)
except FileNotFoundError:
    pass
else:
    try:
        STR_LIST = set(_D1["STR_LIST"])
        SWITCH_3 = True
    except KeyError:
        pass
    try:
        DONT_CARE_INDEX_LIST: set[str] = set(_D1["DONT_CARE_INDEX_LIST"])
        SWITCH_1 = True
    except KeyError:
        pass
    try:
        IGNORE_LIST: set[str] = set(_D1["IGNORE_LIST"])
        SWITCH_2 = True
    except KeyError:
        pass


def _analyze_structure(cmd: str, item: int | str | list | dict | bool | NoneType, target_key="", /):
    final_key: str = f"{cmd}{target_key}"
    _typ: str = type(item).__name__
    if SWITCH_3 and final_key in STR_LIST:
        item = json.loads(item)  # type:ignore[reportArgumentType]
        _typ = "str_dict"
    if result.get(final_key) is None:
        result[final_key] = {"type": {}}
    if _typ not in result[final_key]["type"]:
        result[final_key]["type"][_typ] = result[final_key]["type"].get(_typ, 0) + 1
    if isinstance(item, dict):
        for key, value in item.items():
            _tk: str = f"{target_key}.{key}"
            if target_key == ".info[0][15].extra.emots":
                _tk = f"{target_key}.ANY"
            _analyze_structure(cmd, value, _tk)
    elif isinstance(item, list):
        for index, list_item in enumerate(item):
            _tk = f"{target_key}[IDX]" if SWITCH_2 and final_key in DONT_CARE_INDEX_LIST else f"{target_key}[{index}]"
            _analyze_structure(cmd, list_item, _tk)
    if final_key in (f"{cmd}.cmd", f"{cmd}.msg_id", f"{cmd}.send_time", cmd):
        return
    if isinstance(item, (dict, list)):
        return
    if SWITCH_1 and final_key in IGNORE_LIST:
        return
    if result[final_key].get("value") is None:
        result[final_key]["value"] = {}
    t1: str = repr(item)
    if result[final_key]["value"].get(t1) is None:
        result[final_key]["value"][t1] = 0
    result[final_key]["value"][t1] = result[final_key]["value"][t1] + 1


def p_main(in_path: str | Path):
    with open(in_path, "r", encoding="utf-8") as file_in:
        for line in tqdm(file_in.readlines(), leave=False, desc=f"{os.path.basename(in_path)}"):
            try:
                item: dict = json.loads(line[line.find("{") :])
            except json.JSONDecodeError:
                continue
            _analyze_structure(item["cmd"], item)
    return result
