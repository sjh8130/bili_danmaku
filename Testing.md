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

## commandDms
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
| idStr		| 10	| string	| 弹幕id str类型 |

### command__类型
| command 7		| content	|
| -				| -			|
| #ACTORFOLLOW# | "合作up主" |
| #ATTENTION#	| "关注弹幕" |
| #GRADE#		| "哔瓣评分" |
| #LINK#		| **自定义内容** |
| #RESERVE#		| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#			| **自定义内容** |
| #VOTE#		| "投票弹幕" |

### ACTORFOLLOW__合作up主
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_01] |
| mid					| num	| **合作up主 mid** |
| midstr				| str	| **合作up主 mid string** |
| face					| str	| **合作up主 头像 URL** |

### ATTENTION__关注
| key					| type	| value | 备注 |
| -						| -		| -	| - |
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_02] |
| type					| num	| 2 |
| arc_type				| num	| 0 |

### GRADE__评分
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

### LINK__链接
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

### RESERVE__预约
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
| live_popularity_str	| str	| 直播 :"`x.y万人气`" / "`x人看过`/ "`x.y万人看过`"  |
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

### UP__带有【UP】的~~普通~~弹幕
| key					| type	| value	|
| -						| -		| -		|
| icon					| str	| **UP主头像URL** |

### VOTE__投票
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

#### VOTE__options
| key					| type	| value	|
| -						| -		| -		|
| idx					| num	| start:1 |
| desc					| str	| **选项内容** |
| cnt					| num	| 0? |
| has_self_def			| bool	| false? |

### posX,posY
| key	| min		| max	|
| -		| -:		| -:	|
| posX	|	118		|	549	|
| posY	|	80.5	|	889	|

