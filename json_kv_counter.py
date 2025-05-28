import json
import os
import sys
import time
from pathlib import Path

from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json  # type:ignore

result: dict[str, dict[str, dict]] = {}
DONT_CARE_INDEX_LIST = {
    "root.elems",
    "root.colorfulSrc",
    "root.segmentRules",
}


def _a(item: int | str | list | dict | bool | None, target_key: str = "root") -> None:
    _typ: str = type(item).__name__
    if result.get(target_key) is None:
        result[target_key] = {"type": {}}
    if _typ not in result[target_key]["type"]:
        result[target_key]["type"][_typ] = result[target_key]["type"].get(_typ, 0) + 1
    if isinstance(item, dict):
        for key, value in item.items():
            tk2: str = f"{target_key}.{key}"
            _a(value, tk2)
    elif isinstance(item, list):
        for index, list_item in enumerate(item):
            tk2 = f"{target_key}[X]" if target_key in DONT_CARE_INDEX_LIST else f"{target_key}[{index}]"
            _a(list_item, tk2)
    if isinstance(item, (dict, list)):
        return
    if result[target_key].get("value") is None:
        result[target_key]["value"] = {}
    t1: str = repr(item)
    if result[target_key]["value"].get(t1) is None:
        result[target_key]["value"][t1] = 0
    result[target_key]["value"][t1] = result[target_key]["value"][t1] + 1


def _b(ii: str | Path):
    with open(ii, encoding="utf-8") as fp:
        item: dict = simdjson.load(fp)  # type:ignore
        _a(item)
    return result


def main() -> None:
    p1 = "json_kvs.json"
    if True and os.path.exists(os.path.join(od, p1)):
        with open(os.path.join(od, p1), encoding="utf-8") as fp:
            result.update(simdjson.load(fp))  # type:ignore
    for path in tqdm(paths, leave=False):
        if not os.path.exists(od):
            os.makedirs(od)
        if path == od:
            continue
        _b(path)
    with open(os.path.join(od, p1), "w", encoding="utf-8") as fp:
        json.dump(
            result,
            fp,
            ensure_ascii=False,
            indent="\t",
            sort_keys=True,
        )


if __name__ == "__main__":
    paths = sys.argv[1:]
    od = "Z:\\" if os.name == "nt" else "/mnt/z/"
    start_time = time.time()
    main()
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    time.sleep(10)
