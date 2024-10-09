import base64
import brotli
import json


def decode_input():
    while True:
        try:
            a = bytes(input("请输入数据: "), "utf-8")
            b = base64.b64decode(a)
            c = brotli.decompress(b[16:])
            d = json.loads(c[16:])
            e = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
            print(e)
        except Exception as ex:
            print(f"处理时发生错误: {ex}")


if __name__ == "__main__":
    decode_input()
