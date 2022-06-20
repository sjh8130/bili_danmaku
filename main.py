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


def BV_to_AV(input_BV):
    result = 0
    for i in range(6):
        result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
    return (result-BV_AV_add) ^ BV_AV_xor


def AV_to_BV(input_AV):
    input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
    result = list('BV1  4 1 7  ')
    for i in range(6):
        result[s[i]] = BV_AV_table[input_AV//58**i % 58]
    return ''.join(result)


def getDanmu(cid, segment_index):
    url = 'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=' + cid + '&segment_index=' + str(segment_index)

    time.sleep(1)
    danmu = requests.get(url, headers=headers)
    try:
        if json.loads(danmu.content)["code"] == -412:
            print("-412 BAN")
            sys.exit(1)
    except EnvironmentError:
        print(1)

    try:
        if json.loads(danmu.content)["code"] == -400:
            print("-400 ERR")
            sys.exit(1)
    except EnvironmentError:
        print(1)

    danmaku_seg = dm_pb2.DmSegMobileReply()
    danmaku_seg.ParseFromString(danmu.content)

    danmuobj = json.loads(MessageToJson(danmaku_seg))

    return danmuobj


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
    json_All = requests.get(url, headers=headers).content
    json_List = json.loads(json_All)
    json_Data = json_List["data"]
    json_Data_page = json_Data["pages"]
    main_Title = json_Data["title"]
    # print(json_Data_page)

    if json_List["data"]["stat"]["danmaku"] == 0:
        for i in range(0, len(json_Data_page)):
            duration = int(json_Data_page[i]["duration"])
            cid = str(json_Data_page[i]["cid"])
            P_Title = str(json_Data_page[i]["part"])
            print(bvid, avid, "P", str(i+1), "/", len(json_Data_page), cid, duration, math.ceil(duration/360), main_Title, "|", P_Title)
        sys.exit(1)

    for i in range(0, len(json_Data_page)):
        duration = int(json_Data_page[i]["duration"])
        cid = str(json_Data_page[i]["cid"])
        P_Title = str(json_Data_page[i]["part"])
        print(bvid, avid, "P", str(i+1), "/", len(json_Data_page), cid, duration, math.ceil(duration/360), main_Title, "|", P_Title)
        progress_bar = tqdm(total=math.ceil(duration/360), leave=True, ncols=100)
        for segments in range(1, math.ceil(duration/360)+1):
            # print(vid, segment_index)
            ans = getDanmu(cid, segments)
            File_Name = str(bvid + "_" + avid + "_P" + str(i+1) + "_" + cid + "_" + main_Title + "_pTitle_" + P_Title + ".json").replace("/","_")
            with open(File_Name, "a", encoding="utf-8") as f:
                f.write(json.dumps(ans, ensure_ascii=False))
            progress_bar.update(1)
        progress_bar.close()
    sys.exit(0)

"""
}]}{"elems": [{
}, {
"""
