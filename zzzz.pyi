from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AI: SubtitleType
Assist: SubtitleAiStatus
AvatarTypeNFT: AvatarType
AvatarTypeNone: AvatarType
BubbleTypeClickButton: BubbleType
BubbleTypeDmSettingPanel: BubbleType
BubbleTypeNone: BubbleType
CC: SubtitleType
CheckboxTypeColorDM: CheckboxType
CheckboxTypeEncourage: CheckboxType
CheckboxTypeNone: CheckboxType
DESCRIPTOR: _descriptor.FileDescriptor
DMAttrBitFromLive: DMAttrBit
DMAttrBitProtect: DMAttrBit
DMAttrHighLike: DMAttrBit
Exposure: SubtitleAiStatus
ExposureTypeDMSend: ExposureType
ExposureTypeNone: ExposureType
None: SubtitleAiStatus
Normal: SubtitleAiType
PostPanelBizTypeColorDM: PostPanelBizType
PostPanelBizTypeEncourage: PostPanelBizType
PostPanelBizTypeFragClose: PostPanelBizType
PostPanelBizTypeNFTDM: PostPanelBizType
PostPanelBizTypeNone: PostPanelBizType
PostPanelBizTypeRecommend: PostPanelBizType
PostStatusClosed: PostStatus
PostStatusNormal: PostStatus
RenderTypeNone: RenderType
RenderTypeRotation: RenderType
RenderTypeSingle: RenderType
ToastFunctionTypeNone: ToastFunctionType
ToastFunctionTypePostPanel: ToastFunctionType
Translate: SubtitleAiType

class Avatar(_message.Message):
	__slots__ = ["avatar_type", "id", "url"]
	AVATAR_TYPE_FIELD_NUMBER: _ClassVar[int]
	ID_FIELD_NUMBER: _ClassVar[int]
	URL_FIELD_NUMBER: _ClassVar[int]
	avatar_type: AvatarType
	id: str
	url: str
	def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., avatar_type: _Optional[_Union[AvatarType, str]] = ...) -> None: ...

class Bubble(_message.Message):
	__slots__ = ["text", "url"]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	URL_FIELD_NUMBER: _ClassVar[int]
	text: str
	url: str
	def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class BubbleV2(_message.Message):
	__slots__ = ["bubble_type", "exposure_once", "exposure_type", "text", "url"]
	BUBBLE_TYPE_FIELD_NUMBER: _ClassVar[int]
	EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
	EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	URL_FIELD_NUMBER: _ClassVar[int]
	bubble_type: BubbleType
	exposure_once: bool
	exposure_type: ExposureType
	text: str
	url: str
	def __init__(self, text: _Optional[str] = ..., url: _Optional[str] = ..., bubble_type: _Optional[_Union[BubbleType, str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[_Union[ExposureType, str]] = ...) -> None: ...

class Button(_message.Message):
	__slots__ = ["action", "text"]
	ACTION_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	action: int
	text: str
	def __init__(self, text: _Optional[str] = ..., action: _Optional[int] = ...) -> None: ...

class BuzzwordConfig(_message.Message):
	__slots__ = ["keywords"]
	KEYWORDS_FIELD_NUMBER: _ClassVar[int]
	keywords: _containers.RepeatedCompositeFieldContainer[BuzzwordShowConfig]
	def __init__(self, keywords: _Optional[_Iterable[_Union[BuzzwordShowConfig, _Mapping]]] = ...) -> None: ...

class BuzzwordShowConfig(_message.Message):
	__slots__ = ["buzzword_id", "id", "name", "schema", "schema_type", "source"]
	BUZZWORD_ID_FIELD_NUMBER: _ClassVar[int]
	ID_FIELD_NUMBER: _ClassVar[int]
	NAME_FIELD_NUMBER: _ClassVar[int]
	SCHEMA_FIELD_NUMBER: _ClassVar[int]
	SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
	SOURCE_FIELD_NUMBER: _ClassVar[int]
	buzzword_id: int
	id: int
	name: str
	schema: str
	schema_type: int
	source: int
	def __init__(self, name: _Optional[str] = ..., schema: _Optional[str] = ..., source: _Optional[int] = ..., id: _Optional[int] = ..., buzzword_id: _Optional[int] = ..., schema_type: _Optional[int] = ...) -> None: ...

class CheckBox(_message.Message):
	__slots__ = ["default_value", "show", "text", "type"]
	DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
	SHOW_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	default_value: bool
	show: bool
	text: str
	type: CheckboxType
	def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[CheckboxType, str]] = ..., default_value: bool = ..., show: bool = ...) -> None: ...

class CheckBoxV2(_message.Message):
	__slots__ = ["default_value", "text", "type"]
	DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	default_value: bool
	text: str
	type: int
	def __init__(self, text: _Optional[str] = ..., type: _Optional[int] = ..., default_value: bool = ...) -> None: ...

class ClickButton(_message.Message):
	__slots__ = ["bubble", "landscape_text", "landscape_text_focus", "portrait_text", "portrait_text_focus", "render_type", "show"]
	BUBBLE_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
	RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
	SHOW_FIELD_NUMBER: _ClassVar[int]
	bubble: Bubble
	landscape_text: _containers.RepeatedScalarFieldContainer[str]
	landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
	portrait_text: _containers.RepeatedScalarFieldContainer[str]
	portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
	render_type: RenderType
	show: bool
	def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., show: bool = ..., bubble: _Optional[_Union[Bubble, _Mapping]] = ...) -> None: ...

class ClickButtonV2(_message.Message):
	__slots__ = ["exposure_once", "exposure_type", "landscape_text", "landscape_text_focus", "portrait_text", "portrait_text_focus", "render_type", "text_input_post"]
	EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
	EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_TEXT_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_TEXT_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_TEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
	RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
	TEXT_INPUT_POST_FIELD_NUMBER: _ClassVar[int]
	exposure_once: bool
	exposure_type: int
	landscape_text: _containers.RepeatedScalarFieldContainer[str]
	landscape_text_focus: _containers.RepeatedScalarFieldContainer[str]
	portrait_text: _containers.RepeatedScalarFieldContainer[str]
	portrait_text_focus: _containers.RepeatedScalarFieldContainer[str]
	render_type: int
	text_input_post: bool
	def __init__(self, portrait_text: _Optional[_Iterable[str]] = ..., landscape_text: _Optional[_Iterable[str]] = ..., portrait_text_focus: _Optional[_Iterable[str]] = ..., landscape_text_focus: _Optional[_Iterable[str]] = ..., render_type: _Optional[int] = ..., text_input_post: bool = ..., exposure_once: bool = ..., exposure_type: _Optional[int] = ...) -> None: ...

