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


def getDanmu(cid, segment_index):
    url = 'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=' + cid + '&segment_index=' + str(segment_index)

    time.sleep(2)
    danmu = requests.get(url, headers=headers)

    danmaku_seg = dm_pb2.DmSegMobileReply()
    danmaku_seg.ParseFromString(danmu.content)

    danmuobj = json.loads(MessageToJson(danmaku_seg))

    return danmuobj


if __name__ == '__main__':
    bvid = sys.argv[1]

    url = "https://api.bilibili.com/x/player/pagelist?bvid=" + bvid
    strCidJson = requests.get(url, headers=headers).content
    jsonCid = json.loads(strCidJson)
    # print(jsonCid["data"])

    for i in range(0, len(jsonCid["data"])):
        duration = int(jsonCid["data"][i]["duration"])
        cid = str(jsonCid["data"][i]["cid"])
        print(bvid,"P", i+1, "/", len(jsonCid["data"]), cid, duration, math.ceil(duration/360))
        pbar = tqdm(total=math.ceil(duration/360))
        for segment_index in range(1, math.ceil(duration/360)+1):
            # print(bvid, segment_index)
            ans = getDanmu(cid, segment_index)
            with open(bvid+"_P"+str(i+1)+"_"+cid+".json", "a", encoding="utf-8") as f:
                f.write(json.dumps(ans, ensure_ascii=False))
            pbar.update(1)
        pbar.close()

"""
}]}{"elems": [{
}, {
"""