## 直播弹幕格式
~~最低发包间隔1ms~~
| link | name | desc |
| - | - | - |
| [link](#ACTIVITY_MATCH_GIFT)	| ACTIVITY_MATCH_GIFT					| |
| [link](#ANCHOR_LOT_CHECKSTATUS)	| ANCHOR_LOT_CHECKSTATUS			| 抽奖检查 |
| [link](#ANCHOR_LOT_START)	| ANCHOR_LOT_START							| 抽奖开始 |
| [link](#ANCHOR_LOT_END)	| ANCHOR_LOT_END							| 抽奖结束 |
| [link](#ANCHOR_LOT_AWARD)	| ANCHOR_LOT_AWARD							| 抽奖结果 |
| [link](#AREA_RANK_CHANGED)	| AREA_RANK_CHANGED						| |
| [link](#BOX_ACTIVITY_START)	| BOX_ACTIVITY_START					| |
| [link](#CHANGE_ROOM_INFO)	| CHANGE_ROOM_INFO							| |
| [link](#CHASE_FRAME_SWITCH)	| CHASE_FRAME_SWITCH					| |
| [link](#COMBO_SEND)	| COMBO_SEND									| |
| [link](#COMMON_NOTICE_DANMAKU)	| COMMON_NOTICE_DANMAKU				| |
| [link](#CUT_OFF)	| CUT_OFF											| 切断直播！|
| [link](#DANMU_AGGREGATION)	| DANMU_AGGREGATION						| 抽奖通知 |
| [link](#DANMU_GIFT_LOTTERY_AWARD)	| DANMU_GIFT_LOTTERY_AWARD			| |
| [link](#DANMU_GIFT_LOTTERY_END)	| DANMU_GIFT_LOTTERY_END			| |
| [link](#DANMU_GIFT_LOTTERY_START)	| DANMU_GIFT_LOTTERY_START			| |
| [link](#DANMU_MSG)	| DANMU_MSG										| 弹幕！ |
| [link](#DANMU_TAG_CHANGE)	| DANMU_TAG_CHANGE							| |
| [link](#ENTRY_EFFECT)	| ENTRY_EFFECT									| 进入直播间特效 |
| [link](#ENTRY_EFFECT_MUST_RECEIVE)	| ENTRY_EFFECT_MUST_RECEIVE		| |
| [link](#FULL_SCREEN_SPECIAL_EFFECT)	| FULL_SCREEN_SPECIAL_EFFECT	| |
| [link](#GOTO_BUY_FLOW)	| GOTO_BUY_FLOW								| 移动端 购买* |
| [link](#GIFT_PANEL_PLAN)	| GIFT_PANEL_PLAN							| |
| [link](#GIFT_STAR_PROCESS)	| GIFT_STAR_PROCESS						| |
| [link](#GUARD_ACHIEVEMENT_ROOM)	| GUARD_ACHIEVEMENT_ROOM			| |
| [link](#GUARD_BENEFIT_RECEIVE)	| GUARD_BENEFIT_RECEIVE				| |
| [link](#GUARD_BUY)			| GUARD_BUY								| 舰长购买 |
| [link](#GUARD_HONOR_THOUSAND)	| GUARD_HONOR_THOUSAND					| |
| [link](#GUARD_LOTTERY_START)	| GUARD_LOTTERY_START					| |
| [link](#GUARD_WINDOWS_OPEN)	| GUARD_WINDOWS_OPEN					| |
| [link](#HOT_BUY_NUM)	| HOT_BUY_NUM									| 推广购物 |
| link	| ~~HOT_RANK_CHANGED~~											| [已移除][热门榜功能下线公告]|
| link	| ~~HOT_RANK_CHANGED_V2~~										| [已移除][热门榜功能下线公告]|
| link	| ~~HOT_RANK_SETTLEMENT~~										| [已移除][热门榜功能下线公告]|
| link	| ~~HOT_RANK_SETTLEMENT_V2~~									| [已移除][热门榜功能下线公告]|
| link	| ~~HOT_ROOM_NOTIFY~~											| |
| [link](#HOUR_RANK_AWARDS)	| HOUR_RANK_AWARDS 							| |
| [link](#INTERACT_WORD)	| INTERACT_WORD								| 进入直播间/关注主播 |
| [link](#LIKE_INFO_V3_CLICK)	| LIKE_INFO_V3_CLICK					| 移动端 用户点赞|
| [link](#LIKE_INFO_V3_UPDATE)	| LIKE_INFO_V3_UPDATE					| 用户点赞更新 |
| [link](#LIKE_SO_HOT)	| LIKE_SO_HOT 									| |
| [link](#LITTLE_MESSAGE_BOX)	| LITTLE_MESSAGE_BOX					| |
| [link](#LITTLE_TIPS)	| LITTLE_TIPS 									| |
| [link](#LIVE)	| LIVE													| |
| [link](#LIVE_INTERNAL_ROOM_LOGIN)	| LIVE_INTERNAL_ROOM_LOGIN			| |
| [link](#LIVE_OPEN_PLATFORM_CLOUD_GAME)	| LIVE_OPEN_PLATFORM_CLOUD_GAME		| |
| [link](#LIVE_OPEN_PLATFORM_GAME)	| LIVE_OPEN_PLATFORM_GAME			| |
| [link](#LIVE_PLAYER_LOG_RECYCLE)	| LIVE_PLAYER_LOG_RECYCLE			| |
| [link](#LOL_ACTIVITY)	| LOL_ACTIVITY									| |
| [link](#MATCH_TEAM_GIFT_RANK)	| MATCH_TEAM_GIFT_RANK					| |
| [link](#MESSAGEBOX_USER_GAIN_MEDAL)	| MESSAGEBOX_USER_GAIN_MEDAL	| |
| [link](#MESSAGEBOX_USER_MEDAL_CHANGE)	| MESSAGEBOX_USER_MEDAL_CHANGE	| |
| [link](#MESSAGEBOX_USER_MEDAL_COMPENSA)	| MESSAGEBOX_USER_MEDAL_COMPENSATION | |
| [link](#MILESTONE_UPDATE_EVENT)	| MILESTONE_UPDATE_EVENT 			| |
| [link](#MULTI_VOICE_STATUS_SYNC)	| MULTI_VOICE_STATUS_SYNC			| |
| [link](#NOTICE_MSG)	| NOTICE_MSG									| 滚动横幅 |
| [link](#ONLINE_RANK_COUNT)	| ONLINE_RANK_COUNT						| 高能用户 |
| [link](#ONLINE_RANK_TOP3)	| ONLINE_RANK_TOP3							| 高能用户前三恭喜 |
| [link](#ONLINE_RANK_V2)	| ONLINE_RANK_V2							| 高能用户TOP7 |
| [link](#PK_AGAIN)	| PK_AGAIN | |
| [link](#PK_BATTLE_CRIT)	| PK_BATTLE_CRIT | |
| [link](#PK_BATTLE_END)	| PK_BATTLE_END | |
| [link](#PK_BATTLE_FINAL_PROCESS)	| PK_BATTLE_FINAL_PROCESS | |
| [link](#PK_BATTLE_GIFT)	| PK_BATTLE_GIFT | |
| [link](#PK_BATTLE_PRE_NEW)	| PK_BATTLE_PRE_NEW | |
| [link](#PK_BATTLE_PRO_TYPE)	| PK_BATTLE_PRO_TYPE | |
| [link](#PK_BATTLE_PROCESS_NEW)	| PK_BATTLE_PROCESS_NEW | |
| [link](#PK_BATTLE_PUNISH_END)	| PK_BATTLE_PUNISH_END | |
| [link](#PK_BATTLE_RANK_CHANGE)	| PK_BATTLE_RANK_CHANGE | |
| [link](#PK_BATTLE_SETTLE_NEW)	| PK_BATTLE_SETTLE_NEW | |
| [link](#PK_BATTLE_SETTLE_V2)	| PK_BATTLE_SETTLE_V2 | |
| [link](#PK_BATTLE_SPECIAL_GIFT)	| PK_BATTLE_SPECIAL_GIFT | |
| [link](#PK_BATTLE_START_NEW)	| PK_BATTLE_START_NEW | |
| [link](#PK_BATTLE_VIDEO_PUNISH_BEGIN)	| PK_BATTLE_VIDEO_PUNISH_BEGIN | |
| [link](#PK_BATTLE_VIDEO_PUNISH_END)	| PK_BATTLE_VIDEO_PUNISH_END | |
| [link](#PK_BATTLE_VOTES_ADD)	| PK_BATTLE_VOTES_ADD | |
| [link](#PK_END)	| PK_END | |
| [link](#PK_LOTTERY_START)	| PK_LOTTERY_START | |
| [link](#PK_MATCH)	| PK_MATCH | |
| [link](#PK_MIC_END)	| PK_MIC_END | |
| [link](#PK_PRE)	| PK_PRE | |
| [link](#PK_PROCESS)	| PK_PROCESS | |
| [link](#PK_SETTLE)	| PK_SETTLE | |
| [link](#PK_START)	| PK_START | |
| [link](#PLAY_TOGETHER)	| PLAY_TOGETHER | |
| [link](#POPULAR_RANK_CHANGED)	| POPULAR_RANK_CHANGED | |
| [link](#POPULARITY_RED_POCKET_NEW)	| POPULARITY_RED_POCKET_NEW | |
| [link](#POPULARITY_RED_POCKET_START)	| POPULARITY_RED_POCKET_START | |
| [link](#POPULARITY_RED_POCKET_WINNER_L)	| POPULARITY_RED_POCKET_WINNER_LIST | |
| [link](#PREPARING)	| PREPARING																| 下播 |
| [link](#RAFFLE_END)	| RAFFLE_END | |
| [link](#RAFFLE_START)	| RAFFLE_START | |
| [link](#RANK_REM)	| RANK_REM | |
| [link](#RED_POCKET_START)	| RED_POCKET_START | |
| [link](#REENTER_LIVE_ROOM)	| REENTER_LIVE_ROOM | |
| [link](#Revenue_PayLimit)	| Revenue_PayLimit | |
| [link](#ROOM_BANNER)	| ROOM_BANNER | |
| [link](#ROOM_BLOCK_INTO)	| ROOM_BLOCK_INTO | |
| [link](#ROOM_BLOCK_MSG)	| ROOM_BLOCK_MSG | |
| [link](#ROOM_CHANGE)	| ROOM_CHANGE | |
| [link](#ROOM_KICKOUT)	| ROOM_KICKOUT | |
| [link](#ROOM_LIMIT)	| ROOM_LIMIT | |
| [link](#ROOM_LOCK)	| ROOM_LOCK | |
| [link](#ROOM_RANK)	| ROOM_RANK | |
| [link](#ROOM_REAL_TIME_MESSAGE_UPDATE)	| ROOM_REAL_TIME_MESSAGE_UPDATE		| |
| [link](#ROOM_REFRESH)	| ROOM_REFRESH | |
| [link](#ROOM_SILENT_OFF)	| ROOM_SILENT_OFF | |
| [link](#ROOM_SILENT_ON)	| ROOM_SILENT_ON | |
| [link](#ROOM_SKIN_MSG)	| ROOM_SKIN_MSG | |
| [link](#SEND_GIFT)	| SEND_GIFT							| 送礼物 |
| [link](#SEND_GIFT_V2)	| SEND_GIFT_V2 | |
| [link](#SEND_TOP)	| SEND_TOP | |
| [link](#SHOPPING_CART_SHOW)	| SHOPPING_CART_SHOW | |
| [link](#SPECIAL_GIFT)	| SPECIAL_GIFT						| |
| [link](#STARLIVE_PK_MSG)	| STARLIVE_PK_MSG | |
| [link](#STOP_LIVE_ROOM_LIST)	| STOP_LIVE_ROOM_LIST				| |
| [link](#SUPER_CHAT_AUDIT)	| SUPER_CHAT_AUDIT | |
| [link](#SUPER_CHAT_ENTRANCE)	| SUPER_CHAT_ENTRANCE | |
| [link](#SUPER_CHAT_MESSAGE)	| SUPER_CHAT_MESSAGE						| SuperChat |
| [link](#SUPER_CHAT_MESSAGE_DELETE)	| SUPER_CHAT_MESSAGE_DELETE			| SuperChat 删除 |
| [link](#SUPER_CHAT_MESSAGE_JPN)	| SUPER_CHAT_MESSAGE_JPN				| SuperChat 日本語 |
| [link](#THERMAL_STORM_DANMU_BEGIN)	| THERMAL_STORM_DANMU_BEGIN | |
| [link](#THERMAL_STORM_DANMU_CANCEL)	| THERMAL_STORM_DANMU_CANCEL | |
| [link](#THERMAL_STORM_DANMU_OVER)	| THERMAL_STORM_DANMU_OVER | |
| [link](#THERMAL_STORM_DANMU_UPDATE)	| THERMAL_STORM_DANMU_UPDATE | |
| [link](#TV_END)	| TV_END | |
| [link](#TV_START)	| TV_START | |
| [link](#USER_PANEL_RED_ALARM)	| USER_PANEL_RED_ALARM | |
| [link](#USER_TITLE_GET)	| USER_TITLE_GET | |
| [link](#USER_TOAST_MSG)	| USER_TOAST_MSG					| |
| [link](#VIDEO_CONNECTION_JOIN_END)	| VIDEO_CONNECTION_JOIN_END | |
| [link](#VIDEO_CONNECTION_JOIN_START)	| VIDEO_CONNECTION_JOIN_START | |
| [link](#VIDEO_CONNECTION_MSG)	| VIDEO_CONNECTION_MSG | |
| [link](#VOICE_JOIN_STATUS)	| VOICE_JOIN_STATUS | |
| [link](#VTR_GIFT_LOTTERY)	| VTR_GIFT_LOTTERY | |
| [link](#WARNING)	| WARNING | |
| [link](#WATCH_LPL_EXPIRED)	| WATCH_LPL_EXPIRED | |
| [link](#WATCHED_CHANGE)	| WATCHED_CHANGE								| 观看人数 |
| [link](#WEB_REPORT_CONTROL)	| WEB_REPORT_CONTROL | |
| [link](#WIDGET_BANNER)	| WIDGET_BANNER | |
| [link](#WIN_ACTIVITY)	| WIN_ACTIVITY | |
| [link](#WIN_ACTIVITY_USER)	| WIN_ACTIVITY_USER | |

### WARNING
[TOP](#直播弹幕格式)  
`Anchor`
| key				| type	| value |
| - | - | - |
| cmd				| str	| "WARNING" |
| msg				| str	| ? |

### LIVE
[TOP](#直播弹幕格式)  
开播
| key 7,8			| type	| value |
| - | - | - |
| cmd				| str	| "LIVE" |
| live_key			| str	| ?*int64* |
| voice_background	| str	| ?"" |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| ?"live_mng" |
| live_model		| num	| ?0 |
| live_time	*		| num	| 开播时间TimeStamp(秒) |
| roomid			| num	| 长_短直播间ID |
```json
{
	"cmd":"LIVE",
	"live_key":"123456789012345678",
	"voice_background":"",
	"sub_session_key":"123456789012345678sub_time:1234567890",
	"live_platform":"events_broadcast",
	"live_model":0,
	"live_time":1234567890,	// ？仅在开播时存在
	"roomid":12345
}
```

### SEND_GIFT
[TOP](#直播弹幕格式)  
送礼物
| key	| type | value |
| - | - | - |
| cmd	| str	| "SEND_GIFT" |
| data	| obj	| |
#### SEND_GIFT__data
| key 54				| type		| value | 备注 |
| - | - | - | - |
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
| - | - | - |
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
| - | - | - |
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
| - | - | - |
| uid					| num		| 接收者uid |
| uname					| str		| 接收者用户名 |

### ONLINE_RANK_V2
[TOP](#直播弹幕格式)  
高能用户前七(左)，实时
| key	| type	| value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_V2" |
| data	| obj	| |
#### ONLINE_RANK_V2__data
| key		| type			| value |
| - | - | - |
| list		| array(obj)	| _7_ |
| rank_type	| str			| "gold-rank" |
#### ONLINE_RANK_V2__data__list
| array[obj] 6			| type	| value |
| - | - | - |
| list[i].uid			| num | uid |
| list[i].face			| str | 头像URL |
| list[i].score			| str | 贡献值 |
| list[i].uname			| str | 用户名 |
| list[i].rank			| num | 排名(1-7) |
| list[i].guard_level	| num | 舰长等级 |

### ONLINE_RANK_TOP3
[TOP](#直播弹幕格式)  
高能用户前三(左)
| key	| type	| value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_TOP3" |
| data	| obj	| |
#### ONLINE_RANK_TOP3__data
| key		| type			| value |
| - | - | - |
| dmscore	| num			| 112 |
| list		| array(obj)	| _1_ |
#### ONLINE_RANK_TOP3__data__list
| array[obj] 2	| type	| value |
| - | - | - |
| list[0]msg	| str	| `f"恭喜 <%{用户名}%> 成为高能用户"` |
| list[0]rank	| num	| 排名(1-3) |

### ONLINE_RANK_COUNT
[TOP](#直播弹幕格式)  
高能用户人数(观众人数)
约每N*5秒发送一次  
| key | type | value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_COUNT" |
| data	| obj	| |
#### ONLINE_RANK_COUNT__data
| key	| type	| value |
| - | - | - |
| count | num	| 最大值约为10000[1-100xx] |

### INTERACT_WORD
[TOP](#直播弹幕格式)  
进入直播间、关注主播通知（高精度）500ms
| key | type	| value |
| - | - | - |
| cmd	| str	| "INTERACT_WORD" |
| data	| obj	| |
#### INTERACT_WORD__data
| key 18			| type	| value |
| - | - | - |
| contribution		| obj	| ？[XXX](#INTERACT_WORD__data__contribution) |
| core_user_type	| num	| ?大部分为0[0-5] |
| dmscore			| num	| 2*N |
| fans_medal		| obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| identities		| array	| [identities](#others) |
| is_spread			| num	| 0,1 |
| msg_type			| num	| |
| privilege_type	| num	| [privilege_type](#others) is_spread==1:`0` |
| roomid			| num	| 长_短直播间ID |
| score				| num	| TimeStamp(毫秒) |
| spread_desc		| str	| is_spread==1:"流量包推广" |
| spread_info		| str	| is_spread==1:"#FF649E" |
| tail_icon			| num	| [0,101,102] |
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
#### INTERACT_WORD__core_user_type
[BACK](#INTERACT_WORD__data)
|core_user_type|等级|VIP|粉丝牌&舰长|直播观众等级|直播UP|粉丝|关注|认证|
|-|-|-|-|-|-|-|-|-|
|1|LV6+|年度大会员|30总督|UL25+||55|1300||
|2|LV6|年度大会员|||UP40|257w||个人认证：百大|
|2|LV6|年度大会员|30总督，25个舰长||UP28+|3w|||
#### INTERACT_WORD__data__contribution
[BACK](#INTERACT_WORD__data)
| key | type	| value |
| - | - | - |
| grade | num	| ？ |
```json
"score":1674560093850
"timestamp":1674560093
"trigger_time":1674560092752782600
```

### WATCHED_CHANGE
[TOP](#直播弹幕格式)  
约每5秒发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "WATCHED_CHANGE" |
| data	| obj	| |
#### WATCHED_CHANGE__data
| key 3			| type	| value |
| - | - | - |
| num			| num	| 人数 |
| text_small	| str	| str(num) <br> "x.y万" |
| text_large	| str	| f"num人看过" <br> "x.y万人看过" |

### ROOM_REAL_TIME_MESSAGE_UPDATE
[TOP](#直播弹幕格式)  
(每N*60秒&数值更新)发送一次，更新关注数、粉丝团人数
| key | type | value |
| - | - | - |
| cmd	| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data	| obj	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE__data
| key 4			| type	| value |
| - | - | - |
| roomid		| num	| 长直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1? |
| fans_club		| num	| 粉丝团成员(活跃人数) |

### LIKE_INFO_V3_CLICK
[TOP](#直播弹幕格式)  
点赞(移动端 双击屏幕)，和`LIKE_INFO_V3_UPDATE`同时发送，实时&每5秒最多发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "LIKE_INFO_V3_CLICK" |
| data	| obj	| |
#### LIKE_INFO_V3_CLICK__data
| key 11			| type	| value |
| - | - | - |
| show_area			| num	| 0 <br> 1(30s) |
| msg_type			| num	| 6 |
| like_icon			| str	| [图标][img_16] |
| uid				| num	|  |
| like_text			| str	| "为主播点赞了" |
| uname				| str	|  |
| uname_color		| str	| "" |
| identities		| array	| [identities](#others) |
| fans_medal		| obj	| [fans_medal](#粉丝牌信息medal_info) |
| contribution_info	| obj	| |
| dmscore			| num	| 20 |
#### LIKE_INFO_V3_CLICK__data__contribution_info
| key | type | value |
| - | - | - |
| grade | num | 0 |

### LIKE_INFO_V3_UPDATE
[TOP](#直播弹幕格式)  
点赞(移动端 双击屏幕)，和`LIKE_INFO_V3_CLICK`同时发送，实时&每5秒最多发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "LIKE_INFO_V3_UPDATE" |
| data	| obj	| |
#### LIKE_INFO_V3_UPDATE__data
| key			| type	| value |
| - | - | - |
| click_count	| num	| 点赞数量 |

### ENTRY_EFFECT
[TOP](#直播弹幕格式)  
欢迎舰长进入直播间，高精度
| key | type | value |
| - | - | - |
| cmd	| str	| "ENTRY_EFFECT" |
| data	| obj	| |
#### ENTRY_EFFECT__data
| key 28					| type | value | |
| - | - | - | - |
| id						| num	| |
| uid						| num	| uid |
| target_id					| num	| 主播uid |
| mock_effect				| num	| 0? |
| face						| str	| 头像URL |
| privilege_type			| num	| [privilege_type](#others) |
| copy_writing				| str	| `f"欢迎(舰长\|提督\|) <%{用户名}%> 进入直播间"` |限长7字符，省略号为`...`
| copy_color				| str	|  |
| highlight_color			| str	|  |
| priority					| num	| 1? |
| basemap_url				| str	| basemap_url=web_basemap_url |
| show_avatar				| num	| 1 |
| effective_time			| num	| effective_time=web_effective_time |
| web_basemap_url			| str	| basemap_url=web_basemap_url |
| web_effective_time		| num	| effective_time=web_effective_time |
| web_effect_close			| num	| 2,4,135,136,137:0 <br> 253,254,291,314,315,316,325,328:1 |
| web_close_time			| num	| 136,137,253,254,291,314,315,316,325,328:900 <br> 4:0 |
| business					| num	| ~~3:`<^icon^>` 1:提督、舰长、`<^icon^> 舰长` 4:用户，无空格~~ |
| copy_writing_v2			| str	| `f"欢迎 <^icon^> <%{用户名}%> 进入直播间"`<br>`f"欢迎(提督\|舰长) <%{用户名}%> 进入直播间"`<br>`f"欢迎<%{用户名}%>进入直播间"`**无空格**<br>`f"欢迎 <^icon^> 舰长 <%{用户名}%> 进入直播间"`<br> |限长6字符，省略号为`…`
| icon_list					| array	|  |
| max_delay_time			| num	| 7 |
| trigger_time				| num	| TimeStamp(皮秒?) |
| identities				| num	| [identities](#others) |
| effect_silent_time		| float	| 0 |
| effective_time_new		| num	| Tag_1 |
| web_dynamic_url_webp		| str	| Tag_1 |
| web_dynamic_url_apng		| str	| Tag_1 |
| mobile_dynamic_url_webp	| str	| Tag_1 |

### STOP_LIVE_ROOM_LIST
[TOP](#直播弹幕格式)  
每30秒发送一次~~(`HH:mm:29`,`HH:mm:59`)~~，推送很多[12,223]直播间ID?
| key | type | value |
| - | - | - |
| cmd	| str	| "STOP_LIVE_ROOM_LIST" |
| data	| obj	| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type	| value |
| - | - | - |
| room_id_list	| array	| [1,2,3,...] |

### GUARD_BUY
[TOP](#直播弹幕格式)  
舰长购买  
| key | type | value |
| - | - | - |
| cmd	| str	| "GUARD_BUY" |
| data	| obj	| |
#### GUARD_BUY__data
| key 9			| type	| value |
| - | - | - |
| uid			| num	| uid |
| username		| str	|  |
| guard_level	| num	| [guard_level](#others) |
| num			| num	| 购买数量 |
| price			| num	| 单价 RMB*1000 |
| gift_id		| num	| 10003:"舰长" 10002:"提督" 10001:"总督" |
| gift_name		| str	|  |
| start_time	| num	| 购买时间 TimeStamp(秒) |
| end_time		| num	| 购买时间 TimeStamp(秒) |

### USER_TOAST_MSG
[TOP](#直播弹幕格式)  
舰长购买通知，实时，显示在聊天区
| key | type | value |
| - | - | - |
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG__data
| key 23				| type	| value |
| - | - | - |
| anchor_show			| bool	| true |
| color					| str	| 舰长:"#00D1F1" <br> 提督:"#E17AFF" <br> 总督:"" |
| dmscore				| num	| 舰长:90 提督:96 总督: |
| effect_id				| num	| 舰长:397 提督:398 总督: |
| end_time				| num	| TimeStamp(秒) |
| face_effect_id		| num	| 舰长:44 <br> 提督:43 <br> 总督: |
| gift_id				| num	| 舰长:10003<br> 提督:10002 <br> 总督:10001 |
| guard_level			| num	| [guard_level](#others) |
| is_show				| num	| 0 |
| num					| num	| 1? |
| op_type				| num	| 3:PC? 2:iOS 1:Android? |
| payflow_id			| str	| 订单号(25) |
| price					| num	| RMB*1000 <br> 连续订阅舰长138，?158，舰长198 <br> 提督1998 <br> 总督19998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| 舰长:590 <br> 提督:591 <br> 总督: |
| start_time			| num	| 购买时间 TimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播当前舰长数 |
| toast_msg				| str	| `f"<%{用户名}%> 自动续费了舰长"` <br> `f"<%{用户名}%> 开通了(舰长\|提督\|总督)，今天是TA陪伴主播的第{}天"` |
| uid					| num	| uid |
| unit					| str	| "月"? |
| user_show				| bool	| true |
| username				| str	| 用户名 |

### NOTICE_MSG
[TOP](#直播弹幕格式)  
滚动横幅
| key 17		| type	| value |
| - | - | - |
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
| - | - | - |
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
| - | - | - |
| head_icon		| str	| |
| tail_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| time			| num	| |
#### NOTICE_MSG__side
| key			| type	| value |
| - | - | - |
| head_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| border		| str	| |
#### NOTICE_MSG__scatter
| key	| type | value |
| - | - | - |
| min	| num | 0 |
| max	| num | 0 |
#### NOTICE_MSG__例
```json
{"cmd":"NOTICE_MSG","id":1,"name":"全区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/b29add66421580c3e680d784a827202e512a40a0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/49869a52d6225a3e70bbf1f4da63f199a95384b2.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":24,"tail_icon_fan":4,"background":"#66A74EFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/ec9b374caec5bd84898f3780a10189be96b86d4e.png","tail_icon":"","background":"#85B971FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个浪漫城堡，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂<%{主播}%>X个浪漫城堡，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32132","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个次元之城，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个次元之城，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31087","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个鸿运小电视，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个鸿运小电视，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31115","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个超级战舰，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个超级战舰，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31483","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂:<%{主播}%>X个点亮星辰，点击前往TA的房间吧！","msg_self":"<%{用户}%>投喂:<%{主播}%>X个点亮星辰，快来围观吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32455","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":207,"name":"舰长跑马灯","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/9fe0397f142174516969a55bcb8705d658c658fb.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#FFB03CFF","color":"#FFFFFFFF","highlight":"#B25AC1FF","time":10},"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},"side":{"head_icon":"https://i0.hdslb.com/bfs/live/21b524fcc316e6d438415607d5531ecc2bf9f4ff.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"","msg_self":"<%{用户}%> 自动续费了主播的 <%舰长%>","link_url":"","msg_type":3,"shield_uid":-1,"business_id":"","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":424,"name":"许愿-星际漫步","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/33ad76e469a1db66734c3a5f0d54206c12b96878.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","msg_self":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31168","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":424,"name":"许愿-星际漫步","full":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/33ad76e469a1db66734c3a5f0d54206c12b96878.png","tail_icon_fa":"https://i0.hdslb.com/bfs/live/7d7af6107ef808438e6c3b4db0c7868bf78e5172.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/9043f0b254a3dc8a48166c5dc6fc2fab5edfe292.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","msg_self":"<%{用户}%>许愿成功，投喂<%{主播}%>X个星际漫步，快来一起太空冒险吧！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"31168","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":738,"name":"BLS任务1k秋","full":{"head_icon":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#b6272b","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/ab106f494f4cc0c94fb78ed46144c72f6db000f6.webp","tail_icon":"","background":"#b6272b","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"BLS限时任务：恭喜主播<%{主播}%>完成限时任务，直播间派发<%XX元%>红包，速抢手慢无！","msg_self":"BLS限时任务：恭喜主播<%{主播}%>完成限时任务，直播间派发<%XX元%>红包，速抢手慢无！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"-1","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":742,"name":"3D小电视飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=0&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32122","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
{"cmd":"NOTICE_MSG","id":742,"name":"3D小电视飞船专用","full":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"https://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon_fa":"https://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":1,"tail_icon_fan":4,"background":"#6097FFFF","color":"#FFFFFF","highlight":"#FFE600","time":15},"half":{"head_icon":"https://i0.hdslb.com/bfs/live/3ac21ee1dc5ea72e5b310c9cddcd6c9bc746d8c8.gif","tail_icon":"","background":"#6097FFFF","color":"#FFFFFFFF","highlight":"#FFE600","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":1234567890,"real_roomid":1234567890,"msg_common":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","msg_self":"<%{用户}%>投喂<%{主播}%>X个小电视飞船，向着浩瀚星辰出发！","link_url":"https://live.bilibili.com/xxxxxxxxxx?broadcast_type=1&is_room_feed=1&from=28003&extra_jump_from=28003&live_lottery_type=1","msg_type":2,"shield_uid":-1,"business_id":"32122","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
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
| key | type | value |
| - | - | - |
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 长_短直播间ID |
#### SUPER_CHAT_MESSAGE__data
| key 27					| type	| value |
| - | - | - |
| background_bottom_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_end		| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_start	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_icon			| str	| "" |
| background_image			| str	| "https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png" |
| background_price_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| color_point				| float	| 0.7 |
| dmscore					| num	| 8*N [16,48,56,64,72,80,120,128] |
| end_time					| num	| TimeStamp(秒) |
| gift						| obj	|  |
| id						| num	| SC id |
| is_ranked					| num	| 1 |
| is_send_audit				| num	| 0,1 |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info):medal_color为`#RRGGBB` |
| message					| str	| SC 内容 |
| message_font_color		| str	|  |
| message_trans				| str	| SC 日本語 翻译 |
| price						| num	| 价格 |
| rate						| num	| 1000 |
| start_time				| num	| TimeStamp(秒) |
| time						| num	| SC剩余时长(秒) |
| token						| str	| hex(64bit) |
| trans_mark				| num	| 是否翻译 |
| ts						| num	| TimeStamp(秒) |
| uid						| num	| uid |
| user_info					| obj	|  |
#### SUPER_CHAT_MESSAGE__data__gift
| key						| type	| value |
| - | - | - |
| gift_id					| num	| 12000 |
| gift_name					| str	| "醒目留言" |
| num						| num	| 1 |
#### SUPER_CHAT_MESSAGE__data__user_info
| key 12					| type	| value |
| - | - | - |
| face						| str	| 头像(URL) |
| face_frame				| str	| 头像框(URL) |
| guard_level				| num	| [guard_level](#others) |
| is_main_vip				| num	|  |
| is_svip					| num	| ?0 |
| is_vip					| num	| ?0 |
| level_color				| str	|  |
| manager					| num	| 管理员？ |
| name_color				| str	|  |
| title						| str	| [头衔](docs/头衔.md) |
| uname						| str	| 用户名 |
| user_level				| num	| 直播观众等级 |
#### SUPER_CHAT_MESSAGE__PriceTable
| 价格区间		| background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	| background_price_color	|
|-|-|-|-|-|-|-|-|
| 30-49.9		| #2A60B2					| #EDF5FF			| #405D85				| #3171D2					| #7497CD					| #A3F6FF				|
| 50-99.9		| #427D9E					| #DBFFFD			| #29718B				| #4EA4C5					| #7DA4BD					| #A3F6FF				|
| 100-499.9		| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 500-999.9		| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 1000-1999.9	| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 2000+			| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|

### SUPER_CHAT_MESSAGE_JPN
[TOP](#直播弹幕格式)  
SuperChat 日本語  
？某些主播的直播间会一直发送此包  
在`SUPER_CHAT_MESSAGE`后约`1100ms/1.1s`内发送  
由`百度翻译`提供翻译 Translated by `Baidu Translate`
| key | type | value |
| - | - | - |
| cmd		| str	| "SUPER_CHAT_MESSAGE_JPN" |
| data		| obj	| |
| roomid	| str	| str(长_短直播间ID) |
#### SUPER_CHAT_MESSAGE_JPN__data
| key 20					| type	| value |
| - | - | - |
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

### SUPER_CHAT_MESSAGE_DELETE
[TOP](#直播弹幕格式)  
SC 删除，约每110秒更新
| key | type | value |
| - | - | - |
| cmd	| str	| "SUPER_CHAT_MESSAGE_DELETE" |
| data	| obj	| |
#### SUPER_CHAT_MESSAGE_DELETE__data
| key		| type			| value |
| - | - | - |
| ids		| array(num)	| SC_id |
| roomid	| num			| 长_短直播间ID |

### DANMU_AGGREGATION
[TOP](#直播弹幕格式)  
抽奖通知，每秒最多更新一次，每个抽奖最多发送`max_time-1`个包
| key | type | value |
| - | - | - |
| cmd	| str	| "DANMU_AGGREGATION" |
| data	| obj	| |
#### DANMU_AGGREGATION__data
| key 11				| type	| value |
| :- | - | - |
| activity_identity		| str	| 抽奖id |
| activity_source		| num	| 1:天选时刻 2:礼物红包 |
| aggregation_cycle		| num	| 1 |
| aggregation_icon		| str	| 天选时刻："https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png" <br> 礼物红包："https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png"|
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| dmscore				| num	| 144 |
| msg					| str	| 天选时刻：弹幕口令 <br><br> 礼物红包:<br>"老板大气！点点红包抽礼物"<br>"点点红包，关注主播抽礼物～"<br>"喜欢主播加关注，点点红包抽礼物"<br>"红包抽礼物，开启今日好运！"<br>"中奖喷雾！中奖喷雾！" |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间TimeStamp(秒) |

### SPECIAL_GIFT
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "SPECIAL_GIFT" |
| data	| obj	| |
#### SEND_GIFT__data
| key | type | value |
| - | - | - |
| 39	| obj	| |
#### SEND_GIFT__data__39
| key 2,7	| type	| value |
| - | - | - |
| action	| str	| (start|end) |
| content	| str	|  |
| hadJoin	| num	| 0 |
| id		| str,num	| start:str end:num |
| num		| num	| 1 |
| storm_gif	| str	| GIF图像 |
| time		| num	| 持续时间 |
```json
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"可爱即正义~~","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"end","id":123412341234}}}
```

### GUARD_HONOR_THOUSAND
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "GUARD_HONOR_THOUSAND" |
| data	| obj	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type			| value |
| - | - | - |
| add	| array(num)	| 用户uid |
| del	| array(num)	| 用户uid |

### ANCHOR_LOT_CHECKSTATUS
[TOP](#直播弹幕格式)  
抽奖(天选时刻)检查？
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_CHECKSTATUS" |
| data	| obj	| |
#### ANCHOR_LOT_CHECKSTATUS__data
| key 3,5			| type	| value |
| - | - | - |
| id				| num	| 抽奖id |
| ？reject_danmu	| null	| ?null |
| ？reject_reason	| str	| ？拒绝理由 |
| status			| num	| ？4:通过 |
| uid				| num	| 主播uid |

### ANCHOR_LOT_START
[TOP](#直播弹幕格式)  
抽奖(天选时刻)开始
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_START" |
| data	| obj	| |
#### ANCHOR_LOT_START__data
| key 33			| type	| value |
| - | - | - |
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
| max_time			| num			| 开奖时间(300,600,900)秒 |
| require_text		| str			| "抽奖条件: 关注主播""至少成为主播的舰长/提督/总督" |
| require_type		| num			| 抽奖条件 1:礼物抽奖 2: 3:大航海 ~~4:UL?~~ |
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
| - | - | - |
| danmu_new[0].danmu		| str	| 弹幕口令[0,15] |
| danmu_new[0].danmu_view	| str	|  |
| danmu_new[0].reject		| bool	|  |

### ANCHOR_LOT_END
[TOP](#直播弹幕格式)  
抽奖(天选时刻)结束
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_END" |
| data	| obj	| |
#### ANCHOR_LOT_END__data
| key	| type	| value |
| - | - | - |
| id	| num	| 抽奖id |

### ANCHOR_LOT_AWARD
[TOP](#直播弹幕格式)  
抽奖(天选时刻) 中奖名单，在`ANCHOR_LOT_END`后约`1~180ms`
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_AWARD" |
| data	| obj	| |
#### ANCHOR_LOT_AWARD__data
| key 10			| type	| value |
| :- | - | - |
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
| :- | - | - |
| uid	| num	| uid |
| uname	| num	| 用户名 |
| face	| num	| 头像 |
| level	| num	| 直播观众等级 UL |
| color	| num	| 直播观众等级_颜色 num(RGB24) |
| num	| num	| 数量 |

### POPULAR_RANK_CHANGED
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "POPULAR_RANK_CHANGED" |
| data	| obj	| |
#### POPULAR_RANK_CHANGED__data
| key		| type	| value |
| - | - | - |
| uid		| num	| 主播uid |
| rank		| num	| [0-100] |
| countdown	| num	| [0,3600] |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| cache_key	| str	| `f"rank_change:{hex_256bit}"` |

### PREPARING
[TOP](#直播弹幕格式)  
结束直播
| key		| type	| value |
| - | - | - |
| cmd		| str	| "PREPARING" |
| round		| num	| 1 |
| roomid	| str	| 长_短直播间ID |

### DANMU_MSG
[TOP](#直播弹幕格式)  
弹幕！
| key | type | value |
| - | - | - |
| cmd	| str	| "DANMU_MSG" |
| info	| array	| |
| dm_v2	| str	| base64(proto) UTF-8 [define](#danmu_msg__dm_v2) |
#### DANMU_MSG__info
| array	| type	| value |  |
| - | - | - | - |
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
| - | - | - | - |
| 0[0]	| num		| ？0 |
| 0[1]	| num		| 弹幕位置 |
| 0[2]	| num		| 弹幕字体大小 |
| 0[3]	| num		| 弹幕颜色 |
| 0[4]	| num		| TimeStamp(毫秒) |
| 0[5]	| num		| `dmid` **RANDOM**/天选时刻 为 0 |浏览器网页端：进入直播间时间TimeStamp(秒) iOS/Android:随机
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
| - | - | - | - |
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
| - | - | - |
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
| - | - | - | - |
| 4[0]	| num		| `userLevel` 用户UL等级 |
| 4[1]	| num		| ？0 |
| 4[2]	| num		| UL等级 颜色 |
| 4[3]	| str/num	| `rank` 直播 用户排名|">50000"
| 4[4]	| num		| ? [0,1,2,3] |
#### DANMU_MSG__info__5
| array	| type	| value |
| - | - | - |
| 5[0]	| str	| identification |
| 5[1]	| str	| identification `title` |
#### DANMU_MSG__info__9
validation/checkInfo
| key	| type	| value |
| - | - | - |
| ts	| num	| TimeStamp(秒) |
| ct	| str	| 64bit |
#### DANMU_MSG__info__0__13
| key				| type	| value |
| - | - | - |
| bulge_display		| num	| 0,1 |
| emoticon_unique	| str	| 表情包id |
| height			| num	| 高 |
| in_player_area	| num	| 0,1 |
| is_dynamic		| num	| 0,1 |
| url				| str	| 表情包URL |
| width				| num	| 宽 |
#### DANMU_MSG__info__0__14
| key			| type	| value |
| - | - | - |
| file_duration	| num	|  |
| file_format	| str	|  |
| file_id		| str	|  |
| text			| str	|  |
| voice_url		| str	|  |
#### DANMU_MSG__info__0__15
| key				| type	| value |
| - | - | - |
| mode				| num	| 0 |
| show_player_type	| num	| 0 |
| extra				| str	| [json](#DANMU_MSG__info__0_15__extra) |
#### DANMU_MSG__info__0__15__extra
| key						| type		| value |  |
| - | - | - | - |
| send_from_me				| bool		| false |
| mode						| num		| 0 |
| color						| num		| 弹幕颜色 |
| dm_type					| num		| 0:文本 1:表情包 |
| font_size					| num		| `25` 弹幕字体大小 |
| player_mode				| num		| 弹幕位置 |
| show_player_type			| num		| 0 |
| content					| str		| 弹幕内容/表情包名称 |
| user_hash					| str		| `str(DEC:crc32(uid))`十六进制转十进制转字符串 |
| emoticon_unique			| str		| 表情ID |
| bulge_display				| num		| 0:官方表情包 1:房间表情包 |
| recommend_score			| num		| ？弹幕推荐等级/？智能屏蔽等级 |
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
#### DANMU_MSG__info__0__15__extra__emots
emoticonOptions
| key				| type		| value |
| - | - | - |
| emoticon_id		| str	|  |
| emoji 			| str	|  |
| descript 			| str	|  |
| url				| str	|  |
| width				| str	|  |
| height 			| str	|  |
| emoticon_unique	| str	|  |
| count 			| str	|  |
#### DANMU_MSG__info__0__16
| key				| type	| value |
| - | - | - |
| activity_identity	| str	| ？"" |
| activity_source	| num	| ？0 |
| not_show			| num	| ？0 |
```json
"emots":{"[dog]":{"emoticon_id":208,"emoji":"[dog]","descript":"[dog]","url":"http://i0.hdslb.com/bfs/live/4428c84e694fbf4e0ef6c06e958d9352c3582740.png","width":20,"height":20,"emoticon_unique":"emoji_208","count":1}}
```
#### DANMU_MSG__dm_v2
上线时间 2023-02-17 05:50:13~~05:50:24(UTC+8)
| id	| key			| type		| value |
| - | - | - | - |
| 01	| dmid			| int64		|  |
| 02	| dmid_unique	| string	|  |
| 03	| mode			| uint32	| 弹幕类型 |
| 04	| fontsize		| uint32	| 弹幕字号 |
| 05	| color			| uint32	| 弹幕颜色 |
| 06	| midHash		| string	| 发送着mid hash |
| 07	| content		| string	| 弹幕正文 |
| 08	| ctime			| int64		| 发送时间TimeStamp(毫秒) |
| 09	| ?				| ?			|  |
| 10	| dmid			| int64		|  |
| 11	| ?				| ?			|  |
| 12	| ?				| ?			|  |
| 13	| chat_bubble	| 			| 聊天气泡 |
| 14	| dm_type		| uint32	|  |
| 15	| emots			| repeat	| 表情 |
| 16	| ?				| ?			|  |
| 17	| ?				| ?			|  |
| 18	| lottery		| 			| 抽奖 |

```protobuf
syntax = "proto3";
message dm_V2 {}
```

### CUT_OFF
[TOP](#直播弹幕格式)  
切断直播！
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "CUT_OFF" |

### MESSAGEBOX_USER_GAIN_MEDAL
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "MESSAGEBOX_USER_GAIN_MEDAL" |
| data	| obj	| |
#### MESSAGEBOX_USER_GAIN_MEDAL__data
| key                   | type	| value |
| - | - | - |
| up_uid		|  | |
| toast			|  | |

### MESSAGEBOX_USER_MEDAL_CHANGE
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "MESSAGEBOX_USER_MEDAL_CHANGE" |
| data	| obj	| |
#### MESSAGEBOX_USER_MEDAL_CHANGE__data
| key                   | type	| value |
| - | - | - |
| up_uid				|  | |
| unlock				|  | |
| multi_unlock_level	|  | |
| upper_bound_content	|  | |

### MESSAGEBOX_USER_MEDAL_COMPENSATION
[TOP](#直播弹幕格式)  
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "MESSAGEBOX_USER_MEDAL_COMPENSATION" |
| data	| obj	| |
#### MESSAGEBOX_USER_MEDAL_COMPENSATION__data
[TOP](#直播弹幕格式)  
| key                   | type	| value |
| - | - | - |
| up_uid				|  | |
| add_score				|  | |

### SHOPPING_CART_SHOW
[TOP](#直播弹幕格式)  
？购物车  
开播后约30ms内发送`status=1`的包
| key | type | value |
| - | - | - |
| cmd	| str	| "SHOPPING_CART_SHOW" |
| data	| obj	| |
#### SHOPPING_CART_SHOW__data
| key		| type	| value |
| - | - | - |
| status	| num	| 开播:1 下播:2 |

### WIDGET_BANNER
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "WIDGET_BANNER" |
| data	| obj	| |
#### WIDGET_BANNER__data
| key			| type	| value |
| - | - | - |
| timestamp		| num	| 当前时间TimeStamp(秒) |
| widget_list	| obj	| "***ID***":{} |
#### WIDGET_BANNER__data__widget_list__ID
| key 15			| type	| value |
| - | - | - |
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
{"id":58,"status":1,"uid":XXXX,"rank":XXXX,"score":XXXX,"season_name":"PK大乱斗S30赛季","season_start":1675656000,"season_end":1677599999,"has_battled":1,"next_rank_need_score":XXX,"pk":{"level1_id":2,"level1_name":"钢之勇者","level1_img":"https://i0.hdslb.com/bfs/live/bf479718209c7ab0112f48099b47c9ffafb3da7f.png","level2_count":3,"level2_img":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png","is_top_level":false},"champion_info":null,"star_light_info":{"threshold_limit":0,"current_gold":0,"current_starLights":0,"max_starLights":0,"platformStrIn":[],"pk_status":0,"winner_status":0},"final_info":{"status":0,"result":0,"duration":XX,"score":XXX},"top100_rank_info":{"rank":0,"next100_need_score":0,"next10_need_score":0,"next1_need_score":0,"over2_need_score":0},"task_info":{"win_task":{"task_info":{"need_num":10,"current_num":X,"status":0},"reward_list":[{"name":"流量包*5个","pic":"http://i0.hdslb.com/bfs/live/495b158d45d8c3016e22552fc846dd4934f9efcb.png","num":5},{"name":"大乱斗之王*1天","pic":"http://i0.hdslb.com/bfs/live/9e841ccdd17e692ade28a8c9ba1cf439ddb21e64.png","num":0}]},"comp_task":{"task_info":{"need_num":15,"current_num":XX,"status":0},"reward_list":[{"name":"大乱斗高手*1天","pic":"http://i0.hdslb.com/bfs/live/9859865b15bb8c90d2e738ad2fe618d63c71b886.png","num":0}]},"time_stamp":TimeStamp_秒,"is_has_task":1,"task_status":0}}
{"id":58,"status":1,"uid":XXXX,"rank":XXXX,"score":XXXX,"season_name":"PK大乱斗S30赛季","season_start":1675656000,"season_end":1677599999,"has_battled":1,"next_rank_need_score":XXX,"pk":{"level1_id":2,"level1_name":"钢之勇者","level1_img":"https://i0.hdslb.com/bfs/live/bf479718209c7ab0112f48099b47c9ffafb3da7f.png","level2_count":3,"level2_img":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png","is_top_level":false},"champion_info":null,"star_light_info":{"threshold_limit":0,"current_gold":0,"current_starLights":0,"max_starLights":0,"platformStrIn":[],"pk_status":0,"winner_status":0},"final_info":{"status":1,"result":0,"duration":XX,"score":XXX},"top100_rank_info":{"rank":0,"next100_need_score":0,"next10_need_score":0,"next1_need_score":0,"over2_need_score":0},"task_info":{"win_task":{"task_info":{"need_num":10,"current_num":X,"status":0},"reward_list":[{"name":"流量包*5个","pic":"http://i0.hdslb.com/bfs/live/495b158d45d8c3016e22552fc846dd4934f9efcb.png","num":5},{"name":"大乱斗之王*1天","pic":"http://i0.hdslb.com/bfs/live/9e841ccdd17e692ade28a8c9ba1cf439ddb21e64.png","num":0}]},"comp_task":{"task_info":{"need_num":15,"current_num":XX,"status":0},"reward_list":[{"name":"大乱斗高手*1天","pic":"http://i0.hdslb.com/bfs/live/9859865b15bb8c90d2e738ad2fe618d63c71b886.png","num":0}]},"time_stamp":TimeStamp_秒,"is_has_task":1,"task_status":0}}
{"id":58,"status":1,"uid":XXXX,"rank":XXXX,"score":XXXX,"season_name":"PK大乱斗S30赛季","season_start":1675656000,"season_end":1677599999,"has_battled":1,"next_rank_need_score":XXX,"pk":{"level1_id":2,"level1_name":"钢之勇者","level1_img":"https://i0.hdslb.com/bfs/live/bf479718209c7ab0112f48099b47c9ffafb3da7f.png","level2_count":3,"level2_img":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png","is_top_level":false},"champion_info":null,"star_light_info":{"threshold_limit":0,"current_gold":0,"current_starLights":0,"max_starLights":0,"platformStrIn":[],"pk_status":0,"winner_status":0},"final_info":{"status":2,"result":0,"duration":XX,"score":XXX},"top100_rank_info":{"rank":0,"next100_need_score":0,"next10_need_score":0,"next1_need_score":0,"over2_need_score":0},"task_info":{"win_task":{"task_info":{"need_num":10,"current_num":X,"status":0},"reward_list":[{"name":"流量包*5个","pic":"http://i0.hdslb.com/bfs/live/495b158d45d8c3016e22552fc846dd4934f9efcb.png","num":5},{"name":"大乱斗之王*1天","pic":"http://i0.hdslb.com/bfs/live/9e841ccdd17e692ade28a8c9ba1cf439ddb21e64.png","num":0}]},"comp_task":{"task_info":{"need_num":15,"current_num":XX,"status":0},"reward_list":[{"name":"大乱斗高手*1天","pic":"http://i0.hdslb.com/bfs/live/9859865b15bb8c90d2e738ad2fe618d63c71b886.png","num":0}]},"time_stamp":TimeStamp_秒,"is_has_task":1,"task_status":0}}
{"id":58,"status":1,"uid":XXXX,"rank":XXXX,"score":XXXX,"season_name":"PK大乱斗S30赛季","season_start":1675656000,"season_end":1677599999,"has_battled":1,"next_rank_need_score":XXX,"pk":{"level1_id":2,"level1_name":"钢之勇者","level1_img":"https://i0.hdslb.com/bfs/live/bf479718209c7ab0112f48099b47c9ffafb3da7f.png","level2_count":3,"level2_img":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png","is_top_level":false},"champion_info":null,"star_light_info":{"threshold_limit":0,"current_gold":0,"current_starLights":0,"max_starLights":0,"platformStrIn":[],"pk_status":0,"winner_status":0},"final_info":{"status":2,"result":0,"duration":XX,"score":XXX},"top100_rank_info":{"rank":0,"next100_need_score":0,"next10_need_score":0,"next1_need_score":0,"over2_need_score":0},"task_info":{"win_task":{"task_info":{"need_num":10,"current_num":X,"status":0},"reward_list":[{"name":"流量包*5个","pic":"http://i0.hdslb.com/bfs/live/495b158d45d8c3016e22552fc846dd4934f9efcb.png","num":5},{"name":"大乱斗之王*1天","pic":"http://i0.hdslb.com/bfs/live/9e841ccdd17e692ade28a8c9ba1cf439ddb21e64.png","num":0}]},"comp_task":{"task_info":{"need_num":15,"current_num":XX,"status":1},"reward_list":[{"name":"大乱斗高手*1天","pic":"http://i0.hdslb.com/bfs/live/9859865b15bb8c90d2e738ad2fe618d63c71b886.png","num":0}]},"time_stamp":TimeStamp_秒,"is_has_task":1,"task_status":0}}
{"id":58,"status":1,"uid":XXXX,"rank":XXXX,"score":XXXX,"season_name":"PK大乱斗S30赛季","season_start":1675656000,"season_end":1677599999,"has_battled":1,"next_rank_need_score":XXX,"pk":{"level1_id":2,"level1_name":"钢之勇者","level1_img":"https://i0.hdslb.com/bfs/live/bf479718209c7ab0112f48099b47c9ffafb3da7f.png","level2_count":3,"level2_img":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png","is_top_level":false},"champion_info":null,"star_light_info":{"threshold_limit":0,"current_gold":0,"current_starLights":0,"max_starLights":0,"platformStrIn":[],"pk_status":0,"winner_status":0},"final_info":{"status":2,"result":1,"duration":XX,"score":XXX},"top100_rank_info":{"rank":0,"next100_need_score":0,"next10_need_score":0,"next1_need_score":0,"over2_need_score":0},"task_info":{"win_task":{"task_info":{"need_num":10,"current_num":X,"status":0},"reward_list":[{"name":"流量包*5个","pic":"http://i0.hdslb.com/bfs/live/495b158d45d8c3016e22552fc846dd4934f9efcb.png","num":5},{"name":"大乱斗之王*1天","pic":"http://i0.hdslb.com/bfs/live/9e841ccdd17e692ade28a8c9ba1cf439ddb21e64.png","num":0}]},"comp_task":{"task_info":{"need_num":15,"current_num":XX,"status":0},"reward_list":[{"name":"大乱斗高手*1天","pic":"http://i0.hdslb.com/bfs/live/9859865b15bb8c90d2e738ad2fe618d63c71b886.png","num":0}]},"time_stamp":TimeStamp_秒,"is_has_task":1,"task_status":0}}
```
#### WIDGET_BANNER__REF
|id		|title|tip_text|tip_text_color|tip_bottom_color|jump_url__app_name|type|band_id|sub_key|
|-|-|-|-|-|-|-|-|-|
|2		|大乱斗|PK大乱斗|A1F8FF|7349D5|chaos|3|0|pk_info|
|309	|争先拜大年|春节活动|FFFFFF|ffeaa0|spring_festival_2023|1|101566||
|307	|花灯闹元宵|花灯闹元宵|8F0606|cf442d|lantern_festival_2023|1|101598||

### GOTO_BUY_FLOW
[TOP](#直播弹幕格式)  
移动端 购买装扮
| key | type | value |
| - | - | - |
| cmd	| str	| "GOTO_BUY_FLOW" |
| data	| obj	| |
#### GOTO_BUY_FLOW__data
| key                   | type	| value |
| - | - | - |
| text | str | "X\*\*正在去买" / "X\*\*等2人正在去买" |

### RECOMMEND_CARD
[TOP](#直播弹幕格式)  
| key | type | value |
| :- | - | - |
| cmd	| str	| "RECOMMEND_CARD" |
| data	| obj	| |
#### RECOMMEND_CARD__data
| key				| type | value |
| - | - | - |
| title_icon | str | https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png |
| recommend_list	| array	| obj[] |
| timestamp			| num	| 当前时间TimeStamp(秒) |
#### RECOMMEND_CARD__data__recommend_list__0
```json
{"shopping_card_detail":{"goods_id":"{}","goods_name":"${商品名称}","goods_price":"${最低价格}","goods_max_price":"","sale_status":0,"coupon_name":"","goods_icon":"http://i0.hdslb.com/bfs/garb/item/7b805767338eb54bbfa324e925d08cbddc88f496.jpg","goods_status":1,"source":5,"h5_url":"https://www.bilibili.com/h5/mall/suit/detail?id=32833&navhide=1&from_id=480432362&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=${source}&goods_id=${goods_id}#/${virdress}","jump_link":"","schema_url":"","is_pre_sale":0,"activity_info":null,"pre_sale_info":null,"early_bird_info":null,"timestamp":${当前时间},"coupon_discount_price":"","selling_point":"","hot_buy_num":xxxx,"gift_buy_info":null,"is_exclusive":false,"coupon_id":"","reward_info":null,"goods_tag_list":null,"virtual_extra_info":{"goods_type":1,"web_container_type":1},"price_info":{"normal":{"prefix_price":"","sale_price":"{最低价格}","suffix_price":"起","strock_price":"","sale_start_time":xxxx,"sale_end_time":0},"activity":null},"btn_info":{"card_btn_status":1,"card_btn_title":"去抢购","card_btn_style":1},"goods_sort_id":0},"recommend_card_extra":null}
```

### COMMON_NOTICE_DANMAKU
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "COMMON_NOTICE_DANMAKU" |
| data	| obj	| |
#### COMMON_NOTICE_DANMAKU__data
| key				| type	| value |
| - | - | - |
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
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#F294AE","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"距离锦鲤小时榜结束还有5分钟，最高10倍的锦鲤红包就在前方！","type":1},{"background_color":["#FA729A"],"background_color_dark":null,"font_bold":false,"font_color":"#FFFFFF","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"【前往查看】","type":3,"uri":"https://live.bilibili.com/activity/live-activity-battle/index.html?app_name=spring_festival_2023&tab=rank&hour=1&with_menu=0&show_close=0&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,0,0,12,0;2,2,375,100p,0,0,0,0,12,0;3,3,100p,70p,0,0,0,0,12,0;4,2,375,100p,0,0,0,0,12,0;5,3,100p,70p,0,0,0,0,12,0;6,3,100p,70p,0,0,0,0,12,0;7,3,100p,70p,0,0,0,0,12,0;8,3,100p,70p,0,0,0,0,12,0&room_id=21013446&uid=387636363#/"}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#61666d","font_color_dark":"#a2a7ae","highlight_font_color":"#FFB027","highlight_font_color_dark":"#FFB027","text":"<%{YYYY}%> 被点亮啦！恭喜 <%{XXXX}%> 成为星球守护者！","type":1}],"dmscore":144,"terminals":[4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"{XXXX} 送出的红包为主播新增{YYYY}个粉丝！","type":1}],"dmscore":144,"terminals":[2,3,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"花灯闹元宵限时任务：任务即将结束，抓紧完成获取{x}红包奖励吧！未完成任务将无法获得奖励","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"{XXXX}在元气赏中五连抽！送出了好多礼物！","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"新春限时任务：恭喜主播完成限时任务，直播间派发{XXX}元红包，速抢手慢无！新任务将在30s后开启","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FB7299","text":"新春限时任务：任务即将结束，抓紧完成获取{XXX}元红包奖励吧！未完成任务将无法获得奖励","type":1}],"dmscore":144,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"font_color":"#FFFFFF","font_color_dark":"#FFFFFF","highlight_font_color":"#FFB027","highlight_font_color_dark":"#FFB027","text":"<%{YYYY}%> 被点亮啦！恭喜 <%{XXXX}%> 成为星球守护者！","type":1}],"dmscore":144,"terminals":[1,2,3]}}
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
| key | type | value |
| - | - | - |
| cmd	| str	| "POPULARITY_RED_POCKET_NEW" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_NEW__data
| key			| type	| value |
| :- | - | - |
| lot_id		| num	| 抽奖id |
| start_time	| num	| 开始时间TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| wait_num		| num	|  |
| uname			| str	| 用户名 |
| uid			| num	| uid |
| action		| str	| `"送出"` |
| num			| num	| 1 |
| gift_name		| str	| `"红包"` |
| gift_id		| num	| `13000` |
| price			| num	| 价格(RMB*10) |
| name_color	| str	| 舰长:"#00D1F1" |
| medal_info	| obj	| [medal_info](#粉丝牌信息medal_info) |

### POPULARITY_RED_POCKET_START
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "POPULARITY_RED_POCKET_START" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_START__data
| key				| type	| value |
| :- | - | - |
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
| [i].key				| type	| value |
| :- | - | - |
| [i].gift_id			| num | 礼物id |
| [i].gift_name			| num | 礼物名称 |
| [i].gift_pic			| num | 礼物图像URL(140*140) |
| [i].num				| num | 数量 |

### POPULARITY_RED_POCKET_WINNER_LIST
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "POPULARITY_RED_POCKET_WINNER_LIST" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_WINNER_LIST__data
| key			| type	| value |
| - | - | - |
| lot_id		| num	| 抽奖id |
| total_num		| num	| |
| winner_info	| array	| array[total_num] |
| awards		| obj	| ${gift_id}:{obj...} |
| version		| num	| 1 |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__winner_info
| array					| type	| value |
| - | - | - |
| winner_info\[i\]\[0\]	| num	| uid |
| winner_info\[i\]\[1\]	| str	| name |
| winner_info\[i\]\[2\]	| num	| `bag_id` |
| winner_info\[i\]\[3\]	| num	| gift_id |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__awards
| key			| type	| value |
| - | - | - |
| {gift_id}award_type		| num	|  |
| {gift_id}award_name		| str	| 礼物名称 |
| {gift_id}award_pic		| str	| URL(140*140) |
| {gift_id}award_big_pic	| str	| URL(360*360) |
| {gift_id}award_price		| num	| 礼物价格(RMB*1000) |

### ROOM_BLOCK_MSG
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "ROOM_BLOCK_MSG" |
| data	| obj	| |
| uid		| str |  |
| uname		| str |  |
### ROOM_BLOCK_MSG__data
| key		| type | value |
| - | - | - |
| dmscore	| num | 30 |
| operator	| num | 1 |
| uid		| num |  |
| uname		| str |  |

### AREA_RANK_CHANGED
[TOP](#直播弹幕格式)  
timestamp: N*5
| key | type | value |
| :- | - | - |
### AREA_RANK_CHANGED
| key | type | value |
| :- | - | - |
| conf_id		| num |  |
| rank_name		| str |  |
| uid			| num |  |
| rank			| num |  |
| icon_url_blue	| str | https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png |
| icon_url_pink	| str | https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png |
| icon_url_grey	| str | https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png |
| action_type	| num | 1 |
| timestamp		| num | TimeStamp(秒) |
| msg_id | str | UUID4 "xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx" |
| jump_url_link | str | https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=￥{uid}&conf_id=￥{conf_id}&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank |
| jump_url_pc | str | https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=￥{uid}&conf_id=￥{conf_id}&pc_ui=338,465,f4eefa,0#/area-rank |
| jump_url_pink | str | https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=￥{uid}&conf_id=￥{conf_id}&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank |
| jump_url_web | str | https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=￥{uid}&conf_id=￥{conf_id}#/area-rank |

### HOT_BUY_NUM
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_BUY_NUM" |
| data	| obj	| |
#### HOT_BUY_NUM__data
| key		| type	| value |
| - | - | - |
| goods_id	| str | id |
| num		| num |  |

### PK_BATTLE_END
[TOP](#直播弹幕格式)  
| key		| type	| value |
| - | - | - |
| cmd		| str	| "PK_BATTLE_END" |
| pk_id		| str	| |
| pk_status	| num	|  |
| timestamp	| obj	| TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_END__data
| key			| type	| value |
| - | - | - |
| battle_type	| num	| |
| timer			| num	| |
| init_info		| obj	| |
| match_info	| obj	| |
#### PK_BATTLE_END__&2_info
| key			| type	| value |
| - | - | - |
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

### WIDGET_GIFT_STAR_PROCESS
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "WIDGET_GIFT_STAR_PROCESS" |
| data	| obj	| |
#### WIDGET_GIFT_STAR_PROCESS__data
| key		| type | value |
| - | - | - |
| start_date		| num	| yyyyMMdd(星期一) |
| process_list		| array	| obj(3) |
| finished			| bool	| |
| ddl_timestamp		| num	| TimeStamp(秒) 下一个星期一00:00:00 UTC+8 |
| version			| num	| 当前时间TimeStamp(毫秒) |
| reward_gift		| num	| |
| reward_gift_img	| str	| |
| reward_gift_name	| str	| "礼物星球" |
#### WIDGET_GIFT_STAR_PROCESS__data__process_list
| key			| type | value |
| - | - | - |
| gift_id		| num	| |
| gift_img		| str	| |
| gift_name		| str	| |
| completed_num	| num	| |
| target_num	| num	| |

### XXXXXXXXXXX
[TOP](#直播弹幕格式)  
| key | type | value |
| - | - | - |
| cmd	| str	| "XXXXXXXXXXX" |
| data	| obj	| |
#### XXXXXXXXXXX__data
| key                   | type	| value |
| - | - | - |
| data	| xxx	| |

### others
[TOP](#直播弹幕格式)  
| key				| type	| value |
| - | - | - |
| guard_level		| num	| 舰长等级 <br> 0:无 <br> 1:总督GOVERNOR <br> 2:提督PREFECT <br> 3:舰长CAPTAIN |
| privilege_type	| num	| ！待确定 2:提督 3:舰长 |
| lot_status		| num	| 抽奖状态 0:开始 1:正在抽奖 2:开奖 |
| identities		| array	| 身份 1:"Normal" 2:"管理员" 3:"粉丝" 4:"Vip" 5:"SVip" 6:"舰长" 7:"提督" 8:"总督" |

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
(\d{16})?\{"cmd":"XXXXXXXXXX",.{1,}\n
```

### 粉丝牌信息medal_info
| key					| type		| value | 备注 |
| - | - | - | - |
| anchor_roomid			| num		| 主播 长_短直播间ID | 
| anchor_uname			| str		| 主播用户名 | 
| guard_level			| num		| [舰长等级](#others) |
| icon_id				| num		| 0 |
| is_lighted			| num		| 0: <br> 1: 七天内在直播间有互动 |
| medal_color			| num/str	| int(RGB24) / #RGB24 |
| medal_color_border	| num		| int(RGB24) |
| medal_color_end		| num		| int(RGB24) |
| medal_color_start		| num		| int(RGB24) |
| medal_level			| num		| 粉丝牌等级 |
| medal_name			| str		| 粉丝团称号 |
| special				| str		| "" |
| target_id				| !num		| 主播uid |

### medal_color
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
