from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ["id_str", "mode", "fontsize", "color", "mid_hash", "content", "ctime", "weight", "rnd", "attr", "biz_scene", "bubble", "dm_type", "emoticons", "voice", "animation", "aggregation", "send_from_me", "check", "user", "room"]
    class EmoticonsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Emoticon
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Emoticon, _Mapping]] = ...) -> None: ...
    ID_STR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MID_HASH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
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
    id_str: str
    mode: int
    fontsize: int
    color: int
    mid_hash: str
    content: str
    ctime: int
    weight: int
    rnd: int
    attr: int
    biz_scene: BizScene
    bubble: Bubble
    dm_type: DmType
    emoticons: _containers.MessageMap[str, Emoticon]
    voice: Voice
    animation: str
    aggregation: Aggregation
    send_from_me: bool
    check: Check
    user: User
    room: Room
    def __init__(self, id_str: _Optional[str] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., mid_hash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., weight: _Optional[int] = ..., rnd: _Optional[int] = ..., attr: _Optional[int] = ..., biz_scene: _Optional[_Union[BizScene, str]] = ..., bubble: _Optional[_Union[Bubble, _Mapping]] = ..., dm_type: _Optional[_Union[DmType, str]] = ..., emoticons: _Optional[_Mapping[str, Emoticon]] = ..., voice: _Optional[_Union[Voice, _Mapping]] = ..., animation: _Optional[str] = ..., aggregation: _Optional[_Union[Aggregation, _Mapping]] = ..., send_from_me: bool = ..., check: _Optional[_Union[Check, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ..., room: _Optional[_Union[Room, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["id", "color"]
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    color: str
    def __init__(self, id: _Optional[int] = ..., color: _Optional[str] = ...) -> None: ...

class emoticons(_message.Message):
    __slots__ = ["description", "detail"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    description: str
    detail: Emoticon
    def __init__(self, description: _Optional[str] = ..., detail: _Optional[_Union[Emoticon, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["uid", "name", "name_color", "face", "vip", "svip", "rank", "mobile_verify", "lpl_status", "attr", "medal", "level", "title", "identify"]
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
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., name_color: _Optional[str] = ..., face: _Optional[str] = ..., vip: _Optional[int] = ..., svip: _Optional[int] = ..., rank: _Optional[int] = ..., mobile_verify: _Optional[int] = ..., lpl_status: _Optional[int] = ..., attr: _Optional[int] = ..., medal: _Optional[_Union[Medal, _Mapping]] = ..., level: _Optional[_Union[UserLevel, _Mapping]] = ..., title: _Optional[_Union[Title, _Mapping]] = ..., identify: _Optional[_Union[Identify, _Mapping]] = ...) -> None: ...

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
