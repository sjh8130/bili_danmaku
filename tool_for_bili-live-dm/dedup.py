import binascii
import gc
import json
import os
import sys
import time
from typing import Any

try:
    import simdjson
except ImportError:
    simdjson = json
# import numba
from loguru import logger
from tqdm import tqdm

_E_MD5 = "d41d8cd98f00b204e9800998ecf8427e"
_log = logger.bind(user="deduplicate jsonl")
_deduplicate_dict: set[str] = set()


def check_username(uname: str) -> bool:
    """if is-censored: return true"""
    return len(uname) == 4 and uname[1:] == "***"


def gift_id_recover(
    batch_combo_id: str = "",
    combo_id: str = "",
    uid: int = 0,
) -> tuple[str, str]:
    """decensor gift_id"""
    a = combo_id.split(":")
    b = batch_combo_id.split(":")
    if batch_combo_id and _E_MD5 in batch_combo_id:
        b[3] = binascii.a2b_hex(b[3][:-32]).decode()
    if combo_id and _E_MD5 in combo_id:
        a[2] = binascii.a2b_hex(a[2][:-32]).decode()
    return ":".join(b), ":".join(a)


def gift_id_enc(
    batch_combo_id: str = "",
    combo_id: str = "",
    uid: int = 0,
) -> tuple[str, str]:
    """re-censor gift_id"""
    a = combo_id.split(":")
    b = batch_combo_id.split(":")
    if combo_id and _E_MD5 not in combo_id:
        a[2] = binascii.b2a_hex(a[2].encode()).decode() + _E_MD5
    if batch_combo_id and _E_MD5 not in batch_combo_id:
        b[3] = binascii.b2a_hex(b[3].encode()).decode() + _E_MD5
    return ":".join(b), ":".join(a)


