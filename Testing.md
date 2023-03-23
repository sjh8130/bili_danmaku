#
[主站弹幕](#主站弹幕格式)
[直播弹幕](#直播弹幕格式)

## 主站弹幕格式
| id	| type		| protobuf-name	| -- |
| -:	| -:		| -				| - |
|  1	|  int64	| id			| 弹幕ID |
|  2	|  int32	| progress		| 弹幕出现时间（毫秒） |
|  3	|  int32	| mode			| 弹幕类型 |
|  4	|  int32	| fontsize		| 弹幕字号 |
|  5	| uint32	| color			| 弹幕颜色 RGB24 |
|  6	| string	| midHash		| 发送者mid hash (CRC32) |
|  7	| string	| content		| 弹幕内容 |
|  8	|  int64	| ctime			| 发送时间 |
|  9	|  int32	| weight		| 屏蔽等级 |
| 10	| string	| action		| `airborne:[time]`<br>`picture:图像url`(图片弹幕) |
| 11	|  int32	| pool			| 弹幕池 |
| 12	| string	| idStr			| 弹幕ID(string) |
| 13	|  int32	| attr			| 弹幕属性位 |
| 14	| ?int64	| usermid		| 发送者mid |
| 15	| ?int??	| *likes*		| 点赞数量 |
| 16	| ?int??	| ~~test16~~	| 弹幕回复，默认为num:0`first:2021-08-07` |
| 17	| ?int??	| ~~test17~~	| 弹幕回复，默认为num:0`last: 2022-09-05` |
| 18	| ?int??	| *reply_count*	| 弹幕回复数量 |
| 19	| ?			| ~~test19~~	| ? |
| 20	| string	| ~~test20~~	| 弹幕回复，默认为str:"0" |
| 21	| string	| ~~test21~~	| 弹幕回复，默认为str:"0" |
| 22	| string	| animation		| json |
| 23	| ?			| ~~test23~~	| ? |

### Danmaku__animation
| key				| type	| value		| |
| -					| -:	| -:		| - |
| id				| num	| 			| 20004: 图片弹幕<br>20016: ?<br>20018: NFT弹幕 |
| cid				| num	| 0			| |
| advanced_block	| num	| 0			| |
| animation_attr	| num	| 0			| first:2022-11-07 |
| mime				| str	| "image"	| |
| resource			| str	| **url**	| ohh、前方高能 图像 <br> NFT头像 |
| scale				| num	| 1			| id==20004 |

```json
// 图片弹幕
{
	"id": "110xxxxxxxxxxxxx632",
	"content": "[ohh]",
	"ctime": "1659xxxxxx",
	"weight": 10,	// 10
	"action": "picture:i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png?scale=1.00",
	"attr": 256,
	"animation": "{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png\",\"scale\":1}"
},
{
	"id":"113*************536",
	"content":"[前方高能]",
	"ctime":"1662******",
	"weight":10,	// 10
	"action":"picture:i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png?scale=1.00",
	"attr":256,
	"animation":"{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png\",\"scale\":1}"},

// NFT弹幕（仅移动端）
{
	"id":"113xxxxxxxxxxxxx240",
	"content":"好耶！",
	"ctime":"1661******",
	"attr":2048,
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxxxxxxx.png\"}"
},
{
	"id":"114*************240",
	"ctime":"1663******",
	"attr":2048,
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"animation_attr\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxxxxxxx.png\"}"
},
```

### commandDms
| name		| id	| type		| desc	|
| -			| -:	| -:		| -	|
| id		|  1	| int64		| 弹幕id |
| oid		|  2	| int64		| 视频cid |
| mid		|  3	| int64		| 发送者mid |
| command	|  4	| string	| #ACTORFOLLOW# 合作up主<br>#ATTENTION# 关注<br>#GRADE# 评分<br>#LINK# 链接<br>#RESERVE# 预约<br>#UP#<br>#VOTE# 投票 |
| content	|  5	| string	| 互动弹幕正文 |
| progress	|  6	| int32		| 出现时间 |
| ctime		|  7	| string	| 创建时间 yyyy-MM-dd HH:mm:ss |
| mtime		|  8	| string	| 发布时间 yyyy-MM-dd HH:mm:ss |
| extra		|  9	| string	| json |
| idStr		| 10	| string	| 弹幕id string |

#### command__类型
| command 7		| content	|
| -				| -			|
| #ACTORFOLLOW# | "合作up主" |
| #ATTENTION#	| "关注弹幕" |
| #GRADE#		| "哔瓣评分" |
| #LINK#		| **自定义内容** |
| #RESERVE#		| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#			| **自定义内容** |
| #VOTE#		| "投票弹幕" |

#### ACTORFOLLOW__合作up主
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_01] |
| mid					| num	| **合作up主 mid** |
| midstr				| str	| **合作up主 mid string** |
| face					| str	| **合作up主 头像 URL** |

#### ATTENTION__关注
| key					| type	| value | 备注 |
| -						| -		| -	| - |
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_02] |
| type					| num	| 2 |
| arc_type				| num	| 0 |

#### GRADE__评分
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| msg					| str	| "哔瓣评分" |
| skin					| num	| 1<br>2 |
| posX					| float	| |
| posY					| float	| |
| grade_id				| num	| id |
| duration				| num	| 5000? |
| icon					| str	| [url][url_03] |
| mid_score				| num	| |
| count					| num	| |
| avg_score				| float	| |
| skin_unselected		| str	| skin=1: [url][url_04]<br>skin=2: [url][url_05] |
| skin_selected			| str	| skin=1: [url][url_06]<br>skin=2: [url][url_07] |
| skin_font_color		| str	| color<br>skin=1: "`#FFB112`"<br>skin=2: "`#FA5555`" |
| summary_duration		| num	| 6000 |
| shrink_icon			| str	| [url][url_08] |
| shrink_title			| str	| "推荐" |
| show_status			| num	| 0 |

#### LINK__链接
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| aid					| num	| **目标视频avid** |
| title					| str	| **目标视频标题** |
| icon					| str	| [url][url_09] |
| bvid					| str	| **目标视频bvid** |
| posX					| float	| |
| posY					| float	| |
| arc_pic				| str	| **目标视频封面** |
| arc_duration			| num	| **目标视频时长** |
| shrink_icon			| str	| [url][url_10] |
| shrink_title			| str	| "视频" |
| show_status			| num	| 0 |
| duration				| num	| |
| arc_type				| num	| 0 |
| jump_url				| str	| "" |

#### RESERVE__预约
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| msg					| str	| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| reserve_type			| num	| 1: 视频<br>2: 直播 |
| reserve_id			| num	| id |
| live_stime			| num	| TimeStamp(秒) | `reserve_type=2` |
| arc_stime				| num	| TimeStamp(秒) | `reserve_type=2` |
| stime					| num	| TimeStamp(秒) | `reserve_type=2` |
| posX					| float	| |
| posY					| float	| |
| duration				| num	| 5000 |
| icon					| str	| [url][url_11] |
| reserve_count			| num	| **预约人数** |
| reserve_state			| num	| 1 |
| user_state			| bool 	| **预约状态** | 需要登录 |
| live_state			| num	| 0: <br> 1:直播中 <br> 2:直播结束 |
| premiere_state		| num	| 0 |
| live_popularity_count	| num	| 0 |
| live_popularity_str	| str	| 直播 :"`x.y万人气`" / "`x人看过`/ "`x.y万人看过`" |
| premiere_online_count	| num	| 0 |
| premiere_view			| num	| 0 |
| jump_url				| str	| **视频/直播回放 URL**<br>**直播间URL** |
| mid					| num	| **目标视频 UP主mid** |
| live_stime_format		| str	| 视频: ""<br>直播: "`(yyyy-)?MM-dd HH:mm`" / "`今天HH:mm`" |
| arc_stime_format		| str	| 视频: ""<br>直播: "`(yyyy-)?MM-dd HH:mm`" / "`今天HH:mm`" |
| stime_format			| str	| 视频: ""<br>直播: "`(yyyy-)?MM-dd HH:mm`" / "`今天HH:mm`" |
| live_lottery			| bool 	| `true` |
| desc					| str	| "" |
| shrink_icon			| str	| [url][url_12] |
| shrink_title			| str	| "预约" |
| show_status			| num	| 0 |

#### UP__带有【UP】的~~普通~~弹幕
| key					| type	| value	|
| -						| -		| -		|
| icon					| str	| **UP主头像URL** |

#### VOTE__投票
| key					| type	| value | 备注	|
| -						| -		| -		| -	|
| vote_id				| num	| id |
| question				| str	| **投票问题** |
| cnt					| num	| **投票人数** |
| options				| array	| **选项** |
| icon					| str	| [url][url_13] |
| my_vote				| num	| **我的选项** |
| pub_dynamic			| bool 	| |
| posX					| float	| |
| posY					| float	| |
| duration				| num	| |
| shrink_icon			| str	| [url][url_14] |
| shrink_title			| str	| "投票" |
| show_status			| num	| 0 |

##### VOTE__options
| key					| type	| value	|
| -						| -		| -		|
| idx					| num	| start:1 |
| desc					| str	| **选项内容** |
| cnt					| num	| 0? |
| has_self_def			| bool	| false? |

#### posX,posY
| key	| min		| max	|
| -		| -:		| -:	|
| posX	|	118		|	549	|
| posY	|	80.5	|	889	|

