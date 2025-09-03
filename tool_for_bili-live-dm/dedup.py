import binascii
import contextlib
import gc
import json
import sys
import time
from collections.abc import Hashable
from decimal import Decimal
from pathlib import Path
from typing import Any

from loguru import logger
from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json

_E_MD5 = "d41d8cd98f00b204e9800998ecf8427e"
_log = logger.bind(user="deduplicate jsonl")
_deduplicate_dict: set[Hashable] = set()


def check_username(uname: str) -> bool:
    """If is-censored: return true."""
    return len(uname) == 4 and uname[1:] == "***"


def gift_id_recover(batch_combo_id: str = "", combo_id: str = "") -> tuple[str, str]:
    """de-censor gift_id."""
    a = combo_id.split(":")
    b = batch_combo_id.split(":")
    if batch_combo_id and _E_MD5 in batch_combo_id:
        b[3] = binascii.a2b_hex(b[3][:-32]).decode()
    if combo_id and _E_MD5 in combo_id:
        a[2] = binascii.a2b_hex(a[2][:-32]).decode()
    return ":".join(b), ":".join(a)


def gift_id_enc(batch_combo_id: str = "", combo_id: str = "") -> tuple[str, str]:
    """re-censor gift_id."""
    a = combo_id.split(":")
    b = batch_combo_id.split(":")
    if combo_id and _E_MD5 not in combo_id:
        a[2] = binascii.b2a_hex(a[2].encode()).decode() + _E_MD5
    if batch_combo_id and _E_MD5 not in batch_combo_id:
        b[3] = binascii.b2a_hex(b[3].encode()).decode() + _E_MD5
    return ":".join(b), ":".join(a)


