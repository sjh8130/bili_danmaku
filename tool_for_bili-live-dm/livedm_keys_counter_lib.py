# cython:language_level=3
import json
from pathlib import Path
from typing import Any

from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json

result: dict[str, dict[str, dict[str, Any]]] = {}
SW1: bool = False
SW2: bool = False
SW3: bool = False
try:
    with Path("livedm_keys_not_interest.json").open(encoding="utf-8") as fp:
        _D1: dict[str, list[str]] = simdjson.load(fp)
except FileNotFoundError:
    pass
else:
    try:
        STR_LIST = set(_D1["STR_LIST"])
        SW3 = True
    except KeyError:
        STR_LIST = set()
    try:
        DONT_CARE_INDEX_LIST: set[str] = set(_D1["DONT_CARE_INDEX_LIST"])
        SW1 = True
    except KeyError:
        DONT_CARE_INDEX_LIST = set()
    try:
        IGNORE_LIST: set[str] = set(_D1["IGNORE_LIST"])
        SW2 = True
    except KeyError:
        IGNORE_LIST = set()


def _a(cmd: str, item: int | str | list[Any] | dict[str, Any] | bool | None, tk: str = "", /):  # noqa: FBT001
    fk: str = f"{cmd}{tk}"
    typ: str = type(item).__name__
    if SW3 and fk in STR_LIST:
        item = simdjson.loads(item)  # pyright: ignore[reportArgumentType]
        typ = "str_dict"
    if result.get(fk) is None:
        result[fk] = {"type": {}}
    if typ not in result[fk]["type"]:
        result[fk]["type"][typ] = result[fk]["type"].get(typ, 0) + 1
    if isinstance(item, dict):
        for key, value in item.items():
            tk2: str = f"{tk}.{key}"
            if tk == ".info[0][15].extra.emots":
                tk2 = f"{tk}.ANY"
            _a(cmd, value, tk2)
    elif isinstance(item, list):
        for index, list_item in enumerate(item):
            tk2 = f"{tk}[IDX]" if SW2 and fk in DONT_CARE_INDEX_LIST else f"{tk}[{index}]"
            _a(cmd, list_item, tk2)
    if fk in {f"{cmd}.cmd", f"{cmd}.msg_id", f"{cmd}.send_time", cmd}:
        return
    if isinstance(item, (dict, list)):
        return
    if SW1 and fk in IGNORE_LIST:
        return
    if result[fk].get("value") is None:
        result[fk]["value"] = {}
    t1: str = repr(item)
    if result[fk]["value"].get(t1) is None:
        result[fk]["value"][t1] = 0
    result[fk]["value"][t1] += 1


def p_main(in_path: Path) -> dict[str, Any]:
    with in_path.open(encoding="utf-8") as file_in:
        for line in tqdm(file_in.readlines(), leave=False, desc=in_path.name):
            try:
                lp = line.find("{")
                if lp:
                    item: dict = simdjson.loads(line[lp:])
                else:
                    item: dict = simdjson.loads(line)
                # item: dict = simdjson.loads(line[line.find("{") :])
            except Exception:  # noqa: BLE001, S112
                continue
            _a(item["cmd"], item)
    return result
