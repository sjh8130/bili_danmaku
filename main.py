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
    danmu_proto = requests.get(url, headers=headers).content
    try:
        status_code = json.loads(danmu_proto)["code"]
        if status_code == -412:
            print_ERROR_412()
            return b""
        if status_code == -400:
            print_ERROR_400()
            return b""
    except UnicodeDecodeError:
        pass
    return danmu_proto


def get_BAS_danmu(avid: str, cid: str):
    url_1 = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}&pid={avid}'
    data_1 = requests.get(url_1, headers=headers).content
    try:
        status_code = json.loads(data_1)["code"]
        if status_code == -412:
            print_ERROR_412()
            return b""
        if status_code == -400:
            print_ERROR_400()
            return b""
    except UnicodeDecodeError:
        pass

    data_2 = dm_pb2.DmWebViewReply()
    data_2.ParseFromString(data_1)
    try:
        data_3 = json.loads(MessageToJson(data_2))["specialDms"]
    except KeyError:
        return b""
    if len(data_3) == 0:
        return b""
    BAS_danmu_proto = b""
    for i in data_3:
        data = requests.get(i, headers=headers).content
        time.sleep(1)
        try:
            status_code = json.loads(data)["code"]
            if status_code == -412:
                print_ERROR_412()
                return b""
            if status_code == -400:
                print_ERROR_400()
                return b""
        except UnicodeDecodeError:
            BAS_danmu_proto += data
            pass
    return BAS_danmu_proto


if __name__ == '__main__':
    # start_time = time.time()
    if sys.argv[1].find("https://www.bilibili.com/video/") == 0:
        vid = sys.argv[1].lstrip("https://www.bilibili.com/video/")
    elif sys.argv[1].find("http://www.bilibili.com/video/") == 0:
        vid = sys.argv[1].lstrip("http://www.bilibili.com/video/")
    elif sys.argv[1].find("https://b23.tv/BV1") == 0:
        vid = sys.argv[1].lstrip("https://b23.tv/")
    else:
        vid = sys.argv[1]
    vid = vid.split("?")[0].split("/")[0]
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
    json_List = json.loads(json_Resp)

    if json_List["code"] == -412:
        print(bvid, avid)
        print_ERROR_412()
        # print("总计用时:", time.time()-start_time) # 性能测试
        sys.exit(1)
    if json_List["code"] == -400:
        print(bvid, avid)
        print_ERROR_400()
        # print("总计用时:", time.time()-start_time) # 性能测试
        sys.exit(1)

    json_Data = json_List["data"]
    sub_Items = json_Data["pages"]
    mainTitle = json_Data["title"]
    sub_Items_Len = len(sub_Items)

    if json_List["data"]["stat"]["danmaku"] == 0:
        for i in range(sub_Items_Len):
            duration = int(sub_Items[i]["duration"])
            cid = str(sub_Items[i]["cid"])
            P_Title = str(sub_Items[i]["part"])
            show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, str(i+1), sub_Items_Len, cid, duration, math.ceil(duration/360), mainTitle, P_Title)
            print(show_string)
            print("No danmu")
            # print("总计用时:", time.time()-start_time) # 性能测试
        sys.exit(1)

    for i in range(sub_Items_Len):
        # 分P开始时间 = time.time() # 性能测试
        Danmaku_Binary = b""
        Temp_Binary = b""
        Temp_Binary = dm_pb2.DmSegMobileReply()
        duration = int(sub_Items[i]["duration"])
        cid = str(sub_Items[i]["cid"])
        P_Title = str(sub_Items[i]["part"])
        show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, str(i+1), sub_Items_Len, cid, duration, math.ceil(duration/360), mainTitle, P_Title)
        print(show_string)

        File_Name = str(bvid + "_" + avid + "_P" + str(i+1) + "_" + cid + "_" + mainTitle + "_pTitle_" + P_Title + ".json").replace("/", "_")

        # BAS开始时间 = time.time() # 性能测试
        BAS_danmu = get_BAS_danmu(avid=avid_in, cid=cid)
        Danmaku_Binary += BAS_danmu
        # BAS结束时间 = time.time() # 性能测试

        Progress_Bar = tqdm(total=math.ceil(duration/360), leave=False)

        for segments in range(math.ceil(duration/360)):
            Danmaku_sub_Items = getDanmu(cid, str(segments+1))
            Danmaku_Binary += Danmaku_sub_Items
            Progress_Bar.update(1)
        Temp_Binary.ParseFromString(Danmaku_Binary)
        Progress_Bar.close()
        with open(File_Name, "w", encoding="utf-8") as f:
            # 写入开始时间 = time.time() # 性能测试
            # print("开始写入") # 性能测试
            f.write(json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False))
        # 分P结束时间 = time.time() # 性能测试
        # print(f"分P {i+1}用时: {分P结束时间-分P开始时间}, BAS用时: {BAS结束时间-BAS开始时间} 写入用时: {分P结束时间-写入开始时间}") # 性能测试
    # print("总计用时:", time.time()-start_time) # 性能测试
    sys.exit(0)
