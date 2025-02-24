import json
import os
import sys
import time

from lxml import etree
from tqdm import tqdm


def process_brec_xml_to_jsonl(file_path: str | os.PathLike):
    preload = open(file_path, "rb").read(512)
    if preload.find(b"encoding="):
        file = open(file_path, "rb").read()
    elif preload[:2] == b"\xef\xbb\xbf":
        file = open(file_path, "r", encoding="utf-8").read()[2:]
    else:
        file = open(file_path, "r", encoding="utf-8").read()
    tree = etree.XML(file)
    dmks = tree.findall(".//d")
    gifts = tree.findall(".//gift")
    # print(a)
    with open(
        "Z:\\BREC_xml_to_jsonl.jsonl" + os.path.basename(file_path),
        "a",
        buffering=2**20,
        encoding="utf-8",
    ) as fp:
        for dm in tqdm(dmks, leave=False):
            dm_info = json.loads(dm.attrib["raw"])
            fp.write(str(dm_info[0][4]))
            fp.write(
                json.dumps(
                    {"cmd": "DANMU_MSG", "info": dm_info},
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
            )
            fp.write("\n")
            # print(i.attrib["raw"])
            # b = 1
        for gift in tqdm(gifts, leave=False):
            gift_data = json.loads(gift.attrib["raw"])
            fp.write(
                str(int(gift_data["timestamp"] * 1000))
                + json.dumps(
                    {"cmd": "SEND_GIFT", "data": gift_data},
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
                + "\n"
            )


if __name__ == "__main__":
    file_paths = sys.argv[1:]
    # file_path = "Z:\\1.xml"
    for path in tqdm(file_paths, leave=False):
        process_brec_xml_to_jsonl(os.path.abspath(path))
    time.sleep(10)
