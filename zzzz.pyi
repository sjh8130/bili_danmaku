from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostPanelBizType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PostPanelBizTypeNone: _ClassVar[PostPanelBizType]
    PostPanelBizTypeEncourage: _ClassVar[PostPanelBizType]
    PostPanelBizTypeColorDM: _ClassVar[PostPanelBizType]
    PostPanelBizTypeNFTDM: _ClassVar[PostPanelBizType]
    PostPanelBizTypeFragClose: _ClassVar[PostPanelBizType]
    PostPanelBizTypeRecommend: _ClassVar[PostPanelBizType]

class RenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RenderTypeNone: _ClassVar[RenderType]
    RenderTypeSingle: _ClassVar[RenderType]
    RenderTypeRotation: _ClassVar[RenderType]

class AvatarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AvatarTypeNone: _ClassVar[AvatarType]
    AvatarTypeNFT: _ClassVar[AvatarType]

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PostStatusNormal: _ClassVar[PostStatus]
    PostStatusClosed: _ClassVar[PostStatus]

class BubbleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BubbleTypeNone: _ClassVar[BubbleType]
    BubbleTypeClickButton: _ClassVar[BubbleType]
    BubbleTypeDmSettingPanel: _ClassVar[BubbleType]

class CheckboxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CheckboxTypeNone: _ClassVar[CheckboxType]
    CheckboxTypeEncourage: _ClassVar[CheckboxType]
    CheckboxTypeColorDM: _ClassVar[CheckboxType]

class ToastFunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ToastFunctionTypeNone: _ClassVar[ToastFunctionType]
    ToastFunctionTypePostPanel: _ClassVar[ToastFunctionType]

class ToastBizType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ToastBizTypeNone: _ClassVar[ToastBizType]
    ToastBizTypeEncourage: _ClassVar[ToastBizType]

class ExposureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ExposureTypeNone: _ClassVar[ExposureType]
    ExposureTypeDMSend: _ClassVar[ExposureType]

class DmColorfulType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NoneType: _ClassVar[DmColorfulType]
    VipGradualColor: _ClassVar[DmColorfulType]
PostPanelBizTypeNone: PostPanelBizType
PostPanelBizTypeEncourage: PostPanelBizType
PostPanelBizTypeColorDM: PostPanelBizType
PostPanelBizTypeNFTDM: PostPanelBizType
PostPanelBizTypeFragClose: PostPanelBizType
PostPanelBizTypeRecommend: PostPanelBizType
RenderTypeNone: RenderType
RenderTypeSingle: RenderType
RenderTypeRotation: RenderType
AvatarTypeNone: AvatarType
AvatarTypeNFT: AvatarType
PostStatusNormal: PostStatus
PostStatusClosed: PostStatus
BubbleTypeNone: BubbleType
BubbleTypeClickButton: BubbleType
BubbleTypeDmSettingPanel: BubbleType
CheckboxTypeNone: CheckboxType
CheckboxTypeEncourage: CheckboxType
CheckboxTypeColorDM: CheckboxType
ToastFunctionTypeNone: ToastFunctionType
ToastFunctionTypePostPanel: ToastFunctionType
ToastBizTypeNone: ToastBizType
ToastBizTypeEncourage: ToastBizType
ExposureTypeNone: ExposureType
ExposureTypeDMSend: ExposureType
NoneType: DmColorfulType
VipGradualColor: DmColorfulType

class DmSegMobileReply(_message.Message):
    __slots__ = ["elems", "state", "ai_flag", "time", "colorful_src"]
    ELEMS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AI_FLAG_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    COLORFUL_SRC_FIELD_NUMBER: _ClassVar[int]
    elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
    state: int
    ai_flag: DanmakuAIFlag
    time: int
    colorful_src: _containers.RepeatedCompositeFieldContainer[DmColorful]
    def __init__(self, elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ..., state: _Optional[int] = ..., ai_flag: _Optional[_Union[DanmakuAIFlag, _Mapping]] = ..., time: _Optional[int] = ..., colorful_src: _Optional[_Iterable[_Union[DmColorful, _Mapping]]] = ...) -> None: ...

