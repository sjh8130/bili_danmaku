import json
import time
import sys
import os
from tqdm import tqdm
from typing import Any

raise Exception("未完成")

result: dict[str, Any] = {}


def analyze_structure(data: Any, parent_key: str = "", depth=1, cmd_type=""):
    """
    递归分析嵌套结构，并更新 result 中每个 key 的类型和 value 出现次数。
    如果遇到嵌套结构，则将嵌套的 key 合并为 'parent.child' 形式。
    """
    if depth == 1 and not cmd_type:
        cmd_type = data["cmd"]

    current_type = type(data).__name__

    match current_type:
        case "dict":
            ...
        case "list":
            ...
        case "int" | "float" | "str" | "None" | "NoneType" | "bool" | "bytes":
            ...

    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            update_result(cmd_type, full_key, value)
            if isinstance(value, (dict, list)):
                analyze_structure(value, full_key, depth + 1, cmd_type)

    elif isinstance(data, list):
        for index, item in enumerate(data):
            item_key = f"{parent_key}[{index}]"
            update_result(cmd_type, item_key, item)
            if isinstance(item, (dict, list)):
                analyze_structure(item, item_key, depth + 1, cmd_type)

    # 处理基本数据类型
    else:
        update_value_count(cmd_type, parent_key, data)


def update_result(cmd_type, key, value):
    """更新结果字典中的结构。"""
    type_name = type(value).__name__
    if type_name in ["list", "dict"] and key not in result:
        result[cmd_type][key] = {
            "type": type_name,
        }
    elif key not in result[cmd_type]:
        if type_name == "dict":
            result[cmd_type][key] = {
                "type": type_name,
            }
        else:
            result[cmd_type][key] = {"type": type_name, "value": dict()}
    update_value_count(cmd_type, key, value)


def update_value_count(cmd_type, key, value):
    """更新值的出现次数。"""
    # 将值转换为字符串，方便比较和统计
    if isinstance(value, dict):
        return
    if isinstance(value, list):
        return
    value_str = str(value)
    try:
        result[cmd_type][key]["value"][value_str] += 1
    except KeyError:
        result[cmd_type][key]["value"][value_str] = 1


