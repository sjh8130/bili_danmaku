#!/dev/null
from functools import lru_cache


@lru_cache
def DanmakuAttrType(attr: int):
    """
    Text
    """
    if attr == 0:
        return "DM "
    o = ""
    b = "00000000000000000000000000000000" + bin(attr).lstrip("0b")
    if b[-1] == "1":
        o += "[保护]"
    if b[-2] == "1":
        o += "[直播]"
    if b[-3] == "1":
        o += "[高赞]"
    if b[-4] == "1":
        o += "[03]"
    if b[-5] == "1":
        o += "[TODO_04]"
    if b[-6] == "1":
        o += "[05]"
    if b[-7] == "1":
        o += "[06]"
    if b[-8] == "1":
        o += "[07]"
    if b[-9] == "1":
        o += "[图片]"
    if b[-10] == "1":
        o += "[09]"
    if b[-11] == "1":
        o += "[10]"
    if b[-12] == "1":
        o += "[NFT]"
    if b[-13] == "1":
        o += "[12]"
    if b[-14] == "1":
        o += "[13]"
    if b[-15] == "1":
        o += "[14]"
    if b[-16] == "1":
        o += "[TODO_15]"
    if b[-17] == "1":
        o += "[16]"
    if b[-18] == "1":
        o += "[17]"
    if b[-19] == "1":
        o += "[18]"
    if b[-20] == "1":
        o += "[19]"
    if b[-21] == "1":
        o += "[20]"
    if b[-22] == "1":
        o += "[21]"
    if b[-23] == "1":
        o += "[22]"
    if b[-24] == "1":
        o += "[23]"
    if b[-25] == "1":
        o += "[24]"
    if b[-26] == "1":
        o += "[25]"
    if b[-27] == "1":
        o += "[26]"
    if b[-28] == "1":
        o += "[27]"
    if b[-29] == "1":
        o += "[28]"
    if b[-30] == "1":
        o += "[29]"
    if b[-31] == "1":
        o += "[30]"
    if b[-32] == "1":
        o += "[31]"
    if b[-33] == "1":
        o += "[32]"
    if b[-34] == "1":
        o += "[33]"
    return o
