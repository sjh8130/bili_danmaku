import sys


def trim_file(input_file_path: str):
    print(input_file_path)
    # 读取文件内容
    with open(input_file_path, "r", encoding="utf-8") as input_file, open(
        input_file_path + "1", "a", 1048576, "utf-8"
    ) as output_file:
        for line in input_file.readlines():
            if "DM_INTERACTION" in line:
                continue
            if "LIKE_INFO_V3_CLICK" in line:
                continue
            if "LIKE_INFO_V3_UPDATE" in line:
                continue
            if "ONLINE_RANK_COUNT" in line:
                continue
            if "ONLINE_RANK_V2" in line:
                continue
            if "STOP_LIVE_ROOM_LIST" in line:
                continue
            if "WATCHED_CHANGE" in line:
                continue
            if "WIDGET_BANNER" in line:
                continue

            ls = line.find("{")
            if ls == 0:
                output_file.write(line)
            else:
                date_raw = line[0:ls]
                if "." in date_raw:
                    date = str(float(date_raw) * 1000)[0:13]
                else:
                    date = date_raw[0:13]
                # output_file.write(date+"\n")
                output_file.write(date + line[ls:])


item = sys.argv[1:]
for i in item:
    trim_file(i)
