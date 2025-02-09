import gc
import json
import os
import sys
import time

from loguru import logger
from tqdm import tqdm

_log = logger.bind(user="deduplicate jsonl")
_deduplicate_dict: dict[str, set[str]] = {}


def _deduplicate_it(itm: dict) -> bool:
    """if exist: return false"""
    xid: str
    cmd = itm["cmd"]
    if cmd not in _deduplicate_dict:
        _deduplicate_dict[cmd] = set()
    match cmd:
        # sort by hot-spot
        case "DANMU_MSG":
            if (xid := f"""{itm["info"][0][7]}${itm["info"][0][4]}${itm["info"][0][5]}${itm["info"][9]["ct"]}${itm["info"][9]["ts"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "INTERACT_WORD":
            if (xid := f"""{itm["data"]["roomid"]}${itm["data"]["score"]}${itm["data"]["timestamp"]}${itm["data"]["trigger_time"]}${itm["data"]["uid"]}${itm["data"]["uname"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "SEND_GIFT":
            if itm["data"]["rnd"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["rnd"])
                return True
        case "COMBO_SEND":
            if itm["data"]["batch_combo_id"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["batch_combo_id"])
                return True
        case "ENTRY_EFFECT":
            if (xid := f"""{itm["data"]["trigger_time"]}${itm["data"]["uid"]}${itm["data"]["target_id"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "COMBO_END":
            if (xid := f"""{itm["data"]["start_time"]}${itm["data"]["end_time"]}${itm["data"]["ruid"]}${itm["data"]["uid"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "SUPER_CHAT_MESSAGE_JPN" | "SUPER_CHAT_MESSAGE" | "ANCHOR_LOT_AWARD" | "ANCHOR_LOT_CHECKSTATUS" | "ANCHOR_LOT_END" | "ANCHOR_LOT_START":
            if itm["data"]["id"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["id"])
                return True
        case "RANK_REM":
            if (xid := f"""{itm["data"]["time"]}${itm["data"]["uid"]}${itm["data"]["ruid"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "GUARD_BUY":
            if (xid := f"""{itm["data"]["start_time"]}${itm["data"]["uid"]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "DANMU_MSG:3:7:1:1:1:1":
            if (xid := f"""{itm["info"][0][4]}""") in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(xid)
                return True
        case "POPULARITY_RED_POCKET_NEW" | "POPULARITY_RED_POCKET_START" | "POPULARITY_RED_POCKET_V2_NEW" | "POPULARITY_RED_POCKET_V2_START" | "POPULARITY_RED_POCKET_V2_WINNER_LIST" | "POPULARITY_RED_POCKET_WINNER_LIST":
            if itm["data"]["lot_id"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["lot_id"])
                return True
        case "USER_TOAST_MSG":
            if itm["data"]["payflow_id"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["payflow_id"])
                return True
        case "AREA_RANK_CHANGED" | "DANMU_AGGREGATION" | "LIVE_INTERACTIVE_GAME" | "LIVE_OPEN_PLATFORM_GAME" | "RECOMMEND_CARD" | "SPREAD_SHOW_FEET_V2":
            if itm["data"]["timestamp"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["timestamp"])
                return True
        case "PK_BATTLE_ENTRANCE":
            if itm["timestamp"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["timestamp"])
                return True
        case "PLAY_TAG" | "VOICE_JOIN_STATUS":
            if itm["data"]["current_time"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["current_time"])
                return True
        case "ROOM_SKIN_MSG":
            if itm["current_time"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["current_time"])
                return True
        case "TRADING_SCORE":
            if itm["data"]["update_time"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["update_time"])
                return True
        case "WEALTH_NOTIFY":
            if itm["data"]["send_time"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["send_time"])
                return True
        case "WIDGET_GIFT_STAR_PROCESS":
            if itm["data"]["version"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["version"])
                return True
        case "POPULAR_RANK_CHANGED":
            if itm["data"]["cache_key"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["cache_key"])
                return True
        case "SHOPPING_BUBBLES_STYLE":
            if itm["data"]["checksum"] in _deduplicate_dict[cmd]:
                return False
            else:
                _deduplicate_dict[cmd].add(itm["data"]["checksum"])
                return True
        case _:
            return True
    return True


def _deduplicate(in_path: str):
    with open(in_path, "r", 1048576, encoding="utf-8") as input_file, open(in_path + "_DEDUP", "w", 10485760, "utf-8") as output_file:
        for line in tqdm(input_file.readlines(), leave=False, desc=f"{os.path.basename(in_path)} "):
            ls = line.find("{")
            itm: dict = json.loads(line[ls:])
            if _deduplicate_it(itm):
                output_file.write(line)


if __name__ == "__main__":
    files_to_process = sys.argv[1:]
    try:
        for file in files_to_process:
            st = time.time()
            _deduplicate_dict.clear()
            gc.collect(0)
            gc.collect(1)
            gc.collect(2)
            _deduplicate(file)
            print(f"{time.time()-st:.3f}: {file}")
    except KeyboardInterrupt:
        print()
    except Exception as e:
        _log.exception(e)
    finally:
        time.sleep(10)
