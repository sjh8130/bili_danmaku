# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x64m.proto\x12 bilibili.community.service.dm.v1\"d\n\x06\x41vatar\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x41\n\x0b\x61vatar_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.AvatarType\"#\n\x06\x42ubble\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"&\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"X\n\x0e\x42uzzwordConfig\x12\x46\n\x08keywords\x18\x01 \x03(\x0b\x32\x34.bilibili.community.service.dm.v1.BuzzwordShowConfig\"x\n\x12\x42uzzwordShowConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x03\x12\x13\n\x0b\x62uzzword_id\x18\x05 \x01(\x03\x12\x13\n\x0bschema_type\x18\x06 \x01(\x05\"{\n\x08\x43heckBox\x12\x0c\n\x04text\x18\x01 \x01(\t\x12<\n\x04type\x18\x02 \x01(\x0e\x32..bilibili.community.service.dm.v1.CheckboxType\x12\x15\n\rdefault_value\x18\x03 \x01(\x08\x12\x0c\n\x04show\x18\x04 \x01(\x08\"\x82\x02\n\x0b\x43lickButton\x12\x15\n\rportrait_text\x18\x01 \x03(\t\x12\x16\n\x0elandscape_text\x18\x02 \x03(\t\x12\x1b\n\x13portrait_text_focus\x18\x03 \x03(\t\x12\x1c\n\x14landscape_text_focus\x18\x04 \x03(\t\x12\x41\n\x0brender_type\x18\x05 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x0c\n\x04show\x18\x06 \x01(\x08\x12\x38\n\x06\x62ubble\x18\x07 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Bubble\"\xa1\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\r\n\x05idStr\x18\n \x01(\t\"P\n\rDanmakuAIFlag\x12?\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuFlag\"\x81\x03\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08progress\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x10\n\x08\x66ontsize\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\x0f\n\x07midHash\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\r\n\x05idStr\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\x12\x0f\n\x07usermid\x18\x0e \x01(\x04\x12\r\n\x05likes\x18\x0f \x01(\r\x12\x0e\n\x06test16\x18\x10 \x01(\x04\x12\x0e\n\x06test17\x18\x11 \x01(\x04\x12\x13\n\x0breply_count\x18\x12 \x01(\r\x12\x11\n\tuser_like\x18\x13 \x01(\r\x12\x0e\n\x06test20\x18\x14 \x01(\t\x12\x0e\n\x06test21\x18\x15 \x01(\t\x12\x11\n\tanimation\x18\x16 \x01(\t\x12\x0e\n\x06test23\x18\x17 \x01(\x0c\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"\xe4\x06\n\x18\x44\x61nmuDefaultPlayerConfig\x12)\n!player_danmaku_use_default_config\x18\x01 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12$\n\x1cinline_player_danmaku_switch\x18\x10 \x01(\x08\x12)\n!player_danmaku_senior_mode_switch\x18\x11 \x01(\x05\x12.\n&player_danmaku_ai_recommended_level_v2\x18\x12 \x01(\x05\x12\x98\x01\n*player_danmaku_ai_recommended_level_v2_map\x18\x13 \x03(\x0b\x32\x64.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig.PlayerDanmakuAiRecommendedLevelV2MapEntry\x1aK\n)PlayerDanmakuAiRecommendedLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x8f\x08\n\x11\x44\x61nmuPlayerConfig\x12\x1d\n\x15player_danmaku_switch\x18\x01 \x01(\x08\x12\"\n\x1aplayer_danmaku_switch_save\x18\x02 \x01(\x08\x12)\n!player_danmaku_use_default_config\x18\x03 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12&\n\x1eplayer_danmaku_enableblocklist\x18\x10 \x01(\x08\x12$\n\x1cinline_player_danmaku_switch\x18\x11 \x01(\x08\x12$\n\x1cinline_player_danmaku_config\x18\x12 \x01(\x05\x12&\n\x1eplayer_danmaku_ios_switch_save\x18\x13 \x01(\x05\x12)\n!player_danmaku_senior_mode_switch\x18\x14 \x01(\x05\x12.\n&player_danmaku_ai_recommended_level_v2\x18\x15 \x01(\x05\x12\x91\x01\n*player_danmaku_ai_recommended_level_v2_map\x18\x16 \x03(\x0b\x32].bilibili.community.service.dm.v1.DanmuPlayerConfig.PlayerDanmakuAiRecommendedLevelV2MapEntry\x1aK\n)PlayerDanmakuAiRecommendedLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"K\n\x18\x44\x61nmuPlayerDynamicConfig\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\"\xb1\x02\n\x15\x44\x61nmuPlayerViewConfig\x12\x61\n\x1d\x64\x61nmuku_default_player_config\x18\x01 \x01(\x0b\x32:.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig\x12R\n\x15\x64\x61nmuku_player_config\x18\x02 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmuPlayerConfig\x12\x61\n\x1d\x64\x61nmuku_player_dynamic_config\x18\x03 \x03(\x0b\x32:.bilibili.community.service.dm.v1.DanmuPlayerDynamicConfig\"\xd8\x04\n\x14\x44\x61nmuWebPlayerConfig\x12\x11\n\tdm_switch\x18\x01 \x01(\x08\x12\x11\n\tai_switch\x18\x02 \x01(\x08\x12\x10\n\x08\x61i_level\x18\x03 \x01(\x05\x12\x10\n\x08\x62locktop\x18\x04 \x01(\x08\x12\x13\n\x0b\x62lockscroll\x18\x05 \x01(\x08\x12\x13\n\x0b\x62lockbottom\x18\x06 \x01(\x08\x12\x12\n\nblockcolor\x18\x07 \x01(\x08\x12\x14\n\x0c\x62lockspecial\x18\x08 \x01(\x08\x12\x14\n\x0cpreventshade\x18\t \x01(\x08\x12\r\n\x05\x64mask\x18\n \x01(\x08\x12\x0f\n\x07opacity\x18\x0b \x01(\x02\x12\x0e\n\x06\x64marea\x18\x0c \x01(\x05\x12\x11\n\tspeedplus\x18\r \x01(\x02\x12\x10\n\x08\x66ontsize\x18\x0e \x01(\x02\x12\x12\n\nscreensync\x18\x0f \x01(\x08\x12\x11\n\tspeedsync\x18\x10 \x01(\x08\x12\x12\n\nfontfamily\x18\x11 \x01(\t\x12\x0c\n\x04\x62old\x18\x12 \x01(\x08\x12\x12\n\nfontborder\x18\x13 \x01(\x05\x12\x11\n\tdraw_type\x18\x14 \x01(\t\x12\x1a\n\x12senior_mode_switch\x18\x15 \x01(\x05\x12\x13\n\x0b\x61i_level_v2\x18\x16 \x01(\x05\x12\x61\n\x0f\x61i_level_v2_map\x18\x17 \x03(\x0b\x32H.bilibili.community.service.dm.v1.DanmuWebPlayerConfig.AiLevelV2MapEntry\x1a\x33\n\x11\x41iLevelV2MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"A\n\x0f\x44mExpoReportReq\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\r\n\x05spmid\x18\x04 \x01(\t\"\x11\n\x0f\x44mExpoReportRes\"\xe3\x0c\n\x11\x44mPlayerConfigReq\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x45\n\x06switch\x18\x02 \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuSwitch\x12N\n\x0bswitch_save\x18\x03 \x01(\x0b\x32\x39.bilibili.community.service.dm.v1.PlayerDanmakuSwitchSave\x12[\n\x12use_default_config\x18\x04 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuUseDefaultConfig\x12\x61\n\x15\x61i_recommended_switch\x18\x05 \x01(\x0b\x32\x42.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedSwitch\x12_\n\x14\x61i_recommended_level\x18\x06 \x01(\x0b\x32\x41.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevel\x12I\n\x08\x62locktop\x18\x07 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.PlayerDanmakuBlocktop\x12O\n\x0b\x62lockscroll\x18\x08 \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockscroll\x12O\n\x0b\x62lockbottom\x18\t \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockbottom\x12S\n\rblockcolorful\x18\n \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuBlockcolorful\x12O\n\x0b\x62lockrepeat\x18\x0b \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockrepeat\x12Q\n\x0c\x62lockspecial\x18\x0c \x01(\x0b\x32;.bilibili.community.service.dm.v1.PlayerDanmakuBlockspecial\x12G\n\x07opacity\x18\r \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.PlayerDanmakuOpacity\x12S\n\rscalingfactor\x18\x0e \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuScalingfactor\x12\x45\n\x06\x64omain\x18\x0f \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuDomain\x12\x43\n\x05speed\x18\x10 \x01(\x0b\x32\x34.bilibili.community.service.dm.v1.PlayerDanmakuSpeed\x12W\n\x0f\x65nableblocklist\x18\x11 \x01(\x0b\x32>.bilibili.community.service.dm.v1.PlayerDanmakuEnableblocklist\x12^\n\x19inlinePlayerDanmakuSwitch\x18\x12 \x01(\x0b\x32;.bilibili.community.service.dm.v1.InlinePlayerDanmakuSwitch\x12[\n\x12senior_mode_switch\x18\x13 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuSeniorModeSwitch\x12\x64\n\x17\x61i_recommended_level_v2\x18\x14 \x01(\x0b\x32\x43.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevelV2\"/\n\x0b\x44mSegConfig\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"\xa1\x01\n\x10\x44mSegMobileReply\x12<\n\x05\x65lems\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12@\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.DanmakuAIFlag\"\xa6\x01\n\x0e\x44mSegMobileReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\x12\x16\n\x0eteenagers_mode\x18\x05 \x01(\x05\x12\n\n\x02ps\x18\x06 \x01(\x03\x12\n\n\x02pe\x18\x07 \x01(\x03\x12\x11\n\tpull_mode\x18\x08 \x01(\x05\x12\x12\n\nfrom_scene\x18\t \x01(\x05\"]\n\rDmSegOttReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegOttReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"]\n\rDmSegSDKReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegSDKReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"\x9a\x06\n\x0b\x44mViewReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x39\n\x04mask\x18\x02 \x01(\x0b\x32+.bilibili.community.service.dm.v1.VideoMask\x12\x41\n\x08subtitle\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.VideoSubtitle\x12\x13\n\x0bspecial_dms\x18\x04 \x03(\t\x12\x44\n\x07\x61i_flag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12N\n\rplayer_config\x18\x06 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.DanmuPlayerViewConfig\x12\x16\n\x0esend_box_style\x18\x07 \x01(\x05\x12\r\n\x05\x61llow\x18\x08 \x01(\x08\x12\x11\n\tcheck_box\x18\t \x01(\t\x12\x1a\n\x12\x63heck_box_show_msg\x18\n \x01(\t\x12\x18\n\x10text_placeholder\x18\x0b \x01(\t\x12\x19\n\x11input_placeholder\x18\x0c \x01(\t\x12\x1d\n\x15report_filter_content\x18\r \x03(\t\x12\x41\n\x0b\x65xpo_report\x18\x0e \x01(\x0b\x32,.bilibili.community.service.dm.v1.ExpoReport\x12I\n\x0f\x62uzzword_config\x18\x0f \x01(\x0b\x32\x30.bilibili.community.service.dm.v1.BuzzwordConfig\x12\x42\n\x0b\x65xpressions\x18\x10 \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\x12?\n\npost_panel\x18\x11 \x03(\x0b\x32+.bilibili.community.service.dm.v1.PostPanel\x12\x15\n\ractivity_meta\x18\x12 \x03(\t\"X\n\tDmViewReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x14\n\x0cis_hard_boot\x18\x05 \x01(\x05\"\xc4\x04\n\x0e\x44mWebViewReply\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\ttext_side\x18\x03 \x01(\t\x12=\n\x06\x64m_sge\x18\x04 \x01(\x0b\x32-.bilibili.community.service.dm.v1.DmSegConfig\x12\x41\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12\x13\n\x0bspecial_dms\x18\x06 \x03(\t\x12\x11\n\tcheck_box\x18\x07 \x01(\x08\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12?\n\ncommandDms\x18\t \x03(\x0b\x32+.bilibili.community.service.dm.v1.CommandDm\x12M\n\rplayer_config\x18\n \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.DanmuWebPlayerConfig\x12\x1d\n\x15report_filter_content\x18\x0b \x03(\t\x12\x42\n\x0b\x65xpressions\x18\x0c \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\x12?\n\npost_panel\x18\r \x03(\x0b\x32+.bilibili.community.service.dm.v1.PostPanel\x12\x15\n\ractivity_meta\x18\x0e \x03(\t\"*\n\nExpoReport\x12\x1c\n\x14should_report_at_end\x18\x01 \x01(\x08\"d\n\nExpression\x12\x0f\n\x07keyword\x18\x01 \x03(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x38\n\x06period\x18\x03 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Period\"I\n\x0b\x45xpressions\x12:\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32,.bilibili.community.service.dm.v1.Expression\"\'\n\x05Label\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x03(\t\"$\n\x06Period\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"*\n\x19InlinePlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\"0\n\x1fPlayerDanmakuAiRecommendedLevel\x12\r\n\x05value\x18\x01 \x01(\x08\"2\n!PlayerDanmakuAiRecommendedLevelV2\x12\r\n\x05value\x18\x01 \x01(\x05\"1\n PlayerDanmakuAiRecommendedSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockbottom\x12\r\n\x05value\x18\x01 \x01(\x08\"+\n\x1aPlayerDanmakuBlockcolorful\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockrepeat\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockscroll\x12\r\n\x05value\x18\x01 \x01(\x08\"*\n\x19PlayerDanmakuBlockspecial\x12\r\n\x05value\x18\x01 \x01(\x08\"&\n\x15PlayerDanmakuBlocktop\x12\r\n\x05value\x18\x01 \x01(\x08\"$\n\x13PlayerDanmakuDomain\x12\r\n\x05value\x18\x01 \x01(\x02\"-\n\x1cPlayerDanmakuEnableblocklist\x12\r\n\x05value\x18\x01 \x01(\x08\"%\n\x14PlayerDanmakuOpacity\x12\r\n\x05value\x18\x01 \x01(\x02\"+\n\x1aPlayerDanmakuScalingfactor\x12\r\n\x05value\x18\x01 \x01(\x02\".\n\x1dPlayerDanmakuSeniorModeSwitch\x12\r\n\x05value\x18\x01 \x01(\x05\"#\n\x12PlayerDanmakuSpeed\x12\r\n\x05value\x18\x01 \x01(\x05\"7\n\x13PlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\x12\x11\n\tcanIgnore\x18\x02 \x01(\x08\"(\n\x17PlayerDanmakuSwitchSave\x12\r\n\x05value\x18\x01 \x01(\x08\".\n\x1dPlayerDanmakuUseDefaultConfig\x12\r\n\x05value\x18\x01 \x01(\x08\"\x8c\x03\n\tPostPanel\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x10\n\x08priority\x18\x03 \x01(\x03\x12\x0e\n\x06\x62iz_id\x18\x04 \x01(\x03\x12\x44\n\x08\x62iz_type\x18\x05 \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.PostPanelBizType\x12\x43\n\x0c\x63lick_button\x18\x06 \x01(\x0b\x32-.bilibili.community.service.dm.v1.ClickButton\x12?\n\ntext_input\x18\x07 \x01(\x0b\x32+.bilibili.community.service.dm.v1.TextInput\x12=\n\tcheck_box\x18\x08 \x01(\x0b\x32*.bilibili.community.service.dm.v1.CheckBox\x12\x36\n\x05toast\x18\t \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Toast\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xf9\x02\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\t\x12\x0b\n\x03lan\x18\x03 \x01(\t\x12\x0f\n\x07lan_doc\x18\x04 \x01(\t\x12\x14\n\x0csubtitle_url\x18\x05 \x01(\t\x12:\n\x06\x61uthor\x18\x06 \x01(\x0b\x32*.bilibili.community.service.dm.v1.UserInfo\x12<\n\x04type\x18\x07 \x01(\x0e\x32..bilibili.community.service.dm.v1.SubtitleType\x12\x15\n\rlan_doc_brief\x18\x08 \x01(\t\x12\x41\n\x07\x61i_type\x18\t \x01(\x0e\x32\x30.bilibili.community.service.dm.v1.SubtitleAiType\x12\x45\n\tai_status\x18\n \x01(\x0e\x32\x32.bilibili.community.service.dm.v1.SubtitleAiStatus\"\xe8\x02\n\tTextInput\x12\x1c\n\x14portrait_placeholder\x18\x01 \x03(\t\x12\x1d\n\x15landscape_placeholder\x18\x02 \x03(\t\x12\x41\n\x0brender_type\x18\x03 \x01(\x0e\x32,.bilibili.community.service.dm.v1.RenderType\x12\x18\n\x10placeholder_post\x18\x04 \x01(\x08\x12\x0c\n\x04show\x18\x05 \x01(\x08\x12\x38\n\x06\x61vatar\x18\x06 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Avatar\x12\x41\n\x0bpost_status\x18\x07 \x01(\x0e\x32,.bilibili.community.service.dm.v1.PostStatus\x12\x36\n\x05label\x18\x08 \x01(\x0b\x32\'.bilibili.community.service.dm.v1.Label\"o\n\x05Toast\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\x0c\n\x04show\x18\x03 \x01(\x08\x12\x38\n\x06\x62utton\x18\x04 \x01(\x0b\x32(.bilibili.community.service.dm.v1.Button\"\\\n\x08UserInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0c\n\x04rank\x18\x06 \x01(\x05\"S\n\tVideoMask\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04plat\x18\x02 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08mask_url\x18\x05 \x01(\t\"o\n\rVideoSubtitle\x12\x0b\n\x03lan\x18\x01 \x01(\t\x12\x0e\n\x06lanDoc\x18\x02 \x01(\t\x12\x41\n\tsubtitles\x18\x03 \x03(\x0b\x32..bilibili.community.service.dm.v1.SubtitleItem*3\n\nAvatarType\x12\x12\n\x0e\x41vatarTypeNone\x10\x00\x12\x11\n\rAvatarTypeNFT\x10\x01*X\n\x0c\x43heckboxType\x12\x14\n\x10\x43heckboxTypeNone\x10\x00\x12\x19\n\x15\x43heckboxTypeEncourage\x10\x01\x12\x17\n\x13\x43heckboxTypeColorDM\x10\x02*L\n\tDMAttrBit\x12\x14\n\x10\x44MAttrBitProtect\x10\x00\x12\x15\n\x11\x44MAttrBitFromLive\x10\x01\x12\x12\n\x0e\x44MAttrHighLike\x10\x02*\xc1\x01\n\x10PostPanelBizType\x12\x18\n\x14PostPanelBizTypeNone\x10\x00\x12\x1d\n\x19PostPanelBizTypeEncourage\x10\x01\x12\x1b\n\x17PostPanelBizTypeColorDM\x10\x02\x12\x19\n\x15PostPanelBizTypeNFTDM\x10\x03\x12\x1d\n\x19PostPanelBizTypeFragClose\x10\x04\x12\x1d\n\x19PostPanelBizTypeRecommend\x10\x05*8\n\nPostStatus\x12\x14\n\x10PostStatusNormal\x10\x00\x12\x14\n\x10PostStatusClosed\x10\x01*N\n\nRenderType\x12\x12\n\x0eRenderTypeNone\x10\x00\x12\x14\n\x10RenderTypeSingle\x10\x01\x12\x16\n\x12RenderTypeRotation\x10\x02*6\n\x10SubtitleAiStatus\x12\x08\n\x04None\x10\x00\x12\x0c\n\x08\x45xposure\x10\x01\x12\n\n\x06\x41ssist\x10\x02*+\n\x0eSubtitleAiType\x12\n\n\x06Normal\x10\x00\x12\r\n\tTranslate\x10\x01*\x1e\n\x0cSubtitleType\x12\x06\n\x02\x43\x43\x10\x00\x12\x06\n\x02\x41I\x10\x01*N\n\x11ToastFunctionType\x12\x19\n\x15ToastFunctionTypeNone\x10\x00\x12\x1e\n\x1aToastFunctionTypePostPanel\x10\x01\x32\xa0\x05\n\x02\x44M\x12s\n\x0b\x44mSegMobile\x12\x30.bilibili.community.service.dm.v1.DmSegMobileReq\x1a\x32.bilibili.community.service.dm.v1.DmSegMobileReply\x12\x64\n\x06\x44mView\x12+.bilibili.community.service.dm.v1.DmViewReq\x1a-.bilibili.community.service.dm.v1.DmViewReply\x12q\n\x0e\x44mPlayerConfig\x12\x33.bilibili.community.service.dm.v1.DmPlayerConfigReq\x1a*.bilibili.community.service.dm.v1.Response\x12j\n\x08\x44mSegOtt\x12-.bilibili.community.service.dm.v1.DmSegOttReq\x1a/.bilibili.community.service.dm.v1.DmSegOttReply\x12j\n\x08\x44mSegSDK\x12-.bilibili.community.service.dm.v1.DmSegSDKReq\x1a/.bilibili.community.service.dm.v1.DmSegSDKReply\x12t\n\x0c\x44mExpoReport\x12\x31.bilibili.community.service.dm.v1.DmExpoReportReq\x1a\x31.bilibili.community.service.dm.v1.DmExpoReportResb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._options = None
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_options = b'8\001'
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._options = None
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_options = b'8\001'
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._options = None
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_options = b'8\001'
  _AVATARTYPE._serialized_start=11146
  _AVATARTYPE._serialized_end=11197
  _CHECKBOXTYPE._serialized_start=11199
  _CHECKBOXTYPE._serialized_end=11287
  _DMATTRBIT._serialized_start=11289
  _DMATTRBIT._serialized_end=11365
  _POSTPANELBIZTYPE._serialized_start=11368
  _POSTPANELBIZTYPE._serialized_end=11561
  _POSTSTATUS._serialized_start=11563
  _POSTSTATUS._serialized_end=11619
  _RENDERTYPE._serialized_start=11621
  _RENDERTYPE._serialized_end=11699
  _SUBTITLEAISTATUS._serialized_start=11701
  _SUBTITLEAISTATUS._serialized_end=11755
  _SUBTITLEAITYPE._serialized_start=11757
  _SUBTITLEAITYPE._serialized_end=11800
  _SUBTITLETYPE._serialized_start=11802
  _SUBTITLETYPE._serialized_end=11832
  _TOASTFUNCTIONTYPE._serialized_start=11834
  _TOASTFUNCTIONTYPE._serialized_end=11912
  _AVATAR._serialized_start=46
  _AVATAR._serialized_end=146
  _BUBBLE._serialized_start=148
  _BUBBLE._serialized_end=183
  _BUTTON._serialized_start=185
  _BUTTON._serialized_end=223
  _BUZZWORDCONFIG._serialized_start=225
  _BUZZWORDCONFIG._serialized_end=313
  _BUZZWORDSHOWCONFIG._serialized_start=315
  _BUZZWORDSHOWCONFIG._serialized_end=435
  _CHECKBOX._serialized_start=437
  _CHECKBOX._serialized_end=560
  _CLICKBUTTON._serialized_start=563
  _CLICKBUTTON._serialized_end=821
  _COMMANDDM._serialized_start=824
  _COMMANDDM._serialized_end=985
  _DANMAKUAIFLAG._serialized_start=987
  _DANMAKUAIFLAG._serialized_end=1067
  _DANMAKUELEM._serialized_start=1070
  _DANMAKUELEM._serialized_end=1455
  _DANMAKUFLAG._serialized_start=1457
  _DANMAKUFLAG._serialized_end=1498
  _DANMAKUFLAGCONFIG._serialized_start=1500
  _DANMAKUFLAGCONFIG._serialized_end=1575
  _DANMUDEFAULTPLAYERCONFIG._serialized_start=1578
  _DANMUDEFAULTPLAYERCONFIG._serialized_end=2446
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_start=2371
  _DANMUDEFAULTPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_end=2446
  _DANMUPLAYERCONFIG._serialized_start=2449
  _DANMUPLAYERCONFIG._serialized_end=3488
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_start=2371
  _DANMUPLAYERCONFIG_PLAYERDANMAKUAIRECOMMENDEDLEVELV2MAPENTRY._serialized_end=2446
  _DANMUPLAYERDYNAMICCONFIG._serialized_start=3490
  _DANMUPLAYERDYNAMICCONFIG._serialized_end=3565
  _DANMUPLAYERVIEWCONFIG._serialized_start=3568
  _DANMUPLAYERVIEWCONFIG._serialized_end=3873
  _DANMUWEBPLAYERCONFIG._serialized_start=3876
  _DANMUWEBPLAYERCONFIG._serialized_end=4476
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_start=4425
  _DANMUWEBPLAYERCONFIG_AILEVELV2MAPENTRY._serialized_end=4476
  _DMEXPOREPORTREQ._serialized_start=4478
  _DMEXPOREPORTREQ._serialized_end=4543
  _DMEXPOREPORTRES._serialized_start=4545
  _DMEXPOREPORTRES._serialized_end=4562
  _DMPLAYERCONFIGREQ._serialized_start=4565
  _DMPLAYERCONFIGREQ._serialized_end=6200
  _DMSEGCONFIG._serialized_start=6202
  _DMSEGCONFIG._serialized_end=6249
  _DMSEGMOBILEREPLY._serialized_start=6252
  _DMSEGMOBILEREPLY._serialized_end=6413
  _DMSEGMOBILEREQ._serialized_start=6416
  _DMSEGMOBILEREQ._serialized_end=6582
  _DMSEGOTTREPLY._serialized_start=6584
  _DMSEGOTTREPLY._serialized_end=6677
  _DMSEGOTTREQ._serialized_start=6679
  _DMSEGOTTREQ._serialized_end=6755
  _DMSEGSDKREPLY._serialized_start=6757
  _DMSEGSDKREPLY._serialized_end=6850
  _DMSEGSDKREQ._serialized_start=6852
  _DMSEGSDKREQ._serialized_end=6928
  _DMVIEWREPLY._serialized_start=6931
  _DMVIEWREPLY._serialized_end=7725
  _DMVIEWREQ._serialized_start=7727
  _DMVIEWREQ._serialized_end=7815
  _DMWEBVIEWREPLY._serialized_start=7818
  _DMWEBVIEWREPLY._serialized_end=8398
  _EXPOREPORT._serialized_start=8400
  _EXPOREPORT._serialized_end=8442
  _EXPRESSION._serialized_start=8444
  _EXPRESSION._serialized_end=8544
  _EXPRESSIONS._serialized_start=8546
  _EXPRESSIONS._serialized_end=8619
  _LABEL._serialized_start=8621
  _LABEL._serialized_end=8660
  _PERIOD._serialized_start=8662
  _PERIOD._serialized_end=8698
  _INLINEPLAYERDANMAKUSWITCH._serialized_start=8700
  _INLINEPLAYERDANMAKUSWITCH._serialized_end=8742
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_start=8744
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_end=8792
  _PLAYERDANMAKUAIRECOMMENDEDLEVELV2._serialized_start=8794
  _PLAYERDANMAKUAIRECOMMENDEDLEVELV2._serialized_end=8844
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_start=8846
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_end=8895
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_start=8897
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_end=8938
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_start=8940
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_end=8983
  _PLAYERDANMAKUBLOCKREPEAT._serialized_start=8985
  _PLAYERDANMAKUBLOCKREPEAT._serialized_end=9026
  _PLAYERDANMAKUBLOCKSCROLL._serialized_start=9028
  _PLAYERDANMAKUBLOCKSCROLL._serialized_end=9069
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_start=9071
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_end=9113
  _PLAYERDANMAKUBLOCKTOP._serialized_start=9115
  _PLAYERDANMAKUBLOCKTOP._serialized_end=9153
  _PLAYERDANMAKUDOMAIN._serialized_start=9155
  _PLAYERDANMAKUDOMAIN._serialized_end=9191
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_start=9193
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_end=9238
  _PLAYERDANMAKUOPACITY._serialized_start=9240
  _PLAYERDANMAKUOPACITY._serialized_end=9277
  _PLAYERDANMAKUSCALINGFACTOR._serialized_start=9279
  _PLAYERDANMAKUSCALINGFACTOR._serialized_end=9322
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_start=9324
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_end=9370
  _PLAYERDANMAKUSPEED._serialized_start=9372
  _PLAYERDANMAKUSPEED._serialized_end=9407
  _PLAYERDANMAKUSWITCH._serialized_start=9409
  _PLAYERDANMAKUSWITCH._serialized_end=9464
  _PLAYERDANMAKUSWITCHSAVE._serialized_start=9466
  _PLAYERDANMAKUSWITCHSAVE._serialized_end=9506
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_start=9508
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_end=9554
  _POSTPANEL._serialized_start=9557
  _POSTPANEL._serialized_end=9953
  _RESPONSE._serialized_start=9955
  _RESPONSE._serialized_end=9996
  _SUBTITLEITEM._serialized_start=9999
  _SUBTITLEITEM._serialized_end=10376
  _TEXTINPUT._serialized_start=10379
  _TEXTINPUT._serialized_end=10739
  _TOAST._serialized_start=10741
  _TOAST._serialized_end=10852
  _USERINFO._serialized_start=10854
  _USERINFO._serialized_end=10946
  _VIDEOMASK._serialized_start=10948
  _VIDEOMASK._serialized_end=11031
  _VIDEOSUBTITLE._serialized_start=11033
  _VIDEOSUBTITLE._serialized_end=11144
  _DM._serialized_start=11915
  _DM._serialized_end=12587
# @@protoc_insertion_point(module_scope)
