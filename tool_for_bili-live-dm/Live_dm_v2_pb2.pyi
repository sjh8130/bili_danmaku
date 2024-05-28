from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class dm_V2(_message.Message):
    __slots__ = ["dmid", "dmid_unique", "mode", "fontsize", "color", "mid_hash", "content", "ctime", "unknown_09", "dmid_2", "unknown_11", "unknown_12", "chat_bubble", "dm_type", "emots", "unknown_16", "unknown_17", "lottery", "unknown_19", "unknown_20", "unknown_21", "unknown_22", "unknown_23", "unknown_24", "unknown_25", "unknown_26", "unknown_27", "unknown_28", "unknown_29", "unknown_30", "unknown_31", "unknown_32", "reserve_33", "reserve_34", "reserve_35", "reserve_36", "reserve_37", "reserve_38", "reserve_39", "reserve_40", "reserve_41", "reserve_42", "reserve_43", "reserve_44", "reserve_45", "reserve_46", "reserve_47", "reserve_48", "reserve_49", "reserve_50", "reserve_51", "reserve_52", "reserve_53", "reserve_54", "reserve_55", "reserve_56", "reserve_57", "reserve_58", "reserve_59", "reserve_60", "reserve_61", "reserve_62", "reserve_63", "reserve_64"]
    DMID_FIELD_NUMBER: _ClassVar[int]
    DMID_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MID_HASH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_09_FIELD_NUMBER: _ClassVar[int]
    DMID_2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_12_FIELD_NUMBER: _ClassVar[int]
    CHAT_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    DM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMOTS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_17_FIELD_NUMBER: _ClassVar[int]
    LOTTERY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_19_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_20_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_21_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_22_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_23_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_24_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_25_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_27_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_29_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_30_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_32_FIELD_NUMBER: _ClassVar[int]
    RESERVE_33_FIELD_NUMBER: _ClassVar[int]
    RESERVE_34_FIELD_NUMBER: _ClassVar[int]
    RESERVE_35_FIELD_NUMBER: _ClassVar[int]
    RESERVE_36_FIELD_NUMBER: _ClassVar[int]
    RESERVE_37_FIELD_NUMBER: _ClassVar[int]
    RESERVE_38_FIELD_NUMBER: _ClassVar[int]
    RESERVE_39_FIELD_NUMBER: _ClassVar[int]
    RESERVE_40_FIELD_NUMBER: _ClassVar[int]
    RESERVE_41_FIELD_NUMBER: _ClassVar[int]
    RESERVE_42_FIELD_NUMBER: _ClassVar[int]
    RESERVE_43_FIELD_NUMBER: _ClassVar[int]
    RESERVE_44_FIELD_NUMBER: _ClassVar[int]
    RESERVE_45_FIELD_NUMBER: _ClassVar[int]
    RESERVE_46_FIELD_NUMBER: _ClassVar[int]
    RESERVE_47_FIELD_NUMBER: _ClassVar[int]
    RESERVE_48_FIELD_NUMBER: _ClassVar[int]
    RESERVE_49_FIELD_NUMBER: _ClassVar[int]
    RESERVE_50_FIELD_NUMBER: _ClassVar[int]
    RESERVE_51_FIELD_NUMBER: _ClassVar[int]
    RESERVE_52_FIELD_NUMBER: _ClassVar[int]
    RESERVE_53_FIELD_NUMBER: _ClassVar[int]
    RESERVE_54_FIELD_NUMBER: _ClassVar[int]
    RESERVE_55_FIELD_NUMBER: _ClassVar[int]
    RESERVE_56_FIELD_NUMBER: _ClassVar[int]
    RESERVE_57_FIELD_NUMBER: _ClassVar[int]
    RESERVE_58_FIELD_NUMBER: _ClassVar[int]
    RESERVE_59_FIELD_NUMBER: _ClassVar[int]
    RESERVE_60_FIELD_NUMBER: _ClassVar[int]
    RESERVE_61_FIELD_NUMBER: _ClassVar[int]
    RESERVE_62_FIELD_NUMBER: _ClassVar[int]
    RESERVE_63_FIELD_NUMBER: _ClassVar[int]
    RESERVE_64_FIELD_NUMBER: _ClassVar[int]
    dmid: int
    dmid_unique: str
    mode: int
    fontsize: int
    color: int
    mid_hash: str
    content: str
    ctime: int
    unknown_09: _containers.RepeatedScalarFieldContainer[bytes]
    dmid_2: int
    unknown_11: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_12: _containers.RepeatedScalarFieldContainer[bytes]
    chat_bubble: chat_bubble
    dm_type: int
    emots: _containers.RepeatedCompositeFieldContainer[emots]
    unknown_16: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_17: _containers.RepeatedScalarFieldContainer[bytes]
    lottery: lottery
    unknown_19: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_20: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_21: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_22: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_23: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_24: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_25: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_26: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_27: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_28: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_29: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_30: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_31: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_32: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_33: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_34: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_35: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_36: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_37: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_38: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_39: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_40: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_41: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_42: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_43: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_44: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_45: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_46: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_47: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_48: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_49: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_50: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_51: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_52: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_53: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_54: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_55: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_56: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_57: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_58: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_59: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_60: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_61: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_62: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_63: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_64: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dmid: _Optional[int] = ..., dmid_unique: _Optional[str] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., mid_hash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., unknown_09: _Optional[_Iterable[bytes]] = ..., dmid_2: _Optional[int] = ..., unknown_11: _Optional[_Iterable[bytes]] = ..., unknown_12: _Optional[_Iterable[bytes]] = ..., chat_bubble: _Optional[_Union[chat_bubble, _Mapping]] = ..., dm_type: _Optional[int] = ..., emots: _Optional[_Iterable[_Union[emots, _Mapping]]] = ..., unknown_16: _Optional[_Iterable[bytes]] = ..., unknown_17: _Optional[_Iterable[bytes]] = ..., lottery: _Optional[_Union[lottery, _Mapping]] = ..., unknown_19: _Optional[_Iterable[bytes]] = ..., unknown_20: _Optional[_Iterable[bytes]] = ..., unknown_21: _Optional[_Iterable[bytes]] = ..., unknown_22: _Optional[_Iterable[bytes]] = ..., unknown_23: _Optional[_Iterable[bytes]] = ..., unknown_24: _Optional[_Iterable[bytes]] = ..., unknown_25: _Optional[_Iterable[bytes]] = ..., unknown_26: _Optional[_Iterable[bytes]] = ..., unknown_27: _Optional[_Iterable[bytes]] = ..., unknown_28: _Optional[_Iterable[bytes]] = ..., unknown_29: _Optional[_Iterable[bytes]] = ..., unknown_30: _Optional[_Iterable[bytes]] = ..., unknown_31: _Optional[_Iterable[bytes]] = ..., unknown_32: _Optional[_Iterable[bytes]] = ..., reserve_33: _Optional[_Iterable[bytes]] = ..., reserve_34: _Optional[_Iterable[bytes]] = ..., reserve_35: _Optional[_Iterable[bytes]] = ..., reserve_36: _Optional[_Iterable[bytes]] = ..., reserve_37: _Optional[_Iterable[bytes]] = ..., reserve_38: _Optional[_Iterable[bytes]] = ..., reserve_39: _Optional[_Iterable[bytes]] = ..., reserve_40: _Optional[_Iterable[bytes]] = ..., reserve_41: _Optional[_Iterable[bytes]] = ..., reserve_42: _Optional[_Iterable[bytes]] = ..., reserve_43: _Optional[_Iterable[bytes]] = ..., reserve_44: _Optional[_Iterable[bytes]] = ..., reserve_45: _Optional[_Iterable[bytes]] = ..., reserve_46: _Optional[_Iterable[bytes]] = ..., reserve_47: _Optional[_Iterable[bytes]] = ..., reserve_48: _Optional[_Iterable[bytes]] = ..., reserve_49: _Optional[_Iterable[bytes]] = ..., reserve_50: _Optional[_Iterable[bytes]] = ..., reserve_51: _Optional[_Iterable[bytes]] = ..., reserve_52: _Optional[_Iterable[bytes]] = ..., reserve_53: _Optional[_Iterable[bytes]] = ..., reserve_54: _Optional[_Iterable[bytes]] = ..., reserve_55: _Optional[_Iterable[bytes]] = ..., reserve_56: _Optional[_Iterable[bytes]] = ..., reserve_57: _Optional[_Iterable[bytes]] = ..., reserve_58: _Optional[_Iterable[bytes]] = ..., reserve_59: _Optional[_Iterable[bytes]] = ..., reserve_60: _Optional[_Iterable[bytes]] = ..., reserve_61: _Optional[_Iterable[bytes]] = ..., reserve_62: _Optional[_Iterable[bytes]] = ..., reserve_63: _Optional[_Iterable[bytes]] = ..., reserve_64: _Optional[_Iterable[bytes]] = ...) -> None: ...

