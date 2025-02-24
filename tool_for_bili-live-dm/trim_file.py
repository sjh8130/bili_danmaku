import json
import sys

# _SKIP_KEYWORDS = ["STOP_LIVE_ROOM_LIST", "LIKE_INFO_V3_CLICK", "LIKE_INFO_V3_UPDATE", "ONLINE_RANK_COUNT", "ONLINE_RANK_V2", "OTHER_SLICE_LOADING_RESULT", "HOT_ROOM_NOTIFY", "DM_INTERACTION", "WATCHED_CHANGE", "WIDGET_BANNER", "NOTICE_MSG", "GUARD_HONOR_THOUSAND"]
_SKIP_KEYWORDS = []


def _trim_file(in_path: str):
    with open(in_path, "r", 1048576, encoding="utf-8") as input_file, open(
        in_path + "_trim", "a", 1048576, "utf-8"
    ) as out_file:
        for line in input_file.readlines():
            # if any(keyword in line for keyword in _SKIP_KEYWORDS):
            #     continue
            ls = line.find("{")
            date_raw = line[:ls]
            if "." in date_raw:
                date = (date_raw.replace(".", "") + "0000000000000")[:13] if ls else ""
            else:
                date = date_raw[:13] if ls else ""
            x = json.loads(line[ls:])
            if x["cmd"] in _SKIP_KEYWORDS:
                continue
            out_file.write(
                date + json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n"
            )


files_to_process = sys.argv[1:]
for file in files_to_process:
    _trim_file(file)