class CommandDm(_message.Message):
	__slots__ = ["command", "content", "ctime", "extra", "id", "idStr", "mid", "mtime", "oid", "progress"]
	COMMAND_FIELD_NUMBER: _ClassVar[int]
	CONTENT_FIELD_NUMBER: _ClassVar[int]
	CTIME_FIELD_NUMBER: _ClassVar[int]
	EXTRA_FIELD_NUMBER: _ClassVar[int]
	IDSTR_FIELD_NUMBER: _ClassVar[int]
	ID_FIELD_NUMBER: _ClassVar[int]
	MID_FIELD_NUMBER: _ClassVar[int]
	MTIME_FIELD_NUMBER: _ClassVar[int]
	OID_FIELD_NUMBER: _ClassVar[int]
	PROGRESS_FIELD_NUMBER: _ClassVar[int]
	command: str
	content: str
	ctime: str
	extra: str
	id: int
	idStr: str
	mid: int
	mtime: str
	oid: int
	progress: int
	def __init__(self, id: _Optional[int] = ..., oid: _Optional[int] = ..., mid: _Optional[int] = ..., command: _Optional[str] = ..., content: _Optional[str] = ..., progress: _Optional[int] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., extra: _Optional[str] = ..., idStr: _Optional[str] = ...) -> None: ...

class DanmakuAIFlag(_message.Message):
	__slots__ = ["dm_flags"]
	DM_FLAGS_FIELD_NUMBER: _ClassVar[int]
	dm_flags: _containers.RepeatedCompositeFieldContainer[DanmakuFlag]
	def __init__(self, dm_flags: _Optional[_Iterable[_Union[DanmakuFlag, _Mapping]]] = ...) -> None: ...

class DanmakuElem(_message.Message):
	__slots__ = ["action", "animation", "attr", "color", "content", "ctime", "fontsize", "id", "idStr", "likes", "midHash", "mode", "pool", "progress", "reply_count", "test16", "test17", "test19", "test20", "test21", "test23", "usermid", "weight"]
	ACTION_FIELD_NUMBER: _ClassVar[int]
	ANIMATION_FIELD_NUMBER: _ClassVar[int]
	ATTR_FIELD_NUMBER: _ClassVar[int]
	COLOR_FIELD_NUMBER: _ClassVar[int]
	CONTENT_FIELD_NUMBER: _ClassVar[int]
	CTIME_FIELD_NUMBER: _ClassVar[int]
	FONTSIZE_FIELD_NUMBER: _ClassVar[int]
	IDSTR_FIELD_NUMBER: _ClassVar[int]
	ID_FIELD_NUMBER: _ClassVar[int]
	LIKES_FIELD_NUMBER: _ClassVar[int]
	MIDHASH_FIELD_NUMBER: _ClassVar[int]
	MODE_FIELD_NUMBER: _ClassVar[int]
	POOL_FIELD_NUMBER: _ClassVar[int]
	PROGRESS_FIELD_NUMBER: _ClassVar[int]
	REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
	TEST16_FIELD_NUMBER: _ClassVar[int]
	TEST17_FIELD_NUMBER: _ClassVar[int]
	TEST19_FIELD_NUMBER: _ClassVar[int]
	TEST20_FIELD_NUMBER: _ClassVar[int]
	TEST21_FIELD_NUMBER: _ClassVar[int]
	TEST23_FIELD_NUMBER: _ClassVar[int]
	USERMID_FIELD_NUMBER: _ClassVar[int]
	WEIGHT_FIELD_NUMBER: _ClassVar[int]
	action: str
	animation: str
	attr: int
	color: int
	content: str
	ctime: int
	fontsize: int
	id: int
	idStr: str
	likes: int
	midHash: str
	mode: int
	pool: int
	progress: int
	reply_count: int
	test16: int
	test17: int
	test19: bytes
	test20: str
	test21: str
	test23: bytes
	usermid: int
	weight: int
	def __init__(self, id: _Optional[int] = ..., progress: _Optional[int] = ..., mode: _Optional[int] = ..., fontsize: _Optional[int] = ..., color: _Optional[int] = ..., midHash: _Optional[str] = ..., content: _Optional[str] = ..., ctime: _Optional[int] = ..., weight: _Optional[int] = ..., action: _Optional[str] = ..., pool: _Optional[int] = ..., idStr: _Optional[str] = ..., attr: _Optional[int] = ..., usermid: _Optional[int] = ..., likes: _Optional[int] = ..., test16: _Optional[int] = ..., test17: _Optional[int] = ..., reply_count: _Optional[int] = ..., test19: _Optional[bytes] = ..., test20: _Optional[str] = ..., test21: _Optional[str] = ..., animation: _Optional[str] = ..., test23: _Optional[bytes] = ...) -> None: ...

