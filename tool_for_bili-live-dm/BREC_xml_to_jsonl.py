import json
import sys

from lxml import etree


def process_brec_xml_to_jsonl(file_path):
    preload = open(file_path, "rb").read(512)

    if preload.find(b"encoding="):
        file = open(file_path, "rb").read()
    elif preload[0:2] == b"\xef\xbb\xbf":
        file = open(file_path, "r", encoding="utf-8").read()[2:]
    else:
        file = open(file_path, "r", encoding="utf-8").read()

    tree = etree.XML(file)
    dmks = tree.findall(".//d")
    gifts = tree.findall(".//gift")
    # print(a)
    with open("Z:\\test.json", "a", encoding="utf-8") as w:
        for dm in dmks:
            dm_info = json.loads(dm.attrib["raw"])
            w.writelines(
                str(dm_info[0][4])
                + json.dumps(
                    {"cmd": "DANMU_MSG", "info": dm_info},
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
                + "\n"
            )
            # print(i.attrib["raw"])
            # b = 1
        for gift in gifts:
            gift_data = json.loads(gift.attrib["raw"])
            w.writelines(
                str(int(gift_data["timestamp"] * 1000))
                + json.dumps(
                    {"cmd": "SEND_GIFT", "data": gift_data},
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
                + "\n"
            )
            # print(i.attrib["raw"])
            # b = 1


if __name__ == "__main__":
    file_paths = sys.argv[1:]
    # file_path = "Z:\\1.xml"
    for path in file_paths:
        process_brec_xml_to_jsonl(path)