class emots(_message.Message):
    __slots__ = ["desc", "detail", "unknown_XXX_03", "unknown_XXX_04"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_03_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_04_FIELD_NUMBER: _ClassVar[int]
    desc: str
    detail: emots_detail
    unknown_XXX_03: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_04: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, desc: _Optional[str] = ..., detail: _Optional[_Union[emots_detail, _Mapping]] = ..., unknown_XXX_03: _Optional[_Iterable[bytes]] = ..., unknown_XXX_04: _Optional[_Iterable[bytes]] = ...) -> None: ...

class emots_detail(_message.Message):
    __slots__ = ["emoticon_unique", "url", "in_player_area", "is_dynamic", "unknown_emots_detail_0005", "height", "width", "reserve_emots_detail_08", "reserve_emots_detail_09", "reserve_emots_detail_10", "reserve_emots_detail_11", "reserve_emots_detail_12", "reserve_emots_detail_13", "reserve_emots_detail_14", "reserve_emots_detail_15", "reserve_emots_detail_16"]
    EMOTICON_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IN_PLAYER_AREA_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EMOTS_DETAIL_0005_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_08_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_09_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_10_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_11_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_12_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_13_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_14_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_15_FIELD_NUMBER: _ClassVar[int]
    RESERVE_EMOTS_DETAIL_16_FIELD_NUMBER: _ClassVar[int]
    emoticon_unique: str
    url: str
    in_player_area: bool
    is_dynamic: bool
    unknown_emots_detail_0005: _containers.RepeatedScalarFieldContainer[bytes]
    height: int
    width: int
    reserve_emots_detail_08: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_09: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_10: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_11: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_12: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_13: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_14: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_15: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_emots_detail_16: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, emoticon_unique: _Optional[str] = ..., url: _Optional[str] = ..., in_player_area: bool = ..., is_dynamic: bool = ..., unknown_emots_detail_0005: _Optional[_Iterable[bytes]] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., reserve_emots_detail_08: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_09: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_10: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_11: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_12: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_13: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_14: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_15: _Optional[_Iterable[bytes]] = ..., reserve_emots_detail_16: _Optional[_Iterable[bytes]] = ...) -> None: ...

class lottery(_message.Message):
    __slots__ = ["unknown_lottery_0001", "is_lottery", "lottery_id", "unknown_lottery_0004", "reserve_lottery_05", "reserve_lottery_06", "reserve_lottery_07", "reserve_lottery_08"]
    UNKNOWN_LOTTERY_0001_FIELD_NUMBER: _ClassVar[int]
    IS_LOTTERY_FIELD_NUMBER: _ClassVar[int]
    LOTTERY_ID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_0004_FIELD_NUMBER: _ClassVar[int]
    RESERVE_LOTTERY_05_FIELD_NUMBER: _ClassVar[int]
    RESERVE_LOTTERY_06_FIELD_NUMBER: _ClassVar[int]
    RESERVE_LOTTERY_07_FIELD_NUMBER: _ClassVar[int]
    RESERVE_LOTTERY_08_FIELD_NUMBER: _ClassVar[int]
    unknown_lottery_0001: _containers.RepeatedScalarFieldContainer[bytes]
    is_lottery: int
    lottery_id: str
    unknown_lottery_0004: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_lottery_05: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_lottery_06: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_lottery_07: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_lottery_08: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, unknown_lottery_0001: _Optional[_Iterable[bytes]] = ..., is_lottery: _Optional[int] = ..., lottery_id: _Optional[str] = ..., unknown_lottery_0004: _Optional[_Iterable[bytes]] = ..., reserve_lottery_05: _Optional[_Iterable[bytes]] = ..., reserve_lottery_06: _Optional[_Iterable[bytes]] = ..., reserve_lottery_07: _Optional[_Iterable[bytes]] = ..., reserve_lottery_08: _Optional[_Iterable[bytes]] = ...) -> None: ...

class chat_bubble(_message.Message):
    __slots__ = ["chat_bubble_type", "chat_bubble_color", "unknown_chat_bubble_0003", "unknown_chat_bubble_0004", "reserve_chat_bubble_05", "reserve_chat_bubble_06", "reserve_chat_bubble_07", "reserve_chat_bubble_08"]
    CHAT_BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_BUBBLE_COLOR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHAT_BUBBLE_0003_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHAT_BUBBLE_0004_FIELD_NUMBER: _ClassVar[int]
    RESERVE_CHAT_BUBBLE_05_FIELD_NUMBER: _ClassVar[int]
    RESERVE_CHAT_BUBBLE_06_FIELD_NUMBER: _ClassVar[int]
    RESERVE_CHAT_BUBBLE_07_FIELD_NUMBER: _ClassVar[int]
    RESERVE_CHAT_BUBBLE_08_FIELD_NUMBER: _ClassVar[int]
    chat_bubble_type: int
    chat_bubble_color: str
    unknown_chat_bubble_0003: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_chat_bubble_0004: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_chat_bubble_05: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_chat_bubble_06: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_chat_bubble_07: _containers.RepeatedScalarFieldContainer[bytes]
    reserve_chat_bubble_08: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, chat_bubble_type: _Optional[int] = ..., chat_bubble_color: _Optional[str] = ..., unknown_chat_bubble_0003: _Optional[_Iterable[bytes]] = ..., unknown_chat_bubble_0004: _Optional[_Iterable[bytes]] = ..., reserve_chat_bubble_05: _Optional[_Iterable[bytes]] = ..., reserve_chat_bubble_06: _Optional[_Iterable[bytes]] = ..., reserve_chat_bubble_07: _Optional[_Iterable[bytes]] = ..., reserve_chat_bubble_08: _Optional[_Iterable[bytes]] = ...) -> None: ...

class unknown(_message.Message):
    __slots__ = ["unknown_XXX_01", "unknown_XXX_02", "unknown_XXX_03", "unknown_XXX_04", "unknown_XXX_05", "unknown_XXX_06", "unknown_XXX_07", "unknown_XXX_08", "unknown_XXX_09", "unknown_XXX_10", "unknown_XXX_11", "unknown_XXX_12", "unknown_XXX_13", "unknown_XXX_14", "unknown_XXX_15", "unknown_XXX_16", "unknown_XXX_17", "unknown_XXX_18", "unknown_XXX_19", "unknown_XXX_20", "unknown_XXX_21", "unknown_XXX_22", "unknown_XXX_23", "unknown_XXX_24", "unknown_XXX_25", "unknown_XXX_26", "unknown_XXX_27", "unknown_XXX_28", "unknown_XXX_29", "unknown_XXX_30", "unknown_XXX_31", "unknown_XXX_32", "unknown_XXX_33", "unknown_XXX_34", "unknown_XXX_35", "unknown_XXX_36", "unknown_XXX_37", "unknown_XXX_38", "unknown_XXX_39", "unknown_XXX_40", "unknown_XXX_41", "unknown_XXX_42", "unknown_XXX_43", "unknown_XXX_44", "unknown_XXX_45", "unknown_XXX_46", "unknown_XXX_47", "unknown_XXX_48", "unknown_XXX_49", "unknown_XXX_50", "unknown_XXX_51", "unknown_XXX_52", "unknown_XXX_53", "unknown_XXX_54", "unknown_XXX_55", "unknown_XXX_56", "unknown_XXX_57", "unknown_XXX_58", "unknown_XXX_59", "unknown_XXX_60", "unknown_XXX_61", "unknown_XXX_62", "unknown_XXX_63", "unknown_XXX_64"]
    UNKNOWN_XXX_01_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_02_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_03_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_04_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_05_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_06_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_07_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_08_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_09_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_13_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_15_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_18_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_19_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_20_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_21_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_22_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_23_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_24_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_25_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_27_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_29_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_30_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_33_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_34_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_35_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_36_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_37_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_38_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_39_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_40_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_41_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_42_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_43_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_44_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_45_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_46_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_47_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_48_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_49_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_50_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_51_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_52_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_53_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_54_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_55_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_56_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_57_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_58_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_59_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_60_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_61_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_62_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_63_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_XXX_64_FIELD_NUMBER: _ClassVar[int]
    unknown_XXX_01: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_02: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_03: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_04: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_05: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_06: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_07: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_08: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_09: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_10: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_11: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_12: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_13: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_14: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_15: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_16: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_17: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_18: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_19: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_20: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_21: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_22: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_23: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_24: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_25: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_26: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_27: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_28: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_29: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_30: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_31: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_32: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_33: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_34: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_35: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_36: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_37: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_38: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_39: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_40: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_41: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_42: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_43: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_44: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_45: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_46: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_47: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_48: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_49: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_50: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_51: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_52: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_53: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_54: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_55: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_56: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_57: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_58: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_59: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_60: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_61: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_62: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_63: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_XXX_64: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, unknown_XXX_01: _Optional[_Iterable[bytes]] = ..., unknown_XXX_02: _Optional[_Iterable[bytes]] = ..., unknown_XXX_03: _Optional[_Iterable[bytes]] = ..., unknown_XXX_04: _Optional[_Iterable[bytes]] = ..., unknown_XXX_05: _Optional[_Iterable[bytes]] = ..., unknown_XXX_06: _Optional[_Iterable[bytes]] = ..., unknown_XXX_07: _Optional[_Iterable[bytes]] = ..., unknown_XXX_08: _Optional[_Iterable[bytes]] = ..., unknown_XXX_09: _Optional[_Iterable[bytes]] = ..., unknown_XXX_10: _Optional[_Iterable[bytes]] = ..., unknown_XXX_11: _Optional[_Iterable[bytes]] = ..., unknown_XXX_12: _Optional[_Iterable[bytes]] = ..., unknown_XXX_13: _Optional[_Iterable[bytes]] = ..., unknown_XXX_14: _Optional[_Iterable[bytes]] = ..., unknown_XXX_15: _Optional[_Iterable[bytes]] = ..., unknown_XXX_16: _Optional[_Iterable[bytes]] = ..., unknown_XXX_17: _Optional[_Iterable[bytes]] = ..., unknown_XXX_18: _Optional[_Iterable[bytes]] = ..., unknown_XXX_19: _Optional[_Iterable[bytes]] = ..., unknown_XXX_20: _Optional[_Iterable[bytes]] = ..., unknown_XXX_21: _Optional[_Iterable[bytes]] = ..., unknown_XXX_22: _Optional[_Iterable[bytes]] = ..., unknown_XXX_23: _Optional[_Iterable[bytes]] = ..., unknown_XXX_24: _Optional[_Iterable[bytes]] = ..., unknown_XXX_25: _Optional[_Iterable[bytes]] = ..., unknown_XXX_26: _Optional[_Iterable[bytes]] = ..., unknown_XXX_27: _Optional[_Iterable[bytes]] = ..., unknown_XXX_28: _Optional[_Iterable[bytes]] = ..., unknown_XXX_29: _Optional[_Iterable[bytes]] = ..., unknown_XXX_30: _Optional[_Iterable[bytes]] = ..., unknown_XXX_31: _Optional[_Iterable[bytes]] = ..., unknown_XXX_32: _Optional[_Iterable[bytes]] = ..., unknown_XXX_33: _Optional[_Iterable[bytes]] = ..., unknown_XXX_34: _Optional[_Iterable[bytes]] = ..., unknown_XXX_35: _Optional[_Iterable[bytes]] = ..., unknown_XXX_36: _Optional[_Iterable[bytes]] = ..., unknown_XXX_37: _Optional[_Iterable[bytes]] = ..., unknown_XXX_38: _Optional[_Iterable[bytes]] = ..., unknown_XXX_39: _Optional[_Iterable[bytes]] = ..., unknown_XXX_40: _Optional[_Iterable[bytes]] = ..., unknown_XXX_41: _Optional[_Iterable[bytes]] = ..., unknown_XXX_42: _Optional[_Iterable[bytes]] = ..., unknown_XXX_43: _Optional[_Iterable[bytes]] = ..., unknown_XXX_44: _Optional[_Iterable[bytes]] = ..., unknown_XXX_45: _Optional[_Iterable[bytes]] = ..., unknown_XXX_46: _Optional[_Iterable[bytes]] = ..., unknown_XXX_47: _Optional[_Iterable[bytes]] = ..., unknown_XXX_48: _Optional[_Iterable[bytes]] = ..., unknown_XXX_49: _Optional[_Iterable[bytes]] = ..., unknown_XXX_50: _Optional[_Iterable[bytes]] = ..., unknown_XXX_51: _Optional[_Iterable[bytes]] = ..., unknown_XXX_52: _Optional[_Iterable[bytes]] = ..., unknown_XXX_53: _Optional[_Iterable[bytes]] = ..., unknown_XXX_54: _Optional[_Iterable[bytes]] = ..., unknown_XXX_55: _Optional[_Iterable[bytes]] = ..., unknown_XXX_56: _Optional[_Iterable[bytes]] = ..., unknown_XXX_57: _Optional[_Iterable[bytes]] = ..., unknown_XXX_58: _Optional[_Iterable[bytes]] = ..., unknown_XXX_59: _Optional[_Iterable[bytes]] = ..., unknown_XXX_60: _Optional[_Iterable[bytes]] = ..., unknown_XXX_61: _Optional[_Iterable[bytes]] = ..., unknown_XXX_62: _Optional[_Iterable[bytes]] = ..., unknown_XXX_63: _Optional[_Iterable[bytes]] = ..., unknown_XXX_64: _Optional[_Iterable[bytes]] = ...) -> None: ...