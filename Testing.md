#
[主站弹幕](#主站弹幕)
[直播弹幕](#直播弹幕)

## 主站弹幕
| id	| type		| protobuf-name	| -- |
| -:	| -:		| -				| - |
|  ~~1~~	|  ~~int64~~	| ~~id~~			| 弹幕ID |
|  2	|  int32	| stime			| 弹幕出现时间（毫秒） |
|  3	|  int32	| mode			| 弹幕类型 |
|  4	|  int32	| size			| 弹幕字号 |
|  5	| uint32	| color			| 弹幕颜色 RGB24 |
|  6	| string	| uhash			| 发送者mid hash (CRC32) |
|  7	| string	| text			| 弹幕内容 |
|  8	|  int64	| date			| 发送时间 |
|  9	|  int32	| weight		| 屏蔽等级 |
| 10	| string	| action		| `airborne:[time]`<br>`picture:图像url`(图片弹幕) |
| 11	|  int32	| pool			| 弹幕池 |
| 12	| string	| dmid			| 弹幕ID |
| 13	|  int32	| attr			| 弹幕属性位 |
| 14	| ?int64	| usermid		| 发送者mid |
| 15	| ?int??	| *likes*		| 点赞数量 |
| 16	| ?int??	| ~~test16~~	| 弹幕回复，默认为 0 `first:2021-08-07` |
| 17	| ?int??	| ~~test17~~	| 弹幕回复，默认为 0 `last: 2022-09-05` |
| 18	| ?int??	| *reply_count*	| 弹幕回复数量 |
| 19	| ?			| ~~test19~~	| ? |
| 20	| string	| ~~test20~~	| 弹幕回复，默认为str:"0" |
| 21	| string	| ~~test21~~	| 弹幕回复，默认为str:"0" |
| 22	| string	| animation		| json |
| 23	| ?			| ~~test23~~	| ? |
| 24	|DmColorful	| 会员彩色弹幕	| ? |

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
	"id":"113xxxxxxxxxxxxx536",
	"content":"[前方高能]",
	"ctime":"1662xxxxxx",
	"weight":10,	// 10
	"action":"picture:i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png?scale=1.00",
	"attr":256,
	"animation":"{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png\",\"scale\":1}"},

// NFT弹幕（仅移动端）
{
	"id":"113xxxxxxxxxxxxx240",
	"content":"好耶！",
	"ctime":"1661xxxxxx",
	"attr":2048,
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxxxxxxx.png\"}"
},
{
	"id":"114xxxxxxxxxxxxx240",
	"ctime":"1663xxxxxx",
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
| command	|  4	| string	| 类型 |
| content	|  5	| string	| 互动弹幕正文 |
| progress	|  6	| int32		| 出现时间 |
| ctime		|  7	| string	| 创建时间 yyyy-MM-dd HH:mm:ss |
| mtime		|  8	| string	| 发布时间 yyyy-MM-dd HH:mm:ss |
| extra		|  9	| string	| json |
| idStr		| 10	| string	| 弹幕id string |

#### command__类型
| command 8			| content	|
| -					| -			|
| #ACTORFOLLOW# 	| "合作up主" |
| #ATTENTION#		| "关注弹幕" |
| #GRADE#			| "评分" |
| #GRADESUMMARY#	| **自定义内容** |
| #LINK#			| **自定义内容** |
| #RESERVE#			| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#				| **自定义内容** |
| #VOTE#			| "投票弹幕" |

#### ACTORFOLLOW__合作up主
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| icon					| str	| [url][url_01] |
| mid					| num	| **合作up主 mid** |
| midstr				| str	| **合作up主 mid string** |
| face					| str	| **合作up主 头像 URL** |

#### ATTENTION__关注
| key					| type	| value	| 备注 |
| -						| -		| -	| - |
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| icon					| str	| [url][url_02] |
| type					| num	| 2 |
| arc_type				| num	| 0 |
| upower_open			| bool	| |
| upower_state			| num	| true: <br> false: |
| upower_icon			| str	| true: https://i0.hdslb.com/bfs/garb/item/33e2e72d9a0c855f036b4cb55448f44af67a0635.png <br> false: "" |
| upower_icon_web		| str	| true: https://i0.hdslb.com/bfs/garb/item/05131ff2c23baa321bc8105b529170bf08b770cb.png <br> false: "" |
| upower_jump_url		| str	| true: f"https://www.bilibili.com/h5/upower/detail?mid={uid}u0026navhide=1u0026prePage=danmu" <br> false: "" |?`\\u0026` `\u0026`
| upower_button_map		| obj/null	| false: null |
| upower_guide			| str	| |
##### ATTENTION__upower_button_map
| key					| type	| value	|
| -						| -		| -		|
| -1					| obj	| |
| 0						| obj	| |
| 1						| obj	| |
| 2						| obj	| |
##### ATTENTION__upower_button_map__[×××]
| key					| type	| value	|
| -						| -		| -		|
| title					| str	| -1,0,2: "充电" <br> 1: "充电中" |
| icon					| obj	| |
| jump_url				| str	|  -1,0,2: --> `upower_jump_url` <br> 1: f"https://www.bilibili.com/h5/upower/detail?mid={uid}u0026navhide=1u0026prePage=danmu" |
##### ATTENTION__upower_button_map__[×××]__icon
| key					| type	| value	|
| -						| -		| -		|
| 10					| str	| --> `upower_icon` |
| 20					| str	| --> `upower_icon` |
| 30					| str	| --> `upower_icon` |
| 40					| str	| --> `upower_icon` |
| 50					| str	| --> `upower_icon` |

#### GRADE__评分
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| msg					| str	| 评分问题 |
| skin					| num	| 1<br>2 |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| grade_id				| num	| id |
| duration				| num	| 5000 |
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

#### GRADESUMMARY__查看总分
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| msg					| str	| **自定义内容** |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| dmids					| array	| [dmid] |
| duration				| num	| 65000 |
| icon					| str	| [url][url_03] |
| grades				| arrar	| array[obj] |
| shrink_icon			| str	| [url][url_08] |
| shrink_title			| str	| "推荐" |
| show_status			| num	| 0 |
##### GRADESUMMARY__grades
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| dmid					| num	| |
| dmid_str				| str	| |
| content				| str	| |
| grade_id				| num	| |
| mid_score				| num	| |
| count					| num	| |
| avg_score				| float	| |

#### LINK__链接
| key					| type	| value	| 备注	|
| -						| -		| -		| -	|
| aid					| num	| **目标视频avid** |
| title					| str	| **目标视频标题** |
| icon					| str	| [url][url_09] |
| bvid					| str	| **目标视频bvid** |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
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
| posX_2				| num	| |
| posY_2				| num	| |
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
| key					| type	| value	| 备注	|
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
| posX_2				| num	| |
| posY_2				| num	| |
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
| has_self_def			| bool	| |

#### posX,posY
| key	| min		| max	|
| -		| -:		| -:	|
| posX	|	118		|	549	|
| posY	|	80.5	|	889	|

## 直播弹幕
~~最低发包间隔1ms~~
| link | name | desc |
|-|-|-|
| [link](#ACTIVITY_MATCH_GIFT)					| ACTIVITY_MATCH_GIFT					| |
| [link](#ADMIN_SHIELD_KEYWORD)					| ADMIN_SHIELD_KEYWORD					| @ |
| [link](#ANCHOR_ECOMMERCE_STATUS)				| ANCHOR_ECOMMERCE_STATUS				| @ |
| [link](#ANCHOR_HELPER_DANMU)					| ANCHOR_HELPER_DANMU					| @ |
| [link](#ANCHOR_LOT_CHECKSTATUS)				| ANCHOR_LOT_CHECKSTATUS				| 抽奖：检查 |
| [link](#ANCHOR_LOT_START)						| ANCHOR_LOT_START						| 抽奖：开始 |
| [link](#ANCHOR_LOT_END)						| ANCHOR_LOT_END						| 抽奖：结束 |
| [link](#ANCHOR_LOT_AWARD)						| ANCHOR_LOT_AWARD						| 抽奖：结果 |
| [link](#AREA_RANK_CHANGED)					| AREA_RANK_CHANGED						| 主播：直播分区更改 |
| [link](#BOX_ACTIVITY_START)					| BOX_ACTIVITY_START					| |
| [link](#CHANGE_ROOM_INFO)						| CHANGE_ROOM_INFO						| WEB:更改直播间背景 |
| [link](#CHASE_FRAME_SWITCH)					| CHASE_FRAME_SWITCH					| |
| [link](#COMBO_END)							| COMBO_END								| |
| [link](#COMBO_SEND)							| COMBO_SEND							| 送礼物：连击 |
| [link](#COMMON_NOTICE_DANMAKU)				| COMMON_NOTICE_DANMAKU					| 弹幕区域：弹幕区通知 |
| [link](#CUT_OFF)								| CUT_OFF								| 切断直播！|
| [link](#DANMU_AGGREGATION)					| DANMU_AGGREGATION						| 通知栏：抽奖通知 |
| [link](#DANMU_GIFT_LOTTERY_AWARD)				| DANMU_GIFT_LOTTERY_AWARD				| |
| [link](#DANMU_GIFT_LOTTERY_END)				| DANMU_GIFT_LOTTERY_END				| |
| [link](#DANMU_GIFT_LOTTERY_START)				| DANMU_GIFT_LOTTERY_START				| |
| [link](#DANMU_MSG)							| DANMU_MSG								| 用户：弹幕！ |
| [link](#DANMU_TAG_CHANGE)						| DANMU_TAG_CHANGE						| |
| [link](#DM_INTERACTION)						| DM_INTERACTION						| 游戏&弹幕：投票 |
| [link](#ENTRY_EFFECT)							| ENTRY_EFFECT							| 进入直播间特效 |
| [link](#ENTRY_EFFECT)							| ENTRY_EFFECT_MUST_RECEIVE				| 进入直播间特效 |
| [link](#FULL_SCREEN_SPECIAL_EFFECT)			| FULL_SCREEN_SPECIAL_EFFECT			| @ |
| [link](#GOTO_BUY_FLOW)						| GOTO_BUY_FLOW							| 移动端 购买 |
| [link](#GIFT_PANEL_PLAN)						| GIFT_PANEL_PLAN						| |
| [link](#GIFT_STAR_PROCESS)					| GIFT_STAR_PROCESS						| 礼物星球：进度|
| [link](#GUARD_ACHIEVEMENT_ROOM)				| GUARD_ACHIEVEMENT_ROOM				| 恭喜主播xxx舰队规模突破xxx |
| [link](#GUARD_BENEFIT_RECEIVE)				| GUARD_BENEFIT_RECEIVE					| |
| [link](#GUARD_BUY)							| GUARD_BUY								| 通知栏：舰长购买 |
| [link](#GUARD_HONOR_THOUSAND)					| GUARD_HONOR_THOUSAND					| 千舰 **广播** |
| [link](#GUARD_LOTTERY_START)					| GUARD_LOTTERY_START					| |
| [link](#GUARD_WINDOWS_OPEN)					| GUARD_WINDOWS_OPEN					| |
| [link](#HOT_BUY_NUM)							| HOT_BUY_NUM							| 移动端_btn：推广购物 |
| link											| ~~HOT_RANK_CHANGED_V2~~				| [热门榜功能下线公告]|
| link											| ~~HOT_RANK_CHANGED~~					| [热门榜功能下线公告]|
| link											| ~~HOT_RANK_SETTLEMENT_V2~~			| [热门榜功能下线公告]|
| link											| ~~HOT_RANK_SETTLEMENT~~				| [热门榜功能下线公告]|
| [link](#HOT_ROOM_NOTIFY)						| HOT_ROOM_NOTIFY						| ？ |
| [link](#HOUR_RANK_AWARDS)						| HOUR_RANK_AWARDS 						| |
| [link](#INTERACT_WORD)						| INTERACT_WORD							| 通知栏：进入直播间/关注主播 |
| [link](#LIKE_INFO_V3_CLICK)					| LIKE_INFO_V3_CLICK					| 移动端：点赞 |
| [link](#LIKE_INFO_V3_NOTICE)					| LIKE_INFO_V3_NOTICE					| 点赞：xxxx |
| [link](#LIKE_INFO_V3_UPDATE)					| LIKE_INFO_V3_UPDATE					| 状态栏：点赞更新 |
| [link](#LIKE_SO_HOT)							| LIKE_SO_HOT 							| |
| [link](#LITTLE_MESSAGE_BOX)					| LITTLE_MESSAGE_BOX					| |
| [link](#LITTLE_TIPS)							| LITTLE_TIPS 							| |
| [link](#LIVE)									| LIVE									| 开播 |
| [link](#LIVE_INTERACTIVE_GAME)				| LIVE_INTERACTIVE_GAME					| @ |
| [link](#LIVE_INTERNAL_ROOM_LOGIN)				| LIVE_INTERNAL_ROOM_LOGIN				| |
| [link](#LIVE_MULTI_VIEW_CHANGE)				| LIVE_MULTI_VIEW_CHANGE				| @ |
| [link](#LIVE_OPEN_PLATFORM_CLOUD_GAME)		| LIVE_OPEN_PLATFORM_CLOUD_GAME			| |
| [link](#LIVE_OPEN_PLATFORM_GAME)				| LIVE_OPEN_PLATFORM_GAME				| 弹幕互动游戏 |
| [link](#LIVE_PANEL_ICON_INFO)					| LIVE_PANEL_ICON_INFO					| |
| [link](#LIVE_PLAYER_LOG_RECYCLE)				| LIVE_PLAYER_LOG_RECYCLE				| |
| [link](#LOG_IN_NOTICE)						| LOG_IN_NOTICE							| !!! |
| [link](#LOL_ACTIVITY)							| LOL_ACTIVITY							| |
| [link](#MATCH_TEAM_GIFT_RANK)					| MATCH_TEAM_GIFT_RANK					| |
| [link](#MESSAGEBOX_USER_GAIN_MEDAL)			| MESSAGEBOX_USER_GAIN_MEDAL			| |
| [link](#MESSAGEBOX_USER_MEDAL_CHANGE)			| MESSAGEBOX_USER_MEDAL_CHANGE			| |
| [link](#MESSAGEBOX_USER_MEDAL_COMPENSATION)	| MESSAGEBOX_USER_MEDAL_COMPENSATION	| |
| [link](#MILESTONE_UPDATE_EVENT)				| MILESTONE_UPDATE_EVENT 				| |
| [link](#MULTI_VOICE_STATUS_SYNC)				| MULTI_VOICE_STATUS_SYNC				| |
| [link](#NOTICE_MSG)							| NOTICE_MSG							| 滚动横幅 |
| [link](#OFFICIAL_ROOM_EVENT)					| OFFICIAL_ROOM_EVENT					| |
| [link](#ONLINE_RANK_COUNT)					| ONLINE_RANK_COUNT						| 状态栏：在线观众 |
| [link](#ONLINE_RANK_TOP3)						| ONLINE_RANK_TOP3						| 高能榜：高能用户前三恭喜 |
| [link](#ONLINE_RANK_V2)						| ONLINE_RANK_V2						| 高能榜：高能用户TOP7 |
| [link](#PK_AGAIN)								| PK_AGAIN								| |
| [link](#PK_BATTLE_CRIT)						| PK_BATTLE_CRIT						| |
| [link](#PK_BATTLE_END)						| PK_BATTLE_END							| PK@ |
| [link](#PK_BATTLE_FINAL_PROCESS)				| PK_BATTLE_FINAL_PROCESS				| PK@ |
| [link](#PK_BATTLE_GIFT)						| PK_BATTLE_GIFT						| |
| [link](#PK_BATTLE_PRE_NEW)					| PK_BATTLE_PRE_NEW						| PK@ |
| [link](#PK_BATTLE_PRO_TYPE)					| PK_BATTLE_PRO_TYPE					| |
| [link](#PK_BATTLE_PROCESS_NEW)				| PK_BATTLE_PROCESS_NEW					| PK@ |
| [link](#PK_BATTLE_PUNISH_END)					| PK_BATTLE_PUNISH_END					| PK@ |
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
| [link](#PLAY_TAG)								| PLAY_TAG								| LOL 比赛：事件 |
| [link](#PLAY_TOGETHER)						| PLAY_TOGETHER							| |
| [link](#POPULAR_RANK_CHANGED)					| POPULAR_RANK_CHANGED					| @ |
| [link](#POPULARITY_RED_POCKET_NEW)			| POPULARITY_RED_POCKET_NEW				| 人气红包 |
| [link](#POPULARITY_RED_POCKET_START)			| POPULARITY_RED_POCKET_START			| 人气红包 |
| [link](#POPULARITY_RED_POCKET_WINNER_LIST)	| POPULARITY_RED_POCKET_WINNER_LIST		| 人气红包 |
| [link](#PREPARING)							| PREPARING								| 下播/被下播 |
| [link](#RAFFLE_END)							| RAFFLE_END							| |
| [link](#RAFFLE_START)							| RAFFLE_START							| |
| [link](#RANK_REM)								| RANK_REM								| @ |
| [link](#RECOMMEND_CARD)						| RECOMMEND_CARD						| 商品推销(移动端) |
| [link](#RED_POCKET_START)						| RED_POCKET_START						| |
| [link](#REENTER_LIVE_ROOM)					| REENTER_LIVE_ROOM						| |
| [link](#Revenue_PayLimit)						| Revenue_PayLimit						| |
| [link](#ROOM_BANNER)							| ROOM_BANNER							| |
| [link](#ROOM_BLOCK_INTO)						| ROOM_BLOCK_INTO						| |
| [link](#ROOM_BLOCK_MSG)						| ROOM_BLOCK_MSG						| 用户封禁 |
| [link](#ROOM_CHANGE)							| ROOM_CHANGE							| 直播间标题更改/直播间分区更改 |
| [link](#ROOM_KICKOUT)							| ROOM_KICKOUT							| |
| [link](#ROOM_LIMIT)							| ROOM_LIMIT							| |
| [link](#ROOM_LOCK)							| ROOM_LOCK								| |
| [link](#ROOM_RANK)							| ROOM_RANK								| |
| [link](#ROOM_REAL_TIME_MESSAGE_UPDATE)		| ROOM_REAL_TIME_MESSAGE_UPDATE			| 当前粉丝团人数，关注人数 |
| [link](#ROOM_REFRESH)							| ROOM_REFRESH							| |
| [link](#ROOM_SILENT_xxx)						| ROOM_SILENT_OFF/ROOM_SILENT_ON		| 直播间全局禁言 |
| [link](#ROOM_SKIN_MSG)						| ROOM_SKIN_MSG							| 直播间皮肤？ |
| [link](#SEND_GIFT)							| SEND_GIFT								| 送礼物 |
| [link](#SEND_GIFT_V2)							| SEND_GIFT_V2							| |
| [link](#SEND_TOP)								| SEND_TOP								| |
| [link](#SHOPPING_CART_SHOW)					| SHOPPING_CART_SHOW					| ？购物车 |
| [link](#SPECIAL_GIFT)							| SPECIAL_GIFT							| 特殊礼物 |
| [link](#STARLIVE_PK_MSG)						| STARLIVE_PK_MSG						| |
| [link](#STOP_LIVE_ROOM_LIST)					| STOP_LIVE_ROOM_LIST					| @ |
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
| [link](#USER_INFO_UPDATE)						| USER_INFO_UPDATE						| |
| [link](#USER_PANEL_RED_ALARM)					| USER_PANEL_RED_ALARM					| |
| [link](#USER_TITLE_GET)						| USER_TITLE_GET						| |
| [link](#USER_TOAST_MSG)						| USER_TOAST_MSG						| 弹幕区域：舰长购买通知 |
| [link](#USER_VIRTUAL_MVP)						| USER_VIRTUAL_MVP						| |
| [link](#VIDEO_CONNECTION_JOIN_END)			| VIDEO_CONNECTION_JOIN_END				| |
| [link](#VIDEO_CONNECTION_JOIN_START)			| VIDEO_CONNECTION_JOIN_START			| |
| [link](#VIDEO_CONNECTION_MSG)					| VIDEO_CONNECTION_MSG					| |
| [link](#VOICE_CHAT_UPDATE)					| VOICE_CHAT_UPDATE						| 语音@ |
| [link](#VOICE_JOIN_STATUS)					| VOICE_JOIN_STATUS						| 语音@ |
| [link](#VTR_GIFT_LOTTERY)						| VTR_GIFT_LOTTERY						| |
| [link](#WARNING)								| WARNING								| 警告 |
| [link](#WATCH_LPL_EXPIRED)					| WATCH_LPL_EXPIRED						| |
| [link](#WATCHED_CHANGE)						| WATCHED_CHANGE						| 观看人数 |
| [link](#WEB_REPORT_CONTROL)					| WEB_REPORT_CONTROL					| |
| [link](#WIDGET_BANNER)						| WIDGET_BANNER							| ？|
| [link](#WIDGET_GIFT_STAR_PROCESS)				| WIDGET_GIFT_STAR_PROCESS				| 礼物星球@ |
| [link](#WIN_ACTIVITY)							| WIN_ACTIVITY							| |
| [link](#WIN_ACTIVITY_USER)					| WIN_ACTIVITY_USER						| |
----
----
### LOG_IN_NOTICE
[TOP](#直播弹幕)  
```json
{
	"cmd":"LOG_IN_NOTICE",
	"data":{
		"notice_msg":"为保护用户隐私，未注册登陆用户将无法查看他人昵称",// *和头像 uid
		"image_web":"http://i0.hdslb.com/bfs/dm/75e7c16b99208df259fe0a93354fd3440cbab412.png",
		"image_app":""
	}
}
```
----
### WARNING
[TOP](#直播弹幕)  
**警告**
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WARNING" |
| msg		| str	| |
| roomid	| str	| 直播间id |
#### WARNING__msg
```json
"因版权原因，请立即调整"
"图片内容不适宜，请立即调整"
"禁止在直播间内展示平台外的评论、弹幕内容，请立即调整"
"违反直播分区规范，请立即更换至游戏区"
"禁止直播违禁游戏，请立即更换"
"直播中涉及低俗内容"
"直播视角不适宜"
```
----
### LIVE
[TOP](#直播弹幕)  
开播
| key 10,11			| type	| value	| xxx
|-|-|-|-|
| cmd				| str	| "LIVE" |
| live_key			| str	| xxxx |
| voice_background	| str	| 仅音频直播_背景 |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| 开播方式 | |
| live_model		| num	| ？Live2D | 3: <br> 4:开启？
| live_time	※		| num	| 开播时间TimeStamp(秒) |
| roomid			| num	| 长_短直播间ID |
| is_report			| bool	| |
| msg_id			| str	| |
| send_time			| num	| |
```json
1678276390438433{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"pc","live_model":0,"live_time":1672502400,"roomid":12345}
1678276420141264{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"pc","live_model":0,"roomid":12345}
1678629817656000{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios_link","live_model":4,"live_time":1672502400,"roomid":12345}
1678629817657000{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios_link","live_model":4,"roomid":12345}
1676034064879000{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","sub_session_key":"111111111111111111sub_time:1676034003","live_platform":"ios","live_model":3,"live_time":1676034003,"roomid":12345}
1678693610423000{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/b4414564939585e079b130765116bb34a46d9ee7.png","sub_session_key":"111111111111111111sub_time:1678693595","live_platform":"ios_link","live_model":3,"live_time":1678693595,"roomid":12345}
1680263124480121{"cmd":"LIVE","live_key":"360846582248079647","voice_background":"","sub_session_key":"360846582248079647sub_time:1680263123","live_platform":"events_broadcast","live_model":0,"live_time":1680263123,"roomid":21987615}
1680263127445895{"cmd":"LIVE","live_key":"360846582248079647","voice_background":"","sub_session_key":"360846582248079647sub_time:1680263123","live_platform":"events_broadcast","live_model":0,"roomid":21987615}
1682764200147614{"cmd":"LIVE","live_key":"363170254022513984","voice_background":"","sub_session_key":"363170254022513984sub_time:1682764199","live_platform":"live_mng","live_model":0,"live_time":1682764199,"roomid":5440}
1683978432633193{"cmd":"LIVE","live_key":"376037065530245407","voice_background":"","sub_session_key":"376037065530245407sub_time:1683978433","live_platform":"events_broadcast","live_model":0,"live_time":1683978433,"roomid":21987615}
1683978435953192{"cmd":"LIVE","live_key":"376037065530245407","voice_background":"","sub_session_key":"376037065530245407sub_time:1683978433","live_platform":"events_broadcast","live_model":0,"roomid":21987615}
1688814113748216{"cmd":"LIVE","is_report":false,"live_key":"382683437231767695","live_model":0,"live_platform":"pc","live_time":1688814114,"msg_id":"136437659867648","roomid":27263119,"send_time":1688814114184,"sub_session_key":"382683437231767695sub_time:1688814114","voice_background":""}
1688788715926489{"cmd":"LIVE","is_report":false,"live_key":"111111111111111111","live_model":0,"live_platform":"pc_link","live_time":1672502400,"msg_id":"xxx","roomid":545068,"send_time":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":""}
1688788715929444{"cmd":"LIVE","is_report":false,"live_key":"111111111111111111","live_model":0,"live_platform":"pc_link","msg_id":"xxx","roomid":545068,"send_time":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":""}
1688821229036805{"cmd":"LIVE","is_report":false,"live_key":"381495578107184056","live_model":0,"live_platform":"live_mng","msg_id":"xxx","roomid":7734200,"send_time":xxx,"sub_session_key":"381495578107184056sub_time:1687706973","voice_background":"http://i0.hdslb.com/bfs/live/24cab10ebe09222c1de678ed8180d7050766c67b.jpg"}
1688996158945176{"cmd":"LIVE","is_report":false,"live_key":"111111111111111111","live_model":5,"live_platform":"android_link","live_time":1672502400,"msg_id":"xxx","roomid":12345,"send_time":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":""}
```
#### live_platform
| live_platform		| desc	|
|-|-|-|-|
| live_mng			| LPL |
| pc				| ~~ |
| pc_link			| PC 直播姬 |
| ios_link			| iOS 直播姬 |
| ios				| iOS Bilibili APP |
| android_link		| Android 直播姬 |
| events_broadcast	| 预录制发布会 |
| xxxxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxxxx	| xxx |

----
### SEND_GIFT
[TOP](#直播弹幕)  
送礼物
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SEND_GIFT" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SEND_GIFT__data
| key 54				| type		| value	| 备注 |
|-|-|-|-|
| action				| str		| "投喂" |
| **batch_combo_id**	| str		| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{时间TimeStamp.4f}"` <br> 盲盒:UUID4 |
| **batch_combo_send**	| null/obj	| [batch_combo_send](#SEND_GIFT__data__batch_combo_send) |
| beatId				| str		| ？"0" |
| biz_source			| str		| "Live" |
| **blind_gift**		| null/obj	| |
| broadcast_id			| num		| 0 |
| coin_type				| str		| "gold"/"silver" |
| combo_resources_id	| num		| 1 |
| combo_send			| null/obj	| |
| combo_stay_time		| num		| 3 |
| combo_total_coin		| num		| !!! |
| crit_prob				| num		| 0 |
| demarcation			| num		| 1,2 |
| discount_price		| num		| xxx |
| dmscore				| num		| 4×N |
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
| is_first				| bool		| |
| is_join_receiver		| bool		| false |
| is_naming				| bool		| |
| is_special_batch		| num		| 0 |
| magnification			| float		| 0 |
| medal_info			| obj		| [粉丝牌信息](#粉丝牌信息medal_info) | 不包含 anchor_uname, anchor_roomid
| name_color			| str		| "" |
| num					| num		| 礼物数量 |
| original_gift_name	| str		| "" |
| price					| num		| 礼物价格,RMB×1000 |
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
| total_coin			| num		| 礼物总价,RMB×1000 |
| uid					| num		| 发送者uid |
| uname					| str		| 发送者昵称 |
#### SEND_GIFT__data__batch_combo_send
| key 10				| type		| value	|
|-|-|-|
| action				| str		| 与父级内容相同 |
| batch_combo_id		| str		| 与父级内容相同 |
| batch_combo_num		| num		| |
| blind_gift			| null/obj	| 与父级内容相同 |
| giftId				| num		| 与父级内容相同 |
| giftName				| str		| 与父级内容相同 |
| gift_num				| num		| 礼物xx |
| send_master			| null		| 与父级内容相同 |
| uid					| num		| 与父级内容相同 |
| uname					| str		| 发送者昵称 |
#### SEND_GIFT__data__combo_send
| key 9					| type		| value	|
|-|-|-|
| action				| str		| 与父级内容相同 |
| combo_id				| str		| ？ |
| combo_num				| num		| |
| giftId				| num		| 与父级内容相同 |
| giftName				| str		| 与父级内容相同 |
| gift_num				| num		| 礼物xx |
| send_master			| null		| 与父级内容相同 |
| uid					| num		| 与父级内容相同 |
| uname					| str		| 发送者昵称 |
#### SEND_GIFT__data__receive_user_info
| key 2					| type		| value	|
|-|-|-|
| uid					| num		| 接收者uid |
| uname					| str		| 接收者昵称 |
```json
{
	"cmd": "SEND_GIFT",
	"data": {
		"action": "投喂",
		"bag_gift": null,
		"batch_combo_id": "",
		"batch_combo_send": null,
		"beatId": "0",
		"biz_source": "Live",
		"blind_gift": null,
		"broadcast_id": 0,
		"coin_type": "silver",
		"combo_resources_id": 1,
		"combo_send": null,
		"combo_stay_time": 5,
		"combo_total_coin": 0,
		"crit_prob": 0,
		"demarcation": 2,
		"discount_price": 0,
		"dmscore": 40,
		"draw": 0,
		"effect": 3,
		"effect_block": 1,
		"face": "$avatar_url",
		"face_effect_id": 0,
		"face_effect_type": 0,
		"float_sc_resource_id": 0,
		"giftId": 31738,
		"giftName": "粉丝团灯牌",
		"giftType": 5,
		"gold": 0,
		"guard_level": 0,
		"is_first": true,
		"is_join_receiver": false,
		"is_naming": false,
		"is_special_batch": 0,
		"magnification": 1,
		"medal_info": {
			"anchor_roomid": 0,
			"anchor_uname": "",
			"guard_level": 0,
			"icon_id": 0,
			"is_lighted": 0,
			"medal_color": 0,
			"medal_color_border": 0,
			"medal_color_end": 0,
			"medal_color_start": 0,
			"medal_level": 0,
			"medal_name": "",
			"special": "",
			"target_id": 0
		},
		"name_color": "",
		"num": 1,
		"original_gift_name": "",
		"price": 1000,
		"rcost":xxxxx,
		"receive_user_info": {
			"uid":xxxxx,
			"uname": "xxxxx"
		},
		"remain": 104,
		"rnd": "1672502400000",
		"send_master": null,
		"silver": 0,
		"super": 0,
		"super_batch_gift_num": 0,
		"super_gift_num": 0,
		"svga_block": 0,
		"switch": true,
		"tag_image": "",
		"tid": "1672502400000",
		"timestamp": 1672502400,
		"top_list": null,
		"total_coin": 1000,
		"uid":xxxxx,
		"uname": "xxxxx",
		"wealth_level": 0
	},
	"is_report": false,
	"msg_id": "xxx",
	"send_time":xxx
}
```
----
### ONLINE_RANK_V2
[TOP](#直播弹幕)  
高能用户前七(左)，实时
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_V2" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ONLINE_RANK_V2__data
| key		| type		| value	|
|-|-|-|
| list		| [7]obj	| |
| rank_type	| str		| "gold-rank" |
#### ONLINE_RANK_V2__data__list
| key 6			| type	| value	|
|-|-|-|
| uid			| num | uid |
| face			| str | 头像URL |
| score			| str | 贡献值 |
| uname			| str | 昵称 |
| rank			| num | 排名(1-7) |
| guard_level	| num | 舰长等级 |
```json
{"cmd":"ONLINE_RANK_V2","data":{"list":[
	{"face":"$avatar_url","guard_level":2,"rank":1,"score":"8","uid":1,"uname":"****"},
	{"face":"$avatar_url","guard_level":2,"rank":2,"score":"7","uid":2,"uname":"****"},
	{"face":"$avatar_url","guard_level":3,"rank":3,"score":"6","uid":3,"uname":"****"},
	{"face":"$avatar_url","guard_level":3,"rank":4,"score":"5","uid":4,"uname":"****"},
	{"face":"$avatar_url","guard_level":3,"rank":5,"score":"4","uid":5,"uname":"****"},
	{"face":"$avatar_url","guard_level":3,"rank":6,"score":"3","uid":6,"uname":"****"},
	{"face":"$avatar_url","guard_level":3,"rank":7,"score":"2","uid":7,"uname":"****"}
],"rank_type":"gold-rank"}
,"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ONLINE_RANK_TOP3
[TOP](#直播弹幕)  
高能用户前三(左)
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_TOP3" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ONLINE_RANK_TOP3__data
| key		| type		| value	|
|-|-|-|
| dmscore	| num		| 112 |
| list		| [1]obj	| |
#### ONLINE_RANK_TOP3__data__list
| key	| type	| value	|
|-|-|-|
| msg	| str	| `f"恭喜 <%{昵称}%> 成为高能用户"` |
| rank	| num	| 排名(1-3) |
```json
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXX%> 成为高能用户","rank":1}]},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXX%> 成为高能用户","rank":2}]},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":112,"list":[{"msg":"恭喜 <%XXX%> 成为高能用户","rank":3}]},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ONLINE_RANK_COUNT
[TOP](#直播弹幕)  
高能用户人数(观众人数)  
约每5×N秒发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_COUNT" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ONLINE_RANK_COUNT__data
| key		| type	| value	|
|-|-|-|
| count		| num	| 最大值**约**为10000[1-100xx] |
```json
{"cmd":"ONLINE_RANK_COUNT","data":{"count":1},"is_report":false,"msg_id":"xxx","send_time":1689168613835}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":10000},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### INTERACT_WORD
[TOP](#直播弹幕)  
进入直播间、关注主播通知（高精度）500ms
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_WORD" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### INTERACT_WORD__data
| key 18				| type		| value	| |
|-|-|-|-|
| contribution			| obj		| ？ |
| contribution.grade	| num		| ？ |
| core_user_type		| num		| ?大部分为0[0-5] |
| dmscore				| num		| | 1 2 3 4 5 6 7 8 9 10 12 14 15 16 18 20 22 26 28 30 32 34 35 40 45 50 60 75
| fans_medal			| null/obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| identities			| []num		| [identities](#others) |
| is_spread				| num		| 0,1 |
| msg_type				| num		| |
| privilege_type		| num		| [privilege_type](#others) is_spread==1:`0` |
| roomid				| num		| 长_短直播间ID |
| score					| num		| ? |
| spread_desc			| str		| is_spread==1:"流量包推广" |
| spread_info			| str		| is_spread==1:"#FF649E" |
| tail_icon				| num		| 0,101,102 |
| timestamp				| num		| TimeStamp(秒) |
| trigger_time			| num		| TimeStamp(皮秒)(100ps) |
| uid					| num		| 发送者uid |
| uname					| str		| 发送者昵称 |
| uname_color			| str		| "" |
#### INTERACT_WORD__msg_type
```js
Entry = 1
Attention = 2
Share = 3
SpecialAttention = 4
MutualAttention = 5
Link = 6
"Entry:进入直播间"
"Entry:光临直播间"！舰长
	u = ((e = {})[L.Sv.Entry] = identity < 3 ? "进入" :"光临",
	e[L.Sv.Attention] = "关注了",
	e[L.Sv.Share] = "分享了",
	e[L.Sv.SpecialAttention] = "特别关注了",
	e[L.Sv.MutualAttention] = "互粉了",
	e[L.Sv.Link] = text,
	e),
	l = this.createElement("span","t-over-hidden interact-name v-middle",username,[["style","color:" + t.nameColor + "; margin-right:4px;"]]),
	f = this.createElement("span","flex-no-shrink v-middle",u[msgType] + (msgType !== L.Sv.Link ? "直播间" :""),msgType > L.Sv.Entry && msgType !== L.Sv.Link ? [["style","color:#F7B500"]] :[["style","color: #999999"]]);
```
```json
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":102,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":2,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":3,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":1,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"流量包推广","spread_info":"#FF649E","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":102,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":2,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":3,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":1,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"流量包推广","spread_info":"#FF649E","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,1],"is_spread":0,"msg_type":3,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":102,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":3,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":3,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[8,3,1],"is_spread":0,"msg_type":1,"privilege_type":1,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":2,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":2,"dmscore":0,"fans_medal":null,"identities":[7,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":2,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":3,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":3,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":5,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":5,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":0},"core_user_type":5,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":1,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"流量包推广","spread_info":"#FF649E","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[8,3,1],"is_spread":0,"msg_type":1,"privilege_type":1,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":1},"core_user_type":3,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":2},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":2},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":2},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":2},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":2},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":3},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":3},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[3,1],"is_spread":0,"msg_type":1,"privilege_type":0,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":3},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[6,3,1],"is_spread":0,"msg_type":1,"privilege_type":3,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"INTERACT_WORD","data":{"contribution":{"grade":3},"core_user_type":0,"dmscore":0,"fans_medal":null,"identities":[7,3,1],"is_spread":0,"msg_type":1,"privilege_type":2,"roomid":0,"score":0,"spread_desc":"","spread_info":"","tail_icon":0,"timestamp":1672502400,"trigger_time":1672502400000000000,"uid":123,"uname":"","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### WATCHED_CHANGE
[TOP](#直播弹幕)  
(每5秒&数值更新)发送一次 用户(包括游客、主播)进入直播间时发送
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WATCHED_CHANGE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### WATCHED_CHANGE__data
| key 3			| type	| value	|
|-|-|-|
| num			| num	| 人数 |
| text_small	| str	| str(num) <br> "x.y万" |
| text_large	| str	| f"num人看过" <br> "x.y万人看过" |
```json
{"cmd":"WATCHED_CHANGE","data":{"num":       0,"text_large":       "0人看过","text_small":"0"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"WATCHED_CHANGE","data":{"num":    9999,"text_small":          "9999","text_large":"9999人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num":   10001,"text_small":         "1.0万","text_large":"1.0万人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num":91921951,"text_large":"9192.1万人看过","text_small":"9192.1万"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### ROOM_REAL_TIME_MESSAGE_UPDATE
[TOP](#直播弹幕)  
(每N×60秒&数值更新)发送一次，更新关注数、粉丝团人数
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE__data
| key 4			| type	| value	|
|-|-|-|
| roomid		| num	| 长直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1? |
| fans_club		| num	| 粉丝团成员(活跃人数) |
```json
{"cmd":"ROOM_REAL_TIME_MESSAGE_UPDATE","data":{"fans":12345,"fans_club":12345,"red_notice":-1,"roomid":123456},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### LIKE_INFO_V3_CLICK
[TOP](#直播弹幕)  
点赞，和`LIKE_INFO_V3_UPDATE`同时发送，实时&每5秒最多发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_CLICK" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### LIKE_INFO_V3_CLICK__data
| key 11					| type	| value	|
|-|-|-|
| show_area					| num	| 0 <br> 1(30s) |
| msg_type					| num	| 6 |
| like_icon					| str	| [图标][img_16] |
| uid						| num	| uid |
| like_text					| str	| "为主播点赞了" |
| uname						| str	| 昵称 |
| uname_color				| str	| "" |
| identities				| []num	| [identities](#others) |
| fans_medal				| obj	| [fans_medal](#粉丝牌信息medal_info) |
| contribution_info			| obj	| |
| contribution_info.grade	| num	| |
| dmscore					| num	| 20 |
```json
{"cmd":"LIKE_INFO_V3_CLICK","data":{"contribution_info":{"grade":0},"dmscore":20,"fans_medal":xxx,"identities":[3,1],"like_icon":"https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png","like_text":"为主播点赞了","msg_type":6,"show_area":1,"uid":xxx,"uname":"xxx","uname_color":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### LIKE_INFO_V3_NOTICE
[TOP](#直播弹幕)  
202306新增  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_NOTICE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### LIKE_INFO_V3_NOTICE__data
| key				| type	| value	|
|-|-|-|
| content_segments	| []	| |
| danmaku_style		| obj	| |
| terminals			| []num	| |
```json
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"试试双击点赞，让主播被更多人看到吧～"                   ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[1,4]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计100，快去号召直播间用户继续为你助力吧~"    ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计500，快去号召直播间用户继续为你助力吧~"    ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计5000，快去号召直播间用户继续为你助力吧~"   ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计10000，快去号召直播间用户继续为你助力吧~"  ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计50000，快去号召直播间用户继续为你助力吧~"  ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计1000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计5000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### LIKE_INFO_V3_UPDATE
[TOP](#直播弹幕)  
点赞，和`LIKE_INFO_V3_CLICK`同时发送，实时&每5秒最多发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_UPDATE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### LIKE_INFO_V3_UPDATE__data
| key			| type	| value	|
|-|-|-|
| click_count	| num	| 点赞数量 |
```json
{"cmd":"LIKE_INFO_V3_UPDATE","data":{"click_count":1},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### HOT_ROOM_NOTIFY
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "HOT_ROOM_NOTIFY" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### HOT_ROOM_NOTIFY__data
| key 4					| type	| value	|
|-|-|-|
| threshold				| num	| 10000 |
| ttl					| num	| 300 |
| exit_no_refresh		| num	| 1 |
| random_delay_req_v2	| []	| |
#### HOT_ROOM_NOTIFY__data__random_delay_req_v2
| key	| type	| value	|
|-|-|-|
| path	| str	| |
| delay	| num	| |
```json
{"cmd":"HOT_ROOM_NOTIFY","data":{"threshold":10000,"ttl":300,"exit_no_refresh":1,"random_delay_req_v2":[{"path":"/live/getRoundPlayVideo","delay":10},{"path":"/xlive/web-room/v1/index/getOffLiveList","delay":120000}]}}
{"cmd":"HOT_ROOM_NOTIFY","data":{"exit_no_refresh":1,"random_delay_req_v2":[{"delay":10,"path":"/live/getRoundPlayVideo"},{"delay":120000,"path":"/xlive/web-room/v1/index/getOffLiveList"}],"threshold":10000,"ttl":300},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### ENTRY_EFFECT
[TOP](#直播弹幕)  
`ENTRY_EFFECT` 欢迎舰长进入直播间，高精度  
`ENTRY_EFFECT_MUST_RECEIVE` 欢迎主播进入直播间，高精度
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ENTRY_EFFECT" "ENTRY_EFFECT_MUST_RECEIVE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ENTRY_EFFECT__data
| key 30					| type | value	| |
|-|-|-|-|
| id						| num	| |
| uid						| num	| 用户uid |
| target_id					| num	| 主播uid |
| mock_effect				| num	| 0? |
| face						| str	| 头像URL |
| privilege_type			| num	| [privilege_type](#others) |
| copy_writing				| str	| `f"欢迎(舰长\|提督\|总督) <%{昵称}%> 进入直播间"` |限长7字符，省略号为`...`
| copy_color				| str	| rgb24 小写 |
| highlight_color			| str	| rgb24 大写 |
| priority					| num	| 1? |
| basemap_url				| str	| basemap_url=web_basemap_url |
| show_avatar				| num	| 1 |
| effective_time			| num	| effective_time=web_effective_time |
| web_basemap_url			| str	| basemap_url=web_basemap_url |
| web_effective_time		| num	| effective_time=web_effective_time |
| web_effect_close			| num	| |
| web_close_time			| num	| |
| business					| num	| |
| copy_writing_v2			| str	| `f"欢迎 <^icon^> <%{昵称}%> 进入直播间"`<br>`f"欢迎(提督\|舰长\|总督) <%{昵称}%> 进入直播间"`<br>`f"欢迎<%{昵称}%>进入直播间"`**无空格**<br>`f"欢迎 <^icon^> 舰长 <%{昵称}%> 进入直播间"`<br> |限长6字符，省略号为`…`
| icon_list					| []num	| |
| max_delay_time			| num	| 7 |
| trigger_time				| num	| TimeStamp(皮秒?) |
| identities				| num	| [identities](#others) |
| effect_silent_time		| float	| 0 |
| effective_time_new		| num	| |
| web_dynamic_url_webp		| str	| |
| web_dynamic_url_apng		| str	| |
| mobile_dynamic_url_webp	| str	| |
| new_style					| num	| |
| wealthy_info				| null/obj	| |
```json
{"cmd":"ENTRY_EFFECT","data":{"id":1,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":1,"copy_writing":"欢迎总督 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#423511","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","show_avatar":1,"effective_time":5,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","web_effective_time":5,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎总督 <%XXX%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":8,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":2,"copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 提督 <%XXX%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":2,"copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 提督 <%XXX%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":2,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":2,"copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_effective_time":3,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎提督 <%XXX%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":7,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":3,"copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":3,"copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":3,"copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":3,"copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_effective_time":2,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎舰长 <%XXX%> 进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[],"id":4,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":1069108539,"trigger_time":1676995200000000000,"uid":12345,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"322315039021057","send_time":1689168647149}

{"cmd":"ENTRY_EFFECT","data":{"id":135,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎 <%XXX%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","show_avatar":1,"effective_time":1,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","icon_list":[1],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":136,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎 <%XXX%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":136,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎 <%XXX%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":33,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":137,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎 <%XXX%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","icon_list":[2],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":137,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎 <%XXX%> 进入直播间","copy_color":"#000000","highlight_color":"#FFF100","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","show_avatar":1,"effective_time":2,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_effective_time":2,"web_effect_close":0,"web_close_time":900,"business":3,"copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","icon_list":[3],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":22,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}

{"cmd":"ENTRY_EFFECT","data":{"id":253,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎<%XXX%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_effective_time":3,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%XXX%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":1,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":253,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎<%XXX%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_effective_time":3,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%XXX%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":0,"web_dynamic_url_webp":"","web_dynamic_url_apng":"","mobile_dynamic_url_webp":""}}
{"cmd":"ENTRY_EFFECT","data":{"id":254,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎<%XXX%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","show_avatar":1,"effective_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%XXX%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":1,"effect_silent_time":0,"effective_time_new":3,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp"}}
{"cmd":"ENTRY_EFFECT","data":{"id":255,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎<%XXX%>进入直播间","copy_color":"#ffffff","highlight_color":"#ffea18","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","show_avatar":1,"effective_time":5,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":4,"copy_writing_v2":"欢迎<%XXX%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":6,"effect_silent_time":0,"effective_time_new":5,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp"}}

{"cmd":"ENTRY_EFFECT","data":{"id":333,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"欢迎<%XXX%>进入直播间","copy_color":"#ffffff","highlight_color":"#fff596","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/00a132d170d94ad80509c8078f9714e27a852ece.png","show_avatar":1,"effective_time":4,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/00a132d170d94ad80509c8078f9714e27a852ece.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":2,"copy_writing_v2":"欢迎<%XXX%>进入直播间","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":8,"effect_silent_time":0,"effective_time_new":4,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/16e46ab8edc770ff673fa0703e9fba068db8ef18.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/fea83bbabefde666608596fcfe7f12e865ddbb3e.vnd.mozilla.apng","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/16e46ab8edc770ff673fa0703e9fba068db8ef18.webp"}}

{"cmd":"ENTRY_EFFECT","data":{"id":368,"uid":12345,"target_id":12345,"mock_effect":0,"face":"$avatar_url","privilege_type":0,"copy_writing":"守护圣法师<%XXX%>进场","copy_color":"#7f3d22","highlight_color":"#e2553c","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/458fc181c69a4ade6f2f799df5fb0ffbb439bdd7.png","show_avatar":1,"effective_time":4,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/458fc181c69a4ade6f2f799df5fb0ffbb439bdd7.png","web_effective_time":0,"web_effect_close":1,"web_close_time":900,"business":5,"copy_writing_v2":"守护圣法师<%XXX%>进场","icon_list":[],"max_delay_time":7,"trigger_time":1676995200000000000,"identities":1,"effect_silent_time":0,"effective_time_new":4,"web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/ea7c2ad133492076575fbc40add59e6b400a7f33.webp","web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/458fc181c69a4ade6f2f799df5fb0ffbb439bdd7.png","mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/ea7c2ad133492076575fbc40add59e6b400a7f33.webp"}}

{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"https://i2.hdslb.com/bfs/face/xxx.jpg","highlight_color":"#FFFFFF","icon_list":[],"id":381,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":113700,"dm_icon_key":"","level":20,"level_total_score":200000,"status":1,"uid":xxx,"upgrade_need_score":86300},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"738070959763456","send_time":1689961638636}

{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[2],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[3],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[],"id":4,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":253,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":135,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT_MUST_RECEIVE","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎总督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 总督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#423511","icon_list":[2],"id":1,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":5},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎总督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 总督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#423511","icon_list":[3],"id":1,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":5},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎总督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎总督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#423511","icon_list":[],"id":1,"identities":8,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/075e4daa4fbf4f4699ff4855ffc9d1546a513540.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":5},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[1],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[1],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":70,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[2],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[3],"id":4,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎舰长 <%XXX%> 进入直播间","copy_writing_v2":"欢迎舰长 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#E6FF00","icon_list":[],"id":4,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/11a6e8eb061c3e715d0a6a2ac0ddea2faa15c15e.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/1de3dd51c0d8a87ec53f10a3ada310bf0387c473.png","business":5,"copy_color":"#6B0F08","copy_writing":"鲜花守护使<%XXX%>进场","copy_writing_v2":"鲜花守护使<%XXX%>进场","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#0053C3","icon_list":[],"id":374,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/1de3dd51c0d8a87ec53f10a3ada310bf0387c473.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/1de3dd51c0d8a87ec53f10a3ada310bf0387c473.png","business":5,"copy_color":"#6B0F08","copy_writing":"鲜花守护使<%XXX%>进场","copy_writing_v2":"鲜花守护使<%XXX%>进场","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#0053C3","icon_list":[1],"id":374,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/1de3dd51c0d8a87ec53f10a3ada310bf0387c473.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":380,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":380,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":380,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":380,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/2541c9d972f1108c1164e74ed3826891608f3e2a.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/446359be88d35ad69a848614430b02e49f1b1b6a.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":4,"face":"$avatar_url","highlight_color":"#92ffff","icon_list":[],"id":404,"identities":7,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/e0184c057c30f1104a4c53fabeab1f497e50d904.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/446359be88d35ad69a848614430b02e49f1b1b6a.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/93635528c8f4380c9c88141b3e1ddd43660acb19.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/e0184c057c30f1104a4c53fabeab1f497e50d904.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":7,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":254,"identities":8,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":254,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":3,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":254,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4a0990210623ac86c16c87532c6b2352503bbcc7.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/eac404ec584e3b672cc087d86b32700105171c4f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4d9135de524a9060a5b8fd1920ca1c6b51f60708.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#92ffff","icon_list":[],"id":375,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/4d9135de524a9060a5b8fd1920ca1c6b51f60708.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":384,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_5.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/6c286ba91c61802d766ad63942e76b4a8c54096d.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":384,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_5.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/6c286ba91c61802d766ad63942e76b4a8c54096d.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":384,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_5.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/52808380c75208e2bc362e597b35b8876b0c9650.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/6c286ba91c61802d766ad63942e76b4a8c54096d.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/0fc7ac7c095f0f4eb3e744590ab17f17922f3eed.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":386,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_7.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/b3b77b7bf24ac71a3e0e17588266fdeb13480930.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":386,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_7.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/b3b77b7bf24ac71a3e0e17588266fdeb13480930.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":386,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_7.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/b3b77b7bf24ac71a3e0e17588266fdeb13480930.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":386,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_7.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5374ef61e07906d2a53074c3cfc4c5cb2357ffed.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/b3b77b7bf24ac71a3e0e17588266fdeb13480930.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/6b63775bed7bbf52eb528ffa073f754cfc79fabc.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":255,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":255,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":1,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":255,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":255,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":255,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":255,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":255,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/5eda562b3c8c59b3414387d49b5668fd98df9d77.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/7ae7aa505237648db33e5f4ebf27807aabc79978.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b71f787399be04feccf4cfdbc81d30ef2e9efcf3.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":253,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":253,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":253,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[],"id":253,"identities":7,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[1],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[2],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":253,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","business":4,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#ffea18","icon_list":[3],"id":253,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/6d38ab463be28a130870c8c43d109473f215963e.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 提督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":2,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 提督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":2,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> 提督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":2,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","business":1,"copy_color":"#ffffff","copy_writing":"欢迎提督 <%XXX%> 进入直播间","copy_writing_v2":"欢迎提督 <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":3,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[],"id":2,"identities":7,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/74a41c65e422116d230d433042881fa5556f7870.png","web_close_time":0,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":3},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[],"id":372,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/2b1ed734175335ef70349d2000ec0eb476fe4a13.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":372,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/2b1ed734175335ef70349d2000ec0eb476fe4a13.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[2],"id":372,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8152c7a468052534ebdc27c2212e1ee421ce5c69.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/2b1ed734175335ef70349d2000ec0eb476fe4a13.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/04b08779ad1ca5cb54ffe44e69c7d9ecd2841ce2.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8262cb75e80a3aa165132b560c1dbd5e6d25760e.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":5,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":385,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/e8143424addd051e5d0a8a00cccce484fc9fd6ca.webp","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_6.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8262cb75e80a3aa165132b560c1dbd5e6d25760e.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/dc6464888022776c02fe6af467d294261c0bf990.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/e8143424addd051e5d0a8a00cccce484fc9fd6ca.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":382,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":382,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":382,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":382,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":382,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":382,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/8be39f9452aac3c078c0d52e249e0916c0ce9bbf.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[],"id":371,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[],"id":371,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":371,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":371,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":371,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":371,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[2],"id":371,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[2],"id":371,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[2],"id":371,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":5,"effective_time_new":4.4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[3],"id":371,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aa01b123db34ec16fd93fe4ba8d330950c00044d.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/4d6358f23612bc98f4e8fc248cc8490fdcdb9599.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/cd5c26f9fac63be48e47662d723c932727db627f.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":381,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":381,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":381,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":381,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":381,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":381,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":381,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":381,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/aee950e6aacddd0b125506f0a47d7fc1695d3ece.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":6,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#fff14b","icon_list":[],"id":232,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":6},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":6,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#fff14b","icon_list":[1],"id":232,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":6},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":6,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#fff14b","icon_list":[1],"id":232,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":6},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":6,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#fff14b","icon_list":[2],"id":232,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/ba319db46b0497c307648bd29702f323c3b19581.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":6},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/c453b9e6d1b87fa65626dea657aed80bffc9e798.png","business":5,"copy_color":"#2A3A5D","copy_writing":"星光守护灵<%XXX%>进场","copy_writing_v2":"星光守护灵<%XXX%>进场","effect_silent_time":0,"effective_time":4,"effective_time_new":4,"face":"$avatar_url","highlight_color":"#FF902D","icon_list":[],"id":378,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/dd6535caad5dc4a041bfa1eb0a855b78a3f11ab1.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/c453b9e6d1b87fa65626dea657aed80bffc9e798.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/18a810b647315a813730ea8d3af6325f25c8fe58.png","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/dd6535caad5dc4a041bfa1eb0a855b78a3f11ab1.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/cb7110026384fe0b8b849bba40502f1d2bce7b74.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[],"id":403,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b525da11b03d4a02409fedec2509d79f737077bb.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/cb7110026384fe0b8b849bba40502f1d2bce7b74.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/e0d170dd21c8f1364e69134b7fcc143d6ec12975.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b525da11b03d4a02409fedec2509d79f737077bb.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/cb7110026384fe0b8b849bba40502f1d2bce7b74.png","business":2,"copy_color":"#ffffff","copy_writing":"欢迎<%XXX%>进入直播间","copy_writing_v2":"欢迎<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":4,"face":"$avatar_url","highlight_color":"#fff596","icon_list":[1],"id":403,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b525da11b03d4a02409fedec2509d79f737077bb.webp","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/cb7110026384fe0b8b849bba40502f1d2bce7b74.png","web_close_time":900,"web_dynamic_url_apng":"https://i0.hdslb.com/bfs/live/mlive/e0d170dd21c8f1364e69134b7fcc143d6ec12975.vnd.mozilla.apng","web_dynamic_url_webp":"https://i0.hdslb.com/bfs/live/mlive/b525da11b03d4a02409fedec2509d79f737077bb.webp","web_effect_close":1,"web_effective_time":0},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":136,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":136,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":136,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/d4708dee21646e6ebcc58e7f6fa2a972c1d25b36.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":135,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":135,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":135,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[1],"id":135,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":1,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":135,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/da6933ea70f31c4df63f4b68b735891284888357.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":383,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":383,"identities":6,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[],"id":383,"identities":7,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":2,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":383,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[1],"id":383,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":383,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[2],"id":383,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":383,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":0,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":383,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":2,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","business":6,"copy_color":"#F7F7F7","copy_writing":"<%XXX%>进入直播间","copy_writing_v2":"<%XXX%>进入直播间","effect_silent_time":0,"effective_time":4,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFFFFF","icon_list":[3],"id":383,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":1,"priority":1,"privilege_type":3,"show_avatar":0,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":{"cur_score":xxx,"dm_icon_key":"ChronosWealth_4.png","level":xxx,"level_total_score":xxx,"status":1,"uid":xxx,"upgrade_need_score":xxx},"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/e2d85de0b44c9201c1cbd0ba4a7c762c58d3472f.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":1,"web_effective_time":4},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[],"id":137,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[],"id":137,"identities":1,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[2],"id":137,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":22,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":73,"privilege_type":0,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":2,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ENTRY_EFFECT","data":{"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","business":3,"copy_color":"#000000","copy_writing":"欢迎 <%XXX%> 进入直播间","copy_writing_v2":"欢迎 <^icon^> <%XXX%> 进入直播间","effect_silent_time":0,"effective_time":2,"effective_time_new":0,"face":"$avatar_url","highlight_color":"#FFF100","icon_list":[3],"id":137,"identities":33,"max_delay_time":7,"mobile_dynamic_url_webp":"","mock_effect":0,"new_style":0,"priority":1,"privilege_type":3,"show_avatar":1,"target_id":xxx,"trigger_time":xxx,"uid":xxx,"wealthy_info":null,"web_basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f7017a13c62c13369b85cb7a9f89981e79a3d2f9.png","web_close_time":900,"web_dynamic_url_apng":"","web_dynamic_url_webp":"","web_effect_close":0,"web_effective_time":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### STOP_LIVE_ROOM_LIST
[TOP](#直播弹幕)  
每30秒发送一次~~(`HH:mm:29`,`HH:mm:59`)~~  
广播 未压缩
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "STOP_LIVE_ROOM_LIST" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type	| value	|
|-|-|-|
| room_id_list	| []num	| |
```json
{"cmd":"STOP_LIVE_ROOM_LIST","data":{"room_id_list":[1,2,3,4,5,6,7,8,9,....]},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### GUARD_BUY
[TOP](#直播弹幕)  
舰长购买  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GUARD_BUY" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### GUARD_BUY__data
| key 9			| type	| value	|
|-|-|-|
| uid			| num	| uid |
| username		| str	| 昵称 |
| guard_level	| num	| [guard_level](#others) |
| num			| num	| 购买数量 |
| price			| num	| 舰长:198000 提督:1998000 总督:19998000 |
| gift_id		| num	| 10003:"舰长" 10002:"提督" 10001:"总督" |
| gift_name		| str	| |
| start_time	| num	| 购买时间 TimeStamp(秒) |
| end_time		| num	| 购买时间 TimeStamp(秒) |
```json
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":3,"num":1,"price":198000,  "gift_id":10003,"gift_name":"舰长","start_time":1672502400,"end_time":1672502400}}
{"cmd":"GUARD_BUY","data":{"uid":12334,"username":"xxx","guard_level":2,"num":1,"price":1998000, "gift_id":10002,"gift_name":"提督","start_time":1672502400,"end_time":1672502400}}
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":1,"num":1,"price":19998000,"gift_id":10001,"gift_name":"总督","start_time":1672502400,"end_time":1672502400}}
{"cmd":"GUARD_BUY","data":{"end_time":1672502400,"gift_id":10003,"gift_name":"舰长","guard_level":3,"num":1,"price":198000,  "start_time":1672502400,"uid":12345,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GUARD_BUY","data":{"end_time":1672502400,"gift_id":10002,"gift_name":"提督","guard_level":2,"num":1,"price":1998000, "start_time":1672502400,"uid":12345,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### USER_TOAST_MSG
[TOP](#直播弹幕)  
舰长购买通知，显示在聊天区
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### USER_TOAST_MSG__data
| key 23				| type	| value	|
|-|-|-|
| anchor_show			| bool	| true |
| color					| str	| 舰长:"#00D1F1" <br> 提督:"#E17AFF" <br> 总督:"#FF7C28" |
| dmscore				| num	| 舰长:90	<br> 提督:96	<br> 总督:102 |
| effect_id				| num	| 舰长:397	<br> 提督:398	<br> 总督:399 |
| end_time				| num	| TimeStamp(秒) |
| face_effect_id		| num	| 舰长:44 <br> 提督:43 <br> 总督:42 |
| gift_id				| num	| 舰长:10003<br> 提督:10002 <br> 总督:10001 |
| guard_level			| num	| [guard_level](#others) |
| is_show				| num	| 0 |
| num					| num	| 1? |
| op_type				| num	| 1: <br> 2: <br> 3: <br> 4: |
| payflow_id			| str	| 订单号(25) |
| price					| num	| RMB×1000 <br> 舰长138 158 198 <br> 提督1598 1998 <br> 总督15998 19998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| 舰长:590 <br> 提督:591 <br> 总督:592 |
| start_time			| num	| 购买时间 TimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播当前舰长数 |
| toast_msg				| str	|`f"<%{昵称}%> 在主播YYY的直播间(开通\|续费)了(舰长\|提督\|总督)，今天是TA陪伴主播的第×××天"` |
| uid					| num	| uid |
| unit					| str	| "月"? |
| user_show				| bool	| true |
| username				| str	| 昵称 |
```json
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":198000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":158000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":158000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":158000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":158000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":198000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":96, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":96, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":158000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":198000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1672502400,"face_effect_id":44,"gift_id":10003,"guard_level":3,"is_show":0,"num":1,"op_type":3,"payflow_id":"230101000000xxxxxxxxxxxxx","price":138000,  "role_name":"舰长","room_effect_id":590,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 开通了舰长，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}

{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":102,"effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1598000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1598000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1598000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":3,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":5194000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了3个月提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1998000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 开通了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1672502400,"face_effect_id":43,"gift_id":10002,"guard_level":2,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":1598000, "role_name":"提督","room_effect_id":591,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 续费了提督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}

{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":19998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":15998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"xxx"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":15998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":19998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":15998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
```
----
### NOTICE_MSG
[TOP](#直播弹幕)  
滚动横幅 **广播**
| key 17※ 18	| type	| value	|
|-|-|-|
| business_id	| str	| xxxx |
| cmd			| str	| "NOTICE_MSG" |
| id			| num	| |
| name			| num	| |
| full			| obj	| |
| half			| obj	| |
| side			| obj	| |
| roomid		| num	| 直播间ID |
| real_roomid	| num	| 长直播间ID |
| msg_common	| str	| |
| msg_self		| str	| |
| link_url		| str	| `f""` |
| msg_type		| num	| |
| shield_uid	| num	| |
| business_id	| str	| |
| scatter		| obj	| |
| marquee_id	| str	| "" |
| notice_type	| num	| 0 |
#### NOTICE_MSG__full
| key			| type	| value	|
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
| key			| type	| value	|
|-|-|-|
| head_icon		| str	| |
| tail_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| time			| num	| |
#### NOTICE_MSG__side
| key			| type	| value	|
|-|-|-|
| head_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| border		| str	| |
#### NOTICE_MSG__scatter
| key	| type	| value	|
|-|-|-|
| min	| num	| 0 |
| max	| num	| 0 |
----
### SUPER_CHAT_MESSAGE
[TOP](#直播弹幕)  
SuperChat
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 长_短直播间ID |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SUPER_CHAT_MESSAGE__data
| key 27					| type		| value	|
|-|-|-|
| background_bottom_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color			| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_end		| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_color_start	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| background_icon			| str	| URL |
| background_image			| str	| URL |
| background_price_color	| str	| [table](#SUPER_CHAT_MESSAGE__PriceTable) |
| color_point				| float	| 0.7 |
| dmscore					| num	| 8×N [16,24,48,56,64,72,80,112,120,128] |
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
| key						| type		| value	|
|-|-|-|
| gift_id					| num		| 12000 |
| gift_name					| str		| "醒目留言" |
| num						| num		| 1 |
#### SUPER_CHAT_MESSAGE__data__user_info
| key 12					| type		| value	|
|-|-|-|
| face						| str		| 头像(URL) |
| face_frame				| str		| 头像框(URL) |
| guard_level				| num		| [guard_level](#others) |
| is_main_vip				| num		| |
| is_svip					| num		| ?0 |
| is_vip					| num		| ?0 |
| level_color				| str		| |
| manager					| num		| 管理员？ |
| name_color				| str		| |
| title						| str		| [头衔](docs/头衔.md) |
| uname						| str		| 昵称 |
| user_level				| num		| 直播观众等级 |
#### SUPER_CHAT_MESSAGE__PriceTable
| price	| background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	| background_price_color	|
|-|-|-|-|-|-|-|-|
| 30-49.9		| #2A60B2	| #EDF5FF	| #405D85	| #3171D2	| #7497CD	| #A3F6FF	|
| 50-99.9		| #427D9E	| #DBFFFD	| #29718B	| #4EA4C5	| #7DA4BD	| #A3F6FF	|
| 100-499.9		| #E2B52B	| #FFF1C5	| #EEBE5C	| #EAB400	| #ECCF75	| #72110E	|
| 500-999.9		| #000000	| #000000	| #000000	| #000000	| #000000	| #000000	|
| 1000-1999.9	| #E54D4D	| #FFE7E4	| #BD666A	| #F63C45	| #EE8B8B	| #FFE163	|
| 2000+			| #000000	| #000000	| #000000	| #000000	| #000000	| #000000	|
```json
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#427D9E","background_color":"#DBFFFD","background_color_end":"#29718B","background_color_start":"#4EA4C5","background_icon":"","background_image":"https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_price_color":"#7DA4BD","color_point":0.7,"dmscore":128,"end_time":1672502400,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"id":12345,"is_ranked":1,"is_send_audit":0,"medal_info":null,"message":"123","message_font_color":"#A3F6FF","message_trans":"","price":50,"rate":1000,"start_time":1672502400,"time":120,"token":"50316B2E","trans_mark":0,"ts":1672502400,"uid":12345,"user_info":{"face":"$avatar_url","face_frame":"https://i0.hdslb.com/bfs/live/09937c3beb0608e267a50ac3c7125c3f2d709098.png","guard_level":2,"is_main_vip":1,"is_svip":0,"is_vip":0,"level_color":"#a068f1","manager":0,"name_color":"#E17AFF","title":"title-634-1","uname":"abc","user_level":32}},"roomid":12345}
"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":"#61c05a","medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":1,"medal_name":"粉丝勋章","special":"","target_id":0}
```
----
### SUPER_CHAT_MESSAGE_JPN
[TOP](#直播弹幕)  
SuperChat 日本語  
？某些主播的直播间会一直发送此包  
在`SUPER_CHAT_MESSAGE`后约`1100ms/1.1s`内发送  
由`百度翻译`提供翻译 / Translated by `Baidu Translate`
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE_JPN" |
| data		| obj	| |
| roomid	| str	| str(长_短直播间ID) |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SUPER_CHAT_MESSAGE_JPN__data
| key 20					| type	| value	|
|-|-|-|
| id						| str	| SC id |
| uid						| str	| uid |
| price						| num	| SC价格 |
| rate						| num	| 1000 |
| message					| str	| 原始SC内容 |
| message_jpn				| str	| 翻译后SC内容 |
| is_ranked					| num	| 0,1 |
| background_image			| str	| |
| background_color			| str	| |
| background_icon			| str	| |
| background_price_color	| str	| |
| background_bottom_color	| str	| |
| ts						| num	| TimeStamp(秒) |
| token						| str	| hex(64bit) |
| medal_info				| obj	| [medal_info](#粉丝牌信息medal_info) 没有(`guard_level`, `is_lighted`, `medal_color_border`, `medal_color_end`, `medal_color_start`) |
| user_info					| obj	| |
| time						| num	| |
| start_time				| num	| TimeStamp(秒) |
| end_time					| num	| TimeStamp(秒) |
| gift						| obj	| |
```json
{"cmd":"SUPER_CHAT_MESSAGE_JPN","data":{"id":"12345","uid":"23456","price":50,"rate":1000,"message":"123","message_jpn":"123","is_ranked":1,"background_image":"https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_color":"#DBFFFD","background_icon":"","background_price_color":"#7DA4BD","background_bottom_color":"#427D9E","ts":1672502400,"token":"50316B2E","medal_info":null,"user_info":{"uname":"abc","face":"$avatar_url","face_frame":"https://i0.hdslb.com/bfs/live/09937c3beb0608e267a50ac3c7125c3f2d709098.png","guard_level":2,"user_level":32,"level_color":"#a068f1","is_vip":0,"is_svip":0,"is_main_vip":1,"title":"title-634-1","manager":0},"time":120,"start_time":1672502400,"end_time":1672502400,"gift":{"num":1,"gift_id":12000,"gift_name":"醒目留言"}},"roomid":"12345"}
```
----
### SUPER_CHAT_MESSAGE_DELETE
[TOP](#直播弹幕)  
SC 删除
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE_DELETE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SUPER_CHAT_MESSAGE_DELETE__data
| key		| type	| value	|
|-|-|-|
| ids		| []num	| SC_id |
| roomid	| num	| 长_短直播间ID |
```json
{"cmd":"SUPER_CHAT_MESSAGE_DELETE","data":{"ids":[123]},"roomid":12345}
{"cmd":"SUPER_CHAT_MESSAGE_DELETE","data":{"ids":[123]},"is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
```
----
### DANMU_AGGREGATION
[TOP](#直播弹幕)  
抽奖通知 每秒最多更新一次 每个抽奖最多发送`max_time-1`个包
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "DANMU_AGGREGATION" |
| data	| obj	| |
#### DANMU_AGGREGATION__data
| key 11				| type	| value	|
|-|-|-|
| activity_identity		| str	| 抽奖id |
| activity_source		| num	| 1:天选时刻 2:礼物红包 |
| aggregation_cycle		| num	| 1 |
| aggregation_icon		| str	| |
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| dmscore				| num	| 144 |
| msg					| str	| 抽奖口令 |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间TimeStamp(秒) |
```json
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":1,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png","aggregation_num":111,"broadcast_msg_type":0,"dmscore":144,"msg":"xxxxx","show_rows":1,"show_time":2,"timestamp":1672502400000}}
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":2,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png","aggregation_num":111,"broadcast_msg_type":0,"dmscore":144,"msg":"老板大气！点点红包抽礼物","show_rows":1,"show_time":2,"timestamp":1672502400},"is_report":false,"msg_id":"xxx","send_time":xxx}
["老板大气！点点红包抽礼物","点点红包，关注主播抽礼物～","喜欢主播加关注，点点红包抽礼物","红包抽礼物，开启今日好运！","中奖喷雾！中奖喷雾！"]

{"aggregation_icon":{"天选时刻":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png", "礼物红包":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png"}}
```
----
### SPECIAL_GIFT
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "SPECIAL_GIFT" |
| data	| obj	| |
#### SPECIAL_GIFT__data
| key	| type	| value	|
|-|-|-|
| 39	| obj	| |
#### SPECIAL_GIFT__data__39
| key 2,7	| type	| value	|
|-|-|-|
| action	| str	| (start|end) |
| content	| str	| |
| hadJoin	| num	| 0 |
| id		| str,num	| start:str end:num |
| num		| num	| 1 |
| storm_gif	| str	| GIF图像 |
| time		| num	| 持续时间 |
```json
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"可爱即正义~~","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"end","id":123412341234}}}
```
----
### GUARD_HONOR_THOUSAND
[TOP](#直播弹幕)  
**广播**
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GUARD_HONOR_THOUSAND" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type	| value	|
|-|-|-|
| add	| []num	| 用户uid |
| del	| []num	| 用户uid |
```json
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[],"del":[xxx]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[xxx],"del":[]},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### ANCHOR_LOT_CHECKSTATUS
[TOP](#直播弹幕)  
抽奖(天选时刻)检查
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_CHECKSTATUS" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_LOT_CHECKSTATUS__data
| key 3,5			| type	| value	|
|-|-|-|
| id				| num	| 抽奖id |
| ?reject_danmu		| null	| ?null |
| ?reject_reason	| str	| 拒绝理由 |
| status			| num	| 4:通过 5:拒绝 |
| uid				| num	| 主播uid |
```json
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"由于奖品格式不合格,请仔细检查后再提交哦","status":5,"uid":12345}}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"","status":4,"uid":12345}}

{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"","status":4,"uid":12345},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"status":4,"uid":12345},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ANCHOR_LOT_START
[TOP](#直播弹幕)  
抽奖(天选时刻)开始
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_START" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_LOT_START__data
| key 33			| type		| value	|
|-|-|-|
| asset_icon		| str		| https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png |
| asset_icon_webp	| str		| https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp |
| award_image		| str		| |
| award_name		| str		| 礼物名称 |
| award_num			| num		| 礼物数量[1,100] |
| award_type		| num		| 0 1 |
| award_price_text	| str		| "价值xxx电池" |
| cur_gift_num		| num		| 0 |
| current_time		| num		| 当前时间TimeStamp(秒) |
| danmu				| str		| 弹幕口令[0,15] |
| danmu_new			| [1]obj	| |
| danmu_type		| num		| `danmu_type:0 === this.danmuType ? "文案弹幕" :"表情弹幕"` |
| gift_id			| num		| 0 |
| gift_name			| str		| ~~礼物抽奖：抽奖条件~~ |
| gift_num			| num		| 礼物抽奖：数量 |
| gift_price		| num		| 礼物抽奖：礼物价格(RMB×1000) |
| goaway_time		| num		| 180? |
| goods_id			| num		| |
| id				| num		| 抽奖id |
| is_broadcast		| num		| 1 |
| join_type			| num		| ？ |
| lot_status		| num		| [lot_status](#others) [0,1,2] |
| max_time			| num		| 开奖时间(60,300,600,900)秒 |
| require_text		| str		| "抽奖条件: 关注主播""至少成为主播的舰长/提督/总督" |
| require_type		| num		| 抽奖条件 1:礼物抽奖 2:粉丝勋章 3:大航海 ~~4:UL?~~ |
| require_value		| num		| [0,1]关注状态/[1,20]粉丝牌等级/[1,3]舰长等级 |
| room_id			| num		| 长_短直播间ID |
| send_gift_ensure	| num		| 0 |
| show_panel		| num		| 1 |
| start_dont_popup	| num		| 0 |
| status			| num		| 1 |
| time				| num		| 剩余时间(秒) |
| url				| str		| https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1 |
| web_url			| str		| https://live.bilibili.com/p/html/live-lottery/anchor-join.html |
#### ANCHOR_LOT_START__data__danmu_new
| key 3			| type	| value	|
|-|-|-|
| danmu			| str	| 弹幕口令[0,15] |
| danmu_view	| str	| |
| reject		| bool	| |
```json
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"当前主播粉丝勋章至少1级","require_type":2,"require_value":1,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"关注主播 +XXXX","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"至少成为主播的舰长","require_type":3,"require_value":3,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}


{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"情书","award_num":1,"award_price_text":"价值52电池","award_type":1,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":0,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"当前主播粉丝勋章至少1级","require_type":2,"require_value":1,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"情书","award_num":1,"award_price_text":"价值52电池","award_type":1,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":0,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"关注主播","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"情书","award_num":1,"award_price_text":"价值52电池","award_type":1,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":0,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"无","require_type":0,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}

{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"当前主播粉丝勋章至少1级","require_type":2,"require_value":1,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"关注主播 +XXXX","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"XXX","send_time":xxx}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":123,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":9999,"require_text":"关注主播","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"GIFT","award_num":1,"award_type":0,"cur_gift_num":0,"current_time":1672502400,"danmu":"Text","danmu_new":[{"danmu":"Text","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":31164,"gift_name":"粉丝团灯牌","gift_num":1,"gift_price":1000,"goaway_time":180,"goods_id":15,"id":123,"is_broadcast":1,"join_type":1,"lot_status":0,"max_time":9999,"require_text":"关注主播","require_type":1,"require_value":0,"room_id":12345,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":9999,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ANCHOR_LOT_END
[TOP](#直播弹幕)  
抽奖(天选时刻)结束
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_END" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_LOT_END__data
| key	| type	| value	|
|-|-|-|
| id	| num	| 抽奖id |
```json
{"cmd":"ANCHOR_LOT_END","data":{"id":12345}}
{"cmd":"ANCHOR_LOT_END","data":{"id":12345},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### ANCHOR_LOT_AWARD
[TOP](#直播弹幕)  
抽奖(天选时刻) 中奖名单，在`ANCHOR_LOT_END`后约`1~180ms`
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_AWARD" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_LOT_AWARD__data
| key 10			| type	| value	|
|-|-|-|
| award_dont_popup	| num	| 1 |
| award_image		| str	| 奖品图像？ |
| award_name		| str	| 奖品名称 |
| award_num			| num	| 1 |
| award_type		| num	| 0 1 |
| award_users		| []obj	| 中奖用户 |
| id				| num	| 抽奖id |
| *ruid*			| num	| uid |
| lot_status		| num	| [lot_status](#others) 2 |
| url				| str	| ...... |
| web_url			| str	| "https://live.bilibili.com/p/html/live-lottery/anchor-join.html" |
#### ANCHOR_LOT_AWARD__data__award_users
| key 6	| type	| value	|
|-|-|-|
| uid	| num	| uid |
| uname	| num	| 昵称 |
| face	| num	| 头像URL |
| level	| num	| 直播观众等级 UL |
| color	| num	| 直播观众等级_颜色 num(RGB24) |
| num	| num	| 数量 |
```json
{
	"cmd": "ANCHOR_LOT_AWARD",
	"data": {
		"award_dont_popup":1,
		"award_image":"",
		"award_name":"GIFT",
		"award_num":1,
		"award_type":0,
		"award_users": [
			{"uid":1,"uname":"A","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":2,"uname":"B","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":3,"uname":"C","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":4,"uname":"D","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":5,"uname":"E","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":6,"uname":"F","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":7,"uname":"G","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":8,"uname":"H","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":9,"uname":"I","face":"$avatar_url","level":x,"color":x,"num":1},
			{"uid":0,"uname":"J","face":"$avatar_url","level":x,"color":x,"num":1}
		],
		"id": 12345,
		"lot_status":2,
		"url": "https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url": "https://live.bilibili.com/p/html/live-lottery/anchor-join.html"
	}
}
////////////////
{
	"cmd":"ANCHOR_LOT_AWARD",
	"data":{
		"award_dont_popup":1,
		"award_image":"",
		"award_name":"情书",
		"award_num":1,
		"award_price_text":"价值52电池",
		"award_type":1,
		"award_users":[{"bag_id":x,"color":x,"face":"$avatar_url","gift_id":31250,"level":xxx,"num":1,"uid":xxx,"uname":"XXX"}],
		"id":12345,
		"lot_status":2,
		"ruid":xxx,
		"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},
	"is_report":false,"msg_id":"xxx","send_time":xxx
}

{
	"cmd":"ANCHOR_LOT_AWARD",
	"data":{
		"award_dont_popup":1,
		"award_image":"",
		"award_name":"GIFT",
		"award_num":1,
		"award_type":0,
		"award_users":[
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"},
			{"color":x,"face":"$avatar_url","level":xxx,"num":1,"uid":xxx,"uname":"XXX"}],
		"id":12345,
		"lot_status":2,
		"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"},
	"is_report":false,"msg_id":"xxx","send_time":xxx
}
```
----
### POPULAR_RANK_CHANGED
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULAR_RANK_CHANGED" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### POPULAR_RANK_CHANGED__data
| key		| type	| value	|
|-|-|-|
| uid		| num	| 主播uid |
| rank		| num	| [0-100] |
| countdown	| num	| [0,3600] |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| cache_key	| str	| `f"rank_change:{hex_256bit}"` |
```json
{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":12345,"rank":25,"countdown":275,"timestamp":1672502400,"cache_key":"rank_change:5566ddf515314299b0035ff169bbb4c6"}}
{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":12345,"rank":24,"countdown":176,"timestamp":1672502400,"cache_key":"rank_change:c73af03a143d47dcae79474b3b298f10"}}
{"cmd":"POPULAR_RANK_CHANGED","data":{"cache_key":"rank_change:e31e1d458d0140fe992ab88250af83aa","countdown":3491,"rank":93,"timestamp":1672502400,"uid":12345},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### PREPARING
[TOP](#直播弹幕)  
结束直播
| key 6		| type	| value	|
|-|-|-|
| cmd		| str	| "PREPARING" |
| round ※	| num	| 1 下播后轮播 |
| roomid	| str	| 长_短直播间ID |
| scatter ※	| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
```json
{"cmd":"PREPARING","roomid":"123"}
{"cmd":"PREPARING","round":1,"roomid":"12345"}
{"cmd":"PREPARING","is_report":false,"msg_id":"xxx","roomid":"12345","send_time":xxx}
{"cmd":"PREPARING","is_report":false,"msg_id":"xxx","roomid":"12345","round":1,"scatter":{"max":30,"min":10},"send_time":xxx}
{"cmd":"PREPARING","is_report":false,"msg_id":"xxx","roomid":"12345","round":1,"send_time":xxx}
```
----
### DANMU_MSG
[TOP](#直播弹幕)  
弹幕！
| key 6		| type	| value	|
|-|-|-|
| cmd		| str	| "DANMU_MSG" |
| info		| array	| |
| dm_v2		| str	| base64(proto) UTF-8 [define](#danmu_msg__dm_v2) |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### DANMU_MSG__info
| array	| type	| value	| 备注	|
|-|-|-|-|
| 0		| array	| [弹幕属性](#DANMU_MSG__info__0) |
| 1		| str	| `text/content` <br> 弹幕内容/表情包名称 |
| 2		| array	| `userInfo`用户主站信息 | "https://account.bilibili.com/account/home"
| 3		| array	| `fansMedal`[粉丝牌](#DANMU_MSG__info__3) | "https://link.bilibili.com/p/center/index#/user-center/wearing-center/my-medal"
| 4		| array	| `user_level`[用户直播区信息](#DANMU_MSG__info__4) | "https://link.bilibili.com/p/center/index#/user-center/my-info/operation"
| 5		| array	| `title` [头衔](docs/头衔.md) | https://link.bilibili.com/p/center/index#/user-center/wearing-center/library
| 6		| num	| ？0 |
| 7		| num	| `guardLevel`[舰长等级](#others) |
| 8		| null	| ？ |
| 9		| obj	| [`validation`](#DANMU_MSG__info__9) |
| 10	| num	| ?0 |
| 11	| num	| ?0 |
| 12	| null	| ？null |
| 13	| null	| ？null |
| 14	| num	| `lpl` |
| 15	| num	| 7×N |7 14 21 28 35 42 49 56 63 70 77 105 112 210:主播
| 16	| array	| `Wealth` |
#### DANMU_MSG__info__0
**弹幕属性**
| array	| type		| value	| 备注	|
|-|-|-|-|
| 0[0]	| num		| ？0 |
| 0[1]	| num		| `mode` 弹幕位置 | 0:普通 4:底部
| 0[2]	| num		| `size/fontsize` 弹幕字体大小 | 25
| 0[3]	| num		| `color` 弹幕颜色 |
| 0[4]	| num		| `ctime` | TimeStamp(毫秒)
| 0[5]	| num		| `dmid/rnd/danmakuRnd` <br> 抽奖/弹幕互动游戏 为 0 | WEB:进入直播间时间TimeStamp(秒) <br> iOS/Android:随机
| 0[6]	| num		| 0? |
| 0[7]	| str		| `midHash` | HEX:crc32(uid)
| 0[8]	| num		| ? |
| 0[9]	| num		| `type/danmakuType` ? [0,1,2,7,9] | 1:节奏风暴 2:天选时刻 9:弹幕互动游戏
| 0[10]	| num		| `chatBubbleType` | 1,2,5
| 0[11]	| str		| `chatBubbleColor` | 5:`"#1453BAFF,#4C2263A2,#3353BAFF"` <br> 2:`"#1453BAFF,#4C2263A2,#3353BAFF"` 1:`"#33FFE99E,#40DCA731,#33FFE99E"`
| 0[12]	| num		| `dm_type/dmType/danmakuSpecialType` | 0:文本 <br> 1:表情包 <br> 2:语音
| 0[13]	| obj/str	| 表情包：[`emoticonOptions`](#DANMU_MSG__info__0__13) <br> 其他:`"{}"` |
| 0[14]	| obj/str	| XXX:[`voiceConfig`/`voiceInfo`](#DANMU_MSG__info__0__14) <br> YYY:`"{}"` |
| 0[15]	| obj 		| [`emoticons/modeInfo`](#DANMU_MSG__info__0__15) |
| 0[16]	| obj 		| `Aggregation/danmakuAggre`[抽奖](#DANMU_MSG__info__0__16) |20230119
| 0[17]	| num 		| `chatBubbleId/idV2` |20230708+
#### DANMU_MSG__info__2
**用户主站信息/userInfo**
| array	| type	| value	| 备注	|
|-|-|-|-|
| 2[0]	| num	| `uid` 用户uid |
| 2[1]	| str	| `uname/username` 昵称 |
| 2[2]	| num	| `isAdmin` 房管 |
| 2[3]	| num	| `isVip` |
| 2[4]	| num	| `isSvip` |
| 2[5]	| num	| `rank` | ？10000 LV0:5000
| 2[6]	| num	| `verify` **bool** |https://s1.hdslb.com/bfs/blive-engineer/live-web-player/room-player.min.js
| 2[7]	| str	| `usernameColor` | 舰长:`"#00D1F1"` <br> 提督:`"#E17AFF"` <br> 总督:`"#FF7C28"`
#### DANMU_MSG__info__3
**粉丝牌/fansMedal**
| array	| type	| value	|
|-|-|-|
| 3[0]	| num	| `level` 粉丝牌 等级 |
| 3[1]	| str	| `label` 粉丝团 称号 |
| 3[2]	| num	| `anchorUsername` 主播昵称 |
| 3[3]	| num	| `shortRoomID/RoomID` 长_短直播间ID |
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
**用户直播区信息/userLevel/user_level**
| array	| type		| value	| 备注	|
|-|-|-|-|
| 4[0]	| num		| `userLevel` 用户UL等级 |
| 4[1]	| num		| ？0 |
| 4[2]	| num		| UL等级 颜色 |
| 4[3]	| str/num	| `rank` 直播 用户排名|">50000"
| 4[4]	| num		| `online_rank` [0,1,2,3] | 高能榜实时排名(仅前三)
#### DANMU_MSG__info__5
**头衔/title**
| array	| type	| value	|
|-|-|-|
| 5[0]	| str	| `old_title` |
| 5[1]	| str	| `title` |
#### DANMU_MSG__info__9
**validation**
| key	| type	| value	|
|-|-|-|
| ts	| num	| TimeStamp(秒) |
| ct	| str	| hex(64bit) |
#### DANMU_MSG__info__16
**Wealth**
| array	| type	| value	|
|-|-|-|
| 16[0]	| num	| level |
| 16[x]	| xxx	| uid |
| 16[x]	| xxx	| level_total_score |
| 16[x]	| xxx	| cur_score |
| 16[x]	| xxx	| upgrade_need_score |
| 16[x]	| xxx	| status |
| 16[x]	| xxx	| dm_icon_key |
#### DANMU_MSG__info__0__13
**表情包1**
| key				| type	| value	|
|-|-|-|
| bulge_display		| num	| 0,1 |
| emoticon_unique	| str	| 表情包id |
| height			| num	| 高 |
| in_player_area	| num	| 0,1 |
| is_dynamic		| num	| 0,1 |
| url				| str	| 表情包URL |
| width				| num	| 宽 |
#### DANMU_MSG__info__0__14
**voiceConfig**
| key				| type	| value	|
|-|-|-|
| file_duration		| num	| |
| file_format		| str	| |
| file_id			| str	| |
| text				| str	| |
| voice_url			| str	| |
#### DANMU_MSG__info__0__15
**表情包2**
| key 3				| type	| value	|
|-|-|-|
| mode				| num	| 0 |
| show_player_type	| num	| 0 |
| extra				| str	| [json](#DANMU_MSG__info__0_15__extra) |
#### DANMU_MSG__info__0__15__extra
| key 28					| type		| value	| 备注	|
|-|-|-|-|
| send_from_me				| bool		| false |
| mode						| num		| 0 |
| color						| num		| 弹幕颜色 |
| dm_type					| num		| 0:文本 1:表情包 |
| font_size					| num		| `25` 弹幕字体大小 |
| player_mode				| num		| 弹幕位置 | 0:？ 1:滚动 2:？ 4:底部
| show_player_type			| num		| 0 |
| content					| str		| 弹幕内容/表情包名称 |
| user_hash					| str		| `str(DEC:midHash)` |
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
| is_audited				| bool		| false | 20230217
| id_str					| str		| hex(132bit/144bit) 33-34 | 20230308
| icon						| obj/null	| url | 2023-06-30 10:58:2x
#### DANMU_MSG__info__0__15__extra__emots
| key 8				| type	| value	|
|-|-|-|
| emoticon_id		| num	| 表情ID |
| emoji 			| str	| |
| descript 			| str	| |
| url				| str	| |
| width				| num	| 宽 |
| height 			| num	| 高 |
| emoticon_unique	| str	| 表情ID |
| count 			| num	| 计数 |
#### DANMU_MSG__info__0__15__extra__icon
| key 2				| type	| value	|
|-|-|-|
| type				| num	| |
| resource			| str	| |
#### DANMU_MSG__info__0__16
**抽奖**
| key 3				| type	| value	|
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
#### DANMU_MSG__example
```json
{
	"cmd":"DANMU_MSG",
	"dm_v2":"CiJiMDdiNDVkNjI3YWM1MWVjNDY4ZjJkZTNhNWNlMWI2MzQ4EAEYGSD///8HKggxYzViNTRjYTIFW2RvZ1048fq0r5YxSJnZ1qUGYgByYwoFW2RvZ10SWgoJZW1vamlfMjA4EklodHRwOi8vaTAuaGRzbGIuY29tL2Jmcy9saXZlLzQ0MjhjODRlNjk0ZmJmNGUwZWY2YzA2ZTk1OGQ5MzUyYzM1ODI3NDAucG5nMBQ4FIoBAJoBDwoHNEIwREY4NBDB+9alBqIBfgjB4LoGEgdTSkg4MTMwIk5odHRwczovL2kwLmhkc2xiLmNvbS9iZnMvYmFzZWxhYnMvYmNkOWQwZjVhODhjYjlkMDRhYWQ3NmFiNGJkMDBlYjJjMTc1Yzg5MS5wbmc4kE5AAVoCCAFiDwgPENqAhwMaBj41MDAwMGoAcgB6AKoBBRix+Z0E",
	"info":[
		[0,1,25,16777215,1689632193905,1689627801,0,"1c5b54ca",0,0,0,"",0,"{}","{}",{"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":0,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"[dog]\",\"user_hash\":\"475747530\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":1,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":{\"[dog]\":{\"emoticon_id\":208,\"emoji\":\"[dog]\",\"descript\":\"[dog]\",\"url\":\"http://i0.hdslb.com/bfs/live/4428c84e694fbf4e0ef6c06e958d9352c3582740.png\",\"width\":20,\"height\":20,\"emoticon_unique\":\"emoji_208\",\"count\":1}},\"is_audited\":false,\"id_str\":\"b07b45d627ac51ec468f2de3a5ce1b6348\",\"icon\":null}","mode":0,"show_player_type":0},{"activity_identity":"","activity_source":0,"not_show":0},0],
		"[dog]",								// 1
		[13545537,"SJH8130",0,0,0,10000,1,""],	// 2
		[],										// 3
		[15,0,6406234,">50000",0],				// 4
		["",""],								// 5
		0,										// 6
		0,										// 7
		null,									// 8
		{"ct":"4B0DF84","ts":1689632193},		// 9
		0,										// 10
		0,										// 11
		null,									// 12
		null,									// 13
		0,										// 14
		210,									// 15
		[0]										// 16
	]
	,"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### CUT_OFF
[TOP](#直播弹幕)  
切断直播！
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CUT_OFF" |
| msg		| str	| |
| is_report	| bool	| |
| msg_id	| str	| |
| roomid	| num	| 直播间id |
| send_time	| num	| |
```json
{"cmd":"CUT_OFF","msg":"...","roomid":xxx}
{"cmd":"CUT_OFF","is_report":false,"msg":"...","msg_id":"xxx","roomid":xxx,"send_time":xxx}
"禁播游戏"
"版权相关"
"违反直播规范"
"直播中涉及低俗内容"
"未持有相关许可，不允许直播相关内容"
"分区错误，直播该游戏请移至虚拟APEX分区直播"
```
----
### SHOPPING_CART_SHOW
[TOP](#直播弹幕)  
？购物车  
开播后约30ms内发送`status=1`的包
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SHOPPING_CART_SHOW" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SHOPPING_CART_SHOW__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 开播:1 下播:2 |
```json
{"cmd":"SHOPPING_CART_SHOW","data":{"status":1},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"SHOPPING_CART_SHOW","data":{"status":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### WIDGET_BANNER
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "WIDGET_BANNER" |
| data	| obj	| |
#### WIDGET_BANNER__data
| key			| type	| value	|
|-|-|-|
| timestamp		| num	| 当前时间TimeStamp(秒) |
| widget_list	| obj	| "***ID***":{} |
#### WIDGET_BANNER__data__widget_list__ID
| key 15			| type	| value	|
|-|-|-|
| id				| num	| ***ID*** |
| title				| str	| |
| cover				| str	| "" |
| web_cover			| str	| "" |
| tip_text			| str	| |
| tip_text_color	| str	| |
| tip_bottom_color	| str	| |
| jump_url			| str	| |
| url				| str	| "" |
| stay_time			| num	| 5 |
| site				| num	| 1 |
| platform_in		| arr	| ["live","blink","live_link","web","pc_link"] |
| type				| str	| |
| band_id			| num	| |
| sub_key			| str	| |
| sub_data			| str	| urlencoded(json) |
| is_add			| bool	| true |
----
### GOTO_BUY_FLOW
[TOP](#直播弹幕)  
移动端 购买装扮
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GOTO_BUY_FLOW" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### GOTO_BUY_FLOW__data
| key	| type	| value	|
|-|-|-|
| text	| str	| |
```json
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等2人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等3人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等4人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等5人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等6人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等7人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等8人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等9人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等10人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等11人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等12人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等13人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等14人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等16人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等17人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等18人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等19人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等22人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等27人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等32人正在去买"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### RECOMMEND_CARD
[TOP](#直播弹幕)  
商品推销(移动端)  
3KB~16+KB  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "RECOMMEND_CARD" |
| data	| obj	| |
#### RECOMMEND_CARD__data
| key				| type	| value	|
|-|-|-|
| title_icon		| str	| https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png |
| recommend_list	| obj[]	| |
| timestamp			| num	| 当前时间TimeStamp(秒) |
#### RECOMMEND_CARD__data__recommend_list
| key					| type		| value	|
|-|-|-|
| recommend_card_extra	| null/?	| |
| shopping_card_detail	| obj		| |
#### RECOMMEND_CARD__data__recommend_list__shopping_card_detail
| key 32								| type	| value	|
|-|-|-|
| active_info							| null/?	| |
| activity_info							| null/?	| |
| btn_info								| null/obj 6	| |
| btn_info > card_btn_click_url			| str		| |
| btn_info > card_btn_jumpurl			| str		| |
| btn_info > card_btn_route_jump_url	| str		| |
| btn_info > card_btn_status			| num		| |
| btn_info > card_btn_style				| num		| |
| btn_info > card_btn_title				| str		| 状态 |
||||
| coupon_discount_price					| str		| |
| coupon_id								| str		| |
| coupon_info							| null/?	| |
| coupon_name							| str		| |
| early_bird_info						| null/?	| |
| gift_buy_info							| null/?	| |
| goods_icon							| str		| 商品图片 |
| goods_id								| str		| |
| goods_max_price						| str		| 最高价 |
| goods_name							| str		| 商品名称 |
| goods_price							| str		| 价格 |
| goods_sort_id							| num		| |
| goods_status							| num		| |
| goods_tag_list						| null/?	| |
| h5_url								| str		| |
| hot_buy_num							| num		| 本次直播 已售数量 |
| is_exclusive							| num		| |
| is_pre_sale							| bool		| |
| jump_link								| str		| |
| jump_url								| str		| |
| pre_sale_info							| null/?	| |
| price_info							| obj 2		| |
| price_info > activity					| null/?	| |
| price_info > normal					| obj 7		| |
| price_info > normal > prefix_price	| str		| |
| price_info > normal > sale_end_time	| num		| |
| price_info > normal > sale_price		| str		| 最低价格 |
| price_info > normal > sale_start_time	| num		| |
| price_info > normal > strock_price	| str		| |
| price_info > normal > strock_show		| num		| |
| price_info > normal > suffix_price	| str		| |
||||
| reward_info							| null/?	| |
| sale_status							| num		| |
| schema_url							| str		| |
| selling_point							| str		| |
| source								| num		| |
| timestamp								| num		| 当前时间 |
| virtual_extra_info					| null/?	| |

```json
{"cmd":"RECOMMEND_CARD","data":{"recommend_list":[{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/dd/80/********************************.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"9.9","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":10,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/d6/f2/********************************.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"199","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":10,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/31/1e/********************************.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"999","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":10,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/e0/79/********************************.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"359","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":10,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}}],"timestamp":1672502400,"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png","update_list":[]},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"RECOMMEND_CARD","data":{"recommend_list":[{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":3,"card_btn_style":0,"card_btn_title":"已下架"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/9b/e6/47e7dadb6d7659fa9198fe575a80f599.jpg","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"369","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":""}},"reward_info":null,"sale_status":3,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":3,"card_btn_style":0,"card_btn_title":"已下架"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/8e/c0/********************************.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"369","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"369","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":3,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FshowSku%3D1%26actionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":3,"card_btn_style":0,"card_btn_title":"已下架"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/33/60/4c22ee1b1f826bd3aea92a390ffe4db4.png","goods_id":"*******************","goods_max_price":"999","goods_name":"商品名称","goods_price":"999","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"389","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":"起"}},"reward_info":null,"sale_status":3,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_jumpurl":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DgoToPay%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","card_btn_route_jump_url":"","card_btn_status":3,"card_btn_style":0,"card_btn_title":"已下架"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/mall/mall/e7/f8/105444195009d0cc312002b288a67331.png","goods_id":"*******************","goods_max_price":"769","goods_name":"商品名称","goods_price":"769","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=2&goods_id=*******************#/member","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"bilibili://live/dispatcher?url=https%3A%2F%2Fmall.bilibili.com%2Fneul-next%2Fdetaillive%2Fdetail.html%3FactionType%3DopenH5Page%26noReffer%3Dtrue%26noTitleBar%3D1%26page%3Ddetaillive_detail%26loadingShow%3D1%26itemsId%3D********%26extraInfo%3D%257B%2522degradeJumpUrl%2522%253A%2522https%25253A%25252F%25252Fmall.bilibili.com%25252Fdetail.html%25253FloadingShow%25253D1%252526noTitleBar%25253D1%252526itemsId%25253D********%2522%252C%2522realtimeRequest%2522%253A%257B%2522itemsId%2522%253A********%252C%2522liveQuery%2522%253A%257B%2522roomId%2522%253A*******%257D%252C%2522shopId%2522%253A****%257D%257D%26goFrom%3Dna&rawContent={\"degradeJumpUrl\":\"https%3A%2F%2Fmall.bilibili.com%2Fdetail.html%3FloadingShow%3D1%26noTitleBar%3D1%26itemsId%3D********\",\"realtimeRequest\":{\"itemsId\":********,\"liveQuery\":{\"roomId\":*******},\"shopId\":****}}","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"769","sale_start_time":0,"strock_price":"","strock_show":0,"suffix_price":""}},"reward_info":null,"sale_status":3,"schema_url":"","selling_point":"","source":2,"timestamp":1672502400,"virtual_extra_info":null}}],"timestamp":1672502400,"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png","update_list":[]},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"RECOMMEND_CARD","data":{"recommend_list":[{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":null,"coupon_discount_price":"0.00","coupon_id":"","coupon_info":null,"coupon_name":"立减00元","early_bird_info":null,"gift_buy_info":null,"goods_icon":"http://i0.hdslb.com/bfs/e-commerce-goods/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"商品名称","goods_price":"15.9","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=1&goods_id=*******************#/taobao","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":null},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"","source":1,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":null,"coupon_discount_price":"5.90","coupon_id":"","coupon_info":null,"coupon_name":"立减4元","early_bird_info":null,"gift_buy_info":null,"goods_icon":"http://i0.hdslb.com/bfs/e-commerce-goods/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"商品名称","goods_price":"9.9","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=1&goods_id=*******************#/taobao","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":null},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"","source":1,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":null,"coupon_discount_price":"7.80","coupon_id":"","coupon_info":null,"coupon_name":"立减11元","early_bird_info":null,"gift_buy_info":null,"goods_icon":"http://i0.hdslb.com/bfs/e-commerce-goods/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"商品名称","goods_price":"18.8","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=1&goods_id=*******************#/taobao","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":null},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"最后9件","source":1,"timestamp":1672502400,"virtual_extra_info":null}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":null,"coupon_discount_price":"7.90","coupon_id":"","coupon_info":null,"coupon_name":"立减5元","early_bird_info":null,"gift_buy_info":null,"goods_icon":"http://i0.hdslb.com/bfs/e-commerce-goods/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"商品名称","goods_price":"12.9","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://live.bilibili.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=1&goods_id=*******************#/taobao","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":null},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"","source":1,"timestamp":1672502400,"virtual_extra_info":null}}],"timestamp":1672502400,"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png","update_list":[]},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"RECOMMEND_CARD","data":{"recommend_list":[{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"","card_btn_jumpurl":"","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/garb/item/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"*主题装扮名称*","goods_price":"8.00","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://www.bilibili.com/h5/mall/suit/detail?id=4389&navhide=1&rebate=3493113265916063&from_id=$uid&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=5&goods_id=*******************#/virdress","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"8.00","sale_start_time":1616756400,"strock_price":"","strock_show":1,"suffix_price":"起"}},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"","source":5,"timestamp":1672502400,"virtual_extra_info":{"goods_type":1,"web_container_type":1}}},{"recommend_card_extra":null,"shopping_card_detail":{"active_info":null,"activity_info":null,"btn_info":{"card_btn_click_url":"","card_btn_jumpurl":"","card_btn_route_jump_url":"","card_btn_status":1,"card_btn_style":1,"card_btn_title":"去抢购"},"coupon_discount_price":"","coupon_id":"","coupon_info":null,"coupon_name":"","early_bird_info":null,"gift_buy_info":null,"goods_icon":"https://i0.hdslb.com/bfs/garb/item/****************************************.jpg","goods_id":"*******************","goods_max_price":"","goods_name":"*主题装扮名称*","goods_price":"10.00","goods_sort_id":0,"goods_status":1,"goods_tag_list":null,"h5_url":"https://www.bilibili.com/h5/mall/suit/detail?id=34358&navhide=1&rebate=3493113265916063&from_id=$uid&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=5&goods_id=*******************#/virdress","hot_buy_num":xxx,"is_exclusive":false,"is_pre_sale":0,"jump_link":"","jump_url":"","pre_sale_info":null,"price_info":{"activity":null,"normal":{"prefix_price":"","sale_end_time":0,"sale_price":"10.00","sale_start_time":1646132400,"strock_price":"","strock_show":1,"suffix_price":"起"}},"reward_info":null,"sale_status":0,"schema_url":"","selling_point":"","source":5,"timestamp":1672502400,"virtual_extra_info":{"goods_type":1,"web_container_type":1}}}],"timestamp":1672502400,"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png","update_list":[]},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### COMMON_NOTICE_DANMAKU
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMMON_NOTICE_DANMAKU" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### COMMON_NOTICE_DANMAKU__data
| key				| type	| value	|
|-|-|-|
| biz_id	？		| num	| 0 |
| content_segments	| []obj	| |
| danmaku_style	？	| obj	| |
| danmaku_uri	？	| str	| "" |
| dmscore			| num	| 144 |
| terminals			| []num	| [1,2,3,4,5] |
```json
{}
```
----
### POPULARITY_RED_POCKET_NEW
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_NEW" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_NEW__data
| key			| type	| value	|
|-|-|-|
| lot_id		| num	| 抽奖id |
| start_time	| num	| 开始时间TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| wait_num		| num	| 排队 |
| uname			| str	| 昵称 |
| uid			| num	| uid |
| action		| str	| "送出" |
| num			| num	| 1 |
| gift_name		| str	| "红包" |
| gift_id		| num	| `13000` |
| price			| num	| 价格(RMB×10) |
| name_color	| str	| 舰长:"#00D1F1" |
| medal_info	| obj	| [medal_info](#粉丝牌信息medal_info) |
```json
{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"lot_id":123,"start_time":1672502400,"current_time":1672502400,"wait_num":0,"uname":"直播小电视","uid":1407831746,"action":"送出","num":1,"gift_name":"红包","gift_id":13000,"price":950,"name_color":"","medal_info":{"target_id":0,"special":"","icon_id":0,"anchor_uname":"","anchor_roomid":0,"medal_level":0,"medal_name":"","medal_color":0,"medal_color_start":0,"medal_color_end":0,"medal_color_border":0,"is_lighted":0,"guard_level":0}}}

{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"action":"送出","current_time":1672502400,"gift_id":13000,"gift_name":"红包","lot_id":123,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":0,"medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":0,"medal_name":"","special":"","target_id":0},"name_color":"","num":1,"price":xxxx,"start_time":0,"uid":0,"uname":"","wait_num":xxx,"wealth_level":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"action":"送出","current_time":1672502400,"gift_id":13000,"gift_name":"红包","lot_id":123,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":0,"medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":0,"medal_name":"","special":"","target_id":0},"name_color":"","num":1,"price":xxxx,"start_time":0,"uid":1407831746,"uname":"直播小电视","wait_num":xxx,"wealth_level":80},"is_report":false,"msg_id":"xxx","send_time":xxxx}
```
----
### POPULARITY_RED_POCKET_START
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULARITY_RED_POCKET_START" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### POPULARITY_RED_POCKET_START__data
| key				| type		| value	|
|-|-|-|
| lot_id			| num		| 抽奖id |
| sender_uid		| num		| uid |
| sender_name		| str		| 昵称 |
| sender_face		| str		| 头像URL |
| join_requirement	| num		| 1 |
| danmu				| str		| "老板大气！点点红包抽礼物" |
| current_time		| num		| TimeStamp(秒) 当前时间 |
| start_time		| num		| TimeStamp(秒) 开始时间 |
| end_time			| num		| TimeStamp(秒) 结束时间 |
| last_time			| num		| 持续时间(秒) |
| remove_time		| num		| TimeStamp(秒) 图标移除时间 |
| replace_time		| num		| TimeStamp(秒) 下一个红包显示时间 |
| lot_status		| num		| [lot_status](#others) 1 |
| h5_url			| str		| f"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId={lot_id}" |
| user_status		| num		| 2 |
| awards			| obj[3]	| |
| lot_config_id		| num		| 红包预设 |
| total_price		| num		| 礼物总价值×0.8 |
| wait_num			| num		| 0 |
#### POPULARITY_RED_POCKET_START__data__awards
| key		| type	| value	|
|-|-|-|
| gift_id	| num	| 礼物id |
| gift_name	| num	| 礼物名称 |
| gift_pic	| num	| 礼物图像URL(140×140) |
| num		| num	| 数量 |
```json
{"cmd":"POPULARITY_RED_POCKET_START","data":{"lot_id":12345,"sender_uid":1407831746,"sender_name":"直播小电视","sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","join_requirement":1,"danmu":"老板大气！点点红包抽礼物！","current_time":1672502400,"start_time":1672502400,"end_time":1672502400,"last_time":180,"remove_time":1672502400,"replace_time":1672502400,"lot_status":1,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId={lot_id}","user_status":2,"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"lot_config_id":-1,"total_price":95000,"wait_num":0}}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":4},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":1},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":5000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":6},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":1},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":7000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":30},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":64000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":31},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":65000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":33},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":67000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":33},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":67000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":35},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":69000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":36},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":70000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":38},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":72000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":41},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":75000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":42},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":76000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":42},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":76000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":44},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":78000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":34}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":55000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":34}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":55000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":7},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":32}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":56000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":8},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":32}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":57000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":8},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":32}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":57000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":9},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":34}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":59000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31212,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","num":12},{"gift_id":31214,"gift_name":"牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":26}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":5,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"https://i0.hdslb.com/bfs/face/72e8cf881fd3eb28aac12d4d4920bf18ed95dc5a.jpg","sender_name":"Brx-困困","sender_uid":18201978,"start_time":xxx,"total_price":41600,"user_status":2,"wait_num":4},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":40}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":79000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":40}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":79000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":42}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":80000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":44}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":81000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":46}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":82000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":46}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":82000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":50}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":84000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":52}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":85000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":6},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":38}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":68000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":6},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":44}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":77000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":6},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":44}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":77000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":29},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":48000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":35},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":51000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":3},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":70}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":95,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":200000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":3},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":70}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":95,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":200000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":3},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":70}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":95,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":200000,"user_status":2,"wait_num":3},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":3},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":70}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":95,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":200000,"user_status":2,"wait_num":4},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31215,"gift_name":"花式夸夸","gift_pic":"https://s1.hdslb.com/bfs/live/28186596880db45a7b843f17d6ebb70feeac06f9.png","num":3},{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":70}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":95,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":200000,"user_status":2,"wait_num":5},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":3},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":4},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":5},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":6},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31217,"gift_name":"星愿水晶球","gift_pic":"https://s1.hdslb.com/bfs/live/288536798081e855e8f645bed6a2d2d27f411ee5.png","num":4},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":99},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":10}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":94,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":500000,"user_status":2,"wait_num":7},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":11},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":12},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":13},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":14},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":15},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":16},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":17},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":18},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":19},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":3},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":4},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":5},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":6},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":8},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":10},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":100000,"user_status":2,"wait_num":9},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":46}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":94000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":9},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":99000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":9},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":99000,"user_status":2,"wait_num":3},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":9},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":48}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":99000,"user_status":2,"wait_num":4},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":49},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":91000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31218,"gift_name":"撒花","gift_pic":"https://s1.hdslb.com/bfs/live/90b124681aa8cfea901251a566305638451a80f0.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":51},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":92000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":1},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":3},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":8}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":9000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":20},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":4}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":17000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":20},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":4}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":17000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":22},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":4}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":18000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":22},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":4}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":18000,"user_status":2,"wait_num":2},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":1},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":24},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":4}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":19000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":2},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":15},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":3}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":21000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":3},{"gift_id":30971,"gift_name":"这个好诶","gift_pic":"https://s1.hdslb.com/bfs/live/9260c680959428c45b3a2742e42ea7ae75e457ef.png","num":14},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":12}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":35000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":4},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":3},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":30}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":45000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":4},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":22},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":6}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":38000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":5},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":3},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":34}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":52000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":5},{"gift_id":31250,"gift_name":"情书","gift_pic":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","num":3},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":34}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":52000,"user_status":2,"wait_num":3},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":19},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":43000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"POPULARITY_RED_POCKET_START","data":{"awards":[{"gift_id":31251,"gift_name":"干杯","gift_pic":"https://s1.hdslb.com/bfs/live/96ec38f351a4e190c4a525bc5e11ff09d2874064.png","num":5},{"gift_id":31278,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/b1be22bf5843b6d1164683233bf35947714118bb.png","num":27},{"gift_id":31225,"gift_name":"牛哇牛哇","gift_pic":"https://s1.hdslb.com/bfs/live/91ac8e35dd93a7196325f1e2052356e71d135afb.png","num":5}],"current_time":xxx,"danmu":"老板大气！点点红包抽礼物！","end_time":xxx,"h5_url":"https://live.bilibili.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId=12345","join_requirement":1,"last_time":180,"lot_config_id":-1,"lot_id":12345,"lot_status":1,"remove_time":xxx,"replace_time":xxx,"sender_face":"http://i2.hdslb.com/bfs/face/72c99193ee2c32f14b7b60711ec4c2ce2eced60c.jpg","sender_name":"直播小电视","sender_uid":1407831746,"start_time":xxx,"total_price":47000,"user_status":2,"wait_num":0},"is_report":false,"msg_id":"xxx","send_time":xxxx}
```
----
### POPULARITY_RED_POCKET_WINNER_LIST
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_WINNER_LIST" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_WINNER_LIST__data
| key			| type			| value	|
|-|-|-|
| lot_id		| num			| 抽奖id |
| total_num		| num			| |
| winner_info	| []!total_num	| |
| awards		| obj			| ${gift_id}:{obj...} |
| version		| num			| 1 |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__winner_info
| array	| type	| value	|
|-|-|-|
| 0		| num	| 获奖者_uid |
| 1		| str	| 获奖者昵称 |
| 2		| num	| `bag_id` |
| 3		| num	| gift_id |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__awards
| key			| type	| value	|
|-|-|-|
| award_type	| num	| |
| award_name	| str	| 礼物名称 |
| award_pic		| str	| URL_图像(140×140) |
| award_big_pic	| str	| URL_图像(360×360) |
| award_price	| num	| 礼物单价(RMB×1000) |
```json
{"cmd":"POPULARITY_RED_POCKET_WINNER_LIST","data":{
	"lot_id":12345,"total_num":52,"winner_info":[
		[12345,"NAME",5157131,31218],
		[12345,"NAME",5157132,30971],
		......
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
----
### ROOM_BLOCK_MSG
[TOP](#直播弹幕)  
用户封禁
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_BLOCK_MSG" |
| data		| obj	| |
| uid		| str	| string |
| uname		| str	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ROOM_BLOCK_MSG__data
| key		| type	| value	|
|-|-|-|
| dmscore	| num	| 30 |
| operator	| num	| 1:"房管" 2:"主播" |
| uid		| num	| |
| uname		| str	| |
```json
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":1,"uid":12345,"uname":"xxx"},"is_report":false,"msg_id":"xxxx","send_time":1672502400000,"uid":"12345","uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":2,"uid":12345,"uname":"xxx"},"is_report":false,"msg_id":"xxxx","send_time":1672502400000,"uid":"12345","uname":"xxx"}
```
----
### AREA_RANK_CHANGED
[TOP](#直播弹幕)  
timestamp: N×5
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "AREA_RANK_CHANGED" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### AREA_RANK_CHANGED__data
| key 14		| type	| value	|
|-|-|-|
| conf_id		| num	| |
| rank_name		| str	| |
| uid			| num	| |
| rank			| num	| |
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
{"cmd":"AREA_RANK_CHANGED","data":{"conf_id":24,"rank_name":"电竞航海","uid":9999,"rank":0,"icon_url_blue":"https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png","icon_url_pink":"https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png","icon_url_grey":"https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png","action_type":1,"timestamp":1676968813,"msg_id":"ffffffff-ffff-4fff-ffff-ffffffffffff","jump_url_link":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=****&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank","jump_url_pc":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=****&conf_id=24&pc_ui=338,465,f4eefa,0#/area-rank","jump_url_pink":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=****&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank","jump_url_web":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=****&conf_id=24#/area-rank"}}
{"cmd":"AREA_RANK_CHANGED","data":{"action_type":1,"conf_id":24,"icon_url_blue":"https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png","icon_url_grey":"https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png","icon_url_pink":"https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png","jump_url_link":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=********&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank","jump_url_pc":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=********&conf_id=24&pc_ui=338,465,f4eefa,0#/area-rank","jump_url_pink":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=********&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank","jump_url_web":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=********&conf_id=24#/area-rank","msg_id":"6bbd138d-4fd4-40fe-ab29-4001f2546fa2","rank":0,"rank_name":"电竞航海","timestamp":1672502400,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"AREA_RANK_CHANGED","data":{"action_type":1,"conf_id":24,"icon_url_blue":"https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png","icon_url_grey":"https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png","icon_url_pink":"https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png","jump_url_link":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3&ruid=********&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0#/area-rank","jump_url_pc":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&ruid=********&conf_id=24&pc_ui=338,465,f4eefa,0#/area-rank","jump_url_pink":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&ruid=********&conf_id=24&is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100,12,0;2,2,375,100p,ffffff,0,30,100,0,0;3,3,100p,70p,ffffff,0,30,100,12,0;4,2,375,100p,ffffff,0,30,100,0,0;5,3,100p,70p,ffffff,0,30,100,0,0;6,3,100p,70p,ffffff,0,30,100,0,0;7,3,100p,70p,ffffff,0,30,100,0,0;8,3,100p,70p,ffffff,0,30,100,0,0#/area-rank","jump_url_web":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=********&conf_id=24#/area-rank","msg_id":"4cacb078-36f2-4840-af3e-56cf9a76d2c8","rank":1,"rank_name":"电竞航海","timestamp":1672502400,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```

----
### HOT_BUY_NUM
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "HOT_BUY_NUM" |
| data	| obj	| |
#### HOT_BUY_NUM__data
| key		| type	| value	|
|-|-|-|
| goods_id	| str	| id |
| num		| num	| |
```json
{}
```
----
### PK_BATTLE_END
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_END" |
| pk_id		| str	| |
| pk_status	| num	| # |
| timestamp	| obj	| TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_END__data
| key			| type	| value	|
|-|-|-|
| battle_type	| num	| |
| timer			| num	| |
| init_info		| obj	| |
| match_info	| obj	| |
#### PK_BATTLE_END__data__&2_info
| key			| type	| value	|
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
{"cmd":"PK_BATTLE_END","pk_id":"321224414","pk_status":401,"timestamp":1672502400,"data":{"battle_type":2,"timer":10,"init_info":{"room_id":123,"votes":190,"winner_type":2,"best_uname":"XXX"},"match_info":{"room_id":456,"votes":50,"winner_type":-1,"best_uname":"YYY"}}}
{"cmd":"PK_BATTLE_END","pk_id":"321224459","pk_status":501,"timestamp":1672502400,"data":{"battle_type":2,"timer":10,"init_info":{"room_id":123,"votes":1314,"winner_type":3,"best_uname":"XXX"},"match_info":{"room_id":456,"votes":51,"winner_type":-1,"best_uname":"YYY"}}}
```
----
### WIDGET_GIFT_STAR_PROCESS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WIDGET_GIFT_STAR_PROCESS" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### WIDGET_GIFT_STAR_PROCESS__data
| key				| type	| value	|
|-|-|-|
| start_date		| num	| yyyyMMdd(星期一) |
| process_list		| []obj	| |
| finished			| bool	| |
| ddl_timestamp		| num	| TimeStamp(秒) 下一个星期一00:00:00 UTC+8 |
| version			| num	| 当前时间TimeStamp(毫秒) |
| reward_gift		| num	| |
| reward_gift_img	| str	| |
| reward_gift_name	| str	| "礼物星球" |
#### WIDGET_GIFT_STAR_PROCESS__data__process_list
| key			| type	| value	|
|-|-|-|
| gift_id		| num	| |
| gift_img		| str	| |
| gift_name		| str	| |
| completed_num	| num	| |
| target_num	| num	| |
```json
1680359606{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":14,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":0,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680359605806,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680360351{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":15,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":0,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680360350449,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680361560{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":15,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":0,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680361560532,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680361600{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":15,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680361600357,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680361924{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":16,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680361923992,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680361962{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":17,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680361962396,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680361967{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":18,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680361966216,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680363314{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":18,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680363313305,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680363860{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":19,"target_num":20},{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680363859490,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1680364405{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"start_date":20230327,"process_list":[{"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","completed_num":1,"target_num":8},{"gift_id":32734,"gift_img":"https://s1.hdslb.com/bfs/live/ae339a91cb7e694bd489f1bb1ad2628a3b36997f.png","gift_name":"礼物星球","completed_num":0,"target_num":5},{"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","completed_num":0,"target_num":1}],"finished":false,"ddl_timestamp":1680451200,"version":1680364405207,"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球"}}
1688841104{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{"ddl_timestamp":1688918400,"finished":false,"process_list":[{"completed_num":80,"gift_id":31037,"gift_img":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","gift_name":"礼物星球","target_num":100},{"completed_num":1,"gift_id":31053,"gift_img":"https://s1.hdslb.com/bfs/live/0205d703553d0625ba24aefd421eb5e350ce3c20.png","gift_name":"礼物星球","target_num":8},{"completed_num":0,"gift_id":31591,"gift_img":"https://s1.hdslb.com/bfs/live/239c1e0c584b47601347812536422a37a5e3b3b9.png","gift_name":"礼物星球","target_num":1}],"reward_gift":32269,"reward_gift_img":"https://s1.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球","start_date":20230703,"version":1688841104906},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### LIVE_INTERACTIVE_GAME
[TOP](#直播弹幕)  
with `DANMU_MSG`
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_INTERACTIVE_GAME" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### LIVE_INTERACTIVE_GAME__data
| key 17			| type	| value	|
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
{"cmd":"LIVE_INTERACTIVE_GAME","data":{"type":2,"uid":123,"uname":"XXX","uface":"","gift_id":0,"gift_name":"","gift_num":0,"price":0,"paid":false,"msg":"text","fans_medal_level":18,"guard_level":0,"timestamp":1672502400,"anchor_lottery":null,"pk_info":null,"anchor_info":null,"combo_info":null}}
```
----
### LIVE_MULTI_VIEW_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_MULTI_VIEW_CHANGE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### LIVE_MULTI_VIEW_CHANGE__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_MULTI_VIEW_CHANGE","data":{"scatter":{"max":120,"min":5}},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### SUPER_CHAT_ENTRANCE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_ENTRANCE" |
| data		| obj	| |
| roomid ※	| num	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SUPER_CHAT_ENTRANCE__data
| key				| type	| value	|
|-|-|-|
| status ※			| num	| |
| icon				| str	| |
| jump_url			| str	| |
| broadcast_type	| num	| |
```json
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","jump_url":"https://live.bilibili.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","status":0}}
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"status":1,"jump_url":"https://live.bilibili.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","broadcast_type":1},"roomid":"12345"}
```
----
### SYS_MSG
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SYS_MSG" |
| msg		| str	| |
| url		| str	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
```json
{"cmd":"SYS_MSG","is_report":false,"msg":"争夺开启，时间周五20点至周日20点，逾期不候哟！","msg_id":"410088122626048","send_time":1689336061020,"url":""}	//每周五20:00:59 UTC+8 广播
```
----
### VOICE_JOIN_STATUS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_STATUS" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_STATUS__data
| key 12			| type	| value	|
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
----
### DM_INTERACTION
[TOP](#直播弹幕)  
弹幕投票
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "DM_INTERACTION" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### DM_INTERACTION__data
| key		| type	| value	|
|-|-|-|
| id		| num	| |
| status	| num	| 3:开始 4:进行中 5:结束 |
| type		| num	| |
| data		| str	| json |
#### DM_INTERACTION__data__data
| key					| type	| value	|
|-|-|-|
| question				| str	| |
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
| my_vote				| num	| | **TODO**
#### DM_INTERACTION__data__data__options
| key		| type	| value	|
|-|-|-|
| idx		| num	| start:1 |
| desc		| str	| 投票选项 |
| cnt		| num	| 投票人数 |
| percent	| float	| 百分比 总计数小于~~5~~时为0 |
#### DM_INTERACTION__example
```json
{"cmd":"DM_INTERACTION","data":{"id":104,"status":4,"type":101,"data":"{\"question\":\"本局谁将获得胜利？\",\"options\":[{\"idx\":1,\"desc\":\"AAA\",\"cnt\":0,\"percent\":0},{\"idx\":2,\"desc\":\"BBB\",\"cnt\":0,\"percent\":0}],\"vote_id\":12234567,\"cnt\":0,\"duration\":180000,\"left_duration\":179000,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":1,\"result_text\":\"平局\",\"component\":\"https://live.bilibili.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0\",\"natural_die_duration\":30000,\"my_vote\":0}"}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"question\":\"xxxxx\",\"options\":[{\"idx\":1,\"desc\":\"xxxxx\",\"cnt\":1282,\"percent\":0.24066078468180965},{\"idx\":2,\"desc\":\"yyyyy\",\"cnt\":4045,\"percent\":0.7593392153181904}],\"vote_id\":7194538,\"cnt\":5327,\"duration\":180000,\"left_duration\":0,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":3,\"result_text\":\"红获胜\",\"component\":\"https://live.bilibili.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0\",\"natural_die_duration\":30000,\"my_vote\":0}","id":xxxxx,"status":5,"type":101},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### PLAY_TAG
[TOP](#直播弹幕)  
比赛 事件(开始、First Blood、击败、Double Kill、大小龙、结束)
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PLAY_TAG" |
| data	| obj	| |
#### PLAY_TAG__data
| key	| type	| value	|
|-|-|-|
| tag_id	| num	| |
| pic		| str	| 事件pic |
| timestamp	| num	| 事件发生时间TimeStamp(秒) |
| type		| str	| "ADD" |
```json
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e04525fee9ea6ea6973e8bd1116d9f1f6501d37.png","timestamp":1672502400,"type":"ADD"}}// Double Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e842f1a260e519158712e086e2a10e6fc280e53.png","timestamp":1672502400,"type":"ADD"}}// Quadra Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/152132594676ffb27cd1d7992fe02f92b4909540.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/2ac5e22aa856b3b6739bc725cbe78b42b702eec0.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/3c26626a30fdb70e44e16fd4313fa02785486e30.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/5e59bb41b61b015f3665ba922fc1bd6db00c6d32.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/78c10171a17f19fb6f22296091c106852447ce7a.png","timestamp":1672502400,"type":"ADD"}}// First Blood [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/7c3cc2cdca443b5fcab636ceaec46d5922c257d5.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/92d895535c9517e13b4cb7d908faaf29aefbcb4a.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/bc1e526e05c11c9ffa515810268fca3d96472af7.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c241edb936a544538207f15a896db867878d262c.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c56b9ea02e1617a97fc933481b63ffab57ad296c.png","timestamp":1672502400,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/de9d1486f85777cc74798eb1630abba0a695aa15.png","timestamp":1672502400,"type":"ADD"}}// Triple Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/e01db14207b1a1087d1829db2690753e51080b26.png","timestamp":1672502400,"type":"ADD"}}
```
----
### FULL_SCREEN_SPECIAL_EFFECT
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "FULL_SCREEN_SPECIAL_EFFECT" |
| data	| obj	| |
#### FULL_SCREEN_SPECIAL_EFFECT__data
| key			| type	| value	|
|-|-|-|
| type			| num	| |
| ids			| []num	| |
| queue			| num	| |
| platform_in	| []num	| |
```json
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[433],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[514],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[515],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[670],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[949],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"ids":[514],"platform_in":[1,2],"queue":2,"type":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### TRADING_SCORE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "TRADING_SCORE" |
| data	| obj	| |
#### TRADING_SCORE__data
| key				| type	| value	|
|-|-|-|
| bubble_show_time	| num	| |
| num				| num	| |
| score_id			| num	| |
| uid				| num	| 主播uid |
| update_time		| num	| 当前时间TimeStamp(秒) |
| update_type		| num	| |
```json
{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":3,"score_id":3,"uid":123,"update_time":1672502400,"update_type":1}}
```
----
### PK_BATTLE_START_NEW
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_START_NEW" |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
| data		| obj	| |
| roomid	| num	| |
#### PK_BATTLE_START_NEW__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_START",    "pk_id":321224540,"pk_status":201,"timestamp":1672502400,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":1672502400,"pk_frozen_time":1676586733,"pk_end_time":1676586743,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":1676586673,"final_conf":{"switch":1,"start_time":1676586553,"end_time":1676586613},"init_info":{"room_id":123,"date_streak":0},"match_info":{"room_id":456,"date_streak":0}},"roomid":"123"}
{"cmd":"PK_BATTLE_START_NEW","pk_id":321224540,"pk_status":201,"timestamp":1672502400,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":1672502400,"pk_frozen_time":1676586733,"pk_end_time":1676586743,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":1676586673,"final_conf":{"switch":1,"start_time":1676586553,"end_time":1676586613},"init_info":{"room_id":123,"date_streak":0},"match_info":{"room_id":456,"date_streak":0}},"roomid":"123"}
```
----
### ROOM_SILENT_xxx
[TOP](#直播弹幕)  
`ROOM_SILENT_ON` 开启直播间全局禁言  
`ROOM_SILENT_OFF` 解除直播间全局禁言  
| key		| type	| value	|
|-|-|-|
| data		| obj	| |
| cmd		| str	| "ROOM_SILENT_ON" "ROOM_SILENT_OFF" |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ROOM_SILENT__data
| key		| type	| value	|
|-|-|-|
| type		| str	| ""关闭 "member"全员禁言 "medal"粉丝牌等级禁言 "level"UL等级禁言 |
| level		| num	| 粉丝牌等级/用户UL等级 |
| second	| num	| 结束时间TimeStamp(秒) |
```json
{"data":{"type":"member","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
{"data":{"type":"level","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
{"data":{"type":"level","level":60,"second":1672502400},"cmd":"ROOM_SILENT_ON"}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"member"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"member"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}

{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"level"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":-1,"type":"level"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"level"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":1672502400,"type":"level"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}

{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"medal"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":-1,"type":"medal"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"medal"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":1672502400,"type":"medal"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}

{"data":{"type":"","level":0,"second":0},"cmd":"ROOM_SILENT_OFF"}
{"cmd":"ROOM_SILENT_OFF","data":{"level":0,"second":0,"type":""},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
```python
match silent.type:
	case "member":  print(f'[{client.room_id}] [主播对所有用户开启了禁言]')
	case "medal":   print(f'[{client.room_id}] [主播对粉丝勋章 ' + silent.level + ' 以下的用户开启了禁言]')
	case "level":   print(f'[{client.room_id}] [主播对用户等级 UL.' + silent.level + ' 以下的用户开启了禁言]')
	case "":        print(f'[{client.room_id}] [主播取消了房间禁言]')
```
----
### CHANGE_ROOM_INFO
[TOP](#直播弹幕)  
更换直播间背景(WEB)  
| key			| type		| value	|
|-|-|-|
| cmd			| str		| "CHANGE_ROOM_INFO" |
| background	| str		| URL |
| roomid		| num/str	| |
| is_report		| bool		| |
| msg_id		| str		| |
| send_time		| num		| |
```json
1683970392.669950{"cmd":"CHANGE_ROOM_INFO","background":"http://i0.hdslb.com/bfs/live/room_bg/17bb8b588f8371a8582fa443fe2d5a0b7ac01453.jpg","roomid":"21987615"}
{"background":"https://i0.hdslb.com/bfs/live/f3c1e1e22dfb1942bd88c33f1aa174efe7a38dfd.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
{"background":"https://i0.hdslb.com/bfs/live/785922a49980e1aa3239249c8360909488940d7d.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
{"background":"https://i0.hdslb.com/bfs/live/636d66a97d5f55099a9d8d6813558d6d4c95fd61.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
{"background":"https://i0.hdslb.com/bfs/live/2bac063036fbcf316e021fbfb8109ff3028360a6.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
{"background":"https://i0.hdslb.com/bfs/live/2836bb7b84c792e2c6aadfd4d1cce13484775fa3.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
{"background":"https://i0.hdslb.com/bfs/live/2388faed3728f3396052273ad4c3c9af21c411fc.jpg","cmd":"CHANGE_ROOM_INFO","is_report":false,"msg_id":"xxx","roomid":12345,"send_time":1672502400000}
```
----
### ROOM_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_CHANGE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ROOM_CHANGE__data
| key 7				| type	| value	|
|-|-|-|
| title				| str	| 直播间标题 |
| area_id			| num	| [分区ID](#分区ID) |
| parent_area_id	| num	| [父分区ID](#分区ID) |
| area_name			| str	| [分区name](#分区ID) |
| parent_area_name	| str	| [父分区name](#分区ID) |
| live_key			| str	| [本次直播live_key](#live) |
| sub_session_key	| str	| [本次直播sub_session_key](#live) |
```json
{"cmd":"ROOM_CHANGE","data":{"title":"直播间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"0","sub_session_key":""}}
{"cmd":"ROOM_CHANGE","data":{"title":"直播间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"111111111111111111","sub_session_key":"111111111111111111sub_time:1672502400"}}
{"cmd":"ROOM_CHANGE","data":{"area_id":xxxx,"area_name":"xxx","live_key":"111111111111111111","parent_area_id":xxxx,"parent_area_name":"xxx","sub_session_key":"111111111111111111sub_time:1672502400","title":"直播间标题"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### OBS_SHIELD_STATUS_UPDATE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OBS_SHIELD_STATUS_UPDATE" |
| data		| obj	| |
| roomid	| str	| 直播间id |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### OBS_SHIELD_STATUS_UPDATE__data
| key		| type	| value	|
|-|-|-|
| change	| num	| 1 |
```json
{"cmd":"OBS_SHIELD_STATUS_UPDATE","data":{"change":1},"roomid":"123"}
{"cmd":"OBS_SHIELD_STATUS_UPDATE","data":{"change":1},"is_report":false,"msg_id":"xxx","roomid":"xxx","send_time":xxx}
```
----
### RING_STATUS_CHANGE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "RING_STATUS_CHANGE" |
| data	| obj	| |
#### RING_STATUS_CHANGE__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 0 |
```json
{"cmd":"RING_STATUS_CHANGE","data":{"status":0}}
```
----
### RING_STATUS_CHANGE_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RING_STATUS_CHANGE_V2" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### RING_STATUS_CHANGE_V2__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 0 |
```json
{"cmd":"RING_STATUS_CHANGE_V2","data":{"status":0}}
{"cmd":"RING_STATUS_CHANGE_V2","data":{"status":1},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### VOICE_JOIN_LIST
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_LIST" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_LIST__data
| key			| type	| value	|
|-|-|-|
| cmd			| str	| |
| room_id		| num	| |
| category		| num	| |
| apply_count	| num	| |
| red_point		| num	| |
| refresh		| num	| |
```json
{"cmd":"VOICE_JOIN_LIST","data":{"cmd":"","room_id":12345,"category":1,"apply_count":0,"red_point":1,"refresh":1},"room_id":12345}
```
----
### VOICE_JOIN_ROOM_COUNT_INFO
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_ROOM_COUNT_INFO" |
| data		| obj	| |
| room_id	| num	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### VOICE_JOIN_ROOM_COUNT_INFO__data
| key			| type	| value	|
|-|-|-|
| cmd			| str	| |
| room_id		| num	| |
| root_status	| num	| |
| room_status	| num	| |
| apply_count	| num	| |
| notify_count	| num	| |
| red_point		| num	| |
```json
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"cmd":"","room_id":12345,"root_status":1,"room_status":1,"apply_count":0,"notify_count":0,"red_point":0},"room_id":12345}
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"apply_count":0,"cmd":"","notify_count":0,"red_point":0,"room_id":12345,"room_status":1,"root_status":1},"is_report":false,"msg_id":"xxx","room_id":12345,"send_time":xxx}
```
----
### ROOM_SKIN_MSG
[TOP](#直播弹幕)  
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "ROOM_SKIN_MSG" |
| skin_id		| num	| |
| status		| num	| 0,1 |
| end_time		| num	| TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| only_local	| bool	| |
| scatter ※		| obj	| |
| skin_config ※	| obj	| |
#### ROOM_SKIN_MSG__skin_config
| key			| type	| value	|
|-|-|-|

```json
{"cmd":"ROOM_SKIN_MSG","skin_id":452,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c6a13965d7ae8ab433ef05f643876d70ccd35204.zip","md5":"6EFCA3C8FEC1A595B2C185FCAE1741A0"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/8bd0abf11eb68e1867eda7ec74c8ff6bc158392a.zip","md5":"DE24184A495D8AC4D36C40E653EE6F1C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0fb370c451460cb0df6dafec005f7c361b6fbd98.zip","md5":"20B5DE12BC2C20037F30DD0ED76DC67F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/2e2857bbaa31de676896d436e3dadd083c439dc0.zip","md5":"66CF9042BBB331FF056DAB75FC56398E","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0847cbf4e927d494015bfa0ef025c2d38b6a3b7a.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/bfb1140f97cef5d1ed42fe32d9d873db17f1e443.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/3cf53eb68bf888cafd958b26f1257ef892de6e6f.jpg","mainText":"#FFffffff","normalText":"#FFffe2b2","highlightContent":"#FF500c22","border":"#FFffe2b2","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":454,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c9a6c91cf1b3c0410053ad8d7453f1d3fa877549.zip","md5":"621F5833CE6FD085E800303AFFB4C3FD"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/3b91fa0f1e9e19016afa7af4c488b378657a5897.zip","md5":"716CCAB55B2D95EC8982F324BB59658C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0369e00a3b15672638bae9c7363d177ebe437281.zip","md5":"5FCA732A31E2B52AAF674F589C97230F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/20fe37059dbdf179ba34907496180caf48f9b2fd.zip","md5":"FD0306E4CE4D2848DDD430CD7C72C341","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/d2b7bf6fb6e6d66780a1227e71ea6bdc66dcf0e2.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF6c99dc","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":461,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/b2e54b7cb64142ee32833d1ed84903fed67a0378.zip","md5":"710AFA69D08FC727EDA821E3AF5CA0C5"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/1143aa4127f6e6faf4ba36c483e506df88b069a8.zip","md5":"55AE9AC3311D58A5EABBABD85366BB2D"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/261dfdb079b3e5ee54f9000cec2274b5f4c5fe7c.zip","md5":"FE1737D3597AC78C791CD408D3A44B3B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/4d1bccb234baa040e379dfe55467e3ccc76658bf.zip","md5":"3CC0D358666AAEE5B0A8CA6411BA6730","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/50b6c93ccdcbdff73589c19eb6138fdf97a95d31.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF4f6dcb","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":64,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/545a91102973626b1e39cec1c7cb93edfd55a7d8.zip","md5":"083B542663A17F47E0379EF7E7269CA3"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/ae3c6c3ca3b32fd21d3612dc7938a5bfce928dcf.zip","md5":"AB4F5A4D83FACA7D45AF2ACCC175CEAF"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/e26c2cb17d3b063d736104926bdeadcacef8a46b.zip","md5":"B2A4F7BD6B4F446BC85980B0B31EF37B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/a6bde45e0de2010afebdeab3572c2d078f2b3525.zip","md5":"9B0E3DEC95E3DB1CDC49CF838B539715","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/78c2321d946dcdf57c37779e674da6983f0850ee.png","giftControlBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/13f1bad1b1c1a050df36beb907d742a6a68d3fdb.png","rankListBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/93db8458c57791f7b89ec75ff54221aa8f33e9fa.png","mainText":"#FFf2ae09","normalText":"#FF999999","highlightContent":"#FFf2ae09","border":"#33999999"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":65,"status":0,"end_time":1672502400,"current_time":1672502400,"only_local":false}
```
----
### PK_BATTLE_ENTRANCE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_ENTRANCE" |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_ENTRANCE__data
| key		| type	| value	|
|-|-|-|
| is_open	| bool	| |
```json
{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1672502400,"data":{"is_open":true}}
```
----
### LIVE_PANEL_CHANGE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "LIVE_PANEL_CHANGE" |
| data	| obj	| |
#### LIVE_PANEL_CHANGE__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_PANEL_CHANGE","data":{"type":2,"scatter":{"max":150,"min":5}}}
{"cmd":"LIVE_PANEL_CHANGE","data":{"scatter":{"max":150,"min":5},"type":2},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### RANK_REM
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RANK_REM" |
| data		| obj	| |
#### RANK_REM__data
| key		| type	| value	|
|-|-|-|
| name		| str	| |
| room_id	| num	| 直播间id |
| ruid		| num	| 主播uid |
| time		| num	| 当前时间TimeStamp(秒) |
| uid		| num	| |
```json
{"cmd":"RANK_REM","data":{"name":"online_gold","room_id":12345,"ruid":12345,"time":1672502400,"uid":123}}
```
----
### GUARD_ACHIEVEMENT_ROOM
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "GUARD_ACHIEVEMENT_ROOM" |
| data	| obj	| |
#### GUARD_ACHIEVEMENT_ROOM__data
| key							| type	| value	|
|-|-|-|
| anchor_basemap_url			| str	| |
| anchor_guard_achieve_level	| num	| |
| anchor_modal					| obj	| |
| app_basemap_url				| str	| |
| current_achievement_level		| num	| 3 |
| dmscore						| num	| 8 |
| event_type					| num	| 1 |
| face							| str	| 主播头像URL |
| first_line_content			| str	| 恭喜主播<%XXX%> |
| first_line_highlight_color	| str	| #FFD432 |
| first_line_normal_color		| str	| #FFFFFF |
| headmap_url					| str	| |
| is_first						| bool	| True |
| is_first_new					| bool	| False |
| room_id						| num	| 12345 |
| second_line_content			| str	| 舰队规模突破<%xxx%> |
| second_line_highlight_color	| str	| #06DDFF |
| second_line_normal_color		| str	| #FFFFFF |
| show_time						| num	| 3 |
| web_basemap_url				| str	| |
#### GUARD_ACHIEVEMENT_ROOM__anchor_modal
| key							| type	| value	|
|-|-|-|
| first_line_content			| str	| 恭喜当前舰队规模突破<%xxx%> |
| highlight_color				| str	| #00DCFF |
| second_line_content			| str	| 至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～ |
| show_time						| num	| 5 |
```json
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":8,"event_type":1,"face":"$avatar_url","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":8,"event_type":2,"face":"$avatar_url","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":false,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"","anchor_guard_achieve_level":0,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%0%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":0},"app_basemap_url":"","current_achievement_level":1,"dmscore":8,"event_type":2,"face":"$avatar_url","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"","first_line_normal_color":"","headmap_url":"","is_first":false,"is_first_new":false,"room_id":1234,"second_line_content":"舰队规模突破<%0%>","second_line_highlight_color":"","second_line_normal_color":"","show_time":3,"web_basemap_url":"普通无需图片"}}
```
----
### PK_BATTLE_FINAL_PROCESS
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_FINAL_PROCESS" |
| data	| obj	| |
#### PK_BATTLE_FINAL_PROCESS__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":1672502400},"pk_id":321224414,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":1672502400},"pk_id":321224414,"pk_status":301,"timestamp":1672502400}
```
----
### PK_BATTLE_MATCH_TIMEOUT
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_MATCH_TIMEOUT" |
| data	| obj	| |
#### PK_BATTLE_MATCH_TIMEOUT__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_MATCH_TIMEOUT","data":{"battle_type":2}}
```
----
### PK_BATTLE_PROCESS_NEW
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_PROCESS_NEW" |
| data	| obj	| |
#### PK_BATTLE_PROCESS_NEW__data
| key			| type	| value	|
|-|-|-|
| battle_type	| num	| |
| init_info		| obj	| |
| match_info	| obj	| |
| pk_id			| num	| |
| pk_status		| num	| |
| timestamp		| num	| |
#### PK_BATTLE_END__data__&2_info
| key			| type		| value	|
|-|-|-|
| room_id		| num		| 我方直播间id or 对方直播间id |
| votes			| num		| |
| best_uname	| num		| 最高贡献者 |
| vision_desc	| num		| |
| assist_info	| null/obj	| |
```json
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":8,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":9,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":1,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"$avatar_url","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":10,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"$avatar_url","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":2,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":45,"votes":51,"best_uname":"YYY","vision_desc":-1}},"pk_id":321224459,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"$avatar_url","uname":"XXX"}]},"match_info":{"room_id":456,"votes":104,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"$avatar_url","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"$avatar_url","uname":"XXX"}]},"match_info":{"room_id":456,"votes":105,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"$avatar_url","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
```
----
### PK_BATTLE_PRE_NEW
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_PRE_NEW" |
| data	| obj	| |
#### PK_BATTLE_PRE_NEW__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":321224475,"pk_status":101,"status_msg":"","timestamp":1672502400,"data":{"is_followed":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":A,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":321224510,"pk_status":101,"status_msg":"","timestamp":1672502400,"data":{"is_followed":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":B,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224414,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":C,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224459,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":D,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224507,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":E,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":321224540,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":12345,"room_id":F,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
```
----
### PK_BATTLE_PUNISH_END
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_PUNISH_END" |
| data	| obj	| |
#### PK_BATTLE_PUNISH_END__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PUNISH_END","pk_id":"321224475","pk_status":1001,"status_msg":"","timestamp":1672502400,"data":{"battle_type":6}}
{"cmd":"PK_BATTLE_PUNISH_END","pk_id":"321224510","pk_status":1001,"status_msg":"","timestamp":1672502400,"data":{"battle_type":6}}
```
----
### PK_BATTLE_PRE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_PRE" |
| data	| obj	| |
#### PK_BATTLE_PRE__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224414,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":1234,"room_id":A,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224459,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":1234,"room_id":B,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224507,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":1234,"room_id":C,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
{"cmd":"PK_BATTLE_PRE","pk_status":101,"pk_id":321224540,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"$avatar_url","uid":1234,"room_id":D,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":12345}
```
----
### PK_BATTLE_PROCESS
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_PROCESS" |
| data	| obj	| |
#### PK_BATTLE_PROCESS__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
#### PK_BATTLE_END__data__&2_info
| key			| type	| value	|
|-|-|-|
| room_id		| num	| 我方直播间id or 对方直播间id |
| votes			| num	| |
| winner_type	| num	| |
| best_uname	| num	| 最高贡献者 |
```json
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224414,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224459,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":-1}},"pk_id":321224459,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":-1}},"pk_id":321224459,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":-1}},"pk_id":321224507,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224414,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224414,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":-1},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":1}},"pk_id":321224507,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224507,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"","vision_desc":0}},"pk_id":321224540,"pk_status":301,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":123,"best_uname":"XXX","vision_desc":0},"match_info":{"room_id":A,"votes":456,"best_uname":"XXX","vision_desc":0}},"pk_id":321224540,"pk_status":301,"timestamp":1672502400}
```
----
### SHOPPING_BUBBLES_STYLE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "SHOPPING_BUBBLES_STYLE" |
| data	| obj	| |
#### SHOPPING_BUBBLES_STYLE__data
| key						| type		| value	|
|-|-|-|
| interval_between_bubbles	| num		| |
| interval_between_queues	| num		| |
| cycle_time				| num		| |
| goods_count				| num		| |
| checksum					| str		| **md5("null")** |
| bubbles_list				| null/?	| |
```json
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":0,"checksum":"37a6259cc0c1dae299a7866489dff0bd","bubbles_list":null}}
```
----
### GIFT_STAR_PROCESS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_STAR_PROCESS" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### GIFT_STAR_PROCESS__data
| key		| type	| value	|
|-|-|-|
| status	| num	| |
| tip		| str	| |
```json
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"棒棒糖已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"打call已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"动鳗电池已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"干杯已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"告白花束已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"情书已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"水晶之恋已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小蛋糕已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小蝴蝶已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小花花已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"星河入梦已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"星愿水晶球已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"这个好诶已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":2,"tip":"所有星球已点亮"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ANCHOR_NORMAL_NOTIFY
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "ANCHOR_NORMAL_NOTIFY" |
| data	| obj	| |
#### ANCHOR_NORMAL_NOTIFY__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ANCHOR_NORMAL_NOTIFY","data":{"type":1,"show_type":1,"info":{"icon":"https://i0.hdslb.com/bfs/live/f3ebd37ee59991bc45538be58e68a6d3aa43ccca.png","title":"","content":"恭喜，获得推荐位buff加持，上推荐的几率大大提高，持续时间：1小时。"}}}
```
----
### LIVE_OPEN_PLATFORM_GAME
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "LIVE_OPEN_PLATFORM_GAME" |
| data	| obj	| |
#### LIVE_OPEN_PLATFORM_GAME__data
| key						| type		| value	|
|-|-|-|
| msg_type					| str		| "panel_update"/"panel_reset"/"game_end" |
| msg_sub_type				| str		| "panel_update"/"panel_reset"/"game_end" |
| game_name					| str		| |
| game_code					| str		| |
| game_id					| str		| UUID4 |
| game_status				| str		| |
| game_msg					| str		| |
| game_conf					| str(obj)	| |
| interactive_panel_conf	| str		| |
| timestamp					| num		| 当前时间 TimeStamp(秒) |
| block_uids				| null/[]	| |
#### LIVE_OPEN_PLATFORM_GAME__data__game_conf
| key				| type	| value	|
|-|-|-|
| roomId			| num	| |
| state				| num	| |
| isShowIdentity	| bool	| |
| endTime			| num	| |
| maxPlayerCount	| num	| |
| players			| []obj	| |
#### LIVE_OPEN_PLATFORM_GAME__data__game_conf__players
| key				| type	| value	|
|-|-|-|
| ......			| xxx	| |
#### LIVE_OPEN_PLATFORM_GAME__data__game_conf__players__role
| key				| type	| value	|
|-|-|-|
| ......			| xxx	| |
```json
{"cmd":"LIVE_OPEN_PLATFORM_GAME","data":{"msg_type":"panel_update","msg_sub_type":"panel_update","game_name":"XXXX","game_code":"16502xxxxxxxx","game_id":"XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX","game_status":"","game_msg":"{\"roomId\":123,\"state\":6,\"isShowIdentity\":true,\"endTime\":1680367570,\"maxPlayerCount\":36,\"players\":[{\"no\":5,\"uid\":1,\"role\":{\"roleType\":4,\"campType\":1,\"isDie\":false}},{\"no\":10,\"uid\":2,\"role\":{\"roleType\":20,\"campType\":2,\"isDie\":false}},{\"no\":12,\"uid\":3,\"role\":{\"roleType\":19,\"campType\":1,\"isDie\":false}},{\"no\":14,\"uid\":4,\"role\":{\"roleType\":23,\"campType\":1,\"isDie\":false}},{\"no\":17,\"uid\":5,\"role\":{\"roleType\":19,\"campType\":1,\"isDie\":false}},{\"no\":20,\"uid\":6,\"role\":{\"roleType\":2,\"campType\":2,\"isDie\":false}},{\"no\":21,\"uid\":7,\"role\":{\"roleType\":18,\"campType\":2,\"isDie\":false}},{\"no\":25,\"uid\":8,\"role\":{\"roleType\":22,\"campType\":1,\"isDie\":false}},{\"no\":26,\"uid\":9,\"role\":{\"roleType\":21,\"campType\":2,\"isDie\":false}},{\"no\":35,\"uid\":10,\"role\":{\"roleType\":13,\"campType\":2,\"isDie\":false}},{\"no\":36,\"uid\":11,\"role\":{\"roleType\":19,\"campType\":1,\"isDie\":false}},{\"no\":30,\"uid\":12,\"role\":{\"roleType\":23,\"campType\":1,\"isDie\":false}},{\"no\":9,\"uid\":13,\"role\":{\"roleType\":23,\"campType\":1,\"isDie\":false}},{\"no\":7,\"uid\":14,\"role\":{\"roleType\":8,\"campType\":1,\"isDie\":true}},{\"no\":18,\"uid\":15,\"role\":{\"roleType\":17,\"campType\":1,\"isDie\":true}},{\"no\":27,\"uid\":1+,\"role\":{\"roleType\":8,\"campType\":1,\"isDie\":true}},{\"no\":34,\"uid\":17,\"role\":{\"roleType\":22,\"campType\":1,\"isDie\":true}},{\"no\":15,\"uid\":18,\"role\":{\"roleType\":1,\"campType\":1,\"isDie\":true}},{\"no\":3,\"uid\":19,\"role\":{\"roleType\":8,\"campType\":1,\"isDie\":true}},{\"no\":6,\"uid\":20,\"role\":{\"roleType\":21,\"campType\":2,\"isDie\":true}},{\"no\":23,\"uid\":21,\"role\":{\"roleType\":2,\"campType\":2,\"isDie\":true}},{\"no\":19,\"uid\":22,\"role\":{\"roleType\":1,\"campType\":1,\"isDie\":true}},{\"no\":11,\"uid\":23,\"role\":{\"roleType\":2,\"campType\":2,\"isDie\":true}},{\"no\":8,\"uid\":24,\"role\":{\"roleType\":9,\"campType\":1,\"isDie\":true}},{\"no\":2,\"uid\":25,\"role\":{\"roleType\":5,\"campType\":1,\"isDie\":true}},{\"no\":16,\"uid\":26,\"role\":{\"roleType\":5,\"campType\":1,\"isDie\":true}},{\"no\":24,\"uid\":27,\"role\":{\"roleType\":9,\"campType\":1,\"isDie\":true}},{\"no\":29,\"uid\":28,\"role\":{\"roleType\":5,\"campType\":1,\"isDie\":true}},{\"no\":13,\"uid\":29,\"role\":{\"roleType\":1,\"campType\":1,\"isDie\":true}},{\"no\":33,\"uid\":30,\"role\":{\"roleType\":3,\"campType\":2,\"isDie\":true}},{\"no\":22,\"uid\":31,\"role\":{\"roleType\":21,\"campType\":2,\"isDie\":true}},{\"no\":1,\"uid\":32,\"role\":{\"roleType\":15,\"campType\":1,\"isDie\":true}},{\"no\":28,\"uid\":33,\"role\":{\"roleType\":9,\"campType\":1,\"isDie\":true}},{\"no\":4,\"uid\":34,\"role\":{\"roleType\":17,\"campType\":1,\"isDie\":true}},{\"no\":31,\"uid\":35,\"role\":{\"roleType\":17,\"campType\":1,\"isDie\":true}},{\"no\":32,\"uid\":36,\"role\":{\"roleType\":11,\"campType\":1,\"isDie\":true}}]}","game_conf":"","interactive_panel_conf":"","timestamp":1680367540,"block_uids":null}}
{"cmd":"LIVE_OPEN_PLATFORM_GAME","data":{"msg_type":"panel_reset", "msg_sub_type":"panel_reset", "game_name":"XXXX","game_code":"16502xxxxxxxx","game_id":"XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX","game_status":"","game_msg":"","game_conf":"","interactive_panel_conf":"","timestamp":1672502400,"block_uids":null}}
{"cmd":"LIVE_OPEN_PLATFORM_GAME","data":{"msg_type":"panel_reset", "msg_sub_type":"panel_reset", "game_name":"XXXX","game_code":"16502xxxxxxxx","game_id":"XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX","game_status":"","game_msg":"","game_conf":"","interactive_panel_conf":"","timestamp":1672502400,"block_uids":null}}
{"cmd":"LIVE_OPEN_PLATFORM_GAME","data":{"msg_type":"game_end",    "msg_sub_type":"game_end",    "game_name":"XXXX","game_code":"16502xxxxxxxx","game_id":"XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX","game_status":"","game_msg":"","game_conf":"","interactive_panel_conf":"","timestamp":1672502400,"block_uids":[]}}
```
----
### room_admin_entrance
[TOP](#直播弹幕)  
设置房管 **小写**  
| key	| type	| value	|
|-|-|-|
| cmd		| str	| "room_admin_entrance" |
| dmscore	| obj	| 45 |
| level		| obj	| 1 |
| msg		| obj	| "系统提示：你已被主播设为房管" |
| uid		| obj	| uid |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
```json
{"cmd":"room_admin_entrance","dmscore":45,"level":1,"msg":"系统提示：你已被主播设为房管","uid":xxxx}
{"cmd":"room_admin_entrance","dmscore":45,"is_report":false,"level":1,"msg":"系统提示：你已被主播设为房管","msg_id":"xxx","send_time":1672502400000,"uid":xxxxx}
```
----
### ROOM_ADMINS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_ADMINS" |
| uids		| []num	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
```json
{"cmd":"ROOM_ADMINS","is_report":false,"msg_id":"xxx","send_time":1672502400000,"uids":[xxx,yyy]}
```
----
### ROOM_ADMIN_REVOKE
[TOP](#直播弹幕)  
移除房管
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_ADMIN_REVOKE" |
| msg		| str	| "撤销房管" |
| uid		| num	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
```json
{"cmd":"ROOM_ADMIN_REVOKE","msg":"撤销房管","uid":xxxx}
{"cmd":"ROOM_ADMIN_REVOKE","is_report":false,"msg":"撤销房管","msg_id":"xxx","send_time":1672502400000,"uid":xxxxx}
```
----
### MVROLECHANGE
[TOP](#直播弹幕)  
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "MVROLECHANGE" |
| data			| obj	| |
#### MVROLECHANGE__data
| key			| type	| value	|
|-|-|-|
| change_uid	| num	| uid |
| role			| num	| |
| room_id		| num	| 直播间id |
| ts			| num	| 当前时间TimeStamp(秒) 向上取整 |
```json
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":0,"room_id":12345,"ts":1672502400}}
```
----
### VOICE_CHAT_UPDATE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_CHAT_UPDATE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### VOICE_CHAT_UPDATE__data
| key	| type	| value	|
|-|-|-|
| url	| str	| |
```json
{"cmd":"VOICE_CHAT_UPDATE","data":{"url":"http://i0.hdslb.com/bfs/live/b7dd570ec64148efab2a97922bb2eebcc29473ca.jpg"},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### MESSAGEBOX_USER_GAIN_MEDAL
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_GAIN_MEDAL" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### MESSAGEBOX_USER_GAIN_MEDAL__data
| key	| type	| value	|
|-|-|-|
| day_limit				| num	| 每日上限 1500/250000 |
| fan_name				| str	| 昵称 |
| guard_level			| num	| 0 |
| highlight_color		| num	| |
| intimacy				| num	| [粉丝勋章进度](#medal__score) |
| is_lighted			| num	| 七天内在直播间有互动 |
| is_received			| num	| 1 |
| is_wear				| num	| 0 |
| medal_color			| num	| [color](#粉丝牌信息medal_info) |
| medal_color_border	| num	| [color](#粉丝牌信息medal_info) |
| medal_color_end		| num	| [color](#粉丝牌信息medal_info) |
| medal_color_start		| num	| [color](#粉丝牌信息medal_info) |
| medal_id				| num	| 粉丝团称号id |
| medal_level			| num	| 粉丝牌等级 |
| medal_name			| str	| 粉丝团称号 |
| msg_content			| str	| 获得`X`点亲密度\n你的粉丝勋章达到`Y`级 |
| msg_title				| str	| 恭喜你获得【`主播`】的粉丝勋章~ <br> 欢迎萌新~ |
| next_intimacy			| num	| 下一级所需经验 |
| normal_color			| num	| |
| toast					| str	| 成功入团并关注主播，得1级大礼包 <br> 大航海:恭喜您加入`主播`的粉丝团，并获得1级大礼包 |
| today_feed			| num	| 0 |
| type					| num	| 0: 1: 2:欢迎萌新 3:获得粉丝勋章 |
| uid					| num	| |
| up_uid				| num	| 主播uid |
```json
{"cmd":"MESSAGEBOX_USER_GAIN_MEDAL","data":{"day_limit":1500,"fan_name":"****","guard_level":0,"highlight_color":16478873,"intimacy":*,"is_lighted":1,"is_received":1,"is_wear":0,"medal_color":6067854,"medal_color_border":6067854,"medal_color_end":6067854,"medal_color_start":6067854,"medal_id":565763,"medal_level":3,"medal_name":"****","msg_content":"获得550点亲密度\n你的粉丝勋章达到3级","msg_title":"恭喜你获得【XXX】的粉丝勋章~","next_intimacy":500,"normal_color":7697781,"toast":"成功入团并关注主播，得1级大礼包","today_feed":0,"type":3,"uid":****,"up_uid":****},"is_report":false,"msg_id":"xxx","send_time":1672502400000}
```
----
### COMBO_SEND
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMBO_SEND" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### COMBO_SEND__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"COMBO_SEND","data":{"action":"投喂","batch_combo_id":"batch:gift:combo_id:x111111x:x222222x:x333333x:1672502400.9999","batch_combo_num":2,"combo_id":"gift:combo_id:x111111x:x222222x:31036:1672502400.9999","combo_num":2,"combo_total_coin":200,"dmscore":8,"gift_id":x333333x,"gift_name":"小花花","gift_num":0,"is_join_receiver":false,"is_naming":false,"is_show":1,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":0,"medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":0,"medal_name":"","special":"","target_id":0},"name_color":"","r_uname":"xxx","receive_user_info":{"uid":x222222x,"uname":"xxx"},"ruid":x222222x,"send_master":null,"total_num":2,"uid":x111111x,"uname":"yyy","wealth_level":2},"is_report":false,"msg_id":"1234567890abcdef","send_time":1688799309809}
{"cmd":"COMBO_SEND","data":{"action":"投喂","batch_combo_id":"batch:gift:combo_id:x111111x:x222222x:x333333x:1672502400.9999","batch_combo_num":3,"combo_id":"gift:combo_id:x111111x:x222222x:x333333x:1672502400.9999","combo_num":3,"combo_total_coin":300,"dmscore":8,"gift_id":x333333x,"gift_name":"小花花","gift_num":0,"is_join_receiver":false,"is_naming":false,"is_show":1,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":0,"medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":0,"medal_name":"","special":"","target_id":0},"name_color":"","r_uname":"xxx","receive_user_info":{"uid":x222222x,"uname":"xxx"},"ruid":x222222x,"send_master":null,"total_num":3,"uid":x111111x,"uname":"yyy","wealth_level":0},"is_report":false,"msg_id":"1234567890abcdef","send_time":1688802748421}
{"cmd":"COMBO_SEND","data":{"action":"投喂","batch_combo_id":"batch:gift:combo_id:x111111x:x222222x:x333333x:1672502400.9999","batch_combo_num":2,"combo_id":"gift:combo_id:x111111x:x222222x:x333333x:1672502400.9999","combo_num":2,"combo_total_coin":200,"dmscore":64,"gift_id":x333333x,"gift_name":"小花花","gift_num":0,"is_join_receiver":false,"is_naming":false,"is_show":1,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":1725515,"medal_color_border":12632256,"medal_color_end":12632256,"medal_color_start":12632256,"medal_level":21,"medal_name":"xxx","special":"","target_id":12345},"name_color":"","r_uname":"xxx","receive_user_info":{"uid":x222222x,"uname":"xxx"},"ruid":x222222x,"send_master":null,"total_num":2,"uid":x111111x,"uname":"yyy","wealth_level":0},"is_report":false,"msg_id":"1234567890abcdef","send_time":1688803159548}
```
----
### ANCHOR_ECOMMERCE_STATUS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_ECOMMERCE_STATUS" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_ECOMMERCE_STATUS__data
| key		| type	| value	|
|-|-|-|
| status	| num	| |
```json
{"cmd":"ANCHOR_ECOMMERCE_STATUS","data":{"status":1}}
{"cmd":"ANCHOR_ECOMMERCE_STATUS","data":{"status":1},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ADMIN_SHIELD_KEYWORD
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ADMIN_SHIELD_KEYWORD" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ADMIN_SHIELD_KEYWORD__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ADMIN_SHIELD_KEYWORD","data":{"action":1,"keyword":"text","name":"username","uid":12345},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ANCHOR_HELPER_DANMU
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_HELPER_DANMU" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ANCHOR_HELPER_DANMU__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |

| id | value |
|-|-|
|101029|新主播扶持规则|
|100855|航海回馈说明页面|
|||
```json
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"","button_platform":0,"button_target":"","msg":"XXX取消了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看>","button_platform":3,"button_target":"bililive://****","msg":"发起航海回馈更容易吸引粉丝开通大航海哦","platform":3,"report":"$uid","report_type":"live.live.guard","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看规则","button_platform":3,"button_target":"bililive://****","msg":"您正在新主播扶持中，良好的互动和直播封面，会帮你吸引观众","platform":3,"report":"$uid","report_type":"star_perception","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去看看","button_platform":3,"button_target":"bililive://****","msg":"本周开播满7有效天，必得****元奖励金！今天再收到******电池，即可+1天哦","platform":3,"report":"$uid","report_type":"weekly_task","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去领取","button_platform":3,"button_target":"bililive://****","msg":"本周开播满1天，恭喜获得***元奖励金。再播1天，再得***元奖励金","platform":3,"report":"$uid","report_type":"weekly_task_finish","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":1,"button_name":"去看看","button_platform":3,"button_target":"bililive://blink/open_voicelink","msg":"XXX申请了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### CARD_MSG
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CARD_MSG" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### CARD_MSG__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"CARD_MSG","data":{"card_data":{"arouse":600,"interval":3,"msg":"主播@你:被我抓到了，怎么还没关注我？","room_id":???,"source_event":3,"uid":xxx},"card_type":"daily_recommend"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"CARD_MSG","data":{"card_data":{"arouse":600,"interval":3,"msg":"快来关注我，下次直播不迷路~","room_id":???,"source_event":3,"uid":xxx},"card_type":"daily_recommend"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ROOM_KICKOUT
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_KICKOUT" |
| data		| obj	| |
| uname		| str	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ROOM_KICKOUT__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"key":"value"}
```
----
### USER_PANEL_RED_ALARM
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_PANEL_RED_ALARM" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### USER_PANEL_RED_ALARM__data
| key		| type	| value	|
|-|-|-|
| alarm_num	| num	| |
| module	| str	| |
```json
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"live_guard"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"room_gift_panel"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"panel_privilege"},"is_report":false,"msg_id":"xxx","send_time":xxx}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"user_head_dot"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### USER_INFO_UPDATE
[TOP](#直播弹幕)  
主播在其他人的直播间◯◯◯
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_INFO_UPDATE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### USER_INFO_UPDATE__data
| key		| type	| value	|
|-|-|-|
| room_id	| num	|  |
| type		| num	| |
| uid		| num	| 主播uid |
```json
{"cmd":"USER_INFO_UPDATE","data":{"room_id":xxx,"type":1,"uid":xxx},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### MESSAGEBOX_USER_MEDAL_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_MEDAL_CHANGE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### MESSAGEBOX_USER_MEDAL_CHANGE__data
| key					| type	| value	|
|-|-|-|
| guard_level			| num	| |
| is_lighted			| num	| |
| medal_color_border	| num	| |
| medal_color_end		| num	| |
| medal_color_start		| num	| |
| medal_level			| num	| |
| medal_name			| num	| |
| multi_unlock_level	| num	| ? |
| type					| num	| |
| uid					| num	| |
| unlock				| num	| |
| unlock_level			| num	| |
| up_uid				| num	| |
| upper_bound_content	| num	| |
```json
{"cmd":"MESSAGEBOX_USER_MEDAL_CHANGE","data":{"guard_level":xxx,"is_lighted":1,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_level":xxx,"medal_name":"xxx","multi_unlock_level":"","type":0,"uid":xxx,"unlock":0,"unlock_level":0,"up_uid":xxx,"upper_bound_content":""},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### WEALTH_NOTIFY
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WEALTH_NOTIFY" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### WEALTH_NOTIFY__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"WEALTH_NOTIFY","data":{"flag":3,"info":{"effect_key":1075,"has_items_changed":1,"level":28,"send_time":xxx,"status":1}},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
----
### ACTIVITY_BANNER_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ACTIVITY_BANNER_CHANGE" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ACTIVITY_BANNER_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ACTIVITY_BANNER_CHANGE","data":{"list":[{"action":"update","activity_title":"虚拟-三相 交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","position":"bottom","timestamp":1690283936}]},"is_report":false,"msg_id":"907048119175684","send_time":1690283936990}
{"cmd":"ACTIVITY_BANNER_CHANGE","data":{"list":[{"action":"update","activity_title":"虚拟-三相交 流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","position":"bottom","timestamp":1690283936}]},"is_report":false,"msg_id":"907048118127107","send_time":1690283936988}
{"cmd":"ACTIVITY_BANNER_CHANGE","data":{"list":[{"action":"update","activity_title":"虚拟-三相交 流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","position":"bottom","timestamp":1690283936}]},"is_report":false,"msg_id":"907048114466818","send_time":1690283936981}
```
----
### ACTIVITY_BANNER_CHANGE_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ACTIVITY_BANNER_CHANGE_V2" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### ACTIVITY_BANNER_CHANGE_V2__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
1690283937473032{"cmd":"ACTIVITY_BANNER_CHANGE_V2","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","ext_data":"","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","platform_info":[{"build":0,"condition":0,"platform":"android"},{"build":0,"condition":0,"platform":"ios"}],"position":"bottom","type":0}],"timestamp":1690283936},"is_report":false,"msg_id":"907048130714115","send_time":1690283937012}
1690283937612368{"cmd":"ACTIVITY_BANNER_CHANGE_V2","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","ext_data":"","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","platform_info":[{"build":0,"condition":0,"platform":"android"},{"build":0,"condition":0,"platform":"ios"}],"position":"bottom","type":0}],"timestamp":1690283936},"is_report":false,"msg_id":"907048129141253","send_time":1690283937009}
1690283936794723{"cmd":"ACTIVITY_BANNER_CHANGE_V2","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","ext_data":"","id":3065,"is_close":1,"jump_url":"https://www.bilibili.com/blackboard/live/activity-qMxJDCQ4kQ.html","platform_info":[{"build":0,"condition":0,"platform":"android"},{"build":0,"condition":0,"platform":"ios"}],"position":"bottom","type":0}],"timestamp":1690283936},"is_report":false,"msg_id":"907048130185729","send_time":1690283937011}
```
----
### SPREAD_SHOW_FEET_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SPREAD_SHOW_FEET_V2" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### SPREAD_SHOW_FEET_V2__data
| key 15		| type	| value	|
|-|-|-|
| click			| num	| |
| coin_cost		| num	| |
| coin_num		| num	| |
| cover_btn		| str	| |
| cover_url		| str	| |
| live_key		| str	| |
| order_id		| num	| |
| order_type	| num	| |
| plan_percent	| num	| 0~100 |
| show			| num	| |
| status		| num	| |
| timestamp		| num	| 秒 |
| title			| str	| |
| total_online	| num	| |
| uid			| num	| |
```json
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":117,"coin_cost":70,"coin_num":100,"cover_btn":"","cover_url":"","live_key":"","order_id":1768xxxx,"order_type":5,"plan_percent":70,"show":8819,"status":1,"timestamp":xxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxxx,"order_type":5,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxxx,"order_type":5,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":2,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":3,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":3,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":2,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx},"is_report":false,"msg_id":"xxx","send_time":xxxx}
```
----
### XXXXXXXXXXX
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "XXXXXXXXXXX" |
| data		| obj	| |
| is_report	| bool	| |
| msg_id	| str	| |
| send_time	| num	| |
#### XXXXXXXXXXX__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"key":"value"}
```

### others
[TOP](#直播弹幕)  
| key				| type	| value	| where	|
|-|-|-|-|
| guard_level		| num	| 舰长等级 <br> 0:无 <br> 1:总督GOVERNOR <br> 2:提督PREFECT <br> 3:舰长CAPTAIN |
| privilege_type	| num	| ！待确定 2:提督 3:舰长 |
| lot_status		| num	| 抽奖状态 0:开始 1:正在抽奖 2:开奖 |
| identities		| []num	| 身份 1:"Normal" 2:"管理员" 3:"粉丝" 4:"Vip" 5:"SVip" 6:"舰长" 7:"提督" 8:"总督" |[INTERACT_WORD](#INTERACT_WORD)[LIKE_INFO_V3_CLICK](#LIKE_INFO_V3_CLICK)[ENTRY_EFFECT](#ENTRY_EFFECT)

```js
face_frame={
	"舰长": "https://i0.hdslb.com/bfs/live/80f732943cc3367029df65e267960d56736a82ee.png",
	"提督": "https://i0.hdslb.com/bfs/live/09937c3beb0608e267a50ac3c7125c3f2d709098.png",
}
```

```js
//未知List
Entry=1	Follow=2	Share=3
Entry=1	Attention=2	Share=3	SpecialAttention=4	MutualAttention=5	Link=6
NORMAL_ROOM = 0	OFFICIAL_ROOM = 1	OFFICIAL_SUB_ROOM = 2
UNSTART = 1	WILL_START_30_SECONDS = 2	START = 3	WILL_END_30_SECONDS = 4	WILL_END_10_SECONDS = 5	END = 6	END_ALL = 7	QUALIFICATION_OFFLINE_EXCEPTION = 8	OFFLINE_EXCEPTION = 9
UNKNOW = 0	PLAYING = 1	PERFORMED = 2	UPCOMING_SHOW = 3
LIVE = "直播"	ROUND = "轮播"	PREPARING = "闲置"
GiftAnimation=0	SuperGift=1	LotteryDanmaku=2	Notice=3	buffCard=4	SuperChat=5	EntryInfo=6	EmojiAnimation=7	EmojiDanmaku=8
normal=1	giftLottery=2	guardLottery=3	guardWelcome=4	giftLotteryResult=5	highEnergy=6	no1=7	notSide=8	chaosPk=9
backgroundTask=1
Normal=0	Meteor=1	Moon=2	Pk=3
Web=1	Android=2	Ios=3	H5=4
controlGroup = 0	experimentalGroup = 1
normal=0	lucky=1	chaosPKScore=2	chaosPKImmune=3	chaosPKBoom=4
noEffect=0	player=1	fullScreenAnimation=2	medal=3
guard-1 = 1 guard-2 = 2	guard-3=3
normal = 0	zong = 1	ti = 2	jian = 3
navigate = 0	reload = 1	backForward = 2	other = 255
Other=0	Mac=1	Windows=2	Unix=3	Linux=4
notStart=0	inProcess=1	end=2
like=1	unlike=2
normal = 1	giftLottery = 2	guardLottery = 3	guardWelcome = 4	giftLotteryResult = 5	highEnergy = 6
HOST = 0	FIRST = 1	SECOND = 2	THIRD = 3	FOURTH = 4	FIFTH = 5	SIXTH = 6	SEVENTH = 7	EIGHTH = 8
left = 0	right = 1
normal=0	month=1	year=2
random=1	again=2	force=3
PK_PRE=200	PK_START=300	PK_END=400	PK_AGAIN=400	PK_SETTLE=400	PK_PROCESS=300	PK_MATCH=100	PK_MIC_END=2044	PK_CLICK_AGAIN=400
noGame=0	inProgress=1	end=2
pre=0	process=1	lastMinute=2	end=3	freeze=4	punish=5	lastMinuteFreeze=6	lastMinuteEnd=7	videoPunish=8
pre=0	start=1	process=2	changeType=3	end=4	settle=5	sendGift=6	buffer=7	triggerBoom=8	punish=9	settleNew=10	finalHit=11	videoPunishBegin=12	videoPunishEnd=13
normal=0	immune=1	kill=2	beKill=3
normal=0	antiBoom=1
none=0	draw=1	win=2	fail=3	passive=-10
none=0	draw=1	win=2	fail=-1	passive=-10
chaosPK=1	videoChasoPK=2	videoPK=6
CAPTAIN = 3	PREFECT = 2	GOVERNOR = 1
Open = 3	Off = 2	On = 1
ACTIVITY = 3	GIFT = 1	ABILITY = 2
guardZong=1	guardTi=2	weekAllAreaTop1=3	weekSubAreaTop1=4
HeavensChoice=1	RedEnvelope=2
default = 0	isMultiVoiceNotOfficialChannel = 1	notMultiVoiceIsOfficialChannel = 2	isMultiVoiceIsOfficialChannel = 3
normal=0	community=1	top=2	special=3	silver=4
PACKAGE = -1	CHARGE = -3
NORMAL = 0	WEBFUllSCREEN = 1	WINDOWFULLSCREEN = 2
LOAD_WASM_FAIL = 1	NOT_SUPPORT_WASM = 2	WATCH_TRACKER_ERROR = 3	ENTER_FAIL = 10	HEARTBEAT_FAIL = 11
other=0	"2g"=2	"3g"=3	"4g"=4
process=0	draw=1	win=2	fail=3
successfulMatch = 100	preparing = 200	processing = 300	punishing = 400	again = 400	normalEnd = 1e3	breakOffEnd = 1100	escapeEnd = 1200	errorEnd = 1300
stoped = 0	stoping = 1	started = 2
NotExpired=0	WillExpired=1	JustExpired=2	HasExpired=3
LivePage = 0	BlancLivePage = 1	PlayerPage = 2	SpacePage = 3
SHOW = 0	NOTSHOW = 1
UN_APPLY = 1	WAITING = 2	PLAYING = 3
NotWin = -2	NotStart = -1	CanDraw = 0	JoinNotDraw = 1	JoinAndWin = 2	NotJoinButDrawn = 3	JoinAndNowDrawn = 4
```

```
face:http(s)?://[is][0-3].hdslb.com/bfs/((face|baselabs)/[0-9a-f]{40}.(jpg|png|gif|webp)|face/member/noface\.jpg)
for i in range(1,len(a)):print(str(a[i]-a[i-1])[0:4])
(\d{10}\.\d{1,3}|\d{16,17})?\{"cmd":[ ]{0,1}"XXXXXXXXXX",.{1,}\n
(\d{16,})?\{("business_id":".{0,11}",)?"cmd":"XXXXXXXXXX",.{1,}\n
```

### 粉丝牌信息medal_info
| key					| type		| value	| 备注 |
|-|-|-|-|
| anchor_roomid			| num		| 主播 短直播间ID | 
| anchor_uname			| str		| 主播昵称 | 
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
