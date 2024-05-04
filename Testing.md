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
| ~~14~~	| ~~?int64~~	| ~~usermid~~		| ~~发送者mid~~ |
| 15	| ?int??	| *likes*		| 点赞数量 |
| 16	| ?int??	| ~~test16~~	| 弹幕回复，默认为 0 `first:2021-08-07` |
| 17	| ?int??	| ~~test17~~	| 弹幕回复，默认为 0 `last: 2022-09-05` |
| 18	| ?int??	| *reply_count*	| 弹幕回复数量 |
| 19	| ?			| ~~test19~~	| ? |
| ~~20~~	| ~~string~~	| ~~test20~~	| 弹幕回复，默认为str:"0" |
| ~~21~~	| ~~string~~	| ~~test21~~	| 弹幕回复，默认为str:"0" |
| 22	| string	| animation		| json |
| 23	| ?			| ~~test23~~	| ? |
| 24	| uint64	| colorful		| 彩色弹幕 |

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
	"text": "[ohh]",
	"weight": 10,	// 10
	"action": "picture:i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png?scale=1.00",
	"attr": 256,
	"animation": "{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png\",\"scale\":1}"
},
{
	"text":"[前方高能]",
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
### DmColorful
| id	| type	|
|||
| 0		| None	|
| 60001	| VipGradualColor |

```json
// VipGradualColor
{"fill_color":"http://i0.hdslb.com/bfs/dm/9dcd329e617035b45d2041ac889c49cb5edd3e44.png","stroke_color":"http://i0.hdslb.com/bfs/dm/716a749b2461e02df0b4dafb59bbaf0ceab79da9.png"}
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
| upower_jump_url		| str	| true: f"https://www.XXXX.com/h5/upower/detail?mid={uid}u0026navhide=1u0026prePage=danmu" <br> false: "" |?`\\u0026` `\u0026`
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
| jump_url				| str	|  -1,0,2: --> `upower_jump_url` <br> 1: f"https://www.XXXX.com/h5/upower/detail?mid={uid}u0026navhide=1u0026prePage=danmu" |
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
| posX	*				| float	| |
| posY	*				| float	| |
| posX_2	*			| num	| |
| posY_2	*			| num	| |
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
| dmids					| []num	| [dmid] |
| duration				| num	| 65000 |
| icon					| str	| [url][url_03] |
| grades				| []obj	| |
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
| reserve_state			| num	| 0/1 |
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
```json
{"msg":"直播预约：冰火歌会2023冰火夏日夜","reserve_type":2,"reserve_id":1646044,"live_stime":1691233200,"arc_stime":1691233200,"stime":1691233200,"posX":193.43,"posY":251.25,"posX_2":29,"posY_2":67,"duration":5000,"icon":"http://i0.hdslb.com/bfs/b/4312fb7b155646fc6fd5f6f8a6a07a062d82587c.png","reserve_count":125988,"reserve_state":0,"user_state":false,"live_state":0,"premiere_state":0,"live_popularity_count":0,"live_popularity_str":"","premiere_online_count":0,"premiere_view":0,"jump_url":"","mid":9617619,"live_stime_format":"今天19:00","arc_stime_format":"今天19:00","stime_format":"今天19:00","live_lottery":true,"desc":"","shrink_icon":"http://i0.hdslb.com/bfs/b/a4b1c7f03e687f680f7c3629c530e3fdd77d63ed.png","shrink_title":"预约","show_status":0}
```

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
|| CMD | 备注 |
|-|-|-|
| [❌](#ACTIVITY_MATCH_GIFT)						| ACTIVITY_MATCH_GIFT					| |
| [✅](#ACTIVITY_BANNER_CHANGE)					| ACTIVITY_BANNER_CHANGE				| |
| [✅](#ACTIVITY_BANNER_CHANGE_V2)				| ACTIVITY_BANNER_CHANGE_V2				| |
| [✅](#ADMIN_SHIELD_KEYWORD)					| ADMIN_SHIELD_KEYWORD					| |
| [⁉](#ANCHOR_BROADCAST)						| ANCHOR_BROADCAST						| |
| [✅](#ANCHOR_ECOMMERCE_STATUS)					| ANCHOR_ECOMMERCE_STATUS				| |
| [✅](#ANCHOR_HELPER_DANMU)						| ANCHOR_HELPER_DANMU					| |
| [✅](#ANCHOR_LOT_CHECKSTATUS)					| ANCHOR_LOT_CHECKSTATUS				| 抽奖：检查 |
| [✅](#ANCHOR_LOT_START)						| ANCHOR_LOT_START						| 抽奖：开始 |
| [✅](#ANCHOR_LOT_END)							| ANCHOR_LOT_END						| 抽奖：结束 |
| [✅](#ANCHOR_LOT_AWARD)						| ANCHOR_LOT_AWARD						| 抽奖：结果 |
| [✅](#ANCHOR_NORMAL_NOTIFY)					| ANCHOR_NORMAL_NOTIFY					||
| [✅](#AREA_RANK_CHANGED)						| AREA_RANK_CHANGED						| ~~主播：直播分区更改~~ |
| [✅](#BENEFIT_CARD_CLEAN)						| BENEFIT_CARD_CLEAN					| |
| [❌](#BOX_ACTIVITY_START)						| BOX_ACTIVITY_START					| |
| [❌](#BIG_R_WELCOME)							| BIG_R_WELCOME							| |
| [✅](#CARD_MSG)								| CARD_MSG								| |
| [✅](#CHANGE_ROOM_INFO)						| CHANGE_ROOM_INFO						| WEB:更改直播间背景 |
| [❌](#CHASE_FRAME_SWITCH)						| CHASE_FRAME_SWITCH					| |
| [✅](#COMBO_END)								| COMBO_END								| |
| [✅](#COMBO_SEND)								| COMBO_SEND							| 送礼物：连击 |
| [✅](#COMMON_NOTICE_DANMAKU)					| COMMON_NOTICE_DANMAKU					| 弹幕区域：弹幕区通知 |
| [✅](#CUT_OFF)									| CUT_OFF								| 切断直播！ **服务端可能不会发送此消息** |
| [✅](#DANMU_AGGREGATION)						| DANMU_AGGREGATION						| 通知栏：抽奖通知 |
| [✅](#DANMU_ACTIVITY_CONFIG)					| DANMU_ACTIVITY_CONFIG					| |
| [❌](#DANMU_GIFT_LOTTERY_AWARD)				| DANMU_GIFT_LOTTERY_AWARD				| |
| [❌](#DANMU_GIFT_LOTTERY_END)					| DANMU_GIFT_LOTTERY_END				| |
| [❌](#DANMU_GIFT_LOTTERY_START)				| DANMU_GIFT_LOTTERY_START				| |
| [✅](#DANMU_MSG)								| DANMU_MSG								| 弹幕 |
| [✅](#DANMU_MSG371111)							| DANMU_MSG371111						| 弹幕: | |
| [❌](#DANMU_TAG_CHANGE)						| DANMU_TAG_CHANGE						| |
| [✅](#DM_INTERACTION)							| DM_INTERACTION						| 互动弹幕（投票、他们都在说） |
| [✅](#ENTRY_EFFECT)							| ENTRY_EFFECT							| 进入直播间特效 |
| [✅](#ENTRY_EFFECT)							| ENTRY_EFFECT_MUST_RECEIVE				| 进入直播间特效 |
| [✅](#FULL_SCREEN_SPECIAL_EFFECT)				| FULL_SCREEN_SPECIAL_EFFECT			| |
| [✅](#GIFT_BOARD_RED_DOT)						| GIFT_BOARD_RED_DOT					| |
| [✅](#GIFT_PANEL_PLAN)							| GIFT_PANEL_PLAN						| |
| [✅](#GIFT_STAR_PROCESS)						| GIFT_STAR_PROCESS						| 礼物星球：进度 |
| [✅](#GOTO_BUY_FLOW)							| GOTO_BUY_FLOW							| 移动端 购买 |
| [✅](#GUARD_ACHIEVEMENT_ROOM)					| GUARD_ACHIEVEMENT_ROOM				| 恭喜主播xxx舰队规模突破xxx |
| [❌](#GUARD_BENEFIT_RECEIVE)					| GUARD_BENEFIT_RECEIVE					| |
| [✅](#GUARD_BUY)								| GUARD_BUY								| 大航海购买(旧) |
| [✅](#GUARD_LEADER_NOTICE)						| GUARD_LEADER_NOTICE					| 舰队指挥官 |
| [✅](#GUARD_HONOR_THOUSAND)					| GUARD_HONOR_THOUSAND					| 千舰 **广播** |
| [❌](#GUARD_LOTTERY_START)						| GUARD_LOTTERY_START					| |
| [❌](#GUARD_WINDOWS_OPEN)						| GUARD_WINDOWS_OPEN					| |
| [✅](#HOT_BUY_NUM)								| HOT_BUY_NUM							| 移动端：购物 |
| 🗑	| HOT_RANK_CHANGED_V2					| [热门榜功能下线公告]|
| 🗑	| HOT_RANK_CHANGED						| [热门榜功能下线公告]|
| 🗑	| HOT_RANK_SETTLEMENT_V2				| [热门榜功能下线公告]|
| 🗑	| HOT_RANK_SETTLEMENT					| [热门榜功能下线公告]|
| [✅](#HOT_ROOM_NOTIFY)							| HOT_ROOM_NOTIFY						| |
| [❌](#HOUR_RANK_AWARDS)						| HOUR_RANK_AWARDS 						| |
| [❌](#HOT_RANK_CHANGED_V2)						| HOT_RANK_CHANGED_V2 					| |
| [❌](#HOT_RANK_SETTLEMENT_V2)					| HOT_RANK_SETTLEMENT_V2 				| |
| [✅](#INTERACT_JOIN_OLD)						| INTERACT_JOIN_OLD						| |
| [✅](#INTERACT_JOIN)							| INTERACT_JOIN							| |
| [⁉](#INTERACT_OPERATION)						| INTERACT_OPERATION					| |
| [✅](#INTERACT_WORD)							| INTERACT_WORD							| 通知栏：进入直播间/关注主播 |
| [✅](#INTERACTIVE_USER)						| INTERACTIVE_USER						| |
| [✅](#LIKE_INFO_V3_CLICK)						| LIKE_INFO_V3_CLICK					| 移动端：点赞 |
| [❌](#LIKE_INFO_V3_NOTICE)						| LIKE_INFO_V3_NOTICE					| 点赞：xxxx |
| [✅](#LIKE_INFO_V3_UPDATE)						| LIKE_INFO_V3_UPDATE					| 状态栏：点赞更新 |
| [❌](#LIKE_SO_HOT)								| LIKE_SO_HOT 							| |
| [✅](#LITTLE_MESSAGE_BOX)						| LITTLE_MESSAGE_BOX					| 提示弹窗，仅用户本人 |
| [✅](#LITTLE_TIPS)								| LITTLE_TIPS 							| 提示弹窗，仅用户本人 |
| [✅](#LIVE)									| LIVE									| 开始直播/主播断流重连 |
| [✅](#LIVE_INTERACTIVE_GAME)					| LIVE_INTERACTIVE_GAME					| 游戏@ |
| [✅](#LIVE_INTERACT_GAME_STATE_CHANGE)			| LIVE_INTERACT_GAME_STATE_CHANGE		| 游戏@ |
| [❌](#LIVE_INTERNAL_ROOM_LOGIN)				| LIVE_INTERNAL_ROOM_LOGIN				| |
| [✅](#LIVE_MULTI_VIEW_CHANGE)					| LIVE_MULTI_VIEW_CHANGE				| |
| [✅](#LIVE_MULTI_VIEW_NEW_INFO)				| LIVE_MULTI_VIEW_NEW_INFO				| 直播多视角 |
| [❌](#LIVE_OPEN_PLATFORM_CLOUD_GAME)			| LIVE_OPEN_PLATFORM_CLOUD_GAME			| |
| [✅](#LIVE_OPEN_PLATFORM_GAME)					| LIVE_OPEN_PLATFORM_GAME				| 弹幕互动游戏 |
| [✅](#LIVE_PANEL_CHANGE_CONTENT)				| LIVE_PANEL_CHANGE_CONTENT				| |
| [✅](#LIVE_PANEL_CHANGE)						| LIVE_PANEL_CHANGE						| |
| [❌](#LIVE_PANEL_ICON_INFO)					| LIVE_PANEL_ICON_INFO					| |
| [❌](#LIVE_PLAYER_LOG_RECYCLE)					| LIVE_PLAYER_LOG_RECYCLE				| |
| [✅](#LIVE_ROOM_TOAST_MESSAGE)					| LIVE_ROOM_TOAST_MESSAGE				| |
| [✅](#LOG_IN_NOTICE)							| LOG_IN_NOTICE							| 游客保护 |
| [✅](#LIKE_GUIDE_USER)							| LIKE_GUIDE_USER						| |
| [❌](#LOL_ACTIVITY)							| LOL_ACTIVITY							| |
| [❌](#MATCH_TEAM_GIFT_RANK)					| MATCH_TEAM_GIFT_RANK					| |
| [✅](#MESSAGEBOX_USER_GAIN_MEDAL)				| MESSAGEBOX_USER_GAIN_MEDAL			| |
| [✅](#MESSAGEBOX_USER_MEDAL_CHANGE)			| MESSAGEBOX_USER_MEDAL_CHANGE			| 粉丝牌升级 |
| [❌](#MESSAGEBOX_USER_MEDAL_COMPENSATION)		| MESSAGEBOX_USER_MEDAL_COMPENSATION	| |
| [❌](#MILESTONE_UPDATE_EVENT)					| MILESTONE_UPDATE_EVENT 				| |
| [✅](#MULTI_VOICE_APPLICATION_ANCHOR)			| MULTI_VOICE_APPLICATION_ANCHOR		| |
| [✅](#MULTI_VOICE_APPLICATION_USER)			| MULTI_VOICE_APPLICATION_USER			| |
| [✅](#MULTI_VOICE_ENTER_ANCHOR)				| MULTI_VOICE_ENTER_ANCHOR				| |
| [✅](#MULTI_VOICE_OPERATIN)					| MULTI_VOICE_OPERATIN					| |
| [✅](#MULTI_VOICE_OWNER_LEAVE)					| MULTI_VOICE_OWNER_LEAVE				| |
| [❌](#MULTI_VOICE_PK_HAT_STATUS)				| MULTI_VOICE_PK_HAT_STATUS				| |
| [✅](#MULTI_VOICE_PK_STATUS)					| MULTI_VOICE_PK_STATUS					| |
| [✅](#MULTI_VOICE_STATUS_SYNC_ANCHOR)			| MULTI_VOICE_STATUS_SYNC_ANCHOR		| |
| [❌](#MULTI_VOICE_STATUS_SYNC)					| MULTI_VOICE_STATUS_SYNC				| |
| [✅](#MVROLECHANGE)							| MVROLECHANGE							| |
| [❌](#NEW_PK_REJECT)							| NEW_PK_REJECT							| |
| [✅](#NEW_PK_START)							| NEW_PK_START							| |
| [✅](#NOTICE_MSG)								| NOTICE_MSG							| 滚动横幅 |
| [✅](#OBS_SHIELD_STATUS_UPDATE)				| OBS_SHIELD_STATUS_UPDATE				| |
| [✅](#OFFICIAL_ROOM_EVENT)						| OFFICIAL_ROOM_EVENT					| |
| [✅](#ONLINE_RANK_COUNT)						| ONLINE_RANK_COUNT						| 状态栏：在线观众 |
| [✅](#ONLINE_RANK_TOP3)						| ONLINE_RANK_TOP3						| 高能榜：高能用户前三恭喜 |
| [✅](#ONLINE_RANK_V2)							| ONLINE_RANK_V2						| 高能榜：高能用户TOP7 |
| [✅](#PANEL_INTERACTIVE_NOTIFY_CHANGE)			| PANEL_INTERACTIVE_NOTIFY_CHANGE		| |
| [❌](#PK_AGAIN)								| PK_AGAIN								| |
| [❌](#PK_BATTLE_ABNORMAL)						| PK_BATTLE_ABNORMAL					| |
| [❌](#PK_BATTLE_CRIT)							| PK_BATTLE_CRIT						| |
| [✅](#PK_BATTLE_END)							| PK_BATTLE_END							| PK@ |
| [✅](#PK_BATTLE_ENTRANCE)						| PK_BATTLE_ENTRANCE					| PK@ |
| [✅](#PK_BATTLE_FINAL_PROCESS)					| PK_BATTLE_FINAL_PROCESS				| PK@ |
| [❌](#PK_BATTLE_GIFT)							| PK_BATTLE_GIFT						| |
| [✅](#PK_BATTLE_MATCH_TIMEOUT)					| PK_BATTLE_MATCH_TIMEOUT				| PK@ |
| [✅](#PK_BATTLE_PRE)							| PK_BATTLE_PRE							| PK@ |
| [✅](#PK_BATTLE_PRE_NEW)						| PK_BATTLE_PRE_NEW						| PK@ |
| [❌](#PK_BATTLE_PRO_TYPE)						| PK_BATTLE_PRO_TYPE					| |
| [✅](#PK_BATTLE_PROCESS_NEW)					| PK_BATTLE_PROCESS						| PK@ |
| [✅](#PK_BATTLE_PROCESS_NEW)					| PK_BATTLE_PROCESS_NEW					| PK@ |
| [✅](#PK_BATTLE_PUNISH_END)					| PK_BATTLE_PUNISH_END					| PK@ |
| [❌](#PK_BATTLE_RANK_CHANGE)					| PK_BATTLE_RANK_CHANGE					| |
| [❌](#PK_BATTLE_SETTLE_NEW)					| PK_BATTLE_SETTLE_NEW					| PK@ |
| [✅](#PK_BATTLE_SETTLE_USER)					| PK_BATTLE_SETTLE_USER					| PK@ |
| [✅](#PK_BATTLE_SETTLE_V2)						| PK_BATTLE_SETTLE_V2					| PK@ |
| [✅](#PK_BATTLE_SETTLE)						| PK_BATTLE_SETTLE						| PK@ |
| [❌](#PK_BATTLE_GIFT)							| PK_BATTLE_SPECIAL_GIFT				| |
| [✅](#PK_BATTLE_START_NEW)						| PK_BATTLE_START						| PK@ |
| [✅](#PK_BATTLE_START_NEW)						| PK_BATTLE_START_NEW					| PK@ |
| [✅](#PK_BATTLE_VIDEO_PUNISH_BEGIN)			| PK_BATTLE_VIDEO_PUNISH_BEGIN			| PK@ |
| [✅](#PK_BATTLE_VIDEO_PUNISH_END)				| PK_BATTLE_VIDEO_PUNISH_END			| PK@ |
| [❌](#PK_BATTLE_VOTES_ADD)						| PK_BATTLE_VOTES_ADD					| |
| [❌](#PK_END)									| PK_END								| |
| [❌](#PK_LOTTERY_START)						| PK_LOTTERY_START						| |
| [❌](#PK_MATCH)								| PK_MATCH								| |
| [❌](#PK_MIC_END)								| PK_MIC_END							| |
| [❌](#PK_PRE)									| PK_PRE								| |
| [❌](#PK_PROCESS)								| PK_PROCESS							| |
| [❌](#PK_SETTLE)								| PK_SETTLE								| |
| [❌](#PK_START)								| PK_START								| |
| [✅](#PLAYTOGETHER_ICON_CHANGE)				| PLAYTOGETHER_ICON_CHANGE				| |
| [✅](#PLAY_TAG)								| PLAY_TAG								| LOL 比赛：事件 |
| [❌](#PLAY_TOGETHER)							| PLAY_TOGETHER							| |
| [✅](#POPULAR_RANK_CHANGED)					| POPULAR_RANK_CHANGED					| 排行榜 |
| [✅](#POPULAR_RANK_GUIDE_CARD)					| POPULAR_RANK_GUIDE_CARD				| 排行榜 |
| [✅](#POPULARITY_RED_POCKET_NEW)				| POPULARITY_RED_POCKET_NEW				| 人气红包 new(抽奖) |
| [✅](#POPULARITY_RED_POCKET_V2_NEW)			| POPULARITY_RED_POCKET_V2_NEW			| 人气红包 new(抽奖) |
| [✅](#POPULARITY_RED_POCKET_START)				| POPULARITY_RED_POCKET_START			| 人气红包 抽奖开始 |
| [✅](#POPULARITY_RED_POCKET_V2_START)			| POPULARITY_RED_POCKET_V2_START		| 人气红包 抽奖开始 |
| [✅](#POPULARITY_RED_POCKET_WINNER_LIST)		| POPULARITY_RED_POCKET_WINNER_LIST		| 人气红包 抽奖结果 |
| [✅](#POPULARITY_RED_POCKET_V2_WINNER_LIST)	| POPULARITY_RED_POCKET_V2_WINNER_LIST	| 人气红包 抽奖结果 |
| [✅](#PREPARING)								| PREPARING								| 结束直播 |
| [✅](#room_admin_entrance)						| room_admin_entrance					| |
| [❌](#RAFFLE_END)								| RAFFLE_END							| |
| [❌](#RAFFLE_START)							| RAFFLE_START							| |
| [✅](#RANK_REM)								| RANK_REM								| |
| [✅](#RECOMMEND_CARD)							| RECOMMEND_CARD						| 商品推销(移动端) |
| [✅](#RING_STATUS_CHANGE)						| RING_STATUS_CHANGE					| |
| [✅](#RING_STATUS_CHANGE_V2)					| RING_STATUS_CHANGE_V2					| |
| [❌](#RED_POCKET_START)						| RED_POCKET_START						| |
| [❌](#REDIRECT_EMPTY_PAGE)						| REDIRECT_EMPTY_PAGE					| |
| [✅](#REENTER_LIVE_ROOM)						| REENTER_LIVE_ROOM						| |
| [❌](#Revenue_PayLimit)						| Revenue_PayLimit						| |
| [✅](#ROOM_ADMINS)								| ROOM_ADMINS							| |
| [✅](#ROOM_ADMIN_REVOKE)						| ROOM_ADMIN_REVOKE						| |
| [✅](#WIDGET_BANNER)							| ROOM_BANNER							| |
| [❌](#ROOM_BLOCK_INTO)							| ROOM_BLOCK_INTO						| |
| [✅](#ROOM_BLOCK_MSG)							| ROOM_BLOCK_MSG						| 用户封禁 |
| [✅](#ROOM_CHANGE)								| ROOM_CHANGE							| 直播信息更改 |
| [❌](#ROOM_KICKOUT)							| ROOM_KICKOUT							| |
| [❌](#ROOM_LIMIT)								| ROOM_LIMIT							| |
| [✅](#ROOM_LOCK)								| ROOM_LOCK								| |
| [✅](#ROOM_NEWS_AUDIT_CHANGE)					| ROOM_NEWS_AUDIT_CHANGE				| |
| [✅](#ROOM_NEWS_UPDATE)						| ROOM_NEWS_UPDATE						| |
| [❌](#ROOM_RANK)								| ROOM_RANK								| |
| [✅](#ROOM_REAL_TIME_MESSAGE_UPDATE)			| ROOM_REAL_TIME_MESSAGE_UPDATE			| 当前粉丝团人数，关注人数 |
| [❌](#ROOM_REFRESH)							| ROOM_REFRESH							| |
| [✅](#ROOM_SILENT)								| ROOM_SILENT_OFF/ROOM_SILENT_ON		| 直播间全局禁言 |
| [✅](#ROOM_SKIN_MSG)							| ROOM_SKIN_MSG							| 直播间背景 |
| [✅](#SEND_GIFT)								| SEND_GIFT								| 送礼物 |
| [✅](#SEND_GIFT_V2)							| SEND_GIFT_V2							| |
| [❌](#SEND_TOP)								| SEND_TOP								| |
| [✅](#SHOPPING_BUBBLES_STYLE)					| SHOPPING_BUBBLES_STYLE				| ？购物车 |
| [✅](#SHOPPING_CART_SHOW)						| SHOPPING_CART_SHOW					| ？购物车 |
| [✅](#SPECIAL_GIFT)							| SPECIAL_GIFT							| 特殊礼物 |
| [✅](#SPREAD_ORDER)							| SPREAD_ORDER							| |
| [✅](#SPREAD_SHOW_FEET_V2)						| SPREAD_SHOW_FEET_V2					| |
| [❌](#STARLIVE_PK_MSG)							| STARLIVE_PK_MSG						| |
| [✅](#STUDIO_ROOM_CLOSE)						| STUDIO_ROOM_CLOSE						| |
| [✅](#STOP_LIVE_ROOM_LIST)						| STOP_LIVE_ROOM_LIST					| |
| [❌](#SUPER_CHAT_AUDIT)						| SUPER_CHAT_AUDIT						| |
| [✅](#SUPER_CHAT_ENTRANCE)						| SUPER_CHAT_ENTRANCE					| SuperChat@ |
| [✅](#SUPER_CHAT_MESSAGE)						| SUPER_CHAT_MESSAGE					| SuperChat |
| [✅](#SUPER_CHAT_MESSAGE_DELETE)				| SUPER_CHAT_MESSAGE_DELETE				| SuperChat 删除 |
| [✅](#SUPER_CHAT_MESSAGE_JPN)					| SUPER_CHAT_MESSAGE_JPN				| SuperChat 日本語 |
| [✅](#SYS_MSG)									| SYS_MSG								| |
| [❌](#THERMAL_STORM_DANMU_BEGIN)				| THERMAL_STORM_DANMU_BEGIN				| |
| [❌](#THERMAL_STORM_DANMU_OVER)				| THERMAL_STORM_DANMU_CANCEL			| |
| [❌](#THERMAL_STORM_DANMU_OVER)				| THERMAL_STORM_DANMU_OVER				| |
| [❌](#THERMAL_STORM_DANMU_UPDATE)				| THERMAL_STORM_DANMU_UPDATE			| |
| [✅](#TRADING_SCORE)							| TRADING_SCORE							| |
| [❌](#TV_END)									| TV_END								| |
| [❌](#TV_START)								| TV_START								| |
| [✅](#UNIVERSAL_EVENT_GIFT)					| UNIVERSAL_EVENT_GIFT					| |
| [✅](#USER_INFO_UPDATE)						| USER_INFO_UPDATE						| |
| [✅](#USER_PANEL_RED_ALARM)					| USER_PANEL_RED_ALARM					| |
| [❌](#USER_TITLE_GET)							| USER_TITLE_GET						| |
| [✅](#USER_TOAST_MSG)							| USER_TOAST_MSG						| 大航海购买(新) |
| [❌](#USER_VIRTUAL_MVP)						| USER_VIRTUAL_MVP						| |
| [❌](#VIDEO_CONNECTION_JOIN_END)				| VIDEO_CONNECTION_JOIN_END				| |
| [❌](#VIDEO_CONNECTION_JOIN_START)				| VIDEO_CONNECTION_JOIN_START			| |
| [❌](#VIDEO_CONNECTION_MSG)					| VIDEO_CONNECTION_MSG					| |
| [✅](#VOICE_CHAT_UPDATE)						| VOICE_CHAT_UPDATE						| 移动端：聊天电台-视频背景 |
| [✅](#VOICE_JOIN_LIST)							| VOICE_JOIN_LIST						| 语音：连麦 |
| [✅](#VOICE_JOIN_ROOM_COUNT_INFO)				| VOICE_JOIN_ROOM_COUNT_INFO			| 语音：连麦排队 |
| [✅](#VOICE_JOIN_STATUS)						| VOICE_JOIN_STATUS						| 语音：连麦 |
| [❌](#VTR_GIFT_LOTTERY)						| VTR_GIFT_LOTTERY						| |
| [✅](#WARNING)									| WARNING								| 警告 |
| [❌](#WATCH_LPL_EXPIRED)						| WATCH_LPL_EXPIRED						| |
| [✅](#WATCHED_CHANGE)							| WATCHED_CHANGE						| 观看人数 |
| [✅](#WEALTH_NOTIFY)							| WEALTH_NOTIFY							| |
| [❌](#WIDGET_BANNER)							| WIDGET_BANNER							| |
| [✅](#WIDGET_GIFT_STAR_PROCESS)				| WIDGET_GIFT_STAR_PROCESS				| 礼物星球@ |
| [✅](#WIDGET_WISH_LIST)						| WIDGET_WISH_LIST						| |
| [❌](#WIN_ACTIVITY)							| WIN_ACTIVITY							| |
| [❌](#WIN_ACTIVITY_USER)						| WIN_ACTIVITY_USER						| |
----
----
### LOG_IN_NOTICE
[TOP](#直播弹幕)  
文档更新：2024-02-17  
```json
{
	"cmd":"LOG_IN_NOTICE",
	"data":{
		"notice_msg":"为保护用户隐私，未登录无法查看他人昵称",// 包括头像和uid
		"image_web":"http://i0.hdslb.com/bfs/dm/75e7c16b99208df259fe0a93354fd3440cbab412.png",
		"image_app":"http://i0.hdslb.com/bfs/dm/b632f7dcd3acf47deffb5f9ccc9546ae97a3415b.png"
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
{"cmd":"WARNING","roomid":xxx,"msg":"..."}
"因版权原因，请立即调整"
"图片内容不适宜，请立即调整"
"禁止在直播间内展示平台外的评论、弹幕内容，请立即调整"
"违反直播分区规范，请立即更换至游戏区"
"禁止直播违禁游戏，请立即更换"
"直播中涉及低俗内容"
"直播视角不适宜"
"****涉及引战"
"未按要求遮挡好友申请通知，请查看游戏直播注意事项"
"禁止宣传平台外交易"
"直播中请勿聚焦/突出敏感部位（如胸/臀/腿等部位）"
"分区错误，直播该游戏请移至APEX英雄分区直播"
"分区错误，直播该游戏请移至我的世界分区直播"
"直播中涉及低俗语音，如：低俗诱导打赏、低俗语聊、使用诱惑/挑逗性质的声音等"
```
----
### LIVE
[TOP](#直播弹幕)  
文档更新：2024-04-22  
开播/主播断线重连(重新推流)
| key 10,11			| type	| value	|
|-|-|-|
| cmd				| str	| "LIVE" |
| live_key			| str	| (18) |
| voice_background	| str	| 直播间背景(URL) |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| 开播方式 | |
| live_model		| num	| ？0 3 4 5 |
| {live_time}		| num	| 开播时间TimeStamp(秒) |
| roomid			| num	| 长直播间ID |
```json
// live_mng
{"cmd":"LIVE","live_key":"363170254022513984","voice_background":"","sub_session_key":"363170254022513984sub_time:1682764199","live_platform":"live_mng","live_model":0,"live_time":1682764199,"roomid":5440}
{"cmd":"LIVE","live_key":"381495578107184056","live_model":0,"live_platform":"live_mng","roomid":7734200,"sub_session_key":"381495578107184056sub_time:1687706973","voice_background":"http://i0.hdslb.com/bfs/live/24cab10ebe09222c1de678ed8180d7050766c67b.jpg"}
{"cmd":"LIVE","live_key":"394341331360552256","live_model":0,"live_platform":"live_mng","roomid":5440,"sub_session_key":"394341331360552256sub_time:1691231326","live_time":1691231326,"voice_background":""}
// events_broadcast
{"cmd":"LIVE","live_key":"360846582248079647","voice_background":"","sub_session_key":"360846582248079647sub_time:1680263123","live_platform":"events_broadcast","live_model":0,"live_time":1680263123,"roomid":21987615}
{"cmd":"LIVE","live_key":"360846582248079647","voice_background":"","sub_session_key":"360846582248079647sub_time:1680263123","live_platform":"events_broadcast","live_model":0,"roomid":21987615}
{"cmd":"LIVE","live_key":"376037065530245407","voice_background":"","sub_session_key":"376037065530245407sub_time:1683978433","live_platform":"events_broadcast","live_model":0,"live_time":1683978433,"roomid":21987615}
{"cmd":"LIVE","live_key":"376037065530245407","voice_background":"","sub_session_key":"376037065530245407sub_time:1683978433","live_platform":"events_broadcast","live_model":0,"roomid":21987615}
{"cmd":"LIVE","live_key":"0",                 "voice_background":"","sub_session_key":"446384257562018079sub_time:1702035945","live_platform":"","live_model":0,"roomid":21987615}
{"cmd":"LIVE","live_key":"446384257562018079","voice_background":"","sub_session_key":"446384257562018079sub_time:1702035945","live_platform":"events_broadcast","live_model":0,"roomid":21987615,"live_time":1702035945}
// pc 开播≠推流
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"pc","live_model":0,"roomid":xxx,"live_time":1672502400}
// pc link
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"pc_link","live_model":0,"roomid":xxx,"live_time":1672502400}
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"pc_link","live_model":0,"roomid":xxx}
{"cmd":"LIVE","live_key":"111111111111111111","live_model":x,"live_platform":"pc_link","roomid":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":"http://i0.hdslb.com/bfs/live/xxx.jpg"}
// ios
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios","live_model":x,"live_time":1672502400,"roomid":xxx}
{"cmd":"LIVE","live_key":"443046118785185369","voice_background":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","sub_session_key":"443046118785185369sub_time:1701436556","live_platform":"ios","live_model":3,"roomid":21919321,"live_time":1701436556}
{"cmd":"LIVE","live_key":"111111111111111111","live_model":x,"live_platform":"ios","roomid":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":""}
// ios link
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"https://i0.hdslb.com/bfs/live/b4414564939585e079b130765116bb34a46d9ee7.png","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios_link","live_model":x,"live_time":1672502400,"roomid":xxx}
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios_link","live_model":x,"live_time":1672502400,"roomid":xxx}
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:1672502400","live_platform":"ios_link","live_model":x,"roomid":xxx}
{"cmd":"LIVE","live_key":"431798621638271942","voice_background":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","sub_session_key":"431798621638271942sub_time:1701175779","live_platform":"ios_link","live_model":3,"roomid":xxx}
// android
{"cmd":"LIVE","live_key":"111111111111111111","live_model":x,"live_platform":"android","live_time":1672502400,"roomid":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":"http://i0.hdslb.com/bfs/live/xxx.jpg"}
{"cmd":"LIVE","live_key":"111111111111111111","live_model":x,"live_platform":"android","roomid":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":"http://i0.hdslb.com/bfs/live/xxx.jpg"}
// android link
{"cmd":"LIVE","live_key":"111111111111111111","live_model":x,"live_platform":"android_link","live_time":1672502400,"roomid":xxx,"sub_session_key":"111111111111111111sub_time:1672502400","voice_background":""}
// Harmony?
{"cmd":"LIVE",....}
```
#### live_platform
| live_platform		| desc	| |
|-|-|-|
| live_mng			| ？官方直播 | LPL/1号直播间(5440)/...
| pc				| ~~ |
| pc_link			| PC 直播姬 |
| ios				| iOS APP |
| ios_link			| iOS 直播姬 |
| android			| Android APP |
| android_link		| Android 直播姬 |
| events_broadcast	| |
| harmony?			| xxx |
| xxxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxxx	| xxx |

----
### SEND_GIFT
[TOP](#直播弹幕)  
文档更新：2024-02-01  
送礼物
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "SEND_GIFT" |
| data			| obj	| |
| msg_id		| str	| |
| p_is_ack		| bool	| |
| p_msg_type	| num	| |
| send_time		| num	| |
#### SEND_GIFT__data
| key 59				| type		| value	|
|-|-|-|
| action				| str		| "投喂" |
| bag_gift				| null/obj	| |
| batch_combo_id		| str		| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{时间TimeStamp.4f}"` / 盲盒:UUID |
| batch_combo_send		| null/obj	| |
| beatId				| str		| "0" |
| biz_source			| str		| "Live" "live" |
| blind_gift			| null/obj	| |
| broadcast_id			| num		| 0 |
| coin_type				| str		| "gold" "silver" |
| combo_resources_id	| num		| 1 |
| combo_send			| null/obj	| |
| combo_stay_time		| num		| 3 5 |
| combo_total_coin		| num		| 0 |
| crit_prob				| num		| 0 |
| demarcation			| num		| 1 2 |
| discount_price		| num		| 0 |
| dmscore				| num		| 4×N |
| draw					| num		| 0 |
| effect				| num		| 0 |
| effect_block			| num		| 0 1 |
| face					| str		| 发送者 头像URL |
| face_effect_id		| num		| 0 |
| face_effect_type		| num		| 0 |
| float_sc_resource_id	| num		| 0 |
| giftId				| num		| 礼物ID |
| giftName				| str		| 礼物名称 |
| giftType				| num		| 礼物类型 |
| gift_tag				| []num		| |
| gold					| num		| 0 |
| group_medal			| null/?	| |
| guard_level			| num		| [大航海等级](#others) |
| is_first				| bool		| |
| is_join_receiver		| bool		| false |
| is_naming				| bool		| |
| is_special_batch		| num		| 0 |
| magnification			| float		| 0 1 |
| medal_info			| obj		| [粉丝勋章](#粉丝勋章medal_info) |
| name_color			| str		| "" |
| num					| num		| 礼物数量 |
| original_gift_name	| str		| "" |
| price					| num		| 礼物价格,RMB×1000 |
| rcost					| num		| ？用户总消费(包括金/银) |
| receive_user_info		| obj		| 接收者(主播)用户信息 |
| receiver_uinfo		| obj		| 接收者(主播)用户信息 [uinfo](#pubilc_uinfo) |
| remain				| num		| 包裹剩余数量 |
| rnd					| str		| rnd=tid |
| send_master			| null/?	| |
| sender_uinfo			| obj		| 发送者 用户信息 [uinfo](#pubilc_uinfo) |
| silver				| num		| 0 |
| super					| num		| 0 |
| super_batch_gift_num	| num		| 0 |
| super_gift_num		| num		| 0 |
| svga_block			| num		| 0 |
| switch				| bool		| true |
| tag_image				| str		| "" |
| tid					| str		| rnd=tid |
| timestamp				| num		| TimeStamp(秒) |
| top_list				| null/?	| |
| total_coin			| num		| 礼物总价,RMB×1000 |
| uid					| num		| 发送者uid |
| uname					| str		| 发送者昵称 |
| wealth_level			| num		| 荣耀等级 |
#### SEND_GIFT__data__bag_gift
| key 2					| type		| value	|
|-|-|-|
| price_for_show		| num		| |
| show_price			| num		| |
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
| combo_id				| str		| |
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
		"demarcation": 1,
		"discount_price": 0,
		"dmscore": 4,
		"draw": 0,
		"effect": 0,
		"effect_block": 1,
		"face": "https://i0.hdslb.com/bfs/baselabs/***.png",
		"face_effect_id": 0,
		"face_effect_type": 0,
		"float_sc_resource_id": 0,
		"giftId": 1,
		"giftName": "辣条",
		"giftType": 5,
		"gift_tag": [],
		"gold": 0,
		"group_medal": null,
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
		"num": 2,
		"original_gift_name": "",
		"price": 100,
		"rcost": 1656082,
		"receive_user_info": {"uid": xxx,"uname": "xxx"},
		"receiver_uinfo": ...,
		"remain": 0,
		"rnd": "4462435941977491968",
		"send_master": null,
		"sender_uinfo": ...,
		"silver": 0,
		"super": 0,
		"super_batch_gift_num": 0,
		"super_gift_num": 0,
		"svga_block": 0,
		"switch": true,
		"tag_image": "",
		"tid": "4462435941977491968",
		"timestamp": 1704872067,
		"top_list": null,
		"total_coin": 200,
		"uid": xxxx,
		"uname": "xxxx",
		"wealth_level": 6
	}
}
"batch_combo_id":"batch:gift:combo_id:AAAA:BBBB:CCCC:DDDD.dddd",
```
----
### ONLINE_RANK_V2
[TOP](#直播弹幕)  
高能用户前七(左)，实时
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_V2" |
| data		| obj	| |
#### ONLINE_RANK_V2__data
| key			| type		| value	|
|-|-|-|
| list			| \[7\]obj	| |
| rank_type		| str		| "gold-rank" |
| online_list	| \[7\]obj	| |
| rank_type		| str		| "online_rank" |
#### ONLINE_RANK_V2__data__list
| key 6			| type	| value	|
|-|-|-|
| uid			| num | uid |
| face			| str | 头像URL |
| score			| str | 贡献值 |
| uname			| str | 昵称 |
| rank			| num | 排名(1-7) |
| guard_level	| num | [大航海等级](#others) |
```json
{
	"cmd":"ONLINE_RANK_V2",
	"data":{
		"online_list":[
			{"uid":1,"face":"xxx","score":"7","uname":"xxx","rank":1,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":2,"face":"xxx","score":"6","uname":"xxx","rank":2,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":3,"face":"xxx","score":"5","uname":"xxx","rank":3,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":4,"face":"xxx","score":"4","uname":"xxx","rank":4,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":5,"face":"xxx","score":"3","uname":"xxx","rank":5,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":6,"face":"xxx","score":"2","uname":"xxx","rank":6,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}},
			{"uid":7,"face":"xxx","score":"1","uname":"xxx","rank":7,"guard_level":0,"is_mystery":false,"uinfo":{"key":"value"}}
		],
	"rank_type":"online_rank"
	}
}
```
----
### ONLINE_RANK_TOP3
[TOP](#直播弹幕)  
高能用户前三(左)  
文档更新：2024-03-16  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_TOP3" |
| data		| obj	| |
#### ONLINE_RANK_TOP3__data
| key		| type		| value	|
|-|-|-|
| dmscore	| num		| 112 |
| list		| [1]obj	| |
#### ONLINE_RANK_TOP3__data__list
| key			| type	| value	|
|-|-|-|
| is_mystery	| bool	| |2023-11-30
| msg			| str	| `f"恭喜 <%XXX%> 成为高能用户"` |
| rank			| num	| 排名(1-3) |
| uid			| num	| |
```json
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":784,"list":[{"is_mystery":false,"msg":"恭喜 <%XXX%> 成为高能用户","rank":1,"uid":1}]}}
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":784,"list":[{"is_mystery":false,"msg":"恭喜 <%XXX%> 成为高能用户","rank":2,"uid":2}]}}
{"cmd":"ONLINE_RANK_TOP3","data":{"dmscore":784,"list":[{"is_mystery":false,"msg":"恭喜 <%XXX%> 成为高能用户","rank":3,"uid":3}]}}
dms: ~20240218: 112
	20240218:196
	20240221~ :784
```
----
### ONLINE_RANK_COUNT
[TOP](#直播弹幕)  
文档更新：2024-04-30  
高能用户人数(观众人数)  
约每5×N秒发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_COUNT" |
| data		| obj	| |
#### ONLINE_RANK_COUNT__data
| key		| type	| value	|
|-|-|-|
| count				| num	| 最大值**约**为10000[1-100xx] |
| count_text		| str	| |
| online_count		| num	| |
| online_count_text	| str	| |
```json
{"cmd":"ONLINE_RANK_COUNT","data":{"count":10000,"count_text":"1万+"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":10001,"count_text":"1万+","online_count":415011,"online_count_text":"41万+"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":0,"count_text":"0"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":0,"count_text":"0","online_count":0,"online_count_text":"0"}}
```
----
### INTERACT_WORD
[TOP](#直播弹幕)  
进入直播间、关注主播通知（高精度）500ms
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_WORD" |
| data		| obj	| |
#### INTERACT_WORD__data
| key 23			| type		| value	| |
|-|-|-|-|
| contribution		| obj		| |
| contribution_v2	| obj		| |
| core_user_type	| num		| ？大部分为0[0-5] |
| dmscore			| num		| |
| fans_medal		| null/obj	| [粉丝勋章](#粉丝勋章medal_info) |
| group_medal		| null/?	| |
| identities		| [+]num	| [identities](#others) |
| is_mystery		| bool		| |
| is_spread			| num		| 流量包推广 0,1 |
| msg_type			| num		| |
| privilege_type	| num		| [privilege_type](#others) is_spread==1:`0` |
| roomid			| num		| 长_短直播间ID |
| score				| num		| ？ |
| spread_desc		| str		| is_spread==1:"流量包推广" |
| spread_info		| str		| is_spread==1:"#FF649E" |
| tail_icon			| num		| 0,101,102 |
| tail_text			| str		| "" |
| timestamp			| num		| TimeStamp(秒) |
| trigger_time		| num		| ？TimeStamp|
| uid				| num		| 用户uid |
| uinfo				| obj		| 用户信息 [uinfo](#pubilc_uinfo) |
| uname				| str		| 用户昵称 |
| uname_color		| str		| "" |
#### INTERACT_WORD__data__contribution
| key 		| type		| value	| |
|-|-|-|-|
| grade		| num		| |
| key 		| type		| value	| |
|-|-|-|-|
| grade		| num		| |
| rank_type	| str		| |
| text		| str		| |
#### INTERACT_WORD__msg_type
|-|type|
|-|-|
|1|进入直播间
|2|关注
|3|分享
|4|特别关注
|5|互粉
Link = 6
```json
{
	"cmd":"INTERACT_WORD",
	"data":{
		"contribution":{"grade":0},
		"contribution_v2":{"grade":0,"rank_type":"","text":""},
		"core_user_type":0,
		"dmscore":2,
		"fans_medal":{"anchor_roomid":0,"guard_level":0,"icon_id":0,"is_lighted":0,"medal_color":0,"medal_color_border":0,"medal_color_end":0,"medal_color_start":0,"medal_level":0,"medal_name":"","score":0,"special":"","target_id":0},
		"group_medal":null,
		"identities":[1],
		"is_mystery":false,
		"is_spread":0,
		"msg_type":1,
		"privilege_type":0,
		"roomid":31399498,
		"score":1704872049684,
		"spread_desc":"",
		"spread_info":"",
		"tail_icon":0,
		"tail_text":"",
		"timestamp":1704872049,
		"trigger_time":1704872048586738400,
		"uid":13545537,
		"uinfo":{"key":"value"},
		"uname":"SJH8130",
		"uname_color":""
	}
}
"contribution_v2":{"grade":123,"rank_type":"daily_rank","text":"日榜前3用户"}
"contribution_v2":{"grade":123,"rank_type":"monthly_rank","text":"月榜前3用户"}
"contribution_v2":{"grade":123,"rank_type":"weekly_rank","text":"周榜前3用户"}
```
----
### WATCHED_CHANGE
[TOP](#直播弹幕)  
(每5秒&数值更新)发送一次 用户(包括游客、主播)进入直播间时发送
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WATCHED_CHANGE" |
| data		| obj	| |
#### WATCHED_CHANGE__data
| key 3			| type	| value	|
|-|-|-|
| num			| num	| 人数 |
| text_small	| str	| str(num) <br> "x.y万" |
| text_large	| str	| f"num人看过" <br> "x.y万人看过" |
```json
{"cmd":"WATCHED_CHANGE","data":{"num":    0,"text_small":    "0","text_large":"0人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num": 9999,"text_small": "9999","text_large":"9999人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num":10001,"text_small":"1.0万","text_large":"1.0万人看过"}}
```
----
### ROOM_REAL_TIME_MESSAGE_UPDATE
[TOP](#直播弹幕)  
(每N×60秒&数值更新)发送一次，更新关注数、粉丝团人数
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data		| obj	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE__data
| key 4			| type	| value	|
|-|-|-|
| roomid		| num	| 长直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1 |
| fans_club		| num	| 粉丝团成员(活跃人数) |
```json
{"cmd":"ROOM_REAL_TIME_MESSAGE_UPDATE","data":{"roomid":9999,"fans":9999,"red_notice":-1,"fans_club":9999}}
```
----
### LIKE_INFO_V3_CLICK
[TOP](#直播弹幕)  
点赞，实时&每5秒最多发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_CLICK" |
| data		| obj	| |
#### LIKE_INFO_V3_CLICK__data
| key 14					| type		| value	|
|-|-|-|
| show_area					| num		| 0 <br> 1(30s) |
| msg_type					| num		| 6 |
| like_icon					| str		| [图标][img_16] |
| uid						| num		| uid |
| like_text					| str		| "为主播点赞了" |
| uname						| str		| 昵称 |
| uname_color				| str		| "" |
| identities				| [+]num	| [identities](#others) |
| fans_medal				| obj		| [fans_medal](#粉丝勋章medal_info) |
| contribution_info			| obj		| |
| dmscore					| num		| 20 |
| group_medal				| null/		| |
| is_mystery				| bool		| |
| uinfo						| null/obj	| [uinfo](#pubilc_uinfo) |
```json
{
	"cmd": "LIKE_INFO_V3_CLICK",
	"data": {
		"contribution_info": {"grade": 0},
		"dmscore": 9999,
		"fans_medal": {"key":"value"},
		"group_medal": null,
		"identities": [3,1],
		"is_mystery": false,
		"like_icon": "https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png",
		"like_text": "为主播点赞了",
		"msg_type": 6,
		"show_area": 0,
		"uid": 9999,
		"uinfo": {"key":"value"},
		"uname": "xxx",
		"uname_color": ""
	}
}
```
----
### LIKE_INFO_V3_NOTICE
[TOP](#直播弹幕)  
202306新增  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_NOTICE" |
| data		| obj	| |
#### LIKE_INFO_V3_NOTICE__data
| key				| type	| value	|
|-|-|-|
| content_segments	| [1]obj	| |
| danmaku_style		| obj		| |
| terminals			| [+]num	| |
```json
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"试试双击点赞，让主播被更多人看到吧～"                   ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[1,4]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计100，快去号召直播间用户继续为你助力吧~"    ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计500，快去号召直播间用户继续为你助力吧~"    ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计5000，快去号召直播间用户继续为你助力吧~"   ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计10000，快去号召直播间用户继续为你助力吧~"  ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计50000，快去号召直播间用户继续为你助力吧~"  ,"type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计1000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE","data":{"content_segments":[{"font_color":"#F494AF","text":"本场点赞已累计5000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
```
----
### LIKE_INFO_V3_UPDATE
[TOP](#直播弹幕)  
点赞，实时&每5秒最多发送一次
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_UPDATE" |
| data		| obj	| |
#### LIKE_INFO_V3_UPDATE__data
| key			| type	| value	|
|-|-|-|
| click_count	| num	| 点赞数量 |
```json
{"cmd":"LIKE_INFO_V3_UPDATE","data":{"click_count":0}}
```
----
### HOT_ROOM_NOTIFY
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "HOT_ROOM_NOTIFY" |
| data		| obj	| |
#### HOT_ROOM_NOTIFY__data
| key 4					| type		| value	|
|-|-|-|
| threshold				| num		| 10000 |
| ttl					| num		| 300 |
| exit_no_refresh		| num		| 1 |
| random_delay_req_v2	| [2]obj	| |
#### HOT_ROOM_NOTIFY__data__random_delay_req_v2
| key	| type	| value	|
|-|-|-|
| path	| str	| |
| delay	| num	| |
```json
{"cmd":"HOT_ROOM_NOTIFY","data":{"threshold":10000,"ttl":300,"exit_no_refresh":1,"random_delay_req_v2":[{"path":"/live/getRoundPlayVideo","delay":10},{"path":"/xlive/web-room/v1/index/getOffLiveList","delay":120000}]}}
```
----
### ENTRY_EFFECT
[TOP](#直播弹幕)  
`ENTRY_EFFECT` 欢迎大航海成员进入直播间，高精度  
`ENTRY_EFFECT_MUST_RECEIVE` 欢迎？进入直播间，高精度
文档更新：2024-02-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ENTRY_EFFECT" "ENTRY_EFFECT_MUST_RECEIVE" |
| data		| obj	| |
#### ENTRY_EFFECT__data
| key 32					| type		| value	| |
|-|-|-|-|
| id						| num		| |
| uid						| num		| 用户uid |
| target_id					| num		| 主播uid |
| mock_effect				| num		| |
| face						| str		| 头像URL |
| privilege_type			| num		| [privilege_type](#others) |
| copy_writing				| str		| `r"(欢迎(舰长\|提督\|总督) )?<%XXX%> 进入直播间"` |限长7字符，省略号为`...`
| copy_color				| str		| #rrggbb |
| highlight_color			| str		| #RRGGBB |
| priority					| num		| |
| basemap_url				| str		| basemap_url=web_basemap_url |
| show_avatar				| num		| 1 |
| effective_time			| num		| effective_time=web_effective_time |
| web_basemap_url			| str		| basemap_url=web_basemap_url |
| web_effective_time		| num		| effective_time=web_effective_time |
| web_effect_close			| num		| |
| web_close_time			| num		| |
| business					| num		| |
| copy_writing_v2			| str		| `r"(欢迎(提督\|舰长\|总督) )?<%XXX%> 进入直播间"`|限长6字符，省略号为`…`
| icon_list					| [+]num	| |
| max_delay_time			| num		| 7 |
| trigger_time				| num		| ？TimeStamp |
| identities				| num		| [identities](#others) |
| effect_silent_time		| float		| 0 |
| effective_time_new		| num		| |
| web_dynamic_url_webp		| str		| |
| web_dynamic_url_apng		| str		| |
| mobile_dynamic_url_webp	| str		| |
| wealthy_info				| null/obj	| |
| new_style					| num		| |
| is_mystery				| bool		| |
| uinfo						| obj		| |
----
### STOP_LIVE_ROOM_LIST
[TOP](#直播弹幕)  
每30秒发送一次(`HH:mm:29`,`HH:mm:59`)  
广播 未压缩  
文档更新：2024-02-23  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "STOP_LIVE_ROOM_LIST" |
| data		| obj	| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type		| value	|
|-|-|-|
| room_id_list	| [+]num	| |
```json
{"cmd":"STOP_LIVE_ROOM_LIST","data":{"room_id_list":[1,2,3,4,5,6,7,8,9]}}
```
----
### GUARD_BUY
[TOP](#直播弹幕)  
大航海购买  
文档更新：2024-04-12  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GUARD_BUY" |
| data		| obj	| |
#### GUARD_BUY__data
| key 9			| type	| value	|
|-|-|-|
| uid			| num	| uid |
| username		| str	| 昵称 |
| guard_level	| num	| [guard_level](#others) |
| num			| num	| 购买数量 |
| price			| num	| 舰长:198000 提督:1998000 总督:19998000 |
| gift_id		| num	| 舰长:10003 提督:10002 总督:10001 |
| gift_name		| str	| |
| start_time	| num	| 购买时间 TimeStamp(秒) |
| end_time		| num	| 购买时间 TimeStamp(秒) |
```json
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":1,"num":1,"price":19998000,"gift_id":10001,"gift_name":"总督","start_time":1704038400,"end_time":1704038400}}
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":2,"num":1,"price":1998000, "gift_id":10002,"gift_name":"提督","start_time":1704038400,"end_time":1704038400}}
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":3,"num":1,"price":198000,  "gift_id":10003,"gift_name":"舰长","start_time":1704038400,"end_time":1704038400}}
{"cmd":"GUARD_BUY","data":{"uid":12345,"username":"xxx","guard_level":3,"num":6,"price":198000,  "gift_id":10003,"gift_name":"舰长","start_time":1704038400,"end_time":1704038400}}
```
----
### USER_TOAST_MSG
[TOP](#直播弹幕)  
大航海购买通知，显示在聊天区  
文档更新：2024-01-28  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG__data
| key 28				| type	| value	|
|-|-|-|
| anchor_show			| bool	| true |
| color					| str	| 舰长:"#00D1F1" <br> 提督:"#E17AFF" <br> 总督:"#FF7C28" |
| dmscore				| num	| 舰长:x	<br> 提督:y	<br> 总督:z <br>`dms=上舰次数*x, 102*u+12*v` |1*舰长=102, 324 432 540 648 684
| effect_id				| num	||
| end_time				| num	| TimeStamp(秒) |
| face_effect_id		| num	| |
| gift_id				| num	| 舰长:10003<br> 提督:10002 <br> 总督:10001 |
| group_name			| str	| |
| group_op_type			| num	| |
| group_role_name		| str	| |
| guard_level			| num	| [guard_level](#others) |
| is_group				| num	| 0 |
| is_show				| num	| 0 |
| num					| num	| 购买数量 |
| op_type				| num	| 1: <br> 2: <br> 3: <br> 4: |
| payflow_id			| str	| 订单号(25)(YYMMDD HHmmss xxxxxxxxxxxxx) |
| price					| num	| 舰长138 158 198 <br> 提督1598 1998 <br> 总督15998 19998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| |
| room_group_effect_id	| num	| |
| start_time			| num	| 购买时间 TimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播当前大航海成员数 |
| toast_msg				| str	|`f"<%XXX%> 在主播YYY的直播间(开通\|续费)了(\d+个月)?(舰长\|提督\|总督)，今天是TA陪伴主播的第\d+天"` |
| uid					| num	| uid |
| unit					| str	| "月" |
| user_show				| bool	| true |
| username				| str	| 昵称 |
```json
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":1,"payflow_id":"240101000000xxxxxxxxxxxxx","price":138000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":96, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":1,"payflow_id":"240101000000xxxxxxxxxxxxx","price":138000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":138000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":138000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":158000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":1,"op_type":1,"payflow_id":"240101000000xxxxxxxxxxxxx","price":198000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":3,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":514000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了3个月舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#00D1F1","dmscore":90, "effect_id":397,"end_time":1704038400,"face_effect_id":44,"gift_id":10003,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":3,"is_group":0,"is_show":0,"num":6,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":948000,"role_name":"舰长","room_effect_id":590,"room_group_effect_id":1337,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了6个月舰长，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}

{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1704038400,"face_effect_id":43,"gift_id":10002,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":2,"is_group":0,"is_show":0,"num":1,"op_type":2,"payflow_id":"240101000000xxxxxxxxxxxxx","price":1598000,"role_name":"提督","room_effect_id":591,"room_group_effect_id":398,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":96, "effect_id":398,"end_time":1704038400,"face_effect_id":43,"gift_id":10002,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":2,"is_group":0,"is_show":0,"num":1,"op_type":1,"payflow_id":"240101000000xxxxxxxxxxxxx","price":1998000,"role_name":"提督","room_effect_id":591,"room_group_effect_id":398,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":102,"effect_id":398,"end_time":1704038400,"face_effect_id":43,"gift_id":10002,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":2,"is_group":0,"is_show":0,"num":1,"op_type":1,"payflow_id":"240101000000xxxxxxxxxxxxx","price":1998000,"role_name":"提督","room_effect_id":591,"room_group_effect_id":398,"start_time":1704038400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了提督，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#E17AFF","dmscore":648,"effect_id":398,"end_time":1711975545,"face_effect_id":43,"gift_id":10002,"group_name":"","group_op_type":0,"group_role_name":"","guard_level":2,"is_group":0,"is_show":0,"num":12,"op_type":2,"payflow_id":"24040120454xxxxxxxxxxxxxx","price":19176000,"role_name":"提督","room_effect_id":591,"room_group_effect_id":398,"start_time":1711975545,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播TTTT的直播间续费了12个月提督，今天是TA陪伴主播的第xx天","uid":12345,"unit":"月","user_show":true,"username":"xxx"}}

{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":19998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间开通了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":15998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 在主播YYY的直播间续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":1,"payflow_id":"230101000000xxxxxxxxxxxxx","price":19998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
{"cmd":"USER_TOAST_MSG","data":{"anchor_show":true,"color":"#FF7C28","dmscore":102,"effect_id":399,"end_time":1672502400,"face_effect_id":42,"gift_id":10001,"guard_level":1,"is_show":0,"num":1,"op_type":2,"payflow_id":"230101000000xxxxxxxxxxxxx","price":15998000,"role_name":"总督","room_effect_id":592,"start_time":1672502400,"svga_block":0,"target_guard_count":123,"toast_msg":"<%XXX%> 续费了总督，今天是TA陪伴主播的第××天","uid":12345,"unit":"月","user_show":true,"username":"XXX"}}
```
----
### NOTICE_MSG
[TOP](#直播弹幕)  
文档更新：2024-04-12  
滚动横幅 **广播**
| key 17※ 18	| type	| value	|
|-|-|-|
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
| link_url		| str	| 目标直播间URL |
| msg_type		| num	| |
| shield_uid	| num	| |
| business_id	| str	| xxxx |
| scatter		| obj	| |
| marquee_id	| str	| |
| notice_type	| num	| 0 |
#### NOTICE_MSG__full
| key			| type	| value	|
|-|-|-|
| head_icon		| str	| |
| tail_icon		| str	| |
| head_icon_fa	| str	| |
| tail_icon_fa	| str	| |
| head_icon_fan	| num	| |
| tail_icon_fan	| num	| |
| background	| str	| "#RRGGBB" |
| color			| str	| "#RRGGBB" |
| highlight		| str	| "#RRGGBB" |
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
| background	| str	| "#RRGGBBAA" |
| color			| str	| "#RRGGBBAA" |
| highlight		| str	| "#RRGGBBAA" |
| border		| str	| "#RRGGBBAA" |
#### NOTICE_MSG__scatter
| key	| type	| value	|
|-|-|-|
| min	| num	| 0 |
| max	| num	| 0 |
```json
{"cmd":"NOTICE_MSG","id":968,"name":"舰长1个月","full":{"head_icon":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","tail_icon":"","head_icon_fa":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","tail_icon_fa":"","head_icon_fan":1,"tail_icon_fan":0,"background":"#FFE2B2","color":"#B87436","highlight":"#E37921","time":10},"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},"side":{"head_icon":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},"roomid":9999,"real_roomid":9999,"msg_common":"","msg_self":"<%xxx%> 在主播 <%xxx%>的直播间续费了舰长，感谢上船陪伴","link_url":"","msg_type":4,"shield_uid":-1,"business_id":"xuser-guard","scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0}
```
----
### SUPER_CHAT_MESSAGE
[TOP](#直播弹幕)  
文档更新：2024-04-22  
SuperChat
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 长_短直播间ID |
| is_report	| bool	| true |
| msg_id	| str	| |
| send_time	| num	| |
#### SUPER_CHAT_MESSAGE__data
| key 27					| type		| value	|
|-|-|-|
| background_bottom_color	| str		| [table](#SC价格颜色表) |
| background_color			| str		| [table](#SC价格颜色表) |
| background_color_end		| str		| [table](#SC价格颜色表) |
| background_color_start	| str		| [table](#SC价格颜色表) |
| background_icon			| str		| URL/"" |
| background_image			| str		| URL/"" |
| background_price_color	| str		| [table](#SC价格颜色表) |
| color_point				| float		| 0.7 |
| dmscore					| num		| ~2020-x-x: `[16,24,48,56,64,72,80,112,120,128]`<br>2024-x-x~: dms/0.7=a*b*c+x+y+z
| end_time					| num		| TimeStamp(秒) |
| gift						| obj		| |
| group_medal				| obj		| |
| id						| num		| SC id |
| is_mystery				| bool		| |
| is_ranked					| num		| 0,1 |
| is_send_audit				| num		| 0,1 |
| medal_info				| obj		| [medal_info](#粉丝勋章medal_info):medal_color为`#rrggbb` |
| message					| str		| SC 内容 |
| message_font_color		| str		| |
| message_trans				| str		| SC 日本語 翻译 |
| price						| num		| 价格(CNY) |
| rate						| num		| 1000 |
| start_time				| num		| TimeStamp(秒) |
| time						| num		| SC剩余时长(秒) |
| token						| str		| hex(64bit) |
| trans_mark				| num		| 是否翻译 |
| ts						| num		| TimeStamp(秒) |
| uid						| num		| uid |
| uinfo						| obj		| [uinfo](#pubilc_uinfo) |
| user_info					| obj		| |
#### SUPER_CHAT_MESSAGE__data__gift
| key						| type		| value	|
|-|-|-|
| gift_id					| num		| 12000 |
| gift_name					| str		| "醒目留言" |
| num						| num		| 1 |
#### SUPER_CHAT_MESSAGE__data__group_medal
| key						| type		| value	|
|-|-|-|
| is_lighted				| num		| |
| medal_id					| num		| |
| name						| str		| |
#### SUPER_CHAT_MESSAGE__data__user_info
| key 12					| type		| value	|
|-|-|-|
| face						| str		| 头像(URL) |
| face_frame				| str		| 头像框(URL) |
| guard_level				| num		| [guard_level](#others) |
| is_main_vip				| num		| ？0 |
| is_svip					| num		| ？0 |
| is_vip					| num		| ？0 |
| level_color				| str		| #rrggbb |
| manager					| num		| ？管理员 |
| name_color				| str		| #RRGGBB |
| title						| str		| [头衔](docs/头衔.md) |
| uname						| str		| 昵称 |
| user_level				| num		| 直播观众等级 (UL) |
```json
{
	"cmd": "SUPER_CHAT_MESSAGE",
	"data": {
		"background_bottom_color": "#xxx",
		"background_color": "#xxx",
		"background_color_end": "#xxx",
		"background_color_start": "#xxx",
		"background_icon": "",
		"background_image": "",
		"background_price_color": "#xxx",
		"color_point": 0.7,
		"dmscore": 9999,
		"end_time": 9999,
		"gift": {"gift_id": 12000,"gift_name": "醒目留言","num": 1},
		"group_medal": {"is_lighted": 0,"medal_id": 0,"name": ""},
		"id": 9999,
		"is_mystery": false,
		"is_ranked": 0,
		"is_send_audit": 1,
		"medal_info": {"key":"value"},
		"message": "xxxxxx",
		"message_font_color": "#A3F6FF",
		"message_trans": "",
		"price": 9999,
		"rate": 1000,
		"start_time": 9999,
		"time": 9999,
		"token": "FFFFFFFF",
		"trans_mark": 0,
		"ts": 9999,
		"uid": 9999,
		"uinfo": {"key":"value"},
		"user_info": {"key":"value"}
	},
	"is_report": true,
	"msg_id": "XXX:???:1000",
	"p_is_ack": true,
	"p_msg_type": 1,
	"send_time": 9999
}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#2A60B2","background_color":"#EDF5FF","background_color_end":"#405D85","background_color_start":"#3171D2","background_icon":"","background_image":"","background_price_color":"#7497CD","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#A3F6FF","message_trans":"","price":30,"rate":1000,"start_time":9999,"time":60,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#2A60B2","background_color":"#EDF5FF","background_color_end":"#405D85","background_color_start":"#3171D2","background_icon":"","background_image":"","background_price_color":"#7497CD","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#A3F6FF","message_trans":"","price":30,"rate":1000,"start_time":9999,"time":60,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:100:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#427D9E","background_color":"#DBFFFD","background_color_end":"#29718B","background_color_start":"#4EA4C5","background_icon":"","background_image":"","background_price_color":"#7DA4BD","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#A3F6FF","message_trans":"","price":50,"rate":1000,"start_time":9999,"time":120,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#427D9E","background_color":"#DBFFFD","background_color_end":"#29718B","background_color_start":"#4EA4C5","background_icon":"","background_image":"","background_price_color":"#7DA4BD","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#A3F6FF","message_trans":"","price":50,"rate":1000,"start_time":9999,"time":120,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:100:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#E2B52B","background_color":"#FFF1C5","background_color_end":"#EEBE5C","background_color_start":"#EAB400","background_icon":"","background_image":"","background_price_color":"#ECCF75","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#72110E","message_trans":"","price":100,"rate":1000,"start_time":9999,"time":300,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#E09443","background_color":"#FFEAD2","background_color_end":"#DB9039","background_color_start":"#FFA850","background_icon":"https://i0.hdslb.com/bfs/live/e12e931ed8d9e5189ab6d1a3a1da35af4f8a55af.png","background_image":"","background_price_color":"#E8AF79","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#72110E","message_trans":"","price":500,"rate":1000,"start_time":9999,"time":1800,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#E54D4D","background_color":"#FFE7E4","background_color_end":"#BD666A","background_color_start":"#F63C45","background_icon":"https://i0.hdslb.com/bfs/live/0cf7b5fdc7084c9ae05f7a371ea2438118529d66.png","background_image":"","background_price_color":"#EE8B8B","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#FFE163","message_trans":"","price":1000,"rate":1000,"start_time":9999,"time":3600,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#E54D4D","background_color":"#FFE7E4","background_color_end":"#BD666A","background_color_start":"#F63C45","background_icon":"https://i0.hdslb.com/bfs/live/0cf7b5fdc7084c9ae05f7a371ea2438118529d66.png","background_image":"https://i0.hdslb.com/bfs/live/34ced2e8be7de1a32f1dc0cd4903ab9f1e115749.png","background_price_color":"#EE8B8B","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#FFE163","message_trans":"","price":1000,"rate":1000,"start_time":9999,"time":3600,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
{"cmd":"SUPER_CHAT_MESSAGE","data":{"background_bottom_color":"#AB1A32","background_color":"#FFD8D8","background_color_end":"#8B0F3D","background_color_start":"#600012","background_icon":"https://i0.hdslb.com/bfs/live/0d9cbbdbad7d3371266cd5b568065415415316ae.png","background_image":"","background_price_color":"#C86A7A","color_point":0.7,"dmscore":9999,"end_time":9999,"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},"group_medal":{"is_lighted":0,"medal_id":0,"name":""},"id":9999,"is_mystery":false,"is_ranked":0,"is_send_audit":1,"medal_info":{"key":"value"},"message":"XXX","message_font_color":"#FFE163","message_trans":"","price":2000,"rate":1000,"start_time":9999,"time":7200,"token":"FFFFFFFF","trans_mark":0,"ts":9999,"uid":9999,"uinfo":{"key":"value"},"user_info":{"key":"value"}},"is_report":true,"msg_id":"XXX:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":9999}
```
### SC价格颜色表
| price | background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	|
|-|-|-|-|-|-|-|
| 30+	| #2A60B2					| #EDF5FF			| #405D85				| #3171D2					| #7497CD					| #A3F6FF				|
| 50+	| #427D9E					| #DBFFFD			| #29718B				| #4EA4C5					| #7DA4BD					| #A3F6FF				|
| 100+	| #E2B52B					| #FFF1C5			| #EEBE5C				| #EAB400					| #ECCF75					| #72110E				|
| 500+	| #E09443					| #FFEAD2			| #DB9039				| #FFA850					| #E8AF79					| #72110E				|
| 1000+	| #E54D4D					| #FFE7E4			| #BD666A				| #F63C45					| #EE8B8B					| #FFE163				|
| 2000+	| #AB1A32					| #FFD8D8			| #8B0F3D				| #600012					| #C86A7A					| #FFE163				|
----
### SUPER_CHAT_MESSAGE_JPN
[TOP](#直播弹幕)  
SuperChat 日本語  
由`百度翻译`提供翻译 / Translated by `Baidu Translate`
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE_JPN" |
| data		| obj	| |
| roomid	| str	| str(长_短直播间ID) |
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
| medal_info				| obj	| [medal_info](#粉丝勋章medal_info) 没有(`guard_level`, `is_lighted`, `medal_color_border`, `medal_color_end`, `medal_color_start`) |
| user_info					| obj	| |
| time						| num	| |
| start_time				| num	| TimeStamp(秒) |
| end_time					| num	| TimeStamp(秒) |
| gift						| obj	| |
```json
{"cmd":"SUPER_CHAT_MESSAGE_JPN","data":{"id":"12345","uid":"23456","price":50,"rate":1000,"message":"123","message_jpn":"123","is_ranked":1,"background_image":"https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_color":"#DBFFFD","background_icon":"","background_price_color":"#7DA4BD","background_bottom_color":"#427D9E","ts":1672502400,"token":"50316B2E","medal_info":null,"user_info":{"key":"value"},"time":120,"start_time":1672502400,"end_time":1672502400,"gift":{"num":1,"gift_id":12000,"gift_name":"醒目留言"}},"roomid":"12345"}
```
----
### SUPER_CHAT_MESSAGE_DELETE
[TOP](#直播弹幕)  
文档更新：2024-04-12  
SC 删除
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE_DELETE" |
| data		| obj	| |
#### SUPER_CHAT_MESSAGE_DELETE__data
| key		| type		| value	|
|-|-|-|
| ids		| [+]num	| SC_id |
| roomid	| num		| 长_短直播间ID |
```json
{"cmd":"SUPER_CHAT_MESSAGE_DELETE","data":{"ids":[123]},"roomid":12345}
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
| aggregation_icon		| str	| (URL) |
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| dmscore				| num	| 144 |
| msg					| str	| 抽奖口令 |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间TimeStamp(秒) |
```json
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":1,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png","aggregation_num":111,"broadcast_msg_type":0,"dmscore":144,"msg":"xxxxx","show_rows":1,"show_time":2,"timestamp":1672502400}}
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"5475890","activity_source":1,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png","aggregation_num":999,"broadcast_msg_type":0,"dmscore":144,"msg":"蔷薇与铳枪","show_rows":1,"show_time":2,"timestamp":1702037680}}
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":2,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png","aggregation_num":111,"broadcast_msg_type":0,"dmscore":144,"msg":"老板大气！点点红包抽礼物","show_rows":1,"show_time":2,"timestamp":1672502400}}
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
文档更新：2024-04-12  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "GUARD_HONOR_THOUSAND" |
| data	| obj	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type		| value	|
|-|-|-|
| add	| [+]num	| 用户uid |
| del	| [+]num	| 用户uid |
```json
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[],"del":[9999]}}
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[9999],"del":[]}}
```
----
### ANCHOR_LOT_CHECKSTATUS
[TOP](#直播弹幕)  
抽奖(天选时刻)检查
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_CHECKSTATUS" |
| data		| obj	| |
#### ANCHOR_LOT_CHECKSTATUS__data
| key 3,5			| type	| value	|
|-|-|-|
| id				| num	| 抽奖id |
| ?reject_danmu		| null	| ？null |
| ?reject_reason	| str	| 拒绝理由 |
| status			| num	| 4:通过 5:拒绝 |
| uid				| num	| 主播uid |
```json
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"由于奖品格式不合格,请仔细检查后再提交哦","status":5,"uid":12345}}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"","status":4,"uid":12345}}

{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"","status":4,"uid":12345}}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"status":4,"uid":12345}}
```
----
### ANCHOR_LOT_START
[TOP](#直播弹幕)  
文档更新：2024-01-19  
抽奖(天选时刻)开始
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_START" |
| data		| obj	| |
#### ANCHOR_LOT_START__data
| key 33			| type		| value	|
|-|-|-|
| asset_icon		| str		| 图像URL(png) |
| asset_icon_webp	| str		| 图像URL(webp) |
| award_image		| str		| |
| award_name		| str		| 礼物名称 |
| award_num			| num		| 礼物数量\[1,100\] |
| award_type		| num		| 0 1 |
| award_price_text	| str		| "价值xxx电池" |
| break_up_time		| num		| 0 |
| cur_gift_num		| num		| 0 |
| current_time		| num		| 当前时间TimeStamp(秒) |
| danmu				| str		| 弹幕口令\[0,15\] |
| danmu_new			| \[1\]obj	| |
| danmu_type		| num		| `danmu_type:0 === this.danmuType ? "文案弹幕" :"表情弹幕"` |
| gift_id			| num		| 0 |
| gift_name			| str		| ~~礼物抽奖：抽奖条件~~ |
| gift_num			| num		| 礼物抽奖：数量 |
| gift_price		| num		| 礼物抽奖：礼物价格(RMB×1000) |
| goaway_time		| num		| ？180 |
| goods_id			| num		| |
| id				| num		| 抽奖id |
| is_broadcast		| num		| 1 |
| join_type			| num		| 0,1 |
| lot_status		| num		| [lot_status](#others) \[0,1,2\] |
| max_time			| num		| 开奖时间(60,300,600,900)秒 |
| require_text		| str		| "抽奖条件: 关注主播" / "至少成为主播的舰长/提督/总督" |
| require_type		| num		| 抽奖条件 1:礼物抽奖 2:粉丝勋章 3:大航海 ~~4:UL？~~ |
| require_value		| num		| [0,1] 关注状态/[1,20] 粉丝勋章等级/[1,3] [大航海等级](#others) |
| room_id			| num		| 长直播间ID |
| send_gift_ensure	| num		| 0 |
| show_panel		| num		| 1 |
| start_dont_popup	| num		| 0 |
| status			| num		| 1 |
| time				| num		| 剩余时间(秒) |
| url				| str		| URL |
| web_url			| str		| https://live.XXXX.com/p/html/live-lottery/anchor-join.html |
#### ANCHOR_LOT_START__data__danmu_new
| key 3			| type	| value	|
|-|-|-|
| danmu			| str	| 弹幕口令\[0,15\] |
| danmu_view	| str	| |
| reject		| bool	| |
```json
{"cmd":"ANCHOR_LOT_START","data":{"asset_icon":"https://i0.hdslb.com/bfs/live/627ee2d9e71c682810e7dc4400d5ae2713442c02.png","asset_icon_webp":"https://i0.hdslb.com/bfs/live/b47453a0d42f30673b6d030159a96d07905d677a.webp","award_image":"","award_name":"PS5轻薄版1台","award_num":1,"award_type":0,"break_up_time":0,"cur_gift_num":0,"current_time":1705662414,"danmu":"2023游戏区年 度盘点冲冲冲！","danmu_new":[{"danmu":"2023游戏区年度盘点冲冲冲！","danmu_view":"","reject":false}],"danmu_type":0,"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,"goaway_time":180,"goods_id":-99998,"id":5708694,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":300,"require_text":"关注主播","require_type":1,"require_value":0,"room_id":5440,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":299,"url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1","web_url":"https://live.bilibili.com/p/html/live-lottery/anchor-join.html"}}
```
----
### ANCHOR_LOT_END
[TOP](#直播弹幕)  
文档更新：2024-01-19  
抽奖(天选时刻)结束
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_END" |
| data		| obj	| |
#### ANCHOR_LOT_END__data
| key	| type	| value	|
|-|-|-|
| id	| num	| 抽奖id |
```json
{"cmd":"ANCHOR_LOT_END","data":{"id":12345}}
```
----
### ANCHOR_LOT_AWARD
[TOP](#直播弹幕)  
文档更新：2024-01-19  
抽奖(天选时刻) 中奖名单
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_AWARD" |
| data		| obj	| |
#### ANCHOR_LOT_AWARD__data
| key 10			| type	| value	|
|-|-|-|
| award_dont_popup	| num				| 1 |
| award_image		| str				| 奖品图像？ |
| award_name		| str				| 奖品名称 |
| award_num			| num				| 1 |
| #award_price_text	| str				| |
| award_type		| num				| 0/1 |
| award_users		| [award_num]obj	| 中奖用户 |
| id				| num				| 抽奖id |
| ruid	#			| num				| uid |
| lot_status		| num				| [lot_status](#others) 2 |
| url				| str				| ...... |
| web_url			| str				| "https://live.XXXX.com/p/html/live-lottery/anchor-join.html" |
#### ANCHOR_LOT_AWARD__data__award_users
| key 6	| type	| value	|
|-|-|-|
| uid			| num	| uid |
| uname			| num	| 昵称 |
| face			| num	| 头像URL |
| level			| num	| 直播观众等级 UL |
| color			| num	| 直播观众等级_颜色 num(RGB24) |
| num			| num	| 数量 |
| is_mystery	| bool	| |
| uinfo			| obj	| [uinfo](#pubilc_uinfo) |
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
			{"uid":1,"uname":"A","face":"http:","level":9999,"color":9999,"num":1,"is_mystery":false,"uinfo":{"key":"value"}},
			{"key":"value"}
			{"uid":2,"uname":"Z","face":"https:","level":9999,"color":9999,"num":1,"is_mystery":false,"uinfo":{"key":"value"}}
		],
		"id": 12345,
		"lot_status":2,
		"url": "https://live.XXXX.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url": "https://live.XXXX.com/p/html/live-lottery/anchor-join.html"
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
		"award_users":[{"bag_id":9999,"color":9999,"face":"...","gift_id":31250,"level":9999,"num":1,"uid":9999,"uname":"XXX"}],
		"id":12345,
		"lot_status":2,
		"ruid":9999,
		"url":"https://live.XXXX.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url":"https://live.XXXX.com/p/html/live-lottery/anchor-join.html"}
}
```
----
### POPULAR_RANK_CHANGED
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULAR_RANK_CHANGED" |
| data		| obj	| |
#### POPULAR_RANK_CHANGED__data
| key		| type	| value	|
|-|-|-|
| uid		| num	| 主播uid |
| rank		| num	| [0-100] |
| countdown	| num	| [0-3600] |
| timestamp	| num	| 当前时间TimeStamp(秒) |
| cache_key	| str	| `f"rank_change:{hex_256bit}"` |
```json
{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":12345,"rank":9999,"countdown":9999,"timestamp":1672502400,"cache_key":"rank_change:ffffffffffffffffffffffffffffffff"}}
```
----
### PREPARING
[TOP](#直播弹幕)  
结束直播
| key 4		| type	| value	|
|-|-|-|
| cmd		| str	| "PREPARING" |
| round*	| num	| 1 下播后轮播 |
| roomid	| str	| 长_短直播间ID |
| scatter*	| obj	| |
```json
{"cmd":"PREPARING","roomid":"123"}
{"cmd":"PREPARING","round":1,"roomid":"12345"}
{"cmd":"PREPARING","roomid":"12345","round":1,"scatter":{"max":30,"min":10}}
```
----
### DANMU_MSG
[TOP](#直播弹幕)  
弹幕！
每3秒广播一次，每次最多60个
| key 3,6		| type	| value	|
|-|-|-|
| cmd			| str	| "DANMU_MSG" |
| info			| array	| |
| dm_v2			| str	| base64(proto) UTF-8 [define](#danmu_msg__dm_v2) |
| p_is_ack		| bool	| |
| p_msg_type	| num	| |
| send_time		| num	| |
#### DANMU_MSG__info
| array	| type		| value	| 备注	|
|-|-|-|-|
| 0		| array		| [弹幕属性](#DANMU_MSG__info__0) |
| 1		| str		| `text/content` <br> 弹幕内容/表情包名称 |
| 2		| array		| `userInfo`用户主站信息 | "https://account.XXXX.com/account/home"
| 3		| array		| `fansMedal`[粉丝勋章](#DANMU_MSG__info__3) | "https://link.XXXX.com/p/center/index#/user-center/wearing-center/my-medal"
| 4		| array		| `user_level`[用户直播区信息](#DANMU_MSG__info__4) | "https://link.XXXX.com/p/center/index#/user-center/my-info/operation"
| 5		| array		| `title` [头衔](docs/头衔.md) | https://link.XXXX.com/p/center/index#/user-center/wearing-center/library
| 6		| num		| |
| 7		| num		| `guardLevel`[大航海等级](#others) |
| 8		| null		| |曾经为 obj
| 9		| obj		| [`validation`](#DANMU_MSG__info__9) |
| 10	| num		| |
| 11	| num		| |
| 12	| null		| |
| 13	| null		| |
| 14	| num		| `lpl` |
| 15	| num		| |7 14 21 28 35 42 49 56 63 70 77 105 112 210 220 234 260 520
| 16	| array		| `Wealth`荣耀等级 |
| 17	| null/array	| `groupMedal` |
#### DANMU_MSG__info__0
**弹幕属性**
| array	| type		| value	| 备注	|
|-|-|-|-|
| 0[0]	| num		| 0 |
| 0[1]	| num		| `mode` 弹幕位置 | 0:普通 4:底部
| 0[2]	| num		| `size/fontsize` 弹幕字体大小 | 25
| 0[3]	| num		| `color` 弹幕颜色 |
| 0[4]	| num		| `ctime` | TimeStamp(毫秒)
| 0[5]	| num		| `dmid/rnd/danmakuRnd` <br> 抽奖/弹幕互动游戏 为 0 | WEB:进入直播间时间TimeStamp(秒) <br> iOS/Android:随机(从int32到int64) 2024-01-11 18:21:18
| 0[6]	| num		| |
| 0[7]	| str		| `midHash` | HEX:crc32(uid)
| 0[8]	| num		| |
| 0[9]	| num		| `type/danmakuType` | [0,1,2,7,9] 1:节奏风暴 2:天选时刻 9:弹幕互动游戏
| 0[10]	| num		| `chatBubbleType` | 0,1,2,5
| 0[11]	| str		| `chatBubbleColor` | 5:`"#1453BAFF,#4C2263A2,#3353BAFF"` <br> 2:`"#1453BAFF,#4C2263A2,#3353BAFF"` 1:`"#33FFE99E,#40DCA731,#33FFE99E"`
| 0[12]	| num		| `dm_type/dmType/danmakuSpecialType` | 0:文本 <br> 1:表情包 <br> 2:语音
| 0[13]	| obj/str	| 表情包:[`emoticonOptions`](#DANMU_MSG__info__0__13) <br> `"{}"` |
| 0[14]	| obj/str	| 语音:[`voiceConfig`/`voiceInfo`](#DANMU_MSG__info__0__14) <br> `"{}"` |
| 0[15]	| obj 		| [`emoticons/modeInfo`](#DANMU_MSG__info__0__15) |
| 0[16]	| obj 		| `Aggregation/danmakuAggre`[抽奖](#DANMU_MSG__info__0__16) |20230119
| 0[17]	| num 		| `chatBubbleId/idV2` |20230708+
#### DANMU_MSG__info__2
**用户主站信息/userInfo**
| array	| type	| value	| 备注	|
|-|-|-|-|
| 2[0]	| num	| `uid` | 用户uid
| 2[1]	| str	| `uname/username` | 昵称
| 2[2]	| num	| `isAdmin` | 房管
| 2[3]	| num	| `isVip` |
| 2[4]	| num	| `isSvip` |
| 2[5]	| num	| `rank` | LV0/非正式会员:5000 / 10000
| 2[6]	| num	| `verify` | 手机号验证
| 2[7]	| str	| `usernameColor` | 舰长:`"#00D1F1"` <br> 提督:`"#E17AFF"` <br> 总督:`"#FF7C28"`
#### DANMU_MSG__info__3
**粉丝勋章/fansMedal**
| array	| type	| value	|
|-|-|-|
| 3[0]	| num	| `level` 粉丝勋章 等级 |
| 3[1]	| str	| `label` 粉丝勋章 称号 |
| 3[2]	| num	| `anchorUsername` 主播昵称 |
| 3[3]	| num	| `shortRoomID/RoomID` 长_短直播间ID |
| 3[4]	| num	| [`medalColor`](#medal_color) |
| 3[5]	| str	| `special` "" |
| 3[6]	| num	| `iconId` 0 |
| 3[7]	| num	| [`medalColorBorder`](#medal_color) |
| 3[8]	| num	| [`medalColorStart`](#medal_color) |
| 3[9]	| num	| [`medalColorEnd`](#medal_color) |
| 3[10]	| num	| [`guardLevel`](#others) [大航海等级](#others) |
| 3[11]	| num	| [`isLight`](#粉丝勋章medal_info) |
| 3[12]	| num	| `anchorId` 主播uid |
#### DANMU_MSG__info__4
**用户直播区信息/userLevel/user_level**
| array	| type		| value	| 备注	|
|-|-|-|-|
| 4[0]	| num		| `userLevel` | 用户UL等级
| 4[1]	| num		| 0 |
| 4[2]	| num		| UL等级 颜色 |
| 4[3]	| str/num	| `rank` 直播 用户排名| ">50000" / 当前排名
| 4[4]	| num		| `online_rank` [0,1,2,3] | 高能榜实时排名(仅前三)
#### DANMU_MSG__info__5
**头衔/title**
| array	| type	| value	|
|-|-|-|
| 5[0]	| str	| `old_title` |
| 5[1]	| str	| `title` |
#### DANMU_MSG__info__8
已废弃
| key	| type	| value	|
|-|-|-|
| uname_color	| str	| |
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
| 16[0]	| num	| `wealth level`荣耀等级 |
#### DANMU_MSG__info__16
**groupMedal**
| array	| type	| value	|
|-|-|-|
| 17[0]	| num	| medal_id |
| 17[1]	| str	| name |
| 17[2]	| num	| is_lighted |
#### DANMU_MSG__info__0__13
**表情包1**
| key 7				| type	| value	|
|-|-|-|
| bulge_display		| num	| 0,1 |
| emoticon_unique	| str	| 表情包id |
| height			| num	| 高 px |
| in_player_area	| num	| 0,1 |
| is_dynamic		| num	| 0,1 |
| url				| str	| 表情包URL(http) |
| width				| num	| 宽 px |
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
| user				| obj	| [uinfo](#pubilc_uinfo) |
#### DANMU_MSG__info__0__15__extra
| key 34					| type		| value	| 备注	|
|-|-|-|-|
| send_from_me				| bool		| false |
| mode						| num		| 0 |
| color						| num		| 弹幕颜色 |
| dm_type					| num		| 0:文本 1:表情包 |
| font_size					| num		| 弹幕字体大小 | 25
| player_mode				| num		| 弹幕位置 | 0: 1:滚动 2: 4:底部
| show_player_type			| num		| 0 |
| content					| str		| 弹幕内容/表情包名称 |
| user_hash					| str		| `str(DEC:midHash)` |
| emoticon_unique			| str		| 表情ID |
| bulge_display				| num		| 0:官方表情包 1:房间表情包 |
| recommend_score			| num		| ？弹幕推荐等级/智能屏蔽等级 | 抽奖:0
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
| icon						| obj/null	| [荣耀装扮](https://link.xxx.com/p/eden/news#/newsdetail?id=3531 ) | 2023-06-30 10:58:2x
| show_reply				| bool		| 直播弹幕回复 |
| reply_mid					| num		| 直播弹幕回复 |
| reply_uname				| str		| 直播弹幕回复 |
| reply_uname_color			| str		| 直播弹幕回复 |
| reply_is_mystery			| bool		| 直播弹幕回复 |
| hit_combo					| num		| 0,1 +1弹幕 |
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
#### DANMU_MSG__dm_v2
	~~上线时间 2023-02-17 05:50:13~05:50:24(UTC+8)~~  
	~~下线时间 2023-02-23 19:30~~  
	上线时间 2023-03-23  
	下线时间 2023-10-25
#### DANMU_MSG__example
```json

//假·抽奖弹幕
{"cmd":"DANMU_MSG","info":[[0,1,25,...,...,1702037197,0,"...",0,0,0,"",0,"{}","{}",...,{"activity_identity":       "","activity_source":0,"not_show":0},0],"蔷薇与铳枪",...,...,...,...,0,0,null,...,0,0,null,null,0,49,[.],null]}
//抽奖弹幕
{"cmd":"DANMU_MSG","info":[[0,1,25,...,...,         0,0,"...",0,2,0,"",0,"{}","{}",...,{"activity_identity":"5475890","activity_source":1,"not_show":1},0],"蔷薇与铳枪",...,...,...,...,0,0,null,...,0,0,null,null,0,7,[.],null]}

//hit_combo(+1)
1705563540106664{"cmd":"DANMU_MSG","info":[[0,1,25,xxx,1705563539903,3745805152027139263,0,"xxx",0,0,0,"",0,"{}","{}",{"mode":0,"show_player_type":0,"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":0,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"太卡了x14\",\"user_hash\":\"xxx\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":4,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null,\"is_audited\":false,\"id_str\":\"03653126fb8b16e475d6fbee9765a8d563\",\"icon\":null,\"show_reply\":true,\"reply_mid\":0,\"reply_uname\":\"\",\"reply_uname_color\":\"\",\"reply_is_mystery\":false,\"hit_combo\":1}","user":{"uid":0,"base":{"name":"江***","face":"https://i0.hdslb.com/bfs/face/xxxx.jpg","is_mystery":false,"name_color":0},"medal":null,"wealth":{"level":0}}},{"activity_identity":"","activity_source":0,"not_show":0},0],"太卡了x14",[0,"江***",0,0,0,10000,1,""],[],[5,0,9868950,">50000",0],["",""],0,0,null,{"ts":1705563539,"ct":"ABA7B5C8"},0,0,null,null,0,7,[0],null],"dm_v2":""}
//
17055636102871506{"cmd":"DANMU_MSG","dm_v2":"","info":[[0,1,25,16777215,1705563611817,1705563582,0,"xxx",0,0,0,"",0,"{}","{}",{"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":0,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"1秒1卡\",\"user_hash\":\"xxx\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":2,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null,\"is_audited\":false,\"id_str\":\"54538fc76948f961201ef8e84265a8d542\",\"icon\":null,\"show_reply\":true,\"reply_mid\":0,\"reply_uname\":\"\",\"reply_uname_color\":\"\",\"reply_is_mystery\":false,\"hit_combo\":0}","mode":0,"show_player_type":0,"user":{"base":{"face":"https://i1.hdslb.com/bfs/face/xxxx.jpg","is_mystery":false,"name":"xxx","name_color":0},"medal":null,"uid":0,"wealth":{"level":11}}},{"activity_identity":"","activity_source":0,"not_show":0},0],"1秒1卡",[0,"xxx",0,0,0,10000,1,""],[22,"xxxx","xxxx",xxxx,1725515,"",0,1725515,1725515,5414290,0,1,xxxx],[16,0,6406234,">50000",0],["",""],0,0,null,{"ct":"E7F6BE4E","ts":1705563611},0,0,null,null,0,56,[11],null],"msg_id":"8917998270159360:10:1000","p_is_ack":true,"p_msg_type":1,"send_time":1705563611808}
1706740160948629{"cmd":"DANMU_MSG","info":[[0,1,25,5816798,1706740160512,1447299731,0,"xxx",0,0,0,"",1,{"bulge_display":0,"emoticon_unique":"official_147","height":60,"in_player_area":1,"is_dynamic":0,"url":"http://i0.hdslb.com/bfs/live/bbd9045570d0c022a984c637e406cb0e1f208aa9.png","width":150},"{}",{"mode":0,"show_player_type":0,"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":5816798,\"dm_type\":1,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"赞\",\"user_hash\":\"xxx\",\"emoticon_unique\":\"official_147\",\"bulge_display\":0,\"recommend_score\":0,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null,\"is_audited\":false,\"id_str\":\"4f5977cb13cdf9a336640bb95065bac976\",\"icon\":null,\"show_reply\":true,\"reply_mid\":0,\"reply_uname\":\"\",\"reply_uname_color\":\"\",\"reply_is_mystery\":false,\"hit_combo\":0}","user":{"uid":xxx,"base":{"name":"xxx","face":"https://i2.hdslb.com/bfs/face/xxx.jpg","name_color":0,"is_mystery":false,"risk_ctrl_info":null,"origin_info":{"name":"xxx","face":"https://i2.hdslb.com/bfs/face/xxx.jpg"},"official_info":{"role":0,"title":"","desc":"","type":-1}},"medal":null,"wealth":null,"title":{"old_title_css_id":"","title_css_id":""},"guard":null,"uhead_frame":null,"guard_leader":{"is_guard_leader":false}}},{"activity_identity":"","activity_source":0,"not_show":0},0],"赞",[xxx,"xxx",0,0,0,10000,1,""],[],[5,0,9868950,">50000",0],["",""],0,0,null,{"ts":1706740160,"ct":"5EFA768D"},0,0,null,null,0,7,[8],null],"dm_v2":""}
//弹幕颜色
[
	{"name":"白色",		"color":"16777215",	"color_hex":"ffffff",	"weight":-9999,"color_id":-9999,"origin":0},	//普通
	{"name":"紫色",		"color":"14893055",	"color_hex":"e33fff",	"weight":0,"color_id":6,"origin":1},			//需要成为该主播的船员方可使用哦!
	{"name":"松石绿",	"color":"5566168",	"color_hex":"54eed8",	"weight":99,"color_id":66,"origin":2},			//需粉丝勋章达5级才能使用哦！
	{"name":"雨后蓝",	"color":"5816798",	"color_hex":"58c1de",	"weight":98,"color_id":67,"origin":2},			//需粉丝勋章达15级才能使用哦！
	{"name":"星空蓝",	"color":"4546550",	"color_hex":"455ff6",	"weight":97,"color_id":68,"origin":2},			//需粉丝勋章达22级才能使用哦！
	{"name":"紫罗兰",	"color":"9920249",	"color_hex":"975ef9",	"weight":96,"color_id":69,"origin":2},			//需粉丝勋章达26级才能使用哦！
	{"name":"梦境红",	"color":"12802438",	"color_hex":"c35986",	"weight":95,"color_id":70,"origin":2},			//需粉丝勋章达30级才能使用哦！
	{"name":"热力橙",	"color":"16747553",	"color_hex":"ff8c21",	"weight":94,"color_id":71,"origin":2},			//需粉丝勋章达34级才能使用哦！
	{"name":"香槟金",	"color":"16774434",	"color_hex":"fff522",	"weight":93,"color_id":72,"origin":2},			//需粉丝勋章达38级才能使用哦！
	{"name":"红色",		"color":"16738408",	"color_hex":"ff6868",	"weight":0,"color_id":8,"origin":3},			//成为老爷即可使用哦！
	{"name":"蓝色",		"color":"6737151",	"color_hex":"66ccff",	"weight":0,"color_id":7,"origin":3},			//成为年费老爷即可使用哦!
	{"name":"盛典金",	"color":"16766720",	"color_hex":"ffd700",	"weight":100,"color_id":44,"origin":4},			//在特定活动中才可以获得哦！
	{"name":"升腾蓝",	"color":"4286945",	"color_hex":"4169e1",	"weight":100,"color_id":43,"origin":4},			//在特定活动中才可以获得哦！
	{"name":"青色",		"color":"65532",	"color_hex":"00fffc",	"weight":0,"color_id":5,"origin":4},			//需要完成【度年如日】成就才能使用哦!
	{"name":"绿色",		"color":"8322816",	"color_hex":"7eff00",	"weight":0,"color_id":4,"origin":4},			//需要完成【如雷贯耳】成就才能使用哦!
	{"name":"黄色弹幕",	"color":"16772431",	"color_hex":"ffed4f",	"weight":0,"color_id":3,"origin":4},			//需要完成【腰缠万贯】成就才能使用哦!
	{"name":"橙色",		"color":"16750592",	"color_hex":"ff9800",	"weight":0,"color_id":2,"origin":4},			//需要完成【追云逐月】成就才能使用哦!
	{"name":"粉色",		"color":"16741274",	"color_hex":"ff739a",	"weight":0,"color_id":1,"origin":4}				//拥有“五魁首”头衔时才可使用哟！
]
```
----
### CUT_OFF
[TOP](#直播弹幕)  
切断直播！
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CUT_OFF" |
| msg		| str	| |
| room_id	| num	| 直播间id |
```json
{"cmd":"CUT_OFF","msg":"...","msg_id":"XXX:1000:1000","p_is_ack":true,"room_id":9999,"send_time":9999}
"禁播游戏"
"版权相关"
"违反直播规范"
"直播中涉及低俗内容"
"未持有相关许可，不允许直播相关内容"
"分区错误，直播该游戏请移至虚拟APEX分区直播"
"直播涉及辱骂引战类内容"
"直播互动区含有违规信息，不支持展示互动信息"
"分区错误，直播该游戏请到THE FINALS分区"
"直播中画面涉及低俗内容（如：文字、图片、物品等）"
"游戏中玩家昵称违反直播规范"
"游戏中玩家信息违反直播规范"
"直播内容不适宜"
"麦上发言不当，请调整上麦门槛，再次违规将封禁直播间"
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
#### SHOPPING_CART_SHOW__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 开播:1 下播:2 |
```json
{"cmd":"SHOPPING_CART_SHOW","data":{"status":1}}
{"cmd":"SHOPPING_CART_SHOW","data":{"status":2}}
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
| widget_list	| obj	| "**ID**":{} |
#### WIDGET_BANNER__data__widget_list__ID
| key 15			| type		| value	|
|-|-|-|
| id				| num		| **ID** |
| title				| str		| |
| cover				| str		| "" |
| web_cover			| str		| "" |
| tip_text			| str		| |
| tip_text_color	| str		| |
| tip_bottom_color	| str		| |
| jump_url			| str		| |
| url				| str		| "" |
| stay_time			| num		| 5 |
| site				| num		| 1 |
| platform_in		| [+]str	| ["live","blink","live_link","web","pc_link"] |
| type				| str		| |
| band_id			| num		| |
| sub_key			| str		| |
| sub_data			| str		| urlencoded(json) |
| is_add			| bool		| true |
----
### GOTO_BUY_FLOW
[TOP](#直播弹幕)  
移动端 购买商品
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GOTO_BUY_FLOW" |
| data		| obj	| |
#### GOTO_BUY_FLOW__data
| key	| type	| value	|
|-|-|-|
| text	| str	| |
```json
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**正在去买"}}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等2人正在去买"}}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等3人正在去买"}}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"X**等32人正在去买"}}
```
----
### RECOMMEND_CARD
[TOP](#直播弹幕)  
文档更新：2024-04-22  
商品推销(移动端)  
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
| goods_id								| str		| Timestamp(ns) |
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
{
	"cmd": "RECOMMEND_CARD",
	"data": {
		"title_icon": "https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png",
		"recommend_list": [
			{
				"shopping_card_detail": {
					"goods_id": "xxx",
					"goods_name": "xxx",
					"goods_price": "1.23",
					"goods_max_price": "",
					"sale_status": 0,
					"coupon_name": "",
					"goods_icon": "https://i0.hdslb.com/bfs/garb/item/xxx.jpg",
					"goods_status": 1,
					"source": 5,
					"h5_url": "https://www.bilibili.com/h5/mall/suit/detail?id=xxxxx&navhide=1&rebate=xxx&from_id=xxx&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=5&goods_id=xxx#/virdress",
					"h5_url": "https://www.bilibili.com/h5/mall/digital-card/home?-Abrowser=live&act_id=xxx&hybrid_set_header=2&lottery_id=0&rebate=xxx&from_id=xxx&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=5&goods_id=xxx#/virdress",
					"jump_link": "",
					"schema_url": "",
					"is_pre_sale": 0,
					"activity_info": null,
					"pre_sale_info": null,
					"early_bird_info": null,
					"timestamp": 9999,
					"coupon_discount_price": "",
					"selling_point": "",
					"hot_buy_num": 0,
					"gift_buy_info": null,
					"is_exclusive": false,
					"coupon_id": "",
					"reward_info": null,
					"goods_tag_list": null,
					"virtual_extra_info": {"goods_type": 1,"web_container_type": 1},
					"price_info": {
						"normal": {"prefix_price": "","sale_price": "1.23","suffix_price": "起","strock_price": "","sale_start_time": 9999,"sale_end_time": 0,"strock_show": 1},
						"activity": null
					},
					"btn_info": {"card_btn_status": 1,"card_btn_title": "去抢购","card_btn_style": 1,"card_btn_jumpurl": "","card_btn_route_jump_url": "","card_btn_click_url": ""},
					"goods_sort_id": 0,
					"coupon_info": null,
					"active_info": null,
					"jump_url": ""
				},
				"recommend_card_extra": null
			},
			{"key":"value"}
		],
		"timestamp": 1713608175,
		"update_list": []
	}
}
```
----
### COMMON_NOTICE_DANMAKU
[TOP](#直播弹幕)  
文档更新：2024-04-12  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMMON_NOTICE_DANMAKU" |
| data		| obj	| |
#### COMMON_NOTICE_DANMAKU__data
| key				| type	| value	|
|-|-|-|
| biz_id	？		| num	| 0 |
| content_segments	| []obj	| |
| danmaku_style	？	| obj	| |
| danmaku_uri	？	| str	| "" |
| dmscore			| num	| 144 |
| terminals			| []num	| [1,2,3,4,5] |
#### COMMON_NOTICE_DANMAKU__data__content_segments
| key				| type	| value	|
|-|-|-|
| background_color			| null	| |
| background_color_dark		| null	| |
| font_bold					| bool	| |
| font_color				| str	| |
| font_color_dark			| str	| |
| highlight_font_color		| str	| |
| highlight_font_color_dark	| str	| |
| img_height				| num	| |
| img_url					| str	| |
| img_width					| num	| |
| text						| str	| |
| type						| num	| |
```json
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#FB7299","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"...","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":1008,"terminals":[1,2,3,4,5]}}
```
----
### POPULARITY_RED_POCKET_NEW
[TOP](#直播弹幕)  
红包抽奖
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
| medal_info	| obj	| [medal_info](#粉丝勋章medal_info) |
| wealth_level	| num	| |
```json
{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"lot_id":123,"start_time":1672502400,"current_time":1672502400,"wait_num":0,"uname":"直播小电视","uid":1407831746,"action":"送出","num":1,"gift_name":"红包","gift_id":13000,"price":950,"name_color":"","medal_info":{"target_id":0,"special":"","icon_id":0,"anchor_uname":"","anchor_roomid":0,"medal_level":0,"medal_name":"","medal_color":0,"medal_color_start":0,"medal_color_end":0,"medal_color_border":0,"is_lighted":0,"guard_level":0}}}
{"cmd":"POPULARITY_RED_POCKET_NEW","data":{"lot_id":xxx,"start_time":1697244276,"current_time":1697244276,"wait_num":0,"uname":"xxxxxxxxx","uid":xxxxxxxxxx,"action":"送出","num":1,"gift_name":"红包","gift_id":13000,"price":100,"name_color":"#00D1F1","medal_info":xxx,"wealth_level":xx}}
```
----
### POPULARITY_RED_POCKET_START
[TOP](#直播弹幕)  
红包抽奖
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULARITY_RED_POCKET_START" |
| data		| obj	| |
#### POPULARITY_RED_POCKET_START__data
| key 19			| type		| value	|
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
| h5_url			| str		| f"https://live.XXXX.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId={lot_id}" |
| user_status		| num		| 2 |
| awards			| [3]obj	| |
| lot_config_id		| num		| 红包预设 |
| total_price		| num		| 礼物总价值×0.8 |
| wait_num			| num		| 队列数量 |
| is_mystery		| bool		| |
| sender_uinfo		| obj		| [unifo](#pubilc_uinfo) |
#### POPULARITY_RED_POCKET_START__data__awards
| key		| type	| value	|
|-|-|-|
| gift_id	| num	| 礼物id |
| gift_name	| num	| 礼物名称 |
| gift_pic	| num	| 礼物图像URL(140×140) |
| num		| num	| 数量 |
----
### POPULARITY_RED_POCKET_WINNER_LIST
[TOP](#直播弹幕)  
红包抽奖
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_WINNER_LIST" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_WINNER_LIST__data
| key			| type			| value	|
|-|-|-|
| lot_id		| num			| 抽奖id |
| total_num		| num			| |
| winner_info	| [total_num]	| |
| awards		| obj			| `{gift_id}:{obj...}` |
| version		| num			| 1 |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__winner_info
| array	| type	| value	|
|-|-|-|
| 0		| num	| 获奖者_uid |
| 1		| str	| 获奖者昵称 |
| 2		| num	| `bag_id` |
| 3		| num	| gift_id |
| 4		| bool	| ? |
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
		[12345,"NAME",5157131,31218,false],
		[12345,"NAME",5157132,30971,false],
		[1,2,3,4,5]
		[12345,"NAME",5137362,31278,false],
		[12345,"NAME",5106864,31278,false],
		[12345,"NAME",5167480,31278,false]
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
| uid		| str	| |
| uname		| str	| |
#### ROOM_BLOCK_MSG__data
| key		| type	| value	|
|-|-|-|
| dmscore	| num	| 30 45 90 135 |
| operator	| num	| 1:"房管" 2:"主播" |
| uid		| num	| |
| uname		| str	| |
```json
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":1,"uid":12345,"uname":"xxx"},"uid":"12345","uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":30,"operator":2,"uid":12345,"uname":"xxx"},"uid":"12345","uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":45,"operator":2,"uid":12345,"uname":"xxx"},"uid":"12345","uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":90,"operator":1,"uid":12345,"uname":"xxx"},"uid":"12345","uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"dmscore":135,"operator":1,"uid":12345,"uname":"xxx"},"uid":"12345","uname":"xxx"}
```
----
### AREA_RANK_CHANGED
[TOP](#直播弹幕)  
文档更新：2024-04-12  
timestamp: N×5
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "AREA_RANK_CHANGED" |
| data		| obj	| |
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
| timestamp		| num	| 当前时间 TimeStamp(秒) |
| msg_id		| str	| UUID |
| jump_url_link	| str	| |
| jump_url_pc	| str	| |
| jump_url_pink	| str	| |
| jump_url_web	| str	| |
```json
{
	"cmd": "AREA_RANK_CHANGED",
	"data": {
		"conf_id": 18,
		"rank_name": "聊天热榜",
		"uid": 1340190821,
		"rank": 0,
		"icon_url_blue": "https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png",
		"icon_url_pink": "https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png",
		"icon_url_grey": "https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png",
		"action_type": 2,
		"timestamp": 1706266146,
		"msg_id": "9db34ad1-49f6-4e64-9fab-d77aecdaf7fb",
		"jump_url_link": "https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3......../area-rank",
		"jump_url_pc": "https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4&......../area-rank",
		"jump_url_pink": "https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1&......../area-rank",
		"jump_url_web": "https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2&ruid=1340190821&conf_id=18#/area-rank"
	}
}
```
----
### HOT_BUY_NUM
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "HOT_BUY_NUM" |
| data		| obj	| |
#### HOT_BUY_NUM__data
| key		| type	| value	|
|-|-|-|
| goods_id	| str	| id |
| num		| num	| |
```json
{"cmd":"HOT_BUY_NUM","data":{"goods_id":"xxx","num":9999}}
```
----
### PK_BATTLE_END
[TOP](#直播弹幕)  
| key 8		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_END" |
| pk_id		| str	| |
| pk_status	| num	| # |
| timestamp	| obj	| TimeStamp(秒) |
| data		| obj	| |
#### PK_BATTLE_END__data
| key 6			| type	| value	|
|-|-|-|
| battle_type	| num	| |
| dm_conf		| obj	| |
| timer			| num	| |
| init_info		| obj	| |
| show_streak	| bool	| |
| match_info	| obj	| |
#### PK_BATTLE_END__data__xxinfo
| key 5			| type	| value	|
|-|-|-|
| assist_info	| []obj	| |
| room_id		| num	| 我方直播间id or 对方直播间id |
| votes			| num	| |
| winner_type	| num	| |
| best_uname	| num	| 最高贡献者 |
#### PK_BATTLE_END__data__xxinfo__assist_info
| key 5	| type	| value	|
|-|-|-|
| face	| str	| |
| rank	| num	| |
| score	| num	| |
| uid	| num	| |
| uname	| str	| |
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
{"cmd":"PK_BATTLE_END","data":{"battle_type":2,"timer":10,"init_info":{"room_id":xxx,"votes":xxx,"winner_type":2,"best_uname":"XXX"},"match_info":{"room_id":xxx,"votes":xxx,"winner_type":-1,"best_uname":"YYY"}}}
{"cmd":"PK_BATTLE_END","data":{"battle_type":2,"timer":10,"init_info":{"room_id":xxx,"votes":xxx,"winner_type":3,"best_uname":"XXX"},"match_info":{"room_id":xxx,"votes":xxx,"winner_type":-1,"best_uname":"YYY"}}}
{"cmd":"PK_BATTLE_END","data":{"battle_sub_type":0,"battle_type":2,"dm_conf":{"bg_color":"#72C5E2","font_color":"#FFE10B"},"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":"1","score":"52","uid":"xxx","uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"votes":xxx,"winner_type":2},"match_info":{"assist_info":[],"best_uname":"","room_id":xxx,"votes":0,"winner_type":-1},"show_streak":false,"timer":10},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":"xxx","pk_status":401,"send_time":xxx,"timestamp":xxx}
```
----
### WIDGET_GIFT_STAR_PROCESS
[TOP](#直播弹幕)  
文档更新：2024-01-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WIDGET_GIFT_STAR_PROCESS" |
| data		| obj	| |
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
| level_info		| obj	| |
#### WIDGET_GIFT_STAR_PROCESS__data__process_list
| key			| type	| value	|
|-|-|-|
| gift_id		| num	| |
| gift_img		| str	| |
| gift_name		| str	| |
| completed_num	| num	| |
| target_num	| num	| |
#### WIDGET_GIFT_STAR_PROCESS__data__level_info
| key			| type	| value	|
|-|-|-|
| star_name		| str	| |
| level_tip		| str	| |
| level_img		| str	| |
| level_id		| num	| |
```json
{"cmd":"WIDGET_GIFT_STAR_PROCESS","data":{
	"start_date":20240122,
	"process_list":[
			{"gift_id":31037,"gift_img":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","gift_name":"礼物星球","completed_num":19,"target_num":21},
			{"gift_id":30758,"gift_img":"https://s1.hdslb.com/bfs/live/3ddb10b055b9d1826829ec0fad93ab56484d4a90.png","gift_name":"礼物星球","completed_num":0,"target_num":30},
			{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":5,"target_num":8}
		],
		"finished":false,"ddl_timestamp":1706457600,"version":1706369896898,
		"reward_gift":32267,"reward_gift_img":"https://i0.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球",
		"level_info":{"star_name":"礼物星球","level_tip":"成就Ⅰ","level_img":"https://i0.hdslb.com/bfs/live/a43790d946829348ee506911f8b5a2a752c6de8e.png","level_id":1}
	}
}
```
----
### LIVE_INTERACTIVE_GAME
[TOP](#直播弹幕)  
文档更新：2024-01-20
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_INTERACTIVE_GAME" |
| data		| obj	| |
#### LIVE_INTERACTIVE_GAME__data
| key 17			| type	| value	|
|-|-|-|
| type				| num	| ？2 |
| uid				| num	| |
| uname				| str	| |
| uface				| str	| |
| gift_id			| num	| |
| gift_name			| str	| |
| gift_num			| num	| |
| price				| num	| |
| paid				| bool	| |
| msg				| str	| 弹幕内容/xxx |
| fans_medal_level	| num	| 粉丝勋章等级 |
| guard_level		| num	| [大航海等级](#others) |
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
#### LIVE_MULTI_VIEW_CHANGE__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_MULTI_VIEW_CHANGE","data":{"scatter":{"max":120,"min":5}}}
```
----
### SUPER_CHAT_ENTRANCE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_ENTRANCE" |
| data		| obj	| |
| {roomid}	| num	| |
#### SUPER_CHAT_ENTRANCE__data
| key				| type	| value	|
|-|-|-|
| {status}			| num	| |
| icon				| str	| |
| jump_url			| str	| |
| broadcast_type	| num	| 0/1 |
```json
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","jump_url":"https://live.XXXX.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","status":0}}
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"status":1,"jump_url":"https://live.XXXX.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","broadcast_type":1},"roomid":"xxx"}
```
----
### SYS_MSG
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SYS_MSG" |
| msg		| str	| |
| url		| str	| |
```json
{"cmd":"SYS_MSG","msg":"争夺开启，时间周五20点至周日20点，逾期不候哟！","url":""}	//每周五20:00:59 UTC+8 广播
```
----
### VOICE_JOIN_STATUS
[TOP](#直播弹幕)  
文档更新：2024-04-22  
连麦用户  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_STATUS" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_STATUS__data
| key 13			| type		| value	|
|-|-|-|
| channel			| str		| 直播间ID / "" |
| channel_type		| str		| "voice" |
| current_time		| num		| 当前时间Timestamp(秒) |
| guard				| num		| 大航海等级 / 0 |
| head_pic			| str		| 头像URL / ""|
| is_mystery		| bool		| |
| room_id			| num		| 直播间ID |
| start_at			| num		| 开始时间Timestamp(秒) / 0 |
| status			| num		| 0 / 1 |
| uid				| num		| 连麦UID / 0 |
| uinfo				| null/obj	| |
| user_name			| str		| |
| web_share_link	| str		| 直播间URL |
```json
{"cmd":"VOICE_JOIN_STATUS","data":{"room_id":xxx,"status":0,"channel":"","channel_type":"voice","uid":0,"user_name":"","head_pic":"","guard":0,"start_at":0,"current_time":xxx,"web_share_link":"https://live.XXXX.com/h5/xxx"},"room_id":xxx}
{"cmd":"VOICE_JOIN_STATUS","data":{"channel":"",   "channel_type":"voice","current_time":xxx,"guard":x,"head_pic":"",   "is_mystery":false,"room_id":12345,"start_at":0,  "status":0,"uid":0,  "uinfo":null,"user_name":"",   "web_share_link":"https://live.bilibili.com/h5/12345"},"msg_id":"xxx:1000:1000","p_is_ack":true,"p_msg_type":1,"room_id":12345,"send_time":xxx}
{"cmd":"VOICE_JOIN_STATUS","data":{"channel":"xxx","channel_type":"voice","current_time":xxx,"guard":x,"head_pic":"xxx","is_mystery":false,"room_id":12345,"start_at":xxx,"status":1,"uid":xxx,"uinfo":null,"user_name":"...","web_share_link":"https://live.bilibili.com/h5/12345"},"msg_id":"xxx:1000:1000","p_is_ack":true,"p_msg_type":1,"room_id":12345,"send_time":xxx}
```
----
### DM_INTERACTION
[TOP](#直播弹幕)  
弹幕投票/他们都在说
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "DM_INTERACTION" |
| data		| obj	| |
#### DM_INTERACTION__data
| key		| type	| value	|
|-|-|-|
| id		| num	| |
| status	| num	| 3:开始 4:进行中 5:结束 |
| type		| num	| |
| data		| str	| json |
#### DM_INTERACTION__questiondata__data
| key					| type	| value	|
|-|-|-|
| **question**			| str	| |
| options				| []obj	| |
| vote_id				| num	| |
| cnt					| num	| 投票总数 |
| duration				| num	| 总时长(ms) |
| left_duration			| num	| 剩余时间(ms) |
| fade_duration			| num	| 1000 (ms) |
| waiting_duration		| num	| -1 |
| result				| num	| |
| result_text			| str	| |
| component				| str	| "https://live.XXXX.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0" |
| natural_die_duration	| num	| 30000 |
| my_vote				| num	| | **TODO**
#### DM_INTERACTION__questiondata__data__options
| key		| type	| value	|
|-|-|-|
| idx		| num	| start:1 |
| desc		| str	| 投票选项 |
| cnt		| num	| 投票人数 |
| percent	| float	| 百分比 总计数小于~~5~~时为0 |
#### DM_INTERACTION__combodata__data
| key					| type		| value	|
|-|-|-|
| **combo**				| [1]obj	| |
| merge_interval		| num		| |
| card_appear_interval	| num		| |
| send_interval			| num		| |
#### DM_INTERACTION__combodata__data__combo_0
| key					| type		| value	|
|-|-|-|
| id					| num		| |
| status				| num		| |
| content				| str		| |
| cnt					| num		| |
| guide					| str		| "他们都在说:" |
| left_duration			| num		| 剩余时间(ms) |
| fade_duration			| num		| |
#### DM_INTERACTION__example
```json
{"cmd":"DM_INTERACTION","data":{"id":104,"status":4,"type":101,"data":"{\"question\":\"本局谁将获得胜利？\",\"options\":[{\"idx\":1,\"desc\":\"AAA\",\"cnt\":0,\"percent\":0},{\"idx\":2,\"desc\":\"BBB\",\"cnt\":0,\"percent\":0}],\"vote_id\":12234567,\"cnt\":0,\"duration\":180000,\"left_duration\":179000,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":1,\"result_text\":\"平局\",\"component\":\"https://live.XXXX.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0\",\"natural_die_duration\":30000,\"my_vote\":0}"}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"question\":\"xxxxx\",\"options\":[{\"idx\":1,\"desc\":\"xxxxx\",\"cnt\":1282,\"percent\":0.24066078468180965},{\"idx\":2,\"desc\":\"yyyyy\",\"cnt\":4045,\"percent\":0.7593392153181904}],\"vote_id\":7194538,\"cnt\":5327,\"duration\":180000,\"left_duration\":0,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":3,\"result_text\":\"红获胜\",\"component\":\"https://live.XXXX.com/p/html/live-app-guessing-game/vote.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,324,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,12,0;3,3,100p,324,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,12,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0;8,3,100p,70p,0,0,30,100,12,0\",\"natural_die_duration\":30000,\"my_vote\":0}","id":xxxxx,"status":5,"type":101}}
{"cmd":"DM_INTERACTION","data":{"id":xxx,"status":4,"type":102,"data":"{\"combo\":[{\"id\":xxx,\"status\":4,\"content\":\"****\",\"cnt\":50,\"guide\":\"他们都在说:\",\"left_duration\":19000,\"fade_duration\":20000}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000}"}}
```
----
### PLAY_TAG
[TOP](#直播弹幕)  
比赛 事件(开始,First Blood,击败,Double Kill,大龙,小龙,推塔,结束)
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PLAY_TAG" |
| data		| obj	| |
#### PLAY_TAG__data
| key	| type	| value	|
|-|-|-|
| tag_id	| num	| |
| pic		| str	| 事件pic |
| timestamp	| num	| 事件发生时间TimeStamp(秒) |
| type		| str	| "ADD" |
```json
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e04525fee9ea6ea6973e8bd1116d9f1f6501d37.png","timestamp":xxx,"type":"ADD"}}// Double Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/0e842f1a260e519158712e086e2a10e6fc280e53.png","timestamp":xxx,"type":"ADD"}}// Quadra Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/152132594676ffb27cd1d7992fe02f92b4909540.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/2ac5e22aa856b3b6739bc725cbe78b42b702eec0.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/3c26626a30fdb70e44e16fd4313fa02785486e30.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/5e59bb41b61b015f3665ba922fc1bd6db00c6d32.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/78c10171a17f19fb6f22296091c106852447ce7a.png","timestamp":xxx,"type":"ADD"}}// First Blood [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/7c3cc2cdca443b5fcab636ceaec46d5922c257d5.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/92d895535c9517e13b4cb7d908faaf29aefbcb4a.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/bc1e526e05c11c9ffa515810268fca3d96472af7.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c241edb936a544538207f15a896db867878d262c.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/c56b9ea02e1617a97fc933481b63ffab57ad296c.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/de9d1486f85777cc74798eb1630abba0a695aa15.png","timestamp":xxx,"type":"ADD"}}// Triple Kill [LOL]
{"cmd":"PLAY_TAG","data":{"tag_id":123,"pic":"https://i0.hdslb.com/bfs/live/e01db14207b1a1087d1829db2690753e51080b26.png","timestamp":xxx,"type":"ADD"}}
{"cmd":"PLAY_TAG","data":{"pic":"https://i0.hdslb.com/bfs/live/xxx.png","tag_id":xxx,"timestamp":xxx,"type":"ADD"}}
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
| ids			| [1]num	| |
| queue			| num	| |
| platform_in	| [+]num	| |
```json
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[433],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[514],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[515],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[670],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[949],"queue":2,"platform_in":[1,2]}}
```
----
### TRADING_SCORE
[TOP](#直播弹幕)  
文档更新：2024-04-12  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "TRADING_SCORE" |
| data		| obj	| |
#### TRADING_SCORE__data
| key				| type	| value	|
|-|-|-|
| bubble_show_time	| num	| |
| num				| num	| |
| score_id			| num	| 3 |
| uid				| num	| 主播uid |
| update_time		| num	| 当前时间TimeStamp(秒) |
| update_type		| num	| 1,2 |
```json
{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":200,"score_id":3,"uid":xxx,"update_time":xxx,"update_type":2}}
{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":xxx,"score_id":3,"uid":xxx,"update_time":xxx,"update_type":1}}
```
----
### PK_BATTLE_START_NEW
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_START" "PK_BATTLE_START_NEW" |
| data		| obj	| |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
| roomid	| num	| |
| send_time	| num	| `pk_start_time` |
#### PK_BATTLE_START_NEW__data
| key 13	| type	| value	|
|-|-|-|
| battle_type		| num	| |
| final_conf		| obj	| |
| final_conf > end_time		| num	| |
| final_conf > start_time	| num	| pk_start_time + 120 |
| final_conf > switch		| num	| pk_start_time + 180 |
| final_hit_votes	| num	| |
| init_info			| obj	| |
| match_info		| obj	| |
| pk_countdown		| num	| pk_start_time + 290 |
| pk_end_time		| num	| pk_start_time + 310 |
| pk_frozen_time	| num	| pk_start_time + 300 |
| pk_start_time		| num	| |
| pk_votes_add		| num	| |
| pk_votes_name		| str	| |
| pk_votes_type		| num	| |
| star_light_msg	| str	| |
```json
{"cmd":"PK_BATTLE_START",    "pk_id":xxx,"pk_status":201,"timestamp":xxx,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":xxx,"pk_frozen_time":xxx,"pk_end_time":xxx,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":xxx,"final_conf":{"switch":1,"start_time":xxx,"end_time":xxx},"init_info":{"room_id":xxx,"date_streak":0},"match_info":{"room_id":xxx,"date_streak":0}},"roomid":"xxx"}
{"cmd":"PK_BATTLE_START_NEW","pk_id":xxx,"pk_status":201,"timestamp":xxx,"data":{"battle_type":2,"final_hit_votes":0,"pk_start_time":xxx,"pk_frozen_time":xxx,"pk_end_time":xxx,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":xxx,"final_conf":{"switch":1,"start_time":xxx,"end_time":xxx},"init_info":{"room_id":xxx,"date_streak":0},"match_info":{"room_id":xxx,"date_streak":0}},"roomid":"xxx"}
{"cmd":"PK_BATTLE_START",    "data":{"battle_sub_type":0,"battle_type":2,"final_conf":{"end_time":xxx,"start_time":xxx,"switch":1},"final_hit_votes":0,"init_info":{"date_streak":0,"room_id":AAAA},"match_info":{"date_streak":0,"room_id":BBBB},"pk_countdown":xxx,"pk_end_time":xxx,"pk_frozen_time":xxx,"pk_start_time":xxx,"pk_votes_add":0,"pk_votes_name":"PK值","pk_votes_type":0,"star_light_msg":""},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":xxx,"pk_status":201,"roomid":"xxx","send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_START_NEW","data":{"battle_sub_type":0,"battle_type":2,"final_conf":{"end_time":xxx,"start_time":xxx,"switch":1},"final_hit_votes":0,"init_info":{"date_streak":0,"room_id":AAAA},"match_info":{"date_streak":0,"room_id":BBBB},"pk_countdown":xxx,"pk_end_time":xxx,"pk_frozen_time":xxx,"pk_start_time":xxx,"pk_votes_add":0,"pk_votes_name":"PK值","pk_votes_type":0,"star_light_msg":""},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":xxx,"pk_status":201,"roomid":"xxx","send_time":xxx,"timestamp":xxx}
```
----
### ROOM_SILENT
[TOP](#直播弹幕)  
`ROOM_SILENT_ON` 开启直播间全局禁言  
`ROOM_SILENT_OFF` 解除直播间全局禁言  
| key		| type	| value	|
|-|-|-|
| data		| obj	| |
| cmd		| str	| "ROOM_SILENT_ON" "ROOM_SILENT_OFF" |
#### ROOM_SILENT__data
| key		| type	| value	|
|-|-|-|
| type		| str	| ""关闭 "member"全员禁言 "medal"粉丝勋章等级禁言 "level"UL等级禁言 |
| level		| num	| 粉丝勋章等级/用户UL等级 |
| second	| num	| 结束时间TimeStamp(秒) -1:永久 |
```json
{"data":{"type":"member","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"member"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"member"}}

{"data":{"type":"level","level":1,"second":-1},"cmd":"ROOM_SILENT_ON"}
{"data":{"type":"level","level":60,"second":1672502400},"cmd":"ROOM_SILENT_ON"}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":-1,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":1672502400,"type":"level"}}

{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":-1,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":1672502400,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":1672502400,"type":"medal"}}

{"data":{"type":"","level":0,"second":0},"cmd":"ROOM_SILENT_OFF"}
{"cmd":"ROOM_SILENT_OFF","data":{"level":0,"second":0,"type":""}}
```
```python
match _type:
	case "member":  print(f'主播对用户等级 UL.{level} 以下的用户开启了禁言')
	case "medal":   print(f'主播对粉丝勋章 {level} 以下的用户开启了禁言')
	case "level":   print(f'主播取消了房间禁言')
	case "":        print(f'主播对所有用户开启了禁言')
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
```json
{"cmd":"CHANGE_ROOM_INFO","background":"http://i0.hdslb.com/bfs/live/room_bg/17bb8b588f8371a8582fa443fe2d5a0b7ac01453.jpg","roomid":"21987615"}
{"background":"https://i0.hdslb.com/bfs/live/f3c1e1e22dfb1942bd88c33f1aa174efe7a38dfd.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
{"background":"https://i0.hdslb.com/bfs/live/785922a49980e1aa3239249c8360909488940d7d.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
{"background":"https://i0.hdslb.com/bfs/live/636d66a97d5f55099a9d8d6813558d6d4c95fd61.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
{"background":"https://i0.hdslb.com/bfs/live/2bac063036fbcf316e021fbfb8109ff3028360a6.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
{"background":"https://i0.hdslb.com/bfs/live/2836bb7b84c792e2c6aadfd4d1cce13484775fa3.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
{"background":"https://i0.hdslb.com/bfs/live/2388faed3728f3396052273ad4c3c9af21c411fc.jpg","cmd":"CHANGE_ROOM_INFO"}//默认背景
```
----
### ROOM_CHANGE
[TOP](#直播弹幕)  
标题更改/分区更改  
文档更新：2024-01-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_CHANGE" |
| data		| obj	| |
#### ROOM_CHANGE__data
| key 7				| type	| value	|
|-|-|-|
| title				| str	| 房间标题 |
| area_id			| num	| [子分区ID](#分区ID) |
| parent_area_id	| num	| [父分区ID](#分区ID) |
| area_name			| str	| [子分区name](#分区ID) |
| parent_area_name	| str	| [父分区name](#分区ID) |
| live_key			| str	| [本次直播live_key ==> LIVE](#live) |
| sub_session_key	| str	| [本次直播sub_session_key ==> LIVE](#live) |
```json
{"cmd":"ROOM_CHANGE","data":{"title":"房间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"0","sub_session_key":""}}
{"cmd":"ROOM_CHANGE","data":{"title":"房间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"111111111111111111","sub_session_key":"111111111111111111sub_time:1672502400"}}
```
----
### OBS_SHIELD_STATUS_UPDATE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OBS_SHIELD_STATUS_UPDATE" |
| data		| obj	| |
| roomid	| str	| 直播间id |
#### OBS_SHIELD_STATUS_UPDATE__data
| key		| type	| value	|
|-|-|-|
| change	| num	| 1 |
```json
{"cmd":"OBS_SHIELD_STATUS_UPDATE","data":{"change":1},"roomid":"xxx"}
```
----
### RING_STATUS_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RING_STATUS_CHANGE" |
| data		| obj	| |
#### RING_STATUS_CHANGE__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 0 |
```json
{"cmd":"RING_STATUS_CHANGE","data":{"status":0}}
{"cmd":"RING_STATUS_CHANGE","data":{"status":1}}
```
----
### RING_STATUS_CHANGE_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RING_STATUS_CHANGE_V2" |
| data		| obj	| |
#### RING_STATUS_CHANGE_V2__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 0 |
```json
{"cmd":"RING_STATUS_CHANGE_V2","data":{"status":0}}
{"cmd":"RING_STATUS_CHANGE_V2","data":{"status":1}}
```
----
### VOICE_JOIN_LIST
[TOP](#直播弹幕)  
文档更新：2024-04-22  
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
{"cmd":"VOICE_JOIN_LIST","data":{"apply_count":x,"category":1,"cmd":"","red_point":1,"refresh":1,"room_id":12345},"msg_id":"xxx:1000:1000","p_is_ack":true,"p_msg_type":1,"room_id":12345,"send_time":xxx}
```
----
### VOICE_JOIN_ROOM_COUNT_INFO
[TOP](#直播弹幕)  
文档更新：2024-04-22  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_ROOM_COUNT_INFO" |
| data		| obj	| |
| room_id	| num	| |
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
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"apply_count":xx,"cmd":"","notify_count":0,"red_point":1,"room_id":12345,"room_status":1,"root_status":1},"msg_id":"xxx:1000:1000","p_is_ack":true,"p_msg_type":1,"room_id":12345,"send_time":xxx}

```
----
### ROOM_SKIN_MSG
[TOP](#直播弹幕)  
~1KB
| key 10,11		| type	| value	|
|-|-|-|
| cmd			| str	| "ROOM_SKIN_MSG" |
| skin_id		| num	| |
| status		| num	| 0,1 |
| end_time		| num	| TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| only_local	| bool	| |
| {scatter}		| obj	| |
| skin_config	| obj	| |
#### ROOM_SKIN_MSG__skin_config
| key		| type	| value	|
|-|-|-|
| android	| obj	| |
| ios		| obj	| |
| ipad		| obj	| |
| web		| obj	| |
#### ROOM_SKIN_MSG__skin_config__x__y
| key		| type	| value	|
|-|-|-|
| zip		| str	| |
| md5		| str	| |
| ...		| ...	| "" |
```json
{"cmd":"ROOM_SKIN_MSG","skin_id":64,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/545a91102973626b1e39cec1c7cb93edfd55a7d8.zip","md5":"083B542663A17F47E0379EF7E7269CA3"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/ae3c6c3ca3b32fd21d3612dc7938a5bfce928dcf.zip","md5":"AB4F5A4D83FACA7D45AF2ACCC175CEAF"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/e26c2cb17d3b063d736104926bdeadcacef8a46b.zip","md5":"B2A4F7BD6B4F446BC85980B0B31EF37B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/a6bde45e0de2010afebdeab3572c2d078f2b3525.zip","md5":"9B0E3DEC95E3DB1CDC49CF838B539715","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/78c2321d946dcdf57c37779e674da6983f0850ee.png","giftControlBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/13f1bad1b1c1a050df36beb907d742a6a68d3fdb.png","rankListBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/93db8458c57791f7b89ec75ff54221aa8f33e9fa.png","mainText":"#FFf2ae09","normalText":"#FF999999","highlightContent":"#FFf2ae09","border":"#33999999"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":65,"status":0,"end_time":1672502400,"current_time":1672502400,"only_local":false}
{"cmd":"ROOM_SKIN_MSG","skin_id":452,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c6a13965d7ae8ab433ef05f643876d70ccd35204.zip","md5":"6EFCA3C8FEC1A595B2C185FCAE1741A0"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/8bd0abf11eb68e1867eda7ec74c8ff6bc158392a.zip","md5":"DE24184A495D8AC4D36C40E653EE6F1C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0fb370c451460cb0df6dafec005f7c361b6fbd98.zip","md5":"20B5DE12BC2C20037F30DD0ED76DC67F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/2e2857bbaa31de676896d436e3dadd083c439dc0.zip","md5":"66CF9042BBB331FF056DAB75FC56398E","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0847cbf4e927d494015bfa0ef025c2d38b6a3b7a.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/bfb1140f97cef5d1ed42fe32d9d873db17f1e443.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/3cf53eb68bf888cafd958b26f1257ef892de6e6f.jpg","mainText":"#FFffffff","normalText":"#FFffe2b2","highlightContent":"#FF500c22","border":"#FFffe2b2","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":454,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/c9a6c91cf1b3c0410053ad8d7453f1d3fa877549.zip","md5":"621F5833CE6FD085E800303AFFB4C3FD"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/3b91fa0f1e9e19016afa7af4c488b378657a5897.zip","md5":"716CCAB55B2D95EC8982F324BB59658C"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/0369e00a3b15672638bae9c7363d177ebe437281.zip","md5":"5FCA732A31E2B52AAF674F589C97230F"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/20fe37059dbdf179ba34907496180caf48f9b2fd.zip","md5":"FD0306E4CE4D2848DDD430CD7C72C341","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/d2b7bf6fb6e6d66780a1227e71ea6bdc66dcf0e2.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF6c99dc","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":461,"status":1,"end_time":1672502400,"current_time":1672502400,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/b2e54b7cb64142ee32833d1ed84903fed67a0378.zip","md5":"710AFA69D08FC727EDA821E3AF5CA0C5"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/1143aa4127f6e6faf4ba36c483e506df88b069a8.zip","md5":"55AE9AC3311D58A5EABBABD85366BB2D"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/261dfdb079b3e5ee54f9000cec2274b5f4c5fe7c.zip","md5":"FE1737D3597AC78C791CD408D3A44B3B"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/4d1bccb234baa040e379dfe55467e3ccc76658bf.zip","md5":"3CC0D358666AAEE5B0A8CA6411BA6730","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/0b8ac21001db3bf723fd2f654868361a07114320.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/50b6c93ccdcbdff73589c19eb6138fdf97a95d31.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/b936cd3a73fe2350ae0bfc0aa0321b8d749ff82c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff72a3","border":"#FF4f6dcb","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":538,"status":1,"end_time":1698063358,"current_time":1697804158,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/6cdcee668487be8b8d5c5a90696b7da1678a198b.zip","md5":"7AD3DD23885BFE9169526AA91EB5962C"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/8a0dc065ec23b7768ed3d2f5c831215f2444d0ad.zip","md5":"CD0DCF08E595B67947A12CB9535B9453"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/04e2c6adbfe34fdbf844a5c66a16f11b79738480.zip","md5":"4660CF2EC92D33A7175FD517035A3E76"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/9e10ccf36fbe12336363e21f0163a32c94f1bc54.zip","md5":"33DFDBDD88559B8E5D82424A222A9756","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/64167ef6d5486ad0c340e6c7f5c55e2e2cdebf16.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/7addf50fa8a5d721f576a7ac4dea55299093300c.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/7ab41451281ae01456888c768d33051e68dc7fc8.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff6699","border":"#FFffffff","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":568,"status":1,"end_time":1715529599,"current_time":1714568146,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/db9ca2a0afff4bd38b8679c80646c4cc18a61446.zip","md5":"D428BAFDC22A8B093F75A8BEBF39F0F1"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/37594ebeb312ee3dcfdc7229b788724e798efe7a.zip","md5":"452348483A003E33AE78473C3AECEF66"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/e41ba19fd46f6af1bd04397288a3393686cd1f54.zip","md5":"9F27B6ECC55E5598F69F8E636D7E1674"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/3928e5013a9007dd79719b7f51aaf105ee6594e1.zip","md5":"EE49188B3EDFF053840C2FC073578267","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/474dab9e0628300c15acfe07d677ea924e8c32c4.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/20abf096e96cb500bd9a21d7ed4b3952cf46d60c.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/c9b9035474aaba42607b346e6276c8268be7f20c.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff6699","border":"#FFffffff","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":613,"status":1,"end_time":1714819852,"current_time":1714560656,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/466e44b634513ea4a4ae72ea18d2f5de55859f0c.zip","md5":"6C4B3989850D66D30B690FCDC2F249CA"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/f1d80652ac011138a9e04d85383056dcddf0bebe.zip","md5":"7F3FA7345D8CA6DD7AD7BF1AA0A0B7C3"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/e732cdc996201dc482c2408f459870668e827aaf.zip","md5":"52F4BB872519DA93EABE2CEBD24E9D26"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/2d2cfc2bb0ea98fd20b6f1ae317e36370cb86885.zip","md5":"8CD9913C7FC8D934422E34967D4CD18A","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/a6dd1970b72a7a5b1841ec80d33cbcb9061751a7.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/667b1ec9b26bb891323d283a35887852e1c903f9.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/77e68c586584e8b081d0d2a938b256a28542fa33.jpg","mainText":"#FFffffff","normalText":"#FFffffff","highlightContent":"#FFff6699","border":"#FFffffff","buttonText":"#FFffffff"}}}}
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
{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1701360000,"data":{"is_open":true}}
{"cmd":"PK_BATTLE_ENTRANCE","timestamp":1701360000,"data":{"is_open":false}}
```
----
### LIVE_PANEL_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_PANEL_CHANGE" |
| data		| obj	| |
#### LIVE_PANEL_CHANGE__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_PANEL_CHANGE","data":{"type":2,"scatter":{"max":150,"min":5}}}
{"cmd":"LIVE_PANEL_CHANGE","data":{"scatter":{"max":150,"min":5},"type":2}}
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
//name
guard	online_gold	online_rank	daily_rank	weekly_rank	monthly_rank
//cmd
RANK_REM_GUARD
RANK_REM_RANK
RANK_REM_RANK_NEW
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
| second_line_content			| str	| 舰队规模突破<%XXX%> |
| second_line_highlight_color	| str	| #06DDFF |
| second_line_normal_color		| str	| #FFFFFF |
| show_time						| num	| 3 |
| web_basemap_url				| str	| |
#### GUARD_ACHIEVEMENT_ROOM__anchor_modal
| key							| type	| value	|
|-|-|-|
| first_line_content			| str	| 恭喜当前舰队规模突破<%XXX%> |
| highlight_color				| str	| #00DCFF |
| second_line_content			| str	| 至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～ |
| show_time						| num	| 5 |
```json
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":8,"event_type":1,"face":"...","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":8,"event_type":2,"face":"...","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":false,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":8,"event_type":1,"face":"...","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"","anchor_guard_achieve_level":0,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%0%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":0},"app_basemap_url":"","current_achievement_level":1,"dmscore":8,"event_type":2,"face":"...","first_line_content":"恭喜主播<%XXX%>","first_line_highlight_color":"","first_line_normal_color":"","headmap_url":"","is_first":false,"is_first_new":false,"room_id":1234,"second_line_content":"舰队规模突破<%0%>","second_line_highlight_color":"","second_line_normal_color":"","show_time":3,"web_basemap_url":"普通无需图片"}}
```
----
### PK_BATTLE_FINAL_PROCESS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_FINAL_PROCESS" |
| data		| obj	| |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
#### PK_BATTLE_FINAL_PROCESS__data
| key 2				| type	| value	|
|-|-|-|
| battle_type		| num	| |
| pk_frozen_time	| num	| |
```json
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":xxx},"pk_id":xxx,"pk_status":201,"timestamp":xxx}
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":2,"pk_frozen_time":xxx},"pk_id":xxx,"pk_status":301,"timestamp":xxx}
```
----
### PK_BATTLE_MATCH_TIMEOUT
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "PK_BATTLE_MATCH_TIMEOUT" |
| data	| obj	| |
#### PK_BATTLE_MATCH_TIMEOUT__data
| key			| type	| value	|
|-|-|-|
| battle_type	| num	| |
```json
{"cmd":"PK_BATTLE_MATCH_TIMEOUT","data":{"battle_type":2}}
```
----
### PK_BATTLE_PROCESS_NEW
[TOP](#直播弹幕)  
PK_BATTLE_PROCESS_NEW  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_PROCESS" "PK_BATTLE_PROCESS_NEW" |
| data		| obj	| |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
#### PK_BATTLE_PROCESS_NEW__data
| key			| type	| value	|
|-|-|-|
| battle_type	| num	| |
| init_info		| obj	| |
| match_info	| obj	| |
#### PK_BATTLE_PROCESS_NEW__data__xxx_info
| key			| type		| value	|
|-|-|-|
| room_id		| num		| 我方直播间id or 对方直播间id |
| votes			| num		| |
| best_uname	| num		| 最高贡献者 |
| vision_desc	| num		| |
| assist_info	| null/obj	| |
#### PK_BATTLE_PROCESS_NEW__data__xxx_info__assist_info
| key			| type		| value	|
|-|-|-|
| award_content | str | |
| face | str | |
| is_mystery | bool | |
| rank | num | |
| uid			| num | |
| uinfo			| null/obj | |
| uname			| str | |
```json
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":8,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":9,"best_uname":"XXXX","vision_desc":0},"match_info":{"room_id":4567,"votes":0,"best_uname":"","vision_desc":0}},"pk_id":321224507,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":1,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"...","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":67890,"votes":0,"best_uname":"","assist_info":null},"match_info":{"room_id":12345,"votes":10,"best_uname":"XXXX","assist_info":[{"rank":1,"uid":111,"face":"...","uname":"XXXXX"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"room_id":12345,"votes":2,"best_uname":"XXX","vision_desc":1},"match_info":{"room_id":45,"votes":51,"best_uname":"YYY","vision_desc":-1}},"pk_id":321224459,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"...","uname":"XXX"}]},"match_info":{"room_id":456,"votes":104,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"...","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":6,"init_info":{"room_id":12345,"votes":10,"best_uname":"XXX","assist_info":[{"rank":1,"uid":23456,"face":"...","uname":"XXX"}]},"match_info":{"room_id":456,"votes":105,"best_uname":"YYY","assist_info":[{"rank":1,"uid":67890,"face":"...","uname":"YYY"}]}},"pk_id":321224475,"pk_status":201,"timestamp":1672502400}

{"cmd":"PK_BATTLE_PROCESS",    "data":{"battle_type":2,"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":1,"uid":xxx,"uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"vision_desc":0,"votes":xxx},"match_info":{"assist_info":null,"best_uname":"","room_id":xxx,"vision_desc":0,"votes":0},"trace_id":"xxxxxxxxxxxxxfffffff"},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":xxx,"pk_status":201,"send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":2,"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":1,"uid":xxx,"uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"vision_desc":0,"votes":xxx},"match_info":{"assist_info":null,"best_uname":"","room_id":xxx,"vision_desc":0,"votes":0},"trace_id":"xxxxxxxxxxxxxfffffff"},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":xxx,"pk_status":201,"send_time":xxx,"timestamp":xxx}
```
----
### PK_BATTLE_PRE_NEW
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_PRE_NEW" |
| pk_status	| num	| |
| pk_id		| num	| |
| timestamp	| num	| |
| data		| obj	| |
| roomid	| num	| |
#### PK_BATTLE_PRE_NEW__data
| key 10			| type		| value	|
|-|-|-|
| battle_type		| num		| |
| match_type		| num		| |
| battle_sub_type	| num		| |
| uname				| str		| |
| face				| str		| |
| uid				| num		| |
| room_id			| num		| |
| season_id			| num		| |
| pre_timer			| num		| |
| pk_votes_name		| str		| |
| end_win_task		| null/xxx	| |
```json
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":xxx,"pk_status":101,"status_msg":"","timestamp":1672502400,"data":{"is_followed":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":xxx,"pk_status":101,"status_msg":"","timestamp":1672502400,"data":{"is_followed":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":10000,"pre_timer":10,"pk_votes_name":"","end_win_task":null,"battle_type":6,"match_type":5}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":xxx,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":xxx,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":xxx,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":xxx,"timestamp":1672502400,"data":{"battle_type":2,"match_type":1,"uname":"XXX","face":"...","uid":xxx,"room_id":xxx,"season_id":58,"pre_timer":10,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":xxx,"timestamp":1712322237,"data":{"battle_type":2,"match_type":1,"battle_sub_type":0,"uname":"xxx","face":"...","uid":xxx,"room_id":xxx,"season_id":72,"pre_timer":10,"pk_votes_name":"PK值","end_win_task":null},"roomid":xxx}
```
----
### PK_BATTLE_PUNISH_END
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_PUNISH_END" |
| data		| obj	| |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
#### PK_BATTLE_PUNISH_END__data
| key			| type	| value	|
|-|-|-|
| battle_type	| num	| |
```json
{"cmd":"PK_BATTLE_PUNISH_END","pk_id":"xxx","pk_status":1001,"status_msg":"","timestamp":1672502400,"data":{"battle_type":6}}
```
----
### PK_BATTLE_PRE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_PRE" |
|+PK_BATTLE_PRE_NEW|||
```json
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":101,"pk_id":345038095,"timestamp":1712322237,"data":{"battle_type":2,"match_type":1,"battle_sub_type":0,"uname":"XXX","face":"XXX","uid":xxx,"room_id":xxx,"season_id":72,"pre_timer":10,"pk_votes_name":"PK值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE",                                                             "data":{"battle_sub_type":0,"battle_type":2,"end_win_task":null,"face":"XXX","match_type":1,"pk_votes_name":"PK值","pre_timer":10,"room_id":xxx,"season_id":72,"uid":xxx,"uname":"XXX"},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"pk_id":345038095,"pk_status":101,"roomid":xxx,"send_time":xxx147,"timestamp":xxx}
```
----
### SHOPPING_BUBBLES_STYLE
[TOP](#直播弹幕)  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "SHOPPING_BUBBLES_STYLE" |
| data	| obj	| |
#### SHOPPING_BUBBLES_STYLE__data
| key						| type			| value	|
|-|-|-|
| interval_between_bubbles	| num			| |
| interval_between_queues	| num			| |
| cycle_time				| num			| |
| goods_count				| num			| |
| checksum					| str			| **md5("null")** |
| bubbles_list				| null/[+]obj	| |
```json
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":0,"checksum":"37a6259cc0c1dae299a7866489dff0bd","bubbles_list":null}}
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"bubbles_list":[{"goods_list":[],"name":"N个宝","priority":6,"show_banner":0,"tag":"goodsnum"},{"goods_list":[],"name":"快抢啊","priority":7,"show_banner":0,"tag":"onlyone"}],"checksum":"6f61ed5d5c2f4cab956ad947c9a63878","cycle_time":180,"goods_count":11,"interval_between_bubbles":10,"interval_between_queues":10}}

{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":2,"checksum":"c726710956d46417400c9b555c483588","bubbles_list":[{"tag":"onlyone","name":"快抢啊","priority":7,"show_banner":0,"goods_list":[]}]}}
```
----
### GIFT_STAR_PROCESS
[TOP](#直播弹幕)  
文档更新：2024-01-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_STAR_PROCESS" |
| data		| obj	| |
#### GIFT_STAR_PROCESS__data
| key		| type	| value	|
|-|-|-|
| status	| num	| |
| tip		| str	| |
```json
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"棒棒糖已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"打call已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"动鳗电池已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"干杯已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"告白花束已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"情书已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"水晶之恋已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小蛋糕已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小蝴蝶已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"小花花已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"星河入梦已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"星愿水晶球已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"玉兔已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"月宫玉兔已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"这个好诶已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"绿色战袍已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"星轨列车已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":2,"tip":"所有星球已点亮"}}
```
----
### ANCHOR_NORMAL_NOTIFY
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_NORMAL_NOTIFY" |
| data		| obj	| |
#### ANCHOR_NORMAL_NOTIFY__data
| key		| type	| value	|
|-|-|-|
| info		| obj	| |
| show_type	| num	| |
| type		| num	| |
```json
{"cmd":"ANCHOR_NORMAL_NOTIFY","data":{"type":1,"show_type":1,"info":{"icon":"https://i0.hdslb.com/bfs/live/f3ebd37ee59991bc45538be58e68a6d3aa43ccca.png","title":"","content":"恭喜，获得推荐位buff加持，上推荐的几率大大提高，持续时间：1小时。"}}}
{"cmd":"ANCHOR_NORMAL_NOTIFY","data":{"info":{"content":"恭喜，获得推荐位buff加持，上推荐的几率大大提高，持续时间：1小时。","icon":"https://i0.hdslb.com/bfs/live/f3ebd37ee59991bc45538be58e68a6d3aa43ccca.png","title":""},"show_type":1,"type":1}}
```
----
### LIVE_OPEN_PLATFORM_GAME
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_OPEN_PLATFORM_GAME" |
| data		| obj	| |
#### LIVE_OPEN_PLATFORM_GAME__data
| key						| type		| value	|
|-|-|-|
| msg_type					| str		| "panel_update"/"panel_reset"/"game_end" |
| msg_sub_type				| str		| "panel_update"/"panel_reset"/"game_end" |
| game_name					| str		| |
| game_code					| str		| |
| game_id					| str		| UUID |
| game_status				| str		| |
| game_msg					| str		| |
| game_conf					| str(obj)	| |
| interactive_panel_conf	| str		| |
| timestamp					| num		| 当前时间 TimeStamp(秒) |
| block_uids				| null/[?]	| |
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
{"cmd":"LIVE_OPEN_PLATFORM_GAME","data":{"block_uids":[],"game_code":"16568xxxxxxxx","game_conf":"","game_id":"xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx","game_msg":"","game_name":"弹幕宠物","game_status":"","interactive_panel_conf":"","msg_sub_type":"game_end","msg_type":"game_end","timestamp":1672502400}}
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
```json
{"cmd":"room_admin_entrance","dmscore":45,"level":1,"msg":"系统提示：你已被主播设为房管","uid":xxxx}
```
----
### ROOM_ADMINS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str		| "ROOM_ADMINS" |
| uids		| [+]num	| |
```json
{"cmd":"ROOM_ADMINS","uids":[xxx,yyy]}
```
----
### ROOM_ADMIN_REVOKE
[TOP](#直播弹幕)  
移除房管
| key 6		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_ADMIN_REVOKE" |
| msg		| str	| "撤销房管" |
| uid		| num	| |
```json
{"cmd":"ROOM_ADMIN_REVOKE","msg":"撤销房管","uid":xxxx}
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
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":0,"room_id":xxx,"ts":1672502400}}
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":0,"room_id":xxx,"ts":1672502400}}
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":1,"room_id":xxx,"ts":1672502400}}
```
----
### VOICE_CHAT_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-01-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_CHAT_UPDATE" |
| data		| obj	| |
#### VOICE_CHAT_UPDATE__data
| key	| type	| value	|
|-|-|-|
| url	| str	| |
```json
{"cmd":"VOICE_CHAT_UPDATE","data":{"url":"http://i0.hdslb.com/bfs/live/b7dd570ec64148efab2a97922bb2eebcc29473ca.jpg"}}
```
----
### MESSAGEBOX_USER_GAIN_MEDAL
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_GAIN_MEDAL" |
| data		| obj	| |
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
| medal_color			| num	| [color](#粉丝勋章medal_info) |
| medal_color_border	| num	| [color](#粉丝勋章medal_info) |
| medal_color_end		| num	| [color](#粉丝勋章medal_info) |
| medal_color_start		| num	| [color](#粉丝勋章medal_info) |
| medal_id				| num	| 粉丝勋章id |
| medal_level			| num	| 粉丝勋章等级 |
| medal_name			| str	| 粉丝勋章称号 |
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
{"cmd":"MESSAGEBOX_USER_GAIN_MEDAL","data":{"day_limit":1500,"fan_name":"xxx","guard_level":0,"highlight_color":16478873,"intimacy":xxx,"is_lighted":1,"is_received":1,"is_wear":0,"medal_color":xxx,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_id":xxx,"medal_level":3,"medal_name":"xxx","msg_content":"获得xxx点亲密度\n你的粉丝勋章达到xxx级","msg_title":"恭喜你获得【XXX】的粉丝勋章~","next_intimacy":xxx,"normal_color":xxx,"toast":"成功入团并关注主播，得1级大礼包","today_feed":xxx,"type":3,"uid":xxx,"up_uid":xxxx}}
```
----
### COMBO_SEND
[TOP](#直播弹幕)  
文档更新：2024-04-12  
礼物连击  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMBO_SEND" |
| data		| obj	| |
#### COMBO_SEND__data
| key				| type	| value	|
|-|-|-|
| action			| str		| |
| batch_combo_id	| str		| |
| batch_combo_num	| num		| |
| coin_type			| str		| |
| combo_id			| str		| |
| combo_num			| num		| |
| combo_total_coin	| num		| |
| dmscore			| num		| |
| gift_id			| num		| |
| gift_name			| str		| |
| gift_num			| num		| |
| group_medal		| null/		| |
| is_join_receiver	| bool		| |
| is_naming			| bool		| |
| is_show			| num		| |
| medal_info		| obj		| |
| name_color		| str		| |
| r_uname			| str		| |
| receive_user_info	| obj		| |
| receiver_uinfo	| obj		| |
| ruid				| num		| |
| send_master		| null/ 	| |
| sender_uinfo		| obj		| |
| total_num			| num		| |
| uid				| num		| |
| uname				| str		| |
| wealth_level		| num		| |
```json
{
	"cmd": "COMBO_SEND",
	"data": {
		"action": "投喂",
		"batch_combo_id": "batch:gift:combo_id:AAAA:BBBB:CCCC:DDDD.dddd",
		"batch_combo_num": xxx,
		"coin_type": "gold",
		"combo_id": "gift:combo_id:AAAA:BBBB:CCCC:EEEE.eeee",
		"combo_num": xxx,
		"combo_total_coin": xxx,
		"dmscore": xxx,
		"gift_id": CCCC,
		"gift_name": "...",
		"gift_num": 0,
		"group_medal": null,
		"is_join_receiver": false,
		"is_naming": false,
		"is_show": 1,
		"medal_info": ...,
		"name_color": "",
		"r_uname": "xxx",
		"receive_user_info": {"uid": BBBB,"uname": "xxx"},
		"receiver_uinfo": ...,
		"ruid": BBBB,
		"send_master": null,
		"sender_uinfo": ...,
		"total_num": ...,
		"uid": AAAA,
		"uname": "yyy",
		"wealth_level": xx
	}
}
```
----
### COMBO_END
[TOP](#直播弹幕)  
文档更新：2024-04-30  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMBO_SEND" |
| data		| obj	| |
| is_report	| bool	| true |
| msg_id	| str	| |
| send_time	| num	| |
#### COMBO_SEND__data
| key				| type	| value	|
|-|-|-|
| action			| str	| |
| batch_combo_num	| num	| |
| combo_num			| num	| |
| combo_total_coin	| num	| |
| end_time			| num	| |
| gift_id			| num	| |
| gift_name			| str	| |
| gift_num			| num	| |
| guard_level		| num	| |
| name_color		| str	| |
| price				| num	| |
| r_uname			| str	| |
| ruid				| num	| |
| send_master		| null	| |
| start_time		| num	| |
| uid				| num	| |
| uname				| str	| |
```json
{"cmd":"COMBO_END","data":{"action":"投喂","batch_combo_num":1,"combo_num":1,"combo_total_coin":100,"end_time":AAA,"gift_id":31036,"gift_name":"小花花","gift_num":1,"guard_level":0,"name_color":"","price":100,"r_uname":"XXX","ruid":XXX,"send_master":null,"start_time":AAA,"uid":YYY,"uname":"YYY"},"is_report":false,"msg_id":"XXX","send_time":XXX}
```
----
### ANCHOR_ECOMMERCE_STATUS
[TOP](#直播弹幕)  
文档更新：2023-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_ECOMMERCE_STATUS" |
| data		| obj	| |
#### ANCHOR_ECOMMERCE_STATUS__data
| key		| type	| value	|
|-|-|-|
| status	| num	| |
```json
{"cmd":"ANCHOR_ECOMMERCE_STATUS","data":{"status":1}}
{"cmd":"ANCHOR_ECOMMERCE_STATUS","data":{"status":1},"is_report":false,"msg_id":"XXX","send_time":XXX}
```
----
### ADMIN_SHIELD_KEYWORD
[TOP](#直播弹幕)  
房管：全局屏蔽字符串
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ADMIN_SHIELD_KEYWORD" |
| data		| obj	| |
#### ADMIN_SHIELD_KEYWORD__data
| key	| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ADMIN_SHIELD_KEYWORD","data":{"action":0,"keyword":"text","name":"username","uid":xxx}}
{"cmd":"ADMIN_SHIELD_KEYWORD","data":{"action":1,"keyword":"text","name":"username","uid":xxx}}
```
----
### ANCHOR_HELPER_DANMU
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_HELPER_DANMU" |
| data		| obj	| |
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
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"","button_platform":0,"button_target":"","msg":"XXX取消了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看>","button_platform":3,"button_target":"bililive://xxxx","msg":"发起航海回馈更容易吸引粉丝开通大航海哦","platform":3,"report":"$uid","report_type":"live.live.guard","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看规则","button_platform":3,"button_target":"bililive://xxxx","msg":"您正在新主播扶持中，良好的互动和直播封面，会帮你吸引观众","platform":3,"report":"$uid","report_type":"star_perception","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去看看","button_platform":3,"button_target":"bililive://xxxx","msg":"本周开播满7有效天，必得xxxx元奖励金！今天再收到xxxxxx电池，即可+1天哦","platform":3,"report":"$uid","report_type":"weekly_task","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去领取","button_platform":3,"button_target":"bililive://xxxx","msg":"本周开播满1天，恭喜获得xxx元奖励金。再播1天，再得xxx元奖励金","platform":3,"report":"$uid","report_type":"weekly_task_finish","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":1,"button_name":"去看看","button_platform":3,"button_target":"bililive://blink/open_voicelink","msg":"XXX申请了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"}}
```
----
### CARD_MSG
[TOP](#直播弹幕)  
文档更新：2024-04-30  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CARD_MSG" |
| data		| obj	| |
#### CARD_MSG__data
| key		| type	| value	|
|-|-|-|
| card_type	| str	| |
| card_data	| obj	| |
#### CARD_MSG__data__card_data
| key			| type	| value	|
|-|-|-|
| - | - | - |
| arouse		| num	| |
| interval		| num	| |
| msg			| str	| |
| room_id		| num	| |
| source_event	| num	| |
| uid			| num	| |
```json
{"cmd":"CARD_MSG","data":{"card_data":{"arouse":600,"interval":3,"msg":"主播@你:被我抓到了，怎么还没关注我？","room_id":xxx,"source_event":3,"uid":xxx},"card_type":"daily_recommend"}}
{"cmd":"CARD_MSG","data":{"card_type":"daily_recommend","card_data":{"arouse":600,"interval":3,"msg":"快来关注我，下次直播不迷路~","room_id":xxx,"source_event":3,"uid":xxx}}}
"daily_recommend"
```
----
### ROOM_KICKOUT
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_KICKOUT" |
| data		| obj	| |
| uname		| str	| |
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
#### USER_PANEL_RED_ALARM__data
| key		| type	| value	|
|-|-|-|
| alarm_num	| num	| |
| module	| str	| |
```json
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"live_guard"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":0,"module":"room_gift_panel"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"room_gift_panel"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"panel_bag"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":0,"module":"panel_bag"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":0,"module":"panel_privilege"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"panel_privilege"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":1,"module":"user_head_dot"}}
```
----
### USER_INFO_UPDATE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_INFO_UPDATE" |
| data		| obj	| |
#### USER_INFO_UPDATE__data
| key		| type	| value	|
|-|-|-|
| room_id	| num	| |
| type		| num	| |
| uid		| num	| 主播uid |
```json
{"cmd":"USER_INFO_UPDATE","data":{"room_id":xxx,"type":1,"uid":xxx}}
```
----
### MESSAGEBOX_USER_MEDAL_CHANGE
[TOP](#直播弹幕)  
文档更新：2023-08-xx  
粉丝牌升级  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_MEDAL_CHANGE" |
| data		| obj	| |
#### MESSAGEBOX_USER_MEDAL_CHANGE__data
| key					| type	| value	|
|-|-|-|
| guard_level			| num	| |
| is_lighted			| num	| |
| medal_color_border	| num	| |
| medal_color_end		| num	| |
| medal_color_start		| num	| |
| medal_level			| num	| |
| medal_name			| str	| |
| multi_unlock_level	| str	| |
| MultiUnlockLevel		| []str	| |
| type					| num	| |
| uid					| num	| |
| unlock				| num	| |
| unlock_level			| num	| |
| up_uid				| num	| |
| upper_bound_content	| str	| |
```json
{"cmd":"MESSAGEBOX_USER_MEDAL_CHANGE","data":{"guard_level":xxx,"is_lighted":xxx,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_level":xxx,"medal_name":"xxx","multi_unlock_level":"","type":0,"uid":xxx,"unlock":0,"unlock_level":0,"up_uid":xxx,"upper_bound_content":""}}
{"cmd":"MESSAGEBOX_USER_MEDAL_CHANGE","data":{"MultiUnlockLevel":[],"guard_level":xxx,"is_lighted":xxx,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_level":xxx,"medal_name":"xxx","multi_unlock_level":"","type":1,"uid":xxx,"unlock":0,"unlock_level":0,"up_uid":xxx,"upper_bound_content":"恭喜你的粉丝勋章【xxx】升到xxx级"}}
{"cmd":"MESSAGEBOX_USER_MEDAL_CHANGE","data":{"MultiUnlockLevel":["5"],"guard_level":x,"is_lighted":xx,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_level":5,"medal_name":"xxxxx","multi_unlock_level":"5","type":1,"uid":xx,"unlock":1,"unlock_level":5,"up_uid":xxx,"upper_bound_content":"恭喜你的粉丝勋章【xxx】升到5级"}}
```
----
### WEALTH_NOTIFY
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WEALTH_NOTIFY" |
| data		| obj	| |
#### WEALTH_NOTIFY__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"WEALTH_NOTIFY","data":{"flag":3,"info":{"effect_key":1075,"has_items_changed":1,"level":xx,"send_time":xxx,"status":1}}}
{"cmd":"WEALTH_NOTIFY","data":{"flag":3,"info":{"effect_key":1076,"has_items_changed":1,"level":xx,"send_time":xxx,"status":1}}}
```
----
### ACTIVITY_BANNER_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ACTIVITY_BANNER_CHANGE" |
| data		| obj	| |
#### ACTIVITY_BANNER_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ACTIVITY_BANNER_CHANGE","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","id":3065,"is_close":1,"jump_url":"https://www.XXXX.com/blackboard/live/activity-qMxJDCQ4kQ.html","position":"bottom","timestamp":1690283936}]}}
```
----
### ACTIVITY_BANNER_CHANGE_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ACTIVITY_BANNER_CHANGE_V2" |
| data		| obj	| |
#### ACTIVITY_BANNER_CHANGE_V2__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ACTIVITY_BANNER_CHANGE_V2","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","ext_data":"","id":3065,"is_close":1,"jump_url":"https://www.XXXX.com/blackboard/live/activity-qMxJDCQ4kQ.html","platform_info":[{"build":0,"condition":0,"platform":"android"},{"build":0,"condition":0,"platform":"ios"}],"position":"bottom","type":0}],"timestamp":1690283936}}
```
----
### SPREAD_SHOW_FEET_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SPREAD_SHOW_FEET_V2" |
| data		| obj	| |
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
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":117,"coin_cost":70,"coin_num":100,"cover_btn":"","cover_url":"","live_key":"","order_id":1768xxxx,"order_type":5,"plan_percent":70,"show":8819,"status":1,"timestamp":xxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxxx,"order_type":5,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxxx,"order_type":5,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":2,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":3,"plan_percent":xxxx,"show":xxxx,"status":1,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":3,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxxx,"coin_cost":xxxx,"coin_num":xxxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxxx,"order_type":2,"plan_percent":xxxx,"show":xxxx,"status":2,"timestamp":xxxx,"title":"流量包推广","total_online":xxxx,"uid":xxxx}}
```
----
### PLAYTOGETHER_ICON_CHANGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PLAYTOGETHER_ICON_CHANGE" |
| data		| obj	| |
#### PLAYTOGETHER_ICON_CHANGE__data
| key			| type	| value	|
|-|-|-|
| area_id		| num	| |
| has_perm		| num	| 0,1 |
| show_count	| num	| |
```json
{"cmd":"PLAYTOGETHER_ICON_CHANGE","data":{"area_id":xxx,"has_perm":0,"show_count":0}}
{"cmd":"PLAYTOGETHER_ICON_CHANGE","data":{"area_id":xxx,"has_perm":1,"show_count":0}}
```
----
### STUDIO_ROOM_CLOSE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "STUDIO_ROOM_CLOSE" |
| msg		| str	| |
| roomid	| str	| |
```json
{"cmd":"STUDIO_ROOM_CLOSE","msg":"演播厅模式已关闭，重新开播即可进入正常模式","roomid":"xxx",}
```
----
### PK_BATTLE_VIDEO_PUNISH_END
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_VIDEO_PUNISH_END" |
| data		| obj	| |
| pk_id		| num	| |
| pk_status	| num	| |
| timestamp	| num	| |
```json
{"cmd":"PK_BATTLE_VIDEO_PUNISH_END","pk_id":"xxx","pk_status":1001,"timestamp":xxx}
```
----
### PK_BATTLE_SETTLE_USER
[TOP](#直播弹幕)  
| key 9			| type	| value	|
|-|-|-|
| cmd			| str	| "PK_BATTLE_SETTLE_USER" |
| data			| obj	| |
| pk_id			| num	| |
| pk_status		| num	| |
| settle_status	| num	| |
| timestamp		| num	| |
#### PK_BATTLE_SETTLE_USER__data
| key 9			| type	| value	|
|-|-|-|
| battle_type	| num	| |
| level_info	| obj	| |
| my_info		| obj	| |
| pk_id			| str	| |
| result_info	| obj	| |
| result_type	| num	| |
| season_id		| num	| |
| settle_status	| num	| |
| winner		| obj	| |
#### PK_BATTLE_SETTLE_USER__data__level_info
| key 4				| type	| value	|
|-|-|-|
| first_rank_img	| str	| |
| first_rank_name	| str	| |
| second_rank_icon	| str	| |
| second_rank_num	| num	| |
#### PK_BATTLE_SETTLE_USER__data__my_info//winner
| key 7			| type	| value	|
|-|-|-|
| best_user		| obj	| |
| exp			| obj	| |
| face			| str	| |
| face_frame	| str	| |
| room_id		| num	| |
| uid			| num	| |
| uname			| str	| |
#### PK_BATTLE_SETTLE_USER__data__result_info
| key 17				| type	| value	|
|-|-|-|
| pk_crit_score			| num	| |
| pk_done_times			| num	| |
| pk_extra_score		| num	| |
| pk_extra_score_slot	| str	| |
| pk_extra_value		| num	| |
| pk_resist_crit_score	| num	| |
| pk_task_score			| num	| |
| pk_times_score		| num	| |
| pk_total_times		| num	| |
| pk_votes				| num	| |
| pk_votes_name			| str	| |
| result_type_score		| num	| |
| task_score_list		| []	| |
| total_score			| num	| |
| win_count				| num	| |
| win_final_hit			| num	| |
| winner_count_score	| num	| |
```json
```
### MULTI_VOICE_STATUS_SYNC_ANCHOR
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_STATUS_SYNC_ANCHOR" |
| data		| obj	| |
#### MULTI_VOICE_STATUS_SYNC_ANCHOR__data
| key						| type		| value	|
|-|-|-|
| info						| str(json)	| |
| info	muteFromUID			| num		| |
| info	isMute				| num		| |
| info	uid					| num		| |
| info	muteTrueOperator	| num		| 开启禁言操作者 |
| info	{auth}				| num		| |
| info	{adminSign}			| str		| 256bit |
```json
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":0,\"muteFromUID\":xxx,\"uid\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":1,\"muteFromUID\":xxx,\"uid\":xxx}"}}

{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":0,\"uid\":xxx,\"muteFromUID\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":1,\"uid\":xxx,\"muteFromUID\":xxx}"}}

{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":0,\"uid\":xxx,\"muteFromUID\":xxx,\"auth\":3,\"adminSign\":\"\",\"muteTrueOperator\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":1,\"uid\":xxx,\"muteFromUID\":xxx,\"auth\":3,\"adminSign\":\"\",\"muteTrueOperator\":xxx}"}}

{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":0,\"uid\":xxx,\"muteFromUID\":xxx,\"auth\":3,\"adminSign\":\"ffffffffffffffffffffffffffffffff\",\"muteTrueOperator\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"isMute\":1,\"uid\":xxx,\"muteFromUID\":xxx,\"auth\":3,\"adminSign\":\"ffffffffffffffffffffffffffffffff\",\"muteTrueOperator\":xxx}"}}

{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"muteFromUID\":xxx,\"isMute\":0,\"uid\":xxx,\"auth\":3,\"muteTrueOperator\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"muteFromUID\":xxx,\"isMute\":1,\"uid\":xxx,\"auth\":3,\"muteTrueOperator\":xxx}"}}

{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"muteFromUID\":xxx,\"isMute\":0,\"uid\":xxx,\"muteTrueOperator\":xxx}"}}
{"cmd":"MULTI_VOICE_STATUS_SYNC_ANCHOR","data":{"info":"{\"muteFromUID\":xxx,\"isMute\":1,\"uid\":xxx,\"muteTrueOperator\":xxx}"}}
```
---
### NEW_PK_START
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "NEW_PK_START" |
| data		| obj	| |
| room_id	| num	| |
#### NEW_PK_START__data
| key 17		| type	| value	|
|-|-|-|
| accept_time	| num	| |
| area_name		| str	| |
| attention		| num	| |
| current_time	| num	| |
| face			| str	| |
| fans			| num	| |
| invited_id	| num	| |
| is_nft		| num	| |
| nft_dmark		| str	| |
| once_again	| num	| |
| online		| num	| |
| ready_timeout	| num	| |
| room_id		| num	| |
| toast			| str	| |
| uid			| num	| |
| uname			| str	| |
| virtual_id	| num	| |
```json
```
---
### MULTI_VOICE_OPERATIN
[TOP](#直播弹幕)  
文档更新：2024-04-30  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_OPERATIN" |
| data		| obj	| |
#### MULTI_VOICE_OPERATIN__data
| key		| type	| value	|
|-|-|-|
| {hat}							| null/xxx	| |
| {pk_group_total_price}		| num		| |
| {pk_group_total_price_text}	| str		| |
| {pk_group_id}					| str		| |
| pk_total_price				| num		| |
| pk_total_price_text			| str		| |
| position						| num		| |
| room_id						| num		| |
| total_price					| str		| |
| total_price_text				| str		| |
| ts							| num		| 100ns |
| uid							| num		| |
| version						| num		| --> ts |
```json
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"pk_group_id":"xxx","pk_group_total_price":xxx,"pk_group_total_price_text":"xxx","pk_total_price":xxx,"pk_total_price_text":"xxx","position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"send_time":xxx}
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"pk_group_total_price_text":"xxx","pk_total_price_text":"xxx","position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"send_time":xxx}
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx},"msg_id":"XXX:1000:1000","p_is_ack":true,"p_msg_type":1,"send_time":xxx}
```
---
### MULTI_VOICE_ENTER_ANCHOR
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_ENTER_ANCHOR" |
| data		| obj	| |
#### MULTI_VOICE_ENTER_ANCHOR__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
want_position -1 0-8
actual_position 0-8
gender -1 0 1
role 0 1 2
{"cmd":"MULTI_VOICE_ENTER_ANCHOR","data":{"actual_position":xxx,"anchor_uid":xxx,"avatar":"https://ix.hdslb.com/bfs/face/member/noface.jpg","gender":xxx,"nickname":"xxx","role":xxx,"uid":xxx,"version":xxx,"want_position":xxx}}
{"cmd":"MULTI_VOICE_ENTER_ANCHOR","data":{"actual_position":xxx,"anchor_uid":xxx,"avatar":"https://ix.hdslb.com/bfs/face/xxx.xxx","gender":xxx,"nickname":"xxx","role":xxx,"uid":xxx,"version":xxx,"want_position":xxx}}
```
---
### MULTI_VOICE_OWNER_LEAVE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_OWNER_LEAVE" |
| data		| obj	| |
#### MULTI_VOICE_OWNER_LEAVE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"MULTI_VOICE_OWNER_LEAVE","data":{"toast":"主播网络异常"}}
```
---
### MULTI_VOICE_PK_STATUS
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_PK_STATUS" |
| data		| obj	| |
#### MULTI_VOICE_PK_STATUS__data
| key					| type		| value	|
|-|-|-|
| anchor_join			| num		| |
| anchor_uid			| num		| |
| break_toast			| str		| |
| create_uid			| num		| |
| curr_phase			| num		| |
| curr_phase_duration	| num		| |
| curr_phase_remaining	| num		| |
| curr_phase_start_time	| str		| |
| end_toast				| str		| |
| end_uid				| num		| |
| group					| \[2\]obj	| |
| pk_id					| str		| |
| pk_type				| num		| |
| positions				| \[1\~8\]obj	| |
| result				| num		| |
| room_id				| num		| |
| start_toast			| str		| |
| version				| num		| |
#### MULTI_VOICE_PK_STATUS__data__group
| key					| type		| value	|
|-|-|-|
| anchor_join			| num		| |
| group_id				| str		| |
| price					| num		| |
| price_text			| str		| |
#### MULTI_VOICE_PK_STATUS__data__positions
| key					| type		| value	|
|-|-|-|
| IsMystery				| bool		| |
| Uinfo					| null/xxx	| |
| animate_avatar		| null/xxx	| |
| avatar				| str		| |
| business_list			| null		| |
| group_id				| str		| |
| hat					| null/xxx	| |
| head_frame			| null/obj	| |
| is_mute				| num		| |
| mute_from_uid			| num		| |
| nickname				| str		| |
| pk_price				| num		| |
| pk_price_text			| str		| |
| pos					| num		| |
| price					| num		| |
| price_text			| str		| |
| role					| num		| |
| uid					| num		| |
---
### INTERACT_JOIN
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_JOIN" |
---
### INTERACT_JOIN_OLD
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_JOIN_OLD" |
---
### SPREAD_ORDER
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SPREAD_ORDER_START" "SPREAD_ORDER_OVER" |
| data		| obj	| |
#### SPREAD_ORDER__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"SPREAD_ORDER_START","data":{"order_id":xxx,"order_status":1,"roomid":xxx,"timestamp":xxx,"uid":xxx}}
{"cmd":"SPREAD_ORDER_OVER","data":{"order_id":xxx,"order_status":0,"timestamp":xxx,"uid":xxx}}
```
---
### ANCHOR_BROADCAST
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_BROADCAST" |
| data		| obj	| |
#### ANCHOR_BROADCAST__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
---
### PK_BATTLE_SETTLE_NEW
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_SETTLE_NEW" |
| data		| obj	| |
#### PK_BATTLE_SETTLE_NEW__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
```
---
### ROOM_NEWS_UPDATE
[TOP](#直播弹幕)  
主播公告 更新?
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_NEWS_UPDATE" |
| data		| obj	| |
#### ROOM_NEWS_UPDATE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ROOM_NEWS_UPDATE","data":{"content_is_open":true,"icon":"https://i0.hdslb.com/bfs/live/7502ba91c9564454d785a1d2dcc5151556f7678c.png","news_content":"xxxxxxxx\nxxxxxxxx","news_page":"","news_type":2}}
{"cmd":"ROOM_NEWS_UPDATE","data":{"content_is_open":true,"icon":"https://i0.hdslb.com/bfs/live/7502ba91c9564454d785a1d2dcc5151556f7678c.png","news_content":"xxxxxxxx","news_page":"","news_type":1}}
```
---
### MULTI_VOICE_APPLICATION_ANCHOR
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_APPLICATION_ANCHOR" |
| data		| obj	| |
#### MULTI_VOICE_APPLICATION_ANCHOR__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"MULTI_VOICE_APPLICATION_ANCHOR","data":{"anchor_uid":xxx,"channel":"","count":xxx,"event":xxx,"operate_uid":xxx,"role":0,"roomId":0,"toast":"取消了连麦申请","uid":xxx,"want_position":xxx}}
{"cmd":"MULTI_VOICE_APPLICATION_ANCHOR","data":{"anchor_uid":xxx,"channel":"","count":xxx,"event":xxx,"operate_uid":xxx,"role":0,"roomId":0,"toast":"申请了连麦","uid":xxx,"want_position":xxx}}
{"cmd":"MULTI_VOICE_APPLICATION_ANCHOR","data":{"anchor_uid":xxx,"channel":"","count":xxx,"event":xxx,"operate_uid":xxx,"role":0,"roomId":0,"toast":"主播拒绝了申请","uid":xxx,"want_position":xxx}}
```
---
### MULTI_VOICE_APPLICATION_USER
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_APPLICATION_USER" |
| data		| obj	| |
#### MULTI_VOICE_APPLICATION_USER__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"MULTI_VOICE_APPLICATION_USER","data":{"anchor_uid":xxx,"channel":"","count":xxx,"event":1,"operate_uid":0,"role":0,"roomId":xxx,"toast":"申请了连麦","uid":xxx,"want_position":xxx}}
{"cmd":"MULTI_VOICE_APPLICATION_USER","data":{"anchor_uid":xxx,"channel":"","count":xxx,"event":4,"operate_uid":0,"role":0,"roomId":xxx,"toast":"取消了连麦申请","uid":xxx,"want_position":xxx}}
```
---
### GIFT_BOARD_RED_DOT
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_BOARD_RED_DOT" |
| data		| obj	| |
| is_report	| bool	| true |
| msg_id	| str	| |
| send_time	| num	| |
#### GIFT_BOARD_RED_DOT__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"GIFT_BOARD_RED_DOT","data":{"categoryL1":"3"},"is_report":false,"msg_id":"xxx","send_time":xxx}
```
---
### LITTLE_MESSAGE_BOX
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LITTLE_MESSAGE_BOX" |
| data		| obj	| |
#### LITTLE_MESSAGE_BOX__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LITTLE_MESSAGE_BOX","data":{"from":"fans_medal","msg":"今日首条弹幕发送成功~亲密度+100","platform":{"android":true,"ios":true,"web":true},"room_id":xxx,"type":1}}
```
---
### ROOM_NEWS_AUDIT_CHANGE
[TOP](#直播弹幕)  
主播公告 更新?
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_NEWS_AUDIT_CHANGE" |
| data		| obj	| |
#### ROOM_NEWS_AUDIT_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ROOM_NEWS_AUDIT_CHANGE","data":{"audit_status":1,"news_content":"xxxxxxxx","news_type":2,"room_id":xxx}}
```
---
### MULTI_VOICE_PK_HAT_STATUS
[TOP](#直播弹幕)  
...
---
### PK_BATTLE_SETTLE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_SETTLE" |
| data		| obj	| |
#### PK_BATTLE_SETTLE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_SETTLE","pk_id":xxx,"pk_status":401,"settle_status":1,"timestamp":xxx,"data":{"battle_type":2,"result_type":2,"star_light_msg":""},"roomid":"xxx"}
```
---
### PK_BATTLE_SETTLE_V2
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_SETTLE_V2" |
| data		| obj	| |
#### PK_BATTLE_SETTLE_V2__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_SETTLE_V2","pk_id":xxx,"pk_status":401,"settle_status":1,"timestamp":xxx,"data":{"pk_id":"xxx","season_id":66,"pk_type":2,"result_type":2,"result_info":{"total_score":xxx,"pk_votes":xxx,"pk_votes_name":"PK值","pk_extra_value":0},"level_info":{"uid":"455592866","first_rank_name":"青铜萌新","second_rank_num":2,"first_rank_img":"https://i0.hdslb.com/bfs/live/bd6ca767900adbda7cd7148db06f72726bef7813.png","second_rank_icon":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png"},"assist_list":[{"id":xxx,"uname":"xxx","face":"x","score":60},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx}],"star_light_msg":""}}
```
---
### PK_BATTLE_VIDEO_PUNISH_BEGIN
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_VIDEO_PUNISH_BEGIN" |
| data		| obj	| |
#### PK_BATTLE_VIDEO_PUNISH_BEGIN__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_VIDEO_PUNISH_BEGIN","pk_id":"xxx","pk_status":701,"timestamp":xxx,"data":{"battle_type":2,"init_info":{"room_id":xxx,"votes":xxx,"winner_type":-1,"best_uname":"xxx"},"match_info":{"room_id":xxx,"votes":xxx,"winner_type":2,"best_uname":"xxx"},"video_punish":{"duration":180,"punish_name":"惩罚"}}}
```
---
### LIVE_ROOM_TOAST_MESSAGE
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_ROOM_TOAST_MESSAGE" |
| data		| obj	| |
#### LIVE_ROOM_TOAST_MESSAGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_ROOM_TOAST_MESSAGE","data":{"message":"由于对方主播提前结束PK，本轮PK我方主播获胜","timestamp":xxx},"timestamp":xxx}
```
---
---
### LIVE_PANEL_CHANGE_CONTENT
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_PANEL_CHANGE_CONTENT" |
| data		| obj	| |
#### LIVE_PANEL_CHANGE_CONTENT__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{
	"cmd":"LIVE_PANEL_CHANGE_CONTENT",
	"data":{
		"setting_list":[
			{"biz_id":1001,"icon":"http://i0.hdslb.com/bfs/live/afd5bc2424ebf7c7c9c68d71ba5a1f7d08154519.png","title":"分享","note":"分享","weight":100,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1012,"icon":"http://i0.hdslb.com/bfs/live/1e3cb35056ebbcc1af5f08f4fe7916f095db26a5.png","title":"管理员","note":"管理员","weight":36,"status_type":1,"notification":null,"custom":null,"jump_url":"https://live.bilibili.com/p/html/live-app-room-admin/index.html?is_live_half_webview=1#/roomManagement","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1011,"icon":"http://i0.hdslb.com/bfs/live/7dbaf07b4c10182aeb0e7a8eda3273d40bb9b9b5.png","title":"小窗播放","note":"小窗播放","weight":15.001,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1003,"icon":"http://i0.hdslb.com/bfs/live/a5407c843e72d5efb678b649aecd7184f0d68494.png","title":"播放设置","note":"播放设置","weight":9,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1004,"icon":"http://i0.hdslb.com/bfs/live/1a1b3b9819f78df76f66b3657a6be2cc0e9b8853.png","title":"弹幕设置","note":" 弹幕设置","weight":8,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1002,"icon":"http://i0.hdslb.com/bfs/live/1b19309441c997d8e9a19ddb939ff6dda2a04a64.png","title":"画质","note":"画质","weight":7,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1005,"icon":"http://i0.hdslb.com/bfs/live/12d66e639a677df2e8b6630a9abe06806acce87d.png","title":"隐藏特效","note":"隐藏特效","weight":6,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1008,"icon":"http://i0.hdslb.com/bfs/live/fe04b9ab783d3a0a4798c20303166b07dcdf8f1d.png","title":"投屏","note":"投屏","weight":5,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1007,"icon":"http://i0.hdslb.com/bfs/live/7e25a262e1cdf294a5d6ca2b1b1527ef4f7caf62.png","title":"举报","note":"举报","weight":5,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1009,"icon":"http://i0.hdslb.com/bfs/live/8e41f28e574952208fe73d09d464c8b369a1a4e9.png","title":"反馈","note":"反馈","weight":4,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1013,"icon":"https://i0.hdslb.com/bfs/live/856061fa98257d996a34850ef4f7a052af6fb3a3.png","title":"清屏","note":"清屏","weight":3,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1006,"icon":"http://i0.hdslb.com/bfs/live/628cdab93480f1f3dfcb4430a1ff08c81c1b6aec.png","title":"仅播声音","note":"仅播声音","weight":2,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1014,"icon":"http://i0.hdslb.com/bfs/live/0884ed6a7c55baf37554c15d79e03c7948421d9b.png","title":"色 觉优化","note":"色觉优化","weight":1,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":1010,"icon":"http://i0.hdslb.com/bfs/live/1c8331a2c520093a830df0ebf9b5f58eb28cd22d.png","title":"添至桌面","note":"添至桌面","weight":1,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null}
			],
		"interaction_list":[
			{"biz_id":999,"icon":"https://i0.hdslb.com/bfs/live/6c068a5ec8e316ca1b3c9a97ba8e47707b3a0fc8.png","title":" 魔法奇遇","note":"魔法奇遇","weight":1,"status_type":1,"notification":null,"custom":[{"icon":"https://i0.hdslb.com/bfs/live/6c068a5ec8e316ca1b3c9a97ba8e47707b3a0fc8.png","title":"魔法奇遇","note":"魔法奇遇","jump_url":"https://live.bilibili.com/activity/live-activity-full/full-next/index.html?app_name=magical_adventure&-Abrowser=live&is_live_half_webview=1&source_event=1&hybrid_half_ui=1,3,100p,80p,0,0,30,100,15,0;2,2,375,100p,0,0,30,100,15,0;3,3,100p,80p,0,0,30,100,15,0;4,2,375,100p,0,0,30,100,15,0;5,3,100p,80p,0,0,30,100,15,0;6,3,100p,80p,0,0,30,100,15,0;7,3,100p,80p,0,0,30,100,15,0;8,3,100p,80p,0,0,30,100,15,0&room_id=5440&uid=9617619#/","status":0,"sub_icon":"https://i0.hdslb.com/bfs/live/a21478ac7eba92d69ddc7655666083d03756a683.png"}],"jump_url":"https://live.bilibili.com/activity/live-activity-full/full-next/index.html?app_name=magical_adventure&-Abrowser=live&is_live_half_webview=1&source_event=1&hybrid_half_ui=1,3,100p,80p,0,0,30,100,15,0;2,2,375,100p,0,0,30,100,15,0;3,3,100p,80p,0,0,30,100,15,0;4,2,375,100p,0,0,30,100,15,0;5,3,100p,80p,0,0,30,100,15,0;6,3,100p,80p,0,0,30,100,15,0;7,3,100p,80p,0,0,30,100,15,0;8,3,100p,80p,0,0,30,100,15,0&room_id=5440&uid=9617619#/","type_id":2,"tab":{"type":"H5","biz_type":"common-H5","tab_comment":null,"tab_topic":null,"aggregation":0,"id":0,"sub_title":"","sub_icon":"","show_outer_aggregation":0,"show_guide_bubble":"","global_id":"","biz_info":""},"dynamic_icon":"","sub_icon":"https://i0.hdslb.com/bfs/live/a21478ac7eba92d69ddc7655666083d03756a683.png","panel_icon":"http://i0.hdslb.com/bfs/live/c339a3569df7351406f29afae77a917aec3073a3.png","match_entrance":0,"icon_info":null}
			],
		"outer_list":[
			{"biz_id":997,"icon":"https://i0.hdslb.com/bfs/live/273904e5c84d293f5f9df5ade5ac0fadc34e9fad.png","title":"送礼","note":"","weight":100,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"https://i0.hdslb.com/bfs/live/a812dfafd427714b3623a352618ca70fa0379c75.webp","sub_icon":"https://i0.hdslb.com/bfs/live/b0b675140c28310a0ff54b05b2fd9a11a5898acf.png","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":33,"icon":"https://i0.hdslb.com/bfs/live/a0e4a9381f9627d2ed89ab67d5ccce1bc1de7ea3.png","title":"购物车","note":"购物车","weight":100,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"https://i0.hdslb.com/bfs/live/76b00ae4363ab572be565dbb62fd44d7c6c7d198.png","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":998,"icon":"https://i0.hdslb.com/bfs/live/ec39c5ec3185f58608e4c143f2461726794403b0.png","title":"更多","note":"","weight":99,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":30,"icon":"https://s1.hdslb.com/bfs/live/53903499f1134661b3b7df5109de59f747d09498.png","title":"快捷送礼","note":"快捷送礼","weight":97,"status_type":1,"notification":null,"custom":[{"icon":"https://s1.hdslb.com/bfs/live/53903499f1134661b3b7df5109de59f747d09498.png","title":"","note":"{\"bubble_text\":\"点击投喂一个%s，让主播感受到你的支持！\",\"desc_text\":\"投喂一个%s支持主播~\",\"duration\":5,\"gift_id\":33996}","jump_url":"","status":0,"sub_icon":"https://s1.hdslb.com/bfs/live/53903499f1134661b3b7df5109de59f747d09498.png"}],"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"https://s1.hdslb.com/bfs/live/53903499f1134661b3b7df5109de59f747d09498.png","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":16,"icon":"https://i0.hdslb.com/bfs/live/024b6050b1cf11ed656a499f013ca14681a131c6.png","title":"表情包","note":"表情包","weight":90,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"https://i0.hdslb.com/bfs/live/57b7d3953b5663931c59f7e889cef76950591f03.png","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":2,"icon":" ","title":"语音连麦","note":" ","weight":5,"status_type":1,"notification":null,"custom":[{"icon":"https://i0.hdslb.com/bfs/live/e3a8c212bc493b88a33fe1853a16270e22d9a70b.png","title":"","note":"连麦功能关闭","jump_url":"","status":2,"sub_icon":"https://i0.hdslb.com/bfs/live/e429e283dbd9e25092a5a73b604527a646cbad32.png"},{"icon":"https://i0.hdslb.com/bfs/live/b8cabd73def53d85bd092f4e8b3f9f6534ec2dc6.png","title":"","note":"连麦","jump_url":"","status":1,"sub_icon":"https://i0.hdslb.com/bfs/live/9500b71c99451040e96312a0f60f269f5c6f0100.png"},{"icon":"https://i0.hdslb.com/bfs/live/c25451d846c5c36a56874626c6496743e6c8b726.webp","title":"","note":"等待中","jump_url":"","status":3,"sub_icon":"https://i0.hdslb.com/bfs/live/0a4e8a81ccc673d7985b6a3c9ecc88baaa0c1e35.webp"},{"icon":"https://i0.hdslb.com/bfs/live/bcf5f48883ddbb96c8680bcc9ed2d4c11798e526.webp","title":"","note":"连麦中","jump_url":"","status":4,"sub_icon":"https://i0.hdslb.com/bfs/live/846230df75319bbe171db0e0d18ec5a8a80e514b.webp"}],"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
			{"biz_id":3,"icon":"https://i0.hdslb.com/bfs/live/a02f9edd13bf77588ec8ed800cf246fbbc158ff3.png","title":"醒目留言","note":"留言传递心意吧","weight":2.1,"status_type":1,"notification":null,"custom":null,"jump_url":"","type_id":2,"tab":null,"dynamic_icon":"","sub_icon":"https://i0.hdslb.com/bfs/live/da519a9d33dd9cf8d6bb38c481cea9180341abbe.png","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null}
			],
		"panel_data":null,
		"is_fixed":0,
		"is_match":0,
		"match_cristina":"",
		"match_icon":"",
		"match_bg_image":""
	}
}
```
---
### GIFT_PANEL_PLAN
[TOP](#直播弹幕)  
~10KB
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_PANEL_PLAN" |
| data		| obj	| |
#### GIFT_PANEL_PLAN__data
| key				| type			| value	|
|-|-|-|
| gift_list			| []obj			| |
| special_type_sort	| null/[]num	| |
| action			| num			| |
#### GIFT_PANEL_PLAN__data__gift_list
| key				| type		| value	|
|-|-|-|
| gift_id			| num			| |
| config			| null/obj		| |
| full_sc_effect	| null/[1]obj	| |
| float_sc_effect	| null			| |
| special_type		| num			| |
| show				| bool			| |
#### GIFT_PANEL_PLAN__data__gift_list__config
| key				| type	| value	|
|-|-|-|
| id | num | |
| name | str | |
| price | num | |
| type | num | |
| coin_type | str | |
| bag_gift | num | |
| effect | num | |
| corner_mark | str | |
| corner_background | str | |
| broadcast | num | |
| draw | num | |
| stay_time | num | |
| animation_frame_num | num | |
| desc | str | |
| rule | str | |
| rights | str | |
| privilege_required | num | |
| count_map | [1]obj | |
| img_basic | str | |
| img_dynamic | str | |
| frame_animation | str | |
| gif | str | |
| webp | str | |
| full_sc_web | str | |
| full_sc_horizontal | str | |
| full_sc_vertical | str | |
| full_sc_horizontal_svga | str | |
| full_sc_vertical_svga | str | |
| bullet_head | str | |
| bullet_tail | str | |
| limit_interval | num | |
| bind_ruid | num | |
| bind_roomid | num | |
| gift_type | num | |
| combo_resources_id | num | |
| max_send_limit | num | |
| weight | num | |
| goods_id | num | |
| has_imaged_gift | num | |
| left_corner_text | str | |
| left_corner_background | str | |
| gift_banner | null/xxx | |
| diy_count_map | num | |
| effect_id | num | |
| first_tips | str | |
| gift_attrs | [1]num | |
| corner_mark_color | str | |
| corner_color_bg | str | |
| web_light | obj | |
| web_dark | obj | |
#### GIFT_PANEL_PLAN__data__gift_list__config__count_map
| key				| type	| value	|
|-|-|-|
| num | num | |
| text | str | |
| desc | str | |
| web_svga | str | |
| vertical_svga | str | |
| horizontal_svga | str | |
| special_color | str | |
| effect_id | num | |
#### GIFT_PANEL_PLAN__data__gift_list__config__web_light+web_dark
| key				| type	| value	|
|-|-|-|
| corner_mark | str | |
| corner_background | str | |
| corner_mark_color | str | |
| corner_color_bg | str | |
#### GIFT_PANEL_PLAN__data__gift_list__full_sc_effect
| key				| type	| value	|
|-|-|-|
| type | num | |
| web_svga | str | |
| horizontal_svga | str | |
| vertical_svga | str | |
| web_mp4 | str | |
| web_mp4_json | str | |
| horizontal_mp4 | str | |
| vertical_mp4 | str | |
| id | num | |
| plan_platform | list | |
| bind_gift_ids | list | |
| web_mp4_md5 | str | |
| horizontal_mp4_md5 | str | |
| vertical_mp4_md5 | str | |
| web_mp4_crc32 | num | |
| horizontal_mp4_crc32 | num | |
| vertical_mp4_crc32 | num | |
| web_mp4_file_size | num | |
| horizontal_mp4_file_size | num | |
| vertical_mp4_file_size | num | |
| h265_conf | obj | |
```json
{"cmd":"GIFT_PANEL_PLAN","data":{"action":2,"gift_list":[{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31482,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31569,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31570,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31646,"show":false,"special_type":6}],"special_type_sort":null}}
{"cmd":"GIFT_PANEL_PLAN","data":{"gift_list":[{"gift_id":32328,"config":{"id":32328,"name":"蛋糕精灵","price":298000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"化身为蛋糕精灵——在这一刻，主播只被你守护 ᕦ(￣︶￣)ᕤ","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","gif":"https://i0.hdslb.com/bfs/open-live/5c761375cbb5ca3f4a974175ac57f5ee707e8f94.gif","webp":"https://i0.hdslb.com/bfs/open-live/b1ddb10efde313428a23a261a42f66f03fd07bb5.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":671,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32329,"config":{"id":32329,"name":"合影留念","price":48000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"告别千篇一律，留下只属于你和主播的专属回忆 (〃'▽'〃)","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","gif":"https://i0.hdslb.com/bfs/open-live/a26d41a96f8ec21a73dc5829ff9daba76e1c745f.gif","webp":"https://i0.hdslb.com/bfs/open-live/f9de197ab1b6cc2d57b13afe4df285188eb72da3.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":4166,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32330,"config":{"id":32330,"name":"派对礼花","price":5000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"空降主播派对趴，用礼花送上美好的祝愿 (╭￣3￣)╭♡","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","gif":"https://i0.hdslb.com/bfs/open-live/ee26062b1a9478b74a9370bb0407b1874adb4e01.gif","webp":"https://i0.hdslb.com/bfs/open-live/27368fa715d29378975ce51357e29ec9c0610f59.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":5000,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32843,"config":{"id":32843,"name":"3D星愿水晶球","price":100000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"3D星愿水晶球，虚拟星球特供","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":10,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":100,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":520,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","gif":"https://i0.hdslb.com/bfs/open-live/8554386857bbcfe5ae55166efabc2c43efdbf571.gif","webp":"https://i0.hdslb.com/bfs/open-live/f7aca02c29236696a01495920f96c801627ed3c0.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":2000,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":1,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32331,"config":{"id":32331,"name":"星辰大海","price":799000,"type":0,"coin_type":"gold","bag_gift":0,"effect":2,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"将主播传送到星辰大海浪漫时空中","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","gif":"https://i0.hdslb.com/bfs/open-live/05fdb6f71132183f270964eb1c953e4360341ad9.gif","webp":"https://i0.hdslb.com/bfs/open-live/5a7af91676d2312d9775c69ff85b5b9fbf00a4a0.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":250,"weight":1,"goods_id":168,"has_imaged_gift":1,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":794,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":[{"type":1,"web_svga":"","horizontal_svga":"","vertical_svga":"","web_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","web_mp4_json":"https://i0.hdslb.com/bfs/live/a728510a3bc7ba2de94b07553f5c1b729b1f7aa4.json","horizontal_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","vertical_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","id":794,"plan_platform":[1,2],"bind_gift_ids":[32331],"web_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","horizontal_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","vertical_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","web_mp4_crc32":564792465,"horizontal_mp4_crc32":564792465,"vertical_mp4_crc32":564792465,"web_mp4_file_size":1474735,"horizontal_mp4_file_size":1474735,"vertical_mp4_file_size":1474735,"h265_conf":{"horizontal_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/b27955fa707fcd0725394bc123310fe8295b3783.mp4","mp4_md5":"1570c241a73bd6903e3395e8cd392402","mp4_json":"","mp4_crc32":518022192,"mp4_file_size":630404},"vertical_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/b27955fa707fcd0725394bc123310fe8295b3783.mp4","mp4_md5":"1570c241a73bd6903e3395e8cd392402","mp4_json":"","mp4_crc32":518022192,"mp4_file_size":630404}}}],"float_sc_effect":null,"special_type":6,"show":true}],"special_type_sort":[12,14,13,13,13,13,13,13,5,6,7,8,9],"action":1}}
{"cmd":"GIFT_PANEL_PLAN","data":{"gift_list":[{"gift_id":32328,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32329,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32330,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32843,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32331,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false}],"special_type_sort":null,"action":2}}
```
---
### SEND_GIFT_V2
[TOP](#直播弹幕)  
文档更新：2024-01-20  
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "SEND_GIFT_V2" |
| data			| obj	| |
| msg_id		| str	| |
| p_is_ack		| bool	| |
| p_msg_type	| num	| |
| send_time		| num	| |
#### SEND_GIFT_V2__data
| key		| type	| value	|
|-|-|-|
| dmscore	| num	| |4 8 12 24 28 32 36 40 56 80
| pb		| base64(protobuf)	| |
```json
{"cmd":"SEND_GIFT_V2","data":{"dmscore":36,"pb":"...."},"msg_id":"xxx","p_is_ack":true,"p_msg_type":1,"send_time":xxx}
```
---
### ROOM_LOCK
[TOP](#直播弹幕)  
直播间封禁
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_LOCK" |
| expire	| str	| UTC+8 |
| roomid	| num	| |
```json
{"cmd":"ROOM_LOCK","expire":"2023-08-27 23:24:19","roomid":xxx}
```
---
### OFFICIAL_ROOM_EVENT
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OFFICIAL_ROOM_EVENT" |
| data		| obj	| |
#### OFFICIAL_ROOM_EVENT__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":2,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 开始表演","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":3}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":3,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":0,"scatter_time":3,"sub_title":"","desc":"","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":4,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 节目单表演结束","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":5,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":9,"scatter_time":3,"sub_title":"","desc":"s后 节目单表演结束","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":7,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":0,"scatter_time":3,"sub_title":"","desc":"","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":2}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":2,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 开始表演","official_base_info":{"uid":441666939,"title":" 冰火歌会2024远航季 正在直播","uname":"虚拟区官方频道","face":"https://i0.hdslb.com/bfs/face/a26b52bc7837ce6867802575d300ed70d5e6f2d5.jpg","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":3}}
```
---
### BENEFIT_CARD_CLEAN
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "BENEFIT_CARD_CLEAN" |
| data		| obj	| |
#### BENEFIT_CARD_CLEAN__data
| key		| type	| value	|
|-|-|-|
| id		| num	| |
```json
{"cmd":"BENEFIT_CARD_CLEAN","data":{"id":xxx}}
```
---
### DANMU_MSG371111
[TOP](#直播弹幕)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "DANMU_MSG:3:7:1:1:1:1" |
| info		| array	| |
| dm_v2		| str	| "" |
#### DANMU_MSG371111__info
| array	| type	| value	| 备注	|
|-|-|-|
| 0		| array		| 假弹幕属性 |
| 1	| str(array)	| 假弹幕内容 |
| 2		| array		| 假用户主站信息 |
| 3		| null		| ~~粉丝勋章~~ |
| 4		| array		| ~~用户直播区信息~~ |
| 5		| array		| ~~头衔~~ |
| 6		| num		| 0 |
| 7		| num		| 0 |
| 8		| null		| null |
| 9		| obj		| `validation` |
| 10	| num		| 0 |
| 11	| num		| 0 |
| 12	| null		| null |
| 13	| null		| null |
| 14	| num		| 0 |
| 15	| num		| 0 |
| 16	| array		| `Wealth` |
| 0[0]	| num		| ？0 |
| 0[1]	| num		| 7 弹幕位置 |
| 0[2]	| num		| 100 弹幕字体大小 |
| 0[3]	| num		| 16777215 弹幕颜色 |
| 0[4]	| num		| TimeStamp(毫秒) |
| 0[5]	| num		| 0 |
| 0[6]	| num		| 0 |
| 0[7]	| str		| "f4dbdf21" `midHash` | crc32("0")
| 0[8]	| num		| 0 |
| 0[9]	| num		| |
| 0[10]	| num		| |
| 0[11]	| str		| |
| 0[12]	| num		| |
| 0[13]	| obj/str	| |
| 0[14]	| obj/str	| |
| 0[15]	| obj 		| |
| 0[16]	| obj 		| |
| 0[17]	| num 		| |
| 1[0]	| float		| |
| 1[1]	| float		| |
| 1[2]	| str		| |
| 1[3]	| float		| |
| 1[4]	| str		| |
| 1[5]	| float		| |
| 1[6]	| float		| |
| 1[7]	| float		| |
| 1[8]	| float		| |
| 1[9]	| num		| |
| 1[10]	| num		| |
| 1[11]	| bool		| |
| 1[12]	| str		| |
| 1[13]	| num		| |
| 2[0]	| num		| 0 假用户uid |
| 2[1]	| str		| "***" 假用户昵称 |
| 2[2]	| num		| 1 房管 |
| 2[3]	| num		| 0 |
| 2[4]	| num		| 0 |
| 2[5]	| num		| 10000 |
| 2[6]	| num		| 1 |
| 2[7]	| str		| "" |
```json
1701778709134270{"cmd":"DANMU_MSG:3:7:1:1:1:1","info":[[0,7,100,16777215,1701778709186,0,0,"f4dbdf21",0,null,null,null,0,"{}","{}",{"mode":0,"show_player_type":0,"extra":"{\"mode\":0,\"send_from_me\":false,\"color\":16777215,\"dm_type\":0,\"font_size\":100,\"player_mode\":7,\"content\":\"[1.0,0.0,\\\"0.8-0.5\\\",10.0,\\\"哈哈哈哈\\\",0.0,0.0,0.0,0.0,10000,0,true,\\\"黑体\\\",1]\"}"},null,null],"[1.0,0.0,\"0.8-0.5\",10.0,\"哈哈哈哈\",0.0,0.0,0.0,0.0,10000,0,true,\"黑体\",1]",[0,"***",1,0,0,10000,1,""],null,[],[],0,0,null,{"ts":1701778709,"ct":"82145D85"},0,0,null,null,0,0,[0]],"dm_v2":""}
```
---
### LIVE_MULTI_VIEW_NEW_INFO
[TOP](#直播弹幕)  
文档更新：2024-01-19
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_MULTI_VIEW_NEW_INFO" |
| data		| obj	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data
| key 12			| type	| value	|
|-|-|-|
| title				| str	| |
| room_id			| num	| |
| copy_writing		| str	| |
| bg_image			| str	| |
| sub_slt_color		| str	| |
| sub_bg_color		| str	| |
| sub_text_color	| str	| |
| view_type			| num	| |
| room_list			| [+]obj	| |
| relation_view		| [+]obj	| |
| view_pattern		| num	| |
| gather_room_list	| []	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__room_list
| key 5			| type	| value	|
|-|-|-|
| order_id		| num	| |
| room_id		| num	| |
| room_name		| str	| |
| live_status	| num	| |
| jump_url		| str	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__relation_view
| key 20			| type	| value	|
|-|-|-|
| order_id			| num	| |
| view_type			| num	| |
| view_id			| num	| |
| view_name			| str	| |
| title				| str	| |
| cover				| str	| |
| jump_url			| str	| |
| switch			| bool	| |
| num				| num	| [WATCHED_CHANGE](#WATCHED_CHANGE) |
| watch_icon		| str	| |
| live_status		| num	| |
| text_small		| str	| [WATCHED_CHANGE](#WATCHED_CHANGE) |
| use_view_vt		| bool	| |
| anchor_face		| str	| |
| match_live_room	| bool	| |
| match_info		| null/	| |
| duration			| num	| |
| up_name			| str	| |
| pub_date			| str	| |
| gather_id			| num	| |

```json
{"cmd":"LIVE_MULTI_VIEW_NEW_INFO","data":{
	"title":"2023游戏区年度榜单公布",
	"room_id":5440,
	"copy_writing":"更 多视角",
	"bg_image":"https://i0.hdslb.com/bfs/live/edaa9477a1d8325dd0c36c419b6fd5f9646b2419.png",
	"sub_slt_color":"#FFFFFF",
	"sub_bg_color":"#333333",
	"sub_text_color":"#FFFFFF",
	"view_type":0,
	"room_list":[
		{"order_id":1,"room_id":5440,"room_name":"哔哩哔哩直播","live_status":1,"jump_url":"https://live.bilibili.com/5440?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":2,"room_id":47867,"room_name":"C酱です","live_status":1,"jump_url":"https://live.bilibili.com/47867?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":3,"room_id":1017,"room_name":"逍遥散人","live_status":1,"jump_url":"https://live.bilibili.com/1017?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":4,"room_id":1029,"room_name":"黑桐谷歌","live_status":1,"jump_url":"https://live.bilibili.com/1029?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":5,"room_id":5495774,"room_name":"智能路障","live_status":1,"jump_url":"https://live.bilibili.com/5495774?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":6,"room_id":544864,"room_name":"舍长驾到","live_status":1,"jump_url":"https://live.bilibili.com/544864?broadcast_type=0&is_room_feed=1&live_from=28022"},
		{"order_id":7,"room_id":14073160,"room_name":"蛋黄咩咩子","live_status":1,"jump_url":"https://live.bilibili.com/14073160?broadcast_type=0&is_room_feed=1&live_from=28022"}
	],
	"relation_view":[
		{"order_id":1,"view_type":0,"view_id":5440,"view_name":"哔哩哔哩直播","title":"2023游戏区年度榜单公布直播","cover":"https://s1.hdslb.com/bfs/static/blive/live-assets/common/images/no-cover.png","jump_url":"https://live.bilibili.com/5440?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":10300,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"1.0万","use_view_vt":false,"anchor_face":"https://i0.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":2,"view_type":0,"view_id":47867,"view_name":"C酱です","title":"一起看高能电玩节吧","cover":"http://i0.hdslb.com/bfs/live/new_room_cover/xxx.jpg","jump_url":"https://live.bilibili.com/47867?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":115635,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"11.5万","use_view_vt":false,"anchor_face":"https://i1.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":3,"view_type":0,"view_id":1017,"view_name":"逍遥散人","title":"一起看游戏年度盘点","cover":"http://i0.hdslb.com/bfs/live/xxx.jpg","jump_url":"https://live.bilibili.com/1017?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":2011,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"2011","use_view_vt":false,"anchor_face":"https://i1.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":4,"view_type":0,"view_id":1029,"view_name":"黑桐谷歌","title":"看年度榜单","cover":"http://i0.hdslb.com/bfs/live/new_room_cover/xxx.jpg","jump_url":"https://live.bilibili.com/1029?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":1801,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"1801","use_view_vt":false,"anchor_face":"https://i0.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":5,"view_type":0,"view_id":5495774,"view_name":"智能路障","title":"猛兽派 对高手回归，看B站游戏年榜","cover":"http://i0.hdslb.com/bfs/live/new_room_cover/xxx.jpg","jump_url":"https://live.bilibili.com/5495774?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":4988,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"4988","use_view_vt":false,"anchor_face":"https://i0.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":6,"view_type":0,"view_id":544864,"view_name":"舍长驾到","title":"舍长的直播（FF16DLC）","cover":"http://i0.hdslb.com/bfs/live/user_cover/xxx.jpg","jump_url":"https://live.bilibili.com/544864?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":3816,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"3816","use_view_vt":false,"anchor_face":"https://i1.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0},
		{"order_id":7,"view_type":0,"view_id":14073160,"view_name":"蛋黄咩咩子","title":"B站年度游戏榜单大赏","cover":"http://i0.hdslb.com/bfs/live/new_room_cover/xxx.jpg","jump_url":"https://live.bilibili.com/14073160?broadcast_type=0&is_room_feed=1&live_from=28022","switch":true,"num":384,"watch_icon":"https://i0.hdslb.com/bfs/live/a725a9e61242ef44d764ac911691a7ce07f36c1d.png","live_status":1,"text_small":"384","use_view_vt":false,"anchor_face":"https://i1.hdslb.com/bfs/face/xxx.jpg","match_live_room":false,"match_info":null,"duration":0,"up_name":"","pub_date":"","gather_id":0}
	],
	"view_pattern":0,
	"gather_room_list":[]}}
```
---
### INTERACTIVE_USER
[TOP](#直播弹幕)  
文档更新：2024-01-20  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACTIVE_USER" |
| data		| obj	| |
#### INTERACTIVE_USER__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"INTERACTIVE_USER","data":{"type":1,"value":{"delay":5,"dm_msg":"主播已开启预言玩法，点击直播间底部互动按钮参与","prophet_status":1,"send_msg":1}}}
{"cmd":"INTERACTIVE_USER","data":{"type":1,"value":{"delay":5,"dm_msg":"主播已开启预言玩法，点击直播间底部互动按钮参与","prophet_status":2,"send_msg":0}}}
{"cmd":"INTERACTIVE_USER","data":{"type":1,"value":{"delay":5,"dm_msg":"主播已开启预言玩法，点击直播间底部互动按钮参与","prophet_status":3,"send_msg":0}}}
```
---
### PANEL_INTERACTIVE_NOTIFY_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-01-20  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PANEL_INTERACTIVE_NOTIFY_CHANGE" |
| data		| obj	| |
#### PANEL_INTERACTIVE_NOTIFY_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PANEL_INTERACTIVE_NOTIFY_CHANGE","data":{"biz_id":4,"end_time":0,"icon":"https://i0.hdslb.com/bfs/live/164a37487431ce065981d76afe6c2fb2083facee.png","last_time":0,"level":1,"text":"预言状态变更"}}
{"cmd":"PANEL_INTERACTIVE_NOTIFY_CHANGE","data":{"biz_id":4,"end_time":180,"icon":"https://i0.hdslb.com/bfs/live/164a37487431ce065981d76afe6c2fb2083facee.png","last_time":5,"level":1,"text":"主播开启预言"}}
```
---
### LIVE_INTERACT_GAME_STATE_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_INTERACT_GAME_STATE_CHANGE" |
| data		| obj	| |
#### LIVE_INTERACT_GAME_STATE_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_INTERACT_GAME_STATE_CHANGE","data":{"game_name":"互动玩法","game_id":"4983b803-df90-4041-9da5-9a99241099d8","action":1},"recv_time":"2024-02-01 20:54:40"}
{"cmd":"LIVE_INTERACT_GAME_STATE_CHANGE","data":{"game_name":"互动玩法","game_id":"ae45e4d4-052a-4b71-84e0-19b3de5a5c3e","action":1},"recv_time":"2024-02-02 13:57:46"}
{"cmd":"LIVE_INTERACT_GAME_STATE_CHANGE","data":{"game_name":"互动玩法","game_id":"9e818862-f1c1-4df4-a8e2-07483fe2cbd1","action":1},"recv_time":"2024-02-02 18:22:51"}
{"cmd":"LIVE_INTERACT_GAME_STATE_CHANGE","data":{"game_name":"互动玩法","game_id":"a876f56e-05fd-4c83-bd9b-c52336789901","action":1},"recv_time":"2024-03-03 15:03:17"}
```
---
### POPULARITY_RED_POCKET_V2_START
[TOP](#直播弹幕)  
红包抽奖
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULARITY_RED_POCKET_V2_START" |
| data		| obj	| |
#### POPULARITY_RED_POCKET_V2_START__data
| key 19				| type		| value	|
|-|-|-|
| lot_id				| num		| 抽奖id |
| sender_uid			| num		| uid |
| sender_name			| str		| 昵称 |
| sender_face			| str		| 头像URL |
| join_requirement		| num		| 1 |
| danmu					| str		| "老板大气！点点红包抽礼物" |
| current_time			| num		| TimeStamp(秒) 当前时间 |
| start_time			| num		| TimeStamp(秒) 开始时间 |
| end_time				| num		| TimeStamp(秒) 结束时间 |
| last_time				| num		| 持续时间(秒) |
| remove_time			| num		| TimeStamp(秒) 图标移除时间 |
| replace_time			| num		| TimeStamp(秒) 下一个红包显示时间 |
| lot_status			| num		| [lot_status](#others) 1 |
| h5_url				| str		| f"https://live.XXXX.com/p/html/live-app-red-envelope/popularity.html?is_live_half_webview=1&hybrid_half_ui=1,5,100p,100p,000000,0,50,0,0,1;2,5,100p,100p,000000,0,50,0,0,1;3,5,100p,100p,000000,0,50,0,0,1;4,5,100p,100p,000000,0,50,0,0,1;5,5,100p,100p,000000,0,50,0,0,1;6,5,100p,100p,000000,0,50,0,0,1;7,5,100p,100p,000000,0,50,0,0,1;8,5,100p,100p,000000,0,50,0,0,1&hybrid_rotate_d=1&hybrid_biz=popularityRedPacket&lotteryId={lot_id}" |
| user_status			| num		| 2 |
| awards				| [3]obj	| |
| lot_config_id			| num		| 红包预设 |
| total_price			| num		| 礼物总价值×0.8 |
| wait_num				| num		| 队列数量 |
| wait_num_v2			| num		| 队列数量 |
| is_mystery			| bool		| |
| rp_type				| num		| |
| sender_uinfo			| obj		| [unifo](#pubilc_uinfo) |
| icon_url				| str		| |
| animation_icon_url	| str		| |
#### POPULARITY_RED_POCKET_V2_START__data__awards
| key		| type	| value	|
|-|-|-|
| gift_id	| num	| 礼物id |
| gift_name	| num	| 礼物名称 |
| gift_pic	| num	| 礼物图像URL(140×140) |
| num		| num	| 数量 |
----
### GUARD_LEADER_NOTICE
[TOP](#直播弹幕)  
文档更新：2024-04-08  
舰队指挥官  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GUARD_LEADER_NOTICE" |
| data		| obj	| |
#### GUARD_LEADER_NOTICE__data
| key		| type	| value	|
|-|-|-|
| jump_url							| str	| |
| input_background_url				| str	| |
| rank_top_background_url2			| str	| |
| face								| str	| |
| anchor_background_url				| str	| |
| rank_top_icon1					| str	| |
| anchor_effect_id					| num	| |
| show								| num	| |
| uid								| num	| |
| rank_top_background_light_url2	| str	| |
| name								| str	| |
| rank_top_icon2					| str	| |
| rank_top_background_url1			| str	| |
| effect_id							| num	| |
| svga_Block						| num	| |
| background_url					| str	| |
```json
{
	"cmd":"GUARD_LEADER_NOTICE",
	"data":{
		"jump_url":"https://live.bilibili.com/p/html/live-app-guard-pilot/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,73p,0,0,30,0,12,0;2,2,375,100p,0,0,30,0,0,0;3,3,100p,73p,0,0,30,0,12,0;4,2,375,100p,0,0,30,0,0,0;5,3,100p,73p,0,0,30,0,12,0;6,3,100p,73p,0,0,30,0,12,0;7,3,100p,73p,0,0,30,0,12,0;8,2,320,480,0,0,30,0,0,0&anchorId={mid}&roomId={room_id}",
		"input_background_url":"https://i0.hdslb.com/bfs/live/ffba0916dc46c0242ad83644b5ccf1870b54a12a.png",
		"rank_top_background_url2":"https://i0.hdslb.com/bfs/live/71397554da8a7bd2ac14905c69891df54ad62ede.png",
		"face":"TOP1_Face",
		"anchor_background_url":"https://i0.hdslb.com/bfs/live/3b8aa82202415b1ed8772ba3aa78628a31d44d51.png",
		"rank_top_icon1":"https://i0.hdslb.com/bfs/live/64b22e65979b32f7e4e8bec1edb38c697fb320fc.png",
		"anchor_effect_id":0,
		"show":1,
		"uid":top1_uid,
		"rank_top_background_light_url2":"https://i0.hdslb.com/bfs/live/c0fbd28b6ddf170b8db2e2c7163eb9d66f66fd8b.png",
		"name":"xxx",
		"rank_top_icon2":"https://i0.hdslb.com/bfs/live/7b9d773c6018ffac9f0eadd3c92f0090e09055f2.png",
		"rank_top_background_url1":"https://i0.hdslb.com/bfs/live/b2832de9cca6a0b3b4872c8d96c05ae713bc51d2.png",
		"effect_id":0,
		"svga_Block":0,
		"background_url":"https://i0.hdslb.com/bfs/live/13306509ffe9d43d5571ac9af84463e4958ab3c4.png"
	}
}
```
---
### WIDGET_WISH_LIST
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WIDGET_WISH_LIST" |
| data		| obj	| |
#### WIDGET_WISH_LIST__data
| key		| type	| value	|
|-|-|-|
| wish | list | |
| wish_status | num | |
| sid | num | |
| wish_status_info | list | |
| wish_name | str | |
| jump_schema | str | |
| type | num | |
| ts | num | |
#### WIDGET_WISH_LIST__data__wish
| key			| type	| value	|
|-|-|-|
| type			| num	| |
| gift_id		| num	| |
| gift_name		| str	| |
| gift_img		| str	| |
| gift_price	| num	| |
| target_num	| num	| |
| current_num	| num	| |
| wish_name		| str	| |
| check_status	| num	| |
| check_reason	| str	| |
| wish_sub_id	| str	| |
| id			| str	| |
#### WIDGET_WISH_LIST__data__wish_status_info
| key		| type	| value	|
|-|-|-|
| wish_status_msg	| str | |
| wish_status_img	| str | |
| wish_status		| num | |
```json
{
	"cmd": "WIDGET_WISH_LIST",
	"data": {
		"wish": [
			{"type": 3,"gift_id": 10002,"gift_name": "提督","gift_img": "https://i0.hdslb.com/bfs/live/ea985665bfdc4b0ce894b8fcf7c29fecc3136a08.png","gift_price": 1998000,"target_num":xxx,"current_num": 0,"wish_name": "","check_status": 0,"check_reason": "","wish_sub_id": "","id": ""},
			{"type": 3,"gift_id": 10003,"gift_name": "舰长","gift_img": "https://i0.hdslb.com/bfs/live/f1be2a2d5b227ce72641de1ad64bcc7f9e4111c3.png","gift_price": 198000,"target_num":xxx,"current_num": 0,"wish_name": "","check_status": 0,"check_reason": "","wish_sub_id": "","id": ""}
		],
		"wish_status": 1,
		"sid": 4151,
		"wish_status_info": [
			{"wish_status_msg":"去设置","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":0},
			{"wish_status_msg":"心愿达成","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":2},
			{"wish_status_msg":"收集失败","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":3}
		],
		"wish_name": "心愿单",
		"jump_schema": "",
		"type": 1,
		"ts": xxx
	}
}
```
---
### UNIVERSAL_EVENT_GIFT
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "UNIVERSAL_EVENT_GIFT" |
| data		| obj	| |
#### UNIVERSAL_EVENT_GIFT__data
| key			| type	| value	|
|-|-|-|
| anchor_uid	| num | |
| info			| obj | |
| room_id		| num | |
```json
{
	"cmd": "UNIVERSAL_EVENT_GIFT",
	"data": {
		"anchor_uid": xxx,
		"info": {
			"biz_session_id": "xxx",
			"business_label": "universal_multi_conn",
			"interact_channel_id": "xxx",
			"interact_connect_type": 0,
			"interact_max_users": 9,
			"interact_mode": {
				"apply_timeout": 20,
				"interact_mode_type": 0,
				"invite_timeout": 20,
				"join_types": [1,2],
				"position_mode": 0
			},
			"interact_template": {
				"is_variable_layout": true,
				"layout_data": {
					"best_area_show_pos": 0,
					"cells": [
						{"default_open": 0,"height": 8,"mobile_avatar_size": 0,"mobile_font_size": 0,"pc_web_avatar_size": 0,"pc_web_font_size": 0,"position": 0,"width": 0,"x": 0,"y": 0,"z_index": 0},
						{"default_open": 0,"height": 0,"mobile_avatar_size": 0,"mobile_font_size": 0,"pc_web_avatar_size": 0,"pc_web_font_size": 0,"position": 1,"width": 0,"x": 5,"y": 0,"z_index": 0},
						{"default_open": 0,"height": 0,"mobile_avatar_size": 0,"mobile_font_size": 0,"pc_web_avatar_size": 0,"pc_web_font_size": 0,"position": 2,"width": 0,"x": 5,"y": 4,"z_index": 0}
					],
					"default_cell": {"default_open": 1,"height": 4,"mobile_avatar_size": 64,"mobile_font_size": 12,"pc_web_avatar_size": 112,"pc_web_font_size": 14,"position": 0,"width": 5,"x": 0,"y": 0,"z_index": 0},
					"height": 8,
					"rtc_resolution": {"code_rate_init": 1600,"code_rate_max": 2000,"code_rate_min": 800,"horizontal_height": 800,"horizontal_width": 1000,"vertical_height": 1152,"vertical_width": 720},
					"width": 10
				},
				"layout_id": "left1_right2",
				"layout_list": null,
				"show_interact_ui": true,
				"template_id": "multi_conn_grid"
			},
			"invoking_time": 1,
			"members": [
				{"face": "xxx","gender": x,"join_time": xxx,"link_id": "xxx","position": 0,"room_id": xxx,"uid": xxx,"uname": "XXX"},
				{"face": "xxx","gender": x,"join_time": xxx,"link_id": "xxx","position": 2,"room_id": xxx,"uid": xxx,"uname": "XXX"},
				{"face": "xxx","gender": x,"join_time": xxx,"link_id": "xxx","position": 1,"room_id": xxx,"uid": xxx,"uname": "XXX"}
			],
			"members_version": xxx,
			"multi_conn_info": {
				"room_owner": xxx,
				"scores": [
					{"price": 100,"price_text": "1","uid": xxx},
					{"price": 100,"price_text": "1","uid": xxx},
					{"price": 100,"price_text": "1","uid": xxx}
				]
			},
			"room_owner": xxx,
			"room_start_at": "",
			"room_start_at_ts": 0,
			"room_status": 1,
			"session_start_at": "",
			"session_start_at_ts": 0,
			"session_status": 1,
			"system_time_unix": xxx,
			"trace_id": "",
			"version": XXX
		},
		"room_id": XXX
	},
	"msg_id": "xxx:xxxx:1000",
	"p_is_ack": true,
	"p_msg_type": 1,
	"send_time": XXX
}
```
---
### LITTLE_TIPS
[TOP](#直播弹幕)  
文档更新：2024-04-24  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "LITTLE_TIPS" |
| data	| obj	| |
#### LITTLE_TIPS__data
| key	| type	| value	|
|-|-|-|
| msg	| str	| |
```json
{"cmd":"LITTLE_TIPS","data":{"msg":"你的粉丝勋章【XXXXXX】已达今日亲密度上限"}}
```
---
### LIKE_GUIDE_USER
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_GUIDE_USER" |
| data		| obj	| |
#### LIKE_GUIDE_USER__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIKE_GUIDE_USER","data":{"show_area":0,"like_text":"主播@你：点点赞支持一下我吧","uid":xxxx,"identities":[1],"msg_type":6,"dmscore":20}}
```
---
### PK_BATTLE_MULTIPLE_AWARD
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PK_BATTLE_MULTIPLE_AWARD" |
| data		| obj	| |
#### PK_BATTLE_MULTIPLE_AWARD__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PK_BATTLE_MULTIPLE_AWARD","data":{"pkid":X,"pk_status":xxx,"award_room":A,"award_no":0,"award_name":"0","award_value":0,"multiple_time":0,"start_time":0,"end_time":0,"status":7}}
{"cmd":"PK_BATTLE_MULTIPLE_AWARD","data":{"pkid":X,"pk_status":xxx,"award_room":B,"award_no":0,"award_name":"0","award_value":0,"multiple_time":0,"start_time":0,"end_time":0,"status":7}}
```
---
### REENTER_LIVE_ROOM
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "REENTER_LIVE_ROOM" |
| data		| obj	| |
| roomid	| num	| |
#### REENTER_LIVE_ROOM__data
| key						| type	| value	|
|-|-|-|
| room_id					| num	| |
| request_random_sec_range	| num	| |
| reason					| num	| |
```json
{"cmd":"REENTER_LIVE_ROOM","data":{"room_id":xxx,"request_random_sec_range":10,"reason":1},"roomid":xxx}
```
---
### DANMU_ACTIVITY_CONFIG
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "DANMU_ACTIVITY_CONFIG" |
| data		| obj	| |
#### DANMU_ACTIVITY_CONFIG__data
| key				| type	| value	|
|-|-|-|
| dm_mode			| num	| |
| dm_setting_switch	| num	| |
| etime				| num	| |
| extra				| str	| |
| id				| num	| |
| material_conf		| obj	| |
| mock_options		| null	| |
| platform			| num	| |
| screen_type		| num	| |
| status			| num	| |
| stime				| num	| |
```json
{
	"cmd": "DANMU_ACTIVITY_CONFIG",
	"data": {
		"dm_mode": 3001,
		"dm_setting_switch": 1,
		"etime": -28800,
		"extra": "",
		"id":xxx,
		"material_conf": {
			"activity_test_material": "http://i0.hdslb.com/bfs/live/a4d2a09ae85ded1dc17571d73ef4a8ada9c40d91.zip",
			"activity_type": 1,
			"main_state_dm_color": "#D0FEFF",
			"material_mode": [
				{"app_key": "iphone","mobi_material": {"mobi_module": "","mobi_module_file": "mobi_meteor.zip","mobi_module_file_name": "mobi_meteor","mobi_module_version": 1,"mobi_pool": "live"}},
				{"app_key": "ipad2","mobi_material": {"mobi_module": "","mobi_module_file": "mobi_meteor.zip","mobi_module_file_name": "mobi_meteor","mobi_module_version": 1,"mobi_pool": "live"}},
				{"app_key": "android","mobi_material": {"mobi_module": "","mobi_module_file": "mobi_meteor.zip","mobi_module_file_name": "mobi_meteor","mobi_module_version": 1,"mobi_pool": "live"}},
				{"app_key": "android64","mobi_material": {"mobi_module": "","mobi_module_file": "mobi_meteor.zip","mobi_module_file_name": "mobi_meteor","mobi_module_version": 1,"mobi_pool": "live"}}
			],
			"objective_state_dm_color": "#D0FEFF",
			"web_material": "{\"main_state_bg\":\"http://i0.hdslb.com/bfs/live/df12a08ce2f43bc6f74a7def65f2332781d13af2.png\",\"objective_state_bg\":\"http://i0.hdslb.com/bfs/live/b89dba7a33a86aad2f0344542e8216cbd1d025a6.png\"}"
		},
		"mock_options": null,
		"platform": [3,2,1,4],
		"screen_type": 3,
		"status": 1,
		"stime": -28800
	},
	"msg_id": "XXX:1000:1000",
	"p_is_ack": true,
	"p_msg_type": 1,
	"send_time":XXX
}
```
---
### POPULAR_RANK_GUIDE_CARD
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULAR_RANK_GUIDE_CARD" |
| data		| obj	| |
#### POPULAR_RANK_GUIDE_CARD__data
| key			| type	| value	|
|-|-|-|
| ruid			| num	| |
| title			| str	| |
| sub_text		| str	| |
| icon_img		| str	| |
| gift_id		| num	| |
| countdown		| num	| |
| popup_title	| str	| |
```json
{"cmd":"POPULAR_RANK_GUIDE_CARD","data":{"ruid":xxx,"title":"目前人气榜NO.1", "sub_text":"帮我投喂人气票冲榜吧~","icon_img":"https://i2.hdslb.com/bfs/face/a6419a5f230c500962c7954c907be74a7cbd61b5.jpg","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"}}
{"cmd":"POPULAR_RANK_GUIDE_CARD","data":{"ruid":xxx,"title":"目前人气榜NO.2", "sub_text":"帮我投喂人气票冲榜吧~","icon_img":"https://i2.hdslb.com/bfs/face/a6419a5f230c500962c7954c907be74a7cbd61b5.jpg","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"}}
{"cmd":"POPULAR_RANK_GUIDE_CARD","data":{"ruid":xxx,"title":"目前人气榜NO.3", "sub_text":"帮我投喂人气票冲榜吧~","icon_img":"https://i2.hdslb.com/bfs/face/a6419a5f230c500962c7954c907be74a7cbd61b5.jpg","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"}}
{"cmd":"POPULAR_RANK_GUIDE_CARD","data":{"ruid":xxx,"title":"目前人气榜NO.25","sub_text":"帮我投喂人气票冲榜吧~","icon_img":"https://i2.hdslb.com/bfs/face/a6419a5f230c500962c7954c907be74a7cbd61b5.jpg","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"}}
```
---
### XXXXXXXXXXX
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "XXXXXXXXXXX" |
| data		| obj	| |
#### XXXXXXXXXXX__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"key":"value"}
```
---

### others
[TOP](#直播弹幕)  
| key				| type	| value	| where	|
|-|-|-|-|
| guard_level		| num	| 大航海等级 <br> 0:无 <br> 1:总督GOVERNOR <br> 2:提督PREFECT <br> 3:舰长CAPTAIN |
| privilege_type	| num	| ！待确定 2:提督 3:舰长 |
| lot_status		| num	| 抽奖状态 0:开始 1:正在抽奖 2:开奖 |
| identities		| []num	| 身份 1:"Normal" 2:"管理员" 3:"粉丝" 4:"Vip" 5:"SVip" 6:"舰长" 7:"提督" 8:"总督" |[INTERACT_WORD](#INTERACT_WORD)[LIKE_INFO_V3_CLICK](#LIKE_INFO_V3_CLICK)[ENTRY_EFFECT](#ENTRY_EFFECT)

```json
"face_frame":{
	"舰长": "https://i0.hdslb.com/bfs/live/80f732943cc3367029df65e267960d56736a82ee.png",
	"提督": "https://i0.hdslb.com/bfs/live/09937c3beb0608e267a50ac3c7125c3f2d709098.png",
}
```
1
```
face:http(s)?://[is][0-3].hdslb.com/bfs/((face|baselabs)/[0-9a-f]{40}.(jpg|png|gif|webp)|face/member/noface\.jpg)
for i in range(1,len(a)):print(str(a[i]-a[i-1])[0:4])
(\d{10}\.\d{1,3}|\d{13,17})?\{"cmd":[ ]{0,1}"XXXXXXXXXX",.{1,}\r?\n
(\d{13,})?\{("business_id":".{0,11}",)?"cmd":"XXXXXXXXXX",.{1,}\r?\n
(\d{13,})?\{"cmd":"(GUARD_ACHIEVEMENT_ROOM|VOICE_CHAT_UPDATE|ROOM_SKIN_MSG|FULL_SCREEN_SPECIAL_EFFECT|TRADING_SCORE|RING_STATUS_CHANGE|PK_BATTLE_ENTRANCE|POPULARITY_RED_POCKET_NEW|POPULARITY_RED_POCKET_START|POPULARITY_RED_POCKET_V2_WINNER_LIST|POPULARITY_RED_POCKET_WINNER_LIST|POPULARITY_RED_POCKET_START|POPULARITY_RED_POCKET_V2_START|POPULARITY_RED_POCKET_V2_NEW|RING_STATUS_CHANGE_V2|GUARD_BUY|SYS_MSG|ANCHOR_LOT_CHECKSTATUS|SEND_GIFT|ONLINE_RANK_TOP3|INTERACT_WORD|POPULAR_RANK_CHANGED|ROOM_REAL_TIME_MESSAGE_UPDATE|AREA_RANK_CHANGED|COMMON_NOTICE_DANMAKU|ENTRY_EFFECT|LIKE_INFO_V3_UPDATE|LIKE_INFO_V3_CLICK|COMBO_SEND|DM_INTERACTION|GUARD_HONOR_THOUSAND|GIFT_STAR_PROCESS|WIDGET_GIFT_STAR_PROCESS|HOT_ROOM_NOTIFY|NOTICE_MSG|DANMU_AGGREGATION|SHOPPING_CART_SHOW|RECOMMEND_CARD|GOTO_BUY_FLOW)",.{1,}\r?\n
(\d{13,})?\{"cmd":"(DM_INTERACTION|LIKE_INFO_V3_CLICK|LIKE_INFO_V3_UPDATE|ONLINE_RANK_COUNT|ONLINE_RANK_V2|STOP_LIVE_ROOM_LIST|WATCHED_CHANGE|WIDGET_BANNER)",.{1,}\r?\n
,\n?\x09{0,}"__typename": ?"(EmbeddedEmote|VideoCommentMessageFragment|Badge|VideoCommentMessage|VideoComment|VideoCommentEdge|VideoCommentConnection|Game|User|Video|PageInfo)"
```

### 粉丝勋章medal_info
| key					| type		| value	| 备注 |
|-|-|-|-|
| anchor_roomid			| num		| 主播 短直播间ID | 
| anchor_uname			| str		| 主播昵称 | 
| guard_level			| num		| [大航海等级](#others) |
| icon_id				| num		| 0！ |
| is_lighted			| num		| 0: <br> 1: 七天内在直播间有互动 |
| medal_color			| num/str	| int(RGB24) / #RRGGBB |
| medal_color_border	| num		| int(RGB24) |
| medal_color_end		| num		| int(RGB24) |
| medal_color_start		| num		| int(RGB24) |
| medal_level			| num		| 粉丝勋章等级 |
| score					| num		| 亲密值 |
| medal_name			| str		| 粉丝勋章称号 |
| special				| str		| ""！ |
| target_id				| !num		| 主播uid |

### PUBILC_uinfo
文档更新：2024-01-28  
| key						| type		| value	|
|-|-|-|-|
| base						| obj		| |
| uid						| str		| uid |
| medal						| null/obj	| |
| wealth					| null/obj	| |
| title						| null/obj	| 活动头衔 |
| guard						| null/obj	| |
| uhead_frame				| null/obj	| |
| guard_leader				| null/obj	| 舰队指挥官 |
#### PUBLIC_uinfo__wealth
| key						| type		| value	|
|-|-|-|-|
| level						| num		| |
| dm_icon_key				| str		| |
#### PUBLIC_uinfo__title
| key						| type		| value	|
|-|-|-|-|
| old_title_css_id			| str		| |
| title_css_id				| str		| |
#### PUBLIC_uinfo__guard
| key						| type		| value	|
|-|-|-|-|
| expired_str				| str		| 过期时间 |
| level						| num		| [大航海等级](#others) |
#### PUBLIC_uinfo__guard_leader
| key						| type		| value	|
|-|-|-|-|
| is_guard_leader			| bool		| |
#### PUBLIC_uinfo__medal
| key						| type		| value	|
|-|-|-|-|
| name						| str		| 粉丝勋章称号 |
| level						| num		| 粉丝勋章等级 |
| color_start				| num		| int(RGB24) |
| color_end					| num		| int(RGB24) |
| color_border				| num		| int(RGB24) |
| color						| num/str	| int(RGB24) |
| id						| num		| |
| typ						| num		| |
| is_light					| num		| 0: <br> 1: 七天内在直播间有互动 |
| ruid						| !num		| 主播uid |
| guard_level				| num		| [大航海等级](#others) |
| score						| num		| 亲密值 |
| guard_icon				| str		| 大航海等级图标 |
| honor_icon				| str		| |
#### PUBLIC_uinfo__base
| key						| type		| value	|
|-|-|-|-|
| face						| obj		| 头像(URL) |
| is_mystery				| bool		| |
| name						| str		| 昵称 |
| name_color				| num		| |
| name_color_str			| str		| #RRGGBB |
| risk_ctrl_info			| null/obj	| |
| origin_info				| obj		| |
| official_info				| obj		| 主站：认证信息 |
##### PUBLIC_uinfo__base__origin_info
| key						| type		| value	|
|-|-|-|-|
| face						| obj		| 头像(URL) |
| name						| str		| 昵称 |
##### PUBLIC_uinfo__base__risk_ctrl_info
| key						| type		| value	|
|-|-|-|-|
| face						| obj		| 头像(URL) |
| name						| str		| 昵称 |
##### PUBLIC_uinfo__base__official_info
| key						| type		| value	|
|-|-|-|-|
| role						| num		| 0:无 7:个人认证 3:机构认证 |
| title						| str		| 认证说明 |
| desc						| str		|  |
| type						| num		| -1:无 0:个人认证 1:机构认证 |
#### PUBILC_uinfo_json
```json
"uinfo":{
	"uid":xxx,
	"base":{
		"name":"XXX",
		"face":"https://i1.hdslb.com/bfs/face/....jpg",
		"name_color":0,
		"is_mystery":false,
		"origin_info":{"face":"https://i0.hdslb.com/bfs/baselabs/xxx.png","name":"XXX"},
		"risk_ctrl_info":{"face":"https://i0.hdslb.com/bfs/baselabs/xxx.png","name":"XXX"},
		"official_info":{"role":0,"title":"","desc":"","type":-1},
		"official_info":{"desc":"","role":7,"title":"bilibili直播高能主播","type":0},
		"official_info":{"role":7,"title":"专栏优质UP主","desc":"","type":0},
		"official_info":{"desc":"","role":1,"title":"bilibili 知名游戏UP主、直播高能主播","type":0},
		"official_info":{"desc":"","role":1,"title":"bilibili 知名虚拟UP主","type":0},
		"official_info":{"desc":"","role":1,"title":"bilibili 知名游戏UP主","type":0},
		"official_info":{"desc":"","role":1,"title":"bilibili 知名美食UP主","type":0},
		"official_info":{"desc":"","role":1,"title":"bilibili 知名UP主","type":0},
		"official_info":{"role":1,"title":"bilibili 知名游戏UP主","desc":"","type":0},
	},
	"medal":{
		"name":"〇〇〇",
		"level":xx,
		"color_start":398668,"color_end":6850801,"color_border":16771156,"color":398668,
		"id":0,
		"typ":0,
		"is_light":x,
		"ruid":xxx,
		"guard_level":x,
		"score":xxx,
		"guard_icon":"https://i0.hdslb.com/bfs/live/98a201c14a64e860a758f089144dcf3f42e7038c.png",
		"honor_icon":""
	},
	"wealth":{"dm_icon_key":"","level":xxx},
	"title":{"old_title_css_id":"","title_css_id":""},
	"guard":{"level":xxx,"expired_str":"2024-xx-xx23:59:59"},
	"uhead_frame":null,
	"guard_leader":{"is_guard_leader":false}
}
```

### medal__score
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

#### x
```
UNIXts(UTC+8)  
140 000 0000	2014-05-14 00:53:20  
150 000 0000	2017-07-14 10:40:00  
160 000 0000	2020-09-13 20:26:40  
161 000 0000	2021-01-07 14:13:20  
162 000 0000	2021-05-03 08:00:00  
163 000 0000	2021-08-27 01:46:40  
164 000 0000	2021-12-20 19:33:20  
165 000 0000	2022-04-15 13:20:00  
166 000 0000	2022-08-09 07:06:40  
167 000 0000	2022-12-03 00:53:20  
168 000 0000	2023-03-28 18:40:00  
169 000 0000	2023-07-22 12:26:40  
170 000 0000	2023-11-15 06:13:20  
171 000 0000	2024-03-10 00:00:00  
172 000 0000	2024-07-03 17:46:40  
180 000 0000	2027-01-15 16:00:00  
```

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
[热门榜功能下线公告]:https://link.XXXX.com/p/eden/news#/newsdetail?id=3270
