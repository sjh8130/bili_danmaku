ALPHABET = "FcwAPNKTMug3GV5Lj7EJnHpWsx4tb8haYeviqBz6rkCy12mUSDQX9RdoZf"
ENCODE_MAP = (8, 7, 0, 5, 1, 3, 2, 4, 6)
DECODE_MAP = (6, 4, 2, 3, 1, 5, 0, 7, 8)


def bv2av(bvid: str) -> int:
    bvid = bvid[3:]
    tmp = 0
    for i in range(9):
        idx = ALPHABET.index(bvid[DECODE_MAP[i]])
        tmp = tmp * 58 + idx
    return (tmp & 2251799813685247) ^ 23442827791579


def av2bv(a: int) -> str:
    b = ["", "", "", "", "", "", "", "", ""]
    tmp = (2251799813685248 | a) ^ 23442827791579
    for i in range(9):
        b[ENCODE_MAP[i]] = ALPHABET[tmp % 58]
        tmp //= 58
    return "BV1" + "".join(b)
