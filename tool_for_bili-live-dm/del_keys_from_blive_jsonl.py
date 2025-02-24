import json
import os
import sys
from enum import StrEnum, auto

import json5
from loguru import logger
from tqdm import tqdm

_log = logger.bind(user="dek_key jsonl")
raise Exception("*todo")
_FALSE_CMP = [0, "", [], False, {}, None]
_SW1: bool = False
IGNORE_LIST = set()
_SW2: bool = False
DONT_CARE_INDEX_LIST = set()
_SW3: bool = False
STR_LIST = set()
try:
    with open("livedm_keys_not_interest.json") as fp:
        _D1: dict[str, list[str]] = json5.load(fp)
except FileNotFoundError:
    pass
else:
    try:
        STR_LIST = set(_D1["STR_LIST"])
        _SW3 = True
    except KeyError:
        pass
    try:
        DONT_CARE_INDEX_LIST: set[str] = set(_D1["DONT_CARE_INDEX_LIST"])
        _SW1 = True
    except KeyError:
        pass
    try:
        IGNORE_LIST: set[str] = set(_D1["IGNORE_LIST"])
        _SW2 = True
    except KeyError:
        pass


class OPR(StrEnum):
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


def _del_keys(
    item_0: dict, key_0: str, value_0, opr: OPR, r=True, cmd="", target_key=""
):
    cmd = item_0["cmd"] if cmd == "" else cmd
    final_key: str = f"{cmd}{target_key}"
    # print("_del_keys", final_key)
    if key_0 in item_0 and isinstance(item_0, dict):
        match opr:
            case OPR.EQ:
                if item_0.get(key_0) == value_0:
                    item_0.pop(key_0)
            case OPR.IN:
                if item_0.get(key_0) in value_0:
                    item_0.pop(key_0)
            case OPR.ANY:
                item_0.pop(key_0)
            case OPR.GT:
                if item_0.get(key_0) > value_0:  # type: ignore[reportOptionalOperand]
                    item_0.pop(key_0)
            case OPR.LT:
                if item_0.get(key_0) < value_0:  # type: ignore[reportOptionalOperand]
                    item_0.pop(key_0)
            case OPR.GEQ:
                if item_0.get(key_0) >= value_0:  # type: ignore[reportOptionalOperand]
                    item_0.pop(key_0)
            case OPR.LEQ:
                if item_0.get(key_0) <= value_0:  # type: ignore[reportOptionalOperand]
                    item_0.pop(key_0)
            case OPR.NEQ:
                if item_0.get(key_0) != value_0:
                    item_0.pop(key_0)
            case OPR.NIN:
                if item_0.get(key_0) not in value_0:
                    item_0.pop(key_0)
            case OPR.IS:
                if item_0.get(key_0) is value_0:
                    item_0.pop(key_0)
            case OPR.NIS:
                if item_0.get(key_0) is not value_0:
                    item_0.pop(key_0)
            case _:
                raise "*ToDo"
    if not r:
        return
    for key_1 in item_0:
        if isinstance(item_0[key_1], dict):
            _tk: str = f"{target_key}.{key_1}"
            _del_keys(item_0[key_1], key_0, value_0, opr, r, cmd, _tk)
        elif isinstance(item_0[key_1], list):
            for index_1, item_l1 in enumerate(item_0[key_1]):
                _tk = (
                    f"{target_key}[IDX]"
                    if _SW2 and final_key in DONT_CARE_INDEX_LIST
                    else f"{target_key}[{index_1}]"
                )
                if f"{cmd}.{key_1}{_tk}" in STR_LIST:
                    item_0[key_1][index_1] = _del_keys(
                        json.dumps(
                            json.loads(item_l1),
                            ensure_ascii=False,
                            separators=(",", ":"),
                        ),
                        key_0,
                        r,
                        cmd,
                        _tk,
                    )  # type:ignore[reportArgumentType]


def _deduplicate(in_path: str):
    with (
        open(in_path, "r", 1048576, encoding="utf-8") as input_file,
        open(in_path + "x_cleaned", "a", 10485760, "utf-8") as output_file,
    ):
        for line in tqdm(
            input_file.readlines(), leave=False, desc=f"{os.path.basename(in_path)}"
        ):
            ls = line.find("{")
            date_raw = line[:ls]
            if "." in date_raw:
                date = (date_raw.replace(".", "") + "0000000000000")[:13] if ls else ""
            else:
                date = date_raw[:13] if ls else ""
            itm: dict = json.loads(line[ls:])
            _del_keys(
                itm,
                "contribution_v2",
                {"grade": 0, "rank_type": "", "text": ""},
                OPR.EQ,
            )
            _del_keys(itm, "contribution", {"grade": 0}, OPR.EQ)
            _del_keys(itm, "danmaku_style", {"background_color": None}, OPR.EQ)
            _del_keys(itm, "danmu", {"area": 0}, OPR.EQ)
            _del_keys(itm, "face_effect_v2", {"id": 0, "type": 0}, OPR.EQ)
            _del_keys(
                itm, "group_medal", {"is_lighted": 0, "medal_id": 0, "name": ""}, OPR.EQ
            )
            _del_keys(itm, "guard_leader", {"is_guard_leader": False}, OPR.EQ)
            _del_keys(itm, "guard", {"level": 0, "expired_str": ""}, OPR.EQ)
            _del_keys(itm, "identities", [1], OPR.EQ)
            _del_keys(
                itm,
                "official_info",
                {"role": 0, "title": "", "desc": "", "type": -1},
                OPR.EQ,
            )
            _del_keys(
                itm,
                "relation_tail",
                {"tail_guide_text": "", "tail_icon": "", "tail_type": 0},
                OPR.EQ,
            )
            _del_keys(
                itm, "title", {"old_title_css_id": "", "title_css_id": ""}, OPR.EQ
            )
            _del_keys(itm, "wealth", {"dm_icon_key": "", "level": 0}, OPR.EQ)
            _del_keys(itm, "show_reply", True, OPR.EQ)
            _del_keys(itm, "anchor_roomid", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "anchor_uname", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "animation", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "anniversary_crowd", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "background_color_dark", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "background_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "bag_gift", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "basemap_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "batch_combo_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "batch_combo_send", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "beatId", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "blind_gift", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "broadcast_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "bulge_display", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "combo_send", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "combo_total_coin", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "core_user_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "crit_prob", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "danmaku_uri", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "direction", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "discount_price", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "dm_icon_key", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "dm_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "dm_v2", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "draw", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "effect_block", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "effect", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "emoticon_unique", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "emots", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "esports_jump_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "face_effect_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "face_effect_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "face", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "fans_medal", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "float_sc_resource_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "gift_tag", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "giftType", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "gold", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "group_guard_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "group_medal", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "group_name", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "group_op_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "group_role_name", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "guard_icon", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "guard_leader", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "guard_level", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "guard", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "head_icon", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "hit_combo", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "honor_icon", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "icon_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "icon_list", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "icon", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_audited", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_first", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_join_receiver", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_light", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_lighted", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_mystery", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_naming", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_report", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_special_batch", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "is_spread", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "jump_to_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "link_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "main_state_dm_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "master_player_hidden", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_color_border", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_color_end", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_color_start", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_level", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal_name", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "medal", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "mobile_dynamic_url_webp", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "mock_effect", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "msg_common", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "name_color_str", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "name_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "objective_state_dm_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "official_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "origin_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "original_gift_name", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "pk_direction", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "player_mode", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "price", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "privilege_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "quartet_direction", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "remain", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "reply_is_mystery", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "reply_mid", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "reply_type_enum", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "reply_uname_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "reply_uname", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "risk_ctrl_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "score", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "send_from_me", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "send_master", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "show_player_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "show_price", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "silver", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "space_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "space_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "special", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "spread_desc", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "spread_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "super_batch_gift_num", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "super_gift_num", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "super", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "svga_block", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "switch", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "tag_image", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "tail_icon", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "tail_text", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "target_id", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "title", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "top_list", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "total_coin", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "typ", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "uhead_frame", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "uname_color", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "user_receive_count", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "wealth_style_info", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "wealth", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "web_dynamic_url_apng", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "web_dynamic_url_webp", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "yeah_space_type", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "yeah_space_url", _FALSE_CMP, OPR.IN)
            _del_keys(itm, "dmscore", 0, opr=OPR.ANY)
            _del_keys(itm, "recommend_score", 0, opr=OPR.ANY)
            _del_keys(itm, "user_hash", 0, opr=OPR.ANY)
            output_file.write(
                date + json.dumps(itm, ensure_ascii=False, separators=(",", ":")) + "\n"
            )


if __name__ == "__main__":
    files_to_process = sys.argv[1:]
    try:
        for file in files_to_process:
            _deduplicate(file)
    except KeyboardInterrupt:
        print()
    except Exception as e:
        _log.exception(e)
        # time.sleep(10)
