import struct
from io import BytesIO

propNameMap = {
    1: "id",
    2: "translated_name",
    3: "idk_name",
    4: "model_path_hash",
    5: "text",
    6: "voice_file",
    7: "still_path_hash",
    8: "speech_balloon_type_id",
    "default": "unknown",
}


def unpackTextAsset(file_bytes, debug_name):
    file = BytesIO(file_bytes)
    offset = 0
    prop_count = struct.unpack("<I", file.read(4))[0]
    offset += 4
    entry_count = struct.unpack("<I", file.read(4))[0]
    offset += 4
    props = []
    for _ in range(prop_count):
        prop_type = struct.unpack("<I", file.read(4))[0]
        offset += 4
        prop_id = struct.unpack("<I", file.read(4))[0]
        offset += 4
        prop_name = propNameMap.get(prop_id, f"{propNameMap['default']}_{prop_id}")
        props.append({"type": prop_type, "name": prop_name})
    entries = []
    for _ in range(entry_count):
        entry = {}
        for prop in props:
            if prop["type"] == 0:  # int32
                entry[prop["name"]] = struct.unpack("<I", file.read(4))[0]
                offset += 4
            elif prop["type"] == 1:  # int64
                entry[prop["name"]] = int.from_bytes(file.read(8), "little", signed=True)
                offset += 8
            elif prop["type"] == 2:  # string
                str_len = struct.unpack("<I", file.read(4))[0]
                offset += 4
                entry[prop["name"]] = file.read(str_len).decode("utf-8")
                offset += str_len
            else:
                print(f"unpackTextAsset: unhandled property type {prop['type']} for file {debug_name}")
        entries.append(entry)
    return entries


if __name__ == "__main__":
    while True:
        file_name = input()
        with open(file_name, "rb") as f:
            print(unpackTextAsset(f.read(), file_name))
