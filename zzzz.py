# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zzzz.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nzzzz.proto\x12 bilibili.community.service.dm.v1\"\xf3\x01\n\x10\x44mSegMobileReply\x12<\n\x05\x65lems\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12@\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.DanmakuAIFlag\x12\x0c\n\x04time\x18\x04 \x01(\x05\x12\x42\n\x0c\x63olorful_src\x18\x05 \x03(\x0b\x32,.bilibili.community.service.dm.v1.DmColorful\"\xa4\x04\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05stime\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\r\n\x05uhash\x18\x06 \x01(\t\x12\x0c\n\x04text\x18\x07 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\x0c\n\x04\x64mid\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\x12\x0f\n\x07usermid\x18\x0e \x01(\x04\x12\r\n\x05likes\x18\x0f \x01(\r\x12\x0e\n\x06test16\x18\x10 \x01(\x04\x12\x0e\n\x06test17\x18\x11 \x01(\x04\x12\x13\n\x0breply_count\x18\x12 \x01(\r\x12\x0e\n\x06test19\x18\x13 \x01(\x0c\x12\x0e\n\x06test20\x18\x14 \x01(\t\x12\x0e\n\x06test21\x18\x15 \x01(\t\x12\x11\n\tanimation\x18\x16 \x01(\t\x12\x0e\n\x06test23\x18\x17 \x01(\x0c\x12\x42\n\x08\x63olorful\x18\x18 \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.DmColorfulType\x12\x0e\n\x06test25\x18\x19 \x01(\x0c\x12\x0e\n\x06test26\x18\x1a \x01(\x0c\x12\x0e\n\x06test27\x18\x1b \x01(\x0c\x12\x0e\n\x06test28\x18\x1c \x01(\x0c\x12\x0e\n\x06test29\x18\x1d \x01(\x0c\x12\x0e\n\x06test30\x18\x1e \x01(\x0c\x12\x0e\n\x06test31\x18\x1f \x01(\x0c\"P\n\rDanmakuAIFlag\x12?\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuFlag\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"\x8a\x05\n\x0e\x44mWebViewReply\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\ttext_side\x18\x03 \x01(\t\x12=\n\x06\x64m_sge\x18\x04 \x01(\x0b\x32-.bilibili.community.service.dm.v1.DmSegConfig\x12\x41\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12\x13\n\x0bspecial_dms\x18\x06 \x03(\t\x12\x11\n\tcheck_box\x18\x07 \x01(\x08\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12?\n\ncommandDms\x18\t \x03(\x0b\x32+.bilibili.community.service.dm.v1.CommandDm\x12M\n\rplayer_config\x18\n \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.DanmuWebPlayerConfig\x12\x1d\n\x15report_filter_content\x18\x0b \x03(\t\x12\x42\n\x0b\x65xpressions\x18\x0c \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\x12?\n\npost_panel\x18\r \x03(\x0b\x32+.bilibili.community.service.dm.v1.PostPanel\x12\x15\n\ractivity_meta\x18\x0e \x03(\t\x12\x44\n\rpost_panel_v2\x18\x0f \x03(\x0b\x32-.bilibili.community.service.dm.v1.PostPanelV2\"/\n\x0b\x44mSegConfig\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"\x9d\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\r\n\x05stime\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\x0c\n\x04\x64mid\x18\n \x01(\t\"\xdc\x04\n\x14\x44\x61nmuWebPlayerConfig\x12\x11\n\tdm_switch\x18\x01 \x01(\x08\x12\x11\n\tai_switch\x18\x02 \x01(\x08\x12\x10\n\x08\x61i_level\x18\x03 \x01(\x05\x12\x10\n\x08type_top\x18\x04 \x01(\x08\x12\x13\n\x0btype_scroll\x18\x05 \x01(\x08\x12\x13\n\x0btype_bottom\x18\x06 \x01(\x08\x12\x12\n\ntype_color\x18\x07 \x01(\x08\x12\x14\n\x0ctype_special\x18\x08 \x01(\x08\x12\x14\n\x0cpreventshade\x18\t \x01(\x08\x12\r\n\x05\x64mask\x18\n \x01(\x08\x12\x0f\n\x07opacity\x18\x0b \x01(\x02\x12\x0e\n\x06\x64marea\x18\x0c \x01(\x05\x12\x11\n\tspeedplus\x18\r \x01(\x02\x12\x10\n\x08\x66ontsize\x18\x0e \x01(\x02\x12\x16\n\x0e\x66ullscreensync\x18\x0f \x01(\x08\x12\x11\n\tspeedsync\x18\x10 \x01(\x08\x12\x12\n\nfontfamily\x18\x11 \x01(\t\x12\x0c\n\x04\x62old\x18\x12 \x01(\x08\x12\x12\n\nfontborder\x18\x13 \x01(\x05\x12\x11\n\tdraw_type\x18\x14 \x01(\t\x12\x1a\n\x12senior_mode_switch\x18\x15 \x01(\x05\x12\x13\n\x0b\x61i_level_v2\x18\x16 \x01(\x05\x12\x61\n\x0f\x61i_level_v2_map\x18\x17 \x03(\x0b\x32H.bilibili.community.service.dm.v1.DanmuWebPlayerConfig.AiLevelV2MapEntry\x1a\x33\n\x11\x41iLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"I\n\x0b\x45xpressions\x12:\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32,.bilibili.community.service.dm.v1.Expression\"d\n\nExpression\x12\x0f\n\x07keyword\x18\x01 \x03(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x38\n\x06period\x18\x03 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Period\"$\n\x06Period\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"\x8c\x03\n\tPostPanel\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x10\n\x08priority\x18\x03 \x01(\x03\x12\x0e\n\x06\x62iz_id\x18\x04 \x01(\x03\x12\x44\n\x08\x62iz_type\x18\x05 \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.PostPanelBizType\x12\x43\n\x0c\x63lick_button\x18\x06 \x01(\x0b\x32-.bilibili.community.service.dm.v1.ClickButton\x12?\n\ntext_input\x18\x07 \x01(\x0b\x32+.bilibili.community.service.dm.v1.TextInput\x12=\n\tcheck_box\x18\x08 \x01(\x0b\x32*.bilibili.community.service.dm.v1.CheckBox\x12\x36\n\x05toast\x18\t \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Toast\"\xad\x04\n\x0bPostPanelV2\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x44\n\x08\x62iz_type\x18\x03 \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.PostPanelBizType\x12\x45\n\x0c\x63lick_button\x18\x04 \x01(\x0b\x32/.bilibili.community.service.dm.v1.ClickButtonV2\x12\x41\n\ntext_input\x18\x05 \x01(\x0b\x32-.bilibili.community.service.dm.v1.TextInputV2\x12?\n\tcheck_box\x18\x06 \x01(\x0b\x32,.bilibili.community.service.dm.v1.CheckBoxV2\x12\x38\n\x05toast\x18\x07 \x01(\x0b\x32).bilibili.community.service.dm.v1.ToastV2\x12:\n\x06\x62ubble\x18\x08 \x01(\x0b\x32*.bilibili.community.service.dm.v1.BubbleV2\x12\x38\n\x05label\x18\t \x01(\x0b\x32).bilibili.community.service.dm.v1.LabelV2\x12\x41\n\x0bpost_status\x18\n \x01(\x0e\x32,.bilibili.community.service.dm.v1.PostStatus\"\x82\x02\n\x0b\x43lickButton\x12\x15\n\rportrait_text\x18\x01 \x03(\t\x12\x16\n\x0elandscape_text\x18\x02 \x03(\t\x12\x1b\n\x13portrait_text_focus\x18\x03 \x03(\t\x12\x1c\n\x14landscape_text_focus\x18\x04 \x03(\t\x12\x41\n\x0brender_type\x18\x05 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x0c\n\x04show\x18\x06 \x01(\x08\x12\x38\n\x06\x62ubble\x18\x07 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Bubble\"\xdd\x02\n\rClickButtonV2\x12\x15\n\rportrait_text\x18\x01 \x03(\t\x12\x16\n\x0elandscape_text\x18\x02 \x03(\t\x12\x1b\n\x13portrait_text_focus\x18\x03 \x03(\t\x12\x1c\n\x14landscape_text_focus\x18\x04 \x03(\t\x12\x41\n\x0brender_type\x18\x05 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x17\n\x0ftext_input_post\x18\x06 \x01(\x08\x12?\n\rexposure_once\x18\x07 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Bubble\x12\x45\n\rexposure_type\x18\x08 \x01(\x0e\x32..bilibili.community.service.dm.v1.ExposureType\"\xe8\x02\n\tTextInput\x12\x1c\n\x14portrait_placeholder\x18\x01 \x03(\t\x12\x1d\n\x15landscape_placeholder\x18\x02 \x03(\t\x12\x41\n\x0brender_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x18\n\x10placeholder_post\x18\x04 \x01(\x08\x12\x0c\n\x04show\x18\x05 \x01(\x08\x12\x38\n\x06\x61vatar\x18\x06 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Avatar\x12\x41\n\x0bpost_status\x18\x07 \x01(\x0e\x32,.bilibili.community.service.dm.v1.PostStatus\x12\x36\n\x05label\x18\x08 \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Label\"\xc1\x01\n\x0bTextInputV2\x12\x1c\n\x14portrait_placeholder\x18\x01 \x03(\t\x12\x1d\n\x15landscape_placeholder\x18\x02 \x03(\t\x12\x41\n\x0brender_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x18\n\x10placeholder_post\x18\x04 \x01(\x08\x12\x18\n\x10text_input_limit\x18\x06 \x01(\x05\"d\n\x06\x41vatar\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x41\n\x0b\x61vatar_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.AvatarType\"\'\n\x05Label\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\"\x87\x01\n\x07LabelV2\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\x12\x15\n\rexposure_once\x18\x03 \x01(\x08\x12\x45\n\rexposure_type\x18\x04 \x01(\x0e\x32..bilibili.community.service.dm.v1.ExposureType\"#\n\x06\x42ubble\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\xc6\x01\n\x08\x42ubbleV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x41\n\x0b\x62ubble_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.BubbleType\x12\x15\n\rexposure_once\x18\x04 \x01(\x08\x12\x45\n\rexposure_type\x18\x05 \x01(\x0e\x32..bilibili.community.service.dm.v1.ExposureType\"{\n\x08\x43heckBox\x12\x0c\n\x04text\x18\x01 \x01(\t\x12<\n\x04type\x18\x02 \x01(\x0e\x32..bilibili.community.service.dm.v1.CheckboxType\x12\x15\n\rdefault_value\x18\x03 \x01(\x08\x12\x0c\n\x04show\x18\x04 \x01(\x08\"o\n\nCheckBoxV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12<\n\x04type\x18\x02 \x01(\x0e\x32..bilibili.community.service.dm.v1.CheckboxType\x12\x15\n\rdefault_value\x18\x03 \x01(\x08\"o\n\x05Toast\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x0c\n\x04show\x18\x03 \x01(\x08\x12\x38\n\x06\x62utton\x18\x04 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Button\"s\n\x07ToastV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12H\n\x0ftoast_button_v2\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.ToastButtonV2\"b\n\rToastButtonV2\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x43\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x33.bilibili.community.service.dm.v1.ToastFunctionType\"&\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"F\n\x07\x41nyBody\x12;\n\x04\x62ody\x18\x01 \x01(\x0b\x32-.bilibili.community.service.dm.v1.typeAnyBody\"Y\n\nDmColorful\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.DmColorfulType\x12\x0b\n\x03src\x18\x02 \x01(\t\".\n\x0btypeAnyBody\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c*\xc1\x01\n\x10PostPanelBizType\x12\x18\n\x14PostPanelBizTypeNone\x10\x00\x12\x1d\n\x19PostPanelBizTypeEncourage\x10\x01\x12\x1b\n\x17PostPanelBizTypeColorDM\x10\x02\x12\x19\n\x15PostPanelBizTypeNFTDM\x10\x03\x12\x1d\n\x19PostPanelBizTypeFragClose\x10\x04\x12\x1d\n\x19PostPanelBizTypeRecommend\x10\x05*N\n\nRenderType\x12\x12\n\x0eRenderTypeNone\x10\x00\x12\x14\n\x10RenderTypeSingle\x10\x01\x12\x16\n\x12RenderTypeRotation\x10\x02*3\n\nAvatarType\x12\x12\n\x0e\x41vatarTypeNone\x10\x00\x12\x11\n\rAvatarTypeNFT\x10\x01*8\n\nPostStatus\x12\x14\n\x10PostStatusNormal\x10\x00\x12\x14\n\x10PostStatusClosed\x10\x01*Y\n\nBubbleType\x12\x12\n\x0e\x42ubbleTypeNone\x10\x00\x12\x19\n\x15\x42ubbleTypeClickButton\x10\x01\x12\x1c\n\x18\x42ubbleTypeDmSettingPanel\x10\x02*X\n\x0c\x43heckboxType\x12\x14\n\x10\x43heckboxTypeNone\x10\x00\x12\x19\n\x15\x43heckboxTypeEncourage\x10\x01\x12\x17\n\x13\x43heckboxTypeColorDM\x10\x02*N\n\x11ToastFunctionType\x12\x19\n\x15ToastFunctionTypeNone\x10\x00\x12\x1e\n\x1aToastFunctionTypePostPanel\x10\x01*?\n\x0cToastBizType\x12\x14\n\x10ToastBizTypeNone\x10\x00\x12\x19\n\x15ToastBizTypeEncourage\x10\x01*<\n\x0c\x45xposureType\x12\x14\n\x10\x45xposureTypeNone\x10\x00\x12\x16\n\x12\x45xposureTypeDMSend\x10\x01*5\n\x0e\x44mColorfulType\x12\x0c\n\x08NoneType\x10\x00\x12\x15\n\x0fVipGradualColor\x10\xe1\xd4\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'zzzz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._options = None
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_options = b'8\001'
  _globals['_POSTPANELBIZTYPE']._serialized_start=6201
  _globals['_POSTPANELBIZTYPE']._serialized_end=6394
  _globals['_RENDERTYPE']._serialized_start=6396
  _globals['_RENDERTYPE']._serialized_end=6474
  _globals['_AVATARTYPE']._serialized_start=6476
  _globals['_AVATARTYPE']._serialized_end=6527
  _globals['_POSTSTATUS']._serialized_start=6529
  _globals['_POSTSTATUS']._serialized_end=6585
  _globals['_BUBBLETYPE']._serialized_start=6587
  _globals['_BUBBLETYPE']._serialized_end=6676
  _globals['_CHECKBOXTYPE']._serialized_start=6678
  _globals['_CHECKBOXTYPE']._serialized_end=6766
  _globals['_TOASTFUNCTIONTYPE']._serialized_start=6768
  _globals['_TOASTFUNCTIONTYPE']._serialized_end=6846
  _globals['_TOASTBIZTYPE']._serialized_start=6848
  _globals['_TOASTBIZTYPE']._serialized_end=6911
  _globals['_EXPOSURETYPE']._serialized_start=6913
  _globals['_EXPOSURETYPE']._serialized_end=6973
  _globals['_DMCOLORFULTYPE']._serialized_start=6975
  _globals['_DMCOLORFULTYPE']._serialized_end=7028
  _globals['_DMSEGMOBILEREPLY']._serialized_start=49
  _globals['_DMSEGMOBILEREPLY']._serialized_end=292
  _globals['_DANMAKUELEM']._serialized_start=295
  _globals['_DANMAKUELEM']._serialized_end=843
  _globals['_DANMAKUAIFLAG']._serialized_start=845
  _globals['_DANMAKUAIFLAG']._serialized_end=925
  _globals['_DANMAKUFLAG']._serialized_start=927
  _globals['_DANMAKUFLAG']._serialized_end=968
  _globals['_DMWEBVIEWREPLY']._serialized_start=971
  _globals['_DMWEBVIEWREPLY']._serialized_end=1621
  _globals['_DMSEGCONFIG']._serialized_start=1623
  _globals['_DMSEGCONFIG']._serialized_end=1670
  _globals['_DANMAKUFLAGCONFIG']._serialized_start=1672
  _globals['_DANMAKUFLAGCONFIG']._serialized_end=1747
  _globals['_COMMANDDM']._serialized_start=1750
  _globals['_COMMANDDM']._serialized_end=1907
  _globals['_DANMUWEBPLAYERCONFIG']._serialized_start=1910
  _globals['_DANMUWEBPLAYERCONFIG']._serialized_end=2514
  _globals['_DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY']._serialized_start=2463
  _globals['_DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY']._serialized_end=2514
  _globals['_EXPRESSIONS']._serialized_start=2516
  _globals['_EXPRESSIONS']._serialized_end=2589
  _globals['_EXPRESSION']._serialized_start=2591
  _globals['_EXPRESSION']._serialized_end=2691
  _globals['_PERIOD']._serialized_start=2693
  _globals['_PERIOD']._serialized_end=2729
  _globals['_POSTPANEL']._serialized_start=2732
  _globals['_POSTPANEL']._serialized_end=3128
  _globals['_POSTPANELV2']._serialized_start=3131
  _globals['_POSTPANELV2']._serialized_end=3688
  _globals['_CLICKBUTTON']._serialized_start=3691
  _globals['_CLICKBUTTON']._serialized_end=3949
  _globals['_CLICKBUTTONV2']._serialized_start=3952
  _globals['_CLICKBUTTONV2']._serialized_end=4301
  _globals['_TEXTINPUT']._serialized_start=4304
  _globals['_TEXTINPUT']._serialized_end=4664
  _globals['_TEXTINPUTV2']._serialized_start=4667
  _globals['_TEXTINPUTV2']._serialized_end=4860
  _globals['_AVATAR']._serialized_start=4862
  _globals['_AVATAR']._serialized_end=4962
  _globals['_LABEL']._serialized_start=4964
  _globals['_LABEL']._serialized_end=5003
  _globals['_LABELV2']._serialized_start=5006
  _globals['_LABELV2']._serialized_end=5141
  _globals['_BUBBLE']._serialized_start=5143
  _globals['_BUBBLE']._serialized_end=5178
  _globals['_BUBBLEV2']._serialized_start=5181
  _globals['_BUBBLEV2']._serialized_end=5379
  _globals['_CHECKBOX']._serialized_start=5381
  _globals['_CHECKBOX']._serialized_end=5504
  _globals['_CHECKBOXV2']._serialized_start=5506
  _globals['_CHECKBOXV2']._serialized_end=5617
  _globals['_TOAST']._serialized_start=5619
  _globals['_TOAST']._serialized_end=5730
  _globals['_TOASTV2']._serialized_start=5732
  _globals['_TOASTV2']._serialized_end=5847
  _globals['_TOASTBUTTONV2']._serialized_start=5849
  _globals['_TOASTBUTTONV2']._serialized_end=5947
  _globals['_BUTTON']._serialized_start=5949
  _globals['_BUTTON']._serialized_end=5987
  _globals['_ANYBODY']._serialized_start=5989
  _globals['_ANYBODY']._serialized_end=6059
  _globals['_DMCOLORFUL']._serialized_start=6061
  _globals['_DMCOLORFUL']._serialized_end=6150
  _globals['_TYPEANYBODY']._serialized_start=6152
  _globals['_TYPEANYBODY']._serialized_end=6198
# @@protoc_insertion_point(module_scope)