class DanmakuElem(_message.Message):
    __slots__ = ["id", "stime", "mode", "size", "color", "uhash", "text", "date", "weight", "action", "pool", "dmid", "attr", "usermid", "likes", "test16", "test17", "reply_count", "test19", "test20", "test21", "animation", "test23", "colorful", "test25", "test26", "test27", "test28", "test29", "test30", "test31"]
    ID_FIELD_NUMBER: _ClassVar[int]
    STIME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    UHASH_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    POOL_FIELD_NUMBER: _ClassVar[int]
    DMID_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    USERMID_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    TEST16_FIELD_NUMBER: _ClassVar[int]
    TEST17_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEST19_FIELD_NUMBER: _ClassVar[int]
    TEST20_FIELD_NUMBER: _ClassVar[int]
    TEST21_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_FIELD_NUMBER: _ClassVar[int]
    TEST23_FIELD_NUMBER: _ClassVar[int]
    COLORFUL_FIELD_NUMBER: _ClassVar[int]
    TEST25_FIELD_NUMBER: _ClassVar[int]
    TEST26_FIELD_NUMBER: _ClassVar[int]
    TEST27_FIELD_NUMBER: _ClassVar[int]
    TEST28_FIELD_NUMBER: _ClassVar[int]
    TEST29_FIELD_NUMBER: _ClassVar[int]
    TEST30_FIELD_NUMBER: _ClassVar[int]
    TEST31_FIELD_NUMBER: _ClassVar[int]
    id: int
    stime: int
    mode: int
    size: int
    color: int
    uhash: str
    text: str
    date: int
    weight: int
    action: str
    pool: int
    dmid: str
    attr: int
    usermid: int
    likes: int
    test16: int
    test17: int
    reply_count: int
    test19: bytes
    test20: str
    test21: str
    animation: str
    test23: bytes
    colorful: DmColorfulType
    test25: bytes
    test26: bytes
    test27: bytes
    test28: bytes
    test29: bytes
    test30: bytes
    test31: bytes
    def __init__(self, id: _Optional[int] = ..., stime: _Optional[int] = ..., mode: _Optional[int] = ..., size: _Optional[int] = ..., color: _Optional[int] = ..., uhash: _Optional[str] = ..., text: _Optional[str] = ..., date: _Optional[int] = ..., weight: _Optional[int] = ..., action: _Optional[str] = ..., pool: _Optional[int] = ..., dmid: _Optional[str] = ..., attr: _Optional[int] = ..., usermid: _Optional[int] = ..., likes: _Optional[int] = ..., test16: _Optional[int] = ..., test17: _Optional[int] = ..., reply_count: _Optional[int] = ..., test19: _Optional[bytes] = ..., test20: _Optional[str] = ..., test21: _Optional[str] = ..., animation: _Optional[str] = ..., test23: _Optional[bytes] = ..., colorful: _Optional[_Union[DmColorfulType, str]] = ..., test25: _Optional[bytes] = ..., test26: _Optional[bytes] = ..., test27: _Optional[bytes] = ..., test28: _Optional[bytes] = ..., test29: _Optional[bytes] = ..., test30: _Optional[bytes] = ..., test31: _Optional[bytes] = ...) -> None: ...

class DanmakuAIFlag(_message.Message):
    __slots__ = ["dm_flags"]
    DM_FLAGS_FIELD_NUMBER: _ClassVar[int]
    dm_flags: _containers.RepeatedCompositeFieldContainer[DanmakuFlag]
    def __init__(self, dm_flags: _Optional[_Iterable[_Union[DanmakuFlag, _Mapping]]] = ...) -> None: ...

