from functools import lru_cache
import os
import re
from datetime import datetime, timedelta, timezone
import sys

# 定义一个函数，用于解析UNIX时间戳，并返回日期

tz = timezone(timedelta(hours=8))


@lru_cache
def get_date_from_timestamp(timestamp: int):
    return datetime.fromtimestamp(timestamp, tz=tz)


# 定义一个函数，用于按日分割文件


def split_file_by_day(input_file_path: str):
    print(input_file_path)

    # 初始化一个字典，按日期存储文件内容
    lines_by_day = {}

    # 获取文件名（不包括扩展名）和扩展名
    base_name, ext = os.path.splitext(os.path.basename(b_name))
    directory = os.path.dirname(input_file_path)

    # 读取文件内容
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # 遍历文件的每一行
    for line in lines:
        # 提取时间戳
        timestamp_match = re.search(r"^(\d+)", line)
        if timestamp_match:
            timestamp = timestamp_match.group(1)[0:13]
            date = get_date_from_timestamp((int(timestamp) // 1_000).__trunc__())

            # 将行添加到对应日期的列表中
            if date not in lines_by_day:
                lines_by_day[date] = []
            lines_by_day[date].append(line)

    # 为每一天创建新文件，并写入内容
    for date, lines in lines_by_day.items():
        output_file_name = f"{base_name}-{date.strftime('%Y-%m-%d')}{ext}"
        output_file_path = os.path.join(directory, output_file_name)
        with open(output_file_path, "a", 1048576, "utf-8") as output_file:
            output_file.writelines(lines)


# 调用函数，按日分割文件
item = sys.argv[1:]
b_name = item[0]
for i in item:
    split_file_by_day(i)
# split_file_by_day("Z://11.jsonl")
# AI
