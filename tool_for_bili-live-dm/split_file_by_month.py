import os
import re
import sys

from functools import lru_cache
from datetime import datetime, timedelta, timezone

import tqdm

_tz = timezone(timedelta(hours=8))


@lru_cache(1000)
def _get_date_from_timestamp(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=_tz)


def _split_file_by_day(input_file_path: str):
    # print(input_file_path)

    # 初始化一个字典，按日期存储文件内容
    lines_by_day: dict[datetime, list[str]] = {}

    # 获取文件名（不包括扩展名）和扩展名
    base_name, ext = os.path.splitext(os.path.basename(b_name))
    directory = os.path.dirname(input_file_path)

    # 读取文件内容
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        # 遍历文件的每一行
        for line in tqdm.tqdm(input_file.readlines(), desc=os.path.basename(input_file_path)):
            # 提取时间戳
            timestamp_match = re.search(r"^(\d+)", line)
            if timestamp_match:
                timestamp = timestamp_match.group(1)[0:13]
                date: datetime = _get_date_from_timestamp((int(timestamp) // 1_000).__floor__())

                # 将行添加到对应日期的列表中
                if date not in lines_by_day:
                    lines_by_day[date] = []
                lines_by_day[date].append(line)

    # 为每一天创建新文件，并写入内容
    for date, lines_1 in tqdm.tqdm(lines_by_day.items(), desc=f"write:{os.path.basename(input_file_path)}"):
        output_file_name = f"{base_name}-{date.strftime('%Y-%m')}{ext}"
        output_file_path = os.path.join(directory, output_file_name)
        with open(output_file_path, "a", 1048576, "utf-8") as output_file:
            output_file.writelines(lines_1)


# 调用函数，按日分割文件
item = sys.argv[1:]
b_name = item[0]
for i in item:
    _split_file_by_day(i)
# split_file_by_day("Z://11.jsonl")
# AI
