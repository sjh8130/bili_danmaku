import json
import os
import sys
from enum import StrEnum, auto
from typing import Any

from loguru import logger
from tqdm import tqdm

try:
    import simdjson
except ImportError:
    simdjson = json

_log = logger.bind(user="dek_key jsonl")
# raise Exception("*todo")
_FALSE_CMP = [0, "", [], False, {}, None]


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


def _del_keys(d: dict, k: str, v:Any, o: OPR):
    if k in d:
        match o:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN:
                if d.get(k) in v:
                    d.pop(k)
            case OPR.ANY:
                d.pop(k)
            case OPR.GT:
                if d.get(k) > v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.LT:
                if d.get(k) < v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.GEQ:
                if d.get(k) >= v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.LEQ:
                if d.get(k) <= v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.NEQ:
                if d.get(k) != v:
                    d.pop(k)
            case OPR.NIN:
                if d.get(k) not in v:
                    d.pop(k)
            case OPR.IS:
                if d.get(k) is v:
                    d.pop(k)
            case OPR.NIS:
                if d.get(k) is not v:
                    d.pop(k)
            case _:
                raise Exception("*ToDo")


def _del_keys_prep(d: dict, k: str, v:Any, o: OPR, cmd="", dep: int = 0):
    cmd = d["cmd"] if cmd == "" else cmd
    # print("_del_keys_prep", cmd)
    for key_1 in d:
        if isinstance(d[key_1], dict):
            ...
        elif isinstance(d[key_1], list):
            for index_1, item_1 in enumerate(d[key_1]):
                ...
                if ... in ...:
                    pass


# no order
E_1 = {"grade": 0, "rank_type": "", "text": ""}
"INTERACT_WORD.contribution_v2"
E_2 = {"grade": 0}
"INTERACT_WORD.contribution"
E_3 = {"background_color": None}
"COMMON_NOTICE_DANMAKU"
E_4 = {"area": 0}
"SEND_GIFT.danmu"
E_5 = {"id": 0, "type": 0}
"SEND_GIFT.face_effect_v2"
E_6 = {"is_lighted": 0, "medal_id": 0, "name": ""}
"group_medal"
E_7 = {"is_guard_leader": False}
"**uinfo**.guard_leader"
E_8 = {"level": 0, "expired_str": ""}
"**uinfo**.guard"
E_9 = [
    {"role": 0, "title": "", "desc": "", "type": -1},
    {"role": 0, "desc": "", "type": -1},
]
"**uinfo**.official_info"
E_10 = [
    {"tail_guide_text": "", "tail_icon": "", "tail_type": 0},
    {"tail_guide_text": "", "tail_type": 0},
]
"INTERACT_WORD.relation_tail"
E_11 = {"old_title_css_id": "", "title_css_id": ""}
"**uinfo**.title"
E_12 = {"dm_icon_key": "", "level": 0}
"**uinfo**.wealth"
E_13 = []

E_14 = []

E_15 = []

E_16 = []

E_17 = []

E_18 = []

E_19 = []

E_20 = []
KEYS_DEL_IF_FALSE = [
    "activity_identity",
    "activity_source",
    "anchor_roomid",
    "anchor_uname",
    "anniversary_crowd",
    "background_color",
    "background_color_dark",
    "bag_gift",
    "basemap_url",
    "batch_combo_id",
    "batch_combo_send",
    "beatId",
    "blind_gift",
    "broadcast_id",
    "bulge_display",
    "combo_send",
    "combo_total_coin",
    "core_user_type",
    "crit_prob",
    "cur_score",
    "danmaku_uri",
    "direction",
    "discount_price",
    "dm_icon_key",
    "dm_type",
    "dm_v2",
    "draw",
    "effect",
    "effect_block",
    "emoticon_unique",
    "emots",
    "esports_jump_url",
    "face",
    "face_effect_id",
    "face_effect_type",
    "fans_medal",
    "float_sc_resource_id",
    "gift_tag",
    "giftType",
    "gold",
    "group_guard_info",
    "group_medal",
    "group_name",
    "group_op_type",
    "group_role_name",
    "guard",
    "guard_icon",
    "guard_leader",
    "guard_level",
    "head_icon",
    "hit_combo",
    "honor_icon",
    "icon",
    "icon_id",
    "icon_list",
    "id",
    "in_player_area",
    "is_audited",
    "is_dynamic",
    "is_first",
    "is_join_receiver",
    "is_light",
    "is_lighted",
    "is_mystery",
    "is_naming",
    "is_report",
    "is_special_batch",
    "is_spread",
    "jump_to_url",
    "level_total_score",
    "link_url",
    "main_state_dm_color",
    "master_player_hidden",
    "medal",
    "medal_color",
    "medal_color_border",
    "medal_color_end",
    "medal_color_start",
    "medal_info",
    "medal_level",
    "medal_name",
    "mobile_dynamic_url_webp",
    "mock_effect",
    "mode",
    "msg_common",
    "name_color",
    "name_color_str",
    "objective_state_dm_color",
    "official_info",
    "origin_info",
    "original_gift_name",
    "pk_direction",
    "player_mode",
    "price",
    "privilege_type",
    "quartet_direction",
    "remain",
    "reply_is_mystery",
    "reply_mid",
    "reply_type_enum",
    "reply_uname",
    "reply_uname_color",
    "risk_ctrl_info",
    "score",
    "send_from_me",
    "send_master",
    "show_player_type",
    "show_price",
    "silver",
    "space_type",
    "space_url",
    "special",
    "spread_desc",
    "spread_info",
    "status",
    "super",
    "super_batch_gift_num",
    "super_gift_num",
    "svga_block",
    "switch",
    "tag_image",
    "tail_icon",
    "tail_text",
    "target_id",
    "title",
    "top_list",
    "total_coin",
    "typ",
    "uhead_frame",
    "uid",
    "uname_color",
    "upgrade_need_score",
    "user_receive_count",
    "voice_background",
    "wealth",
    "wealth_style_info",
    "web_dynamic_url_apng",
    "web_dynamic_url_webp",
    "yeah_space_type",
    "yeah_space_url",
]