def main(in_paths: list[str], output_dir: str):
    global result
    # 用于存储按 cmd 分类的结果
    # {cmd: {key: {type, value_count}}}

    if not in_paths:
        return
    pbar = tqdm(total=len(in_paths), ascii=True, unit="itm", position=1)
    for in_path in in_paths:
        is_err = False
        lineno = 1

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # 创建输出目录

        if in_path == output_dir:
            continue  # 避免读取输出目录内的文件

        with open(in_path, "r", encoding="utf-8") as file_in:
            for line in tqdm(file_in.readlines(), ascii=True, unit="line", position=2, desc=in_path):
                lineno += 1
                left_pos = line.find("{")  # 找到 JSON 部分的起点

                try:
                    cmd_data: dict = json.loads(line[left_pos:])  # 解析 JSON 行
                except json.JSONDecodeError as e:
                    print(f"解析错误：文件 {in_path}，行号 {lineno}")
                    if not is_err:
                        is_err = True
                    continue  # 跳过解析失败的行

                # 获取 cmd 的分类值
                # 如果没有 cmd 字段，则标记为 UNKNOWN
                cmd_type = cmd_data.get("cmd", "UNKNOWN")

                # 初始化该 cmd 分类的结果
                if cmd_type not in result:
                    result[cmd_type] = {"cmd": {"type": "dict", "value": {}}}

                # 递归分析结构，并更新统计信息
                analyze_structure(cmd_data, depth=1, cmd_type=cmd_type)
        pbar.update()
    pbar.close()

    # try:
    #     del result["AREA_RANK_CHANGED"]["data.msg_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["AREA_RANK_CHANGED"]["data.timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["AREA_RANK_CHANGED"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.batch_combo_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.combo_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.medal_info.medal_name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.medal_info.target_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.r_uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receive_user_info.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receive_user_info.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.risk_ctrl_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.base.risk_ctrl_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.receiver_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.risk_ctrl_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.base.risk_ctrl_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.sender_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMBO_SEND"]["data.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMMON_NOTICE_DANMAKU"]["data.content_segments[0].text"]["value"]
    # except:
    #     pass
    # try:
    #     del result["COMMON_NOTICE_DANMAKU"]["data.content_segments[1].text"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_AGGREGATION"]["data.activity_identity"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_AGGREGATION"]["data.aggregation_num"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_AGGREGATION"]["data.timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["dm_v2"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[9].ts"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[9].ct"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].extra"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][16].activity_identity"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][13].emoticon_unique"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][13].url"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base.origin_info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.medal"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.medal.id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["info[0][15].user.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["DANMU_MSG"]["msg_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.copy_writing_v2"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.copy_writing"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.target_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.trigger_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.risk_ctrl_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.base.risk_ctrl_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.guard.expired_str"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.medal"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.medal.id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.guard"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.uinfo.wealth"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ENTRY_EFFECT"]["data.wealthy_info.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.contribution"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.contribution_v2"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.fans_medal"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.roomid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.fans_medal.anchor_roomid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.trigger_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base.origin_info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.guard"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.guard.expired_str"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.medal"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.wealth"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.fans_medal.medal_name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.fans_medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.fans_medal.target_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.medal.id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["INTERACT_WORD"]["data.uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["LIVE"]["live_key"]["value"]
    # except:
    #     pass
    # try:
    #     del result["LIVE"]["live_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["LIVE"]["roomid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["LIVE"]["sub_session_key"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ONLINE_RANK_TOP3"]["data.list[0].msg"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ONLINE_RANK_TOP3"]["data.list[0].uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.current_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.lot_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.guard.expired_str"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.sender_info.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.start_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_NEW"]["data.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.current_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.end_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.h5_url"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.lot_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.remove_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.replace_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.sender_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_START"]["data.start_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_WINNER_LIST"]["data.lot_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["POPULARITY_RED_POCKET_WINNER_LIST"]["data.timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["PREPARING"]["roomid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_BLOCK_MSG"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_BLOCK_MSG"]["data.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_BLOCK_MSG"]["uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_BLOCK_MSG"]["uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_CHANGE"]["data.title"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_REAL_TIME_MESSAGE_UPDATE"]["data.fans_club"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_REAL_TIME_MESSAGE_UPDATE"]["data.fans"]["value"]
    # except:
    #     pass
    # try:
    #     del result["ROOM_REAL_TIME_MESSAGE_UPDATE"]["data.roomid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.batch_combo_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.batch_combo_send"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.batch_combo_send.batch_combo_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.batch_combo_send.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.batch_combo_send.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.blind_gift"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.combo_send"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.combo_send.combo_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.combo_send.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.combo_send.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.medal_info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.medal_info.medal_name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.medal_info.target_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.rcost"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receive_user_info.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receive_user_info.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.risk_ctrl_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.base.risk_ctrl_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.receiver_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.rnd"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.origin_info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.origin_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.origin_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.risk_ctrl_info"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.risk_ctrl_info.face"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.base.risk_ctrl_info.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.medal"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.medal.name"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.medal.ruid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.medal.score"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.sender_uinfo.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.tid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.uid"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["data.uname"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["msg_id"]["value"]
    # except:
    #     pass
    # try:
    #     del result["SEND_GIFT"]["send_time"]["value"]
    # except:
    #     pass
    # try:
    #     del result["WIDGET_GIFT_STAR_PROCESS"]["data.ddl_timestamp"]["value"]
    # except:
    #     pass
    # try:
    #     del result["WIDGET_GIFT_STAR_PROCESS"]["data.start_date"]["value"]
    # except:
    #     pass
    # try:
    #     del result["WIDGET_GIFT_STAR_PROCESS"]["data.version"]["value"]
    # except:
    #     pass

    # 将每个 cmd 分类的数据写入单独的 JSON 文件
    for cmd, result in result.items():
        try:
            del result[cmd]["msg_id"]
        except:
            pass
        try:
            del result[cmd]["send_time"]
        except:
            pass
        cmd_file_path = os.path.join(output_dir, f"{cmd}.json")  # 生成文件路径
        with open(cmd_file_path, "w", encoding="utf-8") as file_io:
            json.dump(result, file_io, ensure_ascii=False, indent="\t")

    print(f"处理完成，所有结果已保存到目录：{output_dir}")


if __name__ == "__main__":

    in_path = sys.argv[1:]  # 从命令行获取输入文件路径
    output_dir = "Z:\\"  # 输出目录路径

    start_time = time.time()
    main(in_path, output_dir)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    print()
    time.sleep(5)