# @numba.jit(cache=True)
def _deduplicate_it(itm: dict[str, dict], has_timestamp: bool) -> bool:
    """if exist: return false"""
    id_1: str
    id_2: str = ""
    dm_id_str: str
    cmd: str = itm["cmd"]  # type:ignore
    data: dict[str, Any] = itm.get("data", None)  # type:ignore
    msg_id = str(itm.get("msg_id", 0))
    match cmd:
        # sort by hot-spot
        case "DANMU_MSG" | "DANMU_MSG:4:0:2:2:2:0":
            dm_id_str = simdjson.loads(itm["info"][0][15]["extra"]).get("id_str", "")
            id_1 = f"""{cmd}${itm["info"][0][7]}${itm["info"][0][4]}${itm["info"][0][5]}${itm["info"][9]["ct"]}${itm["info"][9]["ts"]}${itm["info"][2][0]}${itm["info"][2][1]}${dm_id_str}${msg_id}"""
            # mid_hash,time.Now().Unix(),rnd,ct,ts,uid,uname,extra:dm_id_str,msg_id
            if not (itm["info"][2][1] == 0 and check_username(itm["info"][2][0])):
                id_2 = f"""{cmd}${itm["info"][0][7]}${itm["info"][0][4]}${itm["info"][0][5]}${itm["info"][9]["ct"]}${itm["info"][9]["ts"]}$0${(itm["info"][2][1][0]+'***')if itm['info'][2][1]else ''}${dm_id_str}${msg_id}"""
        case "INTERACT_WORD":
            id_1 = f"""{cmd}${data["roomid"]}${data["score"]}${data["timestamp"]}${data["trigger_time"]}${data.get("uid", 0)}${data["uname"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                id_2 = f"""{cmd}${data["roomid"]}${data["score"]}${data["timestamp"]}${data["trigger_time"]}$0${data["uname"][0]}***${msg_id}"""
        case "SEND_GIFT":
            id_1 = f"""{cmd}${data["rnd"]}${data.get("uid", 0)}${data["uname"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                id_2 = f"""{cmd}${data["rnd"]}$0${data["uname"][0]}***${msg_id}"""
        case "COMBO_SEND":
            id_1 = f"""{cmd}${data["batch_combo_id"]}${data["combo_id"]}${msg_id}"""
            # _t1, _t2 = gift_id_recover(data["batch_combo_id"], data["combo_id"])
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                _bcid, _cid = gift_id_enc(data["batch_combo_id"], data["combo_id"])
                id_2 = f"""{cmd}${_bcid}${_cid}${msg_id}"""
            else:
                id_2 = ""
        case "ENTRY_EFFECT" | "ENTRY_EFFECT_MUST_RECEIVE":
            id_1 = f"""{cmd}${data["trigger_time"]}${data.get("uid", 0)}${data["target_id"]}${msg_id}"""
        case "COMBO_END":
            id_1 = f"""{cmd}${data["start_time"]}${data["end_time"]}${data["ruid"]}${data.get("uid", 0)}${msg_id}"""
        case "SUPER_CHAT_MESSAGE":
            id_1 = f"""{cmd}${data["id"]}${data.get("uid", 0)}${data["user_info"]["uname"]}${data["message"]}${data["message_trans"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["user_info"]["uname"])):
                return True
        case "SUPER_CHAT_MESSAGE_JPN":
            id_1 = f"""{cmd}${data["id"]}${data.get("uid", 0)}${data["user_info"]["uname"]}${data["message"]}${data["message_jpn"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["user_info"]["uname"])):
                return True
        case "ANCHOR_LOT_AWARD" | "ANCHOR_LOT_END" | "ANCHOR_LOT_START":
            id_1 = f"""{cmd}${data["id"]}${msg_id}"""
        case "RANK_REM":
            id_1 = f"""{cmd}${data["time"]}${data.get("uid", 0)}${data["ruid"]}${msg_id}"""
        case "GUARD_BUY":
            id_1 = f"""{cmd}${data["start_time"]}${data.get("uid", 0)}${itm['data']["num"]}${msg_id}"""
        case "DANMU_MSG:3:7:1:1:1:1":
            id_1 = f"""{cmd}${itm["info"][0][4]}${msg_id}"""
        case (
            "POPULARITY_RED_POCKET_NEW"
            | "POPULARITY_RED_POCKET_START"
            | "POPULARITY_RED_POCKET_V2_NEW"
            | "POPULARITY_RED_POCKET_V2_START"
            | "POPULARITY_RED_POCKET_V2_WINNER_LIST"
            | "POPULARITY_RED_POCKET_WINNER_LIST"
        ):
            id_1 = f"""{cmd}${data["lot_id"]}${msg_id}"""
        case "USER_TOAST_MSG":
            id_1 = f"""{cmd}${data["payflow_id"]}${data.get("uid", 0)}${msg_id}"""
        case "COMMON_ANIMATION":
            id_1 = f"""{cmd}${data["order_id"]}${data.get("uid", 0)}${msg_id}"""
        case "LIVE_INTERACTIVE_GAME" | "LIVE_OPEN_PLATFORM_GAME" | "RECOMMEND_CARD" | "SPREAD_SHOW_FEET_V2":
            id_1 = f"""{cmd}${data["timestamp"]}${msg_id}"""
        case "DANMU_AGGREGATION":
            id_1 = f"""{cmd}${data["timestamp"]}${data["activity_identity"]}${msg_id}"""
        case "WIDGET_BANNER" | "ROOM_BANNER":
            id_1 = f"""{cmd}${itm["timestamp"]}${msg_id}"""
        case "PK_BATTLE_ENTRANCE":
            id_1 = f"""{cmd}${itm["timestamp"]}${msg_id}"""
        case "PLAY_TAG" | "VOICE_JOIN_STATUS":
            id_1 = f"""{cmd}${data["current_time"]}${msg_id}"""
        case "ROOM_SKIN_MSG":
            id_1 = f"""{cmd}${itm["current_time"]}${msg_id}"""
        case "TRADING_SCORE":
            id_1 = f"""{cmd}${data["update_time"]}${msg_id}"""
        case "WEALTH_NOTIFY":
            id_1 = f"""{cmd}${data["info"]["send_time"]}${msg_id}"""
        case "WIDGET_GIFT_STAR_PROCESS" | "CHG_RANK_REFRESH":
            id_1 = f"""{cmd}${data["version"]}${msg_id}"""
        case "SHOPPING_BUBBLES_STYLE":
            id_1 = f"""{cmd}${data["checksum"]}${msg_id}"""
        case "LIVE_INTERACT_GAME_STATE_CHANGE":
            id_1 = f"""{cmd}${data["game_id"]}${msg_id}"""
        # special:
        case (
            "COMMON_NOTICE_DANMAKU"
            | "GIFT_STAR_PROCESS"
            | "GOTO_BUY_FLOW"
            | "HOT_BUY_NUM"
            | "LIKE_INFO_V3_NOTICE"
            | "LIKE_INFO_V3_UPDATE"
            | "NOTICE_MSG"
            | "ONLINE_RANK_V2"
            | "ROOM_REAL_TIME_MESSAGE_UPDATE"
            | "SUPER_CHAT_MESSAGE_DELETE"
            | "WATCHED_CHANGE"
            | "WIDGET_GIFT_STAR_PROCESS"
        ):
            id_1 = f"""{cmd}${str(data)}${msg_id}"""
        case "USER_TOAST_MSG_V2":
            id_1 = f"""{cmd}${data["pay_info"]["payflow_id"]}${data["sender_uinfo"].get("uid", 0)}${data["sender_uinfo"]["base"]["name"]}${data["receiver_uinfo"].get("uid", 0)}${data["receiver_uinfo"]["base"]["name"]}${msg_id}"""
        case "WIDGET_WISH_INFO":
            id_1 = f"""{cmd}${data["ts"]}${data["sid"]}${data["tid"]}${msg_id}"""
        case (
            "AREA_RANK_CHANGED"
            | "GUARD_HONOR_THOUSAND"
            | "HOT_ROOM_NOTIFY"
            | "LOG_IN_NOTICE"
            | "ONLINE_RANK_TOP3"
            | "POPULAR_RANK_CHANGED"
            | "RANK_CHANGED"
            | "REVENUE_RANK_CHANGED"
            | "STOP_LIVE_ROOM_LIST"
            | "SUPER_CHAT_ENTRANCE"
        ):
            return False
        case (
            "ACTIVITY_BANNER_CHANGE_V2"
            | "ACTIVITY_BANNER_CHANGE"
            | "ADMIN_SHIELD_KEYWORD"
            | "ANCHOR_BROADCAST"
            | "ANCHOR_ECOMMERCE_STATUS"
            | "ANCHOR_HELPER_DANMU"
            | "ANCHOR_LOT_CHECKSTATUS"
            | "ANCHOR_LOT_NOTICE"
            | "BENEFIT_CARD_CLEAN"
            | "CARD_MSG"
            | "CHANGE_ROOM_INFO"
            | "CUT_OFF"
            | "FULL_SCREEN_SPECIAL_EFFECT"
            | "GIFT_PANEL_PLAN"
            | "GUARD_ACHIEVEMENT_ROOM"
            | "LIVE_ANI_RES_UPDATE"
            | "LIVE_PANEL_CHANGE_CONTENT"
            | "LIVE_PANEL_CHANGE"
            | "LIVE"
            | "MESSAGEBOX_USER_GAIN_MEDAL"
            | "OBS_SHIELD_STATUS_UPDATE"
            | "PLAYTOGETHER_ICON_CHANGE"
            | "POPULAR_RANK_GUIDE_CARD"
            | "POPULARITY_RANK_TAB_CHG"
            | "PREPARING"
            | "RECALL_DANMU_MSG"
            | "RING_STATUS_CHANGE_V2"
            | "RING_STATUS_CHANGE"
            | "room_admin_entrance"
            | "ROOM_ADMIN_REVOKE"
            | "ROOM_ADMINS"
            | "ROOM_BLOCK_MSG"
            | "ROOM_CHANGE"
            | "ROOM_SILENT_OFF"
            | "ROOM_SILENT_ON"
            | "SHOPPING_CART_SHOW"
            | "STUDIO_ROOM_CLOSE"
            | "SYS_MSG"
            | "VOICE_CHAT_UPDATE"
            | "VOICE_JOIN_LIST"
            | "VOICE_JOIN_ROOM_COUNT_INFO"
            | "WARNING"
        ):
            return True
        case _:
            tqdm.write(cmd)
            id_1 = ""
            # return True
    if (id_1 and id_1 in _deduplicate_dict) or (id_2 and id_2 in _deduplicate_dict):
        return False
    else:
        _deduplicate_dict.add(id_1) if id_1 else ...
        _deduplicate_dict.add(id_2) if id_2 else ...
        # _deduplicate_dict.add(str(itm))
        return True


def _deduplicate(in_path: str):
    with open(in_path, "r", 1048576, encoding="utf-8") as input_file:
        a = input_file.readlines()
        _total = len(a)
    with open(in_path + "_DEDUP", "w", 50 * 2**20, "utf-8") as output_file:
        for line in tqdm(a, leave=False, desc=f"{os.path.basename(in_path)} ", position=1):
            if line in _deduplicate_dict:
                continue
            pos = line.find("{")
            itm: dict = simdjson.loads(line[pos:])  # type:ignore
            if _deduplicate_it(itm, bool(pos)):
                output_file.write(line)
            _deduplicate_dict.add(line)
    return _total


if __name__ == "__main__":
    files_to_process = sys.argv[1:]
    try:
        for file in tqdm(files_to_process, leave=False, position=0):
            st = time.time()
            _deduplicate_dict.clear()
            gc.collect(2)
            gc.collect(1)
            gc.collect(0)
            total = _deduplicate(file)
            total_time = time.time() - st
            tqdm.write(f"{file}:{total_time:.3f}s, {(total/total_time):.0f} lines/s")
            # print(f"{file}:{total_time:.3f}s, {(total/total_time):.0f} lines/s")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        _log.exception(e)
    finally:
        print("Done")
        time.sleep(30)