## 直播弹幕格式
~~最低发包间隔1ms~~
| link | name | desc |
|-|-|-|
| [link](#ACTIVITY_MATCH_GIFT)					| ACTIVITY_MATCH_GIFT					| |
| [link](#ANCHOR_LOT_CHECKSTATUS)				| ANCHOR_LOT_CHECKSTATUS				| 抽奖检查 |
| [link](#ANCHOR_LOT_START)						| ANCHOR_LOT_START						| 抽奖开始 |
| [link](#ANCHOR_LOT_END)						| ANCHOR_LOT_END						| 抽奖结束 |
| [link](#ANCHOR_LOT_AWARD)						| ANCHOR_LOT_AWARD						| 抽奖结果 |
| [link](#AREA_RANK_CHANGED)					| AREA_RANK_CHANGED						| |
| [link](#BOX_ACTIVITY_START)					| BOX_ACTIVITY_START					| |
| [link](#CHANGE_ROOM_INFO)						| CHANGE_ROOM_INFO						| WEB:更改直播间背景 |
| [link](#CHASE_FRAME_SWITCH)					| CHASE_FRAME_SWITCH					| |
| [link](#COMBO_SEND)							| COMBO_SEND							| 送礼物-连击 |
| [link](#COMMON_NOTICE_DANMAKU)				| COMMON_NOTICE_DANMAKU					| 弹幕区通知 |
| [link](#CUT_OFF)								| CUT_OFF								| 切断直播！|
| [link](#DANMU_AGGREGATION)					| DANMU_AGGREGATION						| 抽奖通知 |
| [link](#DANMU_GIFT_LOTTERY_AWARD)				| DANMU_GIFT_LOTTERY_AWARD				| |
| [link](#DANMU_GIFT_LOTTERY_END)				| DANMU_GIFT_LOTTERY_END				| |
| [link](#DANMU_GIFT_LOTTERY_START)				| DANMU_GIFT_LOTTERY_START				| |
| [link](#DANMU_MSG)							| DANMU_MSG								| 弹幕！ |
| [link](#DANMU_TAG_CHANGE)						| DANMU_TAG_CHANGE						| |
| [link](#DM_INTERACTION)						| DM_INTERACTION						| 弹幕 投票 |
| [link](#ENTRY_EFFECT)							| ENTRY_EFFECT							| 进入直播间特效 |
| [link](#ENTRY_EFFECT_MUST_RECEIVE)			| ENTRY_EFFECT_MUST_RECEIVE				| |
| [link](#FULL_SCREEN_SPECIAL_EFFECT)			| FULL_SCREEN_SPECIAL_EFFECT			| @ |
| [link](#GOTO_BUY_FLOW)						| GOTO_BUY_FLOW							| 移动端 购买* |
| [link](#GIFT_PANEL_PLAN)						| GIFT_PANEL_PLAN						| |
| [link](#GIFT_STAR_PROCESS)					| GIFT_STAR_PROCESS						| 礼物星球 进度|
| [link](#GUARD_ACHIEVEMENT_ROOM)				| GUARD_ACHIEVEMENT_ROOM				| |
| [link](#GUARD_BENEFIT_RECEIVE)				| GUARD_BENEFIT_RECEIVE					| |
| [link](#GUARD_BUY)							| GUARD_BUY								| 舰长购买 |
| [link](#GUARD_HONOR_THOUSAND)					| GUARD_HONOR_THOUSAND					| 千舰 |
| [link](#GUARD_LOTTERY_START)					| GUARD_LOTTERY_START					| |
| [link](#GUARD_WINDOWS_OPEN)					| GUARD_WINDOWS_OPEN					| |
| [link](#HOT_BUY_NUM)							| HOT_BUY_NUM							| 推广购物 |
| link											| ~~HOT_RANK_CHANGED~~					| [已移除][热门榜功能下线公告]|
| link											| ~~HOT_RANK_CHANGED_V2~~				| [已移除][热门榜功能下线公告]|
| link											| ~~HOT_RANK_SETTLEMENT~~				| [已移除][热门榜功能下线公告]|
| link											| ~~HOT_RANK_SETTLEMENT_V2~~			| [已移除][热门榜功能下线公告]|
| [link](#HOT_ROOM_NOTIFY)						| HOT_ROOM_NOTIFY						| ？ |
| [link](#HOUR_RANK_AWARDS)						| HOUR_RANK_AWARDS 						| |
| [link](#INTERACT_WORD)						| INTERACT_WORD							| 进入直播间/关注主播 |
| [link](#LIKE_INFO_V3_CLICK)					| LIKE_INFO_V3_CLICK					| 移动端 用户点赞|
| [link](#LIKE_INFO_V3_UPDATE)					| LIKE_INFO_V3_UPDATE					| 用户点赞更新 |
| [link](#LIKE_SO_HOT)							| LIKE_SO_HOT 							| |
| [link](#LITTLE_MESSAGE_BOX)					| LITTLE_MESSAGE_BOX					| |
| [link](#LITTLE_TIPS)							| LITTLE_TIPS 							| |
| [link](#LIVE)									| LIVE									| 开播 |
| [link](#LIVE_INTERACTIVE_GAME)				| LIVE_INTERACTIVE_GAME					| @ |
| [link](#LIVE_INTERNAL_ROOM_LOGIN)				| LIVE_INTERNAL_ROOM_LOGIN				| |
| [link](#LIVE_MULTI_VIEW_CHANGE)				| LIVE_MULTI_VIEW_CHANGE				| @ |
| [link](#LIVE_OPEN_PLATFORM_CLOUD_GAME)		| LIVE_OPEN_PLATFORM_CLOUD_GAME			| |
| [link](#LIVE_OPEN_PLATFORM_GAME)				| LIVE_OPEN_PLATFORM_GAME				| |
| [link](#LIVE_PLAYER_LOG_RECYCLE)				| LIVE_PLAYER_LOG_RECYCLE				| |
| [link](#LOL_ACTIVITY)							| LOL_ACTIVITY							| |
| [link](#MATCH_TEAM_GIFT_RANK)					| MATCH_TEAM_GIFT_RANK					| |
| [link](#MESSAGEBOX_USER_GAIN_MEDAL)			| MESSAGEBOX_USER_GAIN_MEDAL			| - |
| [link](#MESSAGEBOX_USER_MEDAL_CHANGE)			| MESSAGEBOX_USER_MEDAL_CHANGE			| - |
| [link](#MESSAGEBOX_USER_MEDAL_COMPENSATION)	| MESSAGEBOX_USER_MEDAL_COMPENSATION	| - |
| [link](#MILESTONE_UPDATE_EVENT)				| MILESTONE_UPDATE_EVENT 				| |
| [link](#MULTI_VOICE_STATUS_SYNC)				| MULTI_VOICE_STATUS_SYNC				| |
| [link](#NOTICE_MSG)							| NOTICE_MSG							| 滚动横幅 |
| [link](#ONLINE_RANK_COUNT)					| ONLINE_RANK_COUNT						| 高能用户 |
| [link](#ONLINE_RANK_TOP3)						| ONLINE_RANK_TOP3						| 高能用户前三恭喜 |
| [link](#ONLINE_RANK_V2)						| ONLINE_RANK_V2						| 高能用户TOP7 |
| [link](#PK_AGAIN)								| PK_AGAIN								| |
| [link](#PK_BATTLE_CRIT)						| PK_BATTLE_CRIT						| |
| [link](#PK_BATTLE_END)						| PK_BATTLE_END							| PK@ |
| [link](#PK_BATTLE_FINAL_PROCESS)				| PK_BATTLE_FINAL_PROCESS				| |
| [link](#PK_BATTLE_GIFT)						| PK_BATTLE_GIFT						| |
| [link](#PK_BATTLE_PRE_NEW)					| PK_BATTLE_PRE_NEW						| |
| [link](#PK_BATTLE_PRO_TYPE)					| PK_BATTLE_PRO_TYPE					| |
| [link](#PK_BATTLE_PROCESS_NEW)				| PK_BATTLE_PROCESS_NEW					| |
| [link](#PK_BATTLE_PUNISH_END)					| PK_BATTLE_PUNISH_END					| |
| [link](#PK_BATTLE_RANK_CHANGE)				| PK_BATTLE_RANK_CHANGE					| |
| [link](#PK_BATTLE_SETTLE_NEW)					| PK_BATTLE_SETTLE_NEW					| |
| [link](#PK_BATTLE_SETTLE_V2)					| PK_BATTLE_SETTLE_V2					| |
| [link](#PK_BATTLE_SPECIAL_GIFT)				| PK_BATTLE_SPECIAL_GIFT				| |
| [link](#PK_BATTLE_START_NEW)					| PK_BATTLE_START_NEW					| PK@ |
| [link](#PK_BATTLE_VIDEO_PUNISH_BEGIN)			| PK_BATTLE_VIDEO_PUNISH_BEGIN			| |
| [link](#PK_BATTLE_VIDEO_PUNISH_END)			| PK_BATTLE_VIDEO_PUNISH_END			| |
| [link](#PK_BATTLE_VOTES_ADD)					| PK_BATTLE_VOTES_ADD					| |
| [link](#PK_END)								| PK_END								| |
| [link](#PK_LOTTERY_START)						| PK_LOTTERY_START						| |
| [link](#PK_MATCH)								| PK_MATCH								| |
| [link](#PK_MIC_END)							| PK_MIC_END							| |
| [link](#PK_PRE)								| PK_PRE								| |
| [link](#PK_PROCESS)							| PK_PROCESS							| |
| [link](#PK_SETTLE)							| PK_SETTLE								| |
| [link](#PK_START)								| PK_START								| |
| [link](#PLAY_TAG)								| PLAY_TAG								| 比赛 事件 |
| [link](#PLAY_TOGETHER)						| PLAY_TOGETHER							| |
| [link](#POPULAR_RANK_CHANGED)					| POPULAR_RANK_CHANGED					| |
| [link](#POPULARITY_RED_POCKET_NEW)			| POPULARITY_RED_POCKET_NEW				| 人气红包 |
| [link](#POPULARITY_RED_POCKET_START)			| POPULARITY_RED_POCKET_START			| 人气红包 |
| [link](#POPULARITY_RED_POCKET_WINNER_LIST)	| POPULARITY_RED_POCKET_WINNER_LIST		| 人气红包 |
| [link](#PREPARING)							| PREPARING								| 下播/被下播 |
| [link](#RAFFLE_END)							| RAFFLE_END							| |
| [link](#RAFFLE_START)							| RAFFLE_START							| |
| [link](#RANK_REM)								| RANK_REM								| |
| [link](#RECOMMEND_CARD)						| RECOMMEND_CARD						| 主播推荐商品 |
| [link](#RED_POCKET_START)						| RED_POCKET_START						| |
| [link](#REENTER_LIVE_ROOM)					| REENTER_LIVE_ROOM						| |
| [link](#Revenue_PayLimit)						| Revenue_PayLimit						| |
| [link](#ROOM_BANNER)							| ROOM_BANNER							| |
| [link](#ROOM_BLOCK_INTO)						| ROOM_BLOCK_INTO						| |
| [link](#ROOM_BLOCK_MSG)						| ROOM_BLOCK_MSG						| 用户封禁 |
| [link](#ROOM_CHANGE)							| ROOM_CHANGE							| |
| [link](#ROOM_KICKOUT)							| ROOM_KICKOUT							| |
| [link](#ROOM_LIMIT)							| ROOM_LIMIT							| |
| [link](#ROOM_LOCK)							| ROOM_LOCK								| |
| [link](#ROOM_RANK)							| ROOM_RANK								| |
| [link](#ROOM_REAL_TIME_MESSAGE_UPDATE)		| ROOM_REAL_TIME_MESSAGE_UPDATE			| 当前粉丝团人数，关注人数 |
| [link](#ROOM_REFRESH)							| ROOM_REFRESH							| |
| [link](#ROOM_SILENT_OFF)						| ROOM_SILENT_OFF						| 取消直播间禁言 |
| [link](#ROOM_SILENT_ON)						| ROOM_SILENT_ON						| 开启直播间禁言 |
| [link](#ROOM_SKIN_MSG)						| ROOM_SKIN_MSG							| |
| [link](#SEND_GIFT)							| SEND_GIFT								| 送礼物 |
| [link](#SEND_GIFT_V2)							| SEND_GIFT_V2							| |
| [link](#SEND_TOP)								| SEND_TOP								| |
| [link](#SHOPPING_CART_SHOW)					| SHOPPING_CART_SHOW					| ？购物车 |
| [link](#SPECIAL_GIFT)							| SPECIAL_GIFT							| 特殊礼物 |
| [link](#STARLIVE_PK_MSG)						| STARLIVE_PK_MSG						| |
| [link](#STOP_LIVE_ROOM_LIST)					| STOP_LIVE_ROOM_LIST					| |
| [link](#SUPER_CHAT_AUDIT)						| SUPER_CHAT_AUDIT						| |
| [link](#SUPER_CHAT_ENTRANCE)					| SUPER_CHAT_ENTRANCE					| SuperChat@ |
| [link](#SUPER_CHAT_MESSAGE)					| SUPER_CHAT_MESSAGE					| SuperChat |
| [link](#SUPER_CHAT_MESSAGE_DELETE)			| SUPER_CHAT_MESSAGE_DELETE				| SuperChat 删除 |
| [link](#SUPER_CHAT_MESSAGE_JPN)				| SUPER_CHAT_MESSAGE_JPN				| SuperChat 日本語 |
| [link](#SYS_MSG)								| SYS_MSG								| @ |
| [link](#THERMAL_STORM_DANMU_BEGIN)			| THERMAL_STORM_DANMU_BEGIN				| |
| [link](#THERMAL_STORM_DANMU_CANCEL)			| THERMAL_STORM_DANMU_CANCEL			| |
| [link](#THERMAL_STORM_DANMU_OVER)				| THERMAL_STORM_DANMU_OVER				| |
| [link](#THERMAL_STORM_DANMU_UPDATE)			| THERMAL_STORM_DANMU_UPDATE			| |
| [link](#TRADING_SCORE)						| TRADING_SCORE							| @ |
| [link](#TV_END)								| TV_END								| |
| [link](#TV_START)								| TV_START								| |
| [link](#USER_PANEL_RED_ALARM)					| USER_PANEL_RED_ALARM					| |
| [link](#USER_TITLE_GET)						| USER_TITLE_GET						| |
| [link](#USER_TOAST_MSG)						| USER_TOAST_MSG						| |
| [link](#VIDEO_CONNECTION_JOIN_END)			| VIDEO_CONNECTION_JOIN_END				| |
| [link](#VIDEO_CONNECTION_JOIN_START)			| VIDEO_CONNECTION_JOIN_START			| |
| [link](#VIDEO_CONNECTION_MSG)					| VIDEO_CONNECTION_MSG					| |
| [link](#VOICE_JOIN_STATUS)					| VOICE_JOIN_STATUS						| 语音@ |
| [link](#VTR_GIFT_LOTTERY)						| VTR_GIFT_LOTTERY						| |
| [link](#WARNING)								| WARNING								| |
| [link](#WATCH_LPL_EXPIRED)					| WATCH_LPL_EXPIRED						| |
| [link](#WATCHED_CHANGE)						| WATCHED_CHANGE						| 观看人数 |
| [link](#WEB_REPORT_CONTROL)					| WEB_REPORT_CONTROL					| |
| [link](#WIDGET_BANNER)						| WIDGET_BANNER							| ？|
| [link](#WIDGET_GIFT_STAR_PROCESS)				| WIDGET_GIFT_STAR_PROCESS				| 礼物星球@ |
| [link](#WIN_ACTIVITY)							| WIN_ACTIVITY							| |
| [link](#WIN_ACTIVITY_USER)					| WIN_ACTIVITY_USER						| |

### WARNING
[TOP](#直播弹幕格式)  
`Anchor`
| key		| type	| value |
|-|-|-|
| cmd		| str	| "WARNING" |
| msg		| str	|  |
| roomid	| str	| 直播间id |
```json
"因版权原因，请立即调整"
"图片内容不适宜，请立即调整"
"禁止在直播间内展示平台外的评论、弹幕内容，请立即调整"
"违反直播分区规范，请立即更换至游戏区"
```

### LIVE
[TOP](#直播弹幕格式)  
开播
| key 7,8			| type	| value |
|-|-|-|
| cmd				| str	| "LIVE" |
| live_key			| str	| xxxx |
| voice_background	| str	| 仅音频直播_背景 |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |字符串拼接错误？
| live_platform		| str	| 开播方式 <br> "live_mng":? <br> "pc":PC <br> "pc_link":PC直播姬 <br> "ios_link": <br>"ios" |
| live_model		| num	| ? |
| live_time	*		| num	| 开播时间TimeStamp(秒) |
| roomid			| num	| 长_短直播间ID |
```json
1678276390438433{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1678276391","live_platform":"pc","live_model":0,"live_time":1678276391,"roomid":12345}
1678276420141264{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1678276391","live_platform":"pc","live_model":0,"roomid":12345}
1678629817.656{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1678629810","live_platform":"ios_link","live_model":4,"live_time":1678629810,"roomid":12345}
1678629817.657{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1678629810","live_platform":"ios_link","live_model":4,"roomid":12345}
1676034064.879{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","sub_session_key":"111111111111111111sub_time:1676034003","live_platform":"ios","live_model":3,"live_time":1676034003,"roomid":12345}
1678693610.423{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/b4414564939585e079b130765116bb34a46d9ee7.png","sub_session_key":"111111111111111111sub_time:1678693595","live_platform":"ios_link","live_model":3,"live_time":1678693595,"roomid":12345}
```

### SEND_GIFT
[TOP](#直播弹幕格式)  
送礼物
| key	| type | value |
|-|-|-|
| cmd	| str	| "SEND_GIFT" |
| data	| obj	| |
#### SEND_GIFT__data
| key 54				| type		| value | 备注 |
|-|-|-|-|
| action				| str		| "投喂" |
| **batch_combo_id**	| str		| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{时间TimeStamp.4f}"` <br> 盲盒:UUID4 |
| **batch_combo_send**	| null/obj	| [batch_combo_send](#SEND_GIFT__data__batch_combo_send) |
| beatId				| str		| ？"0" |
| biz_source			| str		| "Live" |
| **blind_gift**		| null/obj	| null |
| broadcast_id			| num		| 0 |
| coin_type				| str		| "gold"/"silver" |
| combo_resources_id	| num		| 1 |
| combo_send			| null/obj	| null |
| combo_stay_time		| num		| 3 |
| combo_total_coin		| num		| !!! |
| crit_prob				| num		| 0 |
| demarcation			| num		| 1,2 |
| discount_price		| num		| xxx |
| dmscore				| num		| 4*N |
| draw					| num		| 0 |
| effect				| num		| 0 |
| effect_block			| num		| 0 |
| face					| str		| 发送者 头像URL |
| face_effect_id		| num		| 0 |
| face_effect_type		| num		| 0 |
| float_sc_resource_id	| num		| 0 |
| giftId				| num		| 礼物ID |
| giftName				| str		| 礼物名称 |
| giftType				| num		| 礼物类型 |
| gold					| num		| 0 |
| guard_level			| num		| 舰长等级？ |
| is_first				| bool		|  |
| is_join_receiver		| bool		| false |
| is_naming				| bool		|  |
| is_special_batch		| num		| 0 |
| magnification			| float		| 0 |
| medal_info			| obj		| [粉丝牌信息](#粉丝牌信息medal_info) | 无 anchor_uname,anchor_roomid
| name_color			| str		| "" |
| num					| num		| 礼物数量 |
| original_gift_name	| str		| "" |
| price					| num		| 礼物价格,RMB*1000 |
| rcost					| num		| ？ |
| receive_user_info		| obj		| 接收者(主播)用户信息 |
| remain				| num		| 包裹剩余数量 |
| rnd					| str		| rnd=tid f"{礼物获取时间TimeStamp(毫秒)}{某id}"(13+6) |
| send_master			| null		| null |
| silver				| num		| 0 |
| super					| num		| 0 |
| super_batch_gift_num	| num		| 0 |
| super_gift_num		| num		| 0 |
| svga_block			| num		| 0 |
| switch				| bool		| true |
| tag_image				| str		| "" |
| tid					| str		| rnd=tid |
| timestamp				| num		| TimeStamp(秒) |
| top_list				| null		| null |
| total_coin			| num		| 礼物总价,RMB*1000 |
| uid					| num		| 发送者uid |
| uname					| str		| 发送者用户名 |
#### SEND_GIFT__data__batch_combo_send
| key 10				| type		| value |
|-|-|-|
| action				| str		| 与父级内容相同 |
| batch_combo_id		| str		| 与父级内容相同 |
| batch_combo_num		| num		|  |
| blind_gift			| null/obj	| 与父级内容相同 |
| giftId				| num		| 与父级内容相同 |
| giftName				| str		| 与父级内容相同 |
| gift_num				| num		| 礼物xx |
| send_master			| null		| 与父级内容相同 |
| uid					| num		| 与父级内容相同 |
| uname					| str		| 与父级内容相同 |
#### SEND_GIFT__data__combo_send
| key 9					| type		| value |
|-|-|-|
| action				| str		| 与父级内容相同 |
| combo_id				| str		| ？ |
| combo_num				| num		|  |
| giftId				| num		| 与父级内容相同 |
| giftName				| str		| 与父级内容相同 |
| gift_num				| num		| 礼物xx |
| send_master			| null		| 与父级内容相同 |
| uid					| num		| 与父级内容相同 |
| uname					| str		| 与父级内容相同 |
#### SEND_GIFT__data__receive_user_info
| key 2					| type		| value |
|-|-|-|
| uid					| num		| 接收者uid |
| uname					| str		| 接收者用户名 |
```json

```

### ONLINE_RANK_V2
[TOP](#直播弹幕格式)  
高能用户前七(左)，实时
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ONLINE_RANK_V2" |
| data	| obj	| |
#### ONLINE_RANK_V2__data
| key		| type			| value |
|-|-|-|
| list		| array(obj)	| _7_ |
| rank_type	| str			| "gold-rank" |
#### ONLINE_RANK_V2__data__list
| key 6			| type	| value |
|-|-|-|
| uid			| num | uid |
| face			| str | 头像URL |
| score			| str | 贡献值 |
| uname			| str | 用户名 |
| rank			| num | 排名(1-7) |
| guard_level	| num | 舰长等级 |
```json
1678200975.623{"cmd":"ONLINE_RANK_V2","data":{"list":[
	{"uid":1,"face":"https://i0.hdslb.com/bfs/face/xxx.jpg","score":"2420","uname":"xxx","rank":1,"guard_level":3},
	{"uid":2,"face":"https://i1.hdslb.com/bfs/face/xxx.jpg","score":"1410","uname":"xxx","rank":2,"guard_level":3},
	{"uid":3,"face":"http://i0.hdslb.com/bfs/face/xxx.jpg","score":"1391","uname":"xxx","rank":3,"guard_level":3},
	{"uid":4,"face":"https://i1.hdslb.com/bfs/face/xxx.jpg","score":"620","uname":"xxx","rank":4,"guard_level":3},
	{"uid":5,"face":"https://i0.hdslb.com/bfs/face/xxx.jpg","score":"620","uname":"xxx","rank":5,"guard_level":3},
	{"uid":6,"face":"https://i1.hdslb.com/bfs/face/xxx.jpg","score":"520","uname":"xxx","rank":6,"guard_level":0},
	{"uid":7,"face":"https://i0.hdslb.com/bfs/face/xxx.jpg","score":"361","uname":"xxx","rank":7,"guard_level":0}
],"rank_type":"gold-rank"}}
```

### ONLINE_RANK_TOP3
[TOP](#直播弹幕格式)  
高能用户前三(左)
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ONLINE_RANK_TOP3" |
| data	| obj	| |
#### ONLINE_RANK_TOP3__data
| key		| type			| value |
|-|-|-|
| dmscore	| num			| 112 |
| list		| array(obj)	| _1_ |
#### ONLINE_RANK_TOP3__data__list
| array 2		| type	| value |
|-|-|-|
| list[0]msg	| str	| `f"恭喜 <%{用户名}%> 成为高能用户"` |
| list[0]rank	| num	| 排名(1-3) |
```json
1677663535360194{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXXXX%> 成为高能用户","rank":2}]}}
1677663542127936{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXXXX%> 成为高能用户","rank":1}]}}
1677664832482642{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXXXX%> 成为高能用户","rank":3}]}}
```

### ONLINE_RANK_COUNT
[TOP](#直播弹幕格式)  
高能用户人数(观众人数)  
约每N*5秒发送一次
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ONLINE_RANK_COUNT" |
| data	| obj	| |
#### ONLINE_RANK_COUNT__data
| key	| type	| value |
|-|-|-|
| count | num	| 最大值约为10000[1-100xx] |
```json
1678282858171612{"cmd":"ONLINE_RANK_COUNT","data":{"count":10000}}
```

### INTERACT_WORD
[TOP](#直播弹幕格式)  
进入直播间、关注主播通知（高精度）500ms
| key | type	| value |
|-|-|-|
| cmd	| str	| "INTERACT_WORD" |
| data	| obj	| |
#### INTERACT_WORD__data
| key 18			| type	| value | |
|-|-|-|-|
| contribution		| obj	| ？[XXX](#INTERACT_WORD__data__contribution) |
| core_user_type	| num	| ?大部分为0[0-5] |~~钳钳~~
| dmscore			| num	| | 1 2 3 4 5 6 7 8 9 10 12 14 15 16 18 20 22 26 28 30 32 34 35 40 45 50 60 75
| fans_medal		| obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| identities		| array	| [identities](#others) |
| is_spread			| num	| 0,1 |
| msg_type			| num	| |
| privilege_type	| num	| [privilege_type](#others) is_spread==1:`0` |
| roomid			| num	| 长_短直播间ID |
| score				| num	| ? |
| spread_desc		| str	| is_spread==1:"流量包推广" |
| spread_info		| str	| is_spread==1:"#FF649E" |
| tail_icon			| num	| 0,101,102 |
| timestamp			| num	| TimeStamp(秒) |
| trigger_time		| num	| TimeStamp(皮秒)(100ps) |
| uid				| num	| 发送者uid |
| uname				| str	| 发送者 用户名 |
| uname_color		| str	| "" |
#### INTERACT_WORD__msg_type
[BACK](#INTERACT_WORD__data)
```js
t[t.Entry = 1] = "Entry",
t[t.Attention = 2] = "Attention",
t[t.Share = 3] = "Share",
t[t.SpecialAttention = 4] = "SpecialAttention",
t[t.MutualAttention = 5] = "MutualAttention",
t[t.Link = 6] = "Link"
"Entry:进入直播间"
"Entry:光临直播间"！舰长
e.createBehaviorElement = function(t) {
	var e,
	r,
	n = t.username,
	o = t.identity,
	i = t.nameColor,
	a = t.msgType,
	c = t.text,
	u = ((e = {})[L.Sv.Entry] = o < L.R$.GuardJian ? "进入" :"光临",
	e[L.Sv.Attention] = "关注了",
	e[L.Sv.Share] = "分享了",
	e[L.Sv.SpecialAttention] = "特别关注了",
	e[L.Sv.MutualAttention] = "互粉了",
	e[L.Sv.Link] = c,
	e),
	s = (0,C.H)(i),
	l = this.createElement("span","t-over-hidden interact-name v-middle",n,[["style","color:" + s + "; margin-right:4px;"]]),
	f = this.createElement("span","flex-no-shrink v-middle",u[a] + (a !== L.Sv.Link ? "直播间" :""),a > L.Sv.Entry && a !== L.Sv.Link ? [["style","color:#F7B500"]] :[["style","color: #999999"]]);
	if (t.icon) {
		var h = t.icon;
		r = this.createIcon(h,[["style","width: 13px;height: 13px; margin-left: 4px;"]])
	}
	return {
		name:l,
		desc:f,
		icon:r
	}
}
```
#### INTERACT_WORD__data__contribution
[BACK](#INTERACT_WORD__data)
| key	| type	| value |
|-|-|-|
| grade | num	| ？ |
```json
1678277503147255{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":34,"fans_medal":xxxx,"identities":[8,3,1],"is_spread":0,"msg_type":1,"privilege_type":1,"roomid":12345,"score":1728800893855,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1678277502,"trigger_time":1678277501785694700,"uid":12345,"uname":"xxx","uname_color":""}}
```

### WATCHED_CHANGE
[TOP](#直播弹幕格式)  
每5秒最多发送一次 用户(包括游客、主播)进入直播间时发送
| key	| type	| value |
|-|-|-|
| cmd	| str	| "WATCHED_CHANGE" |
| data	| obj	| |
#### WATCHED_CHANGE__data
| key 3			| type	| value |
|-|-|-|
| num			| num	| 人数 |
| text_small	| str	| str(num) <br> "x.y万" |
| text_large	| str	| f"num人看过" <br> "x.y万人看过" |
```json
1678629815790402{"cmd":"WATCHED_CHANGE","data":{"num":0,"text_small":"0","text_large":"0人看过"}}
1678360732205742{"cmd":"WATCHED_CHANGE","data":{"num":9994,"text_small":"9994","text_large":"9994人看过"}}
1679141284351458{"cmd":"WATCHED_CHANGE","data":{"num":10041,"text_small":"1.0万","text_large":"1.0万人看过"}}
1678413241620532{"cmd":"WATCHED_CHANGE","data":{"num":58869009,"text_small":"5886.9万","text_large":"5886.9万人看过"}}
```

### ROOM_REAL_TIME_MESSAGE_UPDATE
[TOP](#直播弹幕格式)  
(每N*60秒&数值更新)发送一次，更新关注数、粉丝团人数
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data	| obj	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE__data
| key 4			| type	| value |
|-|-|-|
| roomid		| num	| 长直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1? |
| fans_club		| num	| 粉丝团成员(活跃人数) |
```json
1678377704726163{"cmd":"ROOM_REAL_TIME_MESSAGE_UPDATE","data":{"roomid":123456,"fans":12345,"red_notice":-1,"fans_club":18692}}
```

### LIKE_INFO_V3_CLICK
[TOP](#直播弹幕格式)  
点赞(移动端 双击屏幕)，和`LIKE_INFO_V3_UPDATE`同时发送，实时&每5秒最多发送一次
| key	| type	| value |
|-|-|-|
| cmd	| str	| "LIKE_INFO_V3_CLICK" |
| data	| obj	| |
#### LIKE_INFO_V3_CLICK__data
| key 11			| type	| value |
|-|-|-|
| show_area			| num	| 0 <br> 1(30s) |
| msg_type			| num	| 6 |
| like_icon			| str	| [图标][img_16] |
| uid				| num	| uid |
| like_text			| str	| "为主播点赞了" |
| uname				| str	| 用户名 |
| uname_color		| str	| "" |
| identities		| array	| [identities](#others) |
| fans_medal		| obj	| [fans_medal](#粉丝牌信息medal_info) |
| contribution_info	| obj	| |
| dmscore			| num	| 20 |
#### LIKE_INFO_V3_CLICK__data__contribution_info
| key	| type	| value |
|-|-|-|
| grade	| num	| 0 |
```json
1677662530746955{"cmd":"LIKE_INFO_V3_CLICK","data":{"show_area":0,"msg_type":6,"like_icon":"https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png","uid":12345,"like_text":"为主播点赞了","uname":"NAME","uname_color":"","identities":[1],"fans_medal":xxx,"contribution_info":{"grade":0},"dmscore":20}}
```

### LIKE_INFO_V3_UPDATE
[TOP](#直播弹幕格式)  
点赞(移动端 双击屏幕)，和`LIKE_INFO_V3_CLICK`同时发送，实时&每5秒最多发送一次
| key	| type	| value |
|-|-|-|
| cmd	| str	| "LIKE_INFO_V3_UPDATE" |
| data	| obj	| |
#### LIKE_INFO_V3_UPDATE__data
| key			| type	| value |
|-|-|-|
| click_count	| num	| 点赞数量 |
```json
1678377737.645{"cmd":"LIKE_INFO_V3_UPDATE","data":{"click_count":59221}}
```

### HOT_ROOM_NOTIFY
[TOP](#直播弹幕格式)  
description
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_ROOM_NOTIFY" |
| data	| obj	| |
#### HOT_ROOM_NOTIFY__data
| key 4					| type | value |
| - | - | - |
| threshold				| num	| 10000 |
| ttl					| num	| 300 |
| exit_no_refresh		| num	| 1 |
| random_delay_req_v2	| array	|  |
#### HOT_ROOM_NOTIFY__data__random_delay_req_v2
| key	| type	| value |
| - | - | - |	
| path	| str	| |
| delay	| num	| |
```json
{"cmd":"HOT_ROOM_NOTIFY","data":{"threshold":10000,"ttl":300,"exit_no_refresh":1,"random_delay_req_v2":[{"path":"/live/getRoundPlayVideo","delay":10},{"path":"/xlive/web-room/v1/index/getOffLiveList","delay":120000}]}}
```

### ENTRY_EFFECT
[TOP](#直播弹幕格式)  
欢迎舰长进入直播间，高精度
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ENTRY_EFFECT" |
| data	| obj	| |
#### ENTRY_EFFECT__data
| key 28					| type | value | |
|-|-|-|-|
| id						| num	| |
| uid						| num	| uid |
| target_id					| num	| 主播uid |
| mock_effect				| num	| 0? |
| face						| str	| 头像URL |
| privilege_type			| num	| [privilege_type](#others) |
| copy_writing				| str	| `f"欢迎(舰长\|提督\|总督) <%{用户名}%> 进入直播间"` |限长7字符，省略号为`...`
| copy_color				| str	|  |
| highlight_color			| str	|  |
| priority					| num	| 1? |
| basemap_url				| str	| basemap_url=web_basemap_url |
| show_avatar				| num	| 1 |
| effective_time			| num	| effective_time=web_effective_time |
| web_basemap_url			| str	| basemap_url=web_basemap_url |
| web_effective_time		| num	| effective_time=web_effective_time |
| web_effect_close			| num	| |
| web_close_time			| num	| |
| business					| num	| |
| copy_writing_v2			| str	| `f"欢迎 <^icon^> <%{用户名}%> 进入直播间"`<br>`f"欢迎(提督\|舰长\|总督) <%{用户名}%> 进入直播间"`<br>`f"欢迎<%{用户名}%>进入直播间"`**无空格**<br>`f"欢迎 <^icon^> 舰长 <%{用户名}%> 进入直播间"`<br> |限长6字符，省略号为`…`
| icon_list					| array	|  |
| max_delay_time			| num	| 7 |
| trigger_time				| num	| TimeStamp(皮秒?) |
| identities				| num	| [identities](#others) |
| effect_silent_time		| float	| 0 |
| effective_time_new		| num	|  |
| web_dynamic_url_webp		| str	|  |
| web_dynamic_url_apng		| str	|  |
| mobile_dynamic_url_webp	| str	|  |
```json
{"cmd":"ENTRY_EFFECT","data":{"id":1,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":1,"copy_writing":"欢迎总督 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#423511","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","show_avatar":1,"effective_time":5,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","web_effective_time":5,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎总督 <%■■%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":8,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":2,"copy_writing":"欢迎提督 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 提督 <%■■%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":2,"copy_writing":"欢迎提督 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 提督 <%■■%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":2,"copy_writing":"欢迎提督 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎提督 <%■■%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":7,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":3,"copy_writing":"欢迎舰长 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%■■%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":3,"copy_writing":"欢迎舰长 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%■■%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":3,"copy_writing":"欢迎舰长 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%■■%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":3,"copy_writing":"欢迎舰长 <%■■%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎舰长 <%■■%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":135,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎 <%■■%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","show_avatar":1,"effective_time":1,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%■■%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":136,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎 <%■■%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%■■%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":136,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎 <%■■%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%■■%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":137,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎 <%■■%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%■■%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":137,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎 <%■■%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%■■%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":253,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎<%■■%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_effective_time":3,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%■■%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":1,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":253,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎<%■■%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_effective_time":3,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%■■%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":254,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎<%■■%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%■■%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":1,"effect_silent_time":0,"effective_time_new":3,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp"}}
{"cmd":"ENTRY_EFFECT","data":{"id":255,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎<%■■%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","show_avatar":1,"effective_time":5,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%■■%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":5,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp"}}
{"cmd":"ENTRY_EFFECT","data":{"id":333,"uid":12345,"target_id":12345,"mock_effect":0,"face":"https://iX.hdslb.com/bfs/face/XXXXX.jpg","privilege_type":0,"copy_writing":"欢迎<%■■%>进入直播间","copy_color":"#ffffff","highlight_color":"#fff596","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/00a132d170d94ad80509c8078f9714e27a852ece.png","show_avatar":1,"effective_time":4,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/00a132d170d94ad80509c8078f9714e27a852ece.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":2,"copy_writing_v2":"欢迎<%■■%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":8,"effect_silent_time":0,"effective_time_new":4,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/16e46ab8edc770ff673fa0703e9fba068db8ef18.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/fea83bbabefde666608596fcfe7f12e865ddbb3e.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/16e46ab8edc770ff673fa0703e9fba068db8ef18.webp"}}
```

### STOP_LIVE_ROOM_LIST
[TOP](#直播弹幕格式)  
每30秒发送一次~~(`HH:mm:29`,`HH:mm:59`)~~，推送很多[12,223]直播间ID?
| key	| type	| value |
|-|-|-|
| cmd	| str	| "STOP_LIVE_ROOM_LIST" |
| data	| obj	| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type	| value |
|-|-|-|
| room_id_list	| array	| [1,2,3,...] |

### GUARD_BUY
[TOP](#直播弹幕格式)  
舰长购买  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "GUARD_BUY" |
| data	| obj	| |
#### GUARD_BUY__data
| key 9			| type	| value |
|-|-|-|
| uid			| num	| uid |
| username		| str	| 用户名 |
| guard_level	| num	| [guard_level](#others) |
| num			| num	| 购买数量 |
| price			| num	| 单价 RMB*1000 |
| gift_id		| num	| 10003:"舰长" 10002:"提督" 10001:"总督" |
| gift_name		| str	|  |
| start_time	| num	| 购买时间 TimeStamp(秒) |
| end_time		| num	| 购买时间 TimeStamp(秒) |
```json
1677244873971786{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":3,"num":1,"price":198000,"gift_id":10003,"gift_name":"舰长","start_time":1677244875,"end_time":1677244875}}
1677244895969637{"cmd":"GUARD_BUY","data":{"uid":12334,"username":"xxx","guard_level":2,"num":1,"price":1998000,"gift_id":10002,"gift_name":"提督","start_time":1677244898,"end_time":1677244898}}
1678276859211683{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":1,"num":1,"price":19998000,"gift_id":10001,"gift_name":"总督","start_time":1678276859,"end_time":1678276859}}
```

### USER_TOAST_MSG
[TOP](#直播弹幕格式)  
舰长购买通知，实时，显示在聊天区
| key	| type	| value |
|-|-|-|
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG__data
| key 23				| type	| value |
|-|-|-|
| anchor_show			| bool	| true |
| color					| str	| 舰长:"#00D1F1" <br> 提督:"#E17AFF" <br> 总督:"#FF7C28" |
| dmscore				| num	| 舰长:90 提督:96 总督:102 |
| effect_id				| num	| 舰长:397 提督:398 总督:399 |
| end_time				| num	| TimeStamp(秒) |
| face_effect_id		| num	| 舰长:44 <br> 提督:43 <br> 总督:42 |
| gift_id				| num	| 舰长:10003<br> 提督:10002 <br> 总督:10001 |
| guard_level			| num	| [guard_level](#others) |
| is_show				| num	| 0 |
| num					| num	| 1? |
| op_type				| num	| 1: <br> 2: <br> 3: <br> 4: |
| payflow_id			| str	| 订单号(25) |
| price					| num	| RMB*1000 <br> 续费舰长138 <br> ?158 <br> 舰长198 <br> 提督1998 <br> 总督19998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| 舰长:590 <br> 提督:591 <br> 总督:592 |
| start_time			| num	| 购买时间 TimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播当前舰长数 |
| toast_msg				| str	| `f"<%{用户名}%> (自动)?续费了舰长"` <br> `f"<%{用户名}%> (开通\|续费)了(舰长\|提督\|总督)，今天是TA陪伴主播的第{xxx}天"` |
| uid					| num	| uid |
| unit					| str	| "月"? |
| user_show				| bool	| true |
| username				| str	| 用户名 |
```json
1678276849538877{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90,"effect_id":397,"end_time":1678276850,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":3,"payflow_id":"2303081958514902124940705","price":138000,"role_name":"舰长","room_effect_id":590,"start_time":1678276850,"svga_block":0,"target_guard_count":728,"toast_msg":"<%XXX%> 开通了舰长，今天是TA陪伴主播的第31天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
1678201235.575{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90,"effect_id":397,"end_time":1678201235,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"2303072300042342176961034","price":198000,"role_name":"舰长","room_effect_id":590,"start_time":1678201235,"svga_block":0,"target_guard_count":584,"toast_msg":"<%XXX%> 开通了舰长，今天是TA陪伴主播的第31天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
1678201569375848{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96,"effect_id":398,"end_time":1678201569,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"2303072305508472189992166","price":1598000,"role_name":"提督","room_effect_id":591,"start_time":1678201569,"svga_block":0,"target_guard_count":598,"toast_msg":"<%XXX%> 续费了提督，今天是TA陪伴主播的第1023天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
1678202425381497{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96,"effect_id":398,"end_time":1678202425,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"2303072320108582147357623","price":1998000,"role_name":"提督","room_effect_id":591,"start_time":1678202425,"svga_block":0,"target_guard_count":619,"toast_msg":"<%XXX%> 开通了提督，今天是TA陪伴主播的第61天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
1678276859218749{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1678276859,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":1,"payflow_id":"2303082000479852109045421","price":19998000,"role_name":"总督","room_effect_id":592,"start_time":1678276859,"svga_block":0,"target_guard_count":729,"toast_msg":"<%XXX%> 续费了总督，今天是TA陪伴主播的第12天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
```

### NOTICE_MSG
[TOP](#直播弹幕格式)  
滚动横幅
| key 17		| type	| value |
|-|-|-|
| cmd			| str	| "NOTICE_MSG" |
| id			| num	|  |
| name			| num	|  |
| full			| obj	|  |
| half			| obj	|  |
| side			| obj	|  |
| roomid		| num	| 长_短直播间ID |
| real_roomid	| num	| 长_短直播间ID |
| msg_common	| str	|  |
| msg_self		| str	|  |
| link_url		| str	| `f""` |
| msg_type		| num	|  |
| shield_uid	| num	|  |
| business_id	| str	|  |
| scatter		| obj	| |
| marquee_id	| str	| "" |
| notice_type	| num	| 0 |
#### NOTICE_MSG__full
| key			| type	| value |
|-|-|-|
| head_icon		| str	| |
| tail_icon		| str	| |
| head_icon_fa	| str	| |
| tail_icon_fa	| str	| |
| head_icon_fan	| str	| |
| tail_icon_fan	| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| time			| num	| |
#### NOTICE_MSG__half
| key			| type	| value |
|-|-|-|
| head_icon		| str	| |
| tail_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| time			| num	| |
#### NOTICE_MSG__side
| key			| type	| value |
|-|-|-|
| head_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| border		| str	| |
#### NOTICE_MSG__scatter
| key	| type | value |
|-|-|-|
| min	| num | 0 |
| max	| num | 0 |
#### NOTICE_MSG__例
```json
广播{"cmd":"NOTICE_MSG","id":1,"name":"全区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/b29add66421580c3e680d784a827202e512a40a0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/49869a52d6225a3e70bbf1f4da63f199a95384b2.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":24,"tail_icon_fan":4,"background":"#66A74EFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/ec9b374caec5bd84898f3780a10189be96b86d4e.png","tail_icon":"","background":"#85B971FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个浪漫城堡，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂<%{主播}%>X个浪漫城堡，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32132","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个次元之城，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个次元之城，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31087","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个鸿运小电视，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个鸿运小电视，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31115","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个超级战舰，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个超级战舰，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31483","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个点亮星辰，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个点亮星辰，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32455","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":207,"name":"舰长跑马灯","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#FFB03CFF","color":"#FFFFFFFF","highlight":"#B25AC1FF","time":10},"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},"side":{"head_icon":"https://i0.hdslb.com/bfs/live/21b524fcc316e6d438415607d5531ecc2bf9f4ff.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"","msg_self":"<%{用户}%> 自动续费了主播的 <%舰长%>","link_url":"","msg_type":3,"shield_uid":-1,"business_id":"","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":424,"name":"许愿-星际漫步","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/33ad76e469a1db66734c3a5f0d54206c12b96878.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","msg_self":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31168","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":424,"name":"许愿-星际漫步","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/33ad76e469a1db66734c3a5f0d54206c12b96878.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","msg_self":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31168","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":738,"name":"BLS任务1k秋","full":{"head_icon":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#b6272b","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon":"","background":"#b6272b","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"BLS限时任务：恭喜主播<%{主播}%>完成限时任务，直播间派发<%XX元%>红包，速抢手慢无！","msg_self":"BLS限时任务：恭喜主播<%{主播}%>完成限时任务，直播间派发<%XX元%>红包，速抢手慢无！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"-1","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
广播{"cmd":"NOTICE_MSG","id":742,"name":"3D小电视飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32122","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
广播{"cmd":"NOTICE_MSG","id":742,"name":"3D小电视飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32122","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":747,"name":"盲盒爆出广播","full":{"head_icon":"https://i0.hdslb.com/bfs/live/6a7222b0d186a1b05053a86f218ac5f2944c1dd1.gif","tail_icon":"","head_icon_fa":"https://i0.hdslb.com/bfs/live/6a7222b0d186a1b05053a86f218ac5f2944c1dd1.gif","tail_icon_fa":"","head_icon_fan":20,"tail_icon_fan":4,"background":"#F2538A","color":"#FFFFFF","highlight":"#FFE600","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/6a7222b0d186a1b05053a86f218ac5f2944c1dd1.gif","tail_icon":"","background":"#F2538A","color":"#FFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"","msg_self":"恭喜<%{用户}%>赠送盲盒爆出{礼物}！","link_url":"","msg_type":2,"shield_uid":-1,"business_id":"32131","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":755,"name":"【新】舰长跑马灯","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#FFB03CFF","color":"#FFFFFFFF","highlight":"#B25AC1FF","time":10},"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},"side":{"head_icon":"https://i0.hdslb.com/bfs/live/21b524fcc316e6d438415607d5531ecc2bf9f4ff.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"","msg_self":"<%{用户}%> 开通了舰长，今天是TA陪伴主播的第<%{DAY}%>天","link_url":"","msg_type":3,"shield_uid":-1,"business_id":"","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":756,"name":"【新】提督跑马灯","full":{"head_icon":"https://i0.hdslb.com/bfs/live/98f29d1e2735d0f4d30765c6ffa00e8d827422f3.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/98f29d1e2735d0f4d30765c6ffa00e8d827422f3.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#FFB03CFF","color":"#FFFFFFFF","highlight":"#B25AC1FF","time":10},"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},"side":{"head_icon":"https://i0.hdslb.com/bfs/live/98f29d1e2735d0f4d30765c6ffa00e8d827422f3.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"","msg_self":"<%{用户}%> 开通了提督，今天是TA陪伴主播的第<%{DAY}%>天","link_url":"","msg_type":3,"shield_uid":-1,"business_id":"","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":804,"name":"人气榜第一名","full":{"head_icon":"https://i0.hdslb.com/bfs/live/f74b09c7fb83123a0dd66c536b6d5b143d271b08.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/f74b09c7fb83123a0dd66c536b6d5b143d271b08.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#FFE6BD","color":"#9D5412","highlight":"#FF6933","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/f74b09c7fb83123a0dd66c536b6d5b143d271b08.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","background":"#FFE6BD","color":"#9D5412","highlight":"#FF6933","time":0},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"恭喜主播<%{主播}%>荣获上小时人气榜第<%{RANK}%>名！点击传送查看精彩内容！","msg_self":"恭喜主播<%{主播}%>荣获上小时人气榜第<%{RANK}%>名！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003","msg_type":1,"shield_uid":-1,"business_id":"","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":814,"name":"幻影飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#F09153","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon":"","background":"#F09153","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个幻影飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个幻影飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32356","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":814,"name":"幻影飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#F09153","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/08978f1721200e11328d1f7d6231b21bcca20488.gif","tail_icon":"","background":"#F09153","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个幻影飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个幻影飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32356","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":815,"name":"奇幻之城专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个奇幻之城，一起看绚烂烟花！","msg_self":"<%{用户}%>投喂<%{主播}%>X个奇幻之城，一起看绚烂烟花！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32361","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":815,"name":"奇幻之城专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/fe66c1ce6ca3fe53167ef0e82ea1317a0af0c4ba.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个奇幻之城，一起看绚烂烟花！","msg_self":"<%{用户}%>投喂<%{主播}%>X个奇幻之城，一起看绚烂烟花！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32361","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
```

### SUPER_CHAT_MESSAGE
[TOP](#直播弹幕格式)  
SuperChat
| key		| type	| value |
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 长_短直播间ID |
#### SUPER_CHAT_MESSAGE__data
| key 27					| type	| value |
|-|-|-|
| background_bottom_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_end		| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_start	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_icon			| str	| "" |
| background_image			| str	| "https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png" |
| background_price_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| color_point				| float	| 0.7 |
| dmscore					| num	| 8*N [16,24,48,56,64,72,80,112,120,128] |
| end_time					| num	| TimeStamp(秒) |
| gift						| obj	| |
| id						| num	| SC id |
| is_ranked					| num	| 1 |
| is_send_audit				| num	| 0,1 |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info):medal_color为`#RRGGBB` |
| message					| str	| SC 内容 |
| message_font_color		| str	| |
| message_trans				| str	| SC 日本語 翻译 |
| price						| num	| 价格 |
| rate						| num	| 1000 |
| start_time				| num	| TimeStamp(秒) |
| time						| num	| SC剩余时长(秒) |
| token						| str	| hex(64bit) |
| trans_mark				| num	| 是否翻译 |
| ts						| num	| TimeStamp(秒) |
| uid						| num	| uid |
| user_info					| obj	| |
#### SUPER_CHAT_MESSAGE__data__gift
| key						| type	| value |
|-|-|-|
| gift_id					| num	| 12000 |
| gift_name					| str	| "醒目留言" |
| num						| num	| 1 |
#### SUPER_CHAT_MESSAGE__data__user_info
| key 12					| type	| value |
|-|-|-|
| face						| str	| 头像(URL) |
| face_frame				| str	| 头像框(URL) |
| guard_level				| num	| [guard_level](#others) |
| is_main_vip				| num	| |
| is_svip					| num	| ?0 |
| is_vip					| num	| ?0 |
| level_color				| str	| |
| manager					| num	| 管理员？ |
| name_color				| str	| |
| title						| str	| [头衔](docs/头衔.md) |
| uname						| str	| 用户名 |
| user_level				| num	| 直播观众等级 |
#### SUPER_CHAT_MESSAGE__PriceTable
| price			| background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	| background_price_color	|
|-|-|-|-|-|-|-|-|
| 30-49.9		| #2A60B2					| #EDF5FF			| #405D85				| #3171D2					| #7497CD					| #A3F6FF				|
| 50-99.9		| #427D9E					| #DBFFFD			| #29718B				| #4EA4C5					| #7DA4BD					| #A3F6FF				|
| 100-499.9		| #E2B52B					| #FFF1C5			| #EEBE5C				| #EAB400					| #ECCF75					| #72110E				|
| 500-999.9		| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 1000-1999.9	| #E54D4D					| #FFE7E4			| #BD666A				| #F63C45					| #EE8B8B					| #FFE163				|
| 2000+			| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
```json

```

### SUPER_CHAT_MESSAGE_JPN
[TOP](#直播弹幕格式)  
SuperChat 日本語  
？某些主播的直播间会一直发送此包  
在`SUPER_CHAT_MESSAGE`后约`1100ms/1.1s`内发送  
由`百度翻译`提供翻译 Translated by `Baidu Translate`
| key		| type	| value |
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE_JPN" |
| data		| obj	| |
| roomid	| str	| str(长_短直播间ID) |
#### SUPER_CHAT_MESSAGE_JPN__data
| key 20					| type	| value |
|-|-|-|
| id						| str	| str(SUPER_CHAT_MESSAGE__data__id) |
| uid						| str	| str(SUPER_CHAT_MESSAGE__data__uid) |
| price						| num	| SC价格 |
| rate						| num	| 1000 |
| message					| str	| 原始SC内容 |
| message_jpn				| str	| 翻译后SC内容 |
| is_ranked					| num	| 0,1 |
| background_image			| str	|  |
| background_color			| str	|  |
| background_icon			| str	|  |
| background_price_color	| str	|  |
| background_bottom_color	| str	|  |
| ts						| num	| TimeStamp(秒) |
| token						| str	| 64bit |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info) 没有(guard_level,is_lighted,medal_color_border,medal_color_end,medal_color_start) |
| user_info					| obj	|  |
| time						| num	|  |
| start_time				| num	| TimeStamp(秒) |
| end_time					| num	| TimeStamp(秒) |
| gift						| obj	|  |
```json

```

### SUPER_CHAT_MESSAGE_DELETE
[TOP](#直播弹幕格式)  
SC 删除
| key	| type	| value |
|-|-|-|
| cmd	| str	| "SUPER_CHAT_MESSAGE_DELETE" |
| data	| obj	| |
#### SUPER_CHAT_MESSAGE_DELETE__data
| key		| type			| value |
|-|-|-|
| ids		| array(num)	| SC_id |
| roomid	| num			| 长_短直播间ID |
```json
1677663595387015{"cmd":"SUPER_CHAT_MESSAGE_DELETE","data":{"ids":[123]},"roomid":12345}
```

### DANMU_AGGREGATION
[TOP](#直播弹幕格式)  
抽奖通知，每秒最多更新一次，每个抽奖最多发送`max_time-1`个包
| key	| type	| value |
|-|-|-|
| cmd	| str	| "DANMU_AGGREGATION" |
| data	| obj	| |
#### DANMU_AGGREGATION__data
| key 11				| type	| value |
|-|-|-|
| activity_identity		| str	| 抽奖id |
| activity_source		| num	| 1:天选时刻 2:礼物红包 |
| aggregation_cycle		| num	| 1 |
| aggregation_icon		| str	| 天选时刻："https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png" <br> 礼物红包："https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png" |
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| dmscore				| num	| 144 |
| msg					| str	| 天选时刻：弹幕口令 <br><br> 礼物红包:<br>"老板大气！点点红包抽礼物"<br>"点点红包，关注主播抽礼物～"<br>"喜欢主播加关注，点点红包抽礼物"<br>"红包抽礼物，开启今日好运！"<br>"中奖喷雾！中奖喷雾！" |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间TimeStamp(秒) |
```json
1677092694519224{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":1,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png","aggregation_num":50,"broadcast_msg_type":0,"dmscore":144,"msg":"xxxxx","show_rows":1,"show_time":2,"timestamp":1677092694}}
1677076078660790{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":2,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png","aggregation_num":675,"broadcast_msg_type":0,"dmscore":144,"msg":"老板大气！点点红包抽礼物","show_rows":1,"show_time":2,"timestamp":1677076078}}
```

### SPECIAL_GIFT
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "SPECIAL_GIFT" |
| data	| obj	| |
#### SEND_GIFT__data
| key	| type	| value |
|-|-|-|
| 39	| obj	| |
#### SEND_GIFT__data__39
| key 2,7	| type	| value |
|-|-|-|
| action	| str	| (start|end) |
| content	| str	|  |
| hadJoin	| num	| 0 |
| id		| str,num	| start:str end:num |
| num		| num	| 1 |
| storm_gif	| str	| GIF图像 |
| time		| num	| 持续时间 |
```json
1678289880692202{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"可爱即正义~~","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
1678289902765839{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"end","id":123412341234}}}
1678289902767841{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"end","id":123412341234}}}
```

### GUARD_HONOR_THOUSAND
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "GUARD_HONOR_THOUSAND" |
| data	| obj	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type			| value |
|-|-|-|
| add	| array(num)	| 用户uid |
| del	| array(num)	| 用户uid |
```json
1677424079061622{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[2],"del":[]}}
1677424664711245{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[],"del":[2]}}
```

### ANCHOR_LOT_CHECKSTATUS
[TOP](#直播弹幕格式)  
抽奖(天选时刻)检查
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ANCHOR_LOT_CHECKSTATUS" |
| data	| obj	| |
#### ANCHOR_LOT_CHECKSTATUS__data
| key 3,5			| type	| value |
|-|-|-|
| id				| num	| 抽奖id |
| ?reject_danmu		| null	| ?null |
| ?reject_reason	| str	| 拒绝理由 |
| status			| num	| 4:通过 |
| uid				| num	| 主播uid |
```json
1678290707539857{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"由于奖品格式不合格,请仔细检查后再提交哦","status":5,"uid":12345}}
1678290940820456{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":234,"reject_danmu":null,"reject_reason":"","status":4,"uid":12345}}
```

### ANCHOR_LOT_START
[TOP](#直播弹幕格式)  
抽奖(天选时刻)开始
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ANCHOR_LOT_START" |
| data	| obj	| |
#### ANCHOR_LOT_START__data
| key 33			| type	| value |
|-|-|-|
| asset_icon		| str			| https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png |
| asset_icon_webp	| str			| https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp |
| award_image		| str			|  |
| award_name		| str			| 礼物名称 |
| award_num			| num			| 礼物数量[1,100] |
| award_type		| num			| 0 |
| cur_gift_num		| num			| 0 |
| current_time		| num			| 当前时间TimeStamp(秒) |
| danmu				| str			| 弹幕口令[0,15] |
| danmu_new			| array(obj)	| _1_ |
| danmu_type		| num			| `danmu_type:0 === this.danmuType ? "文案弹幕" :"表情弹幕"` |
| gift_id			| num			| 0 |
| gift_name			| str			| 礼物抽奖：抽奖条件 |
| gift_num			| num			| 礼物抽奖：数量 |
| gift_price		| num			| 礼物抽奖：礼物价格(RMB*1000) |
| goaway_time		| num			| 180? |
| goods_id			| num			|  |
| id				| num			| 抽奖id |
| is_broadcast		| num			| 1 |
| join_type			| num			| ？ |
| lot_status		| num			| [lot_status](#others) [0,1,2] |
| max_time			| num			| 开奖时间(60,300,600,900)秒 |
| require_text		| str			| "抽奖条件: 关注主播""至少成为主播的舰长/提督/总督" |
| require_type		| num			| 抽奖条件 1:礼物抽奖 2:粉丝勋章 3:大航海 ~~4:UL?~~ |
| require_value		| num			| [0,1]关注状态/[1,20]粉丝牌等级/[1,3]舰长等级 |
| room_id			| num			| 长_短直播间ID |
| send_gift_ensure	| num			| 0 |
| show_panel		| num			| 1 |
| start_dont_popup	| num			| 0 |
| status			| num			| 1 |
| time				| num			| 剩余时间(秒) |
| url				| str			| https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1 |
| web_url			| str			| https://live.bilibili.com/p/html/live-lottery/anchor-join.html |
#### ANCHOR_LOT_START__data__danmu_new
| array 3					| type	| value |
|-|-|-|
| danmu_new[0].danmu		| str	| 弹幕口令[0,15] |
| danmu_new[0].danmu_view	| str	|  |
| danmu_new[0].reject		| bool	|  |
```json
1678278743694174{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":5,"award_type":0,"cur_gift_num":0,"current_time":1678278743,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":300,"require_text":"当前主播粉丝勋章至少1级","require_type":2,"require_value":1,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":299,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}
1677240452378006{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1677240452,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":60,"require_text":"关注主播 +XXXX","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":59,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}
1678279299938599{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":2,"award_type":0,"cur_gift_num":0,"current_time":1678279299,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":300,"require_text":"至少成为主播的舰长","require_type":3,"require_value":3,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":299,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}

```

### ANCHOR_LOT_END
[TOP](#直播弹幕格式)  
抽奖(天选时刻)结束
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ANCHOR_LOT_END" |
| data	| obj	| |
#### ANCHOR_LOT_END__data
| key	| type	| value |
|-|-|-|
| id	| num	| 抽奖id |
```json
1676986894998959{"cmd":"ANCHOR_LOT_END","data":{"id":12345}}
```

### ANCHOR_LOT_AWARD
[TOP](#直播弹幕格式)  
抽奖(天选时刻) 中奖名单，在`ANCHOR_LOT_END`后约`1~180ms`
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ANCHOR_LOT_AWARD" |
| data	| obj	| |
#### ANCHOR_LOT_AWARD__data
| key 10			| type	| value |
|-|-|-|
| award_dont_popup	| num			| 1 |
| award_image		| str			| 奖品图像？ |
| award_name		| str			| 奖品名称 |
| award_num			| num			| 1 |
| award_type		| num			| 0 |
| award_users		| array(obj)	| 中奖用户 |
| id				| num			| 抽奖id |
| lot_status		| num			| [lot_status](#others) 2 |
| url				| str			| https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1 |
| web_url			| str			| "https://live.bilibili.com/p/html/live-lottery/anchor-join.html" |
#### ANCHOR_LOT_AWARD__data__award_users
| key 6	| type	| value |
|-|-|-|
| uid	| num	| uid |
| uname	| num	| 用户名 |
| face	| num	| 头像URL |
| level	| num	| 直播观众等级 UL |
| color	| num	| 直播观众等级_颜色 num(RGB24) |
| num	| num	| 数量 |
```json
1677092990102391{
	"cmd": "ANCHOR_LOT_AWARD",
	"data": {
		"award_dont_popup": 1,
		"award_image": "",
		"award_name": "xxxxx",
		"award_num": 1,
		"award_type": 0,
		"award_users": [
			{"uid":1,"uname":"A","face":"https://i0.hdslb.com/bfs/face/XXX.jpg","level": 11,"color": 6406234,"num":1},
			{"uid":2,"uname":"B","face":"http://i0.hdslb.com/bfs/baselabs/XXX.png","level": 21,"color": 5805790,"num":1},
			{"uid":3,"uname":"C","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","level": 11,"color": 6406234,"num":1},
			{"uid":4,"uname":"D","face":"https://i0.hdslb.com/bfs/face/XXX.jpg","level": 15,"color": 6406234,"num":1},
			{"uid":5,"uname":"E","face":"https://i1.hdslb.com/bfs/face/XXX.jpg","level": 12,"color": 6406234,"num":1},
			{"uid":6,"uname":"F","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","level": 9,"color": 9868950,"num":1},
			{"uid":7,"uname":"G","face":"https://i1.hdslb.com/bfs/face/XXX.jpg","level": 24,"color": 5805790,"num":1},
			{"uid":8,"uname":"H","face":"https://i0.hdslb.com/bfs/face/member/noface.jpg","level": 0,"color": 9868950,"num":1},
			{"uid":9,"uname":"I","face":"http://i0.hdslb.com/bfs/face/XXX.jpg","level": 21,"color": 5805790,"num":1},
			{"uid":0,"uname":"J","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","level": 10,"color": 9868950,"num":1}
		],
		"id": 12345,
		"lot_status": 2,
		"url": "https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url": "https://live.bilibili.com/p/html/live-lottery/anchor-join.html"
	}
}
```

### POPULAR_RANK_CHANGED
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "POPULAR_RANK_CHANGED" |
| data	| obj	| |
#### POPULAR_RANK_CHANGED__data
| key		| type	| value |
|-|-|-|
| uid		| num	| 主播uid |
| rank		| num	| [0-100] |
| countdown	| num	| [0,3600] |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| cache_key	| str	| `f"rank_change:{hex_256bit}"` |
```json
1678204526721102{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":12345,"rank":25,"countdown":275,"timestamp":1678204526,"cache_key":"rank_change:5566ddf515314299b0035ff169bbb4c6"}}
1678204625704025{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":12345,"rank":24,"countdown":176,"timestamp":1678204625,"cache_key":"rank_change:c73af03a143d47dcae79474b3b298f10"}}
```

### PREPARING
[TOP](#直播弹幕格式)  
结束直播
| key		| type	| value |
|-|-|-|
| cmd		| str	| "PREPARING" |
| round *	| num	| 1 下播后轮播 |
| roomid	| str	| 长_短直播间ID |
```json
1677666669650062{"cmd":"PREPARING","roomid":"123"}
1678284426205970{"cmd":"PREPARING","round":1,"roomid":"12345"}
```

### DANMU_MSG
[TOP](#直播弹幕格式)  
弹幕！
| key	| type	| value |
|-|-|-|
| cmd	| str	| "DANMU_MSG" |
| info	| array	| |
| dm_v2	| str	| base64(proto) UTF-8 [define](#danmu_msg__dm_v2) |
#### DANMU_MSG__info
| array	| type	| value |  |
|-|-|-|-|
| 0		| array	| [弹幕属性](#DANMU_MSG__info__0) |
| 1		| str	| `text/content` <br> 弹幕内容/表情包名称 |
| 2		| array	| `userInfo`用户主站信息 | "https://account.bilibili.com/account/home"
| 3		| array	| `fansMedal`[粉丝牌](#DANMU_MSG__info__3) | "https://link.bilibili.com/p/center/index#/user-center/wearing-center/my-medal"
| 4		| array	| `user_level`[用户直播区信息](#DANMU_MSG__info__4) | "https://link.bilibili.com/p/center/index#/user-center/my-info/operation"
| 5		| array	| `title` [头衔](docs/头衔.md) |
| 6		| num	| ？0 |
| 7		| num	| `guardLevel`[舰长等级](#others) |
| 8		| null	| ？ |
| 9		| obj	| [`validation`](#DANMU_MSG__info__9) |
| 10	| num	| ?0 |
| 11	| num	| ?0 |
| 12	| null	| ？null |
| 13	| null	| ？null |
| 14	| num	| `lpl` |
| 15	| num	| 7*N |7:5932 14:2130 21:3134 28:1575 35:4418 42:4236 49:6731 56:4400 63:3991 70:4223 77:18 105:9546 112:408 210:主播
#### DANMU_MSG__info__0
| array	| type		| value |  |
|-|-|-|-|
| 0[0]	| num		| ？0 |
| 0[1]	| num		| 弹幕位置 |
| 0[2]	| num		| 25 弹幕字体大小 |
| 0[3]	| num		| 弹幕颜色 |
| 0[4]	| num		| TimeStamp(毫秒) |
| 0[5]	| num		| `dmid` **RANDOM**/天选时刻 为 0 |浏览器网页端：进入直播间时间TimeStamp(秒) iOS/Android:随机 BOT:当前时间TimeStamp(秒)
| 0[6]	| num		| 0? |
| 0[7]	| str		| HEX:crc32(uid) |
| 0[8]	| num		| ? |
| 0[9]	| num		| `type` ? [0,1,2,7] | 1:节奏风暴 2:天选时刻
| 0[10]	| num		| `chatBubbleType` |
| 0[11]	| str		| `chatBubbleColor` <br> 5:`"#1453BAFF,#4C2263A2,#3353BAFF"` <br> 2:`"#1453BAFF,#4C2263A2,#3353BAFF"` |
| 0[12]	| num		| `DmType` <br> 0:文本 <br> 1:表情包 <br> 2:语音 |
| 0[13]	| obj/str	| 表情包时：[`emoticonOptions`](#DANMU_MSG__info__0__13) <br> 其他:`"{}"` |
| 0[14]	| obj/str	| [`voiceConfig`](#DANMU_MSG__info__0__14) `"{}"` |
| 0[15]	| obj 		| [`emoticons`](#DANMU_MSG__info__0__15) |
| 0[16]	| obj 		| [goto](#DANMU_MSG__info__0__16) |20230119
#### DANMU_MSG__info__2
| array	| type	| value |  |
|-|-|-|-|
| 2[0]	| num	| `uid` 用户uid |
| 2[1]	| str	| `username` 用户名 |
| 2[2]	| num	| `isAdmin` 房管 |
| 2[3]	| num	| `isSvip` |
| 2[4]	| num	| `isSvip` |
| 2[5]	| num	| `rank` ？10000 LV0:5000 |
| 2[6]	| num	| `verify` bool |https://s1.hdslb.com/bfs/blive-engineer/live-web-player/room-player.min.js
| 2[7]	| str	| `usernameColor` <br> 舰长:`"#00D1F1"` <br> 提督:`"#E17AFF"` |
#### DANMU_MSG__info__3
| array	| type	| value |
|-|-|-|
| 3[0]	| num	| `level` 粉丝牌 等级 |
| 3[1]	| str	| `label` 粉丝团 称号 |
| 3[2]	| num	| `anchorUsername` 主播 用户名 |
| 3[3]	| num	| `shortRoomID` 短直播间ID |
| 3[4]	| num	| [`medalColor`](#medal_color) |
| 3[5]	| str	| `special` "" |
| 3[6]	| num	| `iconId` 0 |
| 3[7]	| num	| [`medalColorBorder`](#medal_color) |
| 3[8]	| num	| [`medalColorStart`](#medal_color) |
| 3[9]	| num	| [`medalColorEnd`](#medal_color) |
| 3[10]	| num	| [`guardLevel`](#others) 舰长等级 |
| 3[11]	| num	| [`isLight`](#粉丝牌信息medal_info) |
| 3[12]	| num	| `anchorId` 主播uid |
#### DANMU_MSG__info__4
user_level
| array	| type		| value | 备注 |
|-|-|-|-|
| 4[0]	| num		| `userLevel` 用户UL等级 |
| 4[1]	| num		| ？0 |
| 4[2]	| num		| UL等级 颜色 |
| 4[3]	| str/num	| `rank` 直播 用户排名|">50000"
| 4[4]	| num		| ? [0,1,2,3] |
#### DANMU_MSG__info__5
| array	| type	| value |
|-|-|-|
| 5[0]	| str	| identification |
| 5[1]	| str	| identification `title` |
#### DANMU_MSG__info__9
validation/checkInfo
| key	| type	| value |
|-|-|-|
| ts	| num	| TimeStamp(秒) |
| ct	| str	| 64bit |
#### DANMU_MSG__info__0__13
| key				| type	| value |
|-|-|-|
| bulge_display		| num	| 0,1 |
| emoticon_unique	| str	| 表情包id |
| height			| num	| 高 |
| in_player_area	| num	| 0,1 |
| is_dynamic		| num	| 0,1 |
| url				| str	| 表情包URL |
| width				| num	| 宽 |
#### DANMU_MSG__info__0__14
| key				| type	| value |
|-|-|-|
| file_duration		| num	|  |
| file_format		| str	|  |
| file_id			| str	|  |
| text				| str	|  |
| voice_url			| str	|  |
#### DANMU_MSG__info__0__15
| key				| type	| value |
|-|-|-|
| mode				| num	| 0 |
| show_player_type	| num	| 0 |
| extra				| str	| [json](#DANMU_MSG__info__0_15__extra) |
#### DANMU_MSG__info__0__15__extra
| key						| type		| value |  |
|-|-|-|-|
| send_from_me				| bool		| false |
| mode						| num		| 0 |
| color						| num		| 弹幕颜色 |
| dm_type					| num		| 0:文本 1:表情包 |
| font_size					| num		| `25` 弹幕字体大小 |
| player_mode				| num		| 弹幕位置 | 0:？ 1:滚动 2:？ 4:底部
| show_player_type			| num		| 0 |
| content					| str		| 弹幕内容/表情包名称 |
| user_hash					| str		| `str(DEC:crc32(uid))`十六进制转十进制转字符串 |
| emoticon_unique			| str		| 表情ID |
| bulge_display				| num		| 0:官方表情包 1:房间表情包 |
| recommend_score			| num		| ？弹幕推荐等级/？智能屏蔽等级 | 抽奖:0
| main_state_dm_color		| str		| "" |
| objective_state_dm_color	| str		| "" |
| direction					| num		| 0 |
| pk_direction				| num		| 0 |
| quartet_direction			| num		| 0 |
| anniversary_crowd			| num		| 0 |
| yeah_space_type			| str		| "" |
| yeah_space_url			| str		| "" |
| jump_to_url				| str		| "" |
| space_type				| str		| "" |
| space_url					| str		| "" |
| animation					| obj		| {} |
| emots						| obj/null	| 新的表情包 k:v{obj...} |
| is_audited				| bool		|  | 20230217
| id_str					| str		| 144bit | 20230308
#### DANMU_MSG__info__0__15__extra__emots
emoticonOptions
| key				| type	| value |
|-|-|-|
| emoticon_id		| num	| 表情ID |
| emoji 			| str	|  |
| descript 			| str	|  |
| url				| str	|  |
| width				| num	| 宽 |
| height 			| num	| 高 |
| emoticon_unique	| str	| 表情ID |
| count 			| num	| 计数 |
#### DANMU_MSG__info__0__16
| key				| type	| value |
|-|-|-|
| activity_identity	| str	| 抽奖id |
| activity_source	| num	| 0,1,2 |
| not_show			| num	| 0,1 |
```json
"emots":{"[dog]":{"emoticon_id":208,"emoji":"[dog]","descript":"[dog]","url":"http://i0.hdslb.com/bfs/live/4428c84e694fbf4e0ef6c06e958d9352c3582740.png","width":20,"height":20,"emoticon_unique":"emoji_208","count":1}}
```
#### DANMU_MSG__dm_v2
~~上线时间 2023-02-17 05:50:13~05:50:24(UTC+8)~~  
~~下线时间 2023-02-23 19:30?~~  
上线时间 2023-03-23  

### CUT_OFF
[TOP](#直播弹幕格式)  
切断直播！
**根据JavaScript文件分析**
| key		| type	| value |
|-|-|-|
| cmd		| str	| "CUT_OFF" |
| msg		| str	|  |
| roomid	| num	| 直播间id |
```json
1678377738736567{"cmd":"CUT_OFF","msg":"直播中涉及低俗内容","roomid":12345}
"禁播游戏" "版权相关" "违反直播规范"
```

### MESSAGEBOX_USER_GAIN_MEDAL
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key	| type	| value |
|-|-|-|
| cmd	| str	| "MESSAGEBOX_USER_GAIN_MEDAL" |
| data	| obj	| |
#### MESSAGEBOX_USER_GAIN_MEDAL__data
| key		| type	| value |
|-|-|-|
| up_uid	| XXX	| |
| toast		| XXX	| |

### MESSAGEBOX_USER_MEDAL_CHANGE
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key	| type	| value |
|-|-|-|
| cmd	| str	| "MESSAGEBOX_USER_MEDAL_CHANGE" |
| data	| obj	| |
#### MESSAGEBOX_USER_MEDAL_CHANGE__data
| key					| type	| value |
|-|-|-|
| up_uid				| XXX	| |
| unlock				| XXX	| |
| multi_unlock_level	| XXX	| |
| upper_bound_content	| XXX	| |

### MESSAGEBOX_USER_MEDAL_COMPENSATION
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key	| type	| value |
|-|-|-|
| cmd	| str	| "MESSAGEBOX_USER_MEDAL_COMPENSATION" |
| data	| obj	| |
#### MESSAGEBOX_USER_MEDAL_COMPENSATION__data
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| up_uid	| XXX	| |
| add_score	| XXX	| |

### SHOPPING_CART_SHOW
[TOP](#直播弹幕格式)  
？购物车  
开播后约30ms内发送`status=1`的包
| key	| type	| value |
|-|-|-|
| cmd	| str	| "SHOPPING_CART_SHOW" |
| data	| obj	| |
#### SHOPPING_CART_SHOW__data
| key		| type	| value |
|-|-|-|
| status	| num	| 开播:1 下播:2 |
```json
1678276833737254{"cmd":"SHOPPING_CART_SHOW","data":{"status":1}}
1678284426205438{"cmd":"SHOPPING_CART_SHOW","data":{"status":2}}
```

### WIDGET_BANNER
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "WIDGET_BANNER" |
| data	| obj	| |
#### WIDGET_BANNER__data
| key			| type	| value |
|-|-|-|
| timestamp		| num	| 当前时间TimeStamp(秒) |
| widget_list	| obj	| "***ID***":{} |
#### WIDGET_BANNER__data__widget_list__ID
| key 15			| type	| value |
|-|-|-|
| id				| num	| ***ID*** |
| title				| str	| WIDGET_BANNER__REF |
| cover				| str	| "" |
| web_cover			| str	| "" |
| tip_text			| str	| WIDGET_BANNER__REF |
| tip_text_color	| str	| WIDGET_BANNER__REF |
| tip_bottom_color	| str	| WIDGET_BANNER__REF |
| jump_url			| str	| WIDGET_BANNER__REF |
| url				| str	| "" |
| stay_time			| num	| 5 |
| site				| num	| 1 |
| platform_in		| arr	| ["live","blink","live_link","web","pc_link"] |
| type				| str	| WIDGET_BANNER__REF |
| band_id			| num	| WIDGET_BANNER__REF |
| sub_key			| str	| WIDGET_BANNER__REF |
| sub_data			| str	| urlencode(json) |
| is_add			| bool	| true |
```py
jump_url=f"https://live.bilibili.com/activity/live-activity-battle/index.html?app_name={WIDGET_BANNER__REF}&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,0,0,12,0;2,2,375,100p,0,0,0,0,12,0;3,3,100p,70p,0,0,0,0,12,0;4,2,375,100p,0,0,0,0,12,0;5,3,100p,70p,0,0,0,0,12,0;6,3,100p,70p,0,0,0,0,12,0;7,3,100p,70p,0,0,0,0,12,0;8,3,100p,70p,0,0,0,0,12,0&room_id={直播间id}&uid={uid}#/"
```
#### WIDGET_BANNER__REF
|id		|title|tip_text|tip_text_color|tip_bottom_color|jump_url__app_name|type|band_id|sub_key|
|-|-|-|-|-|-|-|-|-|
|2		|大乱斗|PK大乱斗|A1F8FF|7349D5|chaos|3|0|pk_info|
|309	|争先拜大年|春节活动|FFFFFF|ffeaa0|spring_festival_2023|1|101566||
|307	|花灯闹元宵|花灯闹元宵|8F0606|cf442d|lantern_festival_2023|1|101598||
|xxx	|xxx|xxx|xxx|xxx|xxx|xxx|xxx||
```json
0000000000000000{"cmd":"WIDGET_BANNER","data":{"timestamp":1658063985,"widget_list":{"217":null}}}
0000000000000000{"cmd":"WIDGET_BANNER","data":{"timestamp":1658063995,"widget_list":{"216":null}}}
1678420804547430{"cmd":"WIDGET_BANNER","data":{"timestamp":1678420805,"widget_list":{"322":null}}}
1678421179367186{"cmd":"WIDGET_BANNER","data":{"timestamp":1678421179,"widget_list":{"323":{"id":323,"title":"BLS限时任务","cover":"","web_cover":"","tip_text":"限时任务","tip_text_color":"#FFFFFF","tip_bottom_color":"#2868FF","jump_url":"https://live.bilibili.com/activity/live-activity-battle/index.html?app_name=yq&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,0,0,12,0;2,2,375,100p,0,0,0,0,12,0;3,3,100p,70p,0,0,0,0,12,0;4,2,375,100p,0,0,0,0,12,0;5,3,100p,70p,0,0,0,0,12,0;6,3,100p,70p,0,0,0,0,12,0;7,3,100p,70p,0,0,0,0,12,0;8,3,100p,70p,0,0,0,0,12,0&room_id=XXX&uid=XXX#/101790?nonsense=1","url":"","stay_time":5,"site":1,"platform_in":["live","blink","live_link","web","pc_link"],"type":11,"band_id":101762,"sub_key":"","sub_data":"%7B%22target_val%22%3A120000%2C%22current_val%22%3A3%2C%22task_status%22%3A0%2C%22timeout%22%3A1678424278%2C%22reward_price%22%3A500%2C%22reward_type%22%3A%22red_pocket%22%7D","is_add":true}}}}
```

### GOTO_BUY_FLOW
[TOP](#直播弹幕格式)  
移动端 购买装扮
| key	| type	| value |
|-|-|-|
| cmd	| str	| "GOTO_BUY_FLOW" |
| data	| obj	| |
#### GOTO_BUY_FLOW__data
| key	| type	| value |
|-|-|-|
| text	| str	| "X\*\*正在去买" / "X\*\*等2人正在去买" |
```json
1678277584834531{"cmd":"GOTO_BUY_FLOW","data":{"text":"安**等2人正在去买"}}
1678277611551755{"cmd":"GOTO_BUY_FLOW","data":{"text":"w**正在去买"}}
```

### RECOMMEND_CARD
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "RECOMMEND_CARD" |
| data	| obj	| |
#### RECOMMEND_CARD__data
| key				| type | value |
|-|-|-|
| title_icon | str | https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png |
| recommend_list	| array	| obj[] |
| timestamp			| num	| 当前时间TimeStamp(秒) |
#### RECOMMEND_CARD__data__recommend_list__0
```json
{"shopping_card_detail":{"goods_id":"{}","goods_name":"${商品名称}","goods_price":"${最低价格}","goods_max_price":"","sale_status":0,"coupon_name":"","goods_icon":"http://i0.hdslb.com/bfs/garb/item/7b805767338eb54bbfa324e925d08cbddc88f496.jpg","goods_status":1,"source":5,"h5_url":"https://www.bilibili.com/h5/mall/suit/detail?id=32833&navhide=1&from_id=480432362&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=${source}&goods_id=${goods_id}#/${virdress}","jump_link":"","schema_url":"","is_pre_sale":0,"activity_info":null,"pre_sale_info":null,"early_bird_info":null,"timestamp":${当前时间},"coupon_discount_price":"","selling_point":"","hot_buy_num":xxxx,"gift_buy_info":null,"is_exclusive":false,"coupon_id":"","reward_info":null,"goods_tag_list":null,"virtual_extra_info":{"goods_type":1,"web_container_type":1},"price_info":{"normal":{"prefix_price":"","sale_price":"{最低价格}","suffix_price":"起","strock_price":"","sale_start_time":xxxx,"sale_end_time":0},"activity":null},"btn_info":{"card_btn_status":1,"card_btn_title":"去抢购","card_btn_style":1},"goods_sort_id":0},"recommend_card_extra":null}
1679140929359145{"cmd":"RECOMMEND_CARD","data":{"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png","recommend_list":[],"timestamp":1679140928}}
```

### COMMON_NOTICE_DANMAKU
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "COMMON_NOTICE_DANMAKU" |
| data	| obj	| |
#### COMMON_NOTICE_DANMAKU__data
| key				| type	| value |
|-|-|-|
| biz_id	？		| num	| 0 |
| content_segments	| array	| |
| danmaku_style	？	| obj	| |
| danmaku_uri	？	| str	| "" |
| dmscore			| num	| 144 |
| terminals			| array	| [1,2,3,4,5] |
```json
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#998EFF","font_color_dark":"#998EFF","highlight_font_color":"#998EFF","highlight_font_color_dark":"#998EFF","text":"<%恭喜主播 {XXXX} %>成为 {ZZZZ} 第 {yyyy} 名！","type":1}],"danmaku_style":{"background_color":[],"background_color_dark":[]},"danmaku_uri":"","dmscore":144,"terminals":[4]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#998EFF","font_color_dark":"#998EFF","text":"恭喜主播 {XXXX} 成为{ZZZZ}第{YYYY}名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[4]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#99A5AE","font_color_dark":"#99A5AE","text":"恭喜主播 {XXXX} 成为{ZZZZ}当前第{YYYY}名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#CCCCCC","font_color_dark":"#CCCCCC","text":"恭喜主播 {XXXX} ","type":1},{"font_color":"#F494AF","font_color_dark":"#F494AF","text":"成为上时段 {ZZZZ} 第 {YYYY} 名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[1,2,3]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#CCCCCC","font_color_dark":"#CCCCCC","text":"恭喜主播 {XXXX} ","type":1},{"font_color":"#F494AF","font_color_dark":"#F494AF","text":"成为{ZZZZ}当前第{YYYY}名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[1,2,3]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#FFC73E","font_color_dark":"#FFC73E","highlight_font_color":"#CCCCCC","highlight_font_color_dark":"#CCCCCC","text":"<%恭喜主播 {XXXX} %>成为 {ZZZZ} 第 {YYYY} 名！","type":1}],"danmaku_style":{"background_color":["#66000000"],"background_color_dark":["#66000000"]},"danmaku_uri":"","dmscore":144,"terminals":[1,2,3,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#F9F9F9","font_color_dark":"#F9F9F9","text":"恭喜 {XXXX} 成为上时段 {ZZZZ} 第 {YYYY} 名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,"content_segments":[{"font_color":"#998EFF","font_color_dark":"#998EFF","text":"恭喜 {XXXX} 成为上时段 {ZZZZ} 第 {YYYY} 名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":144,"terminals":[4]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#F294AE","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"恭喜{XXXX}成为红包收割机虚拟星耀赛道第{Y}名！","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#F294AE","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"恭喜{XXXX}荣获上一个锦鲤小时榜冠军，获得{Y}倍加成，价值{Z}元红包雨！","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#F294AE","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"距离锦鲤小时榜结束还有5分钟，最高10倍的锦鲤红包就在前方！","type":1},{"background_color":["#FA729A"],"background_color_dark":null,"font_bold":false,"font_color":"#FFFFFF","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"【前往查看】","type":3,"uri":"https://live.bilibili.com/activity/live-activity-battle/index.html?app_name=spring_festival_2023&tab=rank&hour=1&with_menu=0&show_close=0&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,0,0,12,0;2,2,375,100p,0,0,0,0,12,0;3,3,100p,70p,0,0,0,0,12,0;4,2,375,100p,0,0,0,0,12,0;5,3,100p,70p,0,0,0,0,12,0;6,3,100p,70p,0,0,0,0,12,0;7,3,100p,70p,0,0,0,0,12,0;8,3,100p,70p,0,0,0,0,12,0&room_id={ROOMID}&uid={UID}#/"}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#61666d","font_color_dark":"#a2a7ae","highlight_font_color":"#FFB027","highlight_font_color_dark":"#FFB027","text":"<%{YYYY}%> 被点亮啦！恭喜 <%{XXXX}%> 成为星球守护者！","type":1}],"dmscore":144,"terminals":[4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"{XXXX} 送出的红包为主播新增{YYYY}个粉丝！","type":1}],"dmscore":144,"terminals":[2,3,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"花灯闹元宵限时任务：任务即将结束，抓紧完成获取{x}红包奖励吧！未完成任务将无法获得奖励","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"{XXXX}在元气赏中五连抽！送出了好多礼物！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"新春限时任务：恭喜主播完成限时任务，直播间派发{XXX}元红包，速抢手慢无！新任务将在30s后开启","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"新春限时任务：任务即将结束，抓紧完成获取{XXX}元红包奖励吧！未完成任务将无法获得奖励","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FFFFFF","font_color_dark":"#FFFFFF","highlight_font_color":"#FFB027","highlight_font_color_dark":"#FFB027","text":"<%{YYYY}%> 被点亮啦！恭喜 <%{XXXX}%> 成为星球守护者！","type":1}],"dmscore":144,"terminals":[1,2,3]}}
1678420799573701{"cmd":"COMMON_NOTICE_DANMAKU","data":{"terminals":[1,3,4],"content_segments":[{"type":1,"font_color":"#FD5392","text":"疯狂星期五：活动开启！今日12点～24点，宝盒超级战舰概率翻4倍！赶快来抽！"}]}}
1678420799639093{"cmd":"COMMON_NOTICE_DANMAKU","data":{"terminals":[1,3,4],"content_segments":[{"type":1,"font_color":"#FD5392","text":"疯狂星期五：活动开启！今日12点～24点，盲盒浪漫城堡概率翻4倍！赶快来抽！"}]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"绝杀时刻开启，绝杀结束时领先对手1000乱斗值，即可触发绝杀提前赢得大乱斗胜利！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"绝杀时刻开启，绝杀结束时领先对手500乱斗值，即可触发绝杀提前赢得大乱斗胜利！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"我方主播在绝杀时刻领先对手1000乱斗值，触发绝杀！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"我方主播在绝杀时刻领先对手500乱斗值，触发绝杀！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"我方主播暂时领先！兄弟萌注意守塔，保护好我方主播哟～","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","highlight_font_color":"#FCA622","text":"视频大乱斗玩法小贴士，双方主播可以唱《{XXXX}》，一比高下～","type":1}],"dmscore":144,"terminals":[2,3,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","highlight_font_color":"#FCA622","text":"视频大乱斗玩法小贴士，双方主播可以唱跳《{XXXX}》，一比高下～","type":1}],"dmscore":144,"terminals":[2,3,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","highlight_font_color":"#FCA622","text":"视频大乱斗玩法小贴士，双方主播可以跟随音乐甩头，一比高下～","type":1}],"dmscore":144,"terminals":[2,3,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","highlight_font_color":"#FCA622","text":"视频大乱斗玩法小贴士，双方主播可以跳一段《{XXXX}》，一比高下～","type":1}],"dmscore":144,"terminals":[2,3,5]}}
PK{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","highlight_font_color":"#FCA622","text":"本场PK大乱斗我方获胜！感谢<%<${XXXX}$>%>为胜利做出的贡献","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
```

### POPULARITY_RED_POCKET_NEW
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_NEW" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_NEW__data
| key			| type	| value |
|-|-|-|
| lot_id		| num	| 抽奖id |
| start_time	| num	| 开始时间TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| wait_num		| num	|  |
| uname			| str	| 用户名 |
| uid			| num	| uid |
| action		| str	| "送出" |
| num			| num	| 1 |
| gift_name		| str	| "红包" |
| gift_id		| num	| `13000` |
| price			| num	| 价格(RMB*10) |
| name_color	| str	| 舰长:"#00D1F1" |
| medal_info	| obj	| [medal_info](#粉丝牌信息medal_info) |
```json
1678201324.029{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"lot_id":123,"start_time":1678201324,"current_time":1678201324,"wait_num":0,"uname":"直播小电视","uid":1407831746,"action":"送出","num":1,"gift_name":"红包","gift_id":13000,"price":950,"name_color":"","medal_info":{"target_id":0,"special":"","icon_id":0,"anchor_uname":"","anchor_roomid":0,"medal_level":0,"medal_name":"","medal_color":0,"medal_color_start":0,"medal_color_end":0,"medal_color_border":0,"is_lighted":0,"guard_level":0}}}
```

### POPULARITY_RED_POCKET_START
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_START" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_START__data
| key				| type	| value |
|-|-|-|
| lot_id			| num	| 抽奖id |
| sender_uid		| num	| uid |
| sender_name		| str	| 用户名 |
| sender_face		| str	| 头像URL |
| join_requirement	| num	| 1 |
| danmu				| str	| "老板大气！点点红包抽礼物" |
| current_time		| num	| 1674562037 |
| start_time		| num	| 1674562036 |
| end_time			| num	| 1674562216 |
| last_time			| num	| 180 |
| remove_time		| num	| 1674562231 |
| replace_time		| num	| 1674562226 |
| lot_status		| num	| [lot_status](#others) 1 |
| h5_url			| str	| f"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId={lot_id}" |
| user_status		| num	| 2 |
| awards			| array	| obj[3] |
| lot_config_id		| num	| 红包预设 |
| total_price		| num	| 礼物总价值*0.8 |
| wait_num			| num	| 0 |
#### POPULARITY_RED_POCKET_START__data__awards
| [i].key		| type	| value |
|-|-|-|
| [i].gift_id	| num	| 礼物id |
| [i].gift_name	| num	| 礼物名称 |
| [i].gift_pic	| num	| 礼物图像URL(140*140) |
| [i].num		| num	| 数量 |
```json
1678201325331703{"cmd":"POPULARITY_RED_POCKET_START","data":{"lot_id":12345,"sender_uid":1407831746,"sender_name":"直播小电视","sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","join_requirement":1,"danmu":"老板大气！点点红包抽礼物！","current_time":1678201325,"start_time":1678201324,"end_time":1678201504,"last_time":180,"remove_time":1678201519,"replace_time":1678201514,"lot_status":1,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=9658269","user_status":2,"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"lot_config_id":-1,"total_price":95000,"wait_num":0}}
```

### POPULARITY_RED_POCKET_WINNER_LIST
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_WINNER_LIST" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_WINNER_LIST__data
| key			| type	| value |
|-|-|-|
| lot_id		| num	| 抽奖id |
| total_num		| num	| |
| winner_info	| array	| array[total_num] |
| awards		| obj	| ${gift_id}:{obj...} |
| version		| num	| 1 |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__winner_info
| array			| type	| value |
|-|-|-|
| \[i\]\[0\]	| num	| uid |
| \[i\]\[1\]	| str	| name |
| \[i\]\[2\]	| num	| `bag_id` |
| \[i\]\[3\]	| num	| gift_id |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__awards
| key			| type	| value |
|-|-|-|
| award_type	| num	|  |
| award_name	| str	| 礼物名称 |
| award_pic		| str	| URL_图像(140*140) |
| award_big_pic	| str	| URL_图像(360*360) |
| award_price	| num	| 礼物单价(RMB*1000) |
```json
1678277040970876{"cmd":"POPULARITY_RED_POCKET_WINNER_LIST","data":{
	"lot_id":12345,"total_num":52,"winner_info":[
		[12345,"NAME",5157131,31218],
		[12345,"NAME",5157132,30971],
		[12345,"NAME",5144776,30971],
		[12345,"NAME",5119294,30971],
		[12345,"NAME",5157133,30971],
		[12345,"NAME",5137353,30971],
		[12345,"NAME",5107760,31278],
		[12345,"NAME",5153037,31278],
		[12345,"NAME",5153036,31278],
		[12345,"NAME",5151838,31278],
		[12345,"NAME",5137354,31278],
		[12345,"NAME",5151839,31278],
		[12345,"NAME",5137355,31278],
		[12345,"NAME",5126882,31278],
		[12345,"NAME",5126883,31278],
		[12345,"NAME",5137356,31278],
		[12345,"NAME",5100179,31278],
		[12345,"NAME",5137357,31278],
		[12345,"NAME",5137358,31278],
		[12345,"NAME",5137359,31278],
		[12345,"NAME",5157135,31278],
		[12345,"NAME",5119827,31278],
		[12345,"NAME",5107761,31278],
		[12345,"NAME",5157134,31278],
		[12345,"NAME",5106860,31278],
		[12345,"NAME",5107762,31278],
		[12345,"NAME",5100180,31278],
		[12345,"NAME",5107763,31278],
		[12345,"NAME",5151840,31278],
		[12345,"NAME",5107764,31278],
		[12345,"NAME",5106861,31278],
		[12345,"NAME",5146803,31278],
		[12345,"NAME",5093098,31278],
		[12345,"NAME",5167479,31278],
		[12345,"NAME",5126886,31278],
		[12345,"NAME",5100182,31278],
		[12345,"NAME",5137360,31278],
		[12345,"NAME",5137361,31278],
		[12345,"NAME",5126884,31278],
		[12345,"NAME",5100181,31278],
		[12345,"NAME",5153552,31278],
		[12345,"NAME",5126885,31278],
		[12345,"NAME",5106862,31278],
		[12345,"NAME",5103284,31278],
		[12345,"NAME",5106863,31278],
		[12345,"NAME",5153553,31278],
		[12345,"NAME",5107765,31278],
		[12345,"NAME",5153038,31278],
		[12345,"NAME",5126887,31278],
		[12345,"NAME",5137362,31278],
		[12345,"NAME",5106864,31278],
		[12345,"NAME",5167480,31278]
	],
	"awards":{
		"30971":{"award_type":1,"award_name":"这个好诶","award_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","award_big_pic":"https://i0.hdslb.com/bfs/live/fc69ce781aae94ef0629b68b1d650a3a837086be.png","award_price":1000},
		"31218":{"award_type":1,"award_name":"撒花","award_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","award_big_pic":"https://i0.hdslb.com/bfs/live/ae011224225717129e19a56d898080ff377645a6.png","award_price":66000},
		"31278":{"award_type":1,"award_name":"打call","award_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","award_big_pic":"https://i0.hdslb.com/bfs/live/d31a129b858c1853f0bc588096d1ed313293c30a.png","award_price":500}
		},"version":1}}
```

### ROOM_BLOCK_MSG
[TOP](#直播弹幕格式)  
用户封禁
| key		| type	| value |
|-|-|-|
| cmd		| str	| "ROOM_BLOCK_MSG" |
| data		| obj	| |
| uid		| str	| |
| uname		| str	| |
#### ROOM_BLOCK_MSG__data
| key		| type	| value |
|-|-|-|
| dmscore	| num	| 30 |
| operator	| num	| 1:"房管" 2:"高级房管" |
| uid		| num	|  |
| uname		| str	|  |
```json
1676985275750905{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":2,"uid":12345,"uname":"name"},"uid":"12345","uname":"name"}
1678362977.836{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":1,"uid":1906462188,"uname":"bili_24050293574"},"uid":"1906462188","uname":"bili_24050293574"}
```

### AREA_RANK_CHANGED
[TOP](#直播弹幕格式)  
timestamp: N*5
| key	| type	| value |
|-|-|-|
| cmd	| str	| "AREA_RANK_CHANGED" |
| data	| obj	| |
#### AREA_RANK_CHANGED__data
| key			| type	| value |
|-|-|-|
| conf_id		| num	|  |
| rank_name		| str	|  |
| uid			| num	|  |
| rank			| num	|  |
| icon_url_blue	| str	| https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png |
| icon_url_pink	| str	| https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png |
| icon_url_grey	| str	| https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png |
| action_type	| num	| 1 |
| timestamp		| num	| TimeStamp(秒) |
| msg_id		| str	| UUID4 "xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx" |
| jump_url_link	| str	| https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=￥{uid}&conf_id=￥{conf_id}&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank |
| jump_url_pc	| str	| https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=￥{uid}&conf_id=￥{conf_id}&pc_ui=338,465,f4eefa,0#/area-rank |
| jump_url_pink	| str	| https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=￥{uid}&conf_id=￥{conf_id}&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank |
| jump_url_web	| str	| https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=￥{uid}&conf_id=￥{conf_id}#/area-rank |
```json
1676968815955063{"cmd":"AREA_RANK_CHANGED","data":{"conf_id":24,"rank_name":"电竞航海","uid":9999,"rank":0,"icon_url_blue":"https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png","icon_url_pink":"https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png","icon_url_grey":"https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png","action_type":1,"timestamp":1676968813,"msg_id":"ffffffff-ffff-4fff-ffff-ffffffffffff","jump_url_link":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=9999&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank","jump_url_pc":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=9999&conf_id=24&pc_ui=338,465,f4eefa,0#/area-rank","jump_url_pink":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=9999&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank","jump_url_web":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=9999&conf_id=24#/area-rank"}}
```

### HOT_BUY_NUM
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "HOT_BUY_NUM" |
| data	| obj	| |
#### HOT_BUY_NUM__data
| key		| type	| value |
|-|-|-|
| goods_id	| str | id |
| num		| num |  |
```json

```

### PK_BATTLE_END
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "PK_BATTLE_END" |
| pk_id		| str	| |
| pk_status	| num	| # |
| timestamp	| obj	| TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_END__data
| key			| type	| value |
|-|-|-|
| battle_type	| num	| |
| timer			| num	| |
| init_info		| obj	| |
| match_info	| obj	| |
#### PK_BATTLE_END__data__&2_info
| key			| type	| value |
|-|-|-|
| room_id		| num	| 我方直播间id or 对方直播间id |
| votes			| num	| |
| winner_type	| num	| |
| best_uname	| num	| 最高贡献者 |
```js
// pk_status
pre = 101
process = 201
lastMinute = 301
normalFreeze = 401
combineStreamFreeze = 402
lastMinuteFreeze = 501
punish = 601
punishError = 610
end = 1001
lastMinuteEnd = 1101
matchOverTime = 1201
cancelMatch = 1301
combineStreamFailed = 1401
videoPunishWithNormal = 701
videoPunishWithFinalHit = 702
// winner_type
draw= 1 
normalWin= 2 
lastMinuteWin= 3 
fail = -1
```
```json
{"cmd":"PK_BATTLE_END","pk_id":"321224414","pk_status":401,"timestamp":1676583083,"data":{"battle_type":2,"timer":10,"init_info":{"room_id":123,"votes":190,"winner_type":2,"best_uname":"XXX"},"match_info":{"room_id":456,"votes":50,"winner_type":-1,"best_uname":"YYY"}}}
{"cmd":"PK_BATTLE_END","pk_id":"321224459","pk_status":501,"timestamp":1676584144,"data":{"battle_type":2,"timer":10,"init_info":{"room_id":123,"votes":1314,"winner_type":3,"best_uname":"XXX"},"match_info":{"room_id":456,"votes":51,"winner_type":-1,"best_uname":"YYY"}}}
```

### WIDGET_GIFT_STAR_PROCESS
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "WIDGET_GIFT_STAR_PROCESS" |
| data	| obj	| |
#### WIDGET_GIFT_STAR_PROCESS__data
| key				| type	| value |
|-|-|-|
| start_date		| num	| yyyyMMdd(星期一) |
| process_list		| array	| obj |
| finished			| bool	| |
| ddl_timestamp		| num	| TimeStamp(秒) 下一个星期一00:00:00 UTC+8 |
| version			| num	| 当前时间TimeStamp(毫秒) |
| reward_gift		| num	| |
| reward_gift_img	| str	| |
| reward_gift_name	| str	| "礼物星球" |
#### WIDGET_GIFT_STAR_PROCESS__data__process_list
| key			| type	| value |
|-|-|-|
| gift_id		| num	| |
| gift_img		| str	| |
| gift_name		| str	| |
| completed_num	| num	| |
| target_num	| num	| |
```json

```

### LIVE_INTERACTIVE_GAME
[TOP](#直播弹幕格式)  
with `DANMU_MSG`
| key	| type	| value |
|-|-|-|
| cmd	| str	| "LIVE_INTERACTIVE_GAME" |
| data	| obj	| |
#### LIVE_INTERACTIVE_GAME__data
| key 17			| type	| value |
|-|-|-|
| type				| num	| 2? |
| uid				| num	| |
| uname				| str	| |
| uface				| str	| |
| gift_id			| num	| |
| gift_name			| str	| |
| gift_num			| num	| |
| price				| num	| |
| paid				| bool	| |
| msg				| str	| 弹幕内容/xxx |
| fans_medal_level	| num	| 粉丝牌等级 |
| guard_level		| num	| 舰长等级 |
| timestamp			| num	| TimeStamp(秒) |
| anchor_lottery	| null	| |
| pk_info			| null	| |
| anchor_info		| null	| |
| combo_info		| null	| |
```json
1678437449179347{"cmd":"LIVE_INTERACTIVE_GAME","data":{"type":2,"uid":22603253,"uname":"暮云初雨","uface":"","gift_id":0,"gift_name":"","gift_num":0,"price":0,"paid":false,"msg":"啊？","fans_medal_level":18,"guard_level":0,"timestamp":1678437449,"anchor_lottery":null,"pk_info":null,"anchor_info":null,"combo_info":null}}
```

### LIVE_MULTI_VIEW_CHANGE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "LIVE_MULTI_VIEW_CHANGE" |
| data	| obj	| |
#### LIVE_MULTI_VIEW_CHANGE__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_MULTI_VIEW_CHANGE","data":{"scatter":{"max":120,"min":5}}}
```

### SUPER_CHAT_ENTRANCE
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "SUPER_CHAT_ENTRANCE" |
| data		| obj	| |
| roomid	| num	| |
#### SUPER_CHAT_ENTRANCE__data
| key				| type	| value |
|-|-|-|
| status *			| num	| |
| icon				| str	| |
| jump_url			| str	| |
| broadcast_type	| num	| |
```json
1677263700276272{"cmd":"SUPER_CHAT_ENTRANCE","data":{"icon":"https:\/\/i0.hdslb.com\/bfs\/live\/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","jump_url":"https:\/\/live.bilibili.com\/p\/html\/live-app-superchat2\/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","status":0}}
1677245948100539{"cmd":"SUPER_CHAT_ENTRANCE","data":{"status":1,"jump_url":"https:\/\/live.bilibili.com\/p\/html\/live-app-superchat2\/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","icon":"https:\/\/i0.hdslb.com\/bfs\/live\/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","broadcast_type":1},"roomid":"12345"}

```

### SYS_MSG
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "SYS_MSG" |
| msg	| str	| |
| url	| str	| |
```json
1677240054180146{"cmd":"SYS_MSG","msg":"争夺开启，时间周五20点至周日20点，逾期不候哟！","url":""}
```

### VOICE_JOIN_STATUS
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "VOICE_JOIN_STATUS" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_STATUS__data
| key 12			| type	| value |
|-|-|-|
| room_id			| num	| |
| status			| num	| |
| channel			| str	| |
| channel_type		| str	| |
| uid				| num	| |
| user_name			| str	| |
| head_pic			| str	| |
| guard				| num	| |
| start_at			| num	| |
| current_time		| num	| |
| web_share_link	| str	| |
```json
{"cmd":"VOICE_JOIN_STATUS","data":{"room_id":12345678,"status":0,"channel":"","channel_type":"voice","uid":0,"user_name":"","head_pic":"","guard":0,"start_at":0,"current_time":1676582586,"web_share_link":"https://live.bilibili.com/h5/12345678"},"room_id":12345678}
```

### DM_INTERACTION
[TOP](#直播弹幕格式)  
弹幕投票
| key	| type	| value |
|-|-|-|
| cmd	| str	| "DM_INTERACTION" |
| data	| obj	| |
#### DM_INTERACTION__data
| key		| type	| value |
|-|-|-|
| id		| num	| |
| status	| num	| 5:结束 |
| type		| num	| |
| data		| str	| json |
#### DM_INTERACTION__data__data
| key					| type	| value |
|-|-|-|
| question				| str	|  |
| options				| array	| |
| vote_id				| num	| |
| cnt					| num	| 投票总数 |
| duration				| num	| 总时长(ms) |
| left_duration			| num	| 剩余时间(ms) |
| fade_duration			| num	| 1000 (ms) |
| waiting_duration		| num	| -1 |
| result				| num	| |
| result_text			| str	| |
| component				| str	| "https://live.bilibili.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0" |
| natural_die_duration	| num	| 30000 |
| my_vote				| num	| |
#### DM_INTERACTION__data__data__options
| key		| type	| value |
|-|-|-|
| idx		| num	| start:1 |
| desc		| str	| 投票选项 |
| cnt		| num	| 投票人数 |
| percent	| float	| 百分比 总计数小于~~5~~时为0 |
```json

```

### PLAY_TAG
[TOP](#直播弹幕格式)  
比赛 事件(开始、First Blood、击败、Double Kill、大小龙、结束)
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PLAY_TAG" |
| data	| obj	| |
#### PLAY_TAG__data
| key	| type	| value |
|-|-|-|
| tag_id	| num	| |
| pic		| str	| 事件pic |
| timestamp	| num	| 事件发生时间TimeStamp(秒) |
| type		| str	| "ADD" |
```json
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e04525fee9ea6ea6973e8bd1116d9f1f6501d37.png","timestamp":123,"type":"ADD"}}Double Kill
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e842f1a260e519158712e086e2a10e6fc280e53.png","timestamp":123,"type":"ADD"}}Quadra Kill
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/152132594676ffb27cd1d7992fe02f92b4909540.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/2ac5e22aa856b3b6739bc725cbe78b42b702eec0.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/3c26626a30fdb70e44e16fd4313fa02785486e30.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/5e59bb41b61b015f3665ba922fc1bd6db00c6d32.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/78c10171a17f19fb6f22296091c106852447ce7a.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/7c3cc2cdca443b5fcab636ceaec46d5922c257d5.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/92d895535c9517e13b4cb7d908faaf29aefbcb4a.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/bc1e526e05c11c9ffa515810268fca3d96472af7.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c241edb936a544538207f15a896db867878d262c.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c56b9ea02e1617a97fc933481b63ffab57ad296c.png","timestamp":123,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/de9d1486f85777cc74798eb1630abba0a695aa15.png","timestamp":123,"type":"ADD"}}Triple Kill
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/e01db14207b1a1087d1829db2690753e51080b26.png","timestamp":123,"type":"ADD"}}
```

### FULL_SCREEN_SPECIAL_EFFECT
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "FULL_SCREEN_SPECIAL_EFFECT" |
| data	| obj	| |
#### FULL_SCREEN_SPECIAL_EFFECT__data
| key			| type	| value |
|-|-|-|
| type			| num	| |
| ids			| array num	| |
| queue			| num	| |
| platform_in	| array num	| |
```json
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[433],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[514],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[515],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[670],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[949],"queue":2,"platform_in":[1,2]}}
```

### TRADING_SCORE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "TRADING_SCORE" |
| data	| obj	| |
#### TRADING_SCORE__data
| key				| type	| value |
|-|-|-|
| bubble_show_time	| num	| |
| num				| num	| |
| score_id			| num	| |
| uid				| num	| 主播uid |
| update_time		| num	| 当前时间TimeStamp(秒) |
| update_type		| num	| |
```json
1676995213502299{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":3,"score_id":3,"uid":123,"update_time":1676995214,"update_type":1}}
```

### PK_BATTLE_START
### PK_BATTLE_START_NEW
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "PK_BATTLE_START_NEW" |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
| data		| obj	| |
| roomid	| num	| |
#### PK_BATTLE_START_NEW__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_START",    "pk_id":321224540,"pk_status":201,"timestamp":1676586433,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":1676586433,"pk_frozen_time":1676586733,"pk_end_time":1676586743,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":1676586673,"final_conf":{"switch":1,"start_time":1676586553,"end_time":1676586613},"init_info":{"room_id":123,"date_streak":0},"match_info":{"room_id":456,"date_streak":0}},"roomid":"123"}
{"cmd":"PK_BATTLE_START_NEW","pk_id":321224540,"pk_status":201,"timestamp":1676586433,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":1676586433,"pk_frozen_time":1676586733,"pk_end_time":1676586743,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":1676586673,"final_conf":{"switch":1,"start_time":1676586553,"end_time":1676586613},"init_info":{"room_id":123,"date_streak":0},"match_info":{"room_id":456,"date_streak":0}},"roomid":"123"}
```

### ROOM_SILENT_OFF
[TOP](#直播弹幕格式)  
解除直播间全局禁言
| key	| type	| value |
|-|-|-|
| data	| obj	| |
| cmd	| str	| "ROOM_SILENT_OFF" |
#### ROOM_SILENT_OFF__data
| key		| type	| value |
|-|-|-|
| type		| str	| "" |
| level		| num	| 0 |
| second	| num	| 0 |
```json
1678423818464726{"data":{"type":"","level":0,"second":0},"cmd":"ROOM_SILENT_OFF"}
```

### ROOM_SILENT_ON
[TOP](#直播弹幕格式)  
开启直播间全局禁言
| key	| type	| value |
|-|-|-|
| data	| obj	| |
| cmd	| str	| "ROOM_SILENT_ON" |
#### ROOM_SILENT_ON__data
| key		| type	| value |
|-|-|-|
| type		| str	| "member"全员禁言 "medal"粉丝牌等级禁言 "level"UL等级禁言 |
| level		| num	| 粉丝牌等级/用户UL等级 |
| second	| num	| 结束时间TimeStamp(秒) |
```json
1678423826843822{"data":{"type":"member","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
1678423851808324{"data":{"type":"level","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
1678423882368101{"data":{"type":"level","level":60,"second":1678427481},"cmd":"ROOM_SILENT_ON"}
```

### CHANGE_ROOM_INFO
[TOP](#直播弹幕格式)  
更换直播间背景
| key			| type	| value |
|-|-|-|
| cmd			| str	| "CHANGE_ROOM_INFO" |
| background	| str	| URL |
| roomid		| num	| |
```json
1678603213961484{"cmd":"CHANGE_ROOM_INFO","background":"https:\/\/i0.hdslb.com\/bfs\/live\/f3c1e1e22dfb1942bd88c33f1aa174efe7a38dfd.jpg","roomid":12345}
```

### ROOM_CHANGE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "ROOM_CHANGE" |
| data	| obj	| |
#### ROOM_CHANGE__data
| key 7				| type	| value |
|-|-|-|
| title				| str	| 直播间标题 |
| area_id			| num	| [分区ID](#分区ID) |
| parent_area_id	| num	| [父分区ID](#分区ID) |
| area_name			| str	| [分区name](#分区ID) |
| parent_area_name	| str	| [父分区name](#分区ID) |
| live_key			| str	| 本次直播live_key |
| sub_session_key	| str	| 本次直播sub_session_key |
```json
1678420566686933{"cmd":"ROOM_CHANGE","data":{"title":"直播间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"0","sub_session_key":""}}
1679042602856000{"cmd":"ROOM_CHANGE","data":{"title":"直播间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"111111111111111111","sub_session_key":"111111111111111111sub_time:1679039114"}}
```

### OBS_SHIELD_STATUS_UPDATE
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "OBS_SHIELD_STATUS_UPDATE" |
| data		| obj	| |
| roomid	| str	| 直播间id |
#### OBS_SHIELD_STATUS_UPDATE__data
| key		| type	| value |
|-|-|-|
| change	| num	| 1 |
```json
1679147043057436{"cmd":"OBS_SHIELD_STATUS_UPDATE","data":{"change":1},"roomid":"123"}
1679147160178352{"cmd":"OBS_SHIELD_STATUS_UPDATE","data":{"change":1},"roomid":"123"}
```

### RING_STATUS_CHANGE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "RING_STATUS_CHANGE" |
| data	| obj	| |
#### RING_STATUS_CHANGE__data
| key		| type	| value |
|-|-|-|
| status	| num	| 0 |
```json
1674560418.853{"cmd":"RING_STATUS_CHANGE","data":{"status":0}}
```

### RING_STATUS_CHANGE_V2
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "RING_STATUS_CHANGE_V2" |
| data	| obj	| |
#### RING_STATUS_CHANGE_V2__data
| key		| type	| value |
|-|-|-|
| status	| num	| 0 |
```json
1674560418.853{"cmd":"RING_STATUS_CHANGE_V2","data":{"status":0}}
```

### VOICE_JOIN_LIST
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "VOICE_JOIN_LIST" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_LIST__data
| key			| type	| value |
|-|-|-|
| cmd			| str	| |
| room_id		| num	| |
| category		| num	| |
| apply_count	| num	| |
| red_point		| num	| |
| refresh		| num	| |
```json
1676034447.914{"cmd":"VOICE_JOIN_LIST","data":{"cmd":"","room_id":12345,"category":1,"apply_count":0,"red_point":1,"refresh":1},"room_id":12345}
```

### VOICE_JOIN_ROOM_COUNT_INFO
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "VOICE_JOIN_ROOM_COUNT_INFO" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_ROOM_COUNT_INFO__data
| key			| type	| value |
|-|-|-|
| cmd			| str	| |
| room_id		| num	| |
| root_status	| num	| |
| room_status	| num	| |
| apply_count	| num	| |
| notify_count	| num	| |
| red_point		| num	| |
```json
1676037191.884{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"cmd":"","room_id":12345,"root_status":1,"room_status":1,"apply_count":0,"notify_count":0,"red_point":0},"room_id":12345}
```

### ROOM_SKIN_MSG
[TOP](#直播弹幕格式)  
| key			| type	| value |
|-|-|-|
| cmd			| str	| "ROOM_SKIN_MSG" |
| skin_id		| num	| |
| status		| num	| 0,1 |
| end_time		| num	| TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| only_local	| bool	| |
| scatter *		| obj	| |
| skin_config *	| obj	| |
#### ROOM_SKIN_MSG__skin_config
| key			| type	| value |
|-|-|-|

```json
{"cmd":"ROOM_SKIN_MSG","skin_id":452,"status":1,"end_time":1677254459,"current_time":1676995259,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c6a13965d7ae8ab433ef05f643876d70ccd35204.zip","md5":"6EFCA3C8FEC1A595B2C185FCAE1741A0"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/8bd0abf11eb68e1867eda7ec74c8ff6bc158392a.zip","md5":"DE24184A495D8AC4D36C40E653EE6F1C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0fb370c451460cb0df6dafec005f7c361b6fbd98.zip","md5":"20B5DE12BC2C20037F30DD0ED76DC67F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/2e2857bbaa31de676896d436e3dadd083c439dc0.zip","md5":"66CF9042BBB331FF056DAB75FC56398E","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0847cbf4e927d494015bfa0ef025c2d38b6a3b7a.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/bfb1140f97cef5d1ed42fe32d9d873db17f1e443.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/3cf53eb68bf888cafd958b26f1257ef892de6e6f.jpg","mainText":"#FFffffff","normalText":"#FFffe2b2","highlightContent":"#FF500c22","border":"#FFffe2b2","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":454,"status":1,"end_time":1678809902,"current_time":1678377902,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c9a6c91cf1b3c0410053ad8d7453f1d3fa877549.zip","md5":"621F5833CE6FD085E800303AFFB4C3FD"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/3b91fa0f1e9e19016afa7af4c488b378657a5897.zip","md5":"716CCAB55B2D95EC8982F324BB59658C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0369e00a3b15672638bae9c7363d177ebe437281.zip","md5":"5FCA732A31E2B52AAF674F589C97230F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/20fe37059dbdf179ba34907496180caf48f9b2fd.zip","md5":"FD0306E4CE4D2848DDD430CD7C72C341","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/d2b7bf6fb6e6d66780a1227e71ea6bdc66dcf0e2.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF6c99dc","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":461,"status":1,"end_time":1678972715,"current_time":1678540715,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/b2e54b7cb64142ee32833d1ed84903fed67a0378.zip","md5":"710AFA69D08FC727EDA821E3AF5CA0C5"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/1143aa4127f6e6faf4ba36c483e506df88b069a8.zip","md5":"55AE9AC3311D58A5EABBABD85366BB2D"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/261dfdb079b3e5ee54f9000cec2274b5f4c5fe7c.zip","md5":"FE1737D3597AC78C791CD408D3A44B3B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/4d1bccb234baa040e379dfe55467e3ccc76658bf.zip","md5":"3CC0D358666AAEE5B0A8CA6411BA6730","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/50b6c93ccdcbdff73589c19eb6138fdf97a95d31.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF4f6dcb","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":64,"status":1,"end_time":2145888000,"current_time":1674562980,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/545a91102973626b1e39cec1c7cb93edfd55a7d8.zip","md5":"083B542663A17F47E0379EF7E7269CA3"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/ae3c6c3ca3b32fd21d3612dc7938a5bfce928dcf.zip","md5":"AB4F5A4D83FACA7D45AF2ACCC175CEAF"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/e26c2cb17d3b063d736104926bdeadcacef8a46b.zip","md5":"B2A4F7BD6B4F446BC85980B0B31EF37B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/a6bde45e0de2010afebdeab3572c2d078f2b3525.zip","md5":"9B0E3DEC95E3DB1CDC49CF838B539715","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/78c2321d946dcdf57c37779e674da6983f0850ee.png","giftControlBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/13f1bad1b1c1a050df36beb907d742a6a68d3fdb.png","rankListBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/93db8458c57791f7b89ec75ff54221aa8f33e9fa.png","mainText":"#FFf2ae09","normalText":"#FF999999","highlightContent":"#FFf2ae09","border":"#33999999"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":65,"status":0,"end_time":1674562973,"current_time":1674562973,"only_local":false}
```

### PK_BATTLE_ENTRANCE
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "PK_BATTLE_ENTRANCE" |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_ENTRANCE__data
| key		| type	| value |
|-|-|-|
| is_open	| bool	| |
```json
1678334400341992{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1678334400,"data":{"is_open":true}}
1678334430296768{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1678334430,"data":{"is_open":true}}
1678334460280234{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1678334460,"data":{"is_open":true}}
1678334490256484{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1678334490,"data":{"is_open":true}}
1678334520281183{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1678334520,"data":{"is_open":true}}
```

### LIVE_PANEL_CHANGE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "LIVE_PANEL_CHANGE" |
| data	| obj	| |
#### LIVE_PANEL_CHANGE__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
1678799853226302{"cmd":"LIVE_PANEL_CHANGE","data":{"type":2,"scatter":{"max":150,"min":5}}}
1678799894077773{"cmd":"LIVE_PANEL_CHANGE","data":{"type":2,"scatter":{"max":150,"min":5}}}
```

### RANK_REM
[TOP](#直播弹幕格式)  
| key		| type	| value |
|-|-|-|
| cmd		| str	| "RANK_REM" |
| data		| obj	| |
#### RANK_REM__data
| key		| type	| value |
|-|-|-|
| name		| str	| |
| room_id	| num	| 直播间id |
| ruid		| num	| 主播uid |
| time		| num	| 当前时间TimeStamp(秒) |
| uid		| num	| |
```json
1677075724070173{"cmd":"RANK_REM","data":{"name":"online_gold","room_id":12345,"ruid":12345,"time":1677075723,"uid":123}}
```

### GUARD_ACHIEVEMENT_ROOM
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "GUARD_ACHIEVEMENT_ROOM" |
| data	| obj	| |
#### GUARD_ACHIEVEMENT_ROOM__data
| key							| type	| value |
|-|-|-|
| anchor_basemap_url			| str	| https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png |
| anchor_guard_achieve_level	| num	| 1000 |
| anchor_modal					| obj	| |
| app_basemap_url				| str	| https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png |
| current_achievement_level		| num	| 3 |
| dmscore						| num	| 8 |
| event_type					| num	| 1 |
| face							| str	| 主播头像URL |
| first_line_content			| str	| 恭喜主播<%XXXX%> |
| first_line_highlight_color	| str	| #FFD432 |
| first_line_normal_color		| str	| #FFFFFF |
| headmap_url					| str	| https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png |
| is_first						| bool	| True |
| is_first_new					| bool	| False |
| room_id						| num	| 12345 |
| second_line_content			| str	| 舰队规模突破<%1000%> |
| second_line_highlight_color	| str	| #06DDFF |
| second_line_normal_color		| str	| #FFFFFF |
| show_time						| num	| 3 |
| web_basemap_url				| str	| https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png |
#### GUARD_ACHIEVEMENT_ROOM__anchor_modal
| key							| type	| value |
|-|-|-|
| first_line_content			| str	| 恭喜当前舰队规模突破<%1000%> |
| highlight_color				| str	| #00DCFF |
| second_line_content			| str	| 至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～ |
| show_time						| num	| 5 |
```json
1674562974068000{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":8,"event_type":1,"face":"https://i0.hdslb.com/bfs/face/000c5cdad665d9dc54cf5ea2498aa859c59e77fa.jpg","first_line_content":"恭喜主播<%XXXX%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
1678278669926000{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":8,"event_type":1,"face":"https://i0.hdslb.com/bfs/face/000c5cdad665d9dc54cf5ea2498aa859c59e77fa.jpg","first_line_content":"恭喜主播<%XXXX%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
1678278670200681{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":8,"event_type":1,"face":"https://i0.hdslb.com/bfs/face/000c5cdad665d9dc54cf5ea2498aa859c59e77fa.jpg","first_line_content":"恭喜主播<%XXXX%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
1676995272011427{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"","anchor_guard_achieve_level":0,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%0%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":0},"app_basemap_url":"","current_achievement_level":1,"dmscore":8,"event_type":2,"face":"https://i0.hdslb.com/bfs/face/34f35e3837bc09b274359e3116f07a753a4f0137.jpg","first_line_content":"恭喜主播<%XXXX%>","first_line_highlight_color":"","first_line_normal_color":"","headmap_url":"","is_first":false,"is_first_new":false,"room_id":1234,"second_line_content":"舰队规模突破<%0%>","second_line_highlight_color":"","second_line_normal_color":"","show_time":3,"web_basemap_url":"普通无需图片"}}
```

### PK_BATTLE_FINAL_PROCESS
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_FINAL_PROCESS" |
| data	| obj	| |
#### PK_BATTLE_FINAL_PROCESS__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":1676583082},"pk_id":321224414,"pk_status":201,"timestamp":1676582963}
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":1676583082},"pk_id":321224414,"pk_status":301,"timestamp":1676582902}
```

### PK_BATTLE_MATCH_TIMEOUT
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_MATCH_TIMEOUT" |
| data	| obj	| |
#### PK_BATTLE_MATCH_TIMEOUT__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_MATCH_TIMEOUT","data":{"battle_type":2}}
```

### PK_BATTLE_PROCESS_NEW
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_PROCESS_NEW" |
| data	| obj	| |
#### PK_BATTLE_PROCESS_NEW__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
#### PK_BATTLE_END__data__&2_info
| key			| type	| value |
|-|-|-|
| room_id		| num	| 我方直播间id or 对方直播间id |
| votes			| num	| |
| winner_type	| num	| |
| best_uname	| num	| 最高贡献者 |
```json
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":8,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1676585204}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":9,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1676585205}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":1,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"https://i1.hdslb.com/bfs/face/XXXXX.jpg","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1676584466}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":10,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"https://i1.hdslb.com/bfs/face/XXXXX.jpg","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1676584527}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":1314,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":45,"votes":51,"best_uname":"YYY","vision_desc":-1}},"pk_id":321224459,"pk_status":201,"timestamp":1676584062}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"https://i0.hdslb.com/bfs/face/XXX.jpg","uname":"XXX"}]},"match_info":{"room_id":456,"votes":104,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"https://i1.hdslb.com/bfs/face/YYY.jpg","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1676584547}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"https://i0.hdslb.com/bfs/face/XXX.jpg","uname":"XXX"}]},"match_info":{"room_id":456,"votes":105,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"https://i1.hdslb.com/bfs/face/YYY.jpg","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1676584547}
```

### PK_BATTLE_PRE_NEW
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_PRE_NEW" |
| data	| obj	| |
#### PK_BATTLE_PRE_NEW__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":321224475,"pk_status":101,"status_msg":"","timestamp":1676584371,"data":{"is_followed":1,"uname":"XXX","face":"https://i0.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":A,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":321224510,"pk_status":101,"status_msg":"","timestamp":1676585430,"data":{"is_followed":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":B,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224414,"timestamp":1676582772,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":C,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224459,"timestamp":1676583953,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":D,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224507,"timestamp":1676585193,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i1.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":E,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224540,"timestamp":1676586423,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":12345,"room_id":F,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
```

### PK_BATTLE_PUNISH_END
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_PUNISH_END" |
| data	| obj	| |
#### PK_BATTLE_PUNISH_END__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PUNISH_END","pk_id":"321224475","pk_status":1001,"status_msg":"","timestamp":1676584862,"data":{"battle_type":6}}
{"cmd":"PK_BATTLE_PUNISH_END","pk_id":"321224510","pk_status":1001,"status_msg":"","timestamp":1676585921,"data":{"battle_type":6}}
```

### PK_BATTLE_PRE
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_PRE" |
| data	| obj	| |
#### PK_BATTLE_PRE__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224414,"timestamp":1676582772,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":1234,"room_id":A,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224459,"timestamp":1676583953,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":1234,"room_id":B,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224507,"timestamp":1676585193,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i1.hdslb.com/bfs/face/XXX.jpg","uid":1234,"room_id":C,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224540,"timestamp":1676586423,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"https://i2.hdslb.com/bfs/face/XXX.jpg","uid":1234,"room_id":D,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
```

### PK_BATTLE_PROCESS
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "PK_BATTLE_PROCESS" |
| data	| obj	| |
#### PK_BATTLE_PROCESS__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
#### PK_BATTLE_END__data__&2_info
| key			| type	| value |
|-|-|-|
| room_id		| num	| 我方直播间id or 对方直播间id |
| votes			| num	| |
| winner_type	| num	| |
| best_uname	| num	| 最高贡献者 |
```json
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224414,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224459,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":-1}},"pk_id":321224459,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":-1}},"pk_id":321224459,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":-1}},"pk_id":321224507,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224414,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224414,"pk_status":201,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":-1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":1}},"pk_id":321224507,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224507,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224540,"pk_status":301,"timestamp":1676000000}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":301,"timestamp":1676000000}
```

### XXXXXXXXXXX
[TOP](#直播弹幕格式)  
| key	| type	| value |
|-|-|-|
| cmd	| str	| "XXXXXXXXXXX" |
| data	| obj	| |
#### XXXXXXXXXXX__data
| key	| type	| value |
|-|-|-|
| data	| xxx	| |
```json
{"key":"value"}
```

### others
[TOP](#直播弹幕格式)  
| key				| type	| value | where |
|-|-|-|-|
| guard_level		| num	| 舰长等级 <br> 0:无 <br> 1:总督GOVERNOR <br> 2:提督PREFECT <br> 3:舰长CAPTAIN |
| privilege_type	| num	| ！待确定 2:提督 3:舰长 |
| lot_status		| num	| 抽奖状态 0:开始 1:正在抽奖 2:开奖 |
| identities		| array	| 身份 1:"Normal" 2:"管理员" 3:"粉丝" 4:"Vip" 5:"SVip" 6:"舰长" 7:"提督" 8:"总督" |[INTERACT_WORD](#INTERACT_WORD)

```js
未知List
functionX(t){t[t.backgroundTask=1]="backgroundTask"}
functionX(t){t[t.chaosPK=1]="chaosPK",t[t.videoChasoPK=2]="videoChasoPK",t[t.videoPK=6]="videoPK"}
functionX(t){t[t.Entry=1]="Entry",t[t.Attention=2]="Attention",t[t.Share=3]="Share",t[t.SpecialAttention=4]="SpecialAttention",t[t.MutualAttention=5]="MutualAttention",t[t.Link=6]="Link"}
functionX(t){t[t.Entry=1]="Entry",t[t.Follow=2]="Follow",t[t.Share=3]="Share"}
functionX(t){t[t.GiftAnimation=0]="GiftAnimation",t[t.SuperGift=1]="SuperGift",t[t.LotteryDanmaku=2]="LotteryDanmaku",t[t.Notice=3]="Notice",t[t.buffCard=4]="buffCard",t[t.SuperChat=5]="SuperChat",t[t.EntryInfo=6]="EntryInfo",t[t.EmojiAnimation=7]="EmojiAnimation",t[t.EmojiDanmaku=8]="EmojiDanmaku"}
functionX(t){t[t.guardZong=1]="guardZong",t[t.guardTi=2]="guardTi",t[t.weekAllAreaTop1=3]="weekAllAreaTop1",t[t.weekSubAreaTop1=4]="weekSubAreaTop1"}
functionX(t){t[t.HeavensChoice=1]="HeavensChoice",t[t.RedEnvelope=2]="RedEnvelope"}
functionX(t){t[t.like=1]="like",t[t.unlike=2]="unlike"}
functionX(t){t[t.noEffect=0]="noEffect",t[t.player=1]="player",t[t.fullScreenAnimation=2]="fullScreenAnimation",t[t.medal=3]="medal"}
functionX(t){t[t.noGame=0]="noGame",t[t.inProgress=1]="inProgress",t[t.end=2]="end"}
functionX(t){t[t.none=0]="none",t[t.draw=1]="draw",t[t.win=2]="win",t[t.fail=-1]="fail",t[t.passive=-10]="passive"}
functionX(t){t[t.none=0]="none",t[t.draw=1]="draw",t[t.win=2]="win",t[t.fail=3]="fail",t[t.passive=-10]="passive"}
functionX(t){t[t.normal=0]="normal",t[t.antiBoom=1]="antiBoom"}
functionX(t){t[t.normal=0]="normal",t[t.community=1]="community",t[t.top=2]="top",t[t.special=3]="special",t[t.silver=4]="silver"}
functionX(t){t[t.normal=0]="normal",t[t.immune=1]="immune",t[t.kill=2]="kill",t[t.beKill=3]="beKill"}
functionX(t){t[t.normal=0]="normal",t[t.lucky=1]="lucky",t[t.chaosPKScore=2]="chaosPKScore",t[t.chaosPKImmune=3]="chaosPKImmune",t[t.chaosPKBoom=4]="chaosPKBoom"}
functionX(t){t[t.Normal=0]="Normal",t[t.Meteor=1]="Meteor",t[t.Moon=2]="Moon",t[t.Pk=3]="Pk"}
functionX(t){t[t.normal=0]="normal",t[t.month=1]="month",t[t.year=2]="year"}
functionX(t){t[t.normal=1]="normal",t[t.giftLottery=2]="giftLottery",t[t.guardLottery=3]="guardLottery",t[t.guardWelcome=4]="guardWelcome",t[t.giftLotteryResult=5]="giftLotteryResult",t[t.highEnergy=6]="highEnergy",t[t.no1=7]="no1",t[t.notSide=8]="notSide",t[t.chaosPk=9]="chaosPk"}
functionX(t){t[t.NotExpired=0]="NotExpired",t[t.WillExpired=1]="WillExpired",t[t.JustExpired=2]="JustExpired",t[t.HasExpired=3]="HasExpired"}
functionX(t){t[t.notStart=0]="notStart",t[t.inProcess=1]="inProcess",t[t.end=2]="end"}
functionX(t){t[t.Other=0]="Other",t[t.Mac=1]="Mac",t[t.Windows=2]="Windows",t[t.Unix=3]="Unix",t[t.Linux=4]="Linux"}
functionX(t){t[t.other=0]="other",t[t["2g"]=2]="2g",t[t["3g"]=3]="3g",t[t["4g"]=4]="4g"}
functionX(t){t[t.PK_PRE=200]="PK_PRE",t[t.PK_START=300]="PK_START",t[t.PK_END=400]="PK_END",t[t.PK_AGAIN=400]="PK_AGAIN",t[t.PK_SETTLE=400]="PK_SETTLE",t[t.PK_PROCESS=300]="PK_PROCESS",t[t.PK_MATCH=100]="PK_MATCH",t[t.PK_MIC_END=2044]="PK_MIC_END",t[t.PK_CLICK_AGAIN=400]="PK_CLICK_AGAIN"}
functionX(t){t[t.pre=0]="pre",t[t.process=1]="process",t[t.lastMinute=2]="lastMinute",t[t.end=3]="end",t[t.freeze=4]="freeze",t[t.punish=5]="punish",t[t.lastMinuteFreeze=6]="lastMinuteFreeze",t[t.lastMinuteEnd=7]="lastMinuteEnd",t[t.videoPunish=8]="videoPunish"}
functionX(t){t[t.pre=0]="pre",t[t.start=1]="start",t[t.process=2]="process",t[t.changeType=3]="changeType",t[t.end=4]="end",t[t.settle=5]="settle",t[t.sendGift=6]="sendGift",t[t.buffer=7]="buffer",t[t.triggerBoom=8]="triggerBoom",t[t.punish=9]="punish",t[t.settleNew=10]="settleNew",t[t.finalHit=11]="finalHit",t[t.videoPunishBegin=12]="videoPunishBegin",t[t.videoPunishEnd=13]="videoPunishEnd"}
functionX(t){t[t.process=0]="process",t[t.draw=1]="draw",t[t.win=2]="win",t[t.fail=3]="fail"}
functionX(t){t[t.random=1]="random",t[t.again=2]="again",t[t.force=3]="force"}
functionX(t){t[t.Web=1]="Web",t[t.Android=2]="Android",t[t.Ios=3]="Ios",t[t.H5=4]="H5"}
```

```
face:http(s)?://[is][0-3].hdslb.com/bfs/(face|baselabs)/[0-9a-f]{40}.(jpg|png|gif|webp)
face:http(s)?://[is][0-3].hdslb.com/bfs/face/member/noface.jpg
for i in range(1,len(a)):print(str(a[i]-a[i-1])[0:4])
(\d{16})?\{"cmd":[ ]{0,1}"XXXXXXXXXX",.{1,}\n
```

### 粉丝牌信息medal_info
| key					| type		| value | 备注 |
|-|-|-|-|
| anchor_roomid			| num		| 主播 长_短直播间ID | 
| anchor_uname			| str		| 主播用户名 | 
| guard_level			| num		| [舰长等级](#others) |
| icon_id				| num		| 0！ |
| is_lighted			| num		| 0: <br> 1: 七天内在直播间有互动 |
| medal_color			| num/str	| int(RGB24) / #RGB24 |
| medal_color_border	| num		| int(RGB24) |
| medal_color_end		| num		| int(RGB24) |
| medal_color_start		| num		| int(RGB24) |
| medal_level			| num		| 粉丝牌等级 |
| score					| num		| 亲密值 |
| medal_name			| str		| 粉丝团称号 |
| special				| str		| ""！ |
| target_id				| !num		| 主播uid |

#### medal__score
| score	| medal_level |
|-|-|
| 201	| 1 |
| 300	| 2 |
| 500	| 3 |
| 700	| 4 |
| 1000	| 5 |
| 1500	| 6 |
| 1600	| 7 |
| 1700	| 8 |
| 1900	| 9 |
| 5500	| 10 |
| 10000	| 11 |
| 10000	| 12 |
| 10000	| 13 |
| 15000	| 14 |
| 40000	| 15 |
| 50000	| 16 |
| 100000	| 17 |
| 250000	| 18 |
| 500000	| 19 |
| XXXXXX	| 20 |
| 50002000	| 21 |
| 50002500	| 22 |
| 50003000	| 23 |
| 50007500	| 24 |
| 50015000	| 25 |
| 50040000	| 26 |
| 50090000	| 27 |
| 50160000	| 28 |
| 50280000	| 29 |
| 50700000	| 30 |
| 51200000	| 31 |
| 52000000	| 32 |
| 52500000	| 33 |
| 53000000	| 34 |
| 53500000	| 35 |
| 54000000	| 36 |
| 57500000	| 37 |
| 60000000	| 38 |
| 65000000	| 39 |
| XXXXXXXX	| 40 |

#### medal_color
| medal_level	| medal_color | medal_color_border | medal_color_end | medal_color_start | 备注 |
| -: | -: | -: | -: | -: | - |
| 未互动		| 12632256	| 12632256	| 12632256	| 12632256	|
|     0　　		| 0 | 0 | 0 | 0 |
|  1- 4　　		| 6067854	| 6067854	| 6067854	| 6067854	|
|  5- 8　　		| 6126494	| 6126494	| 6126494	| 6126494	|
|  9-12　　		| 9272486	| 9272486	| 9272486	| 9272486	|
| 13-16　　		| 12478086	| 12478086	| 12478086	| 12478086	|
| 17-20　　		| 13081892	| 13081892	| 13081892	| 13081892	|
| 21-24	无　	| 1725515	| 1725515	| 5414290	| 1725515	|
| 21-24 舰长	| 1725515	| 1725515	| 5414290	| 6809855	|
| 21-24 提督	| 1725515	| 1725515	| 5414290	| ????????	|绝版
| 25-28	无　	| 398668	| 398668	| 6850801	| 398668	|
| 25-28 舰长	| 398668	| 398668	| 6850801	| 6809855	|
| 25-28 提督	| 398668	| 398668	| 6850801	| 16771156	|
| 25-28 总督	| 398668	| 398668	| 6850801	| 16771156	|
| 29-32	无　	| 2951253	| 2951253	| 10329087	| 2951253	|
| 29-32 舰长	| 2951253	| 2951253	| 10329087	| 6809855	|
| 29-32 提督	| 2951253	| 2951253	| 10329087	| 6809855	|
| 29-32 总督	| 2951253	| 2951253	| 10329087	| 6809855	|
| 33-36	无　	| 7996451	| 7996451	| 15304379	| 7996451	|
| 33-36 舰长	| 7996451	| 7996451	| 15304379	| 6809855	|
| 33-36 提督	| 7996451	| 7996451	| 15304379	| 16771156	|
| 33-36 总督	| 7996451	| 7996451	| 15304379	| 16771156	|
| 37-40	无　	| 16736523	| 16736523	| 16765060	| 16736523	|
| 37-40 舰长	| 16736523	| 16736523	| 16765060	| 6809855	|
| 37-40 提督	| 16736523	| 16736523	| 16765060	| 16771156	|
| 37-40 总督	| 16736523	| 16736523	| 16765060	| 16771156	|

### 分区ID
| area_id	| 父分区ID	| 父分区name	| area_name	|
|-|-|-|-|
| 21	| 1	| 娱乐	| 视频唱见 |
| 123	| 1	| 娱乐	| 户外 |
| 145	| 1	| 娱乐	| 视频聊天 |
| 207	| 1	| 娱乐	| 舞见 |
| 399	| 1	| 娱乐	| 日常 |
| 530	| 1	| 娱乐	| 萌宅领域 |
| 706	| 1	| 娱乐	| 情感 |
| 740	| 1	| 娱乐	| 聊天室 |
| 102	| 2	| 网游	| 最终幻想14 |
| 107	| 2	| 网游	| 其他网游 |
| 112	| 2	| 网游	| 龙之谷 |
| 114	| 2	| 网游	| 风暴英雄 |
| 115	| 2	| 网游	| 坦克世界 |
| 164	| 2	| 网游	| 堡垒之夜 |
| 173	| 2	| 网游	| 古剑奇谭OL |
| 176	| 2	| 网游	| 幻想全明星 |
| 181	| 2	| 网游	| 魔兽争霸3 |
| 239	| 2	| 网游	| 刀塔自走棋 |
| 240	| 2	| 网游	| APEX英雄 |
| 248	| 2	| 网游	| 战舰世界 |
| 249	| 2	| 网游	| 星际战甲 |
| 251	| 2	| 网游	| 枪神纪 |
| 252	| 2	| 网游	| 逃离塔科夫 |
| 288	| 2	| 网游	| 怀旧网游 |
| 298	| 2	| 网游	| 新游前瞻 |
| 300	| 2	| 网游	| 封印者 |
| 316	| 2	| 网游	| 战争雷霆 |
| 318	| 2	| 网游	| 使命召唤:战区 |
| 329	| 2	| 网游	| 无畏契约 |
| 331	| 2	| 网游	| 星战前夜：晨曦 |
| 383	| 2	| 网游	| 战意 |
| 388	| 2	| 网游	| FIFAONLINE4 |
| 459	| 2	| 网游	| 永恒轮回 |
| 472	| 2	| 网游	| CFHD |
| 487	| 2	| 网游	| 逆战 |
| 499	| 2	| 网游	| 剑网3缘起 |
| 505	| 2	| 网游	| 剑灵 |
| 519	| 2	| 网游	| 超激斗梦境 |
| 544	| 2	| 网游	| 新世界 |
| 551	| 2	| 网游	| 流放之路 |
| 574	| 2	| 网游	| 冒险岛 |
| 575	| 2	| 网游	| 生死狙击2 |
| 581	| 2	| 网游	| NBA2KOL2 |
| 590	| 2	| 网游	| 失落的方舟 |
| 596	| 2	| 网游	| 天涯明月刀 |
| 599	| 2	| 网游	| 洛奇英雄传 |
| 600	| 2	| 网游	| 猎杀对决 |
| 601	| 2	| 网游	| 综合射击 |
| 607	| 2	| 网游	| 激战2 |
| 610	| 2	| 网游	| QQ飞车 |
| 629	| 2	| 网游	| 反恐精英Online |
| 632	| 2	| 网游	| 黑色沙漠 |
| 633	| 2	| 网游	| FPS沙盒 |
| 634	| 2	| 网游	| 武装突袭 |
| 639	| 2	| 网游	| 阿尔比恩 |
| 642	| 2	| 网游	| 装甲战争 |
| 648	| 2	| 网游	| 风暴奇侠 |
| 649	| 2	| 网游	| 街头篮球 |
| 650	| 2	| 网游	| 骑士精神2 |
| 651	| 2	| 网游	| 艾尔之光 |
| 652	| 2	| 网游	| 大话西游 |
| 653	| 2	| 网游	| 新天龙八部 |
| 654	| 2	| 网游	| 诛仙世界 |
| 656	| 2	| 网游	| VRChat |
| 658	| 2	| 网游	| 星际公民 |
| 659	| 2	| 网游	| Squad战术小队 |
| 663	| 2	| 网游	| 洛奇 |
| 664	| 2	| 网游	| 跑跑卡丁车 |
| 666	| 2	| 网游	| 永劫无间 |
| 667	| 2	| 网游	| 赛尔号 |
| 668	| 2	| 网游	| 造梦西游 |
| 669	| 2	| 网游	| 洛克王国 |
| 670	| 2	| 网游	| 问道 |
| 677	| 2	| 网游	| 人间地狱 |
| 680	| 2	| 网游	| 超击突破 |
| 683	| 2	| 网游	| 奇迹MU |
| 684	| 2	| 网游	| 永恒之塔 |
| 685	| 2	| 网游	| QQ三国 |
| 686	| 2	| 网游	| 彩虹岛 |
| 690	| 2	| 网游	| 英魂之刃 |
| 691	| 2	| 网游	| 铁甲雄兵 |
| 695	| 2	| 网游	| 传奇 |
| 705	| 2	| 网游	| 创世战车 |
| 710	| 2	| 网游	| 梦三国 |
| 729	| 2	| 网游	| 战争与抉择 |
| 737	| 2	| 网游	| 泡泡堂 |
| 78	| 2	| 网游	| DNF |
| 80	| 2	| 网游	| 吃鸡行动 |
| 81	| 2	| 网游	| 三国杀 |
| 82	| 2	| 网游	| 剑网3 |
| 83	| 2	| 网游	| 魔兽世界 |
| 84	| 2	| 网游	| 300英雄 |
| 86	| 2	| 网游	| 英雄联盟 |
| 87	| 2	| 网游	| 守望先锋 |
| 88	| 2	| 网游	| 穿越火线 |
| 89	| 2	| 网游	| CS:GO |
| 91	| 2	| 网游	| 炉石传说 |
| 92	| 2	| 网游	| DOTA2 |
| 93	| 2	| 网游	| 星际争霸2 |
| 35	| 3	| 手游	| 王者荣耀 |
| 36	| 3	| 手游	| 阴阳师 |
| 37	| 3	| 手游	| Fate/GO |
| 39	| 3	| 手游	| 少女前线 |
| 40	| 3	| 手游	| 崩坏3 |
| 41	| 3	| 手游	| 狼人杀 |
| 42	| 3	| 手游	| 解密游戏 |
| 50	| 3	| 手游	| 部落冲突:皇室战争 |
| 98	| 3	| 手游	| 其他手游 |
| 113	| 3	| 手游	| 碧蓝航线 |
| 140	| 3	| 手游	| 决战！平安京 |
| 154	| 3	| 手游	| QQ飞车手游 |
| 156	| 3	| 手游	| 影之诗 |
| 163	| 3	| 手游	| 第五人格 |
| 178	| 3	| 手游	| 梦幻模拟战 |
| 189	| 3	| 手游	| 明日之后 |
| 203	| 3	| 手游	| 忍者必须死3 |
| 212	| 3	| 手游	| 非人学园 |
| 214	| 3	| 手游	| 雀姬 |
| 255	| 3	| 手游	| 明日方舟 |
| 256	| 3	| 手游	| 和平精英 |
| 258	| 3	| 手游	| BanGDream |
| 265	| 3	| 手游	| 跑跑卡丁车手游 |
| 269	| 3	| 手游	| 猫和老鼠手游 |
| 274	| 3	| 手游	| 新游评测 |
| 286	| 3	| 手游	| 百闻牌 |
| 292	| 3	| 手游	| 火影忍者手游 |
| 293	| 3	| 手游	| 战双帕弥什 |
| 303	| 3	| 手游	| 游戏王 |
| 321	| 3	| 手游	| 原神 |
| 330	| 3	| 手游	| 公主连结Re:Dive |
| 333	| 3	| 手游	| CF手游 |
| 342	| 3	| 手游	| 梦幻西游手游 |
| 343	| 3	| 手游	| DNF手游 |
| 352	| 3	| 手游	| 三国杀移动版 |
| 354	| 3	| 手游	| 综合棋牌 |
| 386	| 3	| 手游	| 使命召唤手游 |
| 389	| 3	| 手游	| 天涯明月刀手游 |
| 395	| 3	| 手游	| LOL手游 |
| 407	| 3	| 手游	| 游戏王：决斗链接 |
| 442	| 3	| 手游	| 坎公骑冠剑 |
| 448	| 3	| 手游	| 天地劫：幽城再临 |
| 464	| 3	| 手游	| 摩尔庄园手游 |
| 469	| 3	| 手游	| 荒野乱斗 |
| 473	| 3	| 手游	| 小动物之星 |
| 474	| 3	| 手游	| 哈利波特：魔法觉醒 |
| 478	| 3	| 手游	| 漫威超级战争 |
| 479	| 3	| 手游	| 黎明觉醒：生机 |
| 492	| 3	| 手游	| 暗黑破坏神：不朽 |
| 493	| 3	| 手游	| 宝可梦大集结 |
| 502	| 3	| 手游	| 暗区突围 |
| 504	| 3	| 手游	| 航海王热血航线 |
| 506	| 3	| 手游	| APEX手游 |
| 511	| 3	| 手游	| 漫威对决 |
| 514	| 3	| 手游	| 金铲铲之战 |
| 525	| 3	| 手游	| 少女前线：云图计划 |
| 538	| 3	| 手游	| 东方归言录 |
| 549	| 3	| 手游	| 崩坏：星穹铁道 |
| 550	| 3	| 手游	| 幻塔 |
| 571	| 3	| 手游	| 蛋仔派对 |
| 576	| 3	| 手游	| 恋爱养成游戏 |
| 598	| 3	| 手游	| 深空之眼 |
| 613	| 3	| 手游	| 重返帝国 |
| 615	| 3	| 手游	| 黑色沙漠手游 |
| 641	| 3	| 手游	| FIFA足球世界 |
| 643	| 3	| 手游	| 时空猎人3 |
| 644	| 3	| 手游	| 玛娜希斯回响 |
| 645	| 3	| 手游	| 猫之城 |
| 661	| 3	| 手游	| 奥比岛手游 |
| 675	| 3	| 手游	| 无期迷途 |
| 679	| 3	| 手游	| 休闲小游戏 |
| 687	| 3	| 手游	| 光遇 |
| 688	| 3	| 手游	| 300大作战 |
| 689	| 3	| 手游	| 香肠派对 |
| 704	| 3	| 手游	| 盾之勇者成名录：浪潮 |
| 717	| 3	| 手游	| 跃迁旅人 |
| 718	| 3	| 手游	| 空之要塞：启航 |
| 719	| 3	| 手游	| 欢乐斗地主 |
| 724	| 3	| 手游	| JJ斗地主 |
| 725	| 3	| 手游	| 环形战争 |
| 734	| 3	| 手游	| 弹弹堂 |
| 736	| 3	| 手游	| 猫咪公寓2 |
| 738	| 3	| 手游	| 长安幻想 |
| 190	| 5	| 电台	| 唱见电台 |
| 192	| 5	| 电台	| 聊天电台 |
| 193	| 5	| 电台	| 配音 |
| 216	| 6	| 单机游戏	| 我的世界 |
| 218	| 6	| 单机游戏	| 饥荒 |
| 219	| 6	| 单机游戏	| 以撒 |
| 220	| 6	| 单机游戏	| 辐射76 |
| 226	| 6	| 单机游戏	| 荒野大镖客2 |
| 227	| 6	| 单机游戏	| 刺客信条 |
| 228	| 6	| 单机游戏	| 精灵宝可梦 |
| 235	| 6	| 单机游戏	| 其他单机 |
| 236	| 6	| 单机游戏	| 主机游戏 |
| 237	| 6	| 单机游戏	| 怀旧游戏 |
| 243	| 6	| 单机游戏	| 全境封锁2 |
| 244	| 6	| 单机游戏	| 鬼泣5 |
| 245	| 6	| 单机游戏	| 只狼 |
| 257	| 6	| 单机游戏	| 全面战争 |
| 261	| 6	| 单机游戏	| 马力欧制造2 |
| 270	| 6	| 单机游戏	| 人类一败涂地 |
| 273	| 6	| 单机游戏	| 无主之地3 |
| 276	| 6	| 单机游戏	| 恐怖游戏 |
| 277	| 6	| 单机游戏	| 命运2 |
| 282	| 6	| 单机游戏	| 使命召唤19 |
| 283	| 6	| 单机游戏	| 独立游戏 |
| 295	| 6	| 单机游戏	| 方舟 |
| 302	| 6	| 单机游戏	| FORZA极限竞速 |
| 308	| 6	| 单机游戏	| 塞尔达传说 |
| 309	| 6	| 单机游戏	| 植物大战僵尸 |
| 313	| 6	| 单机游戏	| 仁王2 |
| 326	| 6	| 单机游戏	| 骑马与砍杀 |
| 341	| 6	| 单机游戏	| 盗贼之海 |
| 357	| 6	| 单机游戏	| 糖豆人 |
| 362	| 6	| 单机游戏	| NBA2K |
| 364	| 6	| 单机游戏	| 枪火重生 |
| 387	| 6	| 单机游戏	| 恐鬼症 |
| 424	| 6	| 单机游戏	| 鬼谷八荒 |
| 426	| 6	| 单机游戏	| 重生细胞 |
| 433	| 6	| 单机游戏	| 格斗游戏 |
| 439	| 6	| 单机游戏	| 恐惧之间 |
| 446	| 6	| 单机游戏	| 双人成行 |
| 460	| 6	| 单机游戏	| 弹幕互动玩法 |
| 463	| 6	| 单机游戏	| 亿万僵尸 |
| 500	| 6	| 单机游戏	| 体育游戏 |
| 507	| 6	| 单机游戏	| 胡闹厨房 |
| 535	| 6	| 单机游戏	| 暗黑破坏神2 |
| 548	| 6	| 单机游戏	| 帝国时代4 |
| 555	| 6	| 单机游戏	| 艾尔登法环 |
| 570	| 6	| 单机游戏	| 策略游戏 |
| 578	| 6	| 单机游戏	| 怪物猎人 |
| 579	| 6	| 单机游戏	| 战神 |
| 580	| 6	| 单机游戏	| 彩虹六号：异种 |
| 582	| 6	| 单机游戏	| 暖雪 |
| 583	| 6	| 单机游戏	| 文字游戏 |
| 586	| 6	| 单机游戏	| 消逝的光芒2 |
| 591	| 6	| 单机游戏	| DreadHunger |
| 592	| 6	| 单机游戏	| 恋爱模拟游戏 |
| 593	| 6	| 单机游戏	| 泰拉瑞亚 |
| 594	| 6	| 单机游戏	| 全面战争：战锤3 |
| 597	| 6	| 单机游戏	| 战地风云 |
| 636	| 6	| 单机游戏	| 聚会游戏 |
| 678	| 6	| 单机游戏	| 游戏速通 |
| 693	| 6	| 单机游戏	| 红色警戒2 |
| 694	| 6	| 单机游戏	| 斯普拉遁3 |
| 700	| 6	| 单机游戏	| 卧龙：苍天陨落 |
| 707	| 6	| 单机游戏	| 禁闭求生 |
| 708	| 6	| 单机游戏	| FIFA23 |
| 721	| 6	| 单机游戏	| 生化危机 |
| 723	| 6	| 单机游戏	| 战锤40K:暗潮 |
| 739	| 6	| 单机游戏	| 风帆纪元 |
| 747	| 6	| 单机游戏	| 霍格沃茨之遗 |
| 748	| 6	| 单机游戏	| 狂野之心 |
| 749	| 6	| 单机游戏	| 英雄连3 |
| 750	| 6	| 单机游戏	| 原子之心 |
| 751	| 6	| 单机游戏	| 森林之子 |
| 752	| 6	| 单机游戏	| 歧路旅人2 |
| 753	| 6	| 单机游戏	| Roblox |
| 754	| 6	| 单机游戏	| THEFINALS |
| 371	| 9	| 虚拟主播	| 虚拟日常 |
| 743	| 9	| 虚拟主播	| TopStar |
| 744	| 9	| 虚拟主播	| 虚拟Singer |
| 745	| 9	| 虚拟主播	| 虚拟Gamer |
| 746	| 9	| 虚拟主播	| 虚拟声优 |
| 33	| 10	| 生活	| 影音馆 |
| 367	| 10	| 生活	| 美食 |
| 369	| 10	| 生活	| 萌宠 |
| 378	| 10	| 生活	| 时尚 |
| 624	| 10	| 生活	| 搞笑 |
| 627	| 10	| 生活	| 手工绘画 |
| 628	| 10	| 生活	| 运动 |
| 646	| 10	| 生活	| 生活分享 |
| 372	| 11	| 知识	| 校园学习 |
| 375	| 11	| 知识	| 科技 |
| 376	| 11	| 知识	| 社科法律心理 |
| 377	| 11	| 知识	| 职场·技能 |
| 701	| 11	| 知识	| 科学科普 |
| 702	| 11	| 知识	| 人文历史 |
| 561	| 13	| 赛事	| 游戏赛事 |
| 562	| 13	| 赛事	| 体育赛事 |
| 563	| 13	| 赛事	| 赛事综合 |
| 300000	| 300	| 购物	| 购物 |

# url
[url_01]:http://i0.hdslb.com/bfs/album/19cc369845a2709464f3df9c38bbdea019619acd.png
[url_02]:http://i0.hdslb.com/bfs/album/ea58d134636f05ddc208a13889dd054ae45eb6ef.png
[url_03]:http://i0.hdslb.com/bfs/b/d1f96d0ad5341b214663b62e0de32dcbf776f894.png
[url_04]:http://i0.hdslb.com/bfs/b/1d8fc3daf9201d70189a3778e605d2acf9cae7e9.png
[url_05]:http://i0.hdslb.com/bfs/b/a00a37f4a1f419a42f04f535147d21ac96f27a79.png
[url_06]:http://i0.hdslb.com/bfs/b/ee3aca3dbc22087341cf312d71a1354af527e444.png
[url_07]:http://i0.hdslb.com/bfs/b/c7d3e7d452e4ff5caf719a8e422eca10e5caad1f.png
[url_08]:http://i0.hdslb.com/bfs/b/7e947f8e64c7802a16de7ebec8a8e290160ec668.png
[url_09]:http://i0.hdslb.com/bfs/archive/03ef3f34944e0f78b1b4050fc3f9705d1fa905e3.png
[url_10]:http://i0.hdslb.com/bfs/b/44338bca6bb98a34da40698beb4ee7d19aea92a6.png
[url_11]:http://i0.hdslb.com/bfs/b/4312fb7b155646fc6fd5f6f8a6a07a062d82587c.png
[url_12]:http://i0.hdslb.com/bfs/b/a4b1c7f03e687f680f7c3629c530e3fdd77d63ed.png
[url_13]:http://i0.hdslb.com/bfs/album/5ec559dbd4d54f8c1e76021d52eb9807de94bfb9.png
[url_14]:http://i0.hdslb.com/bfs/b/2eec72efb74244eed5c2f28ce5628de4e9f9c9e8.png
[url_15]:https://i0.hdslb.com/bfs/live/cb2e160ac4f562b347bb5ae6e635688ebc69580f.png
[url_17]:https://i0.hdslb.com/bfs/live/b4961bcfba56a26b69c35690dfcbdabbeb973c64.png
[url_16]:https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png
[热门榜功能下线公告]:https://link.bilibili.com/p/eden/news#/newsdetail?id=3270
