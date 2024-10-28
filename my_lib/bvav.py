# -*- coding: utf-8 -*-

_DATA = [b'F', b'c', b'w', b'A', b'P', b'N', b'K', b'T', b'M', b'u', b'g', b'3', b'G', b'V', b'5', b'L', b'j', b'7', b'E', b'J', b'n', b'H', b'p', b'W', b's', b'x', b'4', b't', b'b', b'8', b'h', b'a', b'Y', b'e', b'v', b'i', b'q', b'B', b'z', b'6', b'r', b'k', b'C', b'y', b'1', b'2', b'm', b'U', b'S', b'D', b'Q', b'X', b'9', b'R', b'd', b'o', b'Z', b'f']

def BV2AV(b: str) -> int:
    b = list(b)
    b[3], b[9] = b[9], b[3]
    b[4], b[7] = b[7], b[4]
    b = b[3:]
    tmp = 0
    for i in b:
        idx = _DATA.index(i.encode())
        tmp = tmp * 58 + idx
    return (tmp & (2 << 50 - 1)) ^ 23442827791579


def AV2BV(a: int) -> str:
    b = [b"B", b"V", b"1", b"0", b"0", b"0", b"0", b"0", b"0", b"0", b"0", b"0"]
    bv_idx = 11
    tmp = (2 << 50 | a) ^ 23442827791579
    while int(tmp) != 0:
        b[bv_idx] = _DATA[int(tmp % 58)]
        tmp /= 58
        bv_idx -= 1
    b[3], b[9] = b[9], b[3]
    b[4], b[7] = b[7], b[4]
    return "".join([i.decode() for i in b])
