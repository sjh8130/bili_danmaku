import math
import time
from google.protobuf.json_format import MessageToJson
import requests
import json
import dm_pb2
import sys
from tqdm import tqdm

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
}

BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58):
    BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608


def BV_to_AV(input_BV: str):
    result = 0
    for i in range(6):
        result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
    return (result-BV_AV_add) ^ BV_AV_xor


def AV_to_BV(input_AV: int):
    input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
    result = list('BV1  4 1 7  ')
    for i in range(6):
        result[s[i]] = BV_AV_table[input_AV//58**i % 58]
    return ''.join(result)


def print_ERROR_412():
    print("         #    #    ###       #####   ###  ##  #")
    print("        ##   ##   #   #      #    # #   # # # #")
    print("       # #    #       #      #    # #   # #  ##")
    print("##### #  #    #     ##       #####  #   # #   #")
    print("      #####   #    #         #    # ##### #   #")
    print("         #    #   #          #    # #   # #   #")
    print("         #   ###  #####      #####  #   # #   #")


def print_ERROR_400():
    print("         #   ###   ###       #####  ####  #### ")
    print("        ##  #   # #   #      #      #   # #   #")
    print("       # #  #  ## #  ##      #      #   # #   #")
    print("##### #  #  # # # # # #      ####   ####  #### ")
    print("      ##### ##  # ##  #      #      #  #  #  # ")
    print("         #  #   # #   #      #      #   # #   #")
    print("         #   ###   ###       #####  #   # #   #")


def getDanmu(cid: str, segment_index: str):
    url = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_index}'

    time.sleep(1)
    danmu = requests.get(url, headers=headers).content
    try:
        if json.loads(danmu)["code"] == -412:
            print_ERROR_412()
        if json.loads(danmu)["code"] == -400:
            print_ERROR_400()
        return ""
    except UnicodeDecodeError:
        pass

    danmaku_seg = dm_pb2.DmSegMobileReply()
    danmaku_seg.ParseFromString(danmu)

    danmuobj = json.loads(MessageToJson(danmaku_seg))

    return danmuobj


def get_BAS_danmu(avid: str, cid: str):
    url_1 = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}&pid={avid}'
    data_1 = requests.get(url_1, headers=headers).content
    if json.loads(data_1)["code"] == -412:
        print_ERROR_412()
        return ""
    if json.loads(data_1)["code"] == -400:
        print_ERROR_400()
        return ""

    data_2 = dm_pb2.DmWebViewReply()
    data_2.ParseFromString(data_1)
    data_3 = json.loads(MessageToJson(data_2))["specialDms"]
    if len(data_3) == 0:
        return ""

    str_ = ""

    for i in data_3:
        data = requests.get(i, headers=headers).content
        if json.loads(data)["code"] == -412:
            print_ERROR_412()
            return ""
        if json.loads(data)["code"] == -400:
            print_ERROR_400()
            return ""

        danmaku_seg = dm_pb2.DmSegMobileReply()
        danmaku_seg.ParseFromString(data)
        data_c = json.loads(MessageToJson(danmaku_seg))
        if data_c != "" and data_c != "{}":
            str_ += json.dumps(data_c, ensure_ascii=False)
    return str_


if __name__ == '__main__':
    if sys.argv[1].find("https://www.bilibili.com/video/") == 0:
        vid = sys.argv[1].lstrip("https://www.bilibili.com/video/")
    else:
        vid = sys.argv[1]

    if vid.find("av") == 0:
        avid = vid
        avid_in = int(avid.lstrip("av"))
        bvid = AV_to_BV(avid_in)
    else:
        bvid = vid
        avid_in = BV_to_AV(bvid)
        avid = "av" + str(avid_in)

    """
    url = "https://api.bilibili.com/x/player/pagelist?bvid=" + bvid
    json_Data = json_List["data"]
    """
    url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    json_Resp = requests.get(url, headers=headers).content

    if json.loads(json_Resp)["code"] == -412:
        print(bvid, avid)
        print_ERROR_412()
        sys.exit(1)
    if json.loads(json_Resp)["code"] == -400:
        print(bvid, avid)
        print_ERROR_400()
        sys.exit(1)

    json_List = json.loads(json_Resp)
    json_Data = json_List["data"]
    sub_Items = json_Data["pages"]
    mainTitle = json_Data["title"]

    if json_List["data"]["stat"]["danmaku"] == 0:
        for i in range(0, len(sub_Items)):
            duration = int(sub_Items[i]["duration"])
            cid = str(sub_Items[i]["cid"])
            P_Title = str(sub_Items[i]["part"])
            show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, str(
                i+1), len(sub_Items), cid, duration, math.ceil(duration/360), mainTitle, P_Title)
            print(show_string)
            print("No danmu")
        sys.exit(1)

    for i in range(0, len(sub_Items)):
        duration = int(sub_Items[i]["duration"])
        cid = str(sub_Items[i]["cid"])
        P_Title = str(sub_Items[i]["part"])
        show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, str(
            i+1), len(sub_Items), cid, duration, math.ceil(duration/360), mainTitle, P_Title)
        print(show_string)
        progress_bar = tqdm(total=math.ceil(duration/360), leave=False)

        File_Name = str(bvid + "_" + avid + "_P" + str(i+1) + "_" + cid +
                        "_" + mainTitle + "_pTitle_" + P_Title + ".json").replace("/", "_")

        BAS_dm = get_BAS_danmu(avid=avid_in, cid=cid)
        if BAS_dm != "" and BAS_dm != "{}":
            with open(File_Name, "a", encoding="utf-8") as f:
                f.write(BAS_dm)

        for segments in range(1, math.ceil(duration/360)+1):
            ans = getDanmu(cid, str(segments))
            ans = json.dumps(ans, ensure_ascii=False)
            if ans != "{}" and ans != "":
                with open(File_Name, "a", encoding="utf-8") as f:
                    f.write(ans)

            progress_bar.update(1)
        progress_bar.close()
    sys.exit(0)
