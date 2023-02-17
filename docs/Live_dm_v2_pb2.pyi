from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class chatBubble(_message.Message):
    __slots__ = ["chat_bubble_color", "chat_bubble_type", "unknown_chat_bubble_0003", "unknown_chat_bubble_0004"]
    CHAT_BUBBLE_COLOR_FIELD_NUMBER: _ClassVar[int]
    CHAT_BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHAT_BUBBLE_0003_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHAT_BUBBLE_0004_FIELD_NUMBER: _ClassVar[int]
    chat_bubble_color: str
    chat_bubble_type: int
    unknown_chat_bubble_0003: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_chat_bubble_0004: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, chat_bubble_type: _Optional[int] = ..., chat_bubble_color: _Optional[str] = ..., unknown_chat_bubble_0003: _Optional[_Iterable[bytes]] = ..., unknown_chat_bubble_0004: _Optional[_Iterable[bytes]] = ...) -> None: ...

class dm_V2(_message.Message):
    __slots__ = ["chat_bubble", "color", "content", "ctime", "dm_type", "dmid", "dmid_2", "dmid_unique", "emots", "fontsize", "lottery", "midHash", "mode", "unknown_09", "unknown_11", "unknown_12", "unknown_16", "unknown_17", "unknown_19", "unknown_20", "unknown_21", "unknown_22", "unknown_23"]
    CHAT_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DMID_2_FIELD_NUMBER: _ClassVar[int]
    DMID_FIELD_NUMBER: _ClassVar[int]
    DMID_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    DM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMOTS_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    LOTTERY_FIELD_NUMBER: _ClassVar[int]
    MIDHASH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_09_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_19_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_20_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_21_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_22_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_23_FIELD_NUMBER: _ClassVar[int]
    chat_bubble: chatBubble
    color: int
    content: str
    ctime: int
    dm_type: int
    dmid: int
    dmid_2: int
    dmid_unique: str
    emots: _containers.RepeatedCompositeFieldContainer[emots]
    fontsize: int
    lottery: lottery
    midHash: str
    mode: int
    unknown_09: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_11: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_12: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_16: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_17: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_19: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_20: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_21: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_22: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_23: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dmid: _Optional[int] = ..., dmid_unique: _Optional[str] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., midHash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., unknown_09: _Optional[_Iterable[bytes]] = ..., dmid_2: _Optional[int] = ..., unknown_11: _Optional[_Iterable[bytes]] = ..., unknown_12: _Optional[_Iterable[bytes]] = ..., chat_bubble: _Optional[_Union[chatBubble, _Mapping]] = ..., dm_type: _Optional[int] = ..., emots: _Optional[_Iterable[_Union[emots, _Mapping]]] = ..., unknown_16: _Optional[_Iterable[bytes]] = ..., unknown_17: _Optional[_Iterable[bytes]] = ..., lottery: _Optional[_Union[lottery, _Mapping]] = ..., unknown_19: _Optional[_Iterable[bytes]] = ..., unknown_20: _Optional[_Iterable[bytes]] = ..., unknown_21: _Optional[_Iterable[bytes]] = ..., unknown_22: _Optional[_Iterable[bytes]] = ..., unknown_23: _Optional[_Iterable[bytes]] = ...) -> None: ...

class emots(_message.Message):
    __slots__ = ["desc", "detail"]
    DESC_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    desc: str
    detail: emots_detail
    def __init__(self, desc: _Optional[str] = ..., detail: _Optional[_Union[emots_detail, _Mapping]] = ...) -> None: ...

class emots_detail(_message.Message):
    __slots__ = ["emoticon_unique", "height", "in_player_area", "is_dynamic", "unknown_emots_detail_0005", "url", "width"]
    EMOTICON_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IN_PLAYER_AREA_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EMOTS_DETAIL_0005_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    emoticon_unique: str
    height: int
    in_player_area: bool
    is_dynamic: bool
    unknown_emots_detail_0005: _containers.RepeatedScalarFieldContainer[bytes]
    url: str
    width: int
    def __init__(self, emoticon_unique: _Optional[str] = ..., url: _Optional[str] = ..., in_player_area: bool = ..., is_dynamic: bool = ..., unknown_emots_detail_0005: _Optional[_Iterable[bytes]] = ..., height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class lottery(_message.Message):
    __slots__ = ["is_lottery", "lotteryId", "unknown_lottery_0001", "unknown_lottery_0004"]
    IS_LOTTERY_FIELD_NUMBER: _ClassVar[int]
    LOTTERYID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_0001_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_0004_FIELD_NUMBER: _ClassVar[int]
    is_lottery: int
    lotteryId: str
    unknown_lottery_0001: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_lottery_0004: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, unknown_lottery_0001: _Optional[_Iterable[bytes]] = ..., is_lottery: _Optional[int] = ..., lotteryId: _Optional[str] = ..., unknown_lottery_0004: _Optional[_Iterable[bytes]] = ...) -> None: ...