def _clean_dm(a: str):
    with (
        open(a, "r", 1048576, encoding="utf-8") as g,
        open(a + "x_cleaned", "a", 10485760, "utf-8") as h,
    ):
        for line_num, f in tqdm(
            enumerate(g.readlines()), leave=False, desc=f"{os.path.basename(a)}"
        ):
            e = f.find("{")
            b = f[:e]
            c = ((b.replace(".", "") + "0000000000000")[:13]).lstrip("0")
            d: dict = simdjson.loads(f[e:])  # type:ignore
            # complex region
            _del_keys_prep(d, "contribution_v2", E_1, OPR.EQ)
            _del_keys_prep(d, "contribution", E_2, OPR.EQ)
            _del_keys_prep(d, "danmaku_style", E_3, OPR.EQ)
            _del_keys_prep(d, "danmu", E_4, OPR.EQ)
            _del_keys_prep(d, "face_effect_v2", E_5, OPR.EQ)
            _del_keys_prep(d, "group_medal", E_6, OPR.EQ)
            _del_keys_prep(d, "guard_leader", E_7, OPR.EQ)
            _del_keys_prep(d, "guard", E_8, OPR.EQ)
            _del_keys_prep(d, "identities", [1], OPR.EQ)
            _del_keys_prep(d, "official_info", E_9, OPR.IN)
            _del_keys_prep(d, "relation_tail", E_10, OPR.EQ)
            _del_keys_prep(d, "title", E_11, OPR.EQ)
            _del_keys_prep(d, "wealth", E_12, OPR.EQ)
            # static
            _del_keys_prep(d, "show_reply", True, OPR.EQ)
            # false compare region
            _del_keys_prep(d, "anchor_roomid", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "anchor_uname", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "animation", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "anniversary_crowd", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "background_color_dark", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "background_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "bag_gift", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "basemap_url", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "batch_combo_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "batch_combo_send", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "beatId", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "blind_gift", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "broadcast_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "bulge_display", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "combo_send", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "combo_total_coin", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "core_user_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "crit_prob", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "danmaku_uri", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "direction", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "discount_price", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "dm_icon_key", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "dm_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "dm_v2", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "draw", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "effect_block", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "effect", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "emoticon_unique", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "emots", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "esports_jump_url", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "face_effect_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "face_effect_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "face", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "fans_medal", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "float_sc_resource_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "gift_tag", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "giftType", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "gold", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "group_guard_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "group_medal", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "group_name", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "group_op_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "group_role_name", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "guard_icon", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "guard_leader", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "guard_level", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "guard", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "head_icon", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "hit_combo", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "honor_icon", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "icon_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "icon_list", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "icon", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_audited", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_first", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_join_receiver", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_light", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_lighted", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_mystery", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_naming", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_report", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_special_batch", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "is_spread", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "jump_to_url", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "link_url", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "main_state_dm_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "master_player_hidden", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_color_border", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_color_end", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_color_start", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_level", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal_name", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "medal", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "mobile_dynamic_url_webp", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "mock_effect", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "msg_common", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "name_color_str", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "name_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "objective_state_dm_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "official_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "origin_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "original_gift_name", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "pk_direction", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "player_mode", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "price", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "privilege_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "quartet_direction", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "remain", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "reply_is_mystery", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "reply_mid", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "reply_type_enum", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "reply_uname_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "reply_uname", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "risk_ctrl_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "score", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "send_from_me", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "send_master", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "show_player_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "show_price", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "silver", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "space_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "space_url", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "special", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "spread_desc", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "spread_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "super_batch_gift_num", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "super_gift_num", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "super", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "svga_block", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "switch", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "tag_image", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "tail_icon", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "tail_text", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "target_id", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "title", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "top_list", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "total_coin", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "typ", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "uhead_frame", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "uname_color", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "user_receive_count", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "wealth_style_info", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "wealth", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "web_dynamic_url_apng", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "web_dynamic_url_webp", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "yeah_space_type", _FALSE_CMP, OPR.IN)
            _del_keys_prep(d, "yeah_space_url", _FALSE_CMP, OPR.IN)
            # anyway region
            _del_keys_prep(d, "dmscore", 0, o=OPR.ANY)
            _del_keys_prep(d, "recommend_score", 0, o=OPR.ANY)
            _del_keys_prep(d, "user_hash", 0, o=OPR.ANY)
            h.write(c + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    files_to_process = sys.argv[1:]
    try:
        for file in files_to_process:
            _clean_dm(file)
    except KeyboardInterrupt:
        print()
    except Exception as e:
        _log.exception(e)
        # time.sleep(10)
