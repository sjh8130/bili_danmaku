from collections.abc import Mapping, Sequence
from enum import IntEnum, auto
from typing import Any

try:
    import simdjson as json
except ImportError:
    import json

FALSE_CMP = [0, "", [], False, {}, None, set(), frozenset()]


class OPR(IntEnum):
    EQ = auto()
    "=="
    NEQ = auto()
    "!="
    GT = auto()
    ">"
    LT = auto()
    "<"
    GEQ = auto()
    ">="
    LEQ = auto()
    "<="
    ANY = auto()
    IN = auto()
    NIN = auto()
    "not in"
    IS = auto()
    NIS = auto()
    "not is"
    FALSE_CMP = auto()
    "false compare"


def sort_str_list(s: str, /) -> str:
    """example: `'1,3,2,4,5'` -> `'1,2,3,4,5'`"""
    if s.count(",") == 0:
        return s
    a = json.loads(f"[{s}]")
    b = sorted(set(a))
    return ",".join(str(c) for c in b)


def sort_list_dict(ld: Sequence[Mapping[str, Any]], k1: str = "item_id", k2: str = "name") -> Sequence[Mapping[Any, Any]]:
    list_temp = [json.loads(i2) for i2 in sorted(json.dumps(item) for item in ld)]
    items_with_k1 = [item for item in list_temp if item[k1] not in {0, "0"}]
    items_with_k2 = [item for item in list_temp if item[k1] in {0, "0"}]
    items_with_k1.sort(key=lambda x: x[k1])  # noqa: FURB118
    items_with_k2.sort(key=lambda x: x[k2])  # noqa: FURB118
    ld[:] = items_with_k1 + items_with_k2  # pyright: ignore[reportIndexIssue]
    return items_with_k1 + items_with_k2


def sort_p6_emoji(ld: list[Mapping[Any, Any]], /) -> list[Mapping[Any, Any]]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict) and isinstance(ld[i]["properties"].get("item_ids"), str):
            ld[i]["properties"]["item_ids"] = sort_str_list(ld[i]["properties"]["item_ids"])
        sort_list_dict(ld[i]["items"])
    return ld


def del_keys(d: Mapping[str, Any], k: str, v: Any = None, operator: OPR = OPR.EQ, *, recursive=True) -> None:
    if isinstance(d, dict) and k in d and (type(d[k]) is type(v) or operator in {OPR.IN, OPR.ANY, OPR.FALSE_CMP}):
        match operator:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN:
                if d.get(k) in v:
                    d.pop(k, None)
            case OPR.FALSE_CMP:
                if d.get(k) in FALSE_CMP:
                    d.pop(k, None)
            case OPR.ANY:
                d.pop(k, None)
            case OPR.GT:
                if isinstance(d[k], (int, float)) and d[k] > v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LT:
                if isinstance(d[k], (int, float)) and d[k] < v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.GEQ:
                if isinstance(d[k], (int, float)) and d[k] >= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LEQ:
                if isinstance(d[k], (int, float)) and d[k] <= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.NEQ:
                if d.get(k) != v:
                    d.pop(k)
            case OPR.NIN:
                if d[k] not in v:
                    d.pop(k)
            case OPR.IS:
                if d.get(k) is v:
                    d.pop(k)
            case OPR.NIS:
                if d.get(k) is not v:
                    d.pop(k)
            case _:
                raise Exception("*ToDo")
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            del_keys(d[key], k, v, operator, recursive=recursive)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    del_keys(item, k, v, operator, recursive=recursive)


def replace_str(d: Mapping[Any, Any] | list[str], old: str, new: str, count: int = -1, *, recursive: bool = True) -> None:
    if not isinstance(d, (dict, list)):
        return
    if not recursive:
        if isinstance(d, dict):
            for key, val in d.items():
                if isinstance(val, str):
                    d[key] = val.replace(old, new, count)
        elif isinstance(d, list):
            for index, val in enumerate(d):
                if isinstance(val, str):
                    d[index] = val.replace(old, new, count)
        return
    if isinstance(d, dict):
        for key, val in d.items():
            if isinstance(val, str):
                d[key] = val.replace(old, new, count)
            elif isinstance(val, (dict, list)):
                replace_str(val, old, new, count, recursive=recursive)
    elif isinstance(d, list):
        for index, val in enumerate(d):
            if isinstance(val, str):
                d[index] = d[index].replace(old, new, count)
            elif isinstance(val, (dict, list)):
                replace_str(val, old, new, count, recursive=recursive)


def replace_str_regexp(d: Mapping[Any, Any] | list[str], old: str, new: str, count: int = -1, *, recursive: bool = True):
    if not isinstance(d, (dict, list)):
        return
    if not recursive:
        if isinstance(d, dict):
            for key, val in d.items():
                if isinstance(val, str):
                    d[key] = val.replace(old, new, count)
        elif isinstance(d, list):
            for index, val in enumerate(d):
                if isinstance(val, str):
                    d[index] = val.replace(old, new, count)
        return
    if isinstance(d, dict):
        for key, val in d.items():
            if isinstance(val, str):
                d[key] = val.replace(old, new, count)
            elif isinstance(val, (dict, list)):
                replace_str_regexp(val, old, new, count, recursive=recursive)
    elif isinstance(d, list):
        for index, val in enumerate(d):
            if isinstance(val, str):
                d[index] = d[index].replace(old, new, count)
            elif isinstance(val, (dict, list)):
                replace_str_regexp(val, old, new, count, recursive=recursive)
