from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class dm_V2(_message.Message):
    __slots__ = ["id_str", "mode", "fontsize", "color", "mid_hash", "content", "ctime", "unknown_08", "dmid", "unknown_10", "type", "chat_bubble", "DmType", "emots", "unknown_15", "unknown_16", "lottery", "unknown_18", "validation", "userinfo", "fan_medal_ext", "unknown_22", "unknown_23", "unknown_24", "unknown_25", "unknown_26", "unknown_27", "unknown_28", "unknown_29", "unknown_30", "unknown_31", "unknown_32"]
    ID_STR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MID_HASH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_08_FIELD_NUMBER: _ClassVar[int]
    DMID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_10_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_BUBBLE_FIELD_NUMBER: _ClassVar[int]
    DMTYPE_FIELD_NUMBER: _ClassVar[int]
    EMOTS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_15_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_16_FIELD_NUMBER: _ClassVar[int]
    LOTTERY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_18_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    USERINFO_FIELD_NUMBER: _ClassVar[int]
    FAN_MEDAL_EXT_FIELD_NUMBER: _ClassVar[int]
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
    id_str: str
    mode: int
    fontsize: int
    color: int
    mid_hash: str
    content: str
    ctime: int
    unknown_08: _containers.RepeatedScalarFieldContainer[bytes]
    dmid: int
    unknown_10: _containers.RepeatedScalarFieldContainer[bytes]
    type: int
    chat_bubble: chat_bubble
    DmType: int
    emots: _containers.RepeatedCompositeFieldContainer[emots]
    unknown_15: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_16: _containers.RepeatedScalarFieldContainer[bytes]
    lottery: lottery
    unknown_18: _containers.RepeatedScalarFieldContainer[bytes]
    validation: validation
    userinfo: userinfo
    fan_medal_ext: fan_medal_ext
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
    def __init__(self, id_str: _Optional[str] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., mid_hash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., unknown_08: _Optional[_Iterable[bytes]] = ..., dmid: _Optional[int] = ..., unknown_10: _Optional[_Iterable[bytes]] = ..., type: _Optional[int] = ..., chat_bubble: _Optional[_Union[chat_bubble, _Mapping]] = ..., DmType: _Optional[int] = ..., emots: _Optional[_Iterable[_Union[emots, _Mapping]]] = ..., unknown_15: _Optional[_Iterable[bytes]] = ..., unknown_16: _Optional[_Iterable[bytes]] = ..., lottery: _Optional[_Union[lottery, _Mapping]] = ..., unknown_18: _Optional[_Iterable[bytes]] = ..., validation: _Optional[_Union[validation, _Mapping]] = ..., userinfo: _Optional[_Union[userinfo, _Mapping]] = ..., fan_medal_ext: _Optional[_Union[fan_medal_ext, _Mapping]] = ..., unknown_22: _Optional[_Iterable[bytes]] = ..., unknown_23: _Optional[_Iterable[bytes]] = ..., unknown_24: _Optional[_Iterable[bytes]] = ..., unknown_25: _Optional[_Iterable[bytes]] = ..., unknown_26: _Optional[_Iterable[bytes]] = ..., unknown_27: _Optional[_Iterable[bytes]] = ..., unknown_28: _Optional[_Iterable[bytes]] = ..., unknown_29: _Optional[_Iterable[bytes]] = ..., unknown_30: _Optional[_Iterable[bytes]] = ..., unknown_31: _Optional[_Iterable[bytes]] = ..., unknown_32: _Optional[_Iterable[bytes]] = ...) -> None: ...

class chat_bubble(_message.Message):
    __slots__ = ["chat_bubble_type", "chat_bubble_color"]
    CHAT_BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_BUBBLE_COLOR_FIELD_NUMBER: _ClassVar[int]
    chat_bubble_type: int
    chat_bubble_color: str
    def __init__(self, chat_bubble_type: _Optional[int] = ..., chat_bubble_color: _Optional[str] = ...) -> None: ...

class emots(_message.Message):
    __slots__ = ["description", "detail", "unknown_emots_03", "unknown_emots_04"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EMOTS_03_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EMOTS_04_FIELD_NUMBER: _ClassVar[int]
    description: str
    detail: emots_detail
    unknown_emots_03: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_emots_04: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, description: _Optional[str] = ..., detail: _Optional[_Union[emots_detail, _Mapping]] = ..., unknown_emots_03: _Optional[_Iterable[bytes]] = ..., unknown_emots_04: _Optional[_Iterable[bytes]] = ...) -> None: ...

