# 
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
| live_stime			| num	| UnixTimeStamp | `reserve_type=2` |
| arc_stime				| num	| UnixTimeStamp | `reserve_type=2` |
| stime					| num	| UnixTimeStamp | `reserve_type=2` |
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
最低发包间隔1ms
```
＋――――――――――――――――――――――――――――――――――――――――――――――――＋＋――――――――――――＋
｜头像　状态　直播标题　分区　排行榜　　　👁👍⚠　分享｜｜高能用户　　 ｜
｜　⚡　ＵＬ　用户名　　　　　　　　粉丝团　　　　　　｜｜大航海　　　 ｜
＋――――――――――――――――――――――――――――――――――――――――――――――――＋|　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜＋――――――――――――＋
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　直播视频区　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　聊天区　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜　　　　　　　｜
｜　　　　　　　　　　　　　　　　　　　　　　　　　　｜｜通知栏（隐藏）｜
＋―――――――――――――――――――――――――――――――――――――――――――――――＋｜🎨　　　　ＳＣ｜
｜　购物　　　　　　　　　　　　　　　　　　　　　　　｜＋―――――――――――――＋
｜　抽奖　　　　　　　　　　　　　　　付费礼物　　　　｜｜　弹幕发送　　｜
｜　红包　　　　　　　　　　　　　　　　　　　　余额　｜｜　　　　　　　｜
＋―――――――――――――――――――――――――――――――――――――――――――――――＋＋―――――――――――――＋
```
| link | name | desc | area |
| - | - | - | - |
| [link](#ACTIVITY_MATCH_GIFT)	| ACTIVITY_MATCH_GIFT					| |
| [link](#ANCHOR_LOT_AWARD)	| ANCHOR_LOT_AWARD							| |直播视频区
| [link](#ANCHOR_LOT_CHECKSTATUS)	| ANCHOR_LOT_CHECKSTATUS			| |
| [link](#ANCHOR_LOT_END)	| ANCHOR_LOT_END							| |抽奖
| [link](#ANCHOR_LOT_START)	| ANCHOR_LOT_START							| 开始天选时刻抽奖 |抽奖
| [link](#AREA_RANK_CHANGED)	| AREA_RANK_CHANGED						| |
| [link](#BOX_ACTIVITY_START)	| BOX_ACTIVITY_START					| |
| [link](#CHANGE_ROOM_INFO)	| CHANGE_ROOM_INFO							| |
| [link](#CHASE_FRAME_SWITCH)	| CHASE_FRAME_SWITCH					| |
| [link](#COMBO_SEND)	| COMBO_SEND									| |
| [link](#COMMON_NOTICE_DANMAKU)	| COMMON_NOTICE_DANMAKU				| |
| [link](#CUT_OFF)	| CUT_OFF											| 系统通知 当前直播间被直播管理员切断直播。|
| [link](#DANMU_AGGREGATION)	| DANMU_AGGREGATION						| 抽奖通知 |通知栏
| [link](#DANMU_GIFT_LOTTERY_AWARD)	| DANMU_GIFT_LOTTERY_AWARD			| |
| [link](#DANMU_GIFT_LOTTERY_END)	| DANMU_GIFT_LOTTERY_END			| |
| [link](#DANMU_GIFT_LOTTERY_START)	| DANMU_GIFT_LOTTERY_START			| |
| [link](#DANMU_MSG)	| DANMU_MSG										| |
| [link](#DANMU_TAG_CHANGE)	| DANMU_TAG_CHANGE							| |
| [link](#ENTRY_EFFECT)	| ENTRY_EFFECT									| 进入直播间特效 |聊天区
| [link](#ENTRY_EFFECT_MUST_RECEIVE)	| ENTRY_EFFECT_MUST_RECEIVE		| |
| [link](#FULL_SCREEN_SPECIAL_EFFECT)	| FULL_SCREEN_SPECIAL_EFFECT	| |
| [link](#GIFT_PANEL_PLAN)	| GIFT_PANEL_PLAN							| |
| [link](#GIFT_STAR_PROCESS)	| GIFT_STAR_PROCESS						| |
| [link](#GUARD_ACHIEVEMENT_ROOM)	| GUARD_ACHIEVEMENT_ROOM			| |
| [link](#GUARD_BENEFIT_RECEIVE)	| GUARD_BENEFIT_RECEIVE				| |
| [link](#GUARD_BUY)	| GUARD_BUY										| 舰长购买 |高能用户
| [link](#GUARD_HONOR_THOUSAND)	| GUARD_HONOR_THOUSAND					| |
| [link](#GUARD_LOTTERY_START)	| GUARD_LOTTERY_START					| |
| [link](#GUARD_WINDOWS_OPEN)	| GUARD_WINDOWS_OPEN					| |
| [link](#HOT_RANK_CHANGED)	| HOT_RANK_CHANGED							| 人气榜排名更改 |已废弃
| [link](#HOT_RANK_CHANGED_V2)	| HOT_RANK_CHANGED_V2					| 人气榜排名更改 |
| [link](#HOT_RANK_SETTLEMENT)	| HOT_RANK_SETTLEMENT					| 分区榜(大) |已废弃
| [link](#HOT_RANK_SETTLEMENT_V2)	| HOT_RANK_SETTLEMENT_V2			| 分区榜(小) |
| [link](#HOT_ROOM_NOTIFY)	| HOT_ROOM_NOTIFY							| |
| [link](#HOUR_RANK_AWARDS)	| HOUR_RANK_AWARDS 							| |
| [link](#INTERACT_WORD)	| INTERACT_WORD								| 进入直播间|通知栏
| [link](#LIKE_INFO_V3_CLICK)	| LIKE_INFO_V3_CLICK					| 用户点赞（移动端）点击|通知栏
| [link](#LIKE_INFO_V3_UPDATE)	| LIKE_INFO_V3_UPDATE					| 用户点赞（移动端）更新|👍
| [link](#LIKE_SO_HOT)	| LIKE_SO_HOT 									| |
| [link](#LITTLE_MESSAGE_BOX)	| LITTLE_MESSAGE_BOX					| |
| [link](#LITTLE_TIPS)	| LITTLE_TIPS 									| |
| [link](#LIVE)	| LIVE													| |视频，状态，高能用户
| [link](#LIVE_INTERNAL_ROOM_LOGIN)	| LIVE_INTERNAL_ROOM_LOGIN			| |
| [link](#LIVE_OPEN_PLATFORM_CLOUD_GAME)	| LIVE_OPEN_PLATFORM_CLOUD_GAME		| |
| [link](#LIVE_OPEN_PLATFORM_GAME)	| LIVE_OPEN_PLATFORM_GAME			| |
| [link](#LIVE_PLAYER_LOG_RECYCLE)	| LIVE_PLAYER_LOG_RECYCLE			| |
| [link](#LOL_ACTIVITY)	| LOL_ACTIVITY									| |
| [link](#MATCH_TEAM_GIFT_RANK)	| MATCH_TEAM_GIFT_RANK					| |
| [link](#MESSAGEBOX_USER_GAIN_MEDAL)	| MESSAGEBOX_USER_GAIN_MEDAL	| |
| [link](#MESSAGEBOX_USER_MEDAL_CHANGE)	| MESSAGEBOX_USER_MEDAL_CHANGE	| |
| [link](#MESSAGEBOX_USER_MEDAL_COMPENSA)	| MESSAGEBOX_USER_MEDAL_COMPENSATION | |
| [link](#MILESTONE_UPDATE_EVENT)	| MILESTONE_UPDATE_EVENT | |
| [link](#MULTI_VOICE_STATUS_SYNC)	| MULTI_VOICE_STATUS_SYNC | |
| [link](#NOTICE_MSG)	| NOTICE_MSG						| |直播视频区
| [link](#ONLINE_RANK_COUNT)	| ONLINE_RANK_COUNT					| |
| [link](#ONLINE_RANK_TOP3)	| ONLINE_RANK_TOP3					| 高能用户前三恭喜 |高能用户，聊天区
| [link](#ONLINE_RANK_V2)	| ONLINE_RANK_V2					| 高能用户TOP7 |高能用户
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
| [link](#POPULAR_RANK_CHANGED)	| POPULAR_RANK_CHANGED | |
| [link](#POPULARITY_RED_POCKET_NEW)	| POPULARITY_RED_POCKET_NEW | |
| [link](#POPULARITY_RED_POCKET_START)	| POPULARITY_RED_POCKET_START | |
| [link](#POPULARITY_RED_POCKET_WINNER_L)	| POPULARITY_RED_POCKET_WINNER_LIST | |
| [link](#PREPARING)	| PREPARING | |
| [link](#PREPARING)	| PREPARING | |
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
| [link](#SEND_GIFT)	| SEND_GIFT							| 送礼物|高能用户，聊天区，通知栏
| [link](#SEND_GIFT_V2)	| SEND_GIFT_V2 | |
| [link](#SEND_TOP)	| SEND_TOP | |
| [link](#SHOPPING_CART_SHOW)	| SHOPPING_CART_SHOW | |
| [link](#SPECIAL_GIFT)	| SPECIAL_GIFT						| |
| [link](#SPECIAL_GIFT)	| SPECIAL_GIFT | |
| [link](#STARLIVE_PK_MSG)	| STARLIVE_PK_MSG | |
| [link](#STOP_LIVE_ROOM_LIST)	| STOP_LIVE_ROOM_LIST				| |
| [link](#SUPER_CHAT_AUDIT)	| SUPER_CHAT_AUDIT | |
| [link](#SUPER_CHAT_ENTRANCE)	| SUPER_CHAT_ENTRANCE | |
| [link](#SUPER_CHAT_MESSAGE)	| SUPER_CHAT_MESSAGE				| SuperChat |聊天区
| [link](#SUPER_CHAT_MESSAGE_DELETE)	| SUPER_CHAT_MESSAGE_DELETE			| SuperChat 删除 |聊天区
| [link](#SUPER_CHAT_MESSAGE_JPN)	| SUPER_CHAT_MESSAGE_JPN			| SuperChat 日本語 |聊天区
| [link](#THERMAL_STORM_DANMU_BEGIN)	| THERMAL_STORM_DANMU_BEGIN | |
| [link](#THERMAL_STORM_DANMU_CANCEL)	| THERMAL_STORM_DANMU_CANCEL | |
| [link](#THERMAL_STORM_DANMU_OVER)	| THERMAL_STORM_DANMU_OVER | |
| [link](#THERMAL_STORM_DANMU_UPDATE)	| THERMAL_STORM_DANMU_UPDATE | |
| [link](#TV_END)	| TV_END | |
| [link](#TV_START)	| TV_START | |
| [link](#USER_PANEL_RED_ALARM)	| USER_PANEL_RED_ALARM | |
| [link](#USER_TITLE_GET)	| USER_TITLE_GET | |
| [link](#USER_TOAST_MSG)	| USER_TOAST_MSG					| |通知栏
| [link](#VIDEO_CONNECTION_JOIN_END)	| VIDEO_CONNECTION_JOIN_END | |
| [link](#VIDEO_CONNECTION_JOIN_START)	| VIDEO_CONNECTION_JOIN_START | |
| [link](#VIDEO_CONNECTION_MSG)	| VIDEO_CONNECTION_MSG | |
| [link](#VOICE_JOIN_STATUS)	| VOICE_JOIN_STATUS | |
| [link](#VTR_GIFT_LOTTERY)	| VTR_GIFT_LOTTERY | |
| [link](#WARNING)	| WARNING | |
| [link](#WATCH_LPL_EXPIRED)	| WATCH_LPL_EXPIRED | |
| [link](#WATCHED_CHANGE)	| WATCHED_CHANGE					| xx人数|👁
| [link](#WEB_REPORT_CONTROL)	| WEB_REPORT_CONTROL | |
| [link](#WIDGET_BANNER)	| WIDGET_BANNER | |
| [link](#WIN_ACTIVITY)	| WIN_ACTIVITY | |
| [link](#WIN_ACTIVITY_USER)	| WIN_ACTIVITY_USER | |

### WARNING
`Anchor`
| key				| type	| value |
| - | - | - |
| cmd				| str	| "WARNING" |
| msg				| str	| ? |

### LIVE
| key				| type	| value |
| - | - | - |
| cmd				| str	| "LIVE" |
| live_key			| str	| ?*int64* |
| voice_background	| str	| ?"" |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| ?"live_mng" |
| live_model		| num	| ?0 |
| live_time	*		| num	| 开播时间UnixTimeStamp(秒) |
| roomid			| num	| 房间号 |
```json
{
	"cmd": "LIVE",
	"live_key": "123456789012345678",
	"voice_background": "",
	"sub_session_key": "123456789012345678sub_time:1234567890",
	"live_platform": "events_broadcast",
	"live_model": 0,
	"live_time": 1234567890, // ？仅在开播时存在
	"roomid": 12345
}
```

### SEND_GIFT
送礼物，实时
| key	| type | value |
| - | - | - |
| cmd	| str	| "SEND_GIFT" |
| data	| obj	| |
#### SEND_GIFT__data
| key 54				| type	| value | 备注 |
| - | - | - | - |
| action				| str	| "投喂" |
| **batch_combo_id**	| str	| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{时间UnixTimeStamp%.4f}"` |
| **batch_combo_id**	| str	| ？UUID | |
| **batch_combo_send**	| null	| ？第一次为 null |
| **batch_combo_send**	| obj	| ？其余为 上一个`batch_combo_id` |
| beatId				| str	| ？"0" |
| biz_source			| str	| "Live" |
| **blind_gift**		| null	| null |
| **blind_gift**		| ?		| ? |
| broadcast_id			| num	| 0 |
| coin_type				| str	| "gold" |
| combo_resources_id	| num	| 1 |
| combo_send			| null	| null |
| combo_stay_time		| num	| 3 |
| combo_total_coin		| num	| !!! |
| crit_prob				| num	| 0 |
| demarcation			| num	| 1 |
| discount_price		| num	| 100 |
| dmscore				| num	| 40 |
| draw					| num	| 0 |
| effect				| num	| 0 |
| effect_block			| num	| 0 |
| face					| str	| 发送者 头像URL |
| face_effect_id		| num	| 0 |
| face_effect_type		| num	| 0 |
| float_sc_resource_id	| num	| 0 |
| giftId				| num	| 礼物ID |
| giftName				| str	| 礼物名称 |
| giftType				| num	| 0 |
| gold					| num	| 0 |
| guard_level			| num	| 0 |
| is_first				| bool	| |
| is_naming				| bool	| |
| is_special_batch		| num	| 0 |
| magnification			| float	| 0 |
| medal_info			| obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| name_color			| str	| "" |
| num					| num	| 0 |
| original_gift_name	| str	| "" |
| price					| num	| 礼物价格,RMB*1000 |
| rcost					| num	| 0 |
| remain				| num	| 0 |
| rnd					| str	| "int64" |
| send_master			| null	| null |
| silver				| num	| 0 |
| super					| num	| 0 |
| super_batch_gift_num	| num	| 0 |
| super_gift_num		| num	| 0 |
| svga_block			| num	| 0 |
| switch				| bool	| true |
| tag_image				| str	| "" |
| tid					| str	| "int64" |
| timestamp				| int	| UnixTimeStamp(秒) |
| top_list				| null	| null |
| total_coin			| num	| 0 |
| uid					| num	| 发送者uid |
| uname					| str	| 发送者 用户名 |

### ONLINE_RANK_V2
排行榜前七(左)，实时
| key	| type	| value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_V2" |
| data	| obj	| |
#### ONLINE_RANK_V2__data
| key		| type	| value |
| - | - | - |
| list		| array	| obj[7] |
| rank_type	| str	| "gold-rank" |
#### ONLINE_RANK_V2__data__list
| key			| type	| value |
| - | - | - |
| uid			| num | uid |
| face			| str | 头像URL |
| score			| str | 贡献值 |
| uname			| str | 用户名 |
| rank			| num | 排名(1-7) |
| guard_level	| num | 舰长等级 |

### ONLINE_RANK_TOP3
排行榜前三(左)，实时
| key	| type	| value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_TOP3" |
| data	| obj	| |
#### ONLINE_RANK_TOP3__data
| key		| type	| value |
| - | - | - |
| dmscore	| num	| 112 |
| list		| array	| obj\[1\] |
#### ONLINE_RANK_TOP3__data__list
| key		| type	| value |
| - | - | - |
| msg		| str	| `f"恭喜 <%{用户名}%> 成为高能用户"` |
| rank		| num	| 排名(1-3) |

### ONLINE_RANK_COUNT
约每N*5秒发送一次  心跳包后1秒
| key | type | value |
| - | - | - |
| cmd	| str	| "ONLINE_RANK_COUNT" |
| data	| obj	| |
#### ONLINE_RANK_COUNT__data
| key	| type	| value |
| - | - | - |
| count | num	| 最大值约为10000[1-100xx] |

### INTERACT_WORD
进入直播间、关注主播通知，实时（高精度？）
| key | type	| value |
| - | - | - |
| cmd	| str	| "INTERACT_WORD" |
| data	| obj	| |
#### INTERACT_WORD__data
| key				| type	| value |
| - | - | - |
| contribution		| obj	| |
| core_user_type	| num	| 大部分为0?[0-5] |
| dmscore			| num	| [dmscore](#others) |
| fans_medal		| obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| identities		| array	| |
| is_spread			| num	| 0,1 |
| msg_type			| num	| |
| privilege_type	| num	| [privilege_type](#others) |
| roomid			| num	| |
| score				| num	| UnixTimeStamp(毫秒)??? |
| spread_desc		| str	| is_spread==1:"流量包推广" |
| spread_info		| str	| is_spread==1:"#FF649E" |
| tail_icon			| num	| [0,101] |
| timestamp			| num	| UnixTimeStamp(秒) |
| trigger_time		| num	| UnixTimeStamp(皮秒?) |
| uid				| num	| 发送者uid |
| uname				| str	| 发送者 用户名 |
| uname_color		| str	| "" |
#### INTERACT_WORD__score
msg_type=1: UnixTimeStamp
msg_type=2: 关注时间UnixTimeStamp
#### INTERACT_WORD__core_user_type
|core_user_type|等级|VIP|粉丝牌&舰长|直播观众等级|直播UP|粉丝|关注|认证|
|-|-|-|-|-|-|-|-|-|
|1|LV6+|年度大会员|30总督|UL25+||55|1300||
|2|LV6|年度大会员|||UP40|257w||个人认证：百大|
|2|LV6|年度大会员|30总督，25个舰长||UP28+|3w|||
#### INTERACT_WORD__data__contribution
在21232条信息中，有6个不为0--------6/21232
| key | type	| value |
| - | - | - |
| grade | num	| 0,1,2,3 |

|contribution|等级|VIP|当前主播-打赏相关|粉丝牌&舰长|直播观众等级|直播UP|粉丝|关注|认证|
|-|-|-|-|-|-|-|-|-|-|
|3|Lv3|大会员|粉丝牌20|?|?|?|33|16|无|
|1>>3|Lv6|年度大会员|数万元SC|?|?|40|257w|~440|个人认证：`2021年度巅峰主播、bilibili 2020百大UP主、知名游戏UP主`|
|-|Lv6|年度大会员|?|?|?|40|155w|~90|个人认证：`2021年度巅峰主播、bilibili 知名游戏UP主、直播高能主播`|
|-|Lv6|年度大会员|粉丝牌28|4舰长|?|15|1.6w|~80|无|
#### INTERACT_WORD__data__identities
```
[1]
[3,1]
"privilege_type": 3, "identities": [6, 1]
```

### HOT_RANK_CHANGED_V2
计时器每半小时(1800秒)重置一次，计时重置后，约每15秒或(N*15)秒发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_RANK_CHANGED_V2" |
| data	| obj	| |
#### HOT_RANK_CHANGED_V2__data
| key			| type	| value |
| - | - | - |
| rank			| num	| 排名[1-50] |
| trend			| num	| 0 |
| countdown		| num	| 倒计时[1-1786] |
| timestamp		| num	| UnixTimeStamp(秒) |
| web_url		| str	| 排行榜URL |
| live_url		| str	| 排行榜URL |
| blink_url		| str	| 排行榜URL |
| live_link_url	| str	| 排行榜URL |
| pc_link_url	| str	| 排行榜URL |
| icon			| str	| [图像][url_15] |
| area_name		| str	| 分区名称(小分区) |
| rank_desc		| str	| `f"{分区名称}top50"` |

### HOT_RANK_CHANGED
计时器每半小时(1800秒)重置一次，计时重置后，约每5秒或(N*5)秒发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_RANK_CHANGED" |
| data	| obj	| |
#### HOT_RANK_CHANGED__data
| key			| type	| value |
| - | - | - |
| rank			| num	| 排名[1-50] |
| trend			| num	| ? |
| countdown		| num	| 倒计时[1-1795]|
| timestamp		| num	| UnixTimeStamp(秒) |
| web_url		| str	| 排行榜URL |
| live_url		| str	| 排行榜URL |
| blink_url		| str	| 排行榜URL |
| live_link_url	| str	| 排行榜URL |
| pc_link_url	| str	| 排行榜URL |
| icon			| str	| 热门:[图像][url_15] <br> 手游:[图像][url_17] |
| area_name		| str	| 分区名称(大分区) |
| rank_desc		| str	| "" |

### WATCHED_CHANGE
约每5秒发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "WATCHED_CHANGE" |
| data	| obj	| |
#### WATCHED_CHANGE__data
| key			| type	| value |
| - | - | - |
| num			| num	| 人数 |
| text_small	| str	| str(num) <br> "x.y万" |
| text_large	| str	| f"num人看过" <br> "x.y万人看过" |

### ROOM_REAL_TIME_MESSAGE_UPDATE
每60秒发送一次，更新关注数、粉丝团人数
| key | type | value |
| - | - | - |
| cmd	| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data	| obj	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE__data
| key			| type	| value |
| - | - | - |
| roomid		| num	| 直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1? |
| fans_club		| num	|  |

### LIKE_INFO_V3_CLICK
点赞(移动端 双击屏幕)，实时，和`LIKE_INFO_V3_UPDATE`同时发送，实时&每5秒最多发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "LIKE_INFO_V3_CLICK" |
| data	| obj	| |
#### LIKE_INFO_V3_CLICK__data
| key				| type	| value |
| - | - | - |
| show_area			| num	| 0 <br> 1(30s) |
| msg_type			| num	| 6 |
| like_icon			| str	| [图标][img_16] |
| uid				| num	|  |
| like_text			| str	| "为主播点赞了" |
| uname				| str	| |
| uname_color		| str	| "" |
| identities		| array	| ? |
| fans_medal		| obj	| [fans_medal](#粉丝牌信息medal_info) |
| contribution_info	| obj	| |
| dmscore			| num	| 20 |
#### LIKE_INFO_V3_CLICK__data__contribution_info
| key | type | value |
| - | - | - |
| grade | num | 0 |

### LIKE_INFO_V3_UPDATE
点赞(移动端 双击屏幕)，实时，和`LIKE_INFO_V3_CLICK`同时发送，实时&每5秒最多发送一次
| key | type | value |
| - | - | - |
| cmd	| str	| "LIKE_INFO_V3_UPDATE" |
| data	| obj	| |
#### LIKE_INFO_V3_UPDATE__data
| key | type	| value |
| - | - | - |
| click_count	| num | |

### HOT_ROOM_NOTIFY
***description***
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_ROOM_NOTIFY" |
| data	| obj	| |
#### HOT_ROOM_NOTIFY__data
| key					| type | value |
| - | - | - |
| threshold				| num | 10000 |
| ttl					| num | 300 |
| exit_no_refresh		| num | 1 |
| random_delay_req_v2	| obj | **固定值** |
#### HOT_ROOM_NOTIFY__data__random_delay_req_v2
| key	| type | value |
| - | - | - |
| path	| str | |
| delay	| num | |
```json
{"cmd":"HOT_ROOM_NOTIFY","data":{"threshold":10000,"ttl":300,"exit_no_refresh":1,"random_delay_req_v2":[{"path":"/live/getRoundPlayVideo","delay":10},{"path":"/xlive/web-room/v1/index/getOffLiveList","delay":120000}]}}
```

### ENTRY_EFFECT
欢迎舰长、提督、(?)进入直播间，实时(高精度?)
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
| copy_color				| str	| **Tag_2** |
| highlight_color			| str	| **Tag_2** |
| priority					| num	| 1? |
| basemap_url				| str	| basemap_url=web_basemap_url |
| show_avatar				| num	| 1 |
| effective_time			| num	| effective_time=web_effective_time |
| web_basemap_url			| str	| basemap_url=web_basemap_url |
| web_effective_time		| num	| effective_time=web_effective_time |
| web_effect_close			| num	| 2,4,135,136,137:0 253,254,291,314,315,316,325,328:1 |
| web_close_time			| num	| 136,137,253,254,291,314,315,316,325,328:900 4:0 |
| business					| num	| ~~3:`<^icon^>` 1:提督、舰长、`<^icon^> 舰长` 4:用户，无空格~~ |
| copy_writing_v2			| str	| `f"欢迎 <^icon^> <%{用户名}%> 进入直播间"`<br>`f"欢迎(提督\|舰长) <%{用户名}%> 进入直播间"`<br>`f"欢迎<%{用户名}%>进入直播间"`**无空格**<br>`f"欢迎 <^icon^> 舰长 <%{用户名}%> 进入直播间"`<br> |限长6字符，省略号为`…`
| icon_list					| array	| ~~`copy_writing_v2`内有`"<^icon^>"`时，数组有值 id=136:1,2 id=137:3 identities=22,33:1~~ |
| max_delay_time			| num	| 7 |
| trigger_time				| num	| UnixTimeStamp(皮秒?) |
| identities				| num	| `copy_writing_v2`内有`"<^icon^>,舰长"`时为`33`<br>有`"<^icon^>"`时为`22`<br>`提督`为`7`<br>`舰长`为`6` |
| effect_silent_time		| float	| 0 |
| effective_time_new		| num	| Tag_1 |
| web_dynamic_url_webp		| str	| Tag_1 |
| web_dynamic_url_apng		| str	| Tag_1 |
| mobile_dynamic_url_webp	| str	| Tag_1 |
#### ENTRY_EFFECT__data__id
前缀:`https://i0.hdslb.com/bfs/live/mlive/` 后缀:`.png`
| id	| desc | copy_color | highlight_color | effective_time | basemap_url | privilege_type
| -: | - |-: | -: | -: | - | - |
| 2		| 提督 | "#ffffff" | "#FFF100" | 3 | 74a41c65e422116d230d433042881fa5556f7870 | 2
| 4		| 舰长 | "#ffffff" | "#E6FF00" | 2 | 11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e | 3
| 135	| 　　 | "#000000" | "#FFF100" | 1 | da6933ea70f31c4df63f4b68b735891284888357 | 0
| 136	| 　　 | "#000000" | "#FFF100" | 2 | d4708dee21646e6ebcc58e7f6fa2a972c1d25b36 | 0
| 137	| 　　 | "#000000" | "#FFF100" | 2 | f7017a13c62c13369b85cb7a9f89981e79a3d2f9 | 0,2
| 253	| 　　 | "#ffffff" | "#ffea18" | 3 | 6d38ab463be28a130870c8c43d109473f215963e | 0
| 254	| 　　 | "#ffffff" | "#ffea18" | 3 | 4a0990210623ac86c16c87532c6b2352503bbcc7 | 0
| 254	| 　　 | "#ffffff" | "#ffea18" | 3 | adffca37e8afc1b8f745342038d4187131794968 | 3
| 291	| 　　 | "#ffffff" | "#ffffff" | 3 | 510a123a3f247d86ad1b1f15aff506c12af73934 | 0
| 314	| 　　 | "#ffffff" | "#92ffff" | 3 | e5f32dbdacd2d019c50ab5621f627786bd97cfe8 | 0
| 315	| 　　 | "#ffffff" | "#98ffff" | 5 | c2feddf0fb3a5bbf6b94da7970f7766455133c55 | 0
| 316	| 　　 | "#ffffff" | "#ffff6D" | 5 | 285faee9bbd04e2847b443df1b7f719e0768e79d | 0
| 325	| 　　 | "#ffffff" | "#fff596" | 3 | 6d077afa6cc49daed46e8b3f1b07376424fbcf94 | 0
| 328	| 　　 | "#ffffff" | "#92ffff" | 4 | c808776866b38239d638cf9106ff27f594249ed8 | 0
| x		| 　　 |  |
| 253	| 　　 | "#ffffff" | "#FFF14B" | 3 | e6b09100caef61b8518f3c0a23f04636e2a8abaa | 0 **Tag_2**
#### ENTRY_EFFECT__data__web_dynamic_url_XXX
前缀:`https://i0.hdslb.com/bfs/live/mlive/`
| XXX	|web_dynamic_url_webp|web_dynamic_url_apng|mobile_dynamic_url_webp| effective_time_new |
|-|-|-|-| -: |
| 1	|`eac404ec584e3b672cc087d86b32700105171c4f.webp`|`0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng`|`eac404ec584e3b672cc087d86b32700105171c4f.webp`|3
| 2	|`5007b1f4546c137dfbb72316b9744c808902aeb3.webp`|`ed4b66c18a31663b8ebadce6a968fbb4f86f6bd8.apng`|`5007b1f4546c137dfbb72316b9744c808902aeb3.webp`|3.1
| 3	|`15bfdcf4a72f8ba1c8b45a99b6c9e9f53a25e8e1.webp`|`db7f605bc2bf8f6f98d30be134bc653e0a3f4296.vnd.mozilla.apng`|`2c952f4aeb7fef8bd753a468da9c357745fc1402.webp`|4.4
| 4	|`9f1ae49431c526a24f9e87b1b6a898b1028ec645.webp`|`f068957a37d9bd6ec0f3e7907be6db63ae2cfe89.vnd.mozilla.apng`|`9f1ae49431c526a24f9e87b1b6a898b1028ec645.webp`|4.4
| 5	||||
| 6	||||
| 7	||||
| 8	||||
| 9	||||
| 10	||||

### STOP_LIVE_ROOM_LIST
每30秒发送一次(`HH:mm:29`,`HH:mm:59`)，推送很多直播间ID?
| key | type | value |
| - | - | - |
| cmd	| str	| "STOP_LIVE_ROOM_LIST" |
| data	| obj	| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type	| value |
| - | - | - |
| room_id_list	| array	|  |

### GUARD_BUY
舰长购买，实时
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
| num			| num	| 1 |
| price			| num	| 价格*1000 |
| gift_id		| num	| 10003:"舰长" 10002:"提督" 10001:"总督" |
| gift_name		| str	|  |
| start_time	| num	| start_time=end_time 购买时间 UnixTimeStamp(秒) |
| end_time		| num	| start_time=end_time 购买时间 UnixTimeStamp(秒) |

### USER_TOAST_MSG
舰长购买通知，实时，显示在聊天区
| key | type | value |
| - | - | - |
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG__data
| key 23				| type	| value |
| - | - | - |
| anchor_show			| bool	| true |
| color					| str	| "舰长":"#00D1F1" <br> "提督":"#E17AFF" <br> "总督": |
| dmscore				| num	| 90 |
| effect_id				| num	| 397 |
| end_time				| num	| start_time=end_time UnixTimeStamp(秒) |
| face_effect_id		| num	| "舰长":44 <br> "提督":43 <br> "总督": |
| gift_id				| num	| 10003:"舰长" <br> 10002:"提督" <br> 10001:"总督" |
| guard_level			| num	| [guard_level](#others) |
| is_show				| num	| 0 |
| num					| num	| 1? |
| op_type				| num	| 3:PC? 2:iOS 1:Android? |
| payflow_id			| str	| 订单号(25) |
| price					| num	| 价格*1000 连续订阅舰长138，iOS连续订阅舰长158，舰长198，提督1998，19998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| "舰长":590 <br> "提督":591 <br> "总督": |
| start_time			| num	| start_time=end_time 购买时间 UnixTimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播总舰长数 |
| toast_msg				| str	| `f"<%{用户名}%> 自动续费了舰长"` <br> `f"<%{用户名}%> 开通了(舰长\|提督\|总督)，今天是TA陪伴主播的第{}天"` |
| uid					| num	| uid |
| unit					| str	| "月"? |
| user_show				| bool	| true |
| username				| str	| 用户名 |

### NOTICE_MSG
滚动横幅，实时
| key			| type	| value |
| - | - | - |
| cmd			| str	| "NOTICE_MSG" |
| id			| num	|  |
| name			| num	|  |
| full			| obj	|  |
| half			| obj	|  |
| side			| obj	|  |
| roomid		| num	|  |
| real_roomid	| num	|  |
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

### HOT_RANK_SETTLEMENT_V2
每30分(1800秒 `HH:25:05, HH:55:05`)广播一次，小分区排行榜topxx
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_RANK_SETTLEMENT_V2" |
| data	| obj	| |
#### HOT_RANK_SETTLEMENT_V2__data
| key		| type	| value |
| - | - | - |
| rank		| num	| 排名 |
| uname		| str	| 主播用户名 |
| face		| str	| 主播头像URL |
| timestamp	| num	| UnixTimeStamp(秒) `HH:25:05 HH:55:05` |
| icon		| str	| url_15 |
| area_name	| str	| 分区名称(小) |
| url		| str	|  |
| cache_key	| str	| 随机值(128bit) |
| dm_msg	| str	| `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜top{rank}! 即将获得热门流量推荐哦！"` `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜榜首!"` `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜top{rank}!"` |
```python
f"https://live.bilibili.com/p/html/live-app-hotrank/result.html?is_live_half_webview=1&hybrid_half_ui=1,5,250,200,f4eefa,0,30,0,0,0;2,5,250,200,f4eefa,0,30,0,0,0;3,5,250,200,f4eefa,0,30,0,0,0;4,5,250,200,f4eefa,0,30,0,0,0;5,5,250,200,f4eefa,0,30,0,0,0;6,5,250,200,f4eefa,0,30,0,0,0;7,5,250,200,f4eefa,0,30,0,0,0;8,5,250,200,f4eefa,0,30,0,0,0&areaId={xxxx}&cache_key={cache_key}"
```

### HOT_RANK_SETTLEMENT
每30分(1800秒 `HH:25:05, HH:55:05`)广播一次，大分区排行榜topxx
| key | type | value |
| - | - | - |
| cmd	| str	| "HOT_RANK_SETTLEMENT" |
| data	| obj	| |
#### HOT_RANK_SETTLEMENT__data
| key		| type	| value |
| - | - | - |
| area_name	| str	| 分区名称(大) |
| cache_key	| str	| 随机值(128bit) |
| dm_msg	| str	| `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜{排行}!"` "榜首,top2-10" |
| dmscore	| str	| 144 |
| face		| str	| 主播头像URL |
| icon		| str	| url_15 |
| rank		| str	| 排名 |
| timestamp	| str	| UnixTimeStamp(秒) `HH:25:05 HH:55:05` |
| uname		| str	| 主播用户名 |
| url		| str	| [HOT_RANK_SETTLEMENT_V2:data:url](#HOT_RANK_SETTLEMENT_V2__data) |

### SUPER_CHAT_MESSAGE
SuperChat
| key | type | value |
| - | - | - |
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 直播间ID |
#### SUPER_CHAT_MESSAGE__data
| key(27)					| type	| value |
| - | - | - |
| background_bottom_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_end		| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_start	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_icon			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_image			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_price_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| color_point				| float	| 0.7 |
| dmscore					| num	|  |
| end_time					| num	| UnixTimeStamp(秒) |
| gift						| obj	|  |
| id						| num	| SC id |
| is_ranked					| num	| ? |
| is_send_audit				| num	| 0 |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info):medal_color为`#RRGGBB` |
| message					| str	| SC 内容 |
| message_font_color		| str	|  |
| message_trans				| str	| SC 日本語 翻译 |
| price						| num	| 价格 |
| rate						| num	| 1000 |
| start_time				| num	| UnixTimeStamp(秒) |
| time						| num	| SC 持续时长(秒) |
| token						| str	| hex(64bit) |
| trans_mark				| num	| 翻译 |
| ts						| num	| UnixTimeStamp(秒) |
| uid						| num	| uid |
| user_info					| obj	|  |
#### SUPER_CHAT_MESSAGE__data__gift
| key						| type	| value |
| - | - | - |
| gift_id					| num	| 12000 |
| gift_name					| str	| "醒目留言" |
| gift_id					| num	| 1 |
#### SUPER_CHAT_MESSAGE__data__user_info
| key						| type	| value |
| - | - | - |
| face						| str	| 头像 |
| face_frame				| str	| 头像框 |
| guard_level				| num	| [guard_level](#others) |
| is_main_vip				| num	|  |
| is_svip					| num	|  |
| is_vip					| num	|  |
| level_color				| str	|  |
| manager					| num	| 管理员？ |
| name_color				| str	|  |
| title						| str	| ？ |
| uname						| str	| 用户名 |
| user_level				| num	| 直播观众等级 |
#### SUPER_CHAT_MESSAGE__PriceTable
| 价格区间		| background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	|
|-|-|-|-|-|-|-|
| 30-49.9		| #2A60B2					| #EDF5FF			| #405D85				| #3171D2					| #7497CD					| #A3F6FF				|
| 50-99.9		| #427D9E					| #DBFFFD			| #29718B				| #4EA4C5					| #7DA4BD					| #A3F6FF				|
| 100-499.9		| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 500-999.9		| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 1000-1999.9	| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|
| 2000+			| #000000					| #000000			| #000000				| #000000					| #000000					| #000000				|

### SUPER_CHAT_MESSAGE_JPN
SuperChat 日本語  某些主播的直播间会一直发送此包
由`百度翻译`提供翻译 Translated by `Baidu Translate`
| key | type | value |
| - | - | - |
| cmd		| str	| "SUPER_CHAT_MESSAGE_JPN" |
| data		| obj	| |
| roomid	| str	| str(直播间ID) |
#### SUPER_CHAT_MESSAGE_JPN__data
| key(20)					| type	| value |
| - | - | - |
| id						| str	| str(SUPER_CHAT_MESSAGE__data__id) |
| uid						| str	| str(SUPER_CHAT_MESSAGE__data__uid) |
| price						| num	|  |
| rate						| num	| 1000 |
| message					| str	| 原始SC内容 |
| message_jpn				| str	| 翻译后SC内容 |
| is_ranked					| num	| 0,1 |
| background_image			| str	|  |
| background_color			| str	|  |
| background_icon			| str	|  |
| background_price_color	| str	|  |
| background_bottom_color	| str	|  |
| ts						| num	| UnixTimeStamp(秒) |
| token						| str	|  |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info) 没有(guard_level,is_lighted,medal_color_border,medal_color_end,medal_color_start) |
| user_info					| obj	|  |
| time						| num	|  |
| start_time				| num	| UnixTimeStamp(秒) |
| end_time					| num	| UnixTimeStamp(秒) |
| gift						| obj	|  |

### SUPER_CHAT_MESSAGE_DELETE
SC 删除，约每110秒更新
| key | type | value |
| - | - | - |
| cmd	| str	| "SUPER_CHAT_MESSAGE_DELETE" |
| data	| obj	| |
#### SUPER_CHAT_MESSAGE_DELETE__data
| key		| type	| value |
| - | - | - |
| ids		| array	| SC id(num) |
| roomid	| num	| 直播间id |

### ANCHOR_LOT_START
抽奖(天选时刻)
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_START" |
| data	| obj	| |
#### ANCHOR_LOT_START__data
| key 33			| type	| value |
| - | - | - |
| asset_icon		| str	| https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png |
| asset_icon_webp	| str	| https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp |
| award_image		| str	|  |
| award_name		| str	| 礼物名称 |
| award_num			| num	| 礼物数量 |
| award_type		| num	| 0 |
| cur_gift_num		| num	| 0 |
| current_time		| num	| 当前时间UnixTimeStamp(秒) |
| danmu				| str	| 弹幕口令 |
| danmu_new			| array	|  |
| danmu_type		| num	| 0 |
| gift_id			| num	| 0 |
| gift_name			| str	|  |
| gift_num			| num	| 1 |
| gift_price		| num	| 0 |
| goaway_time		| num	|  |
| goods_id			| num	|  |
| id				| num	| 抽奖id |
| is_broadcast		| num	| 1 |
| join_type			| num	| 0 |
| lot_status		| num	| 0 |
| max_time			| num	| 开奖时间 |
| require_text		| str	| "抽奖条件：关注主播" |
| require_type		| num	| 抽奖条件 |
| require_value		| num	| 0 |
| room_id			| num	| 直播间id |
| send_gift_ensure	| num	|  |
| show_panel		| num	|  |
| start_dont_popup	| num	|  |
| status			| num	|  |
| time				| num	| 剩余时间(秒) |
| url				| str	| https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1 |
| web_url			| str	| https://live.bilibili.com/p/html/live-lottery/anchor-join.html |

### DANMU_AGGREGATION
抽奖通知，每1秒更新一次，每个抽奖最多发送`max_time-1`个包
| key | type | value |
| - | - | - |
| cmd	| str	| "DANMU_AGGREGATION" |
| data	| obj	| |
#### DANMU_AGGREGATION__data
| key					| type	| value |
| :- | - | - |
| activity_identity		| str	| 抽奖id |
| activity_source		| num	| 1 |
| aggregation_cycle		| num	| 1 |
| aggregation_icon		| str	| "https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png" |
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| dmscore				| num	| 144 |
| msg					| str	| 弹幕口令 |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间UnixTimeStamp(秒) |

### SPECIAL_GIFT
开始：实时  
结束：20秒后？ ，一次发送2个相同的包（2样本）
| key | type | value |
| - | - | - |
| cmd	| str	| "SPECIAL_GIFT" |
| data	| obj	| |
#### SEND_GIFT__39
| key | type | value |
| - | - | - |
| 39	| obj	| |
#### SEND_GIFT__data__39
| key		| type	| value |
| - | - | - |
| action	| str	| (start|end) |
| content	| str	|  |
| hadJoin	| num	| 0 |
| id		| str,num	| start:str end:num |
| num		| num	| 1 |
| storm_gif	| str	| GIF图像 |
| time		| num	| 持续时间 |
```json
{"cmd":"SPECIAL_GIFT", "data": {"39": {"action":"start", "content":"可爱即正义~~", "hadJoin": 0, "id":"123412341234", "num": 1, "storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901", "time": 90}}}
{"cmd":"SPECIAL_GIFT", "data": {"39": {"action":"end", "id": 123412341234}}}
```

### GUARD_HONOR_THOUSAND
| key | type | value |
| - | - | - |
| cmd	| str	| "GUARD_HONOR_THOUSAND" |
| data	| obj	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type	| value |
| - | - | - |
| add	| array	| 用户uid |
| del	| array	| 用户uid |

### ANCHOR_LOT_END
抽奖(天选时刻) 结束
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_END" |
| data	| obj	| |
#### ANCHOR_LOT_END__data
| key	| type	| value |
| - | - | - |
| id	| num	| 抽奖id |

### ANCHOR_LOT_AWARD
抽奖(天选时刻) 中奖名单
| key | type | value |
| - | - | - |
| cmd	| str	| "ANCHOR_LOT_AWARD" |
| data	| obj	| |
#### ANCHOR_LOT_AWARD__data
| key				| type	| value |
| :- | - | - |
| award_dont_popup	| num	| 1 |
| award_image		| str	| 奖品图像？ |
| award_name		| str	| 奖品名称 |
| award_num			| num	| 1 |
| award_type		| num	| 0 |
| award_users		| array	| obj |
| id				| num	| 抽奖id |
| lot_status		| num	| 2 |
| url				| str	| https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1 |
| web_url			| str	| "https://live.bilibili.com/p/html/live-lottery/anchor-join.html" |
#### ANCHOR_LOT_AWARD__data__award_users
| key	| type	| value |
| :- | - | - |
| uid	| num	| uid |
| uname	| num	| 用户名 |
| face	| num	| 头像 |
| level	| num	| 直播观众等级 |
| color	| num	| 直播观众等级_颜色 int(RGB24) |
| num	| num	| 数量 |

### POPULAR_RANK_CHANGED
| key | type | value |
| - | - | - |
| cmd	| str	| "POPULAR_RANK_CHANGED" |
| data	| obj	| |
#### POPULAR_RANK_CHANGED__data
| key		| type	| value |
| - | - | - |
| uid		| num	| 主播uid |
| rank		| num	| [1-100] |
| countdown	| num	| [3600] |
| timestamp	| num	| 当前时间UnixTimeStamp(秒) |
| cache_key	| str	| `f"rank_change:{256bit}"` |

### PREPARING
结束直播
| key		| type	| value |
| - | - | - |
| cmd		| str	| "PREPARING" |
| roomid	| str	| 直播间id |

### DANMU_MSG
| key | type | value |
| - | - | - |
| cmd	| str	| "DANMU_MSG" |
| info	| array	| |
#### DANMU_MSG__info
| list	| type	| value |
| - | - | - |
| 0		| array	| 弹幕属性 |
| 1		| str	| 弹幕内容 |
| 2		| array	| 用户主站信息 |
| 3		| array	| 粉丝牌 |
| 4		| array	| 用户直播区信息 |
| 5		| array	| ？ |
| 6		| num	| ？0 |
| 7		| num	| ？[舰长等级](#others) |
| 8		| null	| ？ |
| 9		| obj	|  |
| 10	| num	| ？0 |
| 11	| num	| ？0 |
| 12	| null	| ？null |
| 13	| null	| ？null |
| 14	| num	| ？0 |
| 15	| num	| ？高能榜 |
#### DANMU_MSG__info__0
| array	| type		| value |
| - | - | - |
| 0:0	| num		| ？0？send_from_me |
| 0:1	| num		| 弹幕位置 |
| 0:2	| num		| 弹幕字体大小 |
| 0:3	| num		| 弹幕颜色 |
| 0:4	| num		| UnixTimeStamp(毫秒) |
| 0:5	| num		| ？用户发送时间UnixTimeStamp(秒) |
| 0:6	| num		| 0? |
| 0:7	| str		| HEX:crc32(uid) |
| 0:8	| num		| ? |
| 0:9	| num		| ? |
| 0:10	| num		| ? |
| 0:11	| str		| 0:10==5::`"#1453BAFF,#4C2263A2,#3353BAFF"` |
| 0:12	| num		| ? |
| 0:13	| obj/str	| 发送表情包时：{obj...} <br> 其他:`"{}"` |
| 0:14	| obj/str	| "{}" |
| 0:15	| obj 		|  |
| 0:16	| obj 		|  |20230119
#### DANMU_MSG__info__0__4
| array	| type	| value | 备注 |
| - | - | - | - |
| 4:0	| num	| 用户UL等级 |
| 4:1	| num	| ？0 |
| 4:2	| num	| UL等级 颜色 |
| 4:3	| str	| `user_level_rank` 直播 用户排名|">50000"
| 4:4	| num	| 0 |
#### DANMU_MSG__info__0__15
| key				| type	| value |
| - | - | - |
| mode				| num	| 0 |
| show_player_type	| num	| 0 |
| extra				| str	| [json](#DANMU_MSG__info__0_15__extra) |
#### DANMU_MSG__info__0__15__extra
| key						| type	| value |
| - | - | - |
| send_from_me				| bool	| 0 |
| mode						| num	| 0 |
| color						| num	| 0 |
| dm_type					| num	| 0 |
| font_size					| num	| 弹幕字体大小 |
| player_mode				| num	| ？1 |
| show_player_type			| num	| ？0 |
| content					| str	| 弹幕内容 |
| user_hash					| str	| `str(DEC:crc32(uid))`十六进制转十进制转字符串 |
| emoticon_unique			| str	| 房间表情ID |
| bulge_display				| num	| 展示粉丝牌 |
| recommend_score			| num	| ？弹幕推荐等级/？智能屏蔽等级 |
| main_state_dm_color		| str	| ？"" |
| objective_state_dm_color	| str	| ？"" |
| direction					| num	| ？0 |
| pk_direction				| num	| ？0 |
| quartet_direction			| num	| ？0 |
| anniversary_crowd			| num	| ？0 |
| yeah_space_type			| str	| ？"" |
| yeah_space_url			| str	| ？"" |
| jump_to_url				| str	| ？"" |
| space_type				| str	| ？"" |
| space_url					| str	| ？"" |
| animation					| obj	| 0 |
| emots						| null?	| 0 |
#### DANMU_MSG__info__0__16
| key				| type	| value |
| - | - | - |
| activity_identity	| str	| ？"" |
| activity_source	| num	| ？0 |
| not_show			| num	| ？0 |
#### DANMU_MSG__info__2
| array	| type		| value |
| - | - | - |
| 2:0	| num		| 用户uid |
| 2:1	| str		| 用户名 |
| 2:2	| num		| ？0 |
| 2:3	| num		| ？0 |
| 2:4	| num		| ？0 |
| 2:5	| num		| ？10000 |
| 2:6	| num		| ？1 |
| 2:7	| str		| ？舰长:`"#00D1F1"` |
#### DANMU_MSG__info__3
| array	| type		| value |
| - | - | - |
| 3:0	| num		| 粉丝牌 等级 |
| 3:1	| str		| 粉丝团 称号 |
| 3:2	| num		| 主播 用户名 |
| 3:3	| num		| 直播间ID |
| 3:4	| num		| [medal_color](#medal_color) |
| 3:5	| str		| ? |
| 3:6	| num		| ? |
| 3:7	| num		| [medal_color_start](#medal_color) |
| 3:8	| num		| [medal_color_border](#medal_color) |
| 3:9	| num		| [medal_color_end](#medal_color) |
| 3:10	| num		| [舰长等级](#others) |
| 3:11	| num		| ？[is_lighted](#粉丝牌信息medal_info) |
| 3:12	| num		| 主播uid |

### CUT_OFF
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "CUT_OFF" |

### MESSAGEBOX_USER_GAIN_MEDAL
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
**根据JavaScript文件分析**
| key | type | value |
| - | - | - |
| cmd	| str	| "MESSAGEBOX_USER_MEDAL_COMPENSATION" |
| data	| obj	| |
#### MESSAGEBOX_USER_MEDAL_COMPENSATION__data
| key                   | type	| value |
| - | - | - |
| up_uid				|  | |
| add_score				|  | |

### XXXXXXXXXXX
| key | type | value |
| - | - | - |
| cmd	| str	| "XXXXXXXXXXX" |
| data	| obj	| |
#### XXXXXXXXXXX__data
| key                   | type	| value |
| - | - | - |
| data |  | |

### others
| key				| type	| value |
| - | - | - |
| dmscore			| num	| 偶数? |
| guard_level		| num	| 舰长等级 <br> 0:无 <br> 1:总督 <br> 2:提督 <br> 3:舰长 |
| privilege_type	| num	| 2:提督 3:舰长 |

uid hash 示例
| type				| value		| 备注 |
| -	| - | - |
| uid　　　　			| `12345678`	|
| 十六进制hash			|	`"9ae0daaf"`	|crc32
| 十进制　hash			|	`2598427311`	|十六进制转十进制
| 字符串型十进制　hash	|	`"2598427311"`	|十六进制转十进制转字符串

```
face:http(s)?://i[0-3].hdslb.com/bfs/(face|baselabs)/[0-9a-f]{40}.(jpg|png|gif|webp)
face:http(s)?://i[0-3].hdslb.com/bfs/face/member/noface.jpg
for i in range(1,len(a)):print(str(a[i]-a[i-1])[0:4])
```

### 粉丝牌信息medal_info
| key					| type	| value | 备注 |
| - | - | - | - |
| anchor_roomid			| num	| 舰长直播间id | 
| anchor_uname			| str	| 舰长用户名 | 
| guard_level			| num	| [舰长等级](#others) |
| icon_id				| num	| 0 |
| is_lighted			| num	| 0: <br> 1: 七天内在直播间有互动 |
| medal_color			| num	| int(HEX:RGB24) | [medal_color](#medal_color)
| medal_color_border	| num	| int(HEX:RGB24) |
| medal_color_end		| num	| int(HEX:RGB24) |
| medal_color_start		| num	| int(HEX:RGB24) |
| medal_level			| num	| 粉丝牌等级 |
| medal_name			| str	| 粉丝团称号 |
| special				| str	| "" |
| target_id				| num	| 主播uid |

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
```css
getMasterLevelStyl(level)
	if level <= 10
		(#61C05A)
	else if level <= 20
		(#5896DE)
	else if level <= 30
		(#A068F1)
	else if level <= 40
		(#FF86B2)

getFansLevelStyl(level)
	if level <= 4
		(#61DDCB)
	else if level <= 8
		(#5896DE)
	else if level <= 12
		(#A068F1)
	else if level <= 16
		(#FF86B2)
	else if level <= 20
		(#f6be18)
	else if level <= 40
		(#f6be18)

getNewFansBgColorStart(level)
	if level <= 24
		(#529d92)
	else if level <= 28
		(#7680a0)
	else if level <= 32
		(#7a6dca)
	else if level <= 36
		(#c65d8b)
	else if level <= 40
		(#fead5d)

getNewFansBgColorEnd(level)
	if level <= 24
		(#1a544b)
	else if level <= 28
		(#414967)
	else if level <= 32
		(#341160)
	else if level <= 36
		(#851332)
	else if level <= 40
		(#ff6913)

getNewFansBorderColor(level)
	if level <= 24
		(#67E8FF)
	else if level <= 28
		(#67E8FF)
	else if level <= 32
		(#FFE854)
	else if level <= 36
		(#FF7AC8)
	else if level <= 40
		(#FFE854)

getNewFansTxtColor(level)
	if level <= 24
		(#414967)
	else if level <= 28
		(#414967)
	else if level <= 32
		(#4B2F83)
	else if level <= 36
		(#B74C77)
	else if level <= 40
		(#FA8511)
.user-level-icon,
.up-level-icon
	width: 40px
	height: 16px
	border-radius: 2px
	border: 1px solid
	display: inline-block
	box-sizing: border-box
	line-height: 14px
	text-align: center
	vertical-align: middle
	font-style: normal
	font-size: 12px
	font-weight: normal

.fans-level-icon
	width: 54px
	height: 16px
	border-radius: 2px
	border: 1px solid
	display: inline-block
	box-sizing: border-box
	line-height: 14px
	text-align: center
	vertical-align: middle
	font-style: normal
	font-size: 12px
	font-weight: normal

.user-level-icon
	for i in (1..60)
		&.lv-{i}
			color: getUserLevelStyl(i)
			border-color: getUserLevelStyl(i)
.up-level-icon
	for i in (1..60)
		&.lv-{i}
			color: getMasterLevelStyl(i)
			border-color: getMasterLevelStyl(i)

.fans-level-icon
	for i in (1..20)
		&.lv-{i}
			position: relative
			color: getFansLevelStyl(i)
			border-color: getFansLevelStyl(i)
			background-color getFansLevelStyl(i)

			&:after
				right: 0
				background: #FFF
				position: absolute
				height: 14px
				width: 14px
				display: inline-block
				content: \" i \"
	for i in (21..40)
		&.lv-{i}
			position: relative
			color: getNewFansTxtColor(i)
			border: 1px solid getNewFansBgColorStart(i)
			background-image: linear-gradient(270deg, getNewFansBgColorStart(i) 0%, getNewFansBgColorEnd(i) 100%)

			&:after
				right: 0
				background: #FFF
				position: absolute
				height: 14px
				width: 16px
				display: inline-block
				content: \" i \"



// WEBPACK FOOTER //
// ./src/style/src/style/level.styl
```
```css
.gray-9 { color: rgb(153, 153, 153); }
.gray-6 { color: rgb(102, 102, 102); }
.blue { color: rgb(35, 174, 230); }
.black { color: rgb(35, 35, 35); }
.pink { color: rgb(255, 148, 177); }
.user-level-icon.lv-1 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-2 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-3 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-4 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-5 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-6 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-7 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-8 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-9 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-10 { color: rgb(150, 150, 150); border-color: rgb(150, 150, 150); }
.user-level-icon.lv-11 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-12 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-13 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-14 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-15 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-16 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-17 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-18 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-19 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-20 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.user-level-icon.lv-21 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-22 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-23 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-24 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-25 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-26 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-27 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-28 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-29 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-30 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.user-level-icon.lv-31 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-32 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-33 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-34 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-35 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-36 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-37 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-38 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-39 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-40 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.user-level-icon.lv-41 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-42 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-43 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-44 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-45 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-46 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-47 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-48 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-49 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-50 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.user-level-icon.lv-51 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-52 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-53 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-54 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-55 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-56 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-57 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-58 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-59 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.user-level-icon.lv-60 { color: rgb(255, 159, 61); border-color: rgb(255, 159, 61); }
.up-level-icon.lv-1 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-2 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-3 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-4 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-5 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-6 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-7 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-8 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-9 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-10 { color: rgb(97, 192, 90); border-color: rgb(97, 192, 90); }
.up-level-icon.lv-11 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-12 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-13 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-14 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-15 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-16 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-17 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-18 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-19 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-20 { color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); }
.up-level-icon.lv-21 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-22 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-23 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-24 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-25 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-26 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-27 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-28 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-29 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-30 { color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); }
.up-level-icon.lv-31 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-32 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-33 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-34 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-35 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-36 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-37 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-38 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-39 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-40 { color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); }
.up-level-icon.lv-41 { }
.up-level-icon.lv-42 { }
.up-level-icon.lv-43 { }
.up-level-icon.lv-44 { }
.up-level-icon.lv-45 { }
.up-level-icon.lv-46 { }
.up-level-icon.lv-47 { }
.up-level-icon.lv-48 { }
.up-level-icon.lv-49 { }
.up-level-icon.lv-50 { }
.up-level-icon.lv-51 { }
.up-level-icon.lv-52 { }
.up-level-icon.lv-53 { }
.up-level-icon.lv-54 { }
.up-level-icon.lv-55 { }
.up-level-icon.lv-56 { }
.up-level-icon.lv-57 { }
.up-level-icon.lv-58 { }
.up-level-icon.lv-59 { }
.up-level-icon.lv-60 { }
.fans-level-icon.lv-1 { position: relative; color: rgb(97, 221, 203); border-color: rgb(97, 221, 203); background-color: rgb(97, 221, 203); }
.fans-level-icon.lv-1::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 1 "; }
.fans-level-icon.lv-2 { position: relative; color: rgb(97, 221, 203); border-color: rgb(97, 221, 203); background-color: rgb(97, 221, 203); }
.fans-level-icon.lv-2::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 2 "; }
.fans-level-icon.lv-3 { position: relative; color: rgb(97, 221, 203); border-color: rgb(97, 221, 203); background-color: rgb(97, 221, 203); }
.fans-level-icon.lv-3::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 3 "; }
.fans-level-icon.lv-4 { position: relative; color: rgb(97, 221, 203); border-color: rgb(97, 221, 203); background-color: rgb(97, 221, 203); }
.fans-level-icon.lv-4::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 4 "; }
.fans-level-icon.lv-5 { position: relative; color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); background-color: rgb(88, 150, 222); }
.fans-level-icon.lv-5::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 5 "; }
.fans-level-icon.lv-6 { position: relative; color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); background-color: rgb(88, 150, 222); }
.fans-level-icon.lv-6::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 6 "; }
.fans-level-icon.lv-7 { position: relative; color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); background-color: rgb(88, 150, 222); }
.fans-level-icon.lv-7::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 7 "; }
.fans-level-icon.lv-8 { position: relative; color: rgb(88, 150, 222); border-color: rgb(88, 150, 222); background-color: rgb(88, 150, 222); }
.fans-level-icon.lv-8::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 8 "; }
.fans-level-icon.lv-9 { position: relative; color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); background-color: rgb(160, 104, 241); }
.fans-level-icon.lv-9::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 9 "; }
.fans-level-icon.lv-10 { position: relative; color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); background-color: rgb(160, 104, 241); }
.fans-level-icon.lv-10::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 10 "; }
.fans-level-icon.lv-11 { position: relative; color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); background-color: rgb(160, 104, 241); }
.fans-level-icon.lv-11::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 11 "; }
.fans-level-icon.lv-12 { position: relative; color: rgb(160, 104, 241); border-color: rgb(160, 104, 241); background-color: rgb(160, 104, 241); }
.fans-level-icon.lv-12::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 12 "; }
.fans-level-icon.lv-13 { position: relative; color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); background-color: rgb(255, 134, 178); }
.fans-level-icon.lv-13::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 13 "; }
.fans-level-icon.lv-14 { position: relative; color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); background-color: rgb(255, 134, 178); }
.fans-level-icon.lv-14::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 14 "; }
.fans-level-icon.lv-15 { position: relative; color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); background-color: rgb(255, 134, 178); }
.fans-level-icon.lv-15::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 15 "; }
.fans-level-icon.lv-16 { position: relative; color: rgb(255, 134, 178); border-color: rgb(255, 134, 178); background-color: rgb(255, 134, 178); }
.fans-level-icon.lv-16::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 16 "; }
.fans-level-icon.lv-17 { position: relative; color: rgb(246, 190, 24); border-color: rgb(246, 190, 24); background-color: rgb(246, 190, 24); }
.fans-level-icon.lv-17::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 17 "; }
.fans-level-icon.lv-18 { position: relative; color: rgb(246, 190, 24); border-color: rgb(246, 190, 24); background-color: rgb(246, 190, 24); }
.fans-level-icon.lv-18::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 18 "; }
.fans-level-icon.lv-19 { position: relative; color: rgb(246, 190, 24); border-color: rgb(246, 190, 24); background-color: rgb(246, 190, 24); }
.fans-level-icon.lv-19::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 19 "; }
.fans-level-icon.lv-20 { position: relative; color: rgb(246, 190, 24); border-color: rgb(246, 190, 24); background-color: rgb(246, 190, 24); }
.fans-level-icon.lv-20::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 14px; display: inline-block; content: " 20 "; }
.fans-level-icon.lv-21 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(82, 157, 146); background-image: linear-gradient(270deg, rgb(82, 157, 146) 0%, rgb(26, 84, 75) 100%); }
.fans-level-icon.lv-21::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 21 "; }
.fans-level-icon.lv-22 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(82, 157, 146); background-image: linear-gradient(270deg, rgb(82, 157, 146) 0%, rgb(26, 84, 75) 100%); }
.fans-level-icon.lv-22::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 22 "; }
.fans-level-icon.lv-23 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(82, 157, 146); background-image: linear-gradient(270deg, rgb(82, 157, 146) 0%, rgb(26, 84, 75) 100%); }
.fans-level-icon.lv-23::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 23 "; }
.fans-level-icon.lv-24 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(82, 157, 146); background-image: linear-gradient(270deg, rgb(82, 157, 146) 0%, rgb(26, 84, 75) 100%); }
.fans-level-icon.lv-24::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 24 "; }
.fans-level-icon.lv-25 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(118, 128, 160); background-image: linear-gradient(270deg, rgb(118, 128, 160) 0%, rgb(65, 73, 103) 100%); }
.fans-level-icon.lv-25::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 25 "; }
.fans-level-icon.lv-26 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(118, 128, 160); background-image: linear-gradient(270deg, rgb(118, 128, 160) 0%, rgb(65, 73, 103) 100%); }
.fans-level-icon.lv-26::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 26 "; }
.fans-level-icon.lv-27 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(118, 128, 160); background-image: linear-gradient(270deg, rgb(118, 128, 160) 0%, rgb(65, 73, 103) 100%); }
.fans-level-icon.lv-27::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 27 "; }
.fans-level-icon.lv-28 { position: relative; color: rgb(65, 73, 103); border: 1px solid rgb(118, 128, 160); background-image: linear-gradient(270deg, rgb(118, 128, 160) 0%, rgb(65, 73, 103) 100%); }
.fans-level-icon.lv-28::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 28 "; }
.fans-level-icon.lv-29 { position: relative; color: rgb(75, 47, 131); border: 1px solid rgb(122, 109, 202); background-image: linear-gradient(270deg, rgb(122, 109, 202) 0%, rgb(52, 17, 96) 100%); }
.fans-level-icon.lv-29::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 29 "; }
.fans-level-icon.lv-30 { position: relative; color: rgb(75, 47, 131); border: 1px solid rgb(122, 109, 202); background-image: linear-gradient(270deg, rgb(122, 109, 202) 0%, rgb(52, 17, 96) 100%); }
.fans-level-icon.lv-30::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 30 "; }
.fans-level-icon.lv-31 { position: relative; color: rgb(75, 47, 131); border: 1px solid rgb(122, 109, 202); background-image: linear-gradient(270deg, rgb(122, 109, 202) 0%, rgb(52, 17, 96) 100%); }
.fans-level-icon.lv-31::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 31 "; }
.fans-level-icon.lv-32 { position: relative; color: rgb(75, 47, 131); border: 1px solid rgb(122, 109, 202); background-image: linear-gradient(270deg, rgb(122, 109, 202) 0%, rgb(52, 17, 96) 100%); }
.fans-level-icon.lv-32::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 32 "; }
.fans-level-icon.lv-33 { position: relative; color: rgb(183, 76, 119); border: 1px solid rgb(198, 93, 139); background-image: linear-gradient(270deg, rgb(198, 93, 139) 0%, rgb(133, 19, 50) 100%); }
.fans-level-icon.lv-33::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 33 "; }
.fans-level-icon.lv-34 { position: relative; color: rgb(183, 76, 119); border: 1px solid rgb(198, 93, 139); background-image: linear-gradient(270deg, rgb(198, 93, 139) 0%, rgb(133, 19, 50) 100%); }
.fans-level-icon.lv-34::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 34 "; }
.fans-level-icon.lv-35 { position: relative; color: rgb(183, 76, 119); border: 1px solid rgb(198, 93, 139); background-image: linear-gradient(270deg, rgb(198, 93, 139) 0%, rgb(133, 19, 50) 100%); }
.fans-level-icon.lv-35::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 35 "; }
.fans-level-icon.lv-36 { position: relative; color: rgb(183, 76, 119); border: 1px solid rgb(198, 93, 139); background-image: linear-gradient(270deg, rgb(198, 93, 139) 0%, rgb(133, 19, 50) 100%); }
.fans-level-icon.lv-36::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 36 "; }
.fans-level-icon.lv-37 { position: relative; color: rgb(250, 133, 17); border: 1px solid rgb(254, 173, 93); background-image: linear-gradient(270deg, rgb(254, 173, 93) 0%, rgb(255, 105, 19) 100%); }
.fans-level-icon.lv-37::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 37 "; }
.fans-level-icon.lv-38 { position: relative; color: rgb(250, 133, 17); border: 1px solid rgb(254, 173, 93); background-image: linear-gradient(270deg, rgb(254, 173, 93) 0%, rgb(255, 105, 19) 100%); }
.fans-level-icon.lv-38::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 38 "; }
.fans-level-icon.lv-39 { position: relative; color: rgb(250, 133, 17); border: 1px solid rgb(254, 173, 93); background-image: linear-gradient(270deg, rgb(254, 173, 93) 0%, rgb(255, 105, 19) 100%); }
.fans-level-icon.lv-39::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 39 "; }
.fans-level-icon.lv-40 { position: relative; color: rgb(250, 133, 17); border: 1px solid rgb(254, 173, 93); background-image: linear-gradient(270deg, rgb(254, 173, 93) 0%, rgb(255, 105, 19) 100%); }
.fans-level-icon.lv-40::after { right: 0px; background: rgb(255, 255, 255); position: absolute; height: 14px; width: 16px; display: inline-block; content: " 40 "; }
```

### 观众等级UL_color
|st|e|color|color_hex|
|-|-|-|-|
|  1 | 10 |  9868950 | #969696 |
| 11 | 20 |  6406234 | #61C05A |
| 21 | 30 |  5805790 | #5896DE |
| 31 | 40 | 10512625 | #A068F1 |
| 41 | 50 | 16746162 | #FF86B2 |
| 51 | 60 | 16752445 | #FF9F3D |


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