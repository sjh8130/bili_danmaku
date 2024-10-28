import sys

_SKIP_KEYWORDS = ["DM_INTERACTION", "LIKE_INFO_V3_CLICK", "LIKE_INFO_V3_UPDATE", "ONLINE_RANK_COUNT", "ONLINE_RANK_V2", "STOP_LIVE_ROOM_LIST", "WATCHED_CHANGE", "WIDGET_BANNER"]


def _trim_file(input_file_path: str):
    print(input_file_path)
    # 读取文件内容
    with open(input_file_path, "r", encoding="utf-8") as input_file, open(input_file_path + "1", "a", 1048576, "utf-8") as output_file:
        for line in input_file.readlines():
            if any(keyword in line for keyword in _SKIP_KEYWORDS):
                continue

            ls = line.find("{")
            if ls == 0:
                output_file.write(line)
            else:
                date_raw = line[:ls]
                if "." in date_raw:
                    date = str(float(date_raw) * 1000)[:13]
                else:
                    date = date_raw[0:13]
                # output_file.write(date+"\n")
                output_file.write(date + line[ls:])


files_to_process = sys.argv[1:]
for file in files_to_process:
    _trim_file(file)