class emots_detail(_message.Message):
    __slots__ = ["emoticon_unique", "emots_url", "is_dynamic", "in_player_area", "bulge_display", "height", "width", "unknown_emots_detail_08"]
    EMOTICON_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    EMOTS_URL_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    IN_PLAYER_AREA_FIELD_NUMBER: _ClassVar[int]
    BULGE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EMOTS_DETAIL_08_FIELD_NUMBER: _ClassVar[int]
    emoticon_unique: str
    emots_url: str
    is_dynamic: int
    in_player_area: int
    bulge_display: int
    height: int
    width: int
    unknown_emots_detail_08: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, emoticon_unique: _Optional[str] = ..., emots_url: _Optional[str] = ..., is_dynamic: _Optional[int] = ..., in_player_area: _Optional[int] = ..., bulge_display: _Optional[int] = ..., height: _Optional[int] = ..., width: _Optional[int] = ..., unknown_emots_detail_08: _Optional[_Iterable[bytes]] = ...) -> None: ...

class lottery(_message.Message):
    __slots__ = ["unknown_lottery_01", "activity_source", "activity_identity", "not_show", "unknown_lottery_05", "unknown_lottery_06", "unknown_lottery_07", "unknown_lottery_08"]
    UNKNOWN_LOTTERY_01_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    NOT_SHOW_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_05_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_06_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_07_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LOTTERY_08_FIELD_NUMBER: _ClassVar[int]
    unknown_lottery_01: _containers.RepeatedScalarFieldContainer[bytes]
    activity_source: int
    activity_identity: str
    not_show: int
    unknown_lottery_05: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_lottery_06: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_lottery_07: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_lottery_08: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, unknown_lottery_01: _Optional[_Iterable[bytes]] = ..., activity_source: _Optional[int] = ..., activity_identity: _Optional[str] = ..., not_show: _Optional[int] = ..., unknown_lottery_05: _Optional[_Iterable[bytes]] = ..., unknown_lottery_06: _Optional[_Iterable[bytes]] = ..., unknown_lottery_07: _Optional[_Iterable[bytes]] = ..., unknown_lottery_08: _Optional[_Iterable[bytes]] = ...) -> None: ...

class validation(_message.Message):
    __slots__ = ["ct", "ts"]
    CT_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    ct: str
    ts: int
    def __init__(self, ct: _Optional[str] = ..., ts: _Optional[int] = ...) -> None: ...

class userinfo(_message.Message):
    __slots__ = ["uid", "username", "username_color", "face", "unknown_userinfo_05", "unknown_userinfo_06", "rank", "verify", "unknown_userinfo_09", "is_admin", "fan_medal", "live_user_info", "title", "unknown_userinfo_14", "unknown_userinfo_15", "unknown_userinfo_16"]
    UID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_COLOR_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_05_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_06_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    VERIFY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_09_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    FAN_MEDAL_FIELD_NUMBER: _ClassVar[int]
    LIVE_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_15_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_USERINFO_16_FIELD_NUMBER: _ClassVar[int]
    uid: int
    username: str
    username_color: str
    face: str
    unknown_userinfo_05: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_userinfo_06: _containers.RepeatedScalarFieldContainer[bytes]
    rank: int
    verify: int
    unknown_userinfo_09: _containers.RepeatedScalarFieldContainer[bytes]
    is_admin: int
    fan_medal: fan_medal
    live_user_info: live_user_info
    title: title
    unknown_userinfo_14: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_userinfo_15: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_userinfo_16: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, uid: _Optional[int] = ..., username: _Optional[str] = ..., username_color: _Optional[str] = ..., face: _Optional[str] = ..., unknown_userinfo_05: _Optional[_Iterable[bytes]] = ..., unknown_userinfo_06: _Optional[_Iterable[bytes]] = ..., rank: _Optional[int] = ..., verify: _Optional[int] = ..., unknown_userinfo_09: _Optional[_Iterable[bytes]] = ..., is_admin: _Optional[int] = ..., fan_medal: _Optional[_Union[fan_medal, _Mapping]] = ..., live_user_info: _Optional[_Union[live_user_info, _Mapping]] = ..., title: _Optional[_Union[title, _Mapping]] = ..., unknown_userinfo_14: _Optional[_Iterable[bytes]] = ..., unknown_userinfo_15: _Optional[_Iterable[bytes]] = ..., unknown_userinfo_16: _Optional[_Iterable[bytes]] = ...) -> None: ...