class DanmakuFlag(_message.Message):
	__slots__ = ["dmid", "flag"]
	DMID_FIELD_NUMBER: _ClassVar[int]
	FLAG_FIELD_NUMBER: _ClassVar[int]
	dmid: int
	flag: int
	def __init__(self, dmid: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class DanmakuFlagConfig(_message.Message):
	__slots__ = ["rec_flag", "rec_switch", "rec_text"]
	REC_FLAG_FIELD_NUMBER: _ClassVar[int]
	REC_SWITCH_FIELD_NUMBER: _ClassVar[int]
	REC_TEXT_FIELD_NUMBER: _ClassVar[int]
	rec_flag: int
	rec_switch: int
	rec_text: str
	def __init__(self, rec_flag: _Optional[int] = ..., rec_text: _Optional[str] = ..., rec_switch: _Optional[int] = ...) -> None: ...

class DanmuDefaultPlayerConfig(_message.Message):
	__slots__ = ["inline_player_danmaku_switch", "player_danmaku_ai_recommended_level", "player_danmaku_ai_recommended_level_v2", "player_danmaku_ai_recommended_level_v2_map", "player_danmaku_ai_recommended_switch", "player_danmaku_blockbottom", "player_danmaku_blockcolorful", "player_danmaku_blockrepeat", "player_danmaku_blockscroll", "player_danmaku_blockspecial", "player_danmaku_blocktop", "player_danmaku_domain", "player_danmaku_opacity", "player_danmaku_scalingfactor", "player_danmaku_senior_mode_switch", "player_danmaku_speed", "player_danmaku_use_default_config"]
	class PlayerDanmakuAiRecommendedLevelV2MapEntry(_message.Message):
		__slots__ = ["key", "value"]
		KEY_FIELD_NUMBER: _ClassVar[int]
		VALUE_FIELD_NUMBER: _ClassVar[int]
		key: int
		value: int
		def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
	INLINE_PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_OPACITY_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SPEED_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
	inline_player_danmaku_switch: bool
	player_danmaku_ai_recommended_level: int
	player_danmaku_ai_recommended_level_v2: int
	player_danmaku_ai_recommended_level_v2_map: _containers.ScalarMap[int, int]
	player_danmaku_ai_recommended_switch: bool
	player_danmaku_blockbottom: bool
	player_danmaku_blockcolorful: bool
	player_danmaku_blockrepeat: bool
	player_danmaku_blockscroll: bool
	player_danmaku_blockspecial: bool
	player_danmaku_blocktop: bool
	player_danmaku_domain: float
	player_danmaku_opacity: float
	player_danmaku_scalingfactor: float
	player_danmaku_senior_mode_switch: int
	player_danmaku_speed: int
	player_danmaku_use_default_config: bool
	def __init__(self, player_danmaku_use_default_config: bool = ..., player_danmaku_ai_recommended_switch: bool = ..., player_danmaku_ai_recommended_level: _Optional[int] = ..., player_danmaku_blocktop: bool = ..., player_danmaku_blockscroll: bool = ..., player_danmaku_blockbottom: bool = ..., player_danmaku_blockcolorful: bool = ..., player_danmaku_blockrepeat: bool = ..., player_danmaku_blockspecial: bool = ..., player_danmaku_opacity: _Optional[float] = ..., player_danmaku_scalingfactor: _Optional[float] = ..., player_danmaku_domain: _Optional[float] = ..., player_danmaku_speed: _Optional[int] = ..., inline_player_danmaku_switch: bool = ..., player_danmaku_senior_mode_switch: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DanmuPlayerConfig(_message.Message):
	__slots__ = ["inline_player_danmaku_config", "inline_player_danmaku_switch", "player_danmaku_ai_recommended_level", "player_danmaku_ai_recommended_level_v2", "player_danmaku_ai_recommended_level_v2_map", "player_danmaku_ai_recommended_switch", "player_danmaku_blockbottom", "player_danmaku_blockcolorful", "player_danmaku_blockrepeat", "player_danmaku_blockscroll", "player_danmaku_blockspecial", "player_danmaku_blocktop", "player_danmaku_domain", "player_danmaku_enableblocklist", "player_danmaku_ios_switch_save", "player_danmaku_opacity", "player_danmaku_scalingfactor", "player_danmaku_senior_mode_switch", "player_danmaku_speed", "player_danmaku_switch", "player_danmaku_switch_save", "player_danmaku_use_default_config"]
	class PlayerDanmakuAiRecommendedLevelV2MapEntry(_message.Message):
		__slots__ = ["key", "value"]
		KEY_FIELD_NUMBER: _ClassVar[int]
		VALUE_FIELD_NUMBER: _ClassVar[int]
		key: int
		value: int
		def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
	INLINE_PLAYER_DANMAKU_CONFIG_FIELD_NUMBER: _ClassVar[int]
	INLINE_PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_ENABLEBLOCKLIST_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_IOS_SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_OPACITY_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SPEED_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SWITCH_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
	PLAYER_DANMAKU_USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
	inline_player_danmaku_config: int
	inline_player_danmaku_switch: bool
	player_danmaku_ai_recommended_level: int
	player_danmaku_ai_recommended_level_v2: int
	player_danmaku_ai_recommended_level_v2_map: _containers.ScalarMap[int, int]
	player_danmaku_ai_recommended_switch: bool
	player_danmaku_blockbottom: bool
	player_danmaku_blockcolorful: bool
	player_danmaku_blockrepeat: bool
	player_danmaku_blockscroll: bool
	player_danmaku_blockspecial: bool
	player_danmaku_blocktop: bool
	player_danmaku_domain: float
	player_danmaku_enableblocklist: bool
	player_danmaku_ios_switch_save: int
	player_danmaku_opacity: float
	player_danmaku_scalingfactor: float
	player_danmaku_senior_mode_switch: int
	player_danmaku_speed: int
	player_danmaku_switch: bool
	player_danmaku_switch_save: bool
	player_danmaku_use_default_config: bool
	def __init__(self, player_danmaku_switch: bool = ..., player_danmaku_switch_save: bool = ..., player_danmaku_use_default_config: bool = ..., player_danmaku_ai_recommended_switch: bool = ..., player_danmaku_ai_recommended_level: _Optional[int] = ..., player_danmaku_blocktop: bool = ..., player_danmaku_blockscroll: bool = ..., player_danmaku_blockbottom: bool = ..., player_danmaku_blockcolorful: bool = ..., player_danmaku_blockrepeat: bool = ..., player_danmaku_blockspecial: bool = ..., player_danmaku_opacity: _Optional[float] = ..., player_danmaku_scalingfactor: _Optional[float] = ..., player_danmaku_domain: _Optional[float] = ..., player_danmaku_speed: _Optional[int] = ..., player_danmaku_enableblocklist: bool = ..., inline_player_danmaku_switch: bool = ..., inline_player_danmaku_config: _Optional[int] = ..., player_danmaku_ios_switch_save: _Optional[int] = ..., player_danmaku_senior_mode_switch: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2: _Optional[int] = ..., player_danmaku_ai_recommended_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DanmuPlayerConfigPanel(_message.Message):
	__slots__ = ["selection_text"]
	SELECTION_TEXT_FIELD_NUMBER: _ClassVar[int]
	selection_text: str
	def __init__(self, selection_text: _Optional[str] = ...) -> None: ...

class DanmuPlayerDynamicConfig(_message.Message):
	__slots__ = ["player_danmaku_domain", "progress"]
	PLAYER_DANMAKU_DOMAIN_FIELD_NUMBER: _ClassVar[int]
	PROGRESS_FIELD_NUMBER: _ClassVar[int]
	player_danmaku_domain: float
	progress: int
	def __init__(self, progress: _Optional[int] = ..., player_danmaku_domain: _Optional[float] = ...) -> None: ...

class DanmuPlayerViewConfig(_message.Message):
	__slots__ = ["danmuku_default_player_config", "danmuku_player_config", "danmuku_player_config_panel", "danmuku_player_dynamic_config"]
	DANMUKU_DEFAULT_PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
	DANMUKU_PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
	DANMUKU_PLAYER_CONFIG_PANEL_FIELD_NUMBER: _ClassVar[int]
	DANMUKU_PLAYER_DYNAMIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
	danmuku_default_player_config: DanmuDefaultPlayerConfig
	danmuku_player_config: DanmuPlayerConfig
	danmuku_player_config_panel: DanmuPlayerConfigPanel
	danmuku_player_dynamic_config: _containers.RepeatedCompositeFieldContainer[DanmuPlayerDynamicConfig]
	def __init__(self, danmuku_default_player_config: _Optional[_Union[DanmuDefaultPlayerConfig, _Mapping]] = ..., danmuku_player_config: _Optional[_Union[DanmuPlayerConfig, _Mapping]] = ..., danmuku_player_dynamic_config: _Optional[_Iterable[_Union[DanmuPlayerDynamicConfig, _Mapping]]] = ..., danmuku_player_config_panel: _Optional[_Union[DanmuPlayerConfigPanel, _Mapping]] = ...) -> None: ...

class DanmuWebPlayerConfig(_message.Message):
	__slots__ = ["ai_level", "ai_level_v2", "ai_level_v2_map", "ai_switch", "blockbottom", "blockcolor", "blockscroll", "blockspecial", "blocktop", "bold", "dm_switch", "dmarea", "dmask", "draw_type", "fontborder", "fontfamily", "fontsize", "opacity", "preventshade", "screensync", "senior_mode_switch", "speedplus", "speedsync"]
	class AiLevelV2MapEntry(_message.Message):
		__slots__ = ["key", "value"]
		KEY_FIELD_NUMBER: _ClassVar[int]
		VALUE_FIELD_NUMBER: _ClassVar[int]
		key: int
		value: int
		def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
	AI_LEVEL_FIELD_NUMBER: _ClassVar[int]
	AI_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
	AI_LEVEL_V2_MAP_FIELD_NUMBER: _ClassVar[int]
	AI_SWITCH_FIELD_NUMBER: _ClassVar[int]
	BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
	BLOCKCOLOR_FIELD_NUMBER: _ClassVar[int]
	BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
	BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
	BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
	BOLD_FIELD_NUMBER: _ClassVar[int]
	DMAREA_FIELD_NUMBER: _ClassVar[int]
	DMASK_FIELD_NUMBER: _ClassVar[int]
	DM_SWITCH_FIELD_NUMBER: _ClassVar[int]
	DRAW_TYPE_FIELD_NUMBER: _ClassVar[int]
	FONTBORDER_FIELD_NUMBER: _ClassVar[int]
	FONTFAMILY_FIELD_NUMBER: _ClassVar[int]
	FONTSIZE_FIELD_NUMBER: _ClassVar[int]
	OPACITY_FIELD_NUMBER: _ClassVar[int]
	PREVENTSHADE_FIELD_NUMBER: _ClassVar[int]
	SCREENSYNC_FIELD_NUMBER: _ClassVar[int]
	SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
	SPEEDPLUS_FIELD_NUMBER: _ClassVar[int]
	SPEEDSYNC_FIELD_NUMBER: _ClassVar[int]
	ai_level: int
	ai_level_v2: int
	ai_level_v2_map: _containers.ScalarMap[int, int]
	ai_switch: bool
	blockbottom: bool
	blockcolor: bool
	blockscroll: bool
	blockspecial: bool
	blocktop: bool
	bold: bool
	dm_switch: bool
	dmarea: int
	dmask: bool
	draw_type: str
	fontborder: int
	fontfamily: str
	fontsize: float
	opacity: float
	preventshade: bool
	screensync: bool
	senior_mode_switch: int
	speedplus: float
	speedsync: bool
	def __init__(self, dm_switch: bool = ..., ai_switch: bool = ..., ai_level: _Optional[int] = ..., blocktop: bool = ..., blockscroll: bool = ..., blockbottom: bool = ..., blockcolor: bool = ..., blockspecial: bool = ..., preventshade: bool = ..., dmask: bool = ..., opacity: _Optional[float] = ..., dmarea: _Optional[int] = ..., speedplus: _Optional[float] = ..., fontsize: _Optional[float] = ..., screensync: bool = ..., speedsync: bool = ..., fontfamily: _Optional[str] = ..., bold: bool = ..., fontborder: _Optional[int] = ..., draw_type: _Optional[str] = ..., senior_mode_switch: _Optional[int] = ..., ai_level_v2: _Optional[int] = ..., ai_level_v2_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DmExpoReportReq(_message.Message):
	__slots__ = ["oid", "session_id", "spmid"]
	OID_FIELD_NUMBER: _ClassVar[int]
	SESSION_ID_FIELD_NUMBER: _ClassVar[int]
	SPMID_FIELD_NUMBER: _ClassVar[int]
	oid: int
	session_id: str
	spmid: str
	def __init__(self, session_id: _Optional[str] = ..., oid: _Optional[int] = ..., spmid: _Optional[str] = ...) -> None: ...

class DmExpoReportRes(_message.Message):
	__slots__ = []
	def __init__(self) -> None: ...

class DmPlayerConfigReq(_message.Message):
	__slots__ = ["ai_recommended_level", "ai_recommended_level_v2", "ai_recommended_switch", "blockbottom", "blockcolorful", "blockrepeat", "blockscroll", "blockspecial", "blocktop", "domain", "enableblocklist", "inlinePlayerDanmakuSwitch", "opacity", "scalingfactor", "senior_mode_switch", "speed", "switch", "switch_save", "ts", "use_default_config"]
	AI_RECOMMENDED_LEVEL_FIELD_NUMBER: _ClassVar[int]
	AI_RECOMMENDED_LEVEL_V2_FIELD_NUMBER: _ClassVar[int]
	AI_RECOMMENDED_SWITCH_FIELD_NUMBER: _ClassVar[int]
	BLOCKBOTTOM_FIELD_NUMBER: _ClassVar[int]
	BLOCKCOLORFUL_FIELD_NUMBER: _ClassVar[int]
	BLOCKREPEAT_FIELD_NUMBER: _ClassVar[int]
	BLOCKSCROLL_FIELD_NUMBER: _ClassVar[int]
	BLOCKSPECIAL_FIELD_NUMBER: _ClassVar[int]
	BLOCKTOP_FIELD_NUMBER: _ClassVar[int]
	DOMAIN_FIELD_NUMBER: _ClassVar[int]
	ENABLEBLOCKLIST_FIELD_NUMBER: _ClassVar[int]
	INLINEPLAYERDANMAKUSWITCH_FIELD_NUMBER: _ClassVar[int]
	OPACITY_FIELD_NUMBER: _ClassVar[int]
	SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
	SENIOR_MODE_SWITCH_FIELD_NUMBER: _ClassVar[int]
	SPEED_FIELD_NUMBER: _ClassVar[int]
	SWITCH_FIELD_NUMBER: _ClassVar[int]
	SWITCH_SAVE_FIELD_NUMBER: _ClassVar[int]
	TS_FIELD_NUMBER: _ClassVar[int]
	USE_DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
	ai_recommended_level: PlayerDanmakuAiRecommendedLevel
	ai_recommended_level_v2: PlayerDanmakuAiRecommendedLevelV2
	ai_recommended_switch: PlayerDanmakuAiRecommendedSwitch
	blockbottom: PlayerDanmakuBlockbottom
	blockcolorful: PlayerDanmakuBlockcolorful
	blockrepeat: PlayerDanmakuBlockrepeat
	blockscroll: PlayerDanmakuBlockscroll
	blockspecial: PlayerDanmakuBlockspecial
	blocktop: PlayerDanmakuBlocktop
	domain: PlayerDanmakuDomain
	enableblocklist: PlayerDanmakuEnableblocklist
	inlinePlayerDanmakuSwitch: InlinePlayerDanmakuSwitch
	opacity: PlayerDanmakuOpacity
	scalingfactor: PlayerDanmakuScalingfactor
	senior_mode_switch: PlayerDanmakuSeniorModeSwitch
	speed: PlayerDanmakuSpeed
	switch: PlayerDanmakuSwitch
	switch_save: PlayerDanmakuSwitchSave
	ts: int
	use_default_config: PlayerDanmakuUseDefaultConfig
	def __init__(self, ts: _Optional[int] = ..., switch: _Optional[_Union[PlayerDanmakuSwitch, _Mapping]] = ..., switch_save: _Optional[_Union[PlayerDanmakuSwitchSave, _Mapping]] = ..., use_default_config: _Optional[_Union[PlayerDanmakuUseDefaultConfig, _Mapping]] = ..., ai_recommended_switch: _Optional[_Union[PlayerDanmakuAiRecommendedSwitch, _Mapping]] = ..., ai_recommended_level: _Optional[_Union[PlayerDanmakuAiRecommendedLevel, _Mapping]] = ..., blocktop: _Optional[_Union[PlayerDanmakuBlocktop, _Mapping]] = ..., blockscroll: _Optional[_Union[PlayerDanmakuBlockscroll, _Mapping]] = ..., blockbottom: _Optional[_Union[PlayerDanmakuBlockbottom, _Mapping]] = ..., blockcolorful: _Optional[_Union[PlayerDanmakuBlockcolorful, _Mapping]] = ..., blockrepeat: _Optional[_Union[PlayerDanmakuBlockrepeat, _Mapping]] = ..., blockspecial: _Optional[_Union[PlayerDanmakuBlockspecial, _Mapping]] = ..., opacity: _Optional[_Union[PlayerDanmakuOpacity, _Mapping]] = ..., scalingfactor: _Optional[_Union[PlayerDanmakuScalingfactor, _Mapping]] = ..., domain: _Optional[_Union[PlayerDanmakuDomain, _Mapping]] = ..., speed: _Optional[_Union[PlayerDanmakuSpeed, _Mapping]] = ..., enableblocklist: _Optional[_Union[PlayerDanmakuEnableblocklist, _Mapping]] = ..., inlinePlayerDanmakuSwitch: _Optional[_Union[InlinePlayerDanmakuSwitch, _Mapping]] = ..., senior_mode_switch: _Optional[_Union[PlayerDanmakuSeniorModeSwitch, _Mapping]] = ..., ai_recommended_level_v2: _Optional[_Union[PlayerDanmakuAiRecommendedLevelV2, _Mapping]] = ...) -> None: ...

class DmSegConfig(_message.Message):
	__slots__ = ["page_size", "total"]
	PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
	TOTAL_FIELD_NUMBER: _ClassVar[int]
	page_size: int
	total: int
	def __init__(self, page_size: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class DmSegMobileReply(_message.Message):
	__slots__ = ["ai_flag", "elems", "state"]
	AI_FLAG_FIELD_NUMBER: _ClassVar[int]
	ELEMS_FIELD_NUMBER: _ClassVar[int]
	STATE_FIELD_NUMBER: _ClassVar[int]
	ai_flag: DanmakuAIFlag
	elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
	state: int
	def __init__(self, elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ..., state: _Optional[int] = ..., ai_flag: _Optional[_Union[DanmakuAIFlag, _Mapping]] = ...) -> None: ...

class DmSegMobileReq(_message.Message):
	__slots__ = ["from_scene", "oid", "pe", "pid", "ps", "pull_mode", "segment_index", "teenagers_mode", "type"]
	FROM_SCENE_FIELD_NUMBER: _ClassVar[int]
	OID_FIELD_NUMBER: _ClassVar[int]
	PE_FIELD_NUMBER: _ClassVar[int]
	PID_FIELD_NUMBER: _ClassVar[int]
	PS_FIELD_NUMBER: _ClassVar[int]
	PULL_MODE_FIELD_NUMBER: _ClassVar[int]
	SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
	TEENAGERS_MODE_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	from_scene: int
	oid: int
	pe: int
	pid: int
	ps: int
	pull_mode: int
	segment_index: int
	teenagers_mode: int
	type: int
	def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ..., teenagers_mode: _Optional[int] = ..., ps: _Optional[int] = ..., pe: _Optional[int] = ..., pull_mode: _Optional[int] = ..., from_scene: _Optional[int] = ...) -> None: ...

class DmSegOttReply(_message.Message):
	__slots__ = ["closed", "elems"]
	CLOSED_FIELD_NUMBER: _ClassVar[int]
	ELEMS_FIELD_NUMBER: _ClassVar[int]
	closed: bool
	elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
	def __init__(self, closed: bool = ..., elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ...) -> None: ...

class DmSegOttReq(_message.Message):
	__slots__ = ["oid", "pid", "segment_index", "type"]
	OID_FIELD_NUMBER: _ClassVar[int]
	PID_FIELD_NUMBER: _ClassVar[int]
	SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	oid: int
	pid: int
	segment_index: int
	type: int
	def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ...) -> None: ...

class DmSegSDKReply(_message.Message):
	__slots__ = ["closed", "elems"]
	CLOSED_FIELD_NUMBER: _ClassVar[int]
	ELEMS_FIELD_NUMBER: _ClassVar[int]
	closed: bool
	elems: _containers.RepeatedCompositeFieldContainer[DanmakuElem]
	def __init__(self, closed: bool = ..., elems: _Optional[_Iterable[_Union[DanmakuElem, _Mapping]]] = ...) -> None: ...

class DmSegSDKReq(_message.Message):
	__slots__ = ["oid", "pid", "segment_index", "type"]
	OID_FIELD_NUMBER: _ClassVar[int]
	PID_FIELD_NUMBER: _ClassVar[int]
	SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	oid: int
	pid: int
	segment_index: int
	type: int
	def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., segment_index: _Optional[int] = ...) -> None: ...

class DmViewReply(_message.Message):
	__slots__ = ["activity_meta", "ai_flag", "allow", "buzzword_config", "check_box", "check_box_show_msg", "closed", "expo_report", "expressions", "input_placeholder", "mask", "player_config", "post_panel", "post_panel2", "report_filter_content", "send_box_style", "special_dms", "subtitle", "text_placeholder"]
	ACTIVITY_META_FIELD_NUMBER: _ClassVar[int]
	AI_FLAG_FIELD_NUMBER: _ClassVar[int]
	ALLOW_FIELD_NUMBER: _ClassVar[int]
	BUZZWORD_CONFIG_FIELD_NUMBER: _ClassVar[int]
	CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
	CHECK_BOX_SHOW_MSG_FIELD_NUMBER: _ClassVar[int]
	CLOSED_FIELD_NUMBER: _ClassVar[int]
	EXPO_REPORT_FIELD_NUMBER: _ClassVar[int]
	EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
	INPUT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	MASK_FIELD_NUMBER: _ClassVar[int]
	PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
	POST_PANEL2_FIELD_NUMBER: _ClassVar[int]
	POST_PANEL_FIELD_NUMBER: _ClassVar[int]
	REPORT_FILTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
	SEND_BOX_STYLE_FIELD_NUMBER: _ClassVar[int]
	SPECIAL_DMS_FIELD_NUMBER: _ClassVar[int]
	SUBTITLE_FIELD_NUMBER: _ClassVar[int]
	TEXT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	activity_meta: _containers.RepeatedScalarFieldContainer[str]
	ai_flag: DanmakuFlagConfig
	allow: bool
	buzzword_config: BuzzwordConfig
	check_box: str
	check_box_show_msg: str
	closed: bool
	expo_report: ExpoReport
	expressions: _containers.RepeatedCompositeFieldContainer[Expressions]
	input_placeholder: str
	mask: VideoMask
	player_config: DanmuPlayerViewConfig
	post_panel: _containers.RepeatedCompositeFieldContainer[PostPanel]
	post_panel2: _containers.RepeatedCompositeFieldContainer[PostPanelV2]
	report_filter_content: _containers.RepeatedScalarFieldContainer[str]
	send_box_style: int
	special_dms: _containers.RepeatedScalarFieldContainer[str]
	subtitle: VideoSubtitle
	text_placeholder: str
	def __init__(self, closed: bool = ..., mask: _Optional[_Union[VideoMask, _Mapping]] = ..., subtitle: _Optional[_Union[VideoSubtitle, _Mapping]] = ..., special_dms: _Optional[_Iterable[str]] = ..., ai_flag: _Optional[_Union[DanmakuFlagConfig, _Mapping]] = ..., player_config: _Optional[_Union[DanmuPlayerViewConfig, _Mapping]] = ..., send_box_style: _Optional[int] = ..., allow: bool = ..., check_box: _Optional[str] = ..., check_box_show_msg: _Optional[str] = ..., text_placeholder: _Optional[str] = ..., input_placeholder: _Optional[str] = ..., report_filter_content: _Optional[_Iterable[str]] = ..., expo_report: _Optional[_Union[ExpoReport, _Mapping]] = ..., buzzword_config: _Optional[_Union[BuzzwordConfig, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[Expressions, _Mapping]]] = ..., post_panel: _Optional[_Iterable[_Union[PostPanel, _Mapping]]] = ..., activity_meta: _Optional[_Iterable[str]] = ..., post_panel2: _Optional[_Iterable[_Union[PostPanelV2, _Mapping]]] = ...) -> None: ...

class DmViewReq(_message.Message):
	__slots__ = ["is_hard_boot", "oid", "pid", "spmid", "type"]
	IS_HARD_BOOT_FIELD_NUMBER: _ClassVar[int]
	OID_FIELD_NUMBER: _ClassVar[int]
	PID_FIELD_NUMBER: _ClassVar[int]
	SPMID_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	is_hard_boot: int
	oid: int
	pid: int
	spmid: str
	type: int
	def __init__(self, pid: _Optional[int] = ..., oid: _Optional[int] = ..., type: _Optional[int] = ..., spmid: _Optional[str] = ..., is_hard_boot: _Optional[int] = ...) -> None: ...

class DmWebViewReply(_message.Message):
	__slots__ = ["activity_meta", "check_box", "commandDms", "count", "dm_sge", "expressions", "flag", "player_config", "post_panel", "report_filter_content", "special_dms", "state", "text", "text_side"]
	ACTIVITY_META_FIELD_NUMBER: _ClassVar[int]
	CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
	COMMANDDMS_FIELD_NUMBER: _ClassVar[int]
	COUNT_FIELD_NUMBER: _ClassVar[int]
	DM_SGE_FIELD_NUMBER: _ClassVar[int]
	EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
	FLAG_FIELD_NUMBER: _ClassVar[int]
	PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
	POST_PANEL_FIELD_NUMBER: _ClassVar[int]
	REPORT_FILTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
	SPECIAL_DMS_FIELD_NUMBER: _ClassVar[int]
	STATE_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	TEXT_SIDE_FIELD_NUMBER: _ClassVar[int]
	activity_meta: _containers.RepeatedScalarFieldContainer[str]
	check_box: bool
	commandDms: _containers.RepeatedCompositeFieldContainer[CommandDm]
	count: int
	dm_sge: DmSegConfig
	expressions: _containers.RepeatedCompositeFieldContainer[Expressions]
	flag: DanmakuFlagConfig
	player_config: DanmuWebPlayerConfig
	post_panel: _containers.RepeatedCompositeFieldContainer[PostPanel]
	report_filter_content: _containers.RepeatedScalarFieldContainer[str]
	special_dms: _containers.RepeatedScalarFieldContainer[str]
	state: int
	text: str
	text_side: str
	def __init__(self, state: _Optional[int] = ..., text: _Optional[str] = ..., text_side: _Optional[str] = ..., dm_sge: _Optional[_Union[DmSegConfig, _Mapping]] = ..., flag: _Optional[_Union[DanmakuFlagConfig, _Mapping]] = ..., special_dms: _Optional[_Iterable[str]] = ..., check_box: bool = ..., count: _Optional[int] = ..., commandDms: _Optional[_Iterable[_Union[CommandDm, _Mapping]]] = ..., player_config: _Optional[_Union[DanmuWebPlayerConfig, _Mapping]] = ..., report_filter_content: _Optional[_Iterable[str]] = ..., expressions: _Optional[_Iterable[_Union[Expressions, _Mapping]]] = ..., post_panel: _Optional[_Iterable[_Union[PostPanel, _Mapping]]] = ..., activity_meta: _Optional[_Iterable[str]] = ...) -> None: ...

class ExpoReport(_message.Message):
	__slots__ = ["should_report_at_end"]
	SHOULD_REPORT_AT_END_FIELD_NUMBER: _ClassVar[int]
	should_report_at_end: bool
	def __init__(self, should_report_at_end: bool = ...) -> None: ...

class Expression(_message.Message):
	__slots__ = ["keyword", "period", "url"]
	KEYWORD_FIELD_NUMBER: _ClassVar[int]
	PERIOD_FIELD_NUMBER: _ClassVar[int]
	URL_FIELD_NUMBER: _ClassVar[int]
	keyword: _containers.RepeatedScalarFieldContainer[str]
	period: _containers.RepeatedCompositeFieldContainer[Period]
	url: str
	def __init__(self, keyword: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ..., period: _Optional[_Iterable[_Union[Period, _Mapping]]] = ...) -> None: ...

class Expressions(_message.Message):
	__slots__ = ["data"]
	DATA_FIELD_NUMBER: _ClassVar[int]
	data: _containers.RepeatedCompositeFieldContainer[Expression]
	def __init__(self, data: _Optional[_Iterable[_Union[Expression, _Mapping]]] = ...) -> None: ...

class InlinePlayerDanmakuSwitch(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class Label(_message.Message):
	__slots__ = ["content", "title"]
	CONTENT_FIELD_NUMBER: _ClassVar[int]
	TITLE_FIELD_NUMBER: _ClassVar[int]
	content: _containers.RepeatedScalarFieldContainer[str]
	title: str
	def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ...) -> None: ...

class LabelV2(_message.Message):
	__slots__ = ["content", "exposure_once", "exposure_type", "title"]
	CONTENT_FIELD_NUMBER: _ClassVar[int]
	EXPOSURE_ONCE_FIELD_NUMBER: _ClassVar[int]
	EXPOSURE_TYPE_FIELD_NUMBER: _ClassVar[int]
	TITLE_FIELD_NUMBER: _ClassVar[int]
	content: _containers.RepeatedScalarFieldContainer[str]
	exposure_once: bool
	exposure_type: int
	title: str
	def __init__(self, title: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ..., exposure_once: bool = ..., exposure_type: _Optional[int] = ...) -> None: ...

class Period(_message.Message):
	__slots__ = ["end", "start"]
	END_FIELD_NUMBER: _ClassVar[int]
	START_FIELD_NUMBER: _ClassVar[int]
	end: int
	start: int
	def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class PlayerDanmakuAiRecommendedLevel(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuAiRecommendedLevelV2(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: int
	def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuAiRecommendedSwitch(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockbottom(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockcolorful(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockrepeat(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockscroll(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlockspecial(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuBlocktop(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuDomain(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: float
	def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuEnableblocklist(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuOpacity(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: float
	def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuScalingfactor(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: float
	def __init__(self, value: _Optional[float] = ...) -> None: ...

class PlayerDanmakuSeniorModeSwitch(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: int
	def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuSpeed(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: int
	def __init__(self, value: _Optional[int] = ...) -> None: ...

class PlayerDanmakuSwitch(_message.Message):
	__slots__ = ["can_ignore", "value"]
	CAN_IGNORE_FIELD_NUMBER: _ClassVar[int]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	can_ignore: bool
	value: bool
	def __init__(self, value: bool = ..., can_ignore: bool = ...) -> None: ...

class PlayerDanmakuSwitchSave(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PlayerDanmakuUseDefaultConfig(_message.Message):
	__slots__ = ["value"]
	VALUE_FIELD_NUMBER: _ClassVar[int]
	value: bool
	def __init__(self, value: bool = ...) -> None: ...

class PostPanel(_message.Message):
	__slots__ = ["biz_id", "biz_type", "check_box", "click_button", "end", "priority", "start", "text_input", "toast"]
	BIZ_ID_FIELD_NUMBER: _ClassVar[int]
	BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
	CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
	CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
	END_FIELD_NUMBER: _ClassVar[int]
	PRIORITY_FIELD_NUMBER: _ClassVar[int]
	START_FIELD_NUMBER: _ClassVar[int]
	TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
	TOAST_FIELD_NUMBER: _ClassVar[int]
	biz_id: int
	biz_type: PostPanelBizType
	check_box: CheckBox
	click_button: ClickButton
	end: int
	priority: int
	start: int
	text_input: TextInput
	toast: Toast
	def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., priority: _Optional[int] = ..., biz_id: _Optional[int] = ..., biz_type: _Optional[_Union[PostPanelBizType, str]] = ..., click_button: _Optional[_Union[ClickButton, _Mapping]] = ..., text_input: _Optional[_Union[TextInput, _Mapping]] = ..., check_box: _Optional[_Union[CheckBox, _Mapping]] = ..., toast: _Optional[_Union[Toast, _Mapping]] = ...) -> None: ...

class PostPanelV2(_message.Message):
	__slots__ = ["biz_type", "bubble", "check_box", "click_button", "end", "label", "post_status", "start", "text_input", "toast"]
	BIZ_TYPE_FIELD_NUMBER: _ClassVar[int]
	BUBBLE_FIELD_NUMBER: _ClassVar[int]
	CHECK_BOX_FIELD_NUMBER: _ClassVar[int]
	CLICK_BUTTON_FIELD_NUMBER: _ClassVar[int]
	END_FIELD_NUMBER: _ClassVar[int]
	LABEL_FIELD_NUMBER: _ClassVar[int]
	POST_STATUS_FIELD_NUMBER: _ClassVar[int]
	START_FIELD_NUMBER: _ClassVar[int]
	TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
	TOAST_FIELD_NUMBER: _ClassVar[int]
	biz_type: int
	bubble: BubbleV2
	check_box: CheckBoxV2
	click_button: ClickButtonV2
	end: int
	label: LabelV2
	post_status: int
	start: int
	text_input: TextInputV2
	toast: ToastV2
	def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., biz_type: _Optional[int] = ..., click_button: _Optional[_Union[ClickButtonV2, _Mapping]] = ..., text_input: _Optional[_Union[TextInputV2, _Mapping]] = ..., check_box: _Optional[_Union[CheckBoxV2, _Mapping]] = ..., toast: _Optional[_Union[ToastV2, _Mapping]] = ..., bubble: _Optional[_Union[BubbleV2, _Mapping]] = ..., label: _Optional[_Union[LabelV2, _Mapping]] = ..., post_status: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
	__slots__ = ["code", "message"]
	CODE_FIELD_NUMBER: _ClassVar[int]
	MESSAGE_FIELD_NUMBER: _ClassVar[int]
	code: int
	message: str
	def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class SubtitleItem(_message.Message):
	__slots__ = ["ai_status", "ai_type", "author", "id", "id_str", "lan", "lan_doc", "lan_doc_brief", "subtitle_url", "type"]
	AI_STATUS_FIELD_NUMBER: _ClassVar[int]
	AI_TYPE_FIELD_NUMBER: _ClassVar[int]
	AUTHOR_FIELD_NUMBER: _ClassVar[int]
	ID_FIELD_NUMBER: _ClassVar[int]
	ID_STR_FIELD_NUMBER: _ClassVar[int]
	LAN_DOC_BRIEF_FIELD_NUMBER: _ClassVar[int]
	LAN_DOC_FIELD_NUMBER: _ClassVar[int]
	LAN_FIELD_NUMBER: _ClassVar[int]
	SUBTITLE_URL_FIELD_NUMBER: _ClassVar[int]
	TYPE_FIELD_NUMBER: _ClassVar[int]
	ai_status: SubtitleAiStatus
	ai_type: SubtitleAiType
	author: UserInfo
	id: int
	id_str: str
	lan: str
	lan_doc: str
	lan_doc_brief: str
	subtitle_url: str
	type: SubtitleType
	def __init__(self, id: _Optional[int] = ..., id_str: _Optional[str] = ..., lan: _Optional[str] = ..., lan_doc: _Optional[str] = ..., subtitle_url: _Optional[str] = ..., author: _Optional[_Union[UserInfo, _Mapping]] = ..., type: _Optional[_Union[SubtitleType, str]] = ..., lan_doc_brief: _Optional[str] = ..., ai_type: _Optional[_Union[SubtitleAiType, str]] = ..., ai_status: _Optional[_Union[SubtitleAiStatus, str]] = ...) -> None: ...

class TextInput(_message.Message):
	__slots__ = ["avatar", "label", "landscape_placeholder", "placeholder_post", "portrait_placeholder", "post_status", "render_type", "show"]
	AVATAR_FIELD_NUMBER: _ClassVar[int]
	LABEL_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	POST_STATUS_FIELD_NUMBER: _ClassVar[int]
	RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
	SHOW_FIELD_NUMBER: _ClassVar[int]
	avatar: _containers.RepeatedCompositeFieldContainer[Avatar]
	label: Label
	landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
	placeholder_post: bool
	portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
	post_status: PostStatus
	render_type: RenderType
	show: bool
	def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., show: bool = ..., avatar: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ..., post_status: _Optional[_Union[PostStatus, str]] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class TextInputV2(_message.Message):
	__slots__ = ["avatar", "landscape_placeholder", "placeholder_post", "portrait_placeholder", "render_type", "text_input_limit"]
	AVATAR_FIELD_NUMBER: _ClassVar[int]
	LANDSCAPE_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	PLACEHOLDER_POST_FIELD_NUMBER: _ClassVar[int]
	PORTRAIT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
	RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
	TEXT_INPUT_LIMIT_FIELD_NUMBER: _ClassVar[int]
	avatar: _containers.RepeatedCompositeFieldContainer[Avatar]
	landscape_placeholder: _containers.RepeatedScalarFieldContainer[str]
	placeholder_post: bool
	portrait_placeholder: _containers.RepeatedScalarFieldContainer[str]
	render_type: RenderType
	text_input_limit: int
	def __init__(self, portrait_placeholder: _Optional[_Iterable[str]] = ..., landscape_placeholder: _Optional[_Iterable[str]] = ..., render_type: _Optional[_Union[RenderType, str]] = ..., placeholder_post: bool = ..., avatar: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ..., text_input_limit: _Optional[int] = ...) -> None: ...

class Toast(_message.Message):
	__slots__ = ["button", "duration", "show", "text"]
	BUTTON_FIELD_NUMBER: _ClassVar[int]
	DURATION_FIELD_NUMBER: _ClassVar[int]
	SHOW_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	button: Button
	duration: int
	show: bool
	text: str
	def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., show: bool = ..., button: _Optional[_Union[Button, _Mapping]] = ...) -> None: ...

class ToastButtonV2(_message.Message):
	__slots__ = ["action", "text"]
	ACTION_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	action: int
	text: str
	def __init__(self, text: _Optional[str] = ..., action: _Optional[int] = ...) -> None: ...

class ToastV2(_message.Message):
	__slots__ = ["duration", "text", "toast_button_v2"]
	DURATION_FIELD_NUMBER: _ClassVar[int]
	TEXT_FIELD_NUMBER: _ClassVar[int]
	TOAST_BUTTON_V2_FIELD_NUMBER: _ClassVar[int]
	duration: int
	text: str
	toast_button_v2: ToastButtonV2
	def __init__(self, text: _Optional[str] = ..., duration: _Optional[int] = ..., toast_button_v2: _Optional[_Union[ToastButtonV2, _Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
	__slots__ = ["face", "mid", "name", "rank", "sex", "sign"]
	FACE_FIELD_NUMBER: _ClassVar[int]
	MID_FIELD_NUMBER: _ClassVar[int]
	NAME_FIELD_NUMBER: _ClassVar[int]
	RANK_FIELD_NUMBER: _ClassVar[int]
	SEX_FIELD_NUMBER: _ClassVar[int]
	SIGN_FIELD_NUMBER: _ClassVar[int]
	face: str
	mid: int
	name: str
	rank: int
	sex: str
	sign: str
	def __init__(self, mid: _Optional[int] = ..., name: _Optional[str] = ..., sex: _Optional[str] = ..., face: _Optional[str] = ..., sign: _Optional[str] = ..., rank: _Optional[int] = ...) -> None: ...

class VideoMask(_message.Message):
	__slots__ = ["cid", "fps", "mask_url", "plat", "time"]
	CID_FIELD_NUMBER: _ClassVar[int]
	FPS_FIELD_NUMBER: _ClassVar[int]
	MASK_URL_FIELD_NUMBER: _ClassVar[int]
	PLAT_FIELD_NUMBER: _ClassVar[int]
	TIME_FIELD_NUMBER: _ClassVar[int]
	cid: int
	fps: int
	mask_url: str
	plat: int
	time: int
	def __init__(self, cid: _Optional[int] = ..., plat: _Optional[int] = ..., fps: _Optional[int] = ..., time: _Optional[int] = ..., mask_url: _Optional[str] = ...) -> None: ...

class VideoSubtitle(_message.Message):
	__slots__ = ["lan", "lanDoc", "subtitles"]
	LANDOC_FIELD_NUMBER: _ClassVar[int]
	LAN_FIELD_NUMBER: _ClassVar[int]
	SUBTITLES_FIELD_NUMBER: _ClassVar[int]
	lan: str
	lanDoc: str
	subtitles: _containers.RepeatedCompositeFieldContainer[SubtitleItem]
	def __init__(self, lan: _Optional[str] = ..., lanDoc: _Optional[str] = ..., subtitles: _Optional[_Iterable[_Union[SubtitleItem, _Mapping]]] = ...) -> None: ...

class AvatarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class BubbleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class CheckboxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class DMAttrBit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class ExposureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class PostPanelBizType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class RenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class SubtitleAiStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class SubtitleAiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class SubtitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []

class ToastFunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
	__slots__ = []
