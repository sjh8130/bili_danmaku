from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BizScene(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BizSceneNone: _ClassVar[BizScene]
    BizSceneLottery: _ClassVar[BizScene]
    BizSceneSurvive: _ClassVar[BizScene]
    BizSceneVoiceConn: _ClassVar[BizScene]
    BizScenePlayBack: _ClassVar[BizScene]
    BizSceneVote: _ClassVar[BizScene]

class DmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DmTypeNormal: _ClassVar[DmType]
    DmTypeEmoticon: _ClassVar[DmType]
    DmTypeVoice: _ClassVar[DmType]
BizSceneNone: BizScene
BizSceneLottery: BizScene
BizSceneSurvive: BizScene
BizSceneVoiceConn: BizScene
BizScenePlayBack: BizScene
BizSceneVote: BizScene
DmTypeNormal: DmType
DmTypeEmoticon: DmType
DmTypeVoice: DmType

class Dm(_message.Message):
    __slots__ = ["dmid", "mode", "size", "color", "uhash", "text", "date", "weight", "rnd", "attr", "biz_scene", "bubble", "dm_type", "emoticons", "voice", "animation", "aggregation", "send_from_me", "check", "user", "room", "icon", "reply", "unknown24", "unknown25", "unknown26", "unknown27", "unknown28", "unknown29", "unknown30", "unknown31", "unknown32"]
    DMID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    UHASH_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RND_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    BIZ_SCENE_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_FIELD_NUMBER: _ClassVar[int]
    DM_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMOTICONS_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    SEND_FROM_ME_FIELD_NUMBER: _ClassVar[int]
    CHECK_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN24_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN25_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN27_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN29_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN30_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN32_FIELD_NUMBER: _ClassVar[int]
    dmid: str
    mode: int
    size: int
    color: int
    uhash: str
    text: str
    date: int
    weight: int
    rnd: int
    attr: int
    biz_scene: BizScene
    bubble: Bubble
    dm_type: DmType
    emoticons: _containers.RepeatedCompositeFieldContainer[emots]
    voice: Voice
    animation: str
    aggregation: Aggregation
    send_from_me: bool
    check: Check
    user: User
    room: Room
    icon: Icon
    reply: Reply
    unknown24: bytes
    unknown25: bytes
    unknown26: bytes
    unknown27: bytes
    unknown28: bytes
    unknown29: bytes
    unknown30: bytes
    unknown31: bytes
    unknown32: bytes
    def __init__(self, dmid: _Optional[str] = ..., mode: _Optional[int] = ..., size: _Optional[int] = ..., color: _Optional[int] = ..., uhash: _Optional[str] = ..., text: _Optional[str] = ..., date: _Optional[int] = ..., weight: _Optional[int] = ..., rnd: _Optional[int] = ..., attr: _Optional[int] = ..., biz_scene: _Optional[_Union[BizScene, str]] = ..., bubble: _Optional[_Union[Bubble, _Mapping]] = ..., dm_type: _Optional[_Union[DmType, str]] = ..., emoticons: _Optional[_Iterable[_Union[emots, _Mapping]]] = ..., voice: _Optional[_Union[Voice, _Mapping]] = ..., animation: _Optional[str] = ..., aggregation: _Optional[_Union[Aggregation, _Mapping]] = ..., send_from_me: bool = ..., check: _Optional[_Union[Check, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ..., room: _Optional[_Union[Room, _Mapping]] = ..., icon: _Optional[_Union[Icon, _Mapping]] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ..., unknown24: _Optional[bytes] = ..., unknown25: _Optional[bytes] = ..., unknown26: _Optional[bytes] = ..., unknown27: _Optional[bytes] = ..., unknown28: _Optional[bytes] = ..., unknown29: _Optional[bytes] = ..., unknown30: _Optional[bytes] = ..., unknown31: _Optional[bytes] = ..., unknown32: _Optional[bytes] = ...) -> None: ...

class Check(_message.Message):
    __slots__ = ["token", "ts"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    token: str
    ts: int
    def __init__(self, token: _Optional[str] = ..., ts: _Optional[int] = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ["uid", "name", "roomid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    roomid: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., roomid: _Optional[int] = ...) -> None: ...

class Bubble(_message.Message):
    __slots__ = ["id", "color", "id_v2"]
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ID_V2_FIELD_NUMBER: _ClassVar[int]
    id: int
    color: str
    id_v2: int
    def __init__(self, id: _Optional[int] = ..., color: _Optional[str] = ..., id_v2: _Optional[int] = ...) -> None: ...

class emots(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: Emoticon
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Emoticon, _Mapping]] = ...) -> None: ...

class Emoticon(_message.Message):
    __slots__ = ["unique", "url", "is_dynamic", "in_player_area", "bulge_display", "height", "width"]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    IN_PLAYER_AREA_FIELD_NUMBER: _ClassVar[int]
    BULGE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    unique: str
    url: str
    is_dynamic: bool
    in_player_area: int
    bulge_display: int
    height: int
    width: int
    def __init__(self, unique: _Optional[str] = ..., url: _Optional[str] = ..., is_dynamic: bool = ..., in_player_area: _Optional[int] = ..., bulge_display: _Optional[int] = ..., height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class Voice(_message.Message):
    __slots__ = ["url", "file_format", "text", "file_duration", "file_id"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_DURATION_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    file_format: str
    text: str
    file_duration: int
    file_id: str
    def __init__(self, url: _Optional[str] = ..., file_format: _Optional[str] = ..., text: _Optional[str] = ..., file_duration: _Optional[int] = ..., file_id: _Optional[str] = ...) -> None: ...

class Aggregation(_message.Message):
    __slots__ = ["is_aggregation", "activity_source", "activity_identity", "not_show"]
    IS_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    NOT_SHOW_FIELD_NUMBER: _ClassVar[int]
    is_aggregation: bool
    activity_source: int
    activity_identity: str
    not_show: int
    def __init__(self, is_aggregation: bool = ..., activity_source: _Optional[int] = ..., activity_identity: _Optional[str] = ..., not_show: _Optional[int] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["uid", "name", "name_color", "face", "vip", "svip", "rank", "mobile_verify", "lpl_status", "attr", "medal", "level", "title", "identify", "wealth"]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_COLOR_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    VIP_FIELD_NUMBER: _ClassVar[int]
    SVIP_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    MOBILE_VERIFY_FIELD_NUMBER: _ClassVar[int]
    LPL_STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_FIELD_NUMBER: _ClassVar[int]
    WEALTH_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    name_color: str
    face: str
    vip: int
    svip: int
    rank: int
    mobile_verify: int
    lpl_status: int
    attr: int
    medal: Medal
    level: UserLevel
    title: Title
    identify: Identify
    wealth: Wealth
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., name_color: _Optional[str] = ..., face: _Optional[str] = ..., vip: _Optional[int] = ..., svip: _Optional[int] = ..., rank: _Optional[int] = ..., mobile_verify: _Optional[int] = ..., lpl_status: _Optional[int] = ..., attr: _Optional[int] = ..., medal: _Optional[_Union[Medal, _Mapping]] = ..., level: _Optional[_Union[UserLevel, _Mapping]] = ..., title: _Optional[_Union[Title, _Mapping]] = ..., identify: _Optional[_Union[Identify, _Mapping]] = ..., wealth: _Optional[_Union[Wealth, _Mapping]] = ...) -> None: ...

class Identify(_message.Message):
    __slots__ = ["beginning_url", "ending_url", "jump_to_url"]
    BEGINNING_URL_FIELD_NUMBER: _ClassVar[int]
    ENDING_URL_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_URL_FIELD_NUMBER: _ClassVar[int]
    beginning_url: str
    ending_url: str
    jump_to_url: str
    def __init__(self, beginning_url: _Optional[str] = ..., ending_url: _Optional[str] = ..., jump_to_url: _Optional[str] = ...) -> None: ...

class Medal(_message.Message):
    __slots__ = ["level", "name", "special", "color", "icon_id", "border_color", "gradient_start_color", "gradient_end_color", "privilege", "light"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ICON_ID_FIELD_NUMBER: _ClassVar[int]
    BORDER_COLOR_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_START_COLOR_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_END_COLOR_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_FIELD_NUMBER: _ClassVar[int]
    level: int
    name: str
    special: str
    color: int
    icon_id: int
    border_color: int
    gradient_start_color: int
    gradient_end_color: int
    privilege: int
    light: int
    def __init__(self, level: _Optional[int] = ..., name: _Optional[str] = ..., special: _Optional[str] = ..., color: _Optional[int] = ..., icon_id: _Optional[int] = ..., border_color: _Optional[int] = ..., gradient_start_color: _Optional[int] = ..., gradient_end_color: _Optional[int] = ..., privilege: _Optional[int] = ..., light: _Optional[int] = ...) -> None: ...

class UserLevel(_message.Message):
    __slots__ = ["level", "color", "rank", "online_rank"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    ONLINE_RANK_FIELD_NUMBER: _ClassVar[int]
    level: int
    color: int
    rank: str
    online_rank: int
    def __init__(self, level: _Optional[int] = ..., color: _Optional[int] = ..., rank: _Optional[str] = ..., online_rank: _Optional[int] = ...) -> None: ...

class Title(_message.Message):
    __slots__ = ["title1", "old_title"]
    TITLE1_FIELD_NUMBER: _ClassVar[int]
    OLD_TITLE_FIELD_NUMBER: _ClassVar[int]
    title1: str
    old_title: str
    def __init__(self, title1: _Optional[str] = ..., old_title: _Optional[str] = ...) -> None: ...

class Record(_message.Message):
    __slots__ = ["dmid", "time_offset"]
    DMID_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    dmid: str
    time_offset: int
    def __init__(self, dmid: _Optional[str] = ..., time_offset: _Optional[int] = ...) -> None: ...

class Wealth(_message.Message):
    __slots__ = ["level"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: int
    def __init__(self, level: _Optional[int] = ...) -> None: ...

class Icon(_message.Message):
    __slots__ = ["prefix"]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    prefix: Prefix
    def __init__(self, prefix: _Optional[_Union[Prefix, _Mapping]] = ...) -> None: ...

class Prefix(_message.Message):
    __slots__ = ["type", "resource"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    type: int
    resource: str
    def __init__(self, type: _Optional[int] = ..., resource: _Optional[str] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["show_reply", "reply_mid", "reply_uname", "reply_uname_color"]
    SHOW_REPLY_FIELD_NUMBER: _ClassVar[int]
    REPLY_MID_FIELD_NUMBER: _ClassVar[int]
    REPLY_UNAME_FIELD_NUMBER: _ClassVar[int]
    REPLY_UNAME_COLOR_FIELD_NUMBER: _ClassVar[int]
    show_reply: bool
    reply_mid: int
    reply_uname: str
    reply_uname_color: str
    def __init__(self, show_reply: bool = ..., reply_mid: _Optional[int] = ..., reply_uname: _Optional[str] = ..., reply_uname_color: _Optional[str] = ...) -> None: ...