class fan_medal(_message.Message):
    __slots__ = ["medal_level", "medal_name", "unknown_fan_medal_03", "medal_color", "unknown_fan_medal_05", "medal_color_start", "medal_color_border", "medal_color_end", "anchor_guard_level", "is_lighted", "unknown_fan_medal_11", "unknown_fan_medal_12", "unknown_fan_medal_13", "unknown_fan_medal_14", "unknown_fan_medal_15", "unknown_fan_medal_16"]
    MEDAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MEDAL_NAME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_03_FIELD_NUMBER: _ClassVar[int]
    MEDAL_COLOR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_05_FIELD_NUMBER: _ClassVar[int]
    MEDAL_COLOR_START_FIELD_NUMBER: _ClassVar[int]
    MEDAL_COLOR_BORDER_FIELD_NUMBER: _ClassVar[int]
    MEDAL_COLOR_END_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_GUARD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_LIGHTED_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_13_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_15_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_16_FIELD_NUMBER: _ClassVar[int]
    medal_level: int
    medal_name: str
    unknown_fan_medal_03: _containers.RepeatedScalarFieldContainer[bytes]
    medal_color: int
    unknown_fan_medal_05: _containers.RepeatedScalarFieldContainer[bytes]
    medal_color_start: int
    medal_color_border: int
    medal_color_end: int
    anchor_guard_level: int
    is_lighted: int
    unknown_fan_medal_11: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_fan_medal_12: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_fan_medal_13: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_fan_medal_14: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_fan_medal_15: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_fan_medal_16: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, medal_level: _Optional[int] = ..., medal_name: _Optional[str] = ..., unknown_fan_medal_03: _Optional[_Iterable[bytes]] = ..., medal_color: _Optional[int] = ..., unknown_fan_medal_05: _Optional[_Iterable[bytes]] = ..., medal_color_start: _Optional[int] = ..., medal_color_border: _Optional[int] = ..., medal_color_end: _Optional[int] = ..., anchor_guard_level: _Optional[int] = ..., is_lighted: _Optional[int] = ..., unknown_fan_medal_11: _Optional[_Iterable[bytes]] = ..., unknown_fan_medal_12: _Optional[_Iterable[bytes]] = ..., unknown_fan_medal_13: _Optional[_Iterable[bytes]] = ..., unknown_fan_medal_14: _Optional[_Iterable[bytes]] = ..., unknown_fan_medal_15: _Optional[_Iterable[bytes]] = ..., unknown_fan_medal_16: _Optional[_Iterable[bytes]] = ...) -> None: ...

class live_user_info(_message.Message):
    __slots__ = ["User_Level", "UL_color", "live_rank", "unknown_live_user_info_04"]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UL_COLOR_FIELD_NUMBER: _ClassVar[int]
    LIVE_RANK_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LIVE_USER_INFO_04_FIELD_NUMBER: _ClassVar[int]
    User_Level: int
    UL_color: int
    live_rank: str
    unknown_live_user_info_04: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, User_Level: _Optional[int] = ..., UL_color: _Optional[int] = ..., live_rank: _Optional[str] = ..., unknown_live_user_info_04: _Optional[_Iterable[bytes]] = ...) -> None: ...

class title(_message.Message):
    __slots__ = ["title1", "title2", "unknown_title_03", "unknown_title_04"]
    TITLE1_FIELD_NUMBER: _ClassVar[int]
    TITLE2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TITLE_03_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TITLE_04_FIELD_NUMBER: _ClassVar[int]
    title1: str
    title2: str
    unknown_title_03: _containers.RepeatedScalarFieldContainer[bytes]
    unknown_title_04: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, title1: _Optional[str] = ..., title2: _Optional[str] = ..., unknown_title_03: _Optional[_Iterable[bytes]] = ..., unknown_title_04: _Optional[_Iterable[bytes]] = ...) -> None: ...

class fan_medal_ext(_message.Message):
    __slots__ = ["anchor_id", "anchor_username", "roomid", "unknown_fan_medal_ext_04"]
    ANCHOR_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FAN_MEDAL_EXT_04_FIELD_NUMBER: _ClassVar[int]
    anchor_id: int
    anchor_username: str
    roomid: int
    unknown_fan_medal_ext_04: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, anchor_id: _Optional[int] = ..., anchor_username: _Optional[str] = ..., roomid: _Optional[int] = ..., unknown_fan_medal_ext_04: _Optional[_Iterable[bytes]] = ...) -> None: ...
