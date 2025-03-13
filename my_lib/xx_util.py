import json
from enum import IntEnum, auto


class OPR(IntEnum):
    EQ = auto()
    NEQ = auto()
    GT = auto()
    LT = auto()
    GEQ = auto()
    LEQ = auto()
    ANY = auto()
    IN = auto()
    NIN = auto()
    IS = auto()
    NIS = auto()


def sort_str_list(s: str, /) -> str:
    """example: '1,3,2,4,5' -> '1,2,3,4,5'"""
    if s.count(",") == 0:
        return s
    a = json.loads(f"[{s}]")
    b = sorted(a)
    return ",".join(str(c) for c in b)


def sort_list_dict(
    ld: list[dict],
    k1: str = "item_id",
    k2: str = "name",
    /,
) -> list[dict]:
    items_with_k1 = [item for item in ld if item[k1] not in {0, "0"}]
    items_with_k2 = [item for item in ld if item[k1] in {0, "0"}]
    items_with_k1.sort(key=lambda x: x[k1])
    items_with_k2.sort(key=lambda x: x[k2])
    return items_with_k1 + items_with_k2


def sort_p6_emoji(ld: list[dict], /) -> list[dict]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict):
            if isinstance(ld[i]["properties"].get("item_ids"), str):
                ld[i]["properties"]["item_ids"] = sort_str_list(
                    ld[i]["properties"]["item_ids"]
                )
        ld[i]["items"] = sort_list_dict(ld[i]["items"])
    return ld


def del_keys(d: dict, k: str, v=None, operator: OPR = OPR.EQ, recursive=True):
    if (
        isinstance(d, dict)
        and k in d
        and (type(d[k]) is type(v) or operator in (OPR.IN, OPR.ANY))
    ):
        match operator:
            case OPR.EQ:
                if d[k] == v:
                    d.pop(k)
            case OPR.IN:
                if d[k] in v:  # type: ignore
                    d.pop(k)
            case OPR.ANY:
                d.pop(k)
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
                if d[k] != v:
                    d.pop(k)
            case OPR.NIN:
                if d[k] not in v:
                    d.pop(k)
            case OPR.IS:
                if d[k] is v:
                    d.pop(k)
            case OPR.NIS:
                if d[k] is not v:
                    d.pop(k)
            case _:
                raise Exception("*ToDo")
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            del_keys(d[key], k, v, operator)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    del_keys(item, k, v, operator)