class DanmakuFlag(_message.Message):
    __slots__ = ["dmid", "flag"]
    DMID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    dmid: int
    flag: int
    def __init__(self, dmid: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class DmWebViewReply(_message.Message):
    __slots__ = ["state", "text", "text_side", "dm_sge", "flag", "special_dms", "check_box", "count", "commandDms", "player_config", "report_filter_content", "expressions", "post_panel", "activity_meta", "post_panel_v2"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_SIDE_FIELD_NUMBER: _ClassVar[int]
    DM_SGE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_DMS_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDDMS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPORT_FILTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    POST_PANEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_META_FIELD_NUMBER: _ClassVar[int]
    POST_PANEL_V2_FIELD_NUMBER: _ClassVar[int]
    state: int
    text: str
    text_side: str
    dm_sge: DmSegConfig
    flag: DanmakuFlagConfig
    special_dms: _containers.RepeatedScalarFieldContainer[str]
    check_box: bool
    count: int
    commandDms: _containers.RepeatedCompositeFieldContainer[CommandDm]
    player_config: DanmuWebPlayerConfig
    report_filter_content: _containers.RepeatedScalarFieldContainer[str]
    expressions: _containers.RepeatedCompositeFieldContainer[Expressions]
    post_panel: _containers.RepeatedCompositeFieldContainer[PostPanel]
    activity_meta: _containers.RepeatedScalarFieldContainer[str]
    post_panel_v2: _containers.RepeatedCompositeFieldContainer[PostPanelV2]
    def __init__(self, state: _Optional[int] = ..., text: _Optional[str] = ..., text_side: _Optional[str] = ..., dm_sge: _Optional[_Union[DmSegConfig, _Mapping]] = ..., flag: _Optional[_Union[DanmakuFlagConfig, _Mapping]] = ..., special_dms: _Optional[_Iterable[str]] = ..., check_box: bool = ..., count: _Optional[int] = ..., commandDms: _Optional[_Iterable[_Union[CommandDm, _Mapping]]] = ..., player_config: _Optional[_Union[DanmuWebPlayerConfig, _Mapping]] = ..., report_filter_content: _Optional[_Iterable[str]] = ..., expressions: _Optional[_Iterable[_Union[Expressions, _Mapping]]] = ..., post_panel: _Optional[_Iterable[_Union[PostPanel, _Mapping]]] = ..., activity_meta: _Optional[_Iterable[str]] = ..., post_panel_v2: _Optional[_Iterable[_Union[PostPanelV2, _Mapping]]] = ...) -> None: ...

class DmSegConfig(_message.Message):
    __slots__ = ["page_size", "total"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    total: int
    def __init__(self, page_size: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class DanmakuFlagConfig(_message.Message):
    __slots__ = ["rec_flag", "rec_text", "rec_switch"]
    REC_FLAG_FIELD_NUMBER: _ClassVar[int]
    REC_TEXT_FIELD_NUMBER: _ClassVar[int]
    REC_SWITCH_FIELD_NUMBER: _ClassVar[int]
    rec_flag: int
    rec_text: str
    rec_switch: int
    def __init__(self, rec_flag: _Optional[int] = ..., rec_text: _Optional[str] = ..., rec_switch: _Optional[int] = ...) -> None: ...

class CommandDm(_message.Message):
    __slots__ = ["id", "oid", "mid", "command", "content", "stime", "ctime", "mtime", "extra", "dmid"]
    ID_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STIME_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    DMID_FIELD_NUMBER: _ClassVar[int]
    id: int
    oid: int
    mid: int
    command: str
    content: str
    stime: int
    ctime: str
    mtime: str
    extra: str
    dmid: str
    def __init__(self, id: _Optional[int] = ..., oid: _Optional[int] = ..., mid: _Optional[int] = ..., command: _Optional[str] = ..., content: _Optional[str] = ..., stime: _Optional[int] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., extra: _Optional[str] = ..., dmid: _Optional[str] = ...) -> None: ...

class DanmuWebPlayerConfig(_message.Message):
    __slots__ = ["dm_switch", "ai_switch", "ai_level", "type_top", "type_scroll", "type_bottom", "type_color", "type_special", "preventshade", "dmask", "opacity", "dmarea", "speedplus", "fontsize", "fullscreensync", "speedsync", "fontfamily", "bold", "fontborder", "draw_type", "senior_mode_switch", "ai_level_v2", "ai_level_v2_map"]
    class AiLevelV2MapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    DM_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_TOP_FIELD_NUMBER: _ClassVar[int]
    TYPE_SCROLL_FIELD_NUMBER: _ClassVar[int]
    TYPE_BOTTOM_FIELD_NUMBER: _ClassVar[int]
    TYPE_COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_SPECIAL_FIELD_NUMBER: _ClassVar[int]
    PREVENTSHADE_FIELD_NUMBER: _ClassVar[int]
    DMASK_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    DMAREA_FIELD_NUMBER: _ClassVar[int]
    SPEEDPLUS_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    FULLSCREENSYNC_FIELD_NUMBER: _ClassVar[int]
    SPEEDSYNC_FIELD_NUMBER: _ClassVar[int]
    FONTFAMILY_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    FONTBORDER_FIELD_NUMBER: _ClassVar[int]
    DRAW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
    AI_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
    dm_switch: bool
    ai_switch: bool
    ai_level: int
    type_top: bool
    type_scroll: bool
    type_bottom: bool
    type_color: bool
    type_special: bool
    preventshade: bool
    dmask: bool
    opacity: float
    dmarea: int
    speedplus: float
    fontsize: float
    fullscreensync: bool
    speedsync: bool
    fontfamily: str
    bold: bool
    fontborder: int
    draw_type: str
    senior_mode_switch: int
    ai_level_v2: int
    ai_level_v2_map: _containers.ScalarMap[int, int]
    def __init__(self, dm_switch: bool = ..., ai_switch: bool = ..., ai_level: _Optional[int] = ..., type_top: bool = ..., type_scroll: bool = ..., type_bottom: bool = ..., type_color: bool = ..., type_special: bool = ..., preventshade: bool = ..., dmask: bool = ..., opacity: _Optional[float] = ..., dmarea: _Optional[int] = ..., speedplus: _Optional[float] = ..., fontsize: _Optional[float] = ..., fullscreensync: bool = ..., speedsync: bool = ..., fontfamily: _Optional[str] = ..., bold: bool = ..., fontborder: _Optional[int] = ..., draw_type: _Optional[str] = ..., senior_mode_switch: _Optional[int] = ..., ai_level_v2: _Optional[int] = ..., ai_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class Expressions(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Expression]
    def __init__(self, data: _Optional[_Iterable[_Union[Expression, _Mapping]]] = ...) -> None: ...

class Expression(_message.Message):
    __slots__ = ["keyword", "url", "period"]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    keyword: _containers.RepeatedScalarFieldContainer[str]
    url: str
    period: _containers.RepeatedCompositeFieldContainer[Period]
    def __init__(self, keyword: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ..., period: _Optional[_Iterable[_Union[Period, _Mapping]]] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ["start", "end"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class PostPanel(_message.Message):
    __slots__ = ["start", "end", "priority", "biz_id", "biz_type", "click_button", "text_input", "check_box", "toast"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    TOAST_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    priority: int
    biz_id: int
    biz_type: PostPanelBizType
    click_button: ClickButton
    text_input: TextInput
    check_box: CheckBox
    toast: Toast
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., priority: _Optional[int] = ..., biz_id: _Optional[int] = ..., biz_type: _Optional[_Union[PostPanelBizType, str]] = ..., click_button: _Optional[_Union[ClickButton, _Mapping]] = ..., text_input: _Optional[_Union[TextInput, _Mapping]] = ..., check_box: _Optional[_Union[CheckBox, _Mapping]] = ..., toast: _Optional[_Union[Toast, _Mapping]] = ...) -> None: ...

class PostPanelV2(_message.Message):
    __slots__ = ["start", "end", "biz_type", "click_button", "text_input", "check_box", "toast", "bubble", "label", "post_status"]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
    TOAST_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    POST_STATUS_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    biz_type: PostPanelBizType
    click_button: ClickButtonV2
    text_input: TextInputV2
    check_box: CheckBoxV2
    toast: ToastV2
    bubble: BubbleV2
    label: LabelV2
    post_status: PostStatus
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., biz_type: _Optional[_Union[PostPanelBizType, str]] = ..., click_button: _Optional[_Union[ClickButtonV2, _Mapping]] = ..., text_input: _Optional[_Union[TextInputV2, _Mapping]] = ..., check_box: _Optional[_Union[CheckBoxV2, _Mapping]] = ..., toast: _Optional[_Union[ToastV2, _Mapping]] = ..., bubble: _Optional[_Union[BubbleV2, _Mapping]] = ..., label: _Optional[_Union[LabelV2, _Mapping]] = ..., post_status: _Optional[_Union[PostStatus, str]] = ...) -> None: ...

class ClickButton(_message.Message):
    __slots__ = ["portrait_text", "landscape_text", "portrait_text_focus", "landscape_text_focus", "render_type", "show", "bubble"]
    PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_FIELD_NUMBER: _ClassVar[int]
    portrait_text: _containers.RepeatedScalarFieldContainer[str]
    landscape_text: _containers.RepeatedScalarFieldContainer[str]
    portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
    landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    show: bool
    bubble: Bubble
    def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., show: bool = ..., bubble: _Optional[_Union[Bubble, _Mapping]] = ...) -> None: ...

class ClickButtonV2(_message.Message):
    __slots__ = ["portrait_text", "landscape_text", "portrait_text_focus", "landscape_text_focus", "render_type", "text_input_post", "exposure_once", "exposure_type"]
    PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_POST_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    portrait_text: _containers.RepeatedScalarFieldContainer[str]
    landscape_text: _containers.RepeatedScalarFieldContainer[str]
    portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
    landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    text_input_post: bool
    exposure_once: Bubble
    exposure_type: ExposureType
    def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., text_input_post: bool = ..., exposure_once: _Optional[_Union[Bubble, _Mapping]] = ..., exposure_type: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class TextInput(_message.Message):
    __slots__ = ["portrait_placeholder", "landscape_placeholder", "render_type", "placeholder_post", "show", "avatar", "post_status", "label"]
    PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    POST_STATUS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
    landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    placeholder_post: bool
    show: bool
    avatar: _containers.RepeatedCompositeFieldContainer[Avatar]
    post_status: PostStatus
    label: Label
    def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., show: bool = ..., avatar: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ..., post_status: _Optional[_Union[PostStatus, str]] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class TextInputV2(_message.Message):
    __slots__ = ["portrait_placeholder", "landscape_placeholder", "render_type", "placeholder_post", "text_input_limit"]
    PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
    landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
    render_type: RenderType
    placeholder_post: bool
    text_input_limit: int
    def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., text_input_limit: _Optional[int] = ...) -> None: ...

class Avatar(_message.Message):
    __slots__ = ["id", "url", "avatar_type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    avatar_type: AvatarType
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., avatar_type: _Optional[_Union[AvatarType, str]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ["title", "content"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ...) -> None: ...

class LabelV2(_message.Message):
    __slots__ = ["title", "content", "exposure_once", "exposure_type"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: _containers.RepeatedScalarFieldContainer[str]
    exposure_once: bool
    exposure_type: ExposureType
    def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class Bubble(_message.Message):
    __slots__ = ["text", "url"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    text: str
    url: str
    def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class BubbleV2(_message.Message):
    __slots__ = ["text", "url", "bubble_type", "exposure_once", "exposure_type"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    url: str
    bubble_type: BubbleType
    exposure_once: bool
    exposure_type: ExposureType
    def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ..., bubble_type: _Optional[_Union[BubbleType, str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class CheckBox(_message.Message):
    __slots__ = ["text", "type", "default_value", "show"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: CheckboxType
    default_value: bool
    show: bool
    def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[CheckboxType, str]] = ..., default_value: bool = ..., show: bool = ...) -> None: ...

class CheckBoxV2(_message.Message):
    __slots__ = ["text", "type", "default_value"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: CheckboxType
    default_value: bool
    def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[CheckboxType, str]] = ..., default_value: bool = ...) -> None: ...

class Toast(_message.Message):
    __slots__ = ["text", "duration", "show", "button"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration: int
    show: bool
    button: Button
    def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., show: bool = ..., button: _Optional[_Union[Button, _Mapping]] = ...) -> None: ...

class ToastV2(_message.Message):
    __slots__ = ["text", "duration", "toast_button_v2"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TOAST_BUTTON_V2_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration: int
    toast_button_v2: ToastButtonV2
    def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., toast_button_v2: _Optional[_Union[ToastButtonV2, _Mapping]] = ...) -> None: ...

class ToastButtonV2(_message.Message):
    __slots__ = ["text", "action"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    text: str
    action: ToastFunctionType
    def __init__(self, text: _Optional[str] = ..., action: _Optional[_Union[ToastFunctionType, str]] = ...) -> None: ...

class Button(_message.Message):
    __slots__ = ["text", "action"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    text: str
    action: int
    def __init__(self, text: _Optional[str] = ..., action: _Optional[int] = ...) -> None: ...

class AnyBody(_message.Message):
    __slots__ = ["body"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: typeAnyBody
    def __init__(self, body: _Optional[_Union[typeAnyBody, _Mapping]] = ...) -> None: ...

class DmColorful(_message.Message):
    __slots__ = ["type", "src"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    type: DmColorfulType
    src: str
    def __init__(self, type: _Optional[_Union[DmColorfulType, str]] = ..., src: _Optional[str] = ...) -> None: ...

class typeAnyBody(_message.Message):
    __slots__ = ["type_url", "value"]
    TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type_url: str
    value: bytes
    def __init__(self, type_url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