def _deduplicate_it(itm: dict[str, Any], timestamp: Decimal, str_itm: str) -> bool:
    """If exist: return false."""
    if itm == {"code": 0}:
        return False
    id_1: Hashable
    id_2: Hashable = ""
    dm_id_str: str
    cmd: str = itm.get("cmd", "")
    if not cmd:
        print("No CMD", str_itm)
        return True
    data: dict[str, Any] = itm.get("data")  # pyright: ignore[reportAssignmentType]
    msg_id = str(itm.get("msg_id", 0))
    match cmd:
        # sort by hot-spot
        case "DANMU_MSG" | "DANMU_MSG:4:0:2:2:2:0":
            dm_id_str = simdjson.loads(itm["info"][0][15]["extra"]).get("id_str", "")
            id_1 = f"""{cmd}${itm["info"][0][7]}${itm["info"][0][4]}${itm["info"][0][5]}${itm["info"][9]["ct"]}${itm["info"][9]["ts"]}${itm["info"][2][0]}${itm["info"][2][1]}${dm_id_str}${msg_id}"""
            # mid_hash,time.Now().Unix(),rnd,ct,ts,uid,uname,extra:dm_id_str,msg_id
            if not (itm["info"][2][1] == 0 and check_username(itm["info"][2][0])):
                id_2 = f"""{cmd}${itm["info"][0][7]}${itm["info"][0][4]}${itm["info"][0][5]}${itm["info"][9]["ct"]}${itm["info"][9]["ts"]}$0${(itm["info"][2][1][0] + "***") if itm["info"][2][1] else ""}${dm_id_str}${msg_id}"""
        case "INTERACT_WORD":
            id_1 = f"""{cmd}${data["roomid"]}${data["score"]}${data["timestamp"]}${data["trigger_time"]}${data.get("uid", 0)}${data["uname"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                with contextlib.suppress(IndexError):
                    id_2 = f"""{cmd}${data["roomid"]}${data["score"]}${data["timestamp"]}${data["trigger_time"]}$0${data["uname"][0]}***${msg_id}"""
        case "ENTRY_EFFECT" | "ENTRY_EFFECT_MUST_RECEIVE":
            id_1 = f"""{cmd}${data["trigger_time"]}${data.get("uid", 0)}${data["target_id"]}${msg_id}"""
        case "SEND_GIFT":
            id_1 = f"""{cmd}${data["rnd"]}${data.get("uid", 0)}${data["uname"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                id_2 = f"""{cmd}${data["rnd"]}$0${data["uname"][0]}***${msg_id}"""
        case "COMBO_SEND":
            id_1 = f"""{cmd}${data["batch_combo_id"]}${data["combo_id"]}${msg_id}"""
            # _t1, _t2 = gift_id_recover(data["batch_combo_id"], data["combo_id"])
            if not (data.get("uid", 0) == 0 and check_username(data["uname"])):
                bcid, cid = gift_id_enc(data["batch_combo_id"], data["combo_id"])
                id_2 = f"""{cmd}${bcid}${cid}${msg_id}"""
            else:
                id_2 = ""
        case "COMBO_END":
            id_1 = f"""{cmd}${data["start_time"]}${data["end_time"]}${data["ruid"]}${data.get("uid", 0)}${msg_id}"""
        case "SUPER_CHAT_MESSAGE":
            id_1 = f"""{cmd}${data["id"]}${data.get("uid", 0)}${data["user_info"]["uname"]}${data["message"]}${data.get("message_trans", "")}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["user_info"]["uname"])):
                pass
        case "SUPER_CHAT_MESSAGE_JPN":
            id_1 = f"""{cmd}${data["id"]}${data.get("uid", 0)}${data["user_info"]["uname"]}${data["message"]}${data["message_jpn"]}${msg_id}"""
            if not (data.get("uid", 0) == 0 and check_username(data["user_info"]["uname"])):
                pass
        case "ANCHOR_LOT_AWARD" | "ANCHOR_LOT_END" | "ANCHOR_LOT_START":
            id_1 = f"""{cmd}${data["id"]}${msg_id}"""
        case "RANK_REM":
            id_1 = f"""{cmd}${data["time"]}${data.get("uid", 0)}${data["ruid"]}${msg_id}"""
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
        case "GUARD_BUY":
            id_1 = f"""{cmd}${data["start_time"]}${data.get("uid", 0)}${itm["data"]["num"]}${msg_id}"""
        case "USER_TOAST_MSG":
            id_1 = f"""{cmd}${data["payflow_id"]}${data.get("uid", 0)}${msg_id}"""
        case "USER_TOAST_MSG_V2":
            id_1 = f"""{cmd}${data["pay_info"]["payflow_id"]}${data["sender_uinfo"].get("uid", 0)}${data["sender_uinfo"]["base"]["name"]}${data["receiver_uinfo"].get("uid", 0)}${data["receiver_uinfo"]["base"]["name"]}${msg_id}"""
        case "COMMON_ANIMATION":
            id_1 = f"""{cmd}${data["order_id"]}${data.get("uid", 0)}${msg_id}"""
        case "LIVE_INTERACTIVE_GAME" | "LIVE_OPEN_PLATFORM_GAME" | "RECOMMEND_CARD" | "SPREAD_SHOW_FEET_V2":
            id_1 = f"""{cmd}${data["timestamp"]}${msg_id}"""
        case "DANMU_AGGREGATION":
            id_1 = f"""{cmd}${data["timestamp"]}${data["activity_identity"]}${msg_id}"""
        case "WIDGET_BANNER" | "ROOM_BANNER":
            id_1 = f"""{cmd}${data["timestamp"]}${msg_id}"""
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
        case "COMMON_NOTICE_DANMAKU" | "GIFT_STAR_PROCESS" | "GOTO_BUY_FLOW" | "HOT_BUY_NUM" | "NOTICE_MSG" | "RADIO_BACKGROUND" | "SUPER_CHAT_MESSAGE_DELETE" | "WIDGET_GIFT_STAR_PROCESS":
            # id_1 = f"""{cmd}${str(data)}${msg_id}"""
            id_1 = str_itm
        case "WIDGET_WISH_INFO" | "WIDGET_WISH_INFO_V2":
            id_1 = f"""{cmd}${data["ts"]}${data["sid"]}${data["tid"]}${msg_id}"""
        case "RECALL_DANMU_MSG" | "RING_STATUS_CHANGE_V2" | "SYS_MSG" | "LIVE" | "PREPARING":
            id_1 = (str_itm, timestamp.to_integral("ROUND_DOWN"))
            id_2 = (str_itm, timestamp.to_integral("ROUND_DOWN") + 1)
        case "INTERACT_WORD_V2":
            id_1 = f"""{cmd}${data["pb"]}"""
        case (
            "AREA_RANK_CHANGED"
            | "GUARD_HONOR_THOUSAND"
            | "HOT_ROOM_NOTIFY"
            | "LIKE_INFO_V3_NOTICE"
            | "LIKE_INFO_V3_UPDATE"
            | "LOG_IN_NOTICE"
            | "master_qn_strategy_chg"
            | "ONLINE_RANK_COUNT"
            | "ONLINE_RANK_TOP3"
            | "ONLINE_RANK_V2"
            | "ONLINE_RANK_V3"
            | "OTHER_SLICE_LOADING_RESULT"
            | "PLAYURL_RELOAD"
            | "POPULAR_RANK_CHANGED"
            | "RANK_CHANGED_V2"
            | "RANK_CHANGED"
            | "REVENUE_RANK_CHANGED"
            | "ROOM_REAL_TIME_MESSAGE_UPDATE"
            | "STOP_LIVE_ROOM_LIST"
            | "SUPER_CHAT_ENTRANCE"
            | "HEARTBEAT_REPLY"  # special
            | "VOICE_JOIN_SWITCH_V2"
            | "VOICE_JOIN_SWITCH"
            | "WATCHED_CHANGE"
        ):
            return False
        case "ANCHOR_LOT_CHECKSTATUS":
            id_1 = (cmd, data["id"], data["status"])
        case "LIKE_INFO_V3_CLICK":
            id_1 = (cmd, data["uid"], timestamp.to_integral("ROUND_DOWN"))
        case (
            "ACTIVITY_BANNER_CHANGE_V2"
            | "ACTIVITY_BANNER_CHANGE"
            | "ADMIN_SHIELD_KEYWORD"
            | "ANCHOR_BROADCAST"
            | "ANCHOR_ECOMMERCE_STATUS"
            | "ANCHOR_HELPER_DANMU"
            | "ANCHOR_LOT_NOTICE"
            | "ANCHOR_NORMAL_NOTIFY"
            | "BENEFIT_CARD_CLEAN"
            | "BENEFIT_STATUS"
            | "CARD_MSG"
            | "CHANGE_ROOM_INFO"
            | "CUT_OFF"
            | "DANMU_ACTIVITY_CONFIG"
            | "FULL_SCREEN_SPECIAL_EFFECT"
            | "GIFT_BOARD_RED_DOT"
            | "GIFT_PANEL_PLAN"
            | "GUARD_ACHIEVEMENT_ROOM"
            | "GUARD_LEADER_NOTICE"
            | "LIVE_ANI_RES_UPDATE"
            | "LIVE_MULTI_VIEW_NEW_INFO"
            | "LIVE_PANEL_CHANGE_CONTENT"
            | "LIVE_PANEL_CHANGE"
            | "MESSAGEBOX_USER_GAIN_MEDAL"
            | "MESSAGEBOX_USER_MEDAL_CHANGE"
            | "OBS_SHIELD_STATUS_UPDATE"
            | "OFFICIAL_ROOM_EVENT"
            | "OTHER_SLICE_SETTING_CHANGED"
            | "PLAYTOGETHER_ICON_CHANGE"
            | "POPULAR_RANK_GUIDE_CARD"
            | "POPULARITY_RANK_TAB_CHG"
            | "PROGRAM_CHANGE"
            | "REENTER_LIVE_ROOM"
            | "RING_STATUS_CHANGE_V2"
            | "RING_STATUS_CHANGE"
            | "room_admin_entrance"
            | "ROOM_ADMIN_REVOKE"
            | "ROOM_ADMINS"
            | "ROOM_BLOCK_MSG"
            | "ROOM_CHANGE"
            | "ROOM_LOCK"
            | "ROOM_SILENT_OFF"
            | "ROOM_SILENT_ON"
            | "SHOPPING_CART_SHOW"
            | "SPECIAL_GIFT"
            | "STUDIO_ROOM_CLOSE"
            | "USER_INFO_UPDATE"
            | "USER_PANEL_RED_ALARM"
            | "VOICE_CHAT_UPDATE"
            | "VOICE_JOIN_LIST"
            | "VOICE_JOIN_ROOM_COUNT_INFO"
            | "WARNING"
        ):
            return True
        case _:
            tqdm.write(cmd)
            id_1 = ""
            return True
    if (id_1 and (id_1 in _deduplicate_dict)) or (id_2 and (id_2 in _deduplicate_dict)):
        return False
    if id_1:
        _deduplicate_dict.add(id_1)
    if id_2:
        _deduplicate_dict.add(id_2)
    # _deduplicate_dict.add(str_itm)
    return True


def _deduplicate(in_path: Path) -> int:
    with in_path.open(encoding="utf-8") as input_file:
        a = input_file.readlines()
        total_ = len(a)
    with in_path.with_suffix(".DEDUP.jsonl").open("w", 50 * 2**20, "utf-8") as output_file:
        for line in tqdm(a, leave=False, desc=in_path.name, position=1):
            if line in _deduplicate_dict:
                continue
            pos = line.find("{")
            str_itm = line[pos:]
            timestamp = line[:pos]
            timestamp_f: Decimal
            match len(timestamp):
                case 13:
                    timestamp_f = Decimal(timestamp) / 1_000
                case 16:
                    timestamp_f = Decimal(timestamp) / 1_000_000
                case 19:
                    timestamp_f = Decimal(timestamp) / 1_000_000_000
                case _:
                    timestamp_f = Decimal(timestamp)
            itm: dict = simdjson.loads(str_itm)
            if _deduplicate_it(itm, timestamp_f, str_itm):
                output_file.write(line)
            _deduplicate_dict.add(line)
    return total_


if __name__ == "__main__":
    st0 = time.time_ns()
    files_to_process = sys.argv[1:]
    try:
        for file in tqdm(files_to_process, leave=False, position=0):
            st1 = time.time()
            _deduplicate_dict.clear()
            gc.collect(2)
            gc.collect(1)
            gc.collect(0)
            total = _deduplicate(Path(file))
            total_time = time.time() - st1
            tqdm.write(f"{file}:{total_time:.3f}s, {(total / total_time):.0f} lines/s")
            # print(f"{file}:{total_time:.3f}s, {(total/total_time):.0f} lines/s")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        _log.exception(e)
    finally:
        et0 = time.time_ns()
        print("Done", (et0 - st0) / 1e9)
        time.sleep(30)
