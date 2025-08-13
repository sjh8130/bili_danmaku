#
[主站弹幕](#主站弹幕)
[直播弹幕](#直播弹幕)

## 主站弹幕
| id	| type		| protobuf-name	| - |
|-:|-:|-|-|
| 1		| uint64	| id			| 弹幕ID |
| 2		| uint32	| progress		| 弹幕出现时间（毫秒） |
| 3		| uint32	| mode			| 弹幕类型 |
| 4		| uint32	| fontsize		| 弹幕字号 |
| 5		| uint32	| color			| 弹幕颜色 RGB24 |
| 6		| string	| mid_hash		| 发送者mid hash (CRC32) |
| 7		| string	| content		| 弹幕内容 |
| 8		| uint64	| ctime			| 发送时间 TimeStamp(秒) |
| 9		| uint32	| weight		| 屏蔽等级 |
| 10	| string	| action		| `airborne:[time_ms]` 跳转<br>`picture:图像url` 图片弹幕 |
| 11	| uint32	| pool			| 弹幕池 |
| 12	| string	| idStr			| 弹幕ID |
| 13	| uint32	| attr			| 弹幕属性位 |
| 14	| uint64	| ~~usermid~~	| ~~发送者mid~~ |
| 15	| uint  	| likes			| 点赞数量 |
| 16	| uint  	| *test16*		| 弹幕回复，默认为 0 |
| 17	| uint  	| *test17*		| 弹幕回复，默认为 0 |
| 18	| uint  	| reply_count	| 弹幕回复数量 |
| 19	| ?			| *test19*		| ? |
| 20	| string	| *test20*		| 弹幕回复，默认为str:"0" |
| 21	| string	| *test21*		| 弹幕回复，默认为str:"0" |
| 22	| string	| animation		| json |
| 23	| string	| extra			| |
| 24	| uint  	| colorful		| 彩色弹幕 |
| 25	| uint32	| type			| ? |
| 26	| uint64	| oid			| 视频cid |
| 27	| uint64	| *test27*		| |

### Danmaku__animation
| key				| type	| value		| |
|-|-:|-:|-|
| id				| num	| 			| 20004: 图片弹幕<br>20016: ?<br>20018: NFT弹幕 |
| cid				| num	| 0			| |
| advanced_block	| num	| 0			| |
| animation_attr	| num	| 0			| first:2022-11-07 |
| mime				| str	| "image"	| |
| resource			| str	| url		| ohh、前方高能 图像 <br> NFT头像 |
| scale				| num	| 1			| id==20004 |
```json
// animation
// animation.id
[20004,20005,20006,20008,20009,20010,20011,20014,20017,20022,20025,20028,50001]
// 图片弹幕
{
	"text":"[ohh]",
	"weight":10,
	"action":"picture:i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png?scale=1.00",
	"attr":256,
	"animation":"{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"animation_attr\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png\",\"scale\":1}"
},
{
	"text":"[前方高能]",
	"weight":10,
	"action":"picture:i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png?scale=1.00",
	"attr":256,
	"animation":"{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"animation_attr\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/bd90726bb0c982c161eab7ad67e8460258a8959c.png\",\"scale\":1}"
},
// airborne
{
	"text":"跳楼02:51",
	"action":"airborne:171000"
},
// NFT弹幕（仅移动端）
{
	"attr":2048,
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxx.png\"}"
},
{
	"attr":2048,
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"animation_attr\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxx.png\"}",
},
```
### DmColorful
| id	| type	|
|||
| 0		| None	|
| 60001	| VipGradualColor |
```json
// VipGradualColor
{
	"fill_color":"http://i0.hdslb.com/bfs/dm/9dcd329e617035b45d2041ac889c49cb5edd3e44.png",
	"stroke_color":"http://i0.hdslb.com/bfs/dm/716a749b2461e02df0b4dafb59bbaf0ceab79da9.png"
}
```
### commandDms
| name		| id	| type		| desc	|
|-|-:|-:|-|
| id		| 1		| uint64	| 弹幕id |
| oid		| 2		| uint64	| 视频cid |
| mid		| 3		| uint64	| 发送者mid |
| command	| 4		| string	| 类型 |
| content	| 5		| string	| 互动弹幕正文 |
| progress	| 6		| uint32	| 出现时间 |
| ctime		| 7		| string	| 创建时间 yyyy-MM-dd HH:mm:ss |
| mtime		| 8		| string	| 发布时间 yyyy-MM-dd HH:mm:ss |
| extra		| 9		| string	| json |
| idStr		| 10	| string	| 弹幕id string |
#### command__类型
s1.hdslb.com/bfs/static/player/main/widgets/npd.xxx.xxx.js
| command			| content	|
|-|-|
| #ACTIVITYCOMBO#	| ##"活动弹幕" |
| #ACTORFOLLOW# 	| "合作up主" |
| #ATTENTION#		| "关注弹幕" |
| #CHECKIN#			| ##"签到弹幕" |
| #CMTIME#			| ##"互动弹幕" |
| #GOODSLIKE#		| ##"商品点赞" |
| #GRADE#			| "评分" |
| #GRADESUMMARY#	| 自定义内容 |
| #LINK#			| 自定义内容 |
| #MANAGERFOLLOW#	| ##"管理团队" |
| #RESERVE#			| "预告: 自定义内容" <br> "直播预约: 自定义内容" |
| #REWARDFANS#		| ##"奖励粉丝" |
| #S13GRADE#		| ##"S13评分" |
| #UP#				| 自定义内容 |
| #VOTE#			| "投票弹幕" |
#### ACTIVITYCOMBO
| key					| type	| value	|
|-|-|-|
| activityType			| xxx		| |
| animationCountOne		| xxx		| |
| animationCountThree	| xxx		| |
| animationCountTwo		| xxx		| |
| comboCount			| xxx		| |
| content				| xxx		| |
| duration				| num		| |
| duration				| xxx		| |
| name					| xxx		| |
| numbers				| xxx		| |
| resource				| xxx		| |
| ~~posX~~				| float		| |
| ~~posY~~				| float		| |
| posX_2				| num		| |
| posY_2				| num		| |
#### ACTORFOLLOW__合作up主
| key 16				| type	| value	|
|-|-|-|
| duration				| num		| |
| ~~posX~~				| float		| |
| ~~posY~~				| float		| |
| posX_2				| num		| |
| posY_2				| num		| |
| icon					| str		| (url) |
| mid					| num		| 合作up主 mid |
| midstr				| str		| 合作up主 mid string |
| face					| str		| 合作up主 头像 URL |
| upower_open			| bool		| |
| upower_guide			| str		| |
| upower_state			| num		| |
| upower_icon_web		| str		| |
| upower_button_map		| obj/null	| |
| shrink_icon			| str		| |
| shrink_title			| str		| |
#### ATTENTION__关注
| key 17				| type		| value	|
|-|-|-|
| duration				| num		| |
| posX					| float		| |
| posY					| float		| |
| posX_2				| num		| |
| posY_2				| num		| |
| icon					| str		| (url) |
| type					| num		| 2 |
| arc_type				| num		| 0 |
| shrink_icon			| str		| |
| shrink_title			| str		| |
| upower_open			| bool		| |
| upower_state			| num		| true: <br> false: |
| upower_icon			| str		| true:(url) <br> false: "" |
| upower_icon_web		| str		| true:(url) <br> false: "" |
| upower_jump_url		| str		| true:(url) <br> false: "" |
| upower_button_map		| obj/null	| false: null |
| upower_guide			| str		| |
##### ATTENTION__upower_button_map
| key					| type	| value	|
|-|-|-|
| -1					| obj	| |
| 0						| obj	| |
| 1						| obj	| |
| 2						| obj	| |
##### ATTENTION__upower_button_map__[×××]
| key					| type	| value	|
|-|-|-|
| title					| str	| -1,0,2: "充电" <br> 1: "充电中" |
| icon					| obj	| |
| jump_url				| str	| -1,0,2: --> `upower_jump_url` <br> 1: (url) |
##### ATTENTION__upower_button_map__[×××]__icon
| key					| type	| value	|
|-|-|-|
| 10					| str	| --> `upower_icon` |
| 20					| str	| --> `upower_icon` |
| 30					| str	| --> `upower_icon` |
| 40					| str	| --> `upower_icon` |
| 50					| str	| --> `upower_icon` |
#### CHECKIN
| key 					| type		| value	|
|-|-|-|
| checkin_id			| xxx	| |
| checkin_series_id		| xxx	| |
| join_people			| xxx	| |
| jump_url				| xxx	| |
| shrink_icon			| xxx	| |
| shrink_title			| xxx	| |
| total					| xxx	| |
| type					| xxx	| |
| user_checked			| xxx	| |
| user_checkin_date		| xxx	| |
| user_completed		| xxx	| |
| user_over_number		| xxx	| |
| ~~posX~~				| float	| |
| ~~posY~~				| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
#### CMTIME
| key 					| type	| value	|
|-|-|-|
| ~~posX~~				| float	| |
| ~~posY~~				| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| dm_key_word			| xxx	| |
| duration				| xxx	| |
| slogan_icon			| xxx	| |
| up_slogan				| xxx	| |
#### GOODSLIKE
| key 					| type	| value	|
|-|-|-|
| ~~posX~~				| float	| |
| ~~posY~~				| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| button_icon			| xxx	| |
| button_selected		| xxx	| |
| button_unselected		| xxx	| |
| desc					| xxx	| |
| duration				| xxx	| |
| icon					| xxx	| |
| item_id_str			| xxx	| |
| item_image			| xxx	| |
| keyword				| xxx	| |
| user_sub				| xxx	| |
#### GRADE__评分
| key 19				| type	| value	|
|-|-|-|
| msg					| str	| 评分问题 |
| skin					| num	| 1 / 2 |
| ? posX				| float	| |
| ? posY				| float	| |
| ? posX_2				| num	| |
| ? posY_2				| num	| |
| grade_id				| num	| id |
| duration				| num	| 5000 |
| icon					| str	| (url) |
| mid_score				| num	| |
| count					| num	| |
| avg_score				| float	| |
| skin_unselected		| str	| skin=1: (url)<br>skin=2: (url) |
| skin_selected			| str	| skin=1: (url)<br>skin=2: (url) |
| skin_font_color		| str	| color<br>skin=1: "`#FFB112`"<br>skin=2: "`#FA5555`" |
| summary_duration		| num	| 6000 |
| shrink_icon			| str	| (url) |
| shrink_title			| str	| "推荐" |
| show_status			| num	| 0 |
#### GRADESUMMARY__查看总分
| key 12				| type	| value	|
|-|-|-|
| msg					| str	| 自定义内容 |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| dmids					| \[\]num	| [dmid] |
| duration				| num	| 65000 |
| icon					| str	| (url) |
| grades				| \[\]obj	| |
| shrink_icon			| str	| (url) |
| shrink_title			| str	| "推荐" |
| show_status			| num	| 0 |
##### GRADESUMMARY__grades
| key 7					| type	| value	|
|-|-|-|
| dmid					| num	| |
| dmid_str				| str	| |
| content				| str	| |
| grade_id				| num	| |
| mid_score				| num	| |
| count					| num	| |
| avg_score				| float	| |
#### LINK__链接
| key 16				| type	| value	|
|-|-|-|
| aid					| num	| 目标视频avid |
| title					| str	| 目标视频标题 |
| icon					| str	| (url) |
| bvid					| str	| 目标视频bvid |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| arc_pic				| str	| 目标视频封面 |
| arc_duration			| num	| 目标视频时长 |
| shrink_icon			| str	| (url) |
| shrink_title			| str	| "视频" |
| show_status			| num	| 0 |
| duration				| num	| |
| arc_type				| num	| 0 |
| jump_url				| str	| "" |
| epid					| ?	| "" |
#### RESERVE__预约
| key 28/31				| type	| value	| 备注	|
|-|-|-|-|
| msg					| str	| "预告: 自定义内容" <br> "直播预约: 自定义内容" |
| reserve_type			| num	| 1: 视频 <br> 2: 直播 |
| reserve_id			| num	| id |
| ? live_stime			| num	| TimeStamp(秒) |reserve_type:2
| ? ~~arc_stime~~		| num	| TimeStamp(秒) |reserve_type:2
| ? stime				| num	| TimeStamp(秒) |reserve_type:2
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| duration				| num	| 5000 |
| icon					| str	| (url) |
| reserve_count			| num	| 预约人数 |
| reserve_state			| num	| 0 / 1 |
| user_state			| bool 	| 预约状态 | 需要登录 |
| live_state			| num	| 0: <br> 1:直播中 <br> 2:直播结束 |
| premiere_state		| num	| 0 |
| live_popularity_count	| num	| 0 |
| live_popularity_str	| str	| 直播 :"`x.y万人气`" / "`x人看过`/ "`x.y万人看过`" |
| premiere_online_count	| num	| 0 |
| premiere_view			| num	| 0 |
| jump_url				| str	| 视频/直播回放 URL <br> 直播间URL |
| mid					| num	| 目标视频 UP主mid |
| live_stime_format		| str	| 视频: ""<br>直播: "`(yyyy-)?MM-dd HH:mm`" / "`今天HH:mm`" |
| ~~arc_stime_format~~	| str	| 视频: ""<br>直播: "`(yyyy-)?MM-dd HH:mm`" / "`今天HH:mm`" |
| stime_format			| str	| 视频: ""<br>直播: "`MM-dd HH:mm`" / "`今天HH:mm`" |
| live_lottery			| bool 	| `true` |
| desc					| str	| "" |
| shrink_icon			| str	| (url) |
| shrink_title			| str	| "预约" |
| show_status			| num	| 0 |
```json
{
	"msg": "直播预约：冰火歌会2023冰火夏日夜",
	"reserve_type": 2,
	"reserve_id":xxx,
	"live_stime":xxxxxxxxxx,
	"arc_stime":xxxxxxxxxx,
	"stime":xxxxxxxxxx,
	"posX": 193.43,
	"posY": 251.25,
	"posX_2": 29,
	"posY_2": 67,
	"duration": 5000,
	"icon": "http://i0.hdslb.com/bfs/b/4312fb7b155646fc6fd5f6f8a6a07a062d82587c.png",
	"reserve_count": 125988,
	"reserve_state": 0,
	"user_state": false,
	"live_state": 0,
	"premiere_state": 0,
	"live_popularity_count": 0,
	"live_popularity_str": "",
	"premiere_online_count": 0,
	"premiere_view": 0,
	"jump_url": "",
	"mid": 9617619,
	"live_stime_format": "今天19:00",
	"arc_stime_format": "今天19:00",
	"stime_format": "今天19:00",
	"live_lottery": true,
	"desc": "",
	"shrink_icon": "http://i0.hdslb.com/bfs/b/a4b1c7f03e687f680f7c3629c530e3fdd77d63ed.png",
	"shrink_title": "预约",
	"show_status": 0
}
```
#### REWARDFANS
| key 					| type	| value	|
|-|-|-|
| duration				| xxx	| |
| sub_title				| xxx	| |
| jump_url				| xxx	| |
| dm_key_word			| xxx	| |
| prefix_icon			| xxx	| |
| follow_mid			| xxx	| |
| activity_id			| xxx	| |
| participated			| xxx	| |
| ~~posX~~				| float		| |
| ~~posY~~				| float		| |
| posX_2				| num		| |
| posY_2				| num		| |
#### S13GRADE
| key 					| type	| value	|
|-|-|-|
| ~~posX~~				| float		| |
| ~~posY~~				| float		| |
| posX_2				| num		| |
| posY_2				| num		| |
| bo_slogan				| xxx	| |
| bo_url				| xxx	| |
| duration				| xxx	| |
| keyword				| xxx	| |
| show_status			| xxx	| |
| shrink_icon			| xxx	| |
| shrink_title			| xxx	| |
| teams					| xxx	| |
#### UP__带有【UP】的~~普通~~弹幕
| key					| type	| value	|
|-|-|-|
| icon					| str	| UP主头像URL |
#### VOTE__投票
| key 15				| type	| value	|
|-|-|-|
| vote_id				| num	| id |
| question				| str	| 投票问题 |
| cnt					| num	| 投票人数 |
| options				| array	| 选项 |
| icon					| str	| (url) |
| my_vote				| num	| 我的选项 |
| pub_dynamic			| bool 	| |
| posX					| float	| |
| posY					| float	| |
| posX_2				| num	| |
| posY_2				| num	| |
| duration				| num	| |
| shrink_icon			| str	| (url) |
| shrink_title			| str	| "投票" |
| show_status			| num	| 0 / 1 |
| mid					| ?	| |
| vote_type				| ?	| |
##### VOTE__options
| key					| type	| value	|
|-|-|-|
| idx					| num	| start:1 |
| desc					| str	| 选项内容 |
| cnt					| num	| 0? |
| has_self_def			| bool	| |
#### posX,posY
| key	| min	| max	|
|-|-:|-:|
| posX	| 118	| 549	|
| posY	| 80.5	| 889	|
```javascript
posX_2 = Math.round(posX / 667 * 100)
posY_2 = Math.round(posY / 375 * 100)
```

## 直播弹幕
| CMD	|link	| 备注 |
|-|-|-|
| ACTIVITY_BANNER_CHANGE				| [✅](#ACTIVITY_BANNER_CHANGE)				| |
| ACTIVITY_BANNER_CHANGE_V2				| [✅](#ACTIVITY_BANNER_CHANGE)				| |
| ACTIVITY_MATCH_GIFT					| [❌](#ACTIVITY_MATCH_GIFT)					| |
| ADMIN_SHIELD_KEYWORD					| [✅](#ADMIN_SHIELD_KEYWORD)				| I管理员屏蔽关键词操作记录 |
| ANCHOR_BROADCAST						| [✅](#ANCHOR_BROADCAST)					| I直播过程中时长里程碑广播 |
| ANCHOR_ECOMMERCE_STATUS				| [✅](#ANCHOR_ECOMMERCE_STATUS)				| I?更新电商状态 |
| ANCHOR_HELPER_DANMU					| [✅](#ANCHOR_HELPER_DANMU)					| I主播互动与奖励提醒 |
| ANCHOR_LOT_AWARD						| [✅](#ANCHOR_LOT_AWARD)					| 抽奖: 结果 |
| ANCHOR_LOT_CHECKSTATUS				| [✅](#ANCHOR_LOT_CHECKSTATUS)				| 抽奖: 检查 |
| ANCHOR_LOT_END						| [✅](#ANCHOR_LOT_END)						| 抽奖: 结束 |
| ANCHOR_LOT_NOTICE						| [✅](#ANCHOR_LOT_NOTICE)					| I弹幕提示抽奖活动信息通知 |
| ANCHOR_LOT_START						| [✅](#ANCHOR_LOT_START)					| 抽奖: 开始 |
| ANCHOR_LOTTERY_ACTIVITY				| [❌](#ANCHOR_LOTTERY_ACTIVITY)				| |
| ANCHOR_NORMAL_NOTIFY					| [✅](#ANCHOR_NORMAL_NOTIFY)				| I主播获得推荐位通知 |
| AREA_RANK_CHANGED						| [✅](#AREA_RANK_CHANGED)					| #直播排名 |
| BAINIAN2020							| [❌](#BAINIAN2020)							| |
| BENEFIT_CARD_CLEAN					| [✅](#BENEFIT_CARD_CLEAN)					| |
| BENEFIT_STATUS						| [❌](#BENEFIT_STATUS)						| |
| BIG_R_WELCOME							| [❌](#BIG_R_WELCOME)						| |
| BOX_ACTIVITY_START					| [❌](#BOX_ACTIVITY_START)					| |
| CARD_MSG								| [✅](#CARD_MSG)							| I卡片消息提醒关注主播 |
| CHANGE_ROOM_INFO						| [✅](#CHANGE_ROOM_INFO)					| WEB:更改直播间背景 |
| CHASE_FRAME_SWITCH					| [❌](#CHASE_FRAME_SWITCH)					| |
| CHG_RANK_REFRESH						| [✅](#CHG_RANK_REFRESH)					| |
| CNY_SESSION_CHANGE					| [✅](#CNY_SESSION_CHANGE)					| 2025春节专用 |
| COLLECTION_PRAISE_STATUS				| [❌](#COLLECTION_PRAISE_STATUS)			| |
| COLLECTION_PRAISE_UPDATE_PROCESS		| [❌](#COLLECTION_PRAISE_UPDATE_PROCESS)	| |
| COMBO_END								| [✅](#COMBO_END)							| 送礼物: 连击 |
| COMBO_SEND							| [✅](#COMBO_SEND)							| 送礼物: 连击 |
| COMMON_ANIMATION						| [✅](#COMMON_ANIMATION)					| |
| COMMON_NOTICE_DANMAKU					| [✅](#COMMON_NOTICE_DANMAKU)				| 弹幕区域: 通知 |
| CONFIRM_AUTO_FOLLOW					| [❌](#CONFIRM_AUTO_FOLLOW)					| |
| CUSTOM_NOTICE_CARD					| [✅](#CUSTOM_NOTICE_CARD)					| |!!!
| CUT_OFF								| [✅](#CUT_OFF)								| 切断直播！ **服务端可能不会发送此消息** |
| DAILY_RANK_SPECIAL					| [❌](#DAILY_RANK_SPECIAL)					| |
| DANMU_ACTIVITY_CONFIG					| [✅](#DANMU_ACTIVITY_CONFIG)				| |
| DANMU_AGGREGATION						| [✅](#DANMU_AGGREGATION)					| 通知栏: 抽奖通知 |
| DANMU_EXTRA							| [❌](#DANMU_EXTRA)							| |
| DANMU_GIFT_LOTTERY_AWARD				| [❌](#DANMU_GIFT_LOTTERY_AWARD)			| |
| DANMU_GIFT_LOTTERY_END				| [❌](#DANMU_GIFT_LOTTERY_END)				| |
| DANMU_GIFT_LOTTERY_START				| [❌](#DANMU_GIFT_LOTTERY_START)			| |
| DANMU_MSG								| [✅](#DANMU_MSG)							| 弹幕 |
| DANMU_TAG_CHANGE						| [❌](#DANMU_TAG_CHANGE)					| |
| DM_INTERACTION						| [✅](#DM_INTERACTION)						| 互动弹幕（投票、他们都在说） |
| EFFECT_DANMAKU_MSG					| [❌](#EFFECT_DANMAKU_MSG)					| |
| ENTRY_EFFECT							| [✅](#ENTRY_EFFECT)						| 进入直播间特效 |
| ENTRY_EFFECT_MUST_RECEIVE				| [✅](#ENTRY_EFFECT)						| 进入直播间特效 |
| EXTRA_BENEFIT_CARD					| [❌](#EXTRA_BENEFIT_CARD)					| |
| FANS_CLUB_POKE_GIFT_NOTICE			| [❌](#FANS_CLUB_POKE_GIFT_NOTICE)			| |
| FOLLOW_PUBLISH_SINGLE					| [❌](#FOLLOW_PUBLISH_SINGLE)				| |
| FREE_GIFT_BUBBLE						| [❌](#FREE_GIFT_BUBBLE)					| |
| FULL_SCREEN_MASK_OPEN					| [❌](#FULL_SCREEN_MASK_OPEN)				| |
| FULL_SCREEN_SPECIAL_EFFECT			| [✅](#FULL_SCREEN_SPECIAL_EFFECT)			| |
| FUNCTION_CARD							| [❌](#FUNCTION_CARD)						| |
| GIFT_BOARD_RED_DOT					| [✅](#GIFT_BOARD_RED_DOT)					| |
| GIFT_PANEL_PLAN						| [✅](#GIFT_PANEL_PLAN)						| I礼物面板计划调整 |
| GIFT_STAR_PROCESS						| [✅](#GIFT_STAR_PROCESS)					| 礼物星球: 进度 |
| GOTO_BUY_FLOW							| [✅](#GOTO_BUY_FLOW)						| 移动端 购买 |
| GUARD_ACHIEVEMENT_ROOM				| [✅](#GUARD_ACHIEVEMENT_ROOM)				| 恭喜主播xxx舰队规模突破xxx |
| GUARD_BENEFIT_RECEIVE					| [❌](#GUARD_BENEFIT_RECEIVE)				| |
| GUARD_BUY								| [✅🗑](#GUARD_BUY)							| 大航海购买(旧) |
| GUARD_HONOR_THOUSAND					| [✅](#GUARD_HONOR_THOUSAND)				| 千舰 |
| GUARD_LEADER_NOTICE					| [✅](#GUARD_LEADER_NOTICE)					| 舰队指挥官 |
| GUARD_LOTTERY_START					| [❌](#GUARD_LOTTERY_START)					| |
| GUARD_WINDOWS_OPEN					| [❌](#GUARD_WINDOWS_OPEN)					| |
| HAS_GUARD_PILOT						| [❌](#HAS_GUARD_PILOT)						| |
| HOT_BUY_NUM							| [✅](#HOT_BUY_NUM)							| 移动端: 购物 |
| HOT_RANK_CHANGED						| [✅🗑](#HOT_RANK_CHANGED)					| **已移除** |
| HOT_RANK_CHANGED_V2					| [✅🗑](#HOT_RANK_CHANGED)					| **已移除** |
| HOT_RANK_SETTLEMENT					| [✅🗑](#HOT_RANK_SETTLEMENT)					| **已移除** |
| HOT_RANK_SETTLEMENT_V2				| [✅🗑](#HOT_RANK_SETTLEMENT)					| **已移除** |
| HALF_SCREEN_TRIGGER					| [✅](#HALF_SCREEN_TRIGGER)					| |
| HOT_ROOM_NOTIFY						| [✅](#HOT_ROOM_NOTIFY)						| |
| HOUR_RANK_AWARDS 						| [✅](#HOUR_RANK_AWARDS)					| |
| INTERACT_JOIN							| [❌](#INTERACT_JOIN)						| |
| INTERACT_JOIN_OLD						| [❌](#INTERACT_JOIN_OLD)					| |
| INTERACT_LEAVE						| [❌](#INTERACT_LEAVE)						| |
| INTERACT_OPERATION					| [❌](#INTERACT_OPERATION)					| |
| INTERACT_WORD							| [✅🗑](#INTERACT_WORD)						| 通知栏: 进入直播间/关注主播 |
| INTERACT_WORD_V2						| [✅](#INTERACT_WORD_V2)					| 通知栏: 进入直播间/关注主播 |
| INTERACTIVE_USER						| [✅](#INTERACTIVE_USER)					| 特殊玩法@ |
| LIKE_GUIDE_USER						| [✅](#LIKE_GUIDE_USER)						| 点赞引导 |
| LIKE_INFO_V3_CLICK					| [✅](#LIKE_INFO_V3_CLICK)					| 点赞 |
| LIKE_INFO_V3_NOTICE					| [✅](#LIKE_INFO_V3_NOTICE)					| 弹幕区域: 点赞通知 |
| LIKE_INFO_V3_UPDATE					| [✅](#LIKE_INFO_V3_UPDATE)					| 状态栏: 点赞更新 |
| LIKE_SO_HOT 							| [❌](#LIKE_SO_HOT)							| |
| LITTLE_MESSAGE_BOX					| [✅](#LITTLE_MESSAGE_BOX)					| 提示弹窗，仅用户本人 |
| LITTLE_TIPS 							| [✅](#LITTLE_TIPS)							| 提示弹窗，仅用户本人 |
| LIVE									| [✅](#LIVE)								| 开播/主播断流重连 |
| LIVE_ANCHOR_SWITCH_UPDATE				| [❌](#LIVE_ANCHOR_SWITCH_UPDATE)			| |
| LIVE_ANI_RES_UPDATE					| [✅](#LIVE_ANI_RES_UPDATE)					| I直播动态礼物资源信息更新命令 |
| LIVE_INTERACT_GAME_STATE_CHANGE		| [✅](#LIVE_INTERACT_GAME_STATE_CHANGE)		| 互动玩法 |
| LIVE_INTERACTIVE_GAME					| [✅](#LIVE_INTERACTIVE_GAME)				| 游戏 |
| LIVE_INTERNAL_ROOM_LOGIN				| [❌](#LIVE_INTERNAL_ROOM_LOGIN)			| |
| LIVE_MULTI_VIEW_CHANGE				| [✅](#LIVE_MULTI_VIEW_CHANGE)				| 直播多视角 |
| LIVE_MULTI_VIEW_EVENT_CHANGE			| [✅](#LIVE_MULTI_VIEW_EVENT_CHANGE)		| 直播多视角 |
| LIVE_MULTI_VIEW_NEW_INFO				| [✅](#LIVE_MULTI_VIEW_NEW_INFO)			| 直播多视角 |
| LIVE_OPEN_PLATFORM_CLOUD_GAME			| [❌](#LIVE_OPEN_PLATFORM_CLOUD_GAME)		| |
| LIVE_OPEN_PLATFORM_GAME				| [✅](#LIVE_OPEN_PLATFORM_GAME)				| 弹幕互动游戏 |
| LIVE_PANEL_CHANGE						| [✅](#LIVE_PANEL_CHANGE)					| I更新直播面板内容 |
| LIVE_PANEL_CHANGE_CONTENT				| [✅](#LIVE_PANEL_CHANGE_CONTENT)			| I更新直播面板内容 |
| LIVE_PANEL_ICON_INFO					| [❌](#LIVE_PANEL_ICON_INFO)				| |
| LIVE_PLAYER_LOG_RECYCLE				| [❌](#LIVE_PLAYER_LOG_RECYCLE)				| |
| LIVE_ROOM_TOAST_MESSAGE				| [✅](#LIVE_ROOM_TOAST_MESSAGE)				| PK |
| LOG_IN_NOTICE							| [✅](#LOG_IN_NOTICE)						| 游客保护 |
| LOL_ACTIVITY							| [❌](#LOL_ACTIVITY)						| |
| LOL_PLAYER_GRADE						| [✅](#LOL_PLAYER_GRADE)					| LOL |
| LPL_REALTIME_STATUS_CHANGED			| [✅](#LPL_REALTIME_STATUS_CHANGED)			| LOL |
| master_qn_strategy_chg				| [❌](#master_qn_strategy_chg)				| |
| MATCH_TEAM_GIFT_RANK					| [❌](#MATCH_TEAM_GIFT_RANK)				| |
| MESSAGEBOX_USER_GAIN_MEDAL			| [✅](#MESSAGEBOX_USER_GAIN_MEDAL)			| 获得粉丝牌 |
| MESSAGEBOX_USER_MEDAL_CHANGE			| [✅](#MESSAGEBOX_USER_MEDAL_CHANGE)		| 粉丝牌升级 |
| MESSAGEBOX_USER_MEDAL_COMPENSATION	| [❌](#MESSAGEBOX_USER_MEDAL_COMPENSATION)	| |
| MILESTONE_UPDATE_EVENT 				| [❌](#MILESTONE_UPDATE_EVENT)				| |
| MULTI_VOICE_APPLICATION				| [❌](#MULTI_VOICE_APPLICATION)				| 连麦 |
| MULTI_VOICE_APPLICATION_ANCHOR		| [✅](#MULTI_VOICE_APPLICATION_ANCHOR)		| 连麦 |
| MULTI_VOICE_APPLICATION_USER			| [✅](#MULTI_VOICE_APPLICATION_USER)		| 连麦 |
| MULTI_VOICE_ENTER_ANCHOR				| [✅](#MULTI_VOICE_ENTER_ANCHOR)			| 连麦 |
| MULTI_VOICE_OPERATIN					| [✅](#MULTI_VOICE_OPERATIN)				| 连麦 |
| MULTI_VOICE_OWNER_LEAVE				| [✅](#MULTI_VOICE_OWNER_LEAVE)				| 连麦 |
| MULTI_VOICE_PK_HAT_STATUS				| [❌](#MULTI_VOICE_PK_HAT_STATUS)			| 连麦 |
| MULTI_VOICE_PK_STATUS					| [✅](#MULTI_VOICE_PK_STATUS)				| 连麦 |
| MULTI_VOICE_PK_STATUS_V2				| [❌](#MULTI_VOICE_PK_STATUS_V2)			| 连麦 |
| MULTI_VOICE_SEND_EMOJI				| [❌](#MULTI_VOICE_SEND_EMOJI)				| 连麦 |
| MULTI_VOICE_STATUS_SYNC				| [❌](#MULTI_VOICE_STATUS_SYNC)				| 连麦 |
| MULTI_VOICE_STATUS_SYNC_ANCHOR		| [✅](#MULTI_VOICE_STATUS_SYNC_ANCHOR)		| 连麦 |
| MVROLECHANGE							| [✅](#MVROLECHANGE)						| |
| NEW_PK_REJECT							| [❌](#NEW_PK_REJECT)						| |
| NEW_PK_START							| [✅](#NEW_PK_START)						| |
| NOTICE_MSG							| [✅](#NOTICE_MSG)							| 滚动横幅 |
| OBS_SHIELD_STATUS_UPDATE				| [✅](#OBS_SHIELD_STATUS_UPDATE)			| |
| OFFICIAL_ROOM_EVENT					| [✅](#OFFICIAL_ROOM_EVENT)					| |
| ON_COMMON_CARD_UPDATE					| [✅](#ON_COMMON_CARD_UPDATE)				| |
| ONLINE_RANK_COUNT						| [✅](#ONLINE_RANK_COUNT)					| 状态栏: 在线观众 |
| ONLINE_RANK_TOP3						| [✅](#ONLINE_RANK_TOP3)					| 高能榜: 高能用户前三恭喜 |
| ONLINE_RANK_V2						| [✅](#ONLINE_RANK_V2)						| 高能榜: 高能用户TOP7 |
| OTHER_SLICE_LOADING_RESULT			| [✅](#OTHER_SLICE_LOADING_RESULT)			| |
| OTHER_SLICE_PUBLISH_RESULT			| [❌](#OTHER_SLICE_PUBLISH_RESULT)			| |
| OTHER_SLICE_SETTING_CHANGED			| [✅](#OTHER_SLICE_SETTING_CHANGED)			| |
| PANEL_INTERACTIVE_NOTIFY_CHANGE		| [✅](#PANEL_INTERACTIVE_NOTIFY_CHANGE)		| |
| PK_AGAIN								| [❌](#PK_ALL)								| PK |
| PK_AUDIENCE							| [❌](#PK_ALL)								| PK |
| PK_BATTLE_ABNORMAL					| [❌](#PK_ALL)								| PK |
| PK_BATTLE_CRIT						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_END							| [✅](#PK_ALL)								| PK |
| PK_BATTLE_END_NEW						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_ENTRANCE					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_FINAL_PROCESS				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_GIFT						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_MATCH_TIMEOUT				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_MULTIPLE_AWARD				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_MULTIPLE_BEGIN				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_MULTIPLE_DRAW_RES			| [✅](#PK_ALL)								| PK |
| PK_BATTLE_MULTIPLE_RES				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PRE							| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PRE_NEW						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PRO_TYPE					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PROCESS						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PROCESS_NEW					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_PUNISH_END					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_RANK_CHANGE					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_SETTLE						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_SETTLE_NEW					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_SETTLE_USER					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_SETTLE_V2					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_SPECIAL_GIFT				| [✅](#PK_ALL)								| PK |
| PK_BATTLE_START						| [✅](#PK_ALL)								| PK |
| PK_BATTLE_START_NEW					| [✅](#PK_ALL)								| PK |
| PK_BATTLE_VIDEO_PUNISH_BEGIN			| [✅](#PK_ALL)								| PK |
| PK_BATTLE_VIDEO_PUNISH_END			| [✅](#PK_ALL)								| PK |
| PK_BATTLE_VOTES_ADD					| [✅](#PK_ALL)								| PK |
| PK_END								| [❌](#PK_ALL)								| PK |
| PK_INFO								| [✅](#PK_ALL)								| PK |
| PK_LOTTERY_START						| [❌](#PK_ALL)								| PK |
| PK_MATCH								| [❌](#PK_ALL)								| PK |
| PK_MIC_END							| [❌](#PK_ALL)								| PK |
| PK_PRE								| [❌](#PK_ALL)								| PK |
| PK_PROCESS							| [❌](#PK_ALL)								| PK |
| PK_SETTLE								| [❌](#PK_ALL)								| PK |
| PK_START								| [❌](#PK_ALL)								| PK |
| PLAY_PROGRESS_BAR						| [❌](#PLAY_PROGRESS_BAR)					| |
| PLAY_TAG								| [✅](#PLAY_TAG)							| LOL/KPL 比赛: 事件 |
| PLAY_TICKETS_NOTIFY					| [❌](#PLAY_TICKETS_NOTIFY)					| |
| PLAY_TOGETHER							| [❌](#PLAY_TOGETHER)						| |
| PLAYTOGETHER_ICON_CHANGE				| [✅](#PLAYTOGETHER_ICON_CHANGE)			| |
| PLAYTOGETHER_ORDER_VOICE_DISPATCH		| [❌](#PLAYTOGETHER_ORDER_VOICE_DISPATCH)	| |
| PLAYTOGETHER_SERVICE_CARD_CHANGE		| [❌](#PLAYTOGETHER_SERVICE_CARD_CHANGE)	| |
| PLAYURL_RELOAD						| [✅](#PLAYURL_RELOAD)						| |
| POPULAR_RANK_CHANGED					| [✅](#POPULAR_RANK_CHANGED)				| 排行榜 |
| POPULAR_RANK_GUIDE_CARD				| [✅](#POPULAR_RANK_GUIDE_CARD)				| 排行榜 |
| POPULARITY_RANK_TAB_CHG				| [✅](#POPULARITY_RANK_TAB_CHG)				| 人气xxx |
| POPULARITY_RED_POCKET_NEW				| [✅](#POPULARITY_RED_POCKET_NEW)			| 人气红包 new(抽奖) |
| POPULARITY_RED_POCKET_START			| [✅](#POPULARITY_RED_POCKET_START)			| 人气红包 抽奖开始 |
| POPULARITY_RED_POCKET_V2_NEW			| [✅](#POPULARITY_RED_POCKET_NEW)			| 人气红包 new(抽奖) |
| POPULARITY_RED_POCKET_V2_START		| [✅](#POPULARITY_RED_POCKET_START)			| 人气红包 抽奖开始 |
| POPULARITY_RED_POCKET_V2_WINNER_LIST	| [✅](#POPULARITY_RED_POCKET_WINNER_LIST)	| 人气红包 抽奖结果 |
| POPULARITY_RED_POCKET_WINNER_LIST		| [✅](#POPULARITY_RED_POCKET_WINNER_LIST)	| 人气红包 抽奖结果 |
| PREPARING								| [✅](#PREPARING)							| 结束直播 |
| PROGRAM_CHANGE						| [✅](#PROGRAM_CHANGE)						| |
| RADIO_BACKGROUND						| [✅](#RADIO_BACKGROUND)					| |
| RAFFLE_END							| [❌](#TV_END)								| |
| RAFFLE_START							| [❌](#TV_START)							| |
| RANK_CHANGED							| [✅](#RANK_CHANGED)						| #直播排名 |
| RANK_CHANGED_V2						| [✅](#RANK_CHANGED)						| #直播排名 |
| RANK_REM								| [✅](#RANK_REM)							| |
| RECALL_DANMU_MSG						| [✅](#RECALL_DANMU_MSG)					| 弹幕-临时封禁(mid) |
| RECOMMEND_CARD						| [✅](#RECOMMEND_CARD)						| 商品推销(移动端) |
| RED_POCKET_START						| [❌](#RED_POCKET_START)					| |
| REDIRECT_EMPTY_PAGE					| [❌](#REDIRECT_EMPTY_PAGE)					| |
| REENTER_LIVE_ROOM						| [✅](#REENTER_LIVE_ROOM)					| |
| REENTER_LIVE_ROOM_V2					| [✅](#REENTER_LIVE_ROOM)					| |
| Revenue_PayLimit						| [❌](#Revenue_PayLimit)					| |
| REVENUE_RANK_CHANGED					| [✅](#REVENUE_RANK_CHANGED)				| #直播排名 |
| RING_STATUS_CHANGE					| [✅](#RING_STATUS_CHANGE)					| |
| RING_STATUS_CHANGE_V2					| [✅](#RING_STATUS_CHANGE)					| |
| room_admin_entrance					| [✅](#room_admin_entrance)					| |
| ROOM_ADMIN_REVOKE						| [✅](#ROOM_ADMIN_REVOKE)					| |
| ROOM_ADMINS							| [✅](#ROOM_ADMINS)							| |
| ROOM_BANNER							| [✅](#WIDGET_BANNER)						| |
| ROOM_BLOCK_INTO						| [❌](#ROOM_BLOCK_INTO)						| |
| ROOM_BLOCK_MSG						| [✅](#ROOM_BLOCK_MSG)						| 用户封禁 |
| ROOM_CHANGE							| [✅](#ROOM_CHANGE)							| 直播信息更改 |
| ROOM_KICKOUT							| [❌](#ROOM_KICKOUT)						| |
| ROOM_LIMIT							| [❌](#ROOM_LIMIT)							| |
| ROOM_LIVE_FORBID						| [❌](#ROOM_LIVE_FORBID)					| |
| ROOM_LOCK								| [✅](#ROOM_LOCK)							| |
| ROOM_MODULE_DISPLAY					| [✅](#ROOM_MODULE_DISPLAY)					| |
| ROOM_NEWS_AUDIT_CHANGE				| [✅](#ROOM_NEWS_AUDIT_CHANGE)				| |
| ROOM_NEWS_UPDATE						| [✅](#ROOM_NEWS_UPDATE)					| |
| ROOM_RANK								| [❌](#ROOM_RANK)							| |
| ROOM_REAL_TIME_MESSAGE_UPDATE			| [✅](#ROOM_REAL_TIME_MESSAGE_UPDATE)		| 当前粉丝团人数，关注人数 |
| ROOM_REFRESH							| [✅](#ROOM_REFRESH)						| @todo |
| ROOM_SILENT_ON						| [✅](#ROOM_SILENT)							| 直播间全局禁言 |
| ROOM_SILENT_OFF						| [✅](#ROOM_SILENT)							| 直播间全局禁言 |
| ROOM_SKIN_MSG							| [✅](#ROOM_SKIN_MSG)						| 直播间背景 |
| ROOM_SWITCH_INFO_CONFIG_CHANGE		| [✅](#ROOM_SWITCH_INFO_CONFIG_CHANGE)		| |
| RUN_UP_DOWN_GUIDE						| [❌](#RUN_UP_DOWN_GUIDE)					| |
| SEND_GIFT								| [✅](#SEND_GIFT)							| 送礼物 |
| SEND_GIFT_V2							| [✅](#SEND_GIFT)							| 送礼物(LPL) |
| SEND_TOP								| [❌](#SEND_TOP)							| |
| SHOPPING_BUBBLES_STYLE				| [✅](#SHOPPING_BUBBLES_STYLE)				| ?购物车 |
| SHOPPING_CART_ITEM					| [❌](#SHOPPING_CART_ITEM)					| |
| SHOPPING_CART_SHOW					| [✅](#SHOPPING_CART_SHOW)					| ?购物车 |
| SHOPPING_EXPLAIN_CARD					| [✅](#SHOPPING_EXPLAIN_CARD)				| ?购物车 |
| SHOPPING_NOTICE						| [❌](#SHOPPING_NOTICE)						| |
| SPECIAL_GIFT							| [✅](#SPECIAL_GIFT)						| 特殊礼物 |
| SPREAD_ORDER							| [✅](#SPREAD_ORDER)						| |
| SPREAD_SHOW_FEET_V2					| [✅](#SPREAD_SHOW_FEET_V2)					| |
| STARLIVE_PK_MSG						| [❌](#STARLIVE_PK_MSG)						| |
| STOP_LIVE_ROOM_LIST					| [✅](#STOP_LIVE_ROOM_LIST)					| |
| STUDIO_ROOM_CLOSE						| [✅](#STUDIO_ROOM_CLOSE)					| |
| SUPER_CHAT_AUDIT						| [❌](#SUPER_CHAT_AUDIT)					| |
| SUPER_CHAT_ENTRANCE					| [✅](#SUPER_CHAT_ENTRANCE)					| SuperChat|
| SUPER_CHAT_MESSAGE					| [✅](#SUPER_CHAT_MESSAGE)					| SuperChat |
| SUPER_CHAT_MESSAGE_DELETE				| [✅](#SUPER_CHAT_MESSAGE_DELETE)			| SuperChat 删除 |
| SUPER_CHAT_MESSAGE_JPN				| [✅](#SUPER_CHAT_MESSAGE_JPN)				| SuperChat 日本語 |
| SUPER_VIP_CONNECT_DIG_V2				| [❌](#SUPER_VIP_CONNECT_DIG_V2)			| |
| SWITCH_CONFIG_BUBBLE					| [❌](#SWITCH_CONFIG_BUBBLE)				| |
| SYS_MSG								| [✅](#SYS_MSG)								| |
| THERMAL_STORM_DANMU_BEGIN				| [❌](#THERMAL_STORM_DANMU_BEGIN)			| |
| THERMAL_STORM_DANMU_CANCEL			| [❌](#THERMAL_STORM_DANMU_CANCEL)			| |
| THERMAL_STORM_DANMU_OVER				| [❌](#THERMAL_STORM_DANMU_OVER)			| |
| THERMAL_STORM_DANMU_UPDATE			| [❌](#THERMAL_STORM_DANMU_UPDATE)			| |
| TRADING_SCORE							| [✅](#TRADING_SCORE)						| |
| TRANSFER_FLOW_INFO					| [❌](#TRANSFER_FLOW_INFO)					| |
| TV_END								| [❌](#TV_END)								| |
| TV_START								| [❌](#TV_START)							| |
| UNIVERSAL_EVENT_GIFT					| [✅](#UNIVERSAL_EVENT_GIFT)				| |
| UNIVERSAL_EVENT_GIFT_V2				| [✅](#UNIVERSAL_EVENT_GIFT_V2)				| |
| UNIVERSAL_INTERACT_INVITATION			| [❌](#UNIVERSAL_INTERACT_INVITATION)		| |
| UNIVERSAL_INTERACT_JOIN				| [❌](#UNIVERSAL_INTERACT_JOIN)				| |
| UNIVERSAL_INTERACT_LEAVE				| [❌](#UNIVERSAL_INTERACT_LEAVE)			| |
| UNIVERSAL_INTERACT_OPERATION			| [❌](#UNIVERSAL_INTERACT_OPERATION)		| |
| USER_INFO_UPDATE						| [✅](#USER_INFO_UPDATE)					| |
| USER_PANEL_RED_ALARM					| [✅](#USER_PANEL_RED_ALARM)				| |
| USER_START_PROPHET					| [❌](#USER_START_PROPHET)					| |
| USER_TITLE_GET						| [❌](#USER_TITLE_GET)						| |
| USER_TOAST_MSG						| [✅](#USER_TOAST_MSG)						| 大航海购买(新) |
| USER_TOAST_MSG_V2						| [✅](#USER_TOAST_MSG_V2)					| 大航海购买(新新) |
| USER_VIRTUAL_MVP						| [✅](#USER_VIRTUAL_MVP)					| 守护圣法师 |
| VIDEO_CONNECTION_JOIN_END				| [❌](#VIDEO_CONNECTION_JOIN_END)			| |
| VIDEO_CONNECTION_JOIN_START			| [❌](#VIDEO_CONNECTION_JOIN_START)			| |
| VIDEO_CONNECTION_MSG					| [❌](#VIDEO_CONNECTION_MSG)				| |
| VOICE_CHAT_UPDATE						| [✅](#VOICE_CHAT_UPDATE)					| 移动端:直播间背景 |
| VOICE_CONN_EVENT						| [❌](#VOICE_CONN_EVENT)					| |
| VOICE_JOIN_ANCHOR_DEAL_USER			| [❌](#VOICE_JOIN_ANCHOR_DEAL_USER)			| |
| VOICE_JOIN_LIST						| [✅](#VOICE_JOIN_LIST)						| 语音: 连麦 |
| VOICE_JOIN_ROOM_COUNT_INFO			| [✅](#VOICE_JOIN_ROOM_COUNT_INFO)			| 语音: 连麦排队 |
| VOICE_JOIN_STATUS						| [✅](#VOICE_JOIN_STATUS)					| 语音: 连麦 |
| VOICE_JOIN_SWITCH						| [✅](#VOICE_JOIN_SWITCH)					| |
| VOICE_JOIN_SWITCH_V2					| [✅](#VOICE_JOIN_SWITCH)					| |
| VOICE_JOIN_USER_START					| [❌](#VOICE_JOIN_USER_START)				| |
| VTR_GIFT_LOTTERY						| [❌](#VTR_GIFT_LOTTERY)					| |
| WARNING								| [✅](#WARNING)								| 警告 |
| WATCH_LPL_EXPIRED						| [❌](#WATCH_LPL_EXPIRED)					| |
| WATCH_ROOM_TOAST_MESSAGE				| [❌](#WATCH_ROOM_TOAST_MESSAGE)			| |
| WATCHED_CHANGE						| [✅](#WATCHED_CHANGE)						| 观看人数 |
| WEALTH_NOTIFY							| [✅](#WEALTH_NOTIFY)						| |
| WEB_REPORT_CONTROL					| [❌](#WEB_REPORT_CONTROL)					| |
| WIDGET_BANNER							| [✅](#WIDGET_BANNER)						| |
| WIDGET_GIFT_STAR_KNIGHT				| [❌](#WIDGET_GIFT_STAR_KNIGHT)				| |
| WIDGET_GIFT_STAR_PROCESS				| [✅](#WIDGET_GIFT_STAR_PROCESS)			| 礼物星球 |
| WIDGET_WISH_INFO						| [✅](#WIDGET_WISH_INFO)					| 礼物星球 |
| WIDGET_WISH_INFO_V2					| [✅](#WIDGET_WISH_INFO)					| 礼物星球 |
| WIDGET_WISH_LIST						| [✅](#WIDGET_WISH_LIST)					| |
| WIN_ACTIVITY							| [✅](#WIN_ACTIVITY)						| |
| WIN_ACTIVITY_USER						| [❌](#WIN_ACTIVITY_USER)					| |

| [--](#XXXXXXXXXXXX)
----
### LOG_IN_NOTICE
[TOP](#直播弹幕)  
```json
文档更新：2024-xx-xx  
20230726"为保护用户隐私，未注册登陆用户将无法查看他人昵称"  
20230814"为保护用户隐私，未登录无法查看他人昵称"+image_app  
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
文档更新：2024-xx-xx  
**警告**  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WARNING" |
| msg		| str	| |
| roomid	| str	| 直播间id |
#### WARNING__msg
```json
{"cmd":"WARNING","roomid":12345,"msg":"xxx"}
"****涉及引战"
"分区错误，直播该游戏请移至xxx分区直播"
"禁止宣传第三方平台"
"禁止宣传平台外交易"
"禁止在直播间内展示平台外的评论、弹幕内容，请立即调整"
"禁止直播违禁游戏，请立即更换"
"图片内容不适宜，请立即调整"
"违反直播分区规范，请立即更换至游戏区"
"未按要求遮挡好友申请通知，请查看游戏直播注意事项"
"虚拟主播形象涉及低俗内容"
"虚拟主播形象涉及低俗违规，请至社区公约查看相关规范；常见违规内容，如：着装不雅/暴露、存在低俗元素等"
"因版权原因，请立即调整"
"直播该游戏，请转移至对应的游戏分区，虚拟主播请转移至虚拟Gamer分区进行直播"
"直播该游戏，请转移至对应的游戏分区进行直播"
"直播该游戏请移至虚拟APEX、APEX英雄分区直播"
"直播该游戏请移至虚拟APEX或APEX英雄分区直播"
"直播间画面涉及低俗内容，如：文字信息涉及低俗诱导、画面涉及低俗图片/低俗形象、画面涉及低俗物品等"
"直播间涉及版权侵权，如：播放无授权的影视节目、演唱会、歌曲、赛事、录播盗播他人直播或作品等内容"
"直播视角不适宜"
"直播中请勿聚焦/突出敏感部位（如胸/臀/腿等部位）"
"直播中涉及低俗内容"
"直播中涉及低俗语音，如：低俗诱导打赏、低俗语聊、使用诱惑/挑逗性质的声音等"
```
----
### LIVE
[TOP](#直播弹幕)  
文档更新：2025-04-xx  
开播/主播断线重连(重新推流)
| key 10,11			| type	| value	|
|-|-|-|
| cmd				| str	| "LIVE" |
| live_key			| str	| num(18) |
| voice_background	| str	| 直播间背景(URL) |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| 开播方式 | |
| live_model		| num	| ?0 1 2 3 4 5 |
| roomid			| num	| 长直播间ID |
| ?live_time		| num	| 开播时间TimeStamp(秒) |
| special_type		| \[\]num	| |
| ?delay			| obj	| |
| ?scatter			| obj	| |
```json
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:xxxxxxxxxx","live_platform":"xxx","live_model":xxx,"roomid":xxx,"live_time":xxxxxxxxxx,"special_types":[xxx]}
{"cmd":"LIVE","delay":{"min":10,"max":30},"scatter":{"min":10,"max":30},"special_type":1,"roomid":"xxx"}
{"cmd":"LIVE","live_key":"111111111111111111","voice_background":"","sub_session_key":"111111111111111111sub_time:xxxxxxxxxx","live_platform":"xxx","live_model":xxx,"roomid":xxx}
```
#### live_platform
| live_platform		| desc	| |
|-|-|-|
| live_mng			| ?官方直播 | LPL/1号直播间(5440)/...
| vc_mng			| ? |
| pc				| ~~ |
| pc_link			| PC 直播姬 |
| ios				| iOS APP |
| ios_link			| iOS 直播姬 |
| android			| Android APP |
| android_link		| Android 直播姬 |
| events_broadcast	| |
| harmony?			| harmony |
| harmony_link?		| ?harmony 直播姬 |
| xxxxxxxxxxxxxxx	| xxx |
| xxxxxxxxxxxxxxx	| xxx |
----
### SEND_GIFT
[TOP](#直播弹幕)  
文档更新：2025-07-01  
送礼物  
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "SEND_GIFT/SEND_GIFT_V2" |
| danmu			| obj	| |
| data			| obj	| |
#### SEND_GIFT__danmu
| key					| type		| value	|
|-|-|-|
| area					| num		| 0,1 |
#### SEND_GIFT__data
| key 59				| type		| value	|
|-|-|-|
| pb					| base64(protobuf)	| |
| action				| str		| "投喂" |
| bag_gift				| null/obj	| |
| batch_combo_id		| str		| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{TimeStamp:.4f}"` <br> `UUID` |
| batch_combo_send		| null/obj	| |
| beatId				| str		| "" / "0" |
| biz_source			| str		| "Live" / "live" |
| blind_gift			| null/obj	| |
| broadcast_id			| num		| 0 |
| coin_type				| str		| "gold" / "silver" |
| combo_resources_id	| num		| 1 |
| combo_send			| null/obj	| |
| combo_stay_time		| num		| 3 / 5 |
| combo_total_coin		| num		| |
| crit_prob				| num		| 0 |
| demarcation			| num		| 1 / 2 |
| discount_price		| num		| |
| dmscore				| num		| |
| draw					| num		| 0 |
| effect				| num		| |
| effect_block			| num		| 0 / 1 |
| face					| str		| 发送者 头像URL |
| face_effect_id		| num		| 0 |
| face_effect_type		| num		| 0 |
| face_effect_v2		| obj		| |
| float_sc_resource_id	| num		| 0 |
| giftId				| num		| 礼物ID |
| giftName				| str		| 礼物名称 |
| giftType				| num		| 礼物类型 |
| gift_info				| obj		| |
| gift_tag				| \[\]num	| |
| gold					| num		| 0 |
| group_medal			| null/obj	| |
| guard_level			| num		| [大航海等级](#others) |
| is_first				| bool		| |
| is_join_receiver		| bool		| false |
| is_naming				| bool		| |
| is_special_batch		| num		| 0 |
| magnification			| float		| 0 / 1 |
| medal_info			| obj		| [粉丝勋章](#粉丝勋章medal_info) |
| name_color			| str		| "" |
| num					| num		| 礼物数量 |
| original_gift_name	| str		| "" |
| price					| num		| 礼物价格,RMB×1000 |
| rcost					| num		| ?用户总消费(包括金/银) |
| receive_user_info		| obj		| 接收者(主播)用户信息(旧) |
| receiver_uinfo		| obj		| 接收者(主播)用户信息 [uinfo](#PUBLIC_uinfo) |
| remain				| num		| 包裹剩余数量 |
| rnd					| str		| rnd=tid |
| send_master			| null/?	| |
| sender_uinfo			| obj		| 发送者 用户信息 [uinfo](#PUBLIC_uinfo) |
| silver				| num		| 0 |
| super					| num		| 0 |
| super_batch_gift_num	| num		| |
| super_gift_num		| num		| |
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
#### SEND_GIFT__data__face_effect_v2
| key 2					| type		| value	|
|-|-|-|
| id					| num		| |
| type					| num		| |
#### SEND_GIFT__data__gift_info
| key 2					| type		| value	|
|-|-|-|
| effect_id				| num		| |
| gif					| str		| |
| has_imaged_gift		| num		| |
| img_basic				| str		| |
| webp					| str		| |
#### SEND_GIFT__data__receive_user_info
| key 2					| type		| value	|
|-|-|-|
| uid					| num		| 接收者uid |
| uname					| str		| 接收者昵称 |
#### SEND_GIFT__data__group_medal
| key 3					| type		| value	|
|-|-|-|
| is_lighted			| num		| |
| medal_id				| num		| |
| name					| str		| |
#### SEND_GIFT__ANY__send_master
| key 3					| type		| value	|
|-|-|-|
| room_id				| num		| |
| uid					| num		| |
| uname					| str		| |
```json
{"cmd":"SEND_GIFT_V2","data":{"dmscore":...,"pb":"..."},...}
{
	"cmd":"SEND_GIFT",
	"data":{
		"action":"投喂",
		"bag_gift":null,
		"batch_combo_id":"xxx",
		"batch_combo_send":{
			"action":"投喂",
			"batch_combo_id":"xxx",
			"batch_combo_num":1,
			"blind_gift":null,
			"gift_id":31164,
			"gift_name":"粉丝团灯牌",
			"gift_num":1,
			"send_master":null,
			"uid":xxx,
			"uname":"xxx"
		},
		"beatId":"0",
		"biz_source":"Live",
		"blind_gift":null,
		"broadcast_id":0,
		"coin_type":"silver""gold",
		"combo_resources_id":1,
		"combo_send":null,
		"combo_stay_time":5,
		"combo_total_coin":0,
		"crit_prob":0,
		"demarcation":1,
		"discount_price":0,
		"dmscore":xxx,
		"draw":0,
		"effect":0,
		"effect_block":1,
		"face":"xxx",
		"face_effect_id":0,
		"face_effect_type":0,
		"float_sc_resource_id":0,
		"giftId":1,
		"giftName":"辣条",
		"giftType":5,
		"gift_tag":[],
		"gold":0,
		"group_medal":null,
		"guard_level":0,
		"is_first":true,
		"is_join_receiver":false,
		"is_naming":false,
		"is_special_batch":0,
		"magnification":1,
		"medal_info":{
			"anchor_roomid":0,
			"anchor_uname":"",
			"guard_level":0,
			"icon_id":0,
			"is_lighted":0,
			"medal_color":0,
			"medal_color_border":0,
			"medal_color_end":0,
			"medal_color_start":0,
			"medal_level":0,
			"medal_name":"",
			"special":"",
			"target_id":0
		},
		"name_color":"",
		"num":2,
		"original_gift_name":"",
		"price":100,
		"rcost":xxx,
		"receive_user_info":{"uid":xxx,"uname":"xxx"},
		"receiver_uinfo":{"key":"value"},
		"remain":0,
		"rnd":"xxxxx",
		"send_master":null,
		"sender_uinfo":{"key":"value"},
		"silver":0,
		"super":0,
		"super_batch_gift_num":0,
		"super_gift_num":0,
		"svga_block":0,
		"switch":true,
		"tag_image":"",
		"tid":"xxxxx",
		"timestamp":xxxxxxxxxx,
		"top_list":null,
		"total_coin":xxx,
		"uid":xxx,
		"uname":"xxx",
		"wealth_level":1
	}
}
"batch_combo_id":"batch:gift:combo_id:AAAA:BBBB:CCCC:DDDD.dddd",
```
----
### ONLINE_RANK_V2
[TOP](#直播弹幕)  
文档更新：2024-11-xx  
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
||||
| online_list	| \[7\]obj	| |
| rank_type		| str		| "online_rank" |
#### ONLINE_RANK_V2__data__list
| key 6			| type	| value	|
|-|-|-|
| uid			| num	| uid |
| face			| str	| 头像URL |
| score			| str	| 贡献值 |
| uname			| str	| 昵称 |
| rank			| num	| 排名(1-7) |
| guard_level	| num	| [大航海等级](#others) |
| is_mystery	| bool	| |
| uinfo			| obj	| [uinfo](#PUBLIC_uinfo) |
```json
{
	"cmd": "ONLINE_RANK_V2",
	"data": {
		"online_list": [
			{
				"uid":xxx,
				"face": "xxx",
				"score": "xxx",
				"uname": "xxx",
				"rank":xxx,
				"guard_level":xxx,
				"is_mystery": false,
				"uinfo": {"key": "value"}
			},
			...
		],
		"rank_type": "online_rank"
	}
}
{
	"cmd": "ONLINE_RANK_V2",
	"data": {
		"list": [
			{
				"uid":xxx,
				"face": "xxx",
				"score": "xxx",
				"uname": "xxx",
				"rank":xxx,
				"guard_level":xxx,
				"is_mystery": false,
				"uinfo": {
					"key": "value"
				}
			},
			...
		],
		"rank_type": "gold-rank"
	}
}
```
----
### ONLINE_RANK_V3
[TOP](#直播弹幕)  
文档更新：2025-07-03  
高能用户前七  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_V3" |
| data		| obj	| |
#### ONLINE_RANK_V2__data
| key	| type	| value	|
|-|-|-|
| pb	| base64(protobuf)	| |
```json
{"cmd":"ONLINE_RANK_V3","data":{"pb":"..."}}
```
### ONLINE_RANK_TOP3
[TOP](#直播弹幕)  
文档更新：2024-11-xx  
高能用户前三(左)  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_TOP3" |
| data		| obj	| |
#### ONLINE_RANK_TOP3__data
| key		| type		| value	|
|-|-|-|
| dmscore	| num		| 112 |
| list		| \[1\]obj	| |
#### ONLINE_RANK_TOP3__data__list
| key			| type	| value	|
|-|-|-|
| is_mystery	| bool	| |
| msg			| str	| |
| rank			| num	| 排名(1-3) |
| uid			| num	| |
```json
{
	"cmd": "ONLINE_RANK_TOP3",
	"data": {
		"dmscore": xxx,
		"list": [
			{
				"is_mystery": false,
				"msg": "恭喜 <%xxx%> 成为高能用户",
				"rank": xxx,
				"uid":xxx
			}
		]
	}
}
```
----
### ONLINE_RANK_COUNT
[TOP](#直播弹幕)  
文档更新：2025-05-01  
高能用户人数(观众人数)  
约每5×N秒发送一次  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ONLINE_RANK_COUNT" |
| data		| obj	| |
#### ONLINE_RANK_COUNT__data
| key		| type	| value	|
|-|-|-|
| count				| num	| 最大值约为9999[1-100xx] |
| count_text		| str	| |
| online_count		| num	| 最大值约为9999 |
| online_count_text	| str	| |
```json
// {"cmd":"ONLINE_RANK_COUNT","data":{"count":10000,"count_text":"1万+"}}
// {"cmd":"ONLINE_RANK_COUNT","data":{"count":10001,"count_text":"1万+","online_count":415011,"online_count_text":"41万+"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":0,"count_text":"0","online_count":0,"online_count_text":"0"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":999,"count_text":"999+","online_count":999,"online_count_text":"999+"}}
{"cmd":"ONLINE_RANK_COUNT","data":{"count":9999,"count_text":"9999+","online_count":9999,"online_count_text":"9999+"}}
```
----
### INTERACT_WORD
[TOP](#直播弹幕)  
文档更新：2025-08-01  
进入直播间、关注主播通知（高精度）500ms  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_WORD" |
| data		| obj	| |
#### INTERACT_WORD__data
| key 23			| type		| value	|
|-|-|-|
| contribution		| obj		| |
| contribution_v2	| obj		| |
| control_info		| obj		| |
| core_user_type	| num		| ?大部分为0 \[0-5\] |
| dmscore			| num		| |
| fans_medal		| null/obj	| [粉丝勋章](#粉丝勋章medal_info) |
| group_medal		| null/?	| |
| identities		| \[+\]num	| [identities](#others) |
| is_mystery		| bool		| |
| is_spread			| num		| 流量包推广 0 / 1 |
| msg_type			| num		| |
| privilege_type	| num		| [privilege_type](#others) is_spread==1:`0` |
| relation_tail		| obj		| |
| roomid			| num		| 长_短直播间ID |
| score				| num		| TimeStamp(毫秒 ms 13) |
| spread_desc		| str		| is_spread==1:"流量包推广" |
| spread_info		| str		| is_spread==1:"#FF649E" |
| tail_icon			| num		| |
| tail_text			| str		| "" |
| timestamp			| num		| TimeStamp(秒 s 10) |
| trigger_time		| num		| TimeStamp(纳秒 ns 19) |
| uid				| num		| 用户uid |
| uinfo				| obj		| 用户信息 [uinfo](#PUBLIC_uinfo) |
| uname				| str		| 用户昵称 |
| uname_color		| str		| "" |
#### INTERACT_WORD__data__contribution
| key 				| type		| value	|
|-|-|-|
| grade				| num		| |
#### INTERACT_WORD__data__contribution_v2
| key 				| type		| value	|
|-|-|-|
| grade				| num		| |
| rank_type			| str		| |
| text				| str		| |
#### INTERACT_WORD__data__control_info
| key 				| type		| value	|
|-|-|-|
| text				| str		| |
| text_color		| str		| |
| type				| num		| |
#### INTERACT_WORD__data__relation_tail
| key 				| type		| value	|
|-|-|-|
| tail_guide_text	| str		| |
| tail_icon			| str		| |
| tail_type			| num		| |
#### INTERACT_WORD__msg_type
|msg_type|desc|
|-|-|
|1|进入直播间
|2|关注
|3|分享
|4|特别关注
|5|互粉
|6|Link
```json
{
	"cmd":"INTERACT_WORD",
	"data":{
		"contribution":{"grade":0},
		"contribution_v2":{"grade":0,"rank_type":"","text":""},
		"control_info":{"text":"","text_color":"","type":0},
		"core_user_type":0,
		"dmscore":xx,
		"fans_medal":null,
		"group_medal":null,
		"identities":[1],
		"is_mystery":false,
		"is_spread":0,
		"msg_type":1,
		"privilege_type":0,
		"relation_tail":{"tail_guide_text":"","tail_icon":"","tail_type":0},
		"roomid":xxx,
		"score":xxxxxxxxxxxxx,
		"spread_desc":"",
		"spread_info":"",
		"tail_icon":0,
		"tail_text":"",
		"timestamp":xxxxxxxxxx,
		"trigger_time":xxxxxxxxxxxxxxxxxxx,
		"uid":xxx,
		"uinfo":{"key":"value"},
		"uname":"xxx",
		"uname_color":""
	}
}
"contribution_v2":[
	{"grade":xxx,"rank_type":"","text":""},
	{"grade":xxx,"rank_type":"daily_rank","text":"日榜前3用户"},
	{"grade":xxx,"rank_type":"monthly_rank","text":"月榜前3用户"},
	{"grade":xxx,"rank_type":"weekly_rank","text":"周榜前3用户"}
]
```
----
### INTERACT_WORD_V2
[TOP](#直播弹幕)  
文档更新：2025-07-01  
进入直播间、关注主播通知  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "INTERACT_WORD_V2" |
| data		| obj	| |
#### INTERACT_WORD__data
| key		| type	| value	|
|-|-|-|
| dmscore	| num	| |
| pb		| base64(protobuf)	| |
```json
{"cmd":"INTERACT_WORD_V2","data":{"dmscore":...,"pb":"xxx"}}
```
----
### WATCHED_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
`max(每5秒, 用户进入直播间)`发送一次  
用户(包括游客、主播)进入直播间时发送  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WATCHED_CHANGE" |
| data		| obj	| |
#### WATCHED_CHANGE__data
| key 3			| type	| value	|
|-|-|-|
| num			| num	| 人数 |
| text_small	| str	| "num" / "x.y万" |
| text_large	| str	| "num人看过" / "x.y万人看过" |
```json
{"cmd":"WATCHED_CHANGE","data":{"num":0,"text_small":"0","text_large":"0人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num":9999,"text_small":"9999","text_large":"9999人看过"}}
{"cmd":"WATCHED_CHANGE","data":{"num":10001,"text_small":"1.0万","text_large":"1.0万人看过"}}
```
----
### ROOM_REAL_TIME_MESSAGE_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
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
| fans_club		| num	| 粉丝团成员(点亮粉丝牌人数) |
```json
{"cmd":"ROOM_REAL_TIME_MESSAGE_UPDATE","data":{"roomid":xxx,"fans":xxx,"red_notice":-1,"fans_club":9999}}
```
----
### LIKE_INFO_V3_CLICK
[TOP](#直播弹幕)  
文档更新：2025-04-01  
点赞，实时&每5秒最多发送一次  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIKE_INFO_V3_CLICK" |
| data		| obj	| |
#### LIKE_INFO_V3_CLICK__data
| key 14			| type		| value	|
|-|-|-|
| contribution_info	| obj		| |
| dmscore			| num		| |
| fans_medal		| obj		| [fans_medal](#粉丝勋章medal_info) |
| group_medal		| null/obj	| |
| identities		| \[+\]num	| [identities](#others) |
| is_mystery		| bool		| |
| like_icon			| str		| |
| like_text			| str		| "为主播点赞了" |
| msg_type			| num		| 6 |
| show_area			| num		| 0 / 1(30s) |
| uid				| num		| uid |
| uinfo				| null/obj	| [uinfo](#PUBLIC_uinfo) |
| uname				| str		| 昵称 |
| uname_color		| str		| "" |
```json
{
	"cmd":"LIKE_INFO_V3_CLICK",
	"data":{
		"contribution_info":{"grade":0},
		"dmscore":xxx,
		"fans_medal":{"key":"value"},
		"group_medal":null,
		"identities":[3,1],
		"is_mystery":false,
		"like_icon":"https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png",
		"like_text":"为主播点赞了",
		"msg_type":6,
		"show_area":0,
		"uid":xxx,
		"uinfo":{"key":"value"},
		"uname":"xxx",
		"uname_color":""
	}
}
```
----
### LIKE_INFO_V3_UPDATE
[TOP](#直播弹幕)  
文档更新：2025-04-01  
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
文档更新：2024-xx-xx  
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
| random_delay_req_v2	| \[2\]obj	| |
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
文档更新：2024-05-01  
`ENTRY_EFFECT` 欢迎大航海成员进入直播间，高精度  
`ENTRY_EFFECT_MUST_RECEIVE` 欢迎???进入直播间，高精度  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ENTRY_EFFECT" "ENTRY_EFFECT_MUST_RECEIVE" |
| data		| obj	| |
#### ENTRY_EFFECT__data
| key 33					| type		| value	|
|-|-|-|
| id						| num		| |
| uid						| num		| 用户uid |
| target_id					| num		| 主播uid |
| mock_effect				| num		| |
| face						| str		| 头像URL |
| privilege_type			| num		| [privilege_type](#others) |
| copy_writing				| str		| |限长7字符，省略号为`...`
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
| copy_writing_v2			| str		| |限长6字符，省略号为`…`
| icon_list					| \[+\]num	| |
| max_delay_time			| num		| 7 |
| trigger_time				| num		| ?TimeStamp(ns?) |
| identities				| num		| [identities](#others) |
| effect_silent_time		| float		| 0 |
| effective_time_new		| num		| |
| web_dynamic_url_webp		| str		| |
| web_dynamic_url_apng		| str		| |
| mobile_dynamic_url_webp	| str		| |
| wealthy_info				| null/obj	| |
| new_style					| num		| |
| is_mystery				| bool		| |
| uinfo						| obj		| [uinfo](#PUBLIC_uinfo) |
| full_cartoon_id			| num		| |
| priority_level			| num		| |
| wealth_style_info			| obj		| |
```json
{
	"cmd":"ENTRY_EFFECT",
	"data":{
		"id":12345,
		"uid":12345,
		"target_id":12345,
		"mock_effect":12345,
		"face":"xxx",
		"privilege_type":0,
		"copy_writing":"<%xxx%> 来了",
		"copy_color":"#000000",
		"highlight_color":"#FFF100",
		"priority":12345,
		"basemap_url":"xxx",
		"show_avatar":1,
		"effective_time":2,
		"web_basemap_url":"xxx",
		"web_effective_time":2,
		"web_effect_close":0,
		"web_close_time":900,
		"business":3,
		"copy_writing_v2":"<%xxx%> 来了",
		"icon_list":[],
		"max_delay_time":7,
		"trigger_time":xxx,
		"identities":1,
		"effect_silent_time":0,
		"effective_time_new":0,
		"web_dynamic_url_webp":"",
		"web_dynamic_url_apng":"",
		"mobile_dynamic_url_webp":"",
		"wealthy_info":null,
		"new_style":0,
		"is_mystery":false,
		"uinfo":{},
		"full_cartoon_id":0,
		"priority_level":0,
		"wealth_style_info":{"url":"https://i0.hdslb.com/bfs/live/47ca74b4068ee8ffaee37b3bf3b9590d7ffcb303.png"}
	}
}
```
```python
# copy_writing
USERNAME = [
	"1234567",
	"1234567...",
]
f"<%{USERNAME}%>进入直播间"
f"欢迎 <%{USERNAME}%> 进入直播间"
f"欢迎{anchor_name} <%{USERNAME}%> 进入直播间"
f"<%{USERNAME}%> 来了"
# copy_writing_v2
USERNAME = [
	"123456",
	"123456…",
]
f"<%{USERNAME}%>进入直播间"
f"欢迎 <%{USERNAME}%> 进入直播间"
f"欢迎{anchor_name} <%{USERNAME}%> 进入直播间"
f"欢迎 <^icon^> <%{USERNAME}%> 进入直播间"
f"欢迎 <^icon^> {anchor_name} <%{USERNAME}%> 进入直播间"
f"<%{USERNAME}%> 来了"
```
----
### STOP_LIVE_ROOM_LIST
[TOP](#直播弹幕)  
文档更新：2025-04-01  
每30秒发送一次(`HH:mm:29`,`HH:mm:59`)  
广播 未压缩
| key			| type		| value	|
|-|-|-|
| cmd			| str		| "STOP_LIVE_ROOM_LIST" |
| data			| obj		| |
#### STOP_LIVE_ROOM_LIST__data
| key			| type		| value	|
|-|-|-|
| room_id_list	| \[+\]num	| |
```json
{"cmd":"STOP_LIVE_ROOM_LIST","data":{"room_id_list":[1,2,3,4,5,6,7,8,9]}}
```
----
### GUARD_BUY
[TOP](#直播弹幕)  
文档更新：2024-04-12  
大航海购买  
**推荐使用 [USER_TOAST_MSG_V2]()**  
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
| price			| num	| 舰长:198000 / 提督:1998000 / 总督:19998000 |
| gift_id		| num	| 舰长:10003 / 提督:10002 / 总督:10001 |
| gift_name		| str	| |
| start_time	| num	| 购买时间 TimeStamp(秒) |
| end_time		| num	| 购买时间 TimeStamp(秒) |
```json
{"cmd":"GUARD_BUY","data":{"uid":xxx,"username":"xxx","guard_level":1,"num":xxx,"price":19998000,"gift_id":10001,"gift_name":"总督","start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx}}
{"cmd":"GUARD_BUY","data":{"uid":xxx,"username":"xxx","guard_level":2,"num":xxx,"price":1998000, "gift_id":10002,"gift_name":"提督","start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx}}
{"cmd":"GUARD_BUY","data":{"uid":xxx,"username":"xxx","guard_level":3,"num":xxx,"price":198000,  "gift_id":10003,"gift_name":"舰长","start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx}}
```
----
### USER_TOAST_MSG
[TOP](#直播弹幕)  
文档更新：2024-11-xx  
大航海购买通知，显示在聊天区  
**推荐使用 [USER_TOAST_MSG_V2]()**  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG__data
| key 28				| type	| value	|
|-|-|-|
| anchor_show			| bool	| true |
| color					| str	| 舰长:"#00D1F1" / 提督:"#E17AFF" / 总督:"#FF7C28" |
| dmscore				| num	| 舰长=90,提督=96,总督=102 <br>OR<br> 舰长=102,提督=108,总督=z |
| effect_id				| num	| |
| end_time				| num	| TimeStamp(秒) |
| face_effect_id		| num	| |
| gift_id				| num	| 舰长:10003 / 提督:10002 / 总督:10001 |
| group_name			| str	| |
| group_op_type			| num	| |
| group_role_name		| str	| |
| guard_level			| num	| [guard_level](#others) |
| is_group				| num	| 0 |
| is_show				| num	| 0 |
| num					| num	| 购买数量 |
| op_type				| num	| 1: 开通大航海广播 / 2: 续费大航海广播 |
| payflow_id			| str	| 订单号(25)(YYMMDD HHmmss xxxxxxxxxxxxx) |
| price					| num	| 舰长138 158 168 198 / 提督1598 1998 / 总督15998 19998 |
| role_name				| str	| "舰长" / "提督" / "总督" |
| room_effect_id		| num	| |
| room_gift_effect_id	| num	| |
| room_group_effect_id	| num	| |
| source				| num	| |
| start_time			| num	| 购买时间 TimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播当前大航海成员数 |
| toast_msg				| str	|`f"<%xxx%> 在主播{xxx}的直播间(开通\|续费)了(\d+个月)?(舰长\|提督\|总督)，今天是TA陪伴主播的第{num}天"` |
| uid					| num	| uid |
| unit					| str	| "月" / "天" |
| user_show				| bool	| true |
| username				| str	| 昵称 |
```json
{
	"cmd":"USER_TOAST_MSG",
	"data":{
		"anchor_show":true,
		"color":"#xxx",
		"dmscore":xxx,
		"effect_id":xxx,
		"end_time":xxxxxxxxx,
		"face_effect_id":xxx,
		"gift_id":xxx,
		"group_name":"",
		"group_op_type":0,
		"group_role_name":"",
		"guard_level":xxx,
		"is_group":0,
		"is_show":0,
		"num":xxx,
		"op_type":,
		"payflow_id":"xxxxxxxxxxxxxxxxxxxxxxxxx",
		"price":xxx,
		"role_name":"xxx",
		"room_effect_id":xxx,
		"room_group_effect_id":xxx,
		"start_time":xxxxxxxxx,
		"svga_block":0,
		"target_guard_count":xxx,
		"toast_msg":"<%xxx%> 在主播xxx的直播间xxx了xxx，今天是TA陪伴主播的第xxx天",
		"uid":xxx,
		"unit":"月",
		"user_show":true,
		"username":"xxx"
	}
}
"<%xxx%>续费了舰长1*5天"
```
----
### NOTICE_MSG
[TOP](#直播弹幕)  
文档更新：2024-11-xx  
滚动横幅  
| key 17,18		| type	| value	|
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
| business_id	| str	| xxx |
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
{
	"cmd":"NOTICE_MSG",
	"id":xxx,"name":"舰长1个月",
	"full":{"head_icon":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","tail_icon":"","head_icon_fa":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","tail_icon_fa":"","head_icon_fan":1,"tail_icon_fan":0,"background":"#FFE2B2","color":"#B87436","highlight":"#E37921","time":10},
	"half":{"head_icon":"","tail_icon":"","background":"","color":"","highlight":"","time":0},
	"side":{"head_icon":"https://i0.hdslb.com/bfs/live/82665c9d263c8673f3f934e23d09c1d0f6bc8f50.png","background":"#FFE9C8FF","color":"#EF903AFF","highlight":"#D54900FF","border":"#FFCFA4FF"},
	"roomid":xxx,"real_roomid":12345,
	"msg_common":"","msg_self":"<%xxx%> 在主播 <%xxx%>的直播间续费了舰长，感谢上船陪伴",
	"link_url":"",
	"msg_type":4,"shield_uid":-1,"business_id":"xuser-guard",
	"scatter":{"min":0,"max":0},"marquee_id":"","notice_type":0
}
```
----
### SUPER_CHAT_MESSAGE
[TOP](#直播弹幕)  
文档更新：2024-04-22  
**醒目留言 SuperChat**
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_MESSAGE" |
| data		| obj	| |
| roomid	| num	| 长_短直播间ID |
#### SUPER_CHAT_MESSAGE__data
| key 30					| type		| value	| 备注
|-|-|-|-|
| background_bottom_color	| str		| [table](#SC价格颜色表) |
| background_color			| str		| [table](#SC价格颜色表) |
| background_color_end		| str		| [table](#SC价格颜色表) |
| background_color_start	| str		| [table](#SC价格颜色表) |
| background_icon			| str		| URL / "" |
| background_image			| str		| URL / "" |
| background_price_color	| str		| [table](#SC价格颜色表) |
| color_point				| float		| 0.7 / 0.9 |
| dmscore					| num		| |
| end_time					| num		| TimeStamp(秒) |
| gift						| obj		| |
| group_medal				| obj		| |
| id						| num		| SC id |
| is_mystery				| bool		| |
| is_ranked					| num		| 0 / 1 |
| is_send_audit				| num		| 0 / 1 |
| medal_info				| null/obj	| [medal_info](#粉丝勋章medal_info):medal_color为`#rrggbb` |
| message					| str		| SC 内容 |
| message_font_color		| str		| |
| message_trans				| str		| SC 日本語 翻译(百度翻译) |与`trans_mark`无关，即`trans_mark`为`0`也有可能有内容
| price						| num		| 价格(CNY) |
| rate						| num		| 1000 |
| start_time				| num		| TimeStamp(秒) |
| time						| num		| SC剩余时长(秒) |
| token						| str		| hex(64bit) |
| trans_mark				| num		| 是否翻译 |
| ts						| num		| TimeStamp(秒) |
| uid						| num		| uid |
| uinfo						| obj		| [uinfo](#PUBLIC_uinfo) |
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
| is_main_vip				| num		| 0 / 1 |
| is_svip					| num		| ?0 |
| is_vip					| num		| ?0 |
| level_color				| str		| #rrggbb |
| manager					| num		| 管理员 |
| name_color				| str		| #RRGGBB |
| title						| str		| [头衔](docs/头衔.md) |
| uname						| str		| 昵称 |
| user_level				| num		| 直播观众等级UL |
#### SUPER_CHAT_MESSAGE__json
```json
{
	"cmd":"SUPER_CHAT_MESSAGE",
	"data":{
		"background_bottom_color":"#xxx",
		"background_color":"#xxx",
		"background_color_end":"#xxx",
		"background_color_start":"#xxx",
		"background_icon":"",
		"background_image":"",
		"background_price_color":"#xxx",
		"color_point":0.7,
		"dmscore":xxx,
		"end_time":xxx,
		"gift":{"gift_id":12000,"gift_name":"醒目留言","num":1},
		"group_medal":{"is_lighted":0,"medal_id":0,"name":""},
		"id":xxx,
		"is_mystery":false,
		"is_ranked":0,
		"is_send_audit":1,
		"medal_info":{"key":"value"},
		"message":"xxx",
		"message_font_color":"#A3F6FF",
		"message_trans":"",
		"price":xxx,
		"rate":1000,
		"start_time":xxx,
		"time":xxx,
		"token":"FFFFFFFF",
		"trans_mark":0,
		"ts":xxx,
		"uid":xxx,
		"uinfo":{"key":"value"},
		"user_info":{"key":"value"}
	}
}
```
### SC价格颜色表
| price | background_bottom_color	| background_color	| background_color_end	| background_color_start	| background_price_color	| message_font_color	|
|-|-|-|-|-|-|-|
| 30+	| #2A60B2 | #EDF5FF | #405D85 | #3171D2 | #7497CD | #A3F6FF |
| 50+	| #427D9E | #DBFFFD | #29718B | #4EA4C5 | #7DA4BD | #A3F6FF |
| 100+	| #E2B52B | #FFF1C5 | #EEBE5C | #EAB400 | #ECCF75 | #72110E |
| 500+	| #E09443 | #FFEAD2 | #DB9039 | #FFA850 | #E8AF79 | #72110E |
| 1000+	| #E54D4D | #FFE7E4 | #BD666A | #F63C45 | #EE8B8B | #FFE163 |
| 2000+	| #AB1A32 | #FFD8D8 | #8B0F3D | #600012 | #C86A7A | #FFE163 |
----
### SUPER_CHAT_MESSAGE_JPN
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
SuperChat 日本語 Japanese  
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
| is_ranked					| num	| 0 / 1 |
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
{"cmd":"SUPER_CHAT_MESSAGE_JPN","data":{"id":"12345","uid":"12345","price":50,"rate":xxx,"message":"123","message_jpn":"123","is_ranked":1,"background_image":"https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_color":"#DBFFFD","background_icon":"","background_price_color":"#7DA4BD","background_bottom_color":"#427D9E","ts":xxxxxxxxxx,"token":"FFFFFFFF","medal_info":null,"user_info":{"key":"value"},"time":120,"start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx,"gift":{"num":1,"gift_id":12000,"gift_name":"醒目留言"}},"roomid":"12345"}
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
| ids		| \[+\]num	| SC_id |
| roomid	| num		| 长_短直播间ID |
```json
{"cmd":"SUPER_CHAT_MESSAGE_DELETE","data":{"ids":[123]},"roomid":12345}
```
----
### DANMU_AGGREGATION
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
抽奖通知 每秒最多更新一次 每个抽奖最多发送`max_time-1`个包  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "DANMU_AGGREGATION" |
| data	| obj	| |
#### DANMU_AGGREGATION__data
| key 11				| type	| value	|
|-|-|-|
| activity_identity		| str	| 抽奖id |
| activity_source		| num	| 1:天选时刻 / 2:礼物红包 |
| aggregation_cycle		| num	| 1 |
| aggregation_icon		| str	| (URL) |
| aggregation_num		| num	| 抽奖人数显示，最大999 |
| broadcast_msg_type	| num	| 0 |
| ~~dmscore~~			| num	| 144 |
| msg					| str	| 抽奖口令 |
| show_rows				| num	| 1 |
| show_time				| num	| 2 |
| timestamp				| num	| 当前时间TimeStamp(秒) |
```json
{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":1,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png","aggregation_num":999,"broadcast_msg_type":0,"msg":"xxx","show_rows":1,"show_time":2,"timestamp":xxxxxxxxxx}}

{"cmd":"DANMU_AGGREGATION","data":{"activity_identity":"12345","activity_source":2,"aggregation_cycle":1,"aggregation_icon":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png","aggregation_num":999,"broadcast_msg_type":0,"msg":"xxx","show_rows":1,"show_time":2,"timestamp":xxxxxxxxxx}}
["老板大气！点点红包抽礼物","点点红包，关注主播抽礼物～","喜欢主播加关注，点点红包抽礼物","红包抽礼物，开启今日好运！","中奖喷雾！中奖喷雾！"]

{"aggregation_icon":{"天选时刻":"https://i0.hdslb.com/bfs/live/c8fbaa863bf9099c26b491d06f9efe0c20777721.png", "礼物红包":"https://i0.hdslb.com/bfs/live/024f7473753c7cc993413e05c69e8b960086e68f.png"}}
```
----
### SPECIAL_GIFT
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "SPECIAL_GIFT" |
| data	| obj	| |
#### SPECIAL_GIFT__data
| key	| type	| value	|
|-|-|-|
| 39	| obj	| |
#### SPECIAL_GIFT__data__39
| key 2,7	| type		| value	|
|-|-|-|
| action	| str		| "start" / "end" |
| content	| str		| |
| hadJoin	| num		| 0 |
| id		| str/num	| |
| num		| num		| 1 |
| storm_gif	| str		| GIF图像 |
| time		| num		| 持续时间 |
```json
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"可爱即正义~~","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"前方高能预警，注意这不是演习","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"start","content":"这个直播间已经被我们承包了！","hadJoin":0,"id":"123412341234","num":1,"storm_gif":"http://static.hdslb.com/live-static/live-room/images/gift-section/mobilegift/2/jiezou.gif?2017011901","time":90}}}
{"cmd":"SPECIAL_GIFT","data":{"39":{"action":"end","id":123412341234}}}
```
----
### GUARD_HONOR_THOUSAND
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "GUARD_HONOR_THOUSAND" |
| data	| obj	| |
#### GUARD_HONOR_THOUSAND__data
| key	| type		| value	|
|-|-|-|
| add	| \[+\]num	| 用户uid	|
| del	| \[+\]num	| 用户uid	|
```json
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[],"del":[9999]}}
{"cmd":"GUARD_HONOR_THOUSAND","data":{"add":[9999],"del":[]}}
```
----
### ANCHOR_LOT_CHECKSTATUS
[TOP](#直播弹幕)  
文档更新：2025-03-xx  
抽奖(天选时刻)检查  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_CHECKSTATUS" |
| data		| obj	| |
#### ANCHOR_LOT_CHECKSTATUS__data
| key 3,6				| type	| value	|
|-|-|-|
| ?award_name_reject	| str	| |
| id					| num	| 抽奖id	|
| ?reject_danmu			| null	| ?null	|
| ?reject_reason		| str	| 拒绝理由	|
| status				| num	| 4:通过 / 5:拒绝	|
| uid					| num	| 主播uid	|
```json
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"reject_danmu":null,"reject_reason":"由于奖品格式不合格,请仔细检查后再提交哦","status":5,"uid":12345}}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"award_name_reject":"","id":12345,"reject_danmu":null,"reject_reason":"","status":4,"uid":123}}
{"cmd":"ANCHOR_LOT_CHECKSTATUS","data":{"id":123,"status":4,"uid":12345}}
```
----
### ANCHOR_LOT_START
[TOP](#直播弹幕)  
文档更新：2025-01-01  
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
| award_type		| num		| 0 / 1 |
| ?award_price_text	| str		| "价值xxx电池" |
| break_up_time		| num		| 0 |
| cur_gift_num		| num		| 0 |
| current_time		| num		| 当前时间TimeStamp(秒) |
| danmu				| str		| 弹幕口令\[0,15\] |
| danmu_new			| \[1\]obj	| |
| danmu_type		| num		| `danmu_type:0 === this.danmuType ? "文案弹幕" :"表情弹幕"` |
| gift_id			| num		| 0 |
| gift_name			| str		| ~~礼物抽奖: 抽奖条件~~ |
| gift_num			| num		| 礼物抽奖: 数量 |
| gift_price		| num		| 礼物抽奖: 礼物价格(RMB×1000) |
| goaway_time		| num		| ?180 |
| goods_id			| num		| |
| id				| num		| 抽奖id |
| is_broadcast		| num		| 1 |
| join_type			| num		| 0 / 1 |
| lot_status		| num		| [lot_status](#others) \[0,1,2\] |
| max_time			| num		| 开奖时间(60,300,600,900)秒 |
| require_text		| str		| "关注主播" / "至少成为主播的舰长/提督/总督" |
| require_type		| num		| 抽奖条件 1:礼物抽奖 / 2:粉丝勋章 / 3:大航海 / ~~4:UL?~~ |
| require_value		| num		| \[0,1\] 关注状态 / \[1,20\] 粉丝勋章等级 / \[1,3\] [大航海等级](#others) |
| room_id			| num		| 长直播间ID |
| send_gift_ensure	| num		| 0 |
| show_panel		| num		| 1 |
| start_dont_popup	| num		| 0 |
| status			| num		| 1 |
| time				| num		| 剩余时间(秒) |
| url				| str		| URL |
| web_url			| str		| URL |
#### ANCHOR_LOT_START__data__danmu_new
| key 3			| type	| value	|
|-|-|-|
| danmu			| str	| 弹幕口令\[0,15\] |
| danmu_view	| str	| |
| reject		| bool	| |
```json
{
	"cmd":"ANCHOR_LOT_START",
	"data":{
		"asset_icon":"https://i0.hdslb.com/bfs/live/cde7d1a68c0d10c6aa283c4c24b968578fa45d75.png",
		"asset_icon_webp":"https://i0.hdslb.com/bfs/live/19b8a1b80f71af777ec615b329549224941b7b6c.webp",
		"award_image":"http://i0.hdslb.com/bfs/live/xxx.xxx","award_name":"xxx","award_num":1,"award_type":0,
		"break_up_time":0,"cur_gift_num":0,"current_time":xxx,
		"danmu":"名至实归，强烈推荐","danmu_new":[{"danmu":"名至实归，强烈推荐","danmu_view":"","reject":false}],"danmu_type":0,
		"gift_id":0,"gift_name":"","gift_num":1,"gift_price":0,
		"goaway_time":180,"goods_id":-99998,"id":xxx,"is_broadcast":1,"join_type":0,"lot_status":0,"max_time":xxx,
		"require_text":"关注主播","require_type":1,"require_value":0,
		"room_id":xxx,"send_gift_ensure":0,"show_panel":1,"start_dont_popup":0,"status":1,"time":xxx,
		"url":"xxx",
		"web_url":"https://live.xxx.com/p/html/live-lottery/anchor-join.html"
	}
}
```
----
### ANCHOR_LOT_END
[TOP](#直播弹幕)  
文档更新：2024-11-01  
抽奖(天选时刻)结束  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_END" |
| data		| obj	| |
#### ANCHOR_LOT_END__data
| key		| type	| value	|
|-|-|-|
| id		| num	| 抽奖id |
```json
{"cmd":"ANCHOR_LOT_END","data":{"id":xxx}}
```
----
### ANCHOR_LOT_AWARD
[TOP](#直播弹幕)  
文档更新：2025-01-01  
抽奖(天选时刻) 中奖名单  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_AWARD" |
| data		| obj	| |
#### ANCHOR_LOT_AWARD__data
| key 10			| type	| value	|
|-|-|-|
| award_dont_popup	| num				| 1 |
| award_image		| str				| 奖品图像? |
| award_name		| str				| 奖品名称 |
| award_num			| num				| 1 |
| ?award_price_text	| str				| |
| award_type		| num				| 0 / 1 |
| award_users		| \[award_num\]obj	| 中奖用户 |
| id				| num				| 抽奖id |
| ?ruid				| num				| uid |
| lot_status		| num				| [lot_status](#others) 2 |
| url				| str				| URL |
| web_url			| str				| URL |
#### ANCHOR_LOT_AWARD__data__award_users
| key 8			| type	| value	|
|-|-|-|
| ~~color~~		| num	| 直播观众等级_颜色 num(RGB24) |
| face			| num	| 头像URL |
| is_mystery	| bool	| |
| level			| num	| 直播观众等级UL |
| num			| num	| 数量 |
| uid			| num	| uid |
| uinfo			| obj	| [uinfo](#PUBLIC_uinfo) |
| uname			| num	| 昵称 |
```json
{
	"cmd":"ANCHOR_LOT_AWARD",
	"data":{
		"award_dont_popup":1,
		"award_image":"xxx",
		"award_name":"xxx",
		"award_num":xxx,
		"award_type":0,
		"award_users":[
			{"face":"xxx","level":0,"num":0,"uid":xxx,"uinfo":xxx,"uname":"xxx"}
		],
		"id":xxx,
		"lot_status":2,
		"url":"xxx",
		"web_url":"https://live.xxx.com/p/html/live-lottery/anchor-join.html"
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
		"award_users":[{"bag_id":9999,"color":9999,"face":"xxx","gift_id":31250,"level":9999,"num":1,"uid":9999,"uname":"xxx"}],
		"id":12345,
		"lot_status":2,
		"ruid":9999,
		"url":"https://live.xxx.com/p/html/live-lottery/anchor-join.html?is_live_half_webview=1&hybrid_biz=live-lottery-anchor&hybrid_half_ui=1,5,100p,100p,000000,0,30,0,0,1;2,5,100p,100p,000000,0,30,0,0,1;3,5,100p,100p,000000,0,30,0,0,1;4,5,100p,100p,000000,0,30,0,0,1;5,5,100p,100p,000000,0,30,0,0,1;6,5,100p,100p,000000,0,30,0,0,1;7,5,100p,100p,000000,0,30,0,0,1;8,5,100p,100p,000000,0,30,0,0,1",
		"web_url":"https://live.xxx.com/p/html/live-lottery/anchor-join.html"
	}
}
```
----
### POPULAR_RANK_CHANGED
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULAR_RANK_CHANGED" |
| data		| obj	| |
#### POPULAR_RANK_CHANGED__data
| key			| type	| value	|
|-|-|-|
| uid			| num	| 主播uid |
| rank			| num	| \[0-100\] |
| countdown		| num	| \[0-3600\] |
| timestamp		| num	| 当前时间TimeStamp(秒) |
| cache_key		| str	| `f"rank_change:{hex_256bit}"` |
| on_rank_name_by_type	| str	| |
| rank_name_by_type	| str	| |
| url_by_type	| str	| |
| rank_by_type	| num	| |
| default_url	| str	| |
```json
{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":xxx,"rank":xxx,"countdown":xxx,"timestamp":xxxxxxxxxx,"cache_key":"rank_change:ffffffffffffffffffffffffffffffff"}}
{"cmd":"POPULAR_RANK_CHANGED","data":{"uid":xxx,"rank":xxx,"countdown":xxx,"timestamp":xxxxxxxxxx,"cache_key":"rank_change:ffffffffffffffffffffffffffffffff","on_rank_name_by_type":"xxx","rank_name_by_type":"人气榜","url_by_type":"xxx","rank_by_type":xxx,"default_url":"xxx"}}
```
----
### PREPARING
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
结束直播  
| key 4		| type	| value	|
|-|-|-|
| cmd		| str	| "PREPARING" |
| ?round	| num	| 1:下播后轮播稿件 |
| roomid	| str	| 长_短直播间ID |
| ?scatter	| obj	| |
```json
{"roomid":"xxx","scatter":{"min":10,"max":30},"round":1,"cmd":"PREPARING"}
{"roomid":"xxx","round":1,"cmd":"PREPARING"}
{"roomid":"xxx","cmd":"PREPARING"}
{"cmd":"PREPARING","roomid":"xxx","round":1,"scatter":{"max":30,"min":10}}
{"cmd":"PREPARING","roomid":"xxx","round":1}
{"cmd":"PREPARING","roomid":"xxx","scatter":{"max":30,"min":10}}
{"cmd":"PREPARING","roomid":"xxx"}
```
----
### DANMU_MSG
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
弹幕！  
每`n`秒广播一次，每次最多`n×20`个  
| key 3,6		| type	| value	|
|-|-|-|
| cmd			| str	| "DANMU_MSG" / "DANMU_MSG:3:7:1:1:1:1" / "DANMU_MSG:4:0:2:2:2:0" |
| info			| array	| |
| dm_v2			| str	| base64(protobuf) UTF-8 |
#### DANMU_MSG__info
| array	| type		| value	| 备注	|
|-|-|-|-|
| 0		| array		| [弹幕属性](#DANMU_MSG__info__0) |
| 1		| str		| `text/content` <br> 弹幕内容/表情包名称 | 371111:大家都在说
| 2		| array		| `userInfo`用户主站信息 |
| 3		| array		| `fansMedal`[粉丝勋章](#DANMU_MSG__info__3) |
| 4		| array		| `user_level`[用户直播区信息](#DANMU_MSG__info__4) |
| 5		| array		| `title` [头衔](docs/头衔.md) |
| 6		| num		| 0 |
| 7		| num		| `PrivilegeType`[大航海等级](#others) |
| 8		| null		| |曾经为 obj
| 9		| obj		| [`validation`](#DANMU_MSG__info__9) |
| 10	| num		| 0 |
| 11	| num		| 0 |
| 12	| null		| |
| 13	| null		| |
| 14	| num		| `lpl` |
| 15	| num		| |
| 16	| array		| `Wealth`荣耀等级 |
| 17	| null/array	| `groupMedal` |
#### DANMU_MSG__info__0
弹幕属性  
| array	| type		| value	| 备注	|
|-|-|-|-|
| 0[0]	| num		| 0 |
| 0[1]	| num		| `mode` 弹幕位置 | 0:普通 / 4:底部 / 3000:LPL?
| 0[2]	| num		| `size/fontsize` 弹幕字体大小 | `SendMsgReq.Fontsize` |
| 0[3]	| num		| `color` 弹幕颜色 |
| 0[4]	| num		| `ctime` | TimeStamp(毫秒) `time.Now().Unix()` |
| 0[5]	| num		| `dmid/rnd/danmakuRnd` <br> 抽奖/弹幕互动游戏 为 0 | `var rand int64` <br> WEB:进入直播间时间TimeStamp(秒) <br> iOS/Android:随机 |
| 0[6]	| num		| 0 |
| 0[7]	| str		| `midHash` | HEX:crc32(uid) |
| 0[8]	| num		| 0 |
| 0[9]	| num		| `type/danmakuType` | \[0,1,2,7,9\] 1:节奏风暴 / 2:天选时刻 / 9:弹幕互动游戏
| 0[10]	| num		| `chatBubbleType` | 0 / 1 / 2 / 5 |
| 0[11]	| str		| `chatBubbleColor` | 5:`"#1453BAFF,#4C2263A2,#3353BAFF"` <br> 2:`"#1453BAFF,#4C2263A2,#3353BAFF"` <br> 1:`"#33FFE99E,#40DCA731,#33FFE99E"`
| 0[12]	| num		| `dm_type/dmType/danmakuSpecialType` | 0:文本 <br> 1:表情包 <br> 2:语音
| 0[13]	| obj/str	| 表情包:[`emoticonOptions`](#DANMU_MSG__info__0__13) <br> `"{}"` |
| 0[14]	| obj/str	| 语音:[`voiceConfig`/`voiceInfo`](#DANMU_MSG__info__0__14) <br> `"{}"` |
| 0[15]	| obj 		| [`emoticons/modeInfo`](#DANMU_MSG__info__0__15) |
| 0[16]	| obj 		| `Aggregation/danmakuAggre`[抽奖](#DANMU_MSG__info__0__16) |20230119
| 0[17]	| num 		| `chatBubbleId/idV2` |20230708+
#### DANMU_MSG__info__2
用户主站信息/userInfo  
| array	| type	| desc	| value	|
|-|-|-|-|
| 2[0]	| num	| `uid` | 用户uid
| 2[1]	| str	| `uname/username`昵称 |
| 2[2]	| num	| `isAdmin/RoomAdmin` 房管 | 0 / 1 |
| 2[3]	| num	| `isVip` | 0 / 1 |
| 2[4]	| num	| `isSvip` | 0 / 1 |
| 2[5]	| num	| `rank` | LV0/非正式会员:5000 / 10000 |
| 2[6]	| num	| `verify/MobileVerify`手机号验证 |
| 2[7]	| str	| `usernameColor` | 舰长:`"#00D1F1"` <br> 提督:`"#E17AFF"` <br> 总督:`"#FF7C28"`
#### DANMU_MSG__info__3
粉丝勋章/fansMedal  
| array	| type	| value	|
|-|-|-|
| 3[0]	| num	| `level` 粉丝勋章 等级 |
| 3[1]	| str	| `label` 粉丝勋章 称号 |
| 3[2]	| num	| `anchorUsername` 主播名称 |
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
用户直播区信息/userLevel/user_level  
| array	| type		| value	|
|-|-|-|
| 4[0]	| num		| `userLevel` 用户UL等级 |
| 4[1]	| num		| 0 |
| 4[2]	| num		| UL等级 颜色 |
| 4[3]	| str/num	| `rank` 用户直播排名 `">50000"` / 当前排名 |
| 4[4]	| num		| `online_rank` \[0,1,2,3\] 高能榜实时排名(仅前三) |
#### DANMU_MSG__info__5
头衔/title  
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
validation  
| key	| type	| value	|
|-|-|-|
| ts	| num	| TimeStamp(秒) |
| ct	| str	| hex(64bit) |
#### DANMU_MSG__info__16
Wealth  
| array	| type	| value	|
|-|-|-|
| 16[0]	| num	| `wealth level`荣耀等级 |
#### DANMU_MSG__info__16
groupMedal  
| array	| type	| value	|
|-|-|-|
| 17[0]	| num	| medal_id |
| 17[1]	| str	| name |
| 17[2]	| num	| is_lighted |
#### DANMU_MSG__info__0__13
表情包1  
| key 7				| type	| value	|
|-|-|-|
| bulge_display		| num	| 0 / 1 |
| emoticon_unique	| str	| 表情包id |
| height			| num	| 高 px |
| in_player_area	| num	| 0 / 1 |
| is_dynamic		| num	| 0 / 1 |
| url				| str	| 表情包URL(有可能http) |
| width				| num	| 宽 px |
#### DANMU_MSG__info__0__14
voiceConfig  
| key				| type	| value	|
|-|-|-|
| file_duration		| num	| |
| file_format		| str	| |
| file_id			| str	| |
| text				| str	| |
| voice_url			| str	| |
#### DANMU_MSG__info__0__15
| key 3				| type	| value	|
|-|-|-|
| extra				| str	| [json](#DANMU_MSG__info__0_15__extra) |
| mode				| num	| 0 / 3000:LPL |
| show_player_type	| num	| 0 |
| user				| obj	| [uinfo](#PUBLIC_uinfo) |
#### DANMU_MSG__info__0__15__extra
| key 37					| type		| value	| 备注	|
|-|-|-|-|
| send_from_me				| bool		| false |
| master_player_hidden		| bool		| false |
| mode						| num		| 0 |
| color						| num		| 弹幕颜色 |
| dm_type					| num		| 0:文本 / 1:表情包 |
| font_size					| num		| 弹幕字体大小 | 25
| player_mode				| num		| 弹幕位置 | 0:xxx / 1:滚动 / 2:xxx / 4:底部
| show_player_type			| num		| 0 |
| content					| str		| 弹幕内容/表情包名称 |
| user_hash					| str		| `str(DEC:midHash)` |
| emoticon_unique			| str		| 表情ID |
| bulge_display				| num		| 0:官方表情包 / 1:房间表情包 |
| recommend_score			| num		| ?弹幕推荐等级/智能屏蔽等级 | 抽奖:0
| main_state_dm_color		| str		| "" |
| objective_state_dm_color	| str		| "" |
| direction					| num		| 0 / 1 / 2 |
| pk_direction				| num		| 0 / 1 / 2 |
| quartet_direction			| num		| 0 |
| anniversary_crowd			| num		| 0 |202206-
| yeah_space_type			| str		| "" |
| yeah_space_url			| str		| "" |
| jump_to_url				| str		| "" |
| space_type				| str		| "" |
| space_url					| str		| "" |
| animation					| obj		| |202206-
| emots						| obj/null	| 新的表情包 k:v{obj...} |202206-
| is_audited				| bool		| false | 20230217
| id_str					| str		| hex | 20230308
| icon						| obj/null	| [荣耀装扮](https://link.xxx.com/p/eden/news#/newsdetail?id=3531 ) | 2023-06-30 10:58:2x
| show_reply				| bool		| 弹幕回复 |202206-
| reply_mid					| num		| 弹幕回复-uid |202206-
| reply_uname				| str		| 弹幕回复-昵称 |202206-
| reply_uname_color			| str		| 弹幕回复 |202206-
| reply_is_mystery			| bool		| 弹幕回复 |202206-
| reply_type_enum			| num		| 弹幕回复 |2025-
| hit_combo					| num		| 0,1 +1弹幕 |202206-
| esports_jump_url			| str		| |20240905
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
抽奖
| key 3				| type	| value	|
|-|-|-|
| activity_identity	| str	| 抽奖id |
| activity_source	| num	| 0 / 1 / 2 |
| not_show			| num	| 0 / 1 |
#### DANMU_MSG__dm_v2
	~~上线时间 2023-02-17 05:50:13~05:50:24(UTC+8)~~
	~~下线时间 2023-02-23 19:30~~
	上线时间 2023-03-23
	下线时间 2023-10-25
#### DANMU_MSG__example
```json
//大弹幕
{"cmd":"DANMU_MSG:3:7:1:1:1:1","info":[[0,7,100,16777215,xxx,xxx,0,"f4dbdf21",0,null,null,null,0,"{}","{}",{"mode":0,"show_player_type":0,"extra":"{\"mode\":0,\"send_from_me\":false,\"color\":16777215,\"dm_type\":0,\"font_size\":100,\"player_mode\":7,\"content\":\"[1.0,0.0,\\\"0.8-0.5\\\",10.0,\\\"哈哈哈哈\\\",0.0,0.0,0.0,0.0,10000,0,true,\\\"黑体\\\",1]\"}"},null,null],"[1.0,0.0,\"0.8-0.5\",10.0,\"哈哈哈哈\",0.0,0.0,0.0,0.0,10000,0,true,\"黑体\",1]",[0,"***",1,0,0,10000,1,""],null,[],[],0,0,null,{"ts":xxxxxxxxxx,"ct":"82145D85"},0,0,null,null,0,0,[0]]}
//假·抽奖弹幕
{"cmd":"DANMU_MSG","info":[[0,1,25, 16777215,xxx,xxx,0,"xxx",0,0,0,"",0,"{}","{}",{},{"activity_identity":"",       "activity_source":0,"not_show":0},0],"蔷薇与铳枪",[0,"***",1,0,0,10000,1,""],[],[0,0,0,">50000",0],["",""],0,0,null,{"ts":xxx,"ct":"xxx"},0,0,null,null,0,49,[0],null]}
//抽奖弹幕
{"cmd":"DANMU_MSG","info":[[0,1,25, 16777215,xxx,xxx,0,"xxx",0,2,0,"",0,"{}","{}",{},{"activity_identity":"5475890","activity_source":1,"not_show":1},0],"蔷薇与铳枪",[0,"***",1,0,0,10000,1,""],[],[0,0,0,">50000",0],["",""],0,0,null,{"ts":xxx,"ct":"xxx"},0,0,null,null,0,7,[0],null]}
//hit_combo(+1) 、 int64 dmid
{"cmd":"DANMU_MSG","info":[[0,1,25, 16777215,xxx,3745805152027139263,0,"x",0,0,0,"",0,"{}","{}",{"mode":0,"show_player_type":0,"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":0,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"太卡了x14\",\"user_hash\":\"xxx\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":4,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null,\"is_audited\":false,\"id_str\":\"03653126fb8b16e475d6fbee9765a8d563\",\"icon\":null,\"show_reply\":true,\"reply_mid\":0,\"reply_uname\":\"\",\"reply_uname_color\":\"\",\"reply_is_mystery\":false,\"hit_combo\":1}","user":{"uid":0,"base":{"name":"江***","face":"xxx","is_mystery":false,"name_color":0},"medal":null,"wealth":{"level":0}}},{"activity_identity":"","activity_source":0,"not_show":0},0],"太卡了x14",[0,"江***",0,0,0,10000,1,""],[],[5,0,9868950,">50000",0],["",""],0,0,null,{"ts":xxxxxxxxxx,"ct":"ABA7B5C8"},0,0,null,null,0,7,[0],null]}
//
{"cmd":"DANMU_MSG","info":[[0,1,25, 16777215,xxx,xxx,0,"xxx",0,0,0,"",1,{"bulge_display":0,"emoticon_unique":"official_331","height":60,"in_player_area":1,"is_dynamic":1,"url":"http://i0.hdslb.com/bfs/live/cbf2746062242e77bdcb9eb08edbf9b151fe0c2e.png","width":200},"{}",{"extra":"{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":1,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"啊\",\"user_hash\":\"xxx\",\"emoticon_unique\":\"official_331\",\"bulge_display\":0,\"recommend_score\":0,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"anniversary_crowd\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\",\"animation\":{},\"emots\":null,\"is_audited\":false,\"id_str\":\"xxxx\",\"icon\":null,\"show_reply\":true,\"reply_mid\":0,\"reply_uname\":\"\",\"reply_uname_color\":\"\",\"reply_is_mystery\":false,\"reply_type_enum\":0,\"hit_combo\":0,\"esports_jump_url\":\"\"}","mode":0,"show_player_type":0,"user":{"base":{"face":"xxx","is_mystery":false,"name":"xxx","name_color":0,"name_color_str":"","official_info":{"desc":"","role":0,"title":"","type":-1},"origin_info":{"face":"xxx","name":"xxx"},"risk_ctrl_info":null},"guard":null,"guard_leader":{"is_guard_leader":false},"medal":{"color":xxx,"color_border":xxx,"color_end":xxx,"color_start":xxx,"guard_icon":"","guard_level":0,"honor_icon":"","id":xxx,"is_light":1,"level":xxx,"name":"xxx","ruid":2222,"score":xxx,"typ":0,"user_receive_count":0,"v2_medal_color_border":"#xxx","v2_medal_color_end":"#xxx","v2_medal_color_level":"#xxx","v2_medal_color_start":"#xxx","v2_medal_color_text":"#xxx"},"title":{"old_title_css_id":"","title_css_id":""},"uhead_frame":null,"uid":xxx,"wealth":null}},{"activity_identity":"","activity_source":0,"not_show":0},0],"啊",[xxx,"xxx",0,0,0,10000,1,""],[xxx,"xxx","xxx",xxx,xxxx,"",0,xxxx,xxxx,xxxx,0,1,2222],[7,0,xxx,">50000",0],["",""],0,0,null,{"ct":"xxx","ts":xxx},0,0,null,null,0,xxx,[xx],null]}
```
#### 弹幕颜色
|name|color|color.hex(RGB)|weight|color_id|origin|描述|
|-|-:|-:|-:|-:|-:|-|
|`普`白色|`16777215`|`0xffffff` `ffffff`|-9999|-9999|0|普通|
|`航`紫色|`14893055`|`0xe33fff` `e33fff`|0|6|1|需要成为该主播的船员方可使用哦!|
|`粉`松石绿|`5566168`|`0x54eed8` `54eed8`|99|66|2|需粉丝勋章达5级才能使用哦！|
|`粉`雨后蓝|`5816798`|`0x58c1de` `58c1de`|98|67|2|需粉丝勋章达15级才能使用哦！|
|`粉`星空蓝|`4546550`|`0x455ff6` `455ff6`|97|68|2|需粉丝勋章达22级才能使用哦！|
|`粉`紫罗兰|`9920249`|`0x975ef9` `975ef9`|96|69|2|需粉丝勋章达26级才能使用哦！|
|`粉`梦境红|`12802438`|`0xc35986` `c35986`|95|70|2|需粉丝勋章达30级才能使用哦！|
|`粉`热力橙|`16747553`|`0xff8c21` `ff8c21`|94|71|2|需粉丝勋章达34级才能使用哦！|
|`粉`香槟金|`16774434`|`0xfff522` `fff522`|93|72|2|需粉丝勋章达38级才能使用哦！|
|`爷`红色|`16738408`|`0xff6868` `ff6868`|0|8|3|成为老爷即可使用哦！|
|`爷`蓝色|`6737151`|`0x66ccff` `66ccff`|0|7|3|成为年费老爷即可使用哦!|
|`活`盛典金|`16766720`|`0xffd700` `ffd700`|100|44|4|在特定活动中才可以获得哦！|
|`活`升腾蓝|`4286945`|`0x4169e1` `4169e1`|100|43|4|在特定活动中才可以获得哦！|
|`活`青色|`65532`|`0x00fffc` `00fffc`|0|5|4|需要完成【度年如日】成就才能使用哦!|
|`活`绿色|`8322816`|`0x7eff00` `7eff00`|0|4|4|需要完成【如雷贯耳】成就才能使用哦!|
|`活`黄色弹幕|`16772431`|`0xffed4f` `ffed4f`|0|3|4|需要完成【腰缠万贯】成就才能使用哦!|
|`活`橙色|`16750592`|`0xff9800` `ff9800`|0|2|4|需要完成【追云逐月】成就才能使用哦!|
|`活`粉色|`16741274`|`0xff739a` `ff739a`|0|1|4|拥有“五魁首”头衔时才可使用哟！|
----
### CUT_OFF
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
切断直播！  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CUT_OFF" |
| msg		| str	| |
| room_id	| num	| 直播间id |
```json
{"cmd":"CUT_OFF","msg":"xxx","room_id":xxx}
"版权相关"
"分区错误，直播该游戏请到THE FINALS分区"
"分区错误，直播该游戏请移至虚拟APEX分区直播"
"禁播游戏"
"麦上发言不当，请调整上麦门槛，再次违规将封禁直播间"
"违反直播规范"
"未持有相关许可，不允许直播相关内容"
"未持有新闻发布许可，不允许直播时政类内容"
"因版权原因，请立即调整"
"游戏中玩家昵称违反直播规范"
"游戏中玩家信息违反直播规范"
"直播互动区含有违规信息，不支持展示互动信息"
"直播内容不适宜"
"直播涉及辱骂引战类内容"
"直播中画面涉及低俗内容（如：文字、图片、物品等）"
"直播中涉及低俗内容"
```
----
### SHOPPING_CART_SHOW
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
?购物车  
开播后约30ms内发送`status=1`的包  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SHOPPING_CART_SHOW" |
| data		| obj	| |
#### SHOPPING_CART_SHOW__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 开播:1 / 下播:2 |
```json
{"cmd":"SHOPPING_CART_SHOW","data":{"status":1}}
{"cmd":"SHOPPING_CART_SHOW","data":{"status":2}}
```
----
### WIDGET_BANNER
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "ROOM_BANNER" / "WIDGET_BANNER" |
| data	| obj	| |
#### WIDGET_BANNER__data
| key			| type	| value	|
|-|-|-|
| timestamp		| num	| 当前时间TimeStamp(秒) |
| widget_list	| obj	| "ID":{} |
#### WIDGET_BANNER__data__widget_list__ID
| key 15			| type		| value	|
|-|-|-|
| id				| num		| ID |
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
| platform_in		| \[+\]str	| \["live","blink","live_link","web","pc_link"\] |
| type				| str		| |
| band_id			| num		| |
| sub_key			| str		| |
| sub_data			| str		| urlencoded(json) |
| is_add			| bool		| true |
----
### GOTO_BUY_FLOW
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
移动端 购买商品  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GOTO_BUY_FLOW" |
| data		| obj	| |
#### GOTO_BUY_FLOW__data
| key		| type	| value	|
|-|-|-|
| text		| str	| |
```json
{"cmd":"GOTO_BUY_FLOW","data":{"text":"x**正在去买"}}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"x**等x人正在去买"}}
{"cmd":"GOTO_BUY_FLOW","data":{"text":"x**等xx人正在去买"}}
```
----
### RECOMMEND_CARD
[TOP](#直播弹幕)  
文档更新：2024-05-28  
商品推销(移动端)  
| key					| type		| value	|
|-|-|-|
| cmd					| str		| "RECOMMEND_CARD" |
| data					| obj		| |
#### RECOMMEND_CARD__data
| key					| type		| value	|
|-|-|-|
| title_icon			| str		| https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png |
| recommend_list		| \[\]obj	| |
| timestamp				| num		| 当前时间TimeStamp(秒) |
#### RECOMMEND_CARD__data__recommend_list
| key					| type		| value	|
|-|-|-|
| shopping_card_detail	| obj		| |
| recommend_card_extra	| null/?	| |
#### RECOMMEND_CARD__data__recommend_list__shopping_card_detail
| key 32					| type	| value	|
|-|-|-|
| active_info				| null/?	| |
| activity_info				| null/?	| |
| btn_info					| null/obj	| |
| coupon_discount_price		| str		| |
| coupon_id					| str		| |
| coupon_info				| null/?	| |
| coupon_name				| str		| |
| early_bird_info			| null/?	| |
| gift_buy_info				| null/?	| |
| goods_icon				| str		| 商品图片 |
| goods_id					| str		| |
| goods_max_price			| str		| 最高价 |
| goods_name				| str		| 商品名称 |
| goods_price				| str		| 价格 |
| goods_sort_id				| num		| |
| goods_status				| num		| |
| goods_tag_list			| null/?	| |
| h5_url					| str		| |
| hot_buy_num				| num		| 本次直播 已售数量 |
| is_exclusive				| num		| |
| is_pre_sale				| bool		| |
| jump_link					| str		| |
| jump_url					| str		| |
| pre_sale_info				| null/?	| |
| price_info				| obj		| |
| reward_info				| null/?	| |
| sale_status				| num		| |
| schema_url				| str		| |
| selling_point				| str		| |
| source					| num		| |
| timestamp					| num		| TimeStamp(秒) |
| virtual_extra_info		| null/obj	| |
#### RECOMMEND_CARD__data__recommend_list__shopping_card_detail__btn_info
| key 6						| type		| value	|
|-|-|-|
| card_btn_click_url		| str		| |
| card_btn_jumpurl			| str		| |
| card_btn_route_jump_url	| str		| |
| card_btn_status			| num		| |
| card_btn_style			| num		| |
| card_btn_title			| str		| 状态 |
#### RECOMMEND_CARD__data__recommend_list__shopping_card_detail__price_info
| key 2						| type		| value	|
|-|-|-|
| normal					| obj 		| |
| ?activity					| null/?	| |
#### RECOMMEND_CARD__data__recommend_list__shopping_card_detail__price_info__normal
| key 7						| type		| value	|
|-|-|-|
| prefix_price				| str		| |
| sale_end_time				| num		| |
| sale_price				| str		| 最低价格 |
| sale_start_time			| num		| |
| strock_price				| str		| |
| strock_show				| num		| |
| suffix_price				| str		| |
```json
{
	"cmd":"RECOMMEND_CARD",
	"data":{
		"title_icon":"https://i0.hdslb.com/bfs/live/3053f47729c4974b1cfe4cd98482c28d4e23a1c2.png",
		"recommend_list":[
			{
				"shopping_card_detail":{
					"goods_id":"xxx",
					"goods_name":"xxx",
					"goods_price":"1.23",
					"goods_max_price":"",
					"sale_status":0,
					"coupon_name":"",
					"goods_icon":xxx,
					"goods_status":1,
					"source":5,
					"h5_url":xxx,
					"jump_link":"",
					"schema_url":"",
					"is_pre_sale":0,
					"activity_info":null,
					"pre_sale_info":null,
					"early_bird_info":null,
					"timestamp":xxx,
					"coupon_discount_price":"",
					"selling_point":"",
					"hot_buy_num":0,
					"gift_buy_info":null,
					"is_exclusive":false,
					"coupon_id":"",
					"reward_info":null,
					"goods_tag_list":null,
					"virtual_extra_info":{"goods_type":1,"web_container_type":1},
					"price_info":{"normal":{"prefix_price":"","sale_price":"1.23","suffix_price":"起","strock_price":"","sale_start_time":9999,"sale_end_time":0,"strock_show":1},"activity":null},
					"price_info":{"normal":{"prefix_price":"","sale_price":"1.23","suffix_price":"",  "strock_price":"","sale_start_time":xxx,"sale_end_time":xxx,"strock_show":1},
					"btn_info":{"card_btn_status":1,"card_btn_title":"去抢购","card_btn_style":1,"card_btn_jumpurl":"","card_btn_route_jump_url":"","card_btn_click_url":""},
					"goods_sort_id":0,
					"coupon_info":null,
					"active_info":null,
					"jump_url":""
				},
				"recommend_card_extra":null
			},
			{"key":"value"}
		],
		"timestamp":xxxxxxxxxx,
		"update_list":[]
	}
}
```
```python
recommend_list > shopping_card_detail > h5_url
# 主播装扮
"https://www.xxx.com/h5/mall/suit/detail?id={suit_id}&navhide=1                                               &rebate=2019116459&from_id={uid}&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui={xxx}&web_type=1&source=5&goods_id={goods_id}#/virdress",
# 主播收藏集
"https://www.xxx.com/h5/mall/digital-card/home?-Abrowser=live&act_id={act_id}&hybrid_set_header=2&lottery_id=0&rebate=2019116459&from_id={uid}&s_video=0&f_source=zhibo&is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui={xxx}&web_type=1&source=5&goods_id={goods_id}#/virdress",
# 带货
"TODO"
recommend_list > shopping_card_detail > price_info
# 主播装扮
{"normal":{"prefix_price":"","sale_price":"1.23","suffix_price":"起","strock_price":"","sale_start_time":9999,"sale_end_time":0,"strock_show":1},"activity":null}
# 主播收藏集
{"normal":{"prefix_price":"","sale_price":"9.90","suffix_price":"","strock_price":"","sale_start_time":xxx,"sale_end_time":xxx,"strock_show":1}}
# 带货
"TODO"
recommend_list > shopping_card_detail > goods_icon
# 主播装扮
"https://i0.hdslb.com/bfs/garb/item/xxx.jpg"
# 主播收藏集
"https://i0.hdslb.com/bfs/garb/xxx.jpg"
# 带货

```
----
### LIKE_INFO_V3_NOTICE
### COMMON_NOTICE_DANMAKU
[TOP](#直播弹幕)  
文档更新：2024-05-23  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMMON_NOTICE_DANMAKU" "LIKE_INFO_V3_NOTICE" |
| data		| obj	| |
#### COMMON_NOTICE_DANMAKU__data
| key				| type		| value	|
|-|-|-|
| ?biz_id			| num		| 0 |
| content_segments	| \[\]obj	| |
| ?danmaku_style	| obj		| |
| ?danmaku_uri		| str		| "" |
| dmscore			| num		| ? |
| terminals			| \[1+\]num	| \[1,2,3,4,5\] |
#### COMMON_NOTICE_DANMAKU__data__danmaku_style
| key						| type		| value	|
|-|-|-|
| background_color			| null/xxx	| |
| background_color_dark		| null/xxx	| |
#### COMMON_NOTICE_DANMAKU__data__content_segments
| key							| type			| value	|
|-|-|-|
| ?background_color				| null/\[1\]str	| |
| ?background_color_dark		| null/xxx		| |
| ?font_bold					| bool			| |
| font_color					| str			| "#RRGGBB" |
| ?font_color_dark				| str			| "" / "#RRGGBB" |
| ?highlight_font_color			| str			| "" / "#RRGGBB" |
| ?highlight_font_color_dark	| str			| "" / "#RRGGBB" |
| ?img_height					| num			| |
| ?img_url						| str			| |
| ?img_width					| num			| |
| text							| str			| |
| type							| num			| |
| ?uri							| num			| |
```json
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"content_segments":[{"background_color":null,"background_color_dark":null,"font_bold":false,"font_color":"#xxxxxx","font_color_dark":"","highlight_font_color":"","highlight_font_color_dark":"","img_height":0,"img_url":"","img_width":0,"text":"xxx","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"dmscore":xxx,"terminals":[1,2,3,4,5]}}
{"cmd":"COMMON_NOTICE_DANMAKU","data":{"biz_id":0,	"content_segments":[{"font_color":"#998EFF","font_color_dark":"#998EFF","text":"恭喜 xxx 成为上时段 xxx 第 xx 名","type":1}],"danmaku_style":{"background_color":null,"background_color_dark":null},"danmaku_uri":"","dmscore":xxx,"terminals":[4]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"试试双击点赞，让主播被更多人看到吧～","type":1}],"danmaku_style":{"background_color":null},"terminals":[1,4]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计100，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计500，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计5000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计10000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计50000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计1000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
{"cmd":"LIKE_INFO_V3_NOTICE",  "data":{				"content_segments":[{"font_color":"#F494AF",							"text":"本场点赞已累计5000000，快去号召直播间用户继续为你助力吧~","type":1}],"danmaku_style":{"background_color":null},"terminals":[2,5]}}
```
```python
name = ""
content_segments__text=[
	# 主播
	[f"恭喜主播 {name} ",f"成为{rank_name}当前第{rank}名"],
	[f"恭喜主播 {name} ",f"成为上时段 {rank_name} 第 {rank} 名"],
	f"<%恭喜主播 {name} %>成为 上小时人气榜 第 {rank} 名！",
	f"{event_name}：恭喜{name}成功{xxx}！",
	f"{event_name}：恭喜{name}晋级！",
	f"{event_name}：恭喜{name}晋级{xxx}！",
	f"{event_name}：恭喜{name}完成{event_name}LV.{lv}任务，获得{reward_name}奖励！",
	f"{event_name}：恭喜主播{name}获得{rank_name}赛道第{rank}名！",
	f"{event_name}：恭喜主播{name}晋级{xxx}！",
	f"{event_name}：恭喜主播{name}完成LV.{lv}任务，获得{reward_name}奖励！",
	f"恭喜主播 {name} 成为{rank_name}当前第{rank}名",
	f"恭喜主播 {name} 成为{rank_name}第{rank}名",
	f"恭喜 {name} 成为上时段 {rank_name}榜 第 {rank} 名",
	f"恭喜{name}完成{event_name}LV.{lv}任务，获得{reward_name}奖励！",
	"航海回馈审核通过，开始发放",
	"我方主播在绝杀时刻领先对手1000PK值，触发绝杀！",
	"绝杀时刻开启，绝杀结束时领先对手100PK值，即可触发绝杀提前赢得胜利！",
	"我方主播暂时领先！兄弟萌注意守塔，保护好我方主播哟～",
	f"撒花！恭喜主播已完成<%{anchor_name}%>的心愿收集！",
	f"{event_name}(限时任务)?：恭喜主播完成限时任务，获得{num}{reward_name}奖励！",
	f"{event_name}(限时任务)?：恭喜主播完成限时任务，直播间派发{num}元红包，速抢手慢无！",
	f"{event_name}限时任务：任务即将结束，抓紧完成获取{num}{reward_name}奖励吧！未完成任务将无法获得奖励",
	# 用户
	[f"{name}","投喂","大航海盲盒","爆出",f"{anchor_name}*{num}天"],
	f"<%{gift_name}%> 被点亮啦！恭喜 <%{name}%> 成为星球守护者！",
	f"恭喜 <%{name}%> 成为 <%{gift_name}%> 星球守护者~",
	f"{name} 送出的红包为主播新增{num}个粉丝！",
	f"{name}的直播间心动盲盒爆率翻倍开启中，浪漫城堡5倍爆率！",
	f"{name}在你的直播间发送红包啦！你已经获得了部分收益哦～",
	f"{name}在元气赏中五连抽！送出了好多礼物！",
	f"恭喜{name}成功晋级下一阶段！",
	f"恭喜{name}单抽获得",
	f"恭喜{name}单抽获得{item_name}",
	f"恭喜{name}十连抽获得{item_name}...",
	f"恭喜用户 {name} <%荣耀等级升级至{num}级%>",
]
```
----
### POPULARITY_RED_POCKET_NEW
[TOP](#直播弹幕)  
文档更新：2024-05-23  
红包抽奖  
| key			| type		| value	|
|-|-|-|
| cmd			| str		| "POPULARITY_RED_POCKET_NEW" "POPULARITY_RED_POCKET_V2_NEW" |
| data			| obj		| |
#### POPULARITY_RED_POCKET_NEW__data
| key			| type		| value	|
|-|-|-|
| lot_id		| num		| 抽奖id |
| start_time	| num		| 开始时间TimeStamp(秒) |
| current_time	| num		| 当前时间TimeStamp(秒) |
| wait_num		| num		| 排队 |
| wait_num_v2	| num		| 排队 |
| uname			| str		| 昵称 |
| uid			| num		| uid |
| action		| str		| "送出" |
| num			| num		| 1 |
| gift_name		| str		| "红包" |
| gift_id		| num		| `13000` |
| price			| num		| 价格(RMB×10) |
| name_color	| str		| "#RRGGBB" |
| medal_info	| obj		| [medal_info](#粉丝勋章medal_info) |
| wealth_level	| num		| |
| group_medal	| null/xxx	| |
| is_mystery	| bool		| |
| sender_info	| obj		| [uinfo](#PUBLIC_uinfo) |
| gift_icon		| str		| |
| rp_type		| num		| |
```json
{"cmd":"POPULARITY_RED_POCKET_V2_NEW","data":{"lot_id":xxx,"start_time":xxxxxxxxxx,"current_time":xxxxxxxxxx,"wait_num":xx,"wait_num_v2":xx,"uname":"xxx","uid":xxx,"action":"送出","num":1,"gift_name":"红包","gift_id":13000,"price":20,"name_color":"#xxxxxx","medal_info":xxx,"wealth_level":123,"group_medal":null,"is_mystery":false,"sender_info":xxx,"gift_icon":"","rp_type":0}}
```
----
### POPULARITY_RED_POCKET_START
[TOP](#直播弹幕)  
文档更新：2024-05-23  
红包抽奖  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULARITY_RED_POCKET_START" "POPULARITY_RED_POCKET_V2_START" |
| data		| obj	| |
#### POPULARITY_RED_POCKET_START__data
| key 22				| type		| value	|
|-|-|-|
| lot_id				| num		| 抽奖id |
| sender_uid			| num		| uid |
| sender_name			| str		| 昵称 |
| sender_face			| str		| 头像URL |
| join_requirement		| num		| 1 |
| danmu					| str		| "老板大气！点点红包抽礼物" |
| current_time			| num		| TimeStamp(秒) 当前时间 |
| start_time			| num		| TimeStamp(秒) 开始时间 |
| end_time				| num		| TimeStamp(秒) 结束时间 | start_time + last_time
| last_time				| num		| 持续时间(秒) |
| remove_time			| num		| TimeStamp(秒) 图标移除时间 | end_time + 15
| replace_time			| num		| TimeStamp(秒) 下一个红包显示时间 | end_time + 10
| lot_status			| num		| [lot_status](#others) 1 |
| h5_url				| str		| |
| user_status			| num		| 2 |
| awards				| \[3\]obj	| |
| lot_config_id			| num		| 红包预设 |
| total_price			| num		| 礼物总价值×0.8 |
| wait_num				| num		| 队列数量 |
| wait_num_v2			| num		| 队列数量 |
| is_mystery			| bool		| |
| rp_type				| num		| |
| sender_uinfo			| obj		| [uinfo](#PUBLIC_uinfo) |
| icon_url				| str		| |
| animation_icon_url	| str		| |
#### POPULARITY_RED_POCKET_START__data__awards
| key		| type	| value	|
|-|-|-|
| gift_id	| num	| 礼物id |
| gift_name	| num	| 礼物名称 |
| gift_pic	| num	| 礼物图像URL(140×140) |
| num		| num	| 数量 |
```json
{"cmd":"POPULARITY_RED_POCKET_START",   "data":{"lot_id":xxx,"sender_uid":xxx,"sender_name":"xxx","sender_face":"xxx","join_requirement":1,"danmu":"xxx","current_time":xxxxxxxxxx,"start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx,"last_time":180,"remove_time":xxxxxxxxxx,"replace_time":xxxxxxxxxx,"lot_status":1,"h5_url":"xxx","user_status":2,"awards":[{"gift_id":31212,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","num":2},{"gift_id":34003,"gift_name":"人气票","gift_pic":"https://s1.hdslb.com/bfs/live/7164c955ec0ed7537491d189b821cc68f1bea20d.png","num":3},{"gift_id":31216,"gift_name":"小花花","gift_pic":"https://s1.hdslb.com/bfs/live/5126973892625f3a43a8290be6b625b5e54261a5.png","num":3}],"lot_config_id":3,"total_price":1600,"wait_num":xx,"wait_num_v2":xx,"is_mystery":false,"rp_type":0,"sender_uinfo":xxx,"icon_url":"","animation_icon_url":""}}
{"cmd":"POPULARITY_RED_POCKET_V2_START","data":{"lot_id":123,"sender_uid":123,"sender_name":"xxx","sender_face":"xxx","join_requirement":1,"danmu":"xxx","current_time":xxxxxxxxxx,"start_time":xxxxxxxxxx,"end_time":xxxxxxxxxx,"last_time":180,"remove_time":xxxxxxxxxx,"replace_time":xxxxxxxxxx,"lot_status":1,"h5_url":"xxx","user_status":2,"awards":[{"gift_id":31212,"gift_name":"打call","gift_pic":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","num":2},{"gift_id":34003,"gift_name":"人气票","gift_pic":"https://s1.hdslb.com/bfs/live/7164c955ec0ed7537491d189b821cc68f1bea20d.png","num":3},{"gift_id":31216,"gift_name":"小花花","gift_pic":"https://s1.hdslb.com/bfs/live/5126973892625f3a43a8290be6b625b5e54261a5.png","num":3}],"lot_config_id":3,"total_price":1600,"wait_num":xx,"wait_num_v2":xx,"is_mystery":false,"rp_type":0,"sender_uinfo":xxx,"icon_url":"","animation_icon_url":""}}

"danmu":["老板大气！点点红包抽礼物", "点点红包，关注主播抽礼物～"]
```
----
### POPULARITY_RED_POCKET_WINNER_LIST
[TOP](#直播弹幕)  
文档更新：2024-05-23  
红包抽奖  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "POPULARITY_RED_POCKET_WINNER_LIST" "POPULARITY_RED_POCKET_V2_WINNER_LIST" |
| data	| obj	| |
#### POPULARITY_RED_POCKET_WINNER_LIST__data
| key			| type					| value	|
|-|-|-|
| lot_id		| num					| 抽奖id |
| total_num		| num					| |
| award_num		| num					| _:`total_num` / V2:`0` |
| winner_info	| \[total_num\]array	| |
| awards		| obj					| `{gift_id}:{obj...}` |
| version		| num					| 1 |
| rp_type		| num					| |
| timestamp		| num					| _:`timestamp` / V2:`0` |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__winner_info
| array	| type	| value	|
|-|-|-|
| 0 | num	| 获奖者_uid |
| 1 | str	| 获奖者昵称 |
| 2 | num	| `bag_id` |
| 3 | num	| gift_id |
| 4 | bool	| ?false |
| 5 | null	| ?null |
| 6 | num	| `-> timestamp` |
| 7 | num	| ruid |
#### POPULARITY_RED_POCKET_WINNER_LIST__data__awards
| key			| type	| value	|
|-|-|-|
| award_type	| num	| |
| award_name	| str	| 礼物名称 |
| award_pic		| str	| URL_图像(140×140) |
| award_big_pic	| str	| URL_图像(360×360) |
| award_price	| num	| 礼物单价(RMB×1000) |
```json
{
	"cmd":"POPULARITY_RED_POCKET_V2_WINNER_LIST",
	"data":{
		"lot_id":123,
		"total_num":8,
		"award_num":0,
		"winner_info":[
			[12345,"xxx",1234567,31212,false,null,1710000000,123456],
			[xxx]+7
	],
	"awards":{
			"31212":{"award_type":1,"award_name":"打call","award_pic":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","award_big_pic":"https://i0.hdslb.com/bfs/live/9e6521c57f24c7149c054d265818d4b82059f2ef.png","award_price":500},
			"31216":{"award_type":1,"award_name":"小花花","award_pic":"https://s1.hdslb.com/bfs/live/5126973892625f3a43a8290be6b625b5e54261a5.png","award_big_pic":"https://i0.hdslb.com/bfs/live/cf90eac49ac0df5c26312f457e92edfff266f3f1.png","award_price":100},
			"34003":{"award_type":1,"award_name":"人气票","award_pic":"https://s1.hdslb.com/bfs/live/7164c955ec0ed7537491d189b821cc68f1bea20d.png","award_big_pic":"https://i0.hdslb.com/bfs/live/5bfaddf9a78e677501bb6d440f4d690668136496.png","award_price":100}
		},
		"version":1,
		"rp_type":0,
		"timestamp":0
	}
}
{
	"cmd":"POPULARITY_RED_POCKET_WINNER_LIST",
	"data":{
		...
		"total_num":8,
		"award_num":8,
		...
		"timestamp":xxxxxxxxxx
	}
}
```
----
### ROOM_BLOCK_MSG
[TOP](#直播弹幕)  
文档更新：2024-11-01  
用户封禁  
| key		| type		| value	|
|-|-|-|
| cmd		| str		| "ROOM_BLOCK_MSG" |
| data		| obj		| |
| uid		| str/num	| |
| uname		| str		| 昵称 |
#### ROOM_BLOCK_MSG__data
| key		| type	| value	|
|-|-|-|
| block_expired	| num	| 结束时间 |
| dmscore		| num	| 30 45 90 135 180 |
| operator		| num	| 1:房管 / 2:主播 |
| uid			| num	| |
| uname			| str	| 昵称 |
| vaild_period	| str	| 生效时间-描述 | 20240720-20240724
```json
{"cmd":"ROOM_BLOCK_MSG","data":{"block_expired":2145888000,"dmscore":xx,"operator":x,"uid":xxx,"uname":"xxx","vaild_period":"仅本场直播有效"},"uid":xxx,"uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"block_expired":2145888000,"dmscore":xx,"operator":x,"uid":xxx,"uname":"xxx","vaild_period":"永久"},"uid":xxx,"uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"block_expired":xxxxxxxxxx,"dmscore":xx,"operator":x,"uid":xxx,"uname":"xxx","vaild_period":"24小时有效"},"uid":xxx,"uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"block_expired":xxxxxxxxxx,"dmscore":xx,"operator":x,"uid":xxx,"uname":"xxx","vaild_period":"2小时有效"},"uid":xxx,"uname":"xxx"}
{"cmd":"ROOM_BLOCK_MSG","data":{"block_expired":xxxxxxxxxx,"dmscore":xx,"operator":x,"uid":xxx,"uname":"xxx","vaild_period":"7天有效"},"uid":xxx,"uname":"xxx"}
```
----
### AREA_RANK_CHANGED
[TOP](#直播弹幕)  
文档更新：2024-05-26  
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
| action_type	| num	| 1 / 2 |
| timestamp		| num	| 当前时间 TimeStamp(秒) |
| msg_id		| str	| UUID4 |
| jump_url_link	| str	| |
| jump_url_pc	| str	| |
| jump_url_pink	| str	| |
| jump_url_web	| str	| |
```json
{
	"cmd":"AREA_RANK_CHANGED",
	"data":{
		"conf_id":18,
		"rank_name":"聊天热榜",
		"uid":xxx,
		"rank":0,
		"icon_url_blue":"https://i0.hdslb.com/bfs/live/18e2990a546d33368200f9058f3d9dbc4038eb5c.png",
		"icon_url_pink":"https://i0.hdslb.com/bfs/live/a6c490c36e88c7b191a04883a5ec15aed187a8f7.png",
		"icon_url_grey":"https://i0.hdslb.com/bfs/live/cb7444b1faf1d785df6265bfdc1fcfc993419b76.png",
		"action_type":2,
		"timestamp":xxxxxxxxxx,
		"msg_id":"xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
		"jump_url_link":"https://live.xxx.com/p/html/live-app-hotrank/index.html?clientType=3&{ruid=}&{conf_id=}....../area-rank",
		"jump_url_pc":"https://live.xxx.com/p/html/live-app-hotrank/index.html?clientType=4&{ruid=}&{conf_id=}....../area-rank",
		"jump_url_pink":"https://live.xxx.com/p/html/live-app-hotrank/index.html?clientType=1&{ruid=}&{conf_id=}....../area-rank",
		"jump_url_web":"https://live.xxx.com/p/html/live-app-hotrank/index.html?clientType=2&{ruid=}&{conf_id=}#/area-rank"
	}
}
```
----
### HOT_BUY_NUM
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
{"cmd":"HOT_BUY_NUM","data":{"goods_id":"xxx","num":xxx}}
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
| key				| type		| value	|
|-|-|-|
| start_date		| num		| yyyyMMdd(星期一) |
| process_list		| \[+\]obj	| |
| finished			| bool		| |
| ddl_timestamp		| num		| TimeStamp(秒) 下一个星期一 00:00:00 UTC+8 |
| version			| num		| 当前时间TimeStamp(毫秒) |
| reward_gift		| num		| |
| reward_gift_img	| str		| |
| reward_gift_name	| str		| "礼物星球" |
| level_info		| obj		| |
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
	"start_date":yyyymmdd,
	"process_list":[
			{"gift_id":31037,"gift_img":"https://s1.hdslb.com/bfs/live/461be640f60788c1d159ec8d6c5d5cf1ef3d1830.png","gift_name":"礼物星球","completed_num":x,"target_num":xx},
			{"gift_id":30758,"gift_img":"https://s1.hdslb.com/bfs/live/3ddb10b055b9d1826829ec0fad93ab56484d4a90.png","gift_name":"礼物星球","completed_num":x,"target_num":xx},
			{"gift_id":31044,"gift_img":"https://s1.hdslb.com/bfs/live/14dafbf217618f0931c08897e0b3eefc00d0da22.png","gift_name":"礼物星球","completed_num":x,"target_num":xx}
		],
		"finished":false,"ddl_timestamp":xxxxxxxxxx,"version":xxxxxxxxxxxxx,
		"reward_gift":32267,"reward_gift_img":"https://i0.hdslb.com/bfs/live/52edb4ab7377ece34ac15b21154d13d188874b01.png","reward_gift_name":"礼物星球",
		"level_info":{"star_name":"礼物星球","level_tip":"成就Ⅰ","level_img":"https://i0.hdslb.com/bfs/live/a43790d946829348ee506911f8b5a2a752c6de8e.png","level_id":1}
	}
}
```
----
### LIVE_INTERACTIVE_GAME
[TOP](#直播弹幕)  
文档更新：2024-01-20
| key				| type	| value	|
|-|-|-|
| cmd				| str	| "LIVE_INTERACTIVE_GAME" |
| data				| obj	| |
#### LIVE_INTERACTIVE_GAME__data
| key 17			| type	| value	|
|-|-|-|
| type				| num	| ?2 |
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
{"cmd":"LIVE_INTERACTIVE_GAME","data":{"type":2,"uid":123,"uname":"xxx","uface":"","gift_id":0,"gift_name":"","gift_num":0,"price":0,"paid":false,"msg":"text","fans_medal_level":18,"guard_level":0,"timestamp":xxxxxxxxxx,"anchor_lottery":null,"pk_info":null,"anchor_info":null,"combo_info":null}}
```
----
### LIVE_MULTI_VIEW_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_MULTI_VIEW_CHANGE" |
| data		| obj	| |
#### LIVE_MULTI_VIEW_CHANGE__data
| key		| type	| value	|
|-|-|-|
| scatter	| obj	| |
```json
{"cmd":"LIVE_MULTI_VIEW_CHANGE","data":{"scatter":{"max":120,"min":5}}}
```
----
### SUPER_CHAT_ENTRANCE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SUPER_CHAT_ENTRANCE" |
| data		| obj	| |
| ?roomid	| num	| |
#### SUPER_CHAT_ENTRANCE__data
| key				| type	| value	|
|-|-|-|
| ?status			| num	| |
| icon				| str	| |
| jump_url			| str	| |
| broadcast_type	| num	| 0 / 1 |
```json
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","jump_url":"https://live.xxx.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","status":0}}
{"cmd":"SUPER_CHAT_ENTRANCE","data":{"status":1,"jump_url":"https://live.xxx.com/p/html/live-app-superchat2/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,70p,ffffff,0,30,100;2,2,375,100p,ffffff,0,30,100;3,3,100p,70p,ffffff,0,30,100;4,2,375,100p,ffffff,0,30,100;5,3,100p,60p,ffffff,0,30,100;6,3,100p,60p,ffffff,0,30,100;7,3,100p,60p,ffffff,0,30,100","icon":"https://i0.hdslb.com/bfs/live/0a9ebd72c76e9cbede9547386dd453475d4af6fe.png","broadcast_type":1},"roomid":"xxx"}
```
----
### SYS_MSG
[TOP](#直播弹幕)  
文档更新：2024-11-01  
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
{"cmd":"VOICE_JOIN_STATUS","data":{"room_id":12345,"status":0,"channel":"","channel_type":"voice","uid":0,"user_name":"","head_pic":"","guard":0,"start_at":0,"current_time":1111111111,"web_share_link":"https://live.xxx.com/h5/xxx"},"room_id":12345}
{"cmd":"VOICE_JOIN_STATUS","data":{"channel":"",   "channel_type":"voice","current_time":1111111111,"guard":9,"head_pic":"",   "is_mystery":false,"room_id":12345,"start_at":0,         "status":0,"uid":0,    "uinfo":null,"user_name":"",   "web_share_link":"https://live.xxx.com/h5/12345"},"room_id":12345}
{"cmd":"VOICE_JOIN_STATUS","data":{"channel":"xxx","channel_type":"voice","current_time":1111111111,"guard":9,"head_pic":"xxx","is_mystery":false,"room_id":12345,"start_at":1111111111,"status":1,"uid":12345,"uinfo":null,"user_name":"xxx","web_share_link":"https://live.xxx.com/h5/12345"},"room_id":12345}
```
----
### DM_INTERACTION
[TOP](#直播弹幕)  
文档更新：2025-04-01  
弹幕互动  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "DM_INTERACTION" |
| data		| obj	| |
#### DM_INTERACTION__data
| key		| type	| value	|
|-|-|-|
| id		| num	| |
| status	| num	| 3:开始 / 4:进行中 / 5:结束 |
| type		| num	| |
| data		| str	| json |
#### DM_INTERACTION__TYPE101__data
| key					| type		| value	|
|-|-|-|
| question				| str		| |
| options				| \[\]obj	| |
| vote_id				| num		| |
| cnt					| num		| 投票总数 |
| duration				| num		| 总时长(ms) |
| left_duration			| num		| 剩余时间(ms) |
| fade_duration			| num		| 1000 (ms) |
| waiting_duration		| num		| -1 |
| result				| num		| |
| result_text			| str		| |
| component				| str		| |
| natural_die_duration	| num		| 30000 |
| my_vote				| num		| |
#### DM_INTERACTION__TYPE101__data__options
| key					| type		| value	|
|-|-|-|
| idx					| num		| start:1 |
| desc					| str		| 投票选项 |
| cnt					| num		| 投票人数 |
| percent				| float		| 百分比 总计数小于~~5~~时为0 |
#### DM_INTERACTION__TYPE102__data
| key					| type		| value	|
|-|-|-|
| combo					| \[1+\]obj	| |
| merge_interval		| num		| |
| card_appear_interval	| num		| |
| send_interval			| num		| |
| reset_cnt				| num		| |
| display_flag			| num		| |
#### DM_INTERACTION__TYPE102__data__combo
| key					| type		| value	|
|-|-|-|
| id					| num		| |
| status				| num		| |
| content				| str		| |
| cnt					| num		| |
| guide					| str		| "他们都在说:" |
| left_duration			| num		| 剩余时间(ms) |
| fade_duration			| num		| |
| prefix_icon			| str		| |
#### DM_INTERACTION__TYPE103_TYPE105_TYPE106__data
| key					| type		| value	|
|-|-|-|
| fade_duration			| num		| |
| cnt					| num		| |
| card_appear_interval	| num		| |
| suffix_text			| str		| |
| reset_cnt				| num		| |
| display_flag			| num		| |
#### DM_INTERACTION__TYPE104__data
| key					| type		| value	|
|-|-|-|
| fade_duration			| num		| |
| cnt					| num		| |
| card_appear_interval	| num		| |
| suffix_text			| str		| |
| reset_cnt				| num		| |
| display_flag			| num		| |
| gift_id				| num		| |
| gift_alert_message	| str		| |
#### DM_INTERACTION__example
```json
{"cmd":"DM_INTERACTION","data":{"data":"{\"question\":\"xxx\",\"options\":[{\"idx\":1,\"desc\":\"xxx\",\"cnt\":0,\"percent\":0},    {\"idx\":2,\"desc\":\"yyy\",\"cnt\":0,  \"percent\":0}],  \"vote_id\":xxx,\"cnt\":0,  \"duration\":180000,\"left_duration\":xxx,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":xxx,\"result_text\":\"xxx\",\"component\":\"https://live.xxx.com/p/html/live-app-guessing-game/vote.html?...\",\"natural_die_duration\":30000,\"my_vote\":0}","id":104,"status":xxx,"type":101}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"question\":\"xxx\",\"options\":[{\"idx\":1,\"desc\":\"xxx\",\"cnt\":xxx,\"percent\":0.o},{\"idx\":2,\"desc\":\"yyy\",\"cnt\":yyy,\"percent\":o.O}],\"vote_id\":xxx,\"cnt\":xxx,\"duration\":180000,\"left_duration\":xxx,\"fade_duration\":1000,\"waiting_duration\":-1,\"result\":xxx,\"result_text\":\"xxx\",\"component\":\"https://live.xxx.com/p/html/live-app-guessing-game/vote.html?...\",\"natural_die_duration\":30000,\"my_vote\":0}","id":xxx,"status":xxx,"type":101}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"combo\":[{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000,\"reset_cnt\":1,\"display_flag\":0}","dmscore":36,"id":xxx,"status":xxx,"type":102}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"combo\":[{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000,\"reset_cnt\":1,\"display_flag\":0}","dmscore":36,"id":xxx,"status":xxx,"type":102}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"combo\":[{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000,\"reset_cnt\":1,\"display_flag\":0}","dmscore":xxx,"id":xxx,"status":xxx,"type":102}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"combo\":[{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"},{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000,\"reset_cnt\":1,\"display_flag\":0}","dmscore":xxx,"id":xxx,"status":xxx,"type":102}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"combo\":[{\"id\":xxx,\"status\":xxx,\"content\":\"xxx\",\"cnt\":xxx,\"guide\":\"他们都在说:\",\"left_duration\":xxx,\"fade_duration\":10000,\"prefix_icon\":\"\"}],\"merge_interval\":1000,\"card_appear_interval\":1000,\"send_interval\":1000,\"reset_cnt\":1,\"display_flag\":0}","dmscore":xxx,"id":xxx,"status":xxx,"type":102}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"fade_duration\":10000,\"cnt\":xxx,\"card_appear_interval\":0,\"suffix_text\":\"人关注了主播\",\"reset_cnt\":0,\"display_flag\":1}","dmscore":xxx,"id":xxx,"status":xxx,"type":103}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"fade_duration\":10000,\"cnt\":xxx,\"card_appear_interval\":0,\"suffix_text\":\"人在投喂\",\"reset_cnt\":0,\"display_flag\":1,\"gift_id\":xxx,\"gift_alert_message\":\"\"}","dmscore":xxx,"id":xxx,"status":xxx,"type":104}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"fade_duration\":10000,\"cnt\":xxx,\"card_appear_interval\":0,\"suffix_text\":\"人分享了直播间\",\"reset_cnt\":0,\"display_flag\":1}","dmscore":xxx,"id":xxx,"status":xxx,"type":105}}
{"cmd":"DM_INTERACTION","data":{"data":"{\"fade_duration\":10000,\"cnt\":xxx,\"card_appear_interval\":0,\"suffix_text\":\"人正在点赞\",\"reset_cnt\":1,\"display_flag\":1}","dmscore":xxx,"id":xxx,"status":xxx,"type":106}}
```
```python
{
	101:"投票",
	102:"他们都在说:",
	103:"%d人关注了主播",
	104:"%d人在投喂 投喂一个%s支持主播",
	105:"%d人分享了直播间",
	106:"%d人正在点赞",
}
```
----
### PLAY_TAG
[TOP](#直播弹幕)  
文档更新：2024-11-01  
比赛事件  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PLAY_TAG" |
| data		| obj	| |
#### PLAY_TAG__data
| key		| type	| value	|
|-|-|-|
| tag_id	| num	| |
| pic		| str	| 事件pic |
| timestamp	| num	| TimeStamp(秒) |
| type		| str	| "ADD" |
```json
{"cmd":"PLAY_TAG","data":{"tag_id":xxx,"pic":"https://i0.hdslb.com/bfs/live/xxx.png","timestamp":xxx,"type":"ADD"}}
```
----
### FULL_SCREEN_SPECIAL_EFFECT
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "FULL_SCREEN_SPECIAL_EFFECT" |
| data	| obj	| |
#### FULL_SCREEN_SPECIAL_EFFECT__data
| key			| type		| value	|
|-|-|-|
| type			| num		| |
| ids			| \[1\]num	| |
| queue			| num		| |
| platform_in	| \[+\]num	| |
```json
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":2,"ids":[xxx],"queue":2,"platform_in":[1,2]}}
{"cmd":"FULL_SCREEN_SPECIAL_EFFECT","data":{"type":3,"ids":[xxx],"queue":2,"platform_in":[1,2]}}
// ids
[433,514,515,670,949,1022,1045,1816,1226]
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
| update_type		| num	| 1 / 2 |
```json
{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":200,"score_id":3,"uid":12345,"update_time":1111111111,"update_type":2}}
{"cmd":"TRADING_SCORE","data":{"bubble_show_time":3,"num":000,"score_id":3,"uid":12345,"update_time":1111111111,"update_type":1}}
```
----
### ROOM_SILENT
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
`ROOM_SILENT_ON` 开启直播间全局禁言
`ROOM_SILENT_OFF` 解除直播间全局禁言
| key		| type	| value	|
|-|-|-|
| data		| obj	| |
| cmd		| str	| "ROOM_SILENT_ON" / "ROOM_SILENT_OFF" |
#### ROOM_SILENT__data
| key		| type	| value	|
|-|-|-|
| type		| str	| "":关闭 / "member":全员禁言 / "medal":粉丝勋章等级禁言 / "level":UL等级禁言 "wealth":荣耀等级 |
| level		| num	| 粉丝勋章等级:1-40 / 用户UL等级 / 荣耀等级:1-80 |
| second	| num	| 结束时间TimeStamp(秒) / -1:永久 |
| msg		| str	| |
```json
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"member"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":xxxxxxxxxx,"type":"member"}}

{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":-1,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":xxxxxxxxxx,"type":"level"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":60,"second":xxxxxxxxxx,"type":"level"}}

{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":-1,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":-1,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":1,"second":xxxxxxxxxx,"type":"medal"}}
{"cmd":"ROOM_SILENT_ON","data":{"level":40,"second":xxxxxxxxxx,"type":"medal"}}

{"data":{"type":"wealth","level":xxx,"second":xxx,"msg":"[系统]: 主播对荣耀等级xxx级以下的用户开启了禁言"},"cmd":"ROOM_SILENT_ON"}

{"data":{"type":"","level":0,"second":0,"msg":"[系统]: 主播取消了房间禁言"},"cmd":"ROOM_SILENT_OFF"}
```
```python
match data["type"]:
	case "member":	print(f'主播对用户等级 UL.{level} 以下的用户开启了禁言')
	case "medal":	print(f'主播对粉丝勋章 {level} 以下的用户开启了禁言')
	case "level":	print('主播取消了房间禁言')
	case "":		print('主播对所有用户开启了禁言')
```
----
### CHANGE_ROOM_INFO
[TOP](#直播弹幕)  
文档更新：2024-11-11  
更换直播间背景(WEB)  
| key			| type		| value	|
|-|-|-|
| cmd			| str		| "CHANGE_ROOM_INFO" |
| background	| str		| URL |
| roomid		| num/str	| |
```json
{"cmd":"CHANGE_ROOM_INFO","background":"http://i0.hdslb.com/bfs/live/room_bg/17bb8b588f8371a8582fa443fe2d5a0b7ac01453.jpg","roomid":"21987615"}
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/f3c1e1e22dfb1942bd88c33f1aa174efe7a38dfd.jpg","roomid":xxx}//默认背景
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/785922a49980e1aa3239249c8360909488940d7d.jpg","roomid":xxx}//默认背景
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/636d66a97d5f55099a9d8d6813558d6d4c95fd61.jpg","roomid":xxx}//默认背景
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/2bac063036fbcf316e021fbfb8109ff3028360a6.jpg","roomid":xxx}//默认背景
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/2836bb7b84c792e2c6aadfd4d1cce13484775fa3.jpg","roomid":xxx}//默认背景
{"cmd":"CHANGE_ROOM_INFO","background":"https://i0.hdslb.com/bfs/live/2388faed3728f3396052273ad4c3c9af21c411fc.jpg","roomid":xxx}//默认背景
```
----
### ROOM_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
标题更改/分区更改  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_CHANGE" |
| data		| obj	| |
#### ROOM_CHANGE__data
| key 7				| type	| value	|
|-|-|-|
| title				| str	| 房间标题 |
| area_id			| num	| 子分区ID |
| parent_area_id	| num	| 父分区ID |
| area_name			| str	| 子分区name |
| parent_area_name	| str	| 父分区name |
| live_key			| str	| 本次直播live_key ==> LIVE |
| sub_session_key	| str	| 本次直播sub_session_key ==> LIVE |
```json
{"cmd":"ROOM_CHANGE","data":{"title":"房间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"0","sub_session_key":""}}
{"cmd":"ROOM_CHANGE","data":{"title":"房间标题","area_id":0000,"parent_area_id":0000,"area_name":"xxx","parent_area_name":"xxx","live_key":"111111111111111111","sub_session_key":"111111111111111111sub_time:xxxxxxxxxx"}}
```
----
### OBS_SHIELD_STATUS_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RING_STATUS_CHANGE" "RING_STATUS_CHANGE_V2" |
| data		| obj	| |
#### RING_STATUS_CHANGE__data
| status		| num	| 0 / 1 |
| reserve_type	| num	| 0 / 1 |
```json
{"cmd":"RING_STATUS_CHANGE","data":{"status":0}}
{"cmd":"RING_STATUS_CHANGE","data":{"status":1}}
{"cmd":"RING_STATUS_CHANGE_V2","data":{"reserve_type":0,"status":0}}
{"cmd":"RING_STATUS_CHANGE_V2","data":{"reserve_type":0,"status":1}}
```
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
{"cmd":"VOICE_JOIN_LIST","data":{"apply_count":x,"category":1,"cmd":"","red_point":1,"refresh":1,"room_id":12345},"room_id":12345}
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
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"apply_count":xx,"cmd":"","notify_count":0,"red_point":1,"room_id":12345,"room_status":1,"root_status":1},"room_id":12345}
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"cmd":"","room_id":12345,"root_status":1,"room_status":1,"apply_count":xx,"notify_count":0,"red_point":1},"room_id":12345}
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"cmd":"","room_id":12345,"root_status":1,"room_status":1,"apply_count":xx,"notify_count":0,"red_point":0},"room_id":12345}
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"apply_count":xx,"cmd":"","notify_count":0,"red_point":1,"room_id":12345,"room_status":1,"root_status":1},"room_id":12345}
{"cmd":"VOICE_JOIN_ROOM_COUNT_INFO","data":{"apply_count":xx,"cmd":"","notify_count":0,"red_point":0,"room_id":12345,"room_status":1,"root_status":1},"room_id":12345}
```
----
### ROOM_SKIN_MSG
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key 10,11		| type	| value	|
|-|-|-|
| cmd			| str	| "ROOM_SKIN_MSG" |
| skin_id		| num	| |
| status		| num	| 0 / 1 |
| end_time		| num	| TimeStamp(秒) |
| current_time	| num	| 当前时间TimeStamp(秒) |
| only_local	| bool	| |
| ?scatter		| obj	| |
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
| ...		| ...	| ... |
```json
{"cmd":"ROOM_SKIN_MSG","skin_id":xxx,"status":0,"end_time":xxxxxxxxxx,"current_time":xxxxxxxxxx,"only_local":false}
{"cmd":"ROOM_SKIN_MSG","skin_id":xxx,"status":1,"end_time":xxxxxxxxxx,"current_time":xxxxxxxxxx,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.zip","md5":"xxx"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.zip","md5":"xxx"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.zip","md5":"xxx"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.zip","md5":"xxx","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.png","giftControlBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.png","rankListBgPic":"https://i0.hdslb.com/bfs/live/roomSkin/xxx.png","mainText":"#XXxxxxxx","normalText":"#XXxxxxxx","highlightContent":"#XXxxxxxx","border":"#XXxxxxxx"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":xxx,"status":1,"end_time":xxxxxxxxxx,"current_time":xxxxxxxxxx,"only_local":false,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","mainText":"#FFffffff","normalText":"#XXxxxxxx","highlightContent":"#XXxxxxxx","border":"#XXxxxxxx","buttonText":"#FFffffff"}}}}
{"cmd":"ROOM_SKIN_MSG","skin_id":xxx,"status":1,"end_time":xxxxxxxxxx,"current_time":xxxxxxxxxx,"only_local":true,"scatter":{"min":1,"max":200},"skin_config":{"android":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"ios":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"ipad":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx"}},"web":{"1":{"zip":"https://i0.hdslb.com/bfs/live/xxx.zip","md5":"xxx","platform":"web","version":"1","headInfoBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","giftControlBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","rankListBgPic":"https://i0.hdslb.com/bfs/live/xxx.jpg","mainText":"#FFffffff","normalText":"#XXxxxxxx","highlightContent":"#XXxxxxxx","border":"#XXxxxxxx","buttonText":"#FFffffff"}}}}
```
----
### LIVE_PANEL_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_PANEL_CHANGE" |
| data		| obj	| |
#### LIVE_PANEL_CHANGE__data
| key		| type	| value	|
|-|-|-|
| type		| num	| |
| scatter	| obj	| |
```json
{"cmd":"LIVE_PANEL_CHANGE","data":{"type":2,"scatter":{"max":150,"min":5}}}
{"cmd":"LIVE_PANEL_CHANGE","data":{"scatter":{"max":150,"min":5},"type":2}}
```
----
### RANK_REM
[TOP](#直播弹幕)  
文档更新：2024-07-24  
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
| time		| num	| 当前时间TimeStamp\(秒\) \(+10,+15,+20\) |
| uid		| num	| |
```json
//用户被禁言时触发
{"cmd":"RANK_REM","data":{"name":"online_gold","room_id":xxx,"ruid":xxx,"time":xxxxxxxxxx,"uid":xxx}}
{"cmd":"RANK_REM","data":{"name":"online_rank","room_id":xxx,"ruid":xxx,"time":xxxxxxxxxx,"uid":xxx}}
{"cmd":"RANK_REM","data":{"name":"daily_rank","room_id":xxx,"ruid":xxx,"time":xxxxxxxxxx,"uid":xxx}}
{"cmd":"RANK_REM","data":{"name":"weekly_rank","room_id":xxx,"ruid":xxx,"time":xxxxxxxxxx,"uid":xxx}}
{"cmd":"RANK_REM","data":{"name":"monthly_rank","room_id":xxx,"ruid":xxx,"time":xxxxxxxxxx,"uid":xxx}}
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
文档更新：2024-xx-xx  
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
| current_achievement_level		| num	| |
| dmscore						| num	| |
| event_type					| num	| |
| face							| str	| 主播头像URL |
| first_line_content			| str	| 恭喜主播<%xxx%> |
| first_line_highlight_color	| str	| #FFD432 |
| first_line_normal_color		| str	| #FFFFFF |
| headmap_url					| str	| |
| is_first						| bool	| |
| is_first_new					| bool	| |
| room_id						| num	| |
| second_line_content			| str	| 舰队规模突破<%xxx%> |
| second_line_highlight_color	| str	| "#06DDFF" |
| second_line_normal_color		| str	| "#FFFFFF" |
| show_time						| num	| |
| web_basemap_url				| str	| |
#### GUARD_ACHIEVEMENT_ROOM__anchor_modal
| key							| type	| value	|
|-|-|-|
| first_line_content			| str	| 恭喜当前舰队规模突破<%xxx%> |
| highlight_color				| str	| "#00DCFF" |
| second_line_content			| str	| 至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～ |
| show_time						| num	| 5 |
```json
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":99999,"event_type":1,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/c69db9cc9cecd7c2e93718a83a31d26e2234c35a.png","anchor_guard_achieve_level":1000,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%1000%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png","current_achievement_level":3,"dmscore":99999,"event_type":1,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"#FFD432","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/40862cd8245b1742bdc9f2b563fcae1335e6fa6c.png","is_first":true,"is_first_new":true,"room_id":12345,"second_line_content":"舰队规模突破<%1000%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/1f06adc9618a5b6d6b1ea5e4a6ec41fca919ca86.png"}}

{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":99999,"event_type":2,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":false,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":99999,"event_type":1,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"https://i0.hdslb.com/bfs/live/f873a04b1544d8f8bcc37fb2924ac9a2c2554031.png","anchor_guard_achieve_level":100,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%100%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":5},"app_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png","current_achievement_level":2,"dmscore":99999,"event_type":1,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"#F2AE09","first_line_normal_color":"#FFFFFF","headmap_url":"https://i0.hdslb.com/bfs/vc/071eb10548fe9bc482ff69331983d94192ce9507.png","is_first":true,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%100%>","second_line_highlight_color":"#06DDFF","second_line_normal_color":"#FFFFFF","show_time":3,"web_basemap_url":"https://i0.hdslb.com/bfs/live/83008812e86cae42049414e965d6ab6002f061cb.png"}}
{"cmd":"GUARD_ACHIEVEMENT_ROOM","data":{"anchor_basemap_url":"","anchor_guard_achieve_level":0,"anchor_modal":{"first_line_content":"恭喜当前舰队规模突破<%0%>","highlight_color":"#00DCFF","second_line_content":"至直播中心 - 获奖记录填写收货信息可获得实物勋章奖励哦～","show_time":0},"app_basemap_url":"","current_achievement_level":1,"dmscore":99999,"event_type":2,"face":"xxx","first_line_content":"恭喜主播<%xxx%>","first_line_highlight_color":"","first_line_normal_color":"","headmap_url":"","is_first":false,"is_first_new":false,"room_id":12345,"second_line_content":"舰队规模突破<%0%>","second_line_highlight_color":"","second_line_normal_color":"","show_time":3,"web_basemap_url":"普通无需图片"}}
```
----
### SHOPPING_BUBBLES_STYLE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
| checksum					| str			| md5("?") |
| bubbles_list				| null/\[+\]obj	| |
```json
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"bubbles_list":[{"goods_list":[],"name":"N个宝","priority":6,"show_banner":0,"tag":"goodsnum"},{"goods_list":[],"name":"快抢啊","priority":7,"show_banner":0,"tag":"onlyone"}],"checksum":"6f61ed5d5c2f4cab956ad947c9a63878","cycle_time":180,"goods_count":11,"interval_between_bubbles":10,"interval_between_queues":10}}
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":0,"checksum":"37a6259cc0c1dae299a7866489dff0bd","bubbles_list":null}}
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":2,"checksum":"c726710956d46417400c9b555c483588","bubbles_list":[{"tag":"onlyone","name":"快抢啊","priority":7,"show_banner":0,"goods_list":[]}]}}
{"cmd":"SHOPPING_BUBBLES_STYLE","data":{"interval_between_bubbles":10,"interval_between_queues":10,"cycle_time":180,"goods_count":23,"checksum":"c82846a125f8eff5afb65c2e532ec865","bubbles_list":[{"tag":"goodsnum","name":"N个宝","priority":6,"show_banner":0,"goods_list":[]},{"tag":"onlyone","name":"快抢啊","priority":7,"show_banner":0,"goods_list":[]}]}}
```
----
### GIFT_STAR_PROCESS
[TOP](#直播弹幕)  
文档更新：2024-11-11  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_STAR_PROCESS" |
| data		| obj	| |
#### GIFT_STAR_PROCESS__data
| key		| type	| value	|
|-|-|-|
| status	| num	| 1 / 2 |
| tip		| str	| |
```json
{"cmd":"GIFT_STAR_PROCESS","data":{"status":1,"tip":"XXX已点亮"}}
{"cmd":"GIFT_STAR_PROCESS","data":{"status":2,"tip":"所有星球已点亮"}}
```
----
### ANCHOR_NORMAL_NOTIFY
[TOP](#直播弹幕)  
文档更新：2024-11-01  
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
{"cmd":"ANCHOR_NORMAL_NOTIFY","data":{"type":1,"show_type":1,"info":{"icon":"https://i0.hdslb.com/bfs/live/f3ebd37ee59991bc45538be58e68a6d3aa43ccca.png","title":"","content":"恭喜，获得推荐位buff加持，上推荐的几率大大提高，持续时间：x小时。"}}}
{"cmd":"ANCHOR_NORMAL_NOTIFY","data":{"type":1,"show_type":1,"info":{"icon":"https://i0.hdslb.com/bfs/live/f3ebd37ee59991bc45538be58e68a6d3aa43ccca.png","title":"","content":"恭喜，获得推荐位buff加持，上推荐的几率大大提高，持续时间：x小时y分钟。"}}}
```
----
### LIVE_OPEN_PLATFORM_GAME
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_OPEN_PLATFORM_GAME" |
| data		| obj	| |
#### LIVE_OPEN_PLATFORM_GAME__data
| key						| type			| value	|
|-|-|-|
| msg_type					| str			| "panel_update"/"panel_reset"/"game_end" |
| msg_sub_type				| str			| "panel_update"/"panel_reset"/"game_end" |
| game_name					| str			| |
| game_code					| str			| |
| game_id					| str			| UUID |
| game_status				| str			| |
| game_msg					| str			| |
| game_conf					| str(obj)		| |
| interactive_panel_conf	| str			| |
| timestamp					| num			| 当前时间 TimeStamp(秒) |
| block_uids				| null/\[?\]	| |
----
### room_admin_entrance
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
设置房管  
| key	| type	| value	|
|-|-|-|
| cmd		| str	| "room_admin_entrance" |
| dmscore	| obj	| 15×n |
| level		| obj	| 1 |
| msg		| obj	| "系统提示：你已被主播设为房管" |
| uid		| obj	| uid |
```json
{"cmd":"room_admin_entrance","dmscore":45,"level":1,"msg":"系统提示：你已被主播设为房管","uid":xxx}
```
----
### ROOM_ADMINS
[TOP](#直播弹幕)  
文档更新：2024-xx-xx
| key		| type		| value	|
|-|-|-|
| cmd		| str		| "ROOM_ADMINS" |
| uids		| \[+\]num	| |
```json
{"cmd":"ROOM_ADMINS","uids":[1,2]}
```
----
### ROOM_ADMIN_REVOKE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
移除房管  
| key 6		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_ADMIN_REVOKE" |
| msg		| str	| "撤销房管" |
| uid		| num	| |
```json
{"cmd":"ROOM_ADMIN_REVOKE","msg":"撤销房管","uid":1}
```
----
### MVROLECHANGE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":0,"room_id":xxx,"ts":xxxxxxxxxx}}
{"cmd":"MVROLECHANGE","data":{"change_uid":xxx,"role":1,"room_id":xxx,"ts":xxxxxxxxxx}}
```
----
### VOICE_CHAT_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-06-01  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "VOICE_CHAT_UPDATE" |
| data	| obj	| |
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
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_GAIN_MEDAL" |
| data		| obj	| |
#### MESSAGEBOX_USER_GAIN_MEDAL__data
| key	| type	| value	|
|-|-|-|
| day_limit				| num	| 每日上限 1500 / 250000 |
| fan_name				| str	| 昵称 |
| guard_level			| num	| 0 |
| highlight_color		| num	| |
| intimacy				| num	| [粉丝勋章进度](#medal_score) |
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
| msg_content			| str	| "获得`x`点亲密度\n你的粉丝勋章达到`y`级" |
| msg_title				| str	| "恭喜你获得【`主播`】的粉丝勋章~" <br> "欢迎萌新~" |
| next_intimacy			| num	| 下一级所需经验 |
| normal_color			| num	| |
| toast					| str	| "成功入团并关注主播，得1级大礼包" <br> 大航海:"恭喜您加入`主播`的粉丝团，并获得1级大礼包" |
| today_feed			| num	| 0 |
| type					| num	| 0:xxx / 1:xxx / 2:欢迎萌新 / 3:获得粉丝勋章 |
| uid					| num	| |
| up_uid				| num	| 主播uid |
```json
{"cmd":"MESSAGEBOX_USER_GAIN_MEDAL","data":{"day_limit":1500,"fan_name":"xxx","guard_level":0,"highlight_color":xxx,"intimacy":xxx,"is_lighted":1,"is_received":1,"is_wear":0,"medal_color":xxx,"medal_color_border":xxx,"medal_color_end":xxx,"medal_color_start":xxx,"medal_id":xxx,"medal_level":3,"medal_name":"xxx","msg_content":"获得xxx点亲密度\n你的粉丝勋章达到xxx级","msg_title":"恭喜你获得【xxx】的粉丝勋章~","next_intimacy":xxx,"normal_color":xxx,"toast":"成功入团并关注主播，得1级大礼包","today_feed":xxx,"type":3,"uid":xxx,"up_uid":xxx}}
"恭喜你获得【xxx】的粉丝勋章~": 228,
"欢迎萌新~": 12,
"恭喜你获得【123456789ab...】的粉丝勋章~": 385,
"恭喜你获得【123456789...】的粉丝勋章~": 1

"成功入团并关注主播，得1级大礼包": 615,
"恭喜您加入xxx的粉丝团，并获得1级大礼包": 7,
"恭喜您加入xxxxxxxx...的粉丝团，并获得1级大礼包": 4

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
| r_uname			| str		| 昵称 |
| receive_user_info	| obj		| |
| receiver_uinfo	| obj		| [uinfo](#PUBLIC_uinfo) |
| ruid				| num		| |
| send_master		| null/ 	| |
| sender_uinfo		| obj		| [uinfo](#PUBLIC_uinfo) |
| total_num			| num		| |
| uid				| num		| |
| uname				| str		| 昵称 |
| wealth_level		| num		| |
```python
import hashlib
hashlib.md5().hexdigest()

combo_id       = ":".join(["batch","gift","combo_id",sender_uid,receiver_uid,gift_id,time.time():.4f])
batch_combo_id = ":".join(["batch","gift","combo_id",sender_uid,receiver_uid,gift_id,time.time():.4f])

enc_sender_uid = str(binascii.b2a_hex(bytes(str(sender_uid),"ascii")),"ascii")+"d41d8cd98f00b204e9800998ecf8427e"
```
```json
// empty md5:d41d8cd98f00b204e9800998ecf8427e
{
	"cmd":"COMBO_SEND",
	"data":{
		"action":"投喂",
		"batch_combo_id":"batch:gift:combo_id:11111:22222:33333:DDDD.dddd",
		"batch_combo_id":"batch:gift:combo_id:31383333353835323733d41d8cd98f00b204e9800998ecf8427e:22222:33333:DDDD.dddd",
		"batch_combo_num":xxx,
		"coin_type":"gold",
		"combo_id":"gift:combo_id:11111:22222:33333:EEEE.eeee",
		"combo_id":"gift:combo_id:31383333353835323733d41d8cd98f00b204e9800998ecf8427e:22222:33333:EEEE.eeee",
		"combo_num":xxx,
		"combo_total_coin":xxx,
		"dmscore":xxx,
		"gift_id":33333,
		"gift_name":"xxx",
		"gift_num":0,
		"group_medal":null,
		"is_join_receiver":false,
		"is_naming":false,
		"is_show":1,
		"medal_info":...,
		"name_color":"",
		"r_uname":"xxx",
		"receive_user_info":{"uid":22222,"uname":"xxx"},
		"receiver_uinfo":...,
		"ruid":22222,
		"send_master":null,
		"sender_uinfo":...,
		"total_num":...,
		"uid":11111,
		"uname":"yyy",
		"wealth_level":1
	}
}
```
----
### COMBO_END
[TOP](#直播弹幕)  
文档更新：2024-04-30  
| key				| type	| value	|
|-|-|-|
| cmd				| str	| "COMBO_SEND" |
| data				| obj	| |
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
| r_uname			| str	| 昵称 |
| ruid				| num	| |
| send_master		| null	| |
| start_time		| num	| |
| uid				| num	| |
| uname				| str	| 昵称 |
```json
{"cmd":"COMBO_END","data":{"action":"投喂","batch_combo_num":1,"combo_num":1,"combo_total_coin":100,"end_time":AAA,"gift_id":31036,"gift_name":"小花花","gift_num":1,"guard_level":0,"name_color":"","price":100,"r_uname":"xxx","ruid":xxx,"send_master":null,"start_time":AAA,"uid":YYY,"uname":"YYY"}}
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
```
----
### ADMIN_SHIELD_KEYWORD
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
房管: 全局屏蔽字符串  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ADMIN_SHIELD_KEYWORD" |
| data		| obj	| |
#### ADMIN_SHIELD_KEYWORD__data
| key		| type	| value	|
|-|-|-|
| action	| num	| |
| keyword	| str	| |
| name		| str	| |
| uid		| num	| |
```json
{"cmd":"ADMIN_SHIELD_KEYWORD","data":{"action":0,"keyword":"text","name":"username","uid":1}}
{"cmd":"ADMIN_SHIELD_KEYWORD","data":{"action":1,"keyword":"text","name":"username","uid":1}}
```
----
### ANCHOR_HELPER_DANMU
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key				| type	| value	|
|-|-|-|
| cmd				| str	| "ANCHOR_HELPER_DANMU" |
| data				| obj	| |
#### ANCHOR_HELPER_DANMU__data
| key				| type	| value	|
|-|-|-|
| button_label		| num	| |
| button_name		| str	| |
| button_platform	| num	| |
| button_target		| str	| |
| msg				| str	| |
| platform			| num	| |
| report			| str	| |
| report_type		| str	| |
| sender			| str	| |
#### ANCHOR_HELPER_DANMU__list
| id | value |
|-|-|
|101029|新主播扶持规则|
|100855|航海回馈说明页面|
|||
```json
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"","button_platform":0,"button_target":"","msg":"xxx取消了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看>","button_platform":3,"button_target":"bililive://xxxx","msg":"发起航海回馈更容易吸引粉丝开通大航海哦","platform":3,"report":"$uid","report_type":"live.live.guard","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"查看规则","button_platform":3,"button_target":"bililive://xxxx","msg":"您正在新主播扶持中，良好的互动和直播封面，会帮你吸引观众","platform":3,"report":"$uid","report_type":"star_perception","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去看看","button_platform":3,"button_target":"bililive://xxxx","msg":"本周开播满7有效天，必得xxx元奖励金！今天再收到xxx电池，即可+1天哦","platform":3,"report":"$uid","report_type":"weekly_task","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":0,"button_name":"去领取","button_platform":3,"button_target":"bililive://xxxx","msg":"本周开播满1天，恭喜获得xxx元奖励金。再播1天，再得xxx元奖励金","platform":3,"report":"$uid","report_type":"weekly_task_finish","sender":"直播小助手"}}
{"cmd":"ANCHOR_HELPER_DANMU","data":{"button_label":1,"button_name":"去看看","button_platform":3,"button_target":"bililive://blink/open_voicelink","msg":"xxx申请了语音连麦","platform":3,"report":"","report_type":"","sender":"直播小助手"}}
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
### USER_PANEL_RED_ALARM
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_PANEL_RED_ALARM" |
| data		| obj	| |
#### USER_PANEL_RED_ALARM__data
| key		| type	| value	|
|-|-|-|
| alarm_num	| num	| 0/1 |
| module	| str	| |
```json
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":x,"module":"live_guard"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":x,"module":"room_gift_panel"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":x,"module":"panel_bag"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":x,"module":"panel_privilege"}}
{"cmd":"USER_PANEL_RED_ALARM","data":{"alarm_num":x,"module":"user_head_dot"}}
```
----
### USER_INFO_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
文档更新：2024-11-xx  
粉丝牌升级  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MESSAGEBOX_USER_MEDAL_CHANGE" |
| data		| obj	| |
#### MESSAGEBOX_USER_MEDAL_CHANGE__data
| key					| type		| value	|
|-|-|-|
| type					| num		| |
| uid					| num		| |
| up_uid				| num		| |
| medal_level			| num		| |
| medal_name			| str		| |
| medal_color_start		| num		| |
| medal_color_end		| num		| |
| medal_color_border	| num		| |
| is_lighted			| num		| |
| is_lighted_v2			| bool		| |
| guard_level			| num		| |
| unlock				| num		| |
| unlock_level			| num		| |
| multi_unlock_level	| str		| |
| upper_bound_content	| str		| |
| uinfo_medal			| obj		| |
| effect_id				| num		| |
```json
{"cmd":"MESSAGEBOX_USER_MEDAL_CHANGE","data":{"type":1,"uid":xxx,"up_uid":xxx,"medal_level":xxx,"medal_name":"粉丝团","medal_color_start":xxx,"medal_color_end":xxx,"medal_color_border":xxx,"is_lighted":1,"is_lighted_v2":true,"guard_level":0,"unlock":0,"unlock_level":0,"multi_unlock_level":"","upper_bound_content":"恭喜你的粉丝勋章【粉丝团】升到xxx级","uinfo_medal":{"name":"粉丝团","level":xxx,"color_start":xxx,"color_end":xxx,"color_border":xxx,"color":0,"id":0,"typ":0,"is_light":1,"ruid":xxx,"guard_level":0,"score":0,"guard_icon":"","honor_icon":"","v2_medal_color_start":"#xxx","v2_medal_color_end":"#xxx","v2_medal_color_border":"#xxx","v2_medal_color_text":"#xxx","v2_medal_color_level":"#xxx","user_receive_count":0},"effect_id":xxx}}
```
----
### WEALTH_NOTIFY
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WEALTH_NOTIFY" |
| data		| obj	| |
#### WEALTH_NOTIFY__data
| key				| type	| value	|
|-|-|-|
| flag				| num	| |
| info				| obj	| |
#### WEALTH_NOTIFY__data__info
| key				| type	| value	|
|-|-|-|
| effect_key		| num	| |
| has_items_changed	| num	| |
| level				| num	| |
| send_time			| num	| |
| status			| num	| |
```json
{"cmd":"WEALTH_NOTIFY","data":{"flag":3,"info":{"effect_key":1075,"has_items_changed":1,"level":xx,"send_time":xxx,"status":1}}}
{"cmd":"WEALTH_NOTIFY","data":{"flag":3,"info":{"effect_key":1076,"has_items_changed":1,"level":xx,"send_time":xxx,"status":1}}}
```
----
### ACTIVITY_BANNER_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ACTIVITY_BANNER_CHANGE/ACTIVITY_BANNER_CHANGE_V2" |
| data		| obj	| |
#### ACTIVITY_BANNER_CHANGE__data
| key		| type		| value	| 备注 |
|-|-|-|-|
| timestamp	| num		| | V2
| list		| \[1\]obj	| |
#### ACTIVITY_BANNER_CHANGE__data__list
| key 10,11			| type		| value	| 备注 |
|-|-|-|-|
| id				| num		| |
| timestamp			| num		| | not V2
| position			| str		| |
| type				| num		| |
| activity_title	| str		| |
| cover				| str		| |
| jump_url			| str		| |
| is_close			| num		| |
| action			| str		| |
| platform_info		| \[\]obj	| | V2
| ext_data			| str		| | V2
```json
{"cmd":"ACTIVITY_BANNER_CHANGE",   "data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png",              "id":3065,"is_close":1,"jump_url":"https://www.xxx.com/blackboard/live/activity-qMxJDCQ4kQ.html","position":"bottom","timestamp":xxxxxxxxxx}]}}
{"cmd":"ACTIVITY_BANNER_CHANGE_V2","data":{"list":[{"action":"update","activity_title":"虚拟-三相交流电","cover":"https://i0.hdslb.com/bfs/live/94fcd27cc98ab78eaba5efe40d0e29568018686d.png","ext_data":"","id":3065,"is_close":1,"jump_url":"https://www.xxx.com/blackboard/live/activity-qMxJDCQ4kQ.html","platform_info":[{"build":0,"condition":0,"platform":"android"},{"build":0,"condition":0,"platform":"ios"}],"position":"bottom","type":0}],"timestamp":xxxxxxxxxx}}
```
----
### SPREAD_SHOW_FEET_V2
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxx,"order_type":5,"plan_percent":xxx,"show":xxx,"status":1,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"","order_id":xxx,"order_type":5,"plan_percent":xxx,"show":xxx,"status":2,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxx,"order_type":2,"plan_percent":xxx,"show":xxx,"status":1,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxx,"order_type":3,"plan_percent":xxx,"show":xxx,"status":1,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxx,"order_type":3,"plan_percent":xxx,"show":xxx,"status":2,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
{"cmd":"SPREAD_SHOW_FEET_V2","data":{"click":xxx,"coin_cost":xxx,"coin_num":xxx,"cover_btn":"","cover_url":"","live_key":"xxx","order_id":xxx,"order_type":2,"plan_percent":xxx,"show":xxx,"status":2,"timestamp":xxx,"title":"流量包推广","total_online":xxx,"uid":xxx}}
```
----
### PLAYTOGETHER_ICON_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-11-11  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PLAYTOGETHER_ICON_CHANGE" |
| data		| obj	| |
#### PLAYTOGETHER_ICON_CHANGE__data
| key			| type	| value	|
|-|-|-|
| area_id		| num	| |
| has_perm		| num	| 0 / 1 |
| show_count	| num	| |
```json
{"cmd":"PLAYTOGETHER_ICON_CHANGE","data":{"area_id":xxx,"has_perm":0,"show_count":0}}
{"cmd":"PLAYTOGETHER_ICON_CHANGE","data":{"area_id":xxx,"has_perm":1,"show_count":0}}
```
----
### STUDIO_ROOM_CLOSE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "STUDIO_ROOM_CLOSE" |
| msg		| str	| |
| roomid	| str	| |
```json
{"cmd":"STUDIO_ROOM_CLOSE","msg":"演播厅模式已关闭，重新开播即可进入正常模式","roomid":"xxx",}
```
----
### MULTI_VOICE_STATUS_SYNC_ANCHOR
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_STATUS_SYNC_ANCHOR" |
| data		| obj	| |
#### MULTI_VOICE_STATUS_SYNC_ANCHOR__data
| key				| type		| value	|
|-|-|-|
| info				| str(json)	| |
#### MULTI_VOICE_STATUS_SYNC_ANCHOR__data__info
| key				| type		| value	|
|-|-|-|
| muteFromUID		| num		| |
| isMute			| num		| 0 / 1 |
| uid				| num		| |
| muteTrueOperator	| num		| 开启禁言操作者 |
| ?auth				| num		| |
| ?adminSign		| str		| 256bit |
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
文档更新：2024-xx-xx  
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
| ?hat							| null/xxx	| |
| ?pk_group_total_price			| num		| |
| ?pk_group_total_price_text	| str		| |
| ?pk_group_id					| str		| |
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
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"pk_group_id":"xxx","pk_group_total_price":xxx,"pk_group_total_price_text":"xxx","pk_total_price":xxx,"pk_total_price_text":"xxx","position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx}}
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"pk_group_total_price_text":"xxx","pk_total_price_text":"xxx","position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx}}
{"cmd":"MULTI_VOICE_OPERATIN","data":{"battle_info":null,"hat":null,"position":xxx,"room_id":xxx,"total_price":xxx,"total_price_text":"xxx","ts":xxx,"uid":xxx,"version":xxx}}
```
---
### MULTI_VOICE_ENTER_ANCHOR
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
{"cmd":"MULTI_VOICE_ENTER_ANCHOR","data":{"actual_position":xxx,"anchor_uid":xxx,"avatar":"xxx","gender":xxx,"nickname":"xxx","role":xxx,"uid":xxx,"version":xxx,"want_position":xxx}}
```
---
### MULTI_VOICE_OWNER_LEAVE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "MULTI_VOICE_OWNER_LEAVE" |
| data		| obj	| |
#### MULTI_VOICE_OWNER_LEAVE__data
| key		| type	| value	|
|-|-|-|
| toast		| str	| |
```json
{"cmd":"MULTI_VOICE_OWNER_LEAVE","data":{"toast":"主播网络异常"}}
```
---
### MULTI_VOICE_PK_STATUS
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
### SPREAD_ORDER
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_BROADCAST" |
| data		| obj	| |
#### ANCHOR_BROADCAST__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ANCHOR_BROADCAST","data":{"button_info":{"blink_button_extra":"","blink_button_label":0,"blink_button_target":"","blink_button_type":"","button_name":"","hime_button_extra":"","hime_button_h5_type":"","hime_button_label":0,"hime_button_target":"","hime_button_type":""},"milestone_index":9,"milestone_type":"session_livetime","milestone_value":16800,"msg":"恭喜你，开播时长达到280分钟！","platform":0,"sender":"直播小助手"}}
{"cmd":"ANCHOR_BROADCAST","data":{"button_info":{"blink_button_extra":"","blink_button_label":0,"blink_button_target":"","blink_button_type":"","button_name":"","hime_button_extra":"","hime_button_h5_type":"","hime_button_label":0,"hime_button_target":"","hime_button_type":""},"milestone_index":10,"milestone_type":"session_livetime","milestone_value":18000,"msg":"恭喜你，开播时长达到300分钟！","platform":0,"sender":"直播小助手"}}
{"cmd":"ANCHOR_BROADCAST","data":{"button_info":{"blink_button_extra":"","blink_button_label":0,"blink_button_target":"","blink_button_type":"","button_name":"","hime_button_extra":"","hime_button_h5_type":"","hime_button_label":0,"hime_button_target":"","hime_button_type":""},"milestone_index":11,"milestone_type":"session_livetime","milestone_value":21600,"msg":"恭喜你，开播时长达到360分钟！","platform":0,"sender":"直播小助手"}}
{"cmd":"ANCHOR_BROADCAST","data":{"button_info":{"blink_button_extra":"","blink_button_label":0,"blink_button_target":"","blink_button_type":"","button_name":"","hime_button_extra":"","hime_button_h5_type":"","hime_button_label":0,"hime_button_target":"","hime_button_type":""},"milestone_index":14,"milestone_type":"session_livetime","milestone_value":30000,"msg":"恭喜你，开播时长达到500分钟！","platform":0,"sender":"直播小助手"}}
```
---
### ROOM_NEWS_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
{"cmd":"ROOM_NEWS_UPDATE","data":{"content_is_open":true,"icon":"https://i0.hdslb.com/bfs/live/7502ba91c9564454d785a1d2dcc5151556f7678c.png","news_content":"xxx\nxxx","news_page":"","news_type":2}}
{"cmd":"ROOM_NEWS_UPDATE","data":{"content_is_open":true,"icon":"https://i0.hdslb.com/bfs/live/7502ba91c9564454d785a1d2dcc5151556f7678c.png","news_content":"xxx","news_page":"","news_type":1}}
```
---
### MULTI_VOICE_APPLICATION_ANCHOR
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
文档更新：2024-xx-xx  
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
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_BOARD_RED_DOT" |
| data		| obj	| |
#### GIFT_BOARD_RED_DOT__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"GIFT_BOARD_RED_DOT","data":{"categoryL1":"3"}}
```
---
### LITTLE_MESSAGE_BOX
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
文档更新：2024-xx-xx  
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
{"cmd":"ROOM_NEWS_AUDIT_CHANGE","data":{"audit_status":1,"news_content":"xxx","news_type":2,"room_id":xxx}}
```
---
### LIVE_ROOM_TOAST_MESSAGE
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_ROOM_TOAST_MESSAGE" |
| timestamp	| num	| |
| data		| obj	| |
#### LIVE_ROOM_TOAST_MESSAGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"LIVE_ROOM_TOAST_MESSAGE","data":{"message":"由于对方主播提前结束PK，本轮PK我方主播获胜","timestamp":xxx},"timestamp":xxx}
{"cmd":"LIVE_ROOM_TOAST_MESSAGE","timestamp":xxx,"data":{"timestamp":xxx,"message":"对方主播结束了视频连线"}}
```
---
---
### LIVE_PANEL_CHANGE_CONTENT
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
			{"biz_id":1012,"icon":"http://i0.hdslb.com/bfs/live/1e3cb35056ebbcc1af5f08f4fe7916f095db26a5.png","title":"管理员","note":"管理员","weight":36,"status_type":1,"notification":null,"custom":null,"jump_url":"https://live.xxx.com/p/html/live-app-room-admin/index.html?is_live_half_webview=1#/roomManagement","type_id":1,"tab":null,"dynamic_icon":"","sub_icon":"","panel_icon":"https://i0.hdslb.com/bfs/live/98e692836d408ab7f2b321c717e866a8fd9b3bfd.png","match_entrance":0,"icon_info":null},
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
			{"biz_id":999,"icon":"https://i0.hdslb.com/bfs/live/6c068a5ec8e316ca1b3c9a97ba8e47707b3a0fc8.png","title":" 魔法奇遇","note":"魔法奇遇","weight":1,"status_type":1,"notification":null,"custom":[{"icon":"https://i0.hdslb.com/bfs/live/6c068a5ec8e316ca1b3c9a97ba8e47707b3a0fc8.png","title":"魔法奇遇","note":"魔法奇遇","jump_url":"https://live.xxx.com/activity/live-activity-full/full-next/index.html?app_name=magical_adventure&-Abrowser=live&is_live_half_webview=1&source_event=1&hybrid_half_ui=1,3,100p,80p,0,0,30,100,15,0;2,2,375,100p,0,0,30,100,15,0;3,3,100p,80p,0,0,30,100,15,0;4,2,375,100p,0,0,30,100,15,0;5,3,100p,80p,0,0,30,100,15,0;6,3,100p,80p,0,0,30,100,15,0;7,3,100p,80p,0,0,30,100,15,0;8,3,100p,80p,0,0,30,100,15,0&room_id=5440&uid=9617619#/","status":0,"sub_icon":"https://i0.hdslb.com/bfs/live/a21478ac7eba92d69ddc7655666083d03756a683.png"}],"jump_url":"https://live.xxx.com/activity/live-activity-full/full-next/index.html?app_name=magical_adventure&-Abrowser=live&is_live_half_webview=1&source_event=1&hybrid_half_ui=1,3,100p,80p,0,0,30,100,15,0;2,2,375,100p,0,0,30,100,15,0;3,3,100p,80p,0,0,30,100,15,0;4,2,375,100p,0,0,30,100,15,0;5,3,100p,80p,0,0,30,100,15,0;6,3,100p,80p,0,0,30,100,15,0;7,3,100p,80p,0,0,30,100,15,0;8,3,100p,80p,0,0,30,100,15,0&room_id=5440&uid=9617619#/","type_id":2,"tab":{"type":"H5","biz_type":"common-H5","tab_comment":null,"tab_topic":null,"aggregation":0,"id":0,"sub_title":"","sub_icon":"","show_outer_aggregation":0,"show_guide_bubble":"","global_id":"","biz_info":""},"dynamic_icon":"","sub_icon":"https://i0.hdslb.com/bfs/live/a21478ac7eba92d69ddc7655666083d03756a683.png","panel_icon":"http://i0.hdslb.com/bfs/live/c339a3569df7351406f29afae77a917aec3073a3.png","match_entrance":0,"icon_info":null}
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
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GIFT_PANEL_PLAN" |
| data		| obj	| |
#### GIFT_PANEL_PLAN__data
| key				| type			| value	|
|-|-|-|
| gift_list			| \[\]obj		| |
| special_type_sort	| null/\[\]num	| |
| action			| num			| |
#### GIFT_PANEL_PLAN__data__gift_list
| key				| type		| value	|
|-|-|-|
| gift_id			| num			| |
| config			| null/obj		| |
| full_sc_effect	| null/\[1\]obj	| |
| float_sc_effect	| null			| |
| special_type		| num			| |
| show				| bool			| |
#### GIFT_PANEL_PLAN__data__gift_list__config
| key					| type		| value	|
|-|-|-|
| id						| num	| |
| name						| str		| |
| price						| num		| |
| type						| num		| |
| coin_type					| str		| |
| bag_gift					| num		| |
| effect					| num		| |
| corner_mark				| str		| |
| corner_background			| str		| |
| broadcast					| num		| |
| draw						| num		| |
| stay_time					| num		| |
| animation_frame_num		| num		| |
| desc						| str		| |
| rule						| str		| |
| rights					| str		| |
| privilege_required		| num		| |
| count_map					| \[1\]obj	| |
| img_basic					| str		| |
| img_dynamic				| str		| |
| frame_animation			| str		| |
| gif						| str		| |
| webp						| str		| |
| full_sc_web				| str		| |
| full_sc_horizontal		| str		| |
| full_sc_vertical			| str		| |
| full_sc_horizontal_svga	| str		| |
| full_sc_vertical_svga		| str		| |
| bullet_head				| str		| |
| bullet_tail				| str		| |
| limit_interval			| num		| |
| bind_ruid					| num		| |
| bind_roomid				| num		| |
| gift_type					| num		| |
| combo_resources_id		| num		| |
| max_send_limit			| num		| |
| weight					| num		| |
| goods_id					| num		| |
| has_imaged_gift			| num		| |
| left_corner_text			| str		| |
| left_corner_background	| str		| |
| gift_banner				| null/xxx	| |
| diy_count_map				| num		| |
| effect_id					| num		| |
| first_tips				| str		| |
| gift_attrs				| \[1\]num	| |
| corner_mark_color			| str		| |
| corner_color_bg			| str		| |
| web_light					| obj		| |
| web_dark					| obj		| |
#### GIFT_PANEL_PLAN__data__gift_list__config__count_map
| key						| type	| value	|
|-|-|-|
| num						| num	| |
| text						| str	| |
| desc						| str	| |
| web_svga					| str	| |
| vertical_svga				| str	| |
| horizontal_svga			| str	| |
| special_color				| str	| |
| effect_id					| num	| |
#### GIFT_PANEL_PLAN__data__gift_list__config__web_light+web_dark
| key						| type	| value	|
|-|-|-|
| corner_mark				| str	| |
| corner_background			| str	| |
| corner_mark_color			| str	| |
| corner_color_bg			| str	| |
#### GIFT_PANEL_PLAN__data__gift_list__full_sc_effect
| key						| type	| value	|
|-|-|-|
| type						| num	| |
| web_svga					| str	| |
| horizontal_svga			| str	| |
| vertical_svga				| str	| |
| web_mp4					| str	| |
| web_mp4_json				| str	| |
| horizontal_mp4			| str	| |
| vertical_mp4				| str	| |
| id						| num	| |
| plan_platform				| list	| |
| bind_gift_ids				| list	| |
| web_mp4_md5				| str	| |
| horizontal_mp4_md5		| str	| |
| vertical_mp4_md5			| str	| |
| web_mp4_crc32				| num	| |
| horizontal_mp4_crc32		| num	| |
| vertical_mp4_crc32		| num	| |
| web_mp4_file_size			| num	| |
| horizontal_mp4_file_size	| num	| |
| vertical_mp4_file_size	| num	| |
| h265_conf					| obj	| |
```json
{"cmd":"GIFT_PANEL_PLAN","data":{"action":2,"gift_list":[{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31482,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31569,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31570,"show":false,"special_type":6},{"config":null,"float_sc_effect":null,"full_sc_effect":null,"gift_id":31646,"show":false,"special_type":6}],"special_type_sort":null}}
{"cmd":"GIFT_PANEL_PLAN","data":{"gift_list":[{"gift_id":32328,"config":{"id":32328,"name":"蛋糕精灵","price":298000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"化身为蛋糕精灵——在这一刻，主播只被你守护 ᕦ(￣︶￣)ᕤ","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/44b7b59df3d96f51bbdae937beeae9a20d65e080.png","gif":"https://i0.hdslb.com/bfs/open-live/5c761375cbb5ca3f4a974175ac57f5ee707e8f94.gif","webp":"https://i0.hdslb.com/bfs/open-live/b1ddb10efde313428a23a261a42f66f03fd07bb5.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":671,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32329,"config":{"id":32329,"name":"合影留念","price":48000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"告别千篇一律，留下只属于你和主播的专属回忆 (〃'▽'〃)","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/875c9faeacd9c3196cc94b147a71c14b67ab162e.png","gif":"https://i0.hdslb.com/bfs/open-live/a26d41a96f8ec21a73dc5829ff9daba76e1c745f.gif","webp":"https://i0.hdslb.com/bfs/open-live/f9de197ab1b6cc2d57b13afe4df285188eb72da3.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":4166,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32330,"config":{"id":32330,"name":"派对礼花","price":5000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"空降主播派对趴，用礼花送上美好的祝愿 (╭￣3￣)╭♡","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/fdb3ab2b194c2d7118c9c5ed6d86c37444b050d9.png","gif":"https://i0.hdslb.com/bfs/open-live/ee26062b1a9478b74a9370bb0407b1874adb4e01.gif","webp":"https://i0.hdslb.com/bfs/open-live/27368fa715d29378975ce51357e29ec9c0610f59.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":5000,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32843,"config":{"id":32843,"name":"3D星愿水晶球","price":100000,"type":0,"coin_type":"gold","bag_gift":0,"effect":0,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"3D星愿水晶球，虚拟星球特供","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":10,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":100,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0},{"num":520,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/798c45282f966dab28257eb25a4292d3c0536198.png","gif":"https://i0.hdslb.com/bfs/open-live/8554386857bbcfe5ae55166efabc2c43efdbf571.gif","webp":"https://i0.hdslb.com/bfs/open-live/f7aca02c29236696a01495920f96c801627ed3c0.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":2000,"weight":1,"goods_id":168,"has_imaged_gift":0,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":1,"effect_id":0,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":true},{"gift_id":32331,"config":{"id":32331,"name":"星辰大海","price":799000,"type":0,"coin_type":"gold","bag_gift":0,"effect":2,"corner_mark":"","corner_background":"","broadcast":0,"draw":0,"stay_time":3,"animation_frame_num":1,"desc":"将主播传送到星辰大海浪漫时空中","rule":"","rights":"","privilege_required":0,"count_map":[{"num":1,"text":"","desc":"","web_svga":"","vertical_svga":"","horizontal_svga":"","special_color":"","effect_id":0}],"img_basic":"https://s1.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","img_dynamic":"https://i0.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","frame_animation":"https://i0.hdslb.com/bfs/open-live/ecf06ae35eddfb9bedd7e19b535d024cb57c9cd9.png","gif":"https://i0.hdslb.com/bfs/open-live/05fdb6f71132183f270964eb1c953e4360341ad9.gif","webp":"https://i0.hdslb.com/bfs/open-live/5a7af91676d2312d9775c69ff85b5b9fbf00a4a0.webp","full_sc_web":"","full_sc_horizontal":"","full_sc_vertical":"","full_sc_horizontal_svga":"","full_sc_vertical_svga":"","bullet_head":"","bullet_tail":"","limit_interval":0,"bind_ruid":0,"bind_roomid":0,"gift_type":8,"combo_resources_id":0,"max_send_limit":250,"weight":1,"goods_id":168,"has_imaged_gift":1,"left_corner_text":"","left_corner_background":"","gift_banner":null,"diy_count_map":0,"effect_id":794,"first_tips":"","gift_attrs":[0],"corner_mark_color":"","corner_color_bg":"","web_light":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""},"web_dark":{"corner_mark":"","corner_background":"","corner_mark_color":"","corner_color_bg":""}},"full_sc_effect":[{"type":1,"web_svga":"","horizontal_svga":"","vertical_svga":"","web_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","web_mp4_json":"https://i0.hdslb.com/bfs/live/a728510a3bc7ba2de94b07553f5c1b729b1f7aa4.json","horizontal_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","vertical_mp4":"https://i0.hdslb.com/bfs/live/b9e4e57d45afb83319ba9e92f693907092d80f36.mp4","id":794,"plan_platform":[1,2],"bind_gift_ids":[32331],"web_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","horizontal_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","vertical_mp4_md5":"6fa5395472fac1e10ff2b9f469fda5b7","web_mp4_crc32":564792465,"horizontal_mp4_crc32":564792465,"vertical_mp4_crc32":564792465,"web_mp4_file_size":1474735,"horizontal_mp4_file_size":1474735,"vertical_mp4_file_size":1474735,"h265_conf":{"horizontal_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/b27955fa707fcd0725394bc123310fe8295b3783.mp4","mp4_md5":"1570c241a73bd6903e3395e8cd392402","mp4_json":"","mp4_crc32":518022192,"mp4_file_size":630404},"vertical_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/b27955fa707fcd0725394bc123310fe8295b3783.mp4","mp4_md5":"1570c241a73bd6903e3395e8cd392402","mp4_json":"","mp4_crc32":518022192,"mp4_file_size":630404}}}],"float_sc_effect":null,"special_type":6,"show":true}],"special_type_sort":[12,14,13,13,13,13,13,13,5,6,7,8,9],"action":1}}
{"cmd":"GIFT_PANEL_PLAN","data":{"gift_list":[{"gift_id":32328,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32329,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32330,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32843,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false},{"gift_id":32331,"config":null,"full_sc_effect":null,"float_sc_effect":null,"special_type":6,"show":false}],"special_type_sort":null,"action":2}}
```
---
### ROOM_LOCK
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
封禁直播间  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_LOCK" |
| expire	| str	| UTC+8 |
| roomid	| num	| |
```json
{"cmd":"ROOM_LOCK","expire":"yyyy-mm-dd hh:mm:ss","roomid":xxx}
```
---
### OFFICIAL_ROOM_EVENT
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OFFICIAL_ROOM_EVENT" |
| data		| obj	| |
#### OFFICIAL_ROOM_EVENT__data
| key					| type	| value	|
|-|-|-|
| event_type			| num	| |
| room_id				| num	| |
| official_room_id		| num	| |
| official_anchor_id	| num	| |
| countdown				| num	| |
| scatter_time			| num	| |
| sub_title				| str	| |
| desc					| str	| |
| official_base_info	| obj	| |
| current_room_status	| num	| |
#### OFFICIAL_ROOM_EVENT__data
| key			| type	| value	|
| uid			| num	| |
| title			| str	| |
| uname			| str	| |
| face			| str	| |
| gender		| str	| |
| official_info | obj	| |
```json
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":2,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 开始表演","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":3}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":3,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":0,"scatter_time":3,"sub_title":"","desc":"","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":4,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 节目单表演结束","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":5,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":9,"scatter_time":3,"sub_title":"","desc":"s后 节目单表演结束","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":1}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":7,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":0,"scatter_time":3,"sub_title":"","desc":"","official_base_info":{"uid":441666939,"title":"bilibiliVUP 虚拟之城！","uname":"虚拟区高级运营_Official","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":2}}
{"cmd":"OFFICIAL_ROOM_EVENT","data":{"event_type":2,"room_id":5440,"official_room_id":21496316,"official_anchor_id":441666939,"countdown":30,"scatter_time":3,"sub_title":"","desc":"s后 开始表演","official_base_info":{"uid":441666939,"title":" 冰火歌会2024远航季 正在直播","uname":"虚拟区官方频道","face":"xxx","gender":"保密","official_info":{"role":3,"title":"直播虚拟区官方账号","desc":"","type":1}},"current_room_status":3}}
```
---
### BENEFIT_CARD_CLEAN
[TOP](#直播弹幕)  
文档更新：2024-xx-xx  
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
### LIVE_MULTI_VIEW_NEW_INFO
[TOP](#直播弹幕)  
文档更新：2024-11-01  
直播多视角  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_MULTI_VIEW_NEW_INFO" |
| data		| obj	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data
| key 12			| type		| value	|
|-|-|-|
| title				| str		| |
| room_id			| num		| |
| copy_writing		| str		| |
| bg_image			| str		| |
| sub_slt_color		| str		| |
| sub_bg_color		| str		| |
| sub_text_color	| str		| |
| view_type			| num		| |
| room_list			| \[+\]obj	| |
| relation_view		| \[+\]obj	| |
| view_pattern		| num		| |
| gather_room_list	| \[+\]obj	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__room_list
| key 5			| type	| value	|
|-|-|-|
| order_id		| num	| |
| room_id		| num	| |
| room_name		| str	| (手填) |
| live_status	| num	| |
| jump_url		| str	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__relation_view
| key 20			| type		| value	|
|-|-|-|
| order_id			| num		| |
| view_type			| num		| 0:直播间 / 1:视频 |
| view_id			| num		| 直播间ID / avid |
| view_name			| str		| 视角名称(手填) |
| title				| str		| 直播间标题 / 视频标题 |
| cover				| str		| 直播间封面 / 视频封面 |
| jump_url			| str		| |
| switch			| bool		| 是否可见 |
| num				| num		| 观看人数 [WATCHED_CHANGE](#WATCHED_CHANGE) |
| watch_icon		| str		| |
| live_status		| num		| |
| text_small		| str		| 观看人数 [WATCHED_CHANGE](#WATCHED_CHANGE) |
| use_view_vt		| bool		| |
| anchor_face		| str		| |
| match_live_room	| bool		| |
| match_info		| null/obj	| ^ |
| duration			| num		| 0 / 视频时长(秒) |
| up_name			| str		| |
| pub_date			| str		| "" / 视频投稿时间 "M-dd" |
| gather_id			| num		| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__gather_room_list
| key 6				| type	| value	|
|-|-|-|
| order_id			| num	| |
| gather_title		| str	| |
| exposure_mode		| num	| |
| icon				| str	| |
| gather_id			| num	| |
| gather_type		| num	| |
#### LIVE_MULTI_VIEW_NEW_INFO__data__relation_view__match_info
| key 7				| type	| value	|
|-|-|-|
| match_status		| num	| |
| home_team_name	| str	| |
| away_team_name	| str	| |
| home_team_icon	| str	| URL |
| away_team_icon	| str	| URL |
| home_team_score	| num	| |
| away_team_score	| num	| |
```json
{
	"cmd":"LIVE_MULTI_VIEW_NEW_INFO",
	"data":{
		"title":"xxx",
		"room_id":xxx,
		"copy_writing":"更多视角",
		"bg_image":"https://i0.hdslb.com/bfs/live/edaa9477a1d8325dd0c36c419b6fd5f9646b2419.png",
		"sub_slt_color":"#FFFFFF",
		"sub_bg_color":"#333333",
		"sub_text_color":"#FFFFFF",
		"view_type":xxx,
		"room_list":[
			{"order_id":1,"room_id":xxx,"room_name":"主房间","live_status":xxx,"jump_url":"xxx"},
			{"order_id":xxx,"room_id":xxx,"room_name":"xxx","live_status":xxx,"jump_url":"xxx"}
		],
		"relation_view":[
			{"order_id":1,"view_type":xxx,"view_id":xxx,"view_name":"主房间","title":"xxx","cover":"xxx","jump_url":"xxx","switch":false,"num":xxx,"watch_icon":"xxx","live_status":xxx,"text_small":"xxx","use_view_vt":false,"anchor_face":"xxx","match_live_room":true,"match_info":{"match_status":xxx,"home_team_name":"xxx","away_team_name":"xxx","home_team_icon":"xxx","away_team_icon":"xxx","home_team_score":0,"away_team_score":0},"duration":xxx,"up_name":"","pub_date":"","gather_id":xxx},
			{"order_id":xxx,"view_type":xxx,"view_id":xxx,"view_name":"xxx","title":"xxx","cover":"xxx","jump_url":"xxx","switch":false,"num":xxx,"watch_icon":"xxx","live_status":xxx,"text_small":"xxx","use_view_vt":false,"anchor_face":"xxx","match_live_room":false,"match_info":null,"duration":xxx,"up_name":"","pub_date":"","gather_id":xxx},
			{"order_id":xxx,"view_type":xxx,"view_id":xxx,"view_name":"xxx","title":"xxx","cover":"xxx","jump_url":"xxx","switch":true,"num":xxx,"watch_icon":"xxx","live_status":xxx,"text_small":"xxx","use_view_vt":false,"anchor_face":"xxx","match_live_room":false,"match_info":null,"duration":xxx,"up_name":"","pub_date":"","gather_id":xxx},
			{"order_id":xxx,"view_type":xxx,"view_id":170001,"view_name":"xxxx","title":"xxx","cover":"xxx","jump_url":"xxx://video/170001","switch":false,"num":xxx,"watch_icon":"","live_status":0,"text_small":"xxx","use_view_vt":false,"anchor_face":"xxx","match_live_room":false,"match_info":null,"duration":xxx,"up_name":"xxx","pub_date":"xxx","gather_id":xxx}
		],
		"view_pattern":xxx,
		"gather_room_list":[
			{"order_id":xxx,"gather_title":"精彩视频","exposure_mode":0,"icon":"","gather_id":1,"gather_type":0}
		]
	}
}
"relation_view____cover":[
	"https://s1.hdslb.com/bfs/static/blive/live-assets/common/images/no-cover.png"
	"http://i0.hdslb.com/bfs/live/new_room_cover/xxx.jpg"
	"http://i0.hdslb.com/bfs/live/xxx.jpg"
	"http://i0.hdslb.com/bfs/live/user_cover/xxx.jpg"
	"http://i0.hdslb.com/bfs/archive/xxx.jpg"
	"http://i1.hdslb.com/bfs/archive/xxx.jpg"
]
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
{"cmd":"LIVE_INTERACT_GAME_STATE_CHANGE","data":{"game_name":"互动玩法","game_id":"xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxxx","action":1},"recv_time":"2024-xx-xx xx:xx:xx"}
```
---
### GUARD_LEADER_NOTICE
[TOP](#直播弹幕)  
文档更新：2025-06-10  
舰队指挥官  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "GUARD_LEADER_NOTICE" |
| data		| obj	| |
#### GUARD_LEADER_NOTICE__data
| key		| type	| value	|
|-|-|-|
| input_background_url				| str	| |
| rank_top_background_url1			| str	| |
| effect_id							| num	| |
| display_src						| str	| |
| anchor_background_url				| str	| |
| name								| str	| |
| rank_top_background_url2			| str	| |
| svga_Block						| num	| |
| uid								| num	| |
| background_url					| str	| |
| rank_top_background_light_url2	| str	| |
| anchor_effect_id					| num	| |
| show								| num	| |
| avatar_src						| str	| |
| face								| str	| |
| rank_top_icon1					| str	| |
| rank_top_icon2					| str	| |
| jump_url							| str	| |
```json
{
	"cmd": "GUARD_LEADER_NOTICE",
	"data": {
		"input_background_url": "https://i0.hdslb.com/bfs/live/ffba0916dc46c0242ad83644b5ccf1870b54a12a.png",
		"rank_top_background_url1": "https://i0.hdslb.com/bfs/live/b2832de9cca6a0b3b4872c8d96c05ae713bc51d2.png",
		"effect_id": 0,
		"display_src": "https://i0.hdslb.com/bfs/live/7aed22c78a2a41a5c1b964f1f2a3220c52c1663e.png",
		"anchor_background_url": "https://i0.hdslb.com/bfs/live/3b8aa82202415b1ed8772ba3aa78628a31d44d51.png",
		"name": "xxx",
		"rank_top_background_url2": "https://i0.hdslb.com/bfs/live/71397554da8a7bd2ac14905c69891df54ad62ede.png",
		"svga_Block": 0,
		"uid": xxx,
		"background_url": "https://i0.hdslb.com/bfs/live/13306509ffe9d43d5571ac9af84463e4958ab3c4.png",
		"rank_top_background_light_url2": "https://i0.hdslb.com/bfs/live/c0fbd28b6ddf170b8db2e2c7163eb9d66f66fd8b.png",
		"anchor_effect_id": 0,
		"show": 1,
		"avatar_src": "https://i0.hdslb.com/bfs/live/4d1f0d9a39e368c4b9b4128f58f945099a295c39.png",
		"face": "http://i0.hdslb.com/bfs/face/xxx.jpg",
		"rank_top_icon1": "https://i0.hdslb.com/bfs/live/64b22e65979b32f7e4e8bec1edb38c697fb320fc.png",
		"rank_top_icon2": "https://i0.hdslb.com/bfs/live/7b9d773c6018ffac9f0eadd3c92f0090e09055f2.png",
		"jump_url": "https://live.xxx.com/p/html/live-app-guard-pilot/index.html?is_live_half_webview=1&hybrid_half_ui=1,3,100p,73p,0,0,30,0,12,0;2,2,375,100p,0,0,30,0,0,0;3,3,100p,73p,0,0,30,0,12,0;4,2,375,100p,0,0,30,0,0,0;5,3,100p,73p,0,0,30,0,12,0;6,3,100p,73p,0,0,30,0,12,0;7,3,100p,73p,0,0,30,0,12,0;8,2,320,480,0,0,30,0,0,0&anchorId=xxxx&roomId=xxxx"
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
| key				| type		| value	|
|-|-|-|
| wish				| \[\]obj	| |
| wish_status		| num		| |
| sid				| num		| |
| wish_status_info	| \[\]obj	| |
| wish_name			| str		| |
| jump_schema		| str		| |
| type				| num		| |
| ts				| num		| |
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
	"cmd":"WIDGET_WISH_LIST",
	"data":{
		"wish":[
			{"type":3,"gift_id":10002,"gift_name":"提督","gift_img":"https://i0.hdslb.com/bfs/live/ea985665bfdc4b0ce894b8fcf7c29fecc3136a08.png","gift_price":1998000,"target_num":xxx,"current_num":0,"wish_name":"","check_status":0,"check_reason":"","wish_sub_id":"","id":""},
			{"type":3,"gift_id":10003,"gift_name":"舰长","gift_img":"https://i0.hdslb.com/bfs/live/f1be2a2d5b227ce72641de1ad64bcc7f9e4111c3.png","gift_price":198000,"target_num":xxx,"current_num":0,"wish_name":"","check_status":0,"check_reason":"","wish_sub_id":"","id":""}
		],
		"wish_status":1,
		"sid":4151,
		"wish_status_info":[
			{"wish_status_msg":"去设置","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":0},
			{"wish_status_msg":"心愿达成","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":2},
			{"wish_status_msg":"收集失败","wish_status_img":"https://i0.hdslb.com/bfs/live/2b9a596495d7ce2852a7de17a8baeeca813f6139.png","wish_status":3}
		],
		"wish_name":"心愿单",
		"jump_schema":"",
		"type":1,
		"ts":xxx
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
| anchor_uid	| num	| |
| info			| obj	| |
| room_id		| num	| |
```json
{
	"cmd":"UNIVERSAL_EVENT_GIFT",
	"data":{
		"anchor_uid":xxx,
		"info":{
			"biz_session_id":"xxx",
			"business_label":"universal_multi_conn",
			"interact_channel_id":"xxx",
			"interact_connect_type":0,
			"interact_max_users":9,
			"interact_mode":{
				"apply_timeout":20,
				"interact_mode_type":0,
				"invite_timeout":20,
				"join_types":[1,2],
				"position_mode":0
			},
			"interact_template":{
				"is_variable_layout":true,
				"layout_data":{
					"best_area_show_pos":0,
					"cells":[
						{"default_open":0,"height":8,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":0,"width":0,"x":0,"y":0,"z_index":0},
						{"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":1,"width":0,"x":5,"y":0,"z_index":0},
						{"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":2,"width":0,"x":5,"y":4,"z_index":0}
					],
					"default_cell":{"default_open":1,"height":4,"mobile_avatar_size":64,"mobile_font_size":12,"pc_web_avatar_size":112,"pc_web_font_size":14,"position":0,"width":5,"x":0,"y":0,"z_index":0},
					"height":8,
					"rtc_resolution":{"code_rate_init":1600,"code_rate_max":2000,"code_rate_min":800,"horizontal_height":800,"horizontal_width":1000,"vertical_height":1152,"vertical_width":720},
					"width":10
				},
				"layout_id":"left1_right2",
				"layout_list":null,
				"show_interact_ui":true,
				"template_id":"multi_conn_grid"
			},
			"invoking_time":1,
			"members":[
				{"face":"xxx","gender":x,"join_time":xxx,"link_id":"xxx","position":0,"room_id":xxx,"uid":xxx,"uname":"xxx"},
				{"face":"xxx","gender":x,"join_time":xxx,"link_id":"xxx","position":2,"room_id":xxx,"uid":xxx,"uname":"xxx"},
				{"face":"xxx","gender":x,"join_time":xxx,"link_id":"xxx","position":1,"room_id":xxx,"uid":xxx,"uname":"xxx"}
			],
			"members_version":xxx,
			"multi_conn_info":{
				"room_owner":xxx,
				"scores":[
					{"price":100,"price_text":"1","uid":xxx},
					{"price":100,"price_text":"1","uid":xxx},
					{"price":100,"price_text":"1","uid":xxx}
				]
			},
			"room_owner":xxx,
			"room_start_at":"",
			"room_start_at_ts":0,
			"room_status":1,
			"session_start_at":"",
			"session_start_at_ts":0,
			"session_status":1,
			"system_time_unix":xxx,
			"trace_id":"",
			"version":xxx
		},
		"room_id":xxx
	}
}
{"cmd":"UNIVERSAL_EVENT_GIFT","data":{"anchor_uid":xxx,"info":{"biz_session_id":"xxx","business_label":"universal_multi_conn","interact_channel_id":"xxx","interact_connect_type":0,"interact_max_users":9,"interact_mode":{"apply_timeout":xxx,"interact_mode_type":0,"invite_timeout":xxx,"join_types":[1,2],"position_mode":0},"interact_template":{"is_variable_layout":true,"layout_data":{"best_area_show_pos":-1,"cells":[{"can_zoom":0,"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":0,"width":0,"x":0,"y":0,"z_index":0},{"can_zoom":0,"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":1,"width":0,"x":5,"y":0,"z_index":0}],"default_cell":{"can_zoom":0,"default_open":1,"height":8,"mobile_avatar_size":xxx,"mobile_font_size":xxx,"pc_web_avatar_size":xxx,"pc_web_font_size":xxx,"position":0,"width":5,"x":0,"y":0,"z_index":0},"height":8,"rtc_resolution":{"code_rate_init":xxx,"code_rate_max":xxx,"code_rate_min":xxx,"horizontal_height":xxx,"horizontal_width":xxx,"vertical_height":xxx,"vertical_width":xxx},"width":xxx},"layout_id":"left1_right1","layout_list":null,"show_interact_ui":false,"template_id":"multi_conn_grid"},"invoking_time":1,"members":[{"face":"xxx","gender":1,"join_time":xxx,"link_id":"xxx","position":0,"room_id":xxx,"uid":xxx,"uname":"xxx"},{"face":"xxx","gender":0,"join_time":xxx,"link_id":"xxx","position":1,"room_id":xxx,"uid":xxx,"uname":"xxx"}],"members_version":xxx,"multi_conn_info":{"room_owner":xxx,"scores":[{"price":xxx,"price_text":"xxx","uid":xxx},{"price":xxx,"price_text":"xxx","uid":xxx}],"show_score":1},"room_owner":xxx,"room_start_at":"","room_start_at_ts":0,"room_status":1,"session_start_at":"","session_start_at_ts":0,"session_status":1,"system_time_unix":xxx,"trace_id":"","version":xxx},"room_id":xxx}}
{"cmd":"UNIVERSAL_EVENT_GIFT","data":{"anchor_uid":xxx,"info":{"biz_session_id":"xxx","business_label":"universal_multi_conn","interact_channel_id":"xxx","interact_connect_type":0,"interact_max_users":9,"interact_mode":{"apply_timeout":xxx,"interact_mode_type":0,"invite_timeout":xxx,"join_types":[1,2],"position_mode":0},"interact_template":{"is_variable_layout":true,"layout_data":{"best_area_show_pos":-1,"cells":[{"can_zoom":0,"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":0,"width":0,"x":0,"y":0,"z_index":0},{"can_zoom":0,"default_open":0,"height":0,"mobile_avatar_size":0,"mobile_font_size":0,"pc_web_avatar_size":0,"pc_web_font_size":0,"position":1,"width":0,"x":5,"y":0,"z_index":0}],"default_cell":{"can_zoom":0,"default_open":1,"height":8,"mobile_avatar_size":xxx,"mobile_font_size":xxx,"pc_web_avatar_size":xxx,"pc_web_font_size":xxx,"position":0,"width":5,"x":0,"y":0,"z_index":0},"height":8,"rtc_resolution":{"code_rate_init":xxx,"code_rate_max":xxx,"code_rate_min":xxx,"horizontal_height":xxx,"horizontal_width":xxx,"vertical_height":xxx,"vertical_width":xxx},"width":xxx},"layout_id":"left1_right1","layout_list":null,"show_interact_ui":true,"template_id":"multi_conn_grid"},"invoking_time":1,"members":[{"face":"xxx","gender":1,"join_time":xxx,"link_id":"xxx","position":0,"room_id":xxx,"uid":xxx,"uname":"xxx"},{"face":"xxx","gender":0,"join_time":xxx,"link_id":"xxx","position":1,"room_id":xxx,"uid":xxx,"uname":"xxx"}],"members_version":xxx,"multi_conn_info":{"room_owner":xxx,"scores":[{"price":xxx,"price_text":"xxx","uid":xxx},{"price":xxx,"price_text":"xxx","uid":xxx}],"show_score":1},"room_owner":xxx,"room_start_at":"","room_start_at_ts":0,"room_status":1,"session_start_at":"","session_start_at_ts":0,"session_status":1,"system_time_unix":xxx,"trace_id":"","version":xxx},"room_id":xxx}}
```
---
### LITTLE_TIPS
[TOP](#直播弹幕)  
文档更新：2024-04-24  
用户提示  
| key	| type	| value	|
|-|-|-|
| cmd	| str	| "LITTLE_TIPS" |
| data	| obj	| |
#### LITTLE_TIPS__data
| key	| type	| value	|
|-|-|-|
| msg	| str	| |
```json
{"cmd":"LITTLE_TIPS","data":{"msg":"你的粉丝勋章【xxx】已达今日亲密度上限"}}
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
{"cmd":"LIKE_GUIDE_USER","data":{"show_area":0,"like_text":"主播@你：点点赞支持一下我吧","uid":xxx,"identities":[1],"msg_type":6,"dmscore":20}}
```
---
### REENTER_LIVE_ROOM
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "REENTER_LIVE_ROOM/REENTER_LIVE_ROOM_V2" |
| data		| obj	| |
#### REENTER_LIVE_ROOM__data
| key						| type	| value	|
|-|-|-|
| room_id					| num	| |
| request_random_sec_range	| num	| |
| reason					| num	| |
```json
{"cmd":"REENTER_LIVE_ROOM",   "data":{"room_id":xxx,"request_random_sec_range":10,"reason":1}}
{"cmd":"REENTER_LIVE_ROOM_V2","data":{"request_random_sec_range":30,"reason":1,"enter_room_dup_key":"xxx","target_room_id":xxx,"target_room_url":"https://live.xxx.com/xxx"}}
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
{"cmd":"DANMU_ACTIVITY_CONFIG","data":{
		"dm_mode":3001,
		"dm_setting_switch":1,
		"etime":-28800,
		"extra":"",
		"id":xxx,
		"material_conf":{
			"activity_test_material":"http://i0.hdslb.com/bfs/live/a4d2a09ae85ded1dc17571d73ef4a8ada9c40d91.zip",
			"activity_type":1,
			"main_state_dm_color":"#D0FEFF",
			"material_mode":[
				{"app_key":"iphone","mobi_material":{"mobi_module":"","mobi_module_file":"mobi_meteor.zip","mobi_module_file_name":"mobi_meteor","mobi_module_version":1,"mobi_pool":"live"}},
				{"app_key":"ipad2","mobi_material":{"mobi_module":"","mobi_module_file":"mobi_meteor.zip","mobi_module_file_name":"mobi_meteor","mobi_module_version":1,"mobi_pool":"live"}},
				{"app_key":"android","mobi_material":{"mobi_module":"","mobi_module_file":"mobi_meteor.zip","mobi_module_file_name":"mobi_meteor","mobi_module_version":1,"mobi_pool":"live"}},
				{"app_key":"android64","mobi_material":{"mobi_module":"","mobi_module_file":"mobi_meteor.zip","mobi_module_file_name":"mobi_meteor","mobi_module_version":1,"mobi_pool":"live"}}
			],
			"objective_state_dm_color":"#D0FEFF",
			"web_material":"{\"main_state_bg\":\"http://i0.hdslb.com/bfs/live/df12a08ce2f43bc6f74a7def65f2332781d13af2.png\",\"objective_state_bg\":\"http://i0.hdslb.com/bfs/live/b89dba7a33a86aad2f0344542e8216cbd1d025a6.png\"}"
		},
		"mock_options":null,
		"platform":[3,2,1,4],
		"screen_type":3,
		"status":1,
		"stime":-28800
	}
}
```
---
### POPULAR_RANK_GUIDE_CARD
[TOP](#直播弹幕)  
文档更新：2024-06-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULAR_RANK_GUIDE_CARD" |
| data		| obj	| |
#### POPULAR_RANK_GUIDE_CARD__data
| key			| type	| value	|
|-|-|-|
| ruid			| num	| |
| title			| str	| 1\~100 |
| sub_text		| str	| |
| icon_img		| str	| 头像URL |
| gift_id		| num	| |
| countdown		| num	| |
| popup_title	| str	| |
```json
{"cmd":"POPULAR_RANK_GUIDE_CARD","data":{"ruid":12345,"title":"目前人气榜NO.xxx","sub_text":"帮我投喂人气票冲榜吧~","icon_img":"xxx","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"}}
{"data":{"ruid":12345,"title":"目前人气榜NO.xxx","sub_text":"帮我投喂人气票冲榜吧~","icon_img":"xxx","gift_id":33988,"countdown":10,"popup_title":"投喂一个人气票帮助主播打榜~"},"cmd":"POPULAR_RANK_GUIDE_CARD"}
```
### HOT_RANK_CHANGED
[TOP](#直播弹幕格式)  
文档更新：2024-xx-xx  
**已移除**  
计时器每半小时(1800秒)重置一次，计时重置后，约每15秒或(N×15)秒发送一次  
计时器每半小时(1800秒)重置一次，计时重置后，约每5秒或(N×5)秒发送一次  
| key | type | value |
|-|-|-|
| cmd	| str	| "HOT_RANK_CHANGED" / "HOT_RANK_CHANGED_V2" |
| data	| obj	| |
#### HOT_RANK_CHANGED__data
| key 12		| type	| value |
| area_name		| str	| 分区名称(大/小分区) |
| blink_url		| str	| 排行榜URL |
| countdown		| num	| 倒计时\[1-1800\] |
| icon			| str	| (url) |
| live_link_url	| str	| 排行榜URL |
| live_url		| str	| 排行榜URL |
| pc_link_url	| str	| 排行榜URL |
| rank			| num	| 排名\[1-50\] |
| rank_desc		| str	| `f"{分区名称}top50"` |
| timestamp		| num	| TimeStamp(秒) |
| trend			| num	| 0 |
| web_url		| str	| 排行榜URL |
```json
{"key":"value"}
```
---
### HOT_RANK_SETTLEMENT
[TOP](#直播弹幕格式)  
文档更新：2024-xx-xx  
**已移除**  
每30分(1800秒 `HH:25:05,HH:55:05`)广播一次，大/小分区排行榜topxx  
| key		| type	 | value |
|-|-|-|
| cmd		| str		| "HOT_RANK_SETTLEMENT" / "HOT_RANK_SETTLEMENT_V2" |
| data		| obj		| |
#### HOT_RANK_SETTLEMENT__data
| key		| type		| value |
| area_name	| str		| 分区名称(大/小) |
| cache_key	| str		| hex(128bit) |
| dm_msg	| str		| "恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜top{rank}! 即将获得热门流量推荐哦！" "恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜榜首!" "恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜top{rank}!" |
| dm_msg	| str		| `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜{xxx}!"` "榜首,top2-10" |
| dmscore	| str		| 144 |
| face		| str		| 主播头像URL |
| icon		| str		| (url) |
| rank		| num/str	| 排名 |
| timestamp	| num/str	| TimeStamp(秒) `HH:25:05 HH:55:05` |
| uname		| str		| 主播用户名 |
| url		| str		| |
```json
{"key":"value"}
```
---
### USER_VIRTUAL_MVP
[TOP](#直播弹幕)  
文档更新：2023-05-12  
守护圣法师  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_VIRTUAL_MVP" |
| data		| obj	| |
#### USER_VIRTUAL_MVP__data
| key		| type	| value	|
|-|-|-|
| goods_id			| num	| |
| effect_id			| num	| |
| effect_queue		| num	| |
| uid				| num	| |
| uname				| str	| |
| uname_color		| str	| |
| user_guard_level	| num	| |
| goods_name		| str	| |
| goods_num			| num	| |
| goods_price		| num	| |
| goods_icon		| str	| |
| action			| str	| |
| order_id			| str	| |
| timestamp			| num	| |
| success_toast		| str	| |
| animation_block	| num	| |
```json
{"cmd":"USER_VIRTUAL_MVP","data":{"goods_id":255,"effect_id":1020,"effect_queue":3,"uid":xxx,"uname":"xxx","uname_color":"#FF7C28","user_guard_level":1,"goods_name":"守护圣法师x7天","goods_num":1,"goods_price":12333300,"goods_icon":"http://i0.hdslb.com/bfs/live/c9206642e90b9e3d2eefc01b11ea7f50152314c2.png","action":"解锁","order_id":"2305xxxxxxxxxxxxxxxxxxxxx","timestamp":xxxxxxxxxx,"success_toast":"解锁成功，已为您穿戴守护圣法师装扮","animation_block":0}}
```
---
### ROOM_MODULE_DISPLAY
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key			| type	| value	|
|-|-|-|
| cmd			| str	| "ROOM_MODULE_DISPLAY" |
| data			| obj	| |
#### ROOM_MODULE_DISPLAY__data
| key			| type	| value	|
|-|-|-|
| timestamp		| num	| |
| modules		| obj	| |
#### ROOM_MODULE_DISPLAY__data__modules
| key			| type	| value	|
|-|-|-|
| bottom_banner	| num	| |
| top_banner	| num	| |
| widget_banner	| num	| |
```json
{"cmd":"ROOM_MODULE_DISPLAY","data":{"timestamp":xxx,"modules":{"bottom_banner":1,"top_banner":1,"widget_banner":1}}}
```
---
### SHOPPING_EXPLAIN_CARD
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "SHOPPING_EXPLAIN_CARD" |
| data		| obj	| |
#### SHOPPING_EXPLAIN_CARD__data
| key					| type		| value	|
|-|-|-|
| goods_id				| str		| |
| goods_name			| str		| |
| goods_price			| str		| |
| goods_max_price		| str		| |
| sale_status			| num		| |
| coupon_name			| str		| |
| goods_icon			| str		| |
| status				| num		| |
| h5_url				| str		| |
| source				| num		| |
| timestamp				| num		| |
| is_pre_sale			| num		| |
| activity_info			| null/xxx	| |
| pre_sale_info			| null/xxx	| |
| early_bird_info		| null/xxx	| |
| unique_id				| str		| |
| uid					| num		| |
| selling_point			| str		| |
| coupon_discount_price	| str		| |
| sei_status			| num		| |
| gift_buy_info			| null/xxx	| |
| reward_info			| null/xxx	| |
| is_exclusive			| bool		| |
| coupon_id				| str		| |
| goods_tag_list		| \[\]str	| |
| virtual_extra_info	| null/xxx	| |
| price_info			| obj		| |
| btn_info				| null/xxx	| |
| goods_sort_id			| num		| |
| coupon_info			| null/xxx	| |
| active_info			| null/xxx	| |
| jump_url				| str		| |
| is_repeated			| num		| |
#### SHOPPING_EXPLAIN_CARD__data__price_info
| key					| type		| value	|
|-|-|-|
| normal				| null/xxx	| |
| activity				| null/xxx	| |
```json
{"cmd":"SHOPPING_EXPLAIN_CARD","data":{"goods_id":"xxx","goods_name":"xxx","goods_price":"xxx","goods_max_price":"","sale_status":0,"coupon_name":"","goods_icon":"http://i0.hdslb.com/bfs/e-commerce-goods/xxx.jpg","status":1,"h5_url":"https://live.xxx.com/p/html/live-app-ecommerce/index.html?is_live_half_webview=1&hybrid_rotate_d=0&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12,0;2,2,375,100p,0,0,30,100,0,0;3,3,100p,70p,0,0,30,100,12,0;4,2,375,100p,0,0,30,100,0,0;5,3,100p,70p,0,0,30,100,12,0;6,3,100p,70p,0,0,30,100,12,0;7,3,100p,70p,0,0,30,100,12,0&web_type=1&source=3&goods_id=xxx#/jingdong","source":3,"timestamp":xxx,"is_pre_sale":0,"activity_info":null,"pre_sale_info":null,"early_bird_info":null,"unique_id":"xxx","uid":xxx,"selling_point":"","coupon_discount_price":"","sei_status":0,"gift_buy_info":null,"reward_info":null,"is_exclusive":false,"coupon_id":"","goods_tag_list":["https://i0.hdslb.com/bfs/live/8f27ae1afbe71e9e83dc6f24463de47e3d57f814.png"],"virtual_extra_info":null,"price_info":{"normal":null,"activity":null},"btn_info":null,"goods_sort_id":1,"coupon_info":null,"active_info":null,"jump_url":"","is_repeated":0}}
```
---
### LIVE_MULTI_VIEW_EVENT_CHANGE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_MULTI_VIEW_EVENT_CHANGE" |
| data		| \[\]obj	| |
#### LIVE_MULTI_VIEW_EVENT_CHANGE__data
| key				| type	| value	|
|-|-|-|
| room_id			| num	| 主房间-长ID |
| match_status		| num	| |
| home_team_name	| str	| 我方队伍名称 |
| away_team_name	| str	| 对方队伍名称 |
| home_team_icon	| str	| 我方图标 |
| away_team_icon	| str	| 对方图标 |
| home_team_score	| num	| 我方分数 |
| away_team_score	| num	| 对方分数 |
| time_stamp		| num	| TimeStamp(秒) |
```json
{"cmd":"LIVE_MULTI_VIEW_EVENT_CHANGE","data":[{"room_id":xxx,"match_status":xxx,"home_team_name":"xxx","away_team_name":"xxx","home_team_icon":"xxx","away_team_icon":"xxx","home_team_score":x,"away_team_score":x,"time_stamp":xxx}]}
```
---
### POPULARITY_RANK_TAB_CHG
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "POPULARITY_RANK_TAB_CHG" |
| data		| obj	| |
#### POPULARITY_RANK_TAB_CHG__data
| key				| type	| value	|
|-|-|-|
| room_id			| num	| |
| ruid				| num	| |
| type				| str	| |
| need_refresh_tab	| bool	| |
```json
{"cmd":"POPULARITY_RANK_TAB_CHG","data":{"room_id":xxx,"ruid":xxx,"type":"area","need_refresh_tab":true}}
```
---
### RANK_CHANGED
[TOP](#直播弹幕)  
文档更新：2025-07-02  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RANK_CHANGED" / "RANK_CHANGED_V2" |
| data		| obj	| |
#### RANK_CHANGED__data
| key					| type	| value	|
|-|-|-|
| uid					| num	| |
| rank					| num	| |
| countdown				| num	| |
| timestamp				| num	| |
| url					| str	| |
| on_rank_name_by_type	| str	| |
| rank_name_by_type		| str	| |
| url_by_type			| str	| |
| rank_by_type			| num	| |
| rank_type				| num	| |
```json
{"cmd":"RANK_CHANGED","data":{"uid":xxx,"rank":0,"countdown":0,"timestamp":xxx,"on_rank_name_by_type":"热门榜","rank_name_by_type":"热门榜","url_by_type":"https://live.xxx.com/p/html/live-app-hotrank/index.html?is_live_half_webview=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12;2,2,375,100p,0,0,30,100,0;3,3,100p,70p,0,0,30,100,12;4,2,375,100p,0,0,30,100,0;5,3,100p,70p,0,0,30,100,0;6,3,100p,70p,0,0,30,100,0;7,3,100p,70p,0,0,30,100,0;8,3,100p,70p,0,0,30,100,0&pc_ui=338,465,f4eefa,0&redirect=v2&rank=hot&anchorId={xxx}&rank_type=1","rank_by_type":0,"rank_type":3}}
{"cmd":"RANK_CHANGED_V2","data":{"uid":xxx,"rank":xxx,"countdown":xxx,"timestamp":xxx,"url":"https://live.xxx.com/p/html/live-app-hotrank/index.html?is_live_half_webview=1&hot_type=1&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,30,100,12;2,2,375,100p,0,0,30,100,0;3,3,100p,70p,0,0,30,100,12;4,2,375,100p,0,0,30,100,0;5,3,100p,70p,0,0,30,100,0;6,3,100p,70p,0,0,30,100,0;7,3,100p,70p,0,0,30,100,0;8,3,100p,70p,0,0,30,100,0&pc_ui=338,465,f4eefa,0#/hotv3","on_rank_name_by_type":"全站","rank_name_by_type":"热门榜","url_by_type":"","rank_by_type":0,"rank_type":5,"sub_rank_type":1}}
```
---
### CHG_RANK_REFRESH
[TOP](#直播弹幕)  
文档更新：2024-07-24  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CHG_RANK_REFRESH" |
| data		| obj	| |
#### CHG_RANK_REFRESH__data
| key			| type	| value	|
|-|-|-|
| cmd			| str	| |
| rank_type		| num	| |
| rank_module	| str	| |
| room_id		| num	| |
| ruid			| num	| |
| need_refresh	| bool	| |
| version		| num	| ts(ms) |
```json
{"cmd":"CHG_RANK_REFRESH","data":{"cmd":"CHG_RANK_REFRESH","rank_type":3,"rank_module":"area","room_id":xxx,"ruid":xxx,"need_refresh":true,"version":xxx}}
{"cmd":"CHG_RANK_REFRESH","data":{"cmd":"CHG_RANK_REFRESH","rank_type":4,"rank_module":"area","room_id":xxx,"ruid":xxx,"need_refresh":true,"version":xxx}}
```
---
### USER_TOAST_MSG_V2
[TOP](#直播弹幕)  
文档更新：2024-08-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "USER_TOAST_MSG_V2" |
| data		| obj	| |
#### USER_TOAST_MSG_V2__data
| key				| type	| value |
|-|-|-|
| sender_uinfo		| obj	| [uinfo](#PUBLIC_uinfo) base |
| receiver_uinfo	| obj	| [uinfo](#PUBLIC_uinfo) base |
| guard_info		| obj	| |
| group_guard_info	| null	| |
| pay_info			| obj	| |
| gift_info			| obj	| |
| effect_info		| obj	| |
| toast_msg			| str	| |
| option			| obj	| |
#### USER_TOAST_MSG_V2__data__guard_info
| key				| type	| value |
|-|-|-|
| guard_level		| num	| |
| role_name			| str	| |
| room_guard_count	| num	| |
| op_type			| num	| |
| start_time		| num	| |
| end_time			| num	| |
#### USER_TOAST_MSG_V2__data__pay_info
| key				| type	| value |
|-|-|-|
| payflow_id		| str	| |
| price				| num	| |
| num				| num	| |
| unit				| str	| |
#### USER_TOAST_MSG_V2__data__gift_info
| key				| type	| value |
|-|-|-|
| gift_id			| num	| |
#### USER_TOAST_MSG_V2__data__effect_info
| key					| type	| value |
|-|-|-|
| effect_id				| num	| |
| room_effect_id		| num	| |
| face_effect_id		| num	| |
| room_gift_effect_id	| num	| |
| room_group_effect_id	| num	| |
#### USER_TOAST_MSG_V2__data__option
| key				| type	| value |
|-|-|-|
| anchor_show		| bool	| |
| user_show			| bool	| |
| is_group			| num	| |
| is_show			| num	| |
| source			| num	| |
| svga_block		| num	| |
| color				| str	| |
```json
{
	"cmd":"USER_TOAST_MSG_V2",
	"data":{
		"sender_uinfo":{"uid":xxx,"base":{"name":"xxx","face":""}},
		"receiver_uinfo":{"uid":xxx,"base":{"name":"xxx","face":"xxx"}},
		"guard_info":{"guard_level":2,"role_name":"xx","room_guard_count":xxx,"op_type":xx,"start_time":xxx,"end_time":xxx},
		"group_guard_info":null,
		"pay_info":{"payflow_id":"xxx(25)","price":xxx,"num":xxx,"unit":"月"},
		"gift_info":{"gift_id":xxx},
		"effect_info":{"effect_id":xxx,"room_effect_id":xxx,"face_effect_id":xx,"room_gift_effect_id":0,"room_group_effect_id":xxx},
		"toast_msg":"<%xxx%> 在主播xxx的直播间xx了xx，今天是TA陪伴主播的第xxx天",
		"option":{"anchor_show":true,"user_show":true,"is_group":0,"is_show":0,"source":0,"svga_block":0,"color":"#xxxxxx"}
	}
}
```
---
### WIN_ACTIVITY
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WIN_ACTIVITY" |
| data		| obj	| |
| number	 | num | |
#### WIN_ACTIVITY__data
| key		| type	| value	|
|-|-|-|
| delay_time_min| num	| |
| delay_time_max| num	| |
| activity_id	| num	| |
| jump_url		| str	| |
| weight		| num	| |
| closeable		| num	| |
| title			| str	| |
| title_color	| str	| |
| activity_pic	| str	| |
| background	| str	| |
| current_round	| num	| |
| typeB			| \[\]obj	| |
```json
{"cmd":"WIN_ACTIVITY","number":1,"data":{"delay_time_min":0,"delay_time_max":30,"activity_id":1090,"jump_url":"https://live.xxx.com/p/html/live-app-treasurebox/index.html?is_live_half_webview=1&hybrid_biz=live-app-treasurebox&hybrid_rotate_d=1&hybrid_half_ui=1,3,100p,70p,0,0,30,100;2,2,375,100p,0,0,30,100;3,3,100p,70p,0,0,30,100;4,2,375,100p,0,0,30,100;5,3,100p,70p,0,0,30,100;6,3,100p,70p,0,0,30,100;7,3,100p,70p,0,0,30,100&aid={1090}","weight":20,"closeable":0,"title":"华为nova Flip新生之夜","title_color":"#FFFFFF","activity_pic":"https://i0.hdslb.com/bfs/live/c3ed87683f6e87d256d1f5fdddbfb220fc4c2cdf.png","background":"https://i0.hdslb.com/bfs/live/84cd59bcb1e977359df618dbeb0f7828751f457c.png","current_round":1,"typeB":[{"join_start_time":xxxxxxxxxx,"join_end_time":xxxxxxxxxx,"round_num":1}]}}
```
---
### COMMON_ANIMATION
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "COMMON_ANIMATION" |
| data		| obj	| |
#### COMMON_ANIMATION__data
| key			| type	| value	|
|-|-|-|
| uid			| num	| |
| effect_id		| num	| |
| ?gift_scene	| obj	| |
| demarcation	| num	| |
| order_id		| str	| |
| ?biz_extra	| str	| |
```json
{"cmd":"COMMON_ANIMATION","data":{"uid":xxx,"effect_id":xxx,"demarcation":xxx,"order_id":"xxxxxxxxxxxxxxxxxxxxxxxxx"}}
{"cmd":"COMMON_ANIMATION","data":{"uid":xxx,"effect_id":xxx,"gift_scene":{"scene":"xxx","pay_type":"xxx"},"demarcation":xxx,"order_id":"xxxxxxxxxxxxxxxxxxxxxxxxx","biz_extra":"{xxxxxx}"}}
```
---
### REVENUE_RANK_CHANGED
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "REVENUE_RANK_CHANGED" |
| data		| obj	| |
#### REVENUE_RANK_CHANGED__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"REVENUE_RANK_CHANGED","data":{"conf_id":-20000,"rank_name":"xxx","uid":xxx,"rank":xxx,"icon_url_blue":"(url)","icon_url_pink":"(url)","icon_url_grey":"(url)","action_type":1,"timestamp":xxx,"msg_id":"(UUID4)","jump_url_link":"(url)","jump_url_pc":"(url)","jump_url_pink":"(url)","jump_url_web":"(url)"}}
```
---
### LIVE_ANI_RES_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LIVE_ANI_RES_UPDATE" |
| data		| obj	| |
#### LIVE_ANI_RES_UPDATE__data
| key		| type	| value	|
|-|-|-|
| list		| \[\]obj	| |
#### LIVE_ANI_RES_UPDATE__data
| key		| type	| value	|
|-|-|-|
| id						| num		| |
| type						| num		| |
| weight					| num		| |
| web_mp4_json				| str		| |
| web_svga					| str		| |
| horizontal_svga			| str		| |
| vertical_svga				| str		| |
| web_mp4					| str		| |
| horizontal_mp4			| str		| |
| vertical_mp4				| str		| |
| horizontal_mp4_md5		| str		| |
| vertical_mp4_md5			| str		| |
| web_mp4_md5				| str		| |
| horizontal_mp4_crc32		| num		| |
| vertical_mp4_crc32		| num		| |
| web_mp4_crc32				| num		| |
| horizontal_mp4_file_size	| num		| |
| vertical_mp4_file_size	| num		| |
| web_mp4_file_size			| num		| |
| h265_conf					| obj		| |
| plan_platform				| \[\]num	| |
| broadcast_scope			| num		| |
| bind_giftids				| \[\]num	| |
| title						| str		| |
| online_time				| num		| |
| offline_time				| num		| |
| ctime						| num		| |
| mtime						| num		| now.ts |
```json
{"cmd":"LIVE_ANI_RES_UPDATE","data":{"list":[{"id":299,"type":1,"weight":1,"web_mp4_json":"https://i0.hdslb.com/bfs/live/cd32dc12c7aa8e180f9a00b140397067e0a637a0.json","web_svga":"","horizontal_svga":"","vertical_svga":"","web_mp4":"https://i0.hdslb.com/bfs/live/cf41ee1bb4709178cc75eaa34197360954453363.mp4","horizontal_mp4":"https://i0.hdslb.com/bfs/live/cf41ee1bb4709178cc75eaa34197360954453363.mp4","vertical_mp4":"https://i0.hdslb.com/bfs/live/cf41ee1bb4709178cc75eaa34197360954453363.mp4","horizontal_mp4_md5":"cddb627e55e6ec1387d42838a8197bb9","vertical_mp4_md5":"cddb627e55e6ec1387d42838a8197bb9","web_mp4_md5":"cddb627e55e6ec1387d42838a8197bb9","horizontal_mp4_crc32":635289345,"vertical_mp4_crc32":635289345,"web_mp4_crc32":635289345,"horizontal_mp4_file_size":586900,"vertical_mp4_file_size":586900,"web_mp4_file_size":586900,"h265_conf":{"horizontal_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/5931326cdc246748695ae57d695056eb7bfe8635.mp4","mp4_md5":"23623ce9aa3f927021d53befa85814a4","mp4_json":"","mp4_crc32":1903301928,"mp4_file_size":356236},"vertical_mp4":{"mp4":"https://i0.hdslb.com/bfs/live/5931326cdc246748695ae57d695056eb7bfe8635.mp4","mp4_md5":"23623ce9aa3f927021d53befa85814a4","mp4_json":"","mp4_crc32":1903301928,"mp4_file_size":356236}},"plan_platform":[1,2],"broadcast_scope":1,"bind_giftids":[31053],"title":"告白花束","online_time":xxxxxxxxxx,"offline_time":0,"ctime":xxxxxxxxxx,"mtime":xxxxxxxxxx}]}}
```
---
### LPL_REALTIME_STATUS_CHANGED
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LPL_REALTIME_STATUS_CHANGED" |
| data		| obj	| |
#### LPL_REALTIME_STATUS_CHANGED__data
| key		| type	| value	|
|-|-|-|
| status	| num	| |
```json
{"cmd":"LPL_REALTIME_STATUS_CHANGED","data":{"status":xxx}}
```
---
### LOL_PLAYER_GRADE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "LOL_PLAYER_GRADE" |
| data		| obj	| |
#### LOL_PLAYER_GRADE__data
| key					| type	| value	|
|-|-|-|
| is_dm_entry_visible	| bool	| |
| dm_jump_url			| str	| |
```json
{"cmd":"LOL_PLAYER_GRADE","data":{"is_dm_entry_visible":false,"dm_jump_url":"...."}}
```
---
### ON_COMMON_CARD_UPDATE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ON_COMMON_CARD_UPDATE" |
| data		| obj	| |
#### ON_COMMON_CARD_UPDATE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"ON_COMMON_CARD_UPDATE","data":{"biz_type":"s14_grade_card","biz_id":"ffff-ffff-ffff-ffff-ffff","card_url":"https://live.xxx.com/p/html/s14-league-of-legends/guide.html","extra_json":"{\"title\":\"这波大龙timing如何\",\"players\":[{\"name\":\"A\",\"avg_grade\":\"9.4\"},{\"name\":\"B\",\"avg_grade\":\"4.3\"},{\"name\":\"C\",\"avg_grade\":\"9.1\"}],\"jump_url\":\"https://www.xxx.com/h5/match/data/grade-list/xxxxxxxx?upstream=5\\u0026hidden_na_nav_bar=0\\u0026match_source=live\"}","card_expire_time":10000,"priority":1,"card_width":302,"card_height":64,"immediately_show":true,"round_radius":14.4,"random_display_delay_range":{"min":0,"max":xxxxx}}}
{"cmd":"ON_COMMON_CARD_UPDATE","data":{"biz_type":"cny_quiz_guide","biz_id":"ffffffff-ffff-ffff-ffff-ffffffffffff","card_url":"https://live.xxx.com/p/html/common-active-pendant/index.html#/","card_expire_time":45000,"priority":1,"card_width":302,"card_height":92,"immediately_show":true,"round_radius":9.63,"random_display_delay_range":{"min":0,"max":10000},"only_pad":true}}
```
---
### PK_ALL
[TOP](#直播弹幕)  
文档更新：xxxx-xx-xx  
PK_AGAIN  
PK_BATTLE_CRIT  
PK_BATTLE_END  
PK_BATTLE_ENTRANCE  
PK_BATTLE_FINAL_PROCESS  
PK_BATTLE_GIFT  
PK_BATTLE_MATCH_TIMEOUT  
PK_BATTLE_MULTIPLE_AWARD  
PK_BATTLE_PRE_NEW  
PK_BATTLE_PRO_TYPE  
PK_BATTLE_PROCESS  
PK_BATTLE_PROCESS_NEW  
PK_BATTLE_PUNISH_END  
PK_BATTLE_SETTLE_NEW  
PK_BATTLE_SETTLE_V2  
PK_BATTLE_SPECIAL_GIFT  
PK_BATTLE_START_NEW  
PK_BATTLE_VIDEO_PUNISH_BEGIN  
PK_BATTLE_VIDEO_PUNISH_END  
PK_BATTLE_VOTES_ADD  
PK_END  
PK_MATCH  
PK_MIC_END  
PK_PRE  
PK_PROCESS  
PK_SETTLE  
PK_START  
| key			| type		| value	|
|-|-|-|
| cmd			| str		| |
| data			| obj		| |
| pk_id			| str/num	| |
| pk_status		| num		| |
| roomid		| num		| |
| send_time		| num		| `pk_start_time` |
| timestamp		| num		| TimeStamp(秒) |
#### PK_PRT_2__data
| key				| type		| value	| switch-case	|
|-|-|-|-|
| battle_type		| num		| |
| init_info			| obj		| |
| match_info		| obj		| |
| battle_sub_type	| num		| |
| dm_conf			| obj		| |
| end_win_task		| null/xxx	| |
| face				| str		| |
| final_conf		| obj		| |
| final_hit_votes	| num		| |
| match_type		| num		| |
| pk_countdown		| num		| pk_start_time + 290	|
| pk_end_time		| num		| pk_start_time + 310	|
| pk_frozen_time	| num		| pk_start_time + 300	|
| pk_start_time		| num		| |
| pk_votes_add		| num		| |
| pk_votes_name		| str		| |
| pk_votes_type		| num		| |
| pre_timer			| num		| |
| room_id			| num		| |
| season_id			| num		| |
| show_streak		| bool		| |
| star_light_msg	| str		| |
| timer				| num		| |
| uid				| num		| |
| uname				| str		| |
#### PK_PRT_2__data__match_info
| key			| type		| value	|
|-|-|-|
| room_id		| num		| 我方直播间id or 对方直播间id |
| votes			| num		| |
| best_uname	| num		| 最高贡献者-昵称 |
| vision_desc	| num		| |
| assist_info	| null/obj	| |
#### PK_PRT_2__data__match_info__assist_info
| key			| type		| value	|
|-|-|-|
| award_content	| str		| |
| face			| str		| |
| is_mystery	| bool		| |
| rank			| num		| |
| uid			| num		| |
| uinfo			| null/obj	| |
| uname			| str		| |
#### PK_PRT_2__data__final_conf
| key 3			| type	| value	|
|-|-|-|
| end_time		| num	| |
| start_time	| num	| pk_start_time + 120 |
| switch		| num	| pk_start_time + 180 |
```json
{"cmd":"PK_BATTLE_END","data":{"battle_sub_type":xxx,"battle_type":xxx,"dm_conf":{"bg_color":"#72C5E2","font_color":"#FFE10B"},"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":"1","score":"xxx","uid":"xxx","uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"votes":xxx,"winner_type":-1},"match_info":{"assist_info":[{"award_content":"获得限量气泡框、头像框和进场特效奖励~","face":"xxx","is_mystery":false,"rank":"1","score":"xxx","uid":"xxx","uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"votes":xxx,"winner_type":xxx},"show_streak":false,"timer":xxx},"pk_id":"xxx","pk_status":xxx,"send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_END","data":{"battle_sub_type":xxx,"battle_type":xxx,"dm_conf":{"bg_color":"#72C5E2","font_color":"#FFE10B"},"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":"1","score":"xxx","uid":"xxx","uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"votes":xxx,"winner_type":xxx},"match_info":{"assist_info":[],"best_uname":"","room_id":xxx,"votes":xxx,"winner_type":-1},"show_streak":false,"timer":xxx},"pk_id":"xxx","pk_status":xxx,"send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_END","data":{"battle_type":xxx,"timer":xxx,"init_info":{"room_id":xxx,"votes":xxx,"winner_type":xxx,"best_uname":"xxx"},"match_info":{"room_id":xxx,"votes":xxx,"winner_type":-1,"best_uname":"xxx"}}}
{"cmd":"PK_BATTLE_ENTRANCE","timestamp":xxxxxxxxxx,"data":{"is_open":false}}
{"cmd":"PK_BATTLE_ENTRANCE","timestamp":xxxxxxxxxx,"data":{"is_open":true}}
{"cmd":"PK_BATTLE_FINAL_PROCESS","data":{"battle_type":xxx,"pk_frozen_time":xxx},"pk_id":xxx,"pk_status":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_MATCH_TIMEOUT","data":{"battle_type":2}}
{"cmd":"PK_BATTLE_MULTIPLE_AWARD","data":{"pkid":xxx,"pk_status":xxx,"award_room":xxx,"award_no":xxx,"award_name":"0","award_value":xxx,"multiple_time":0,"start_time":xxx,"end_time":xxx,"status":xxx}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":xxx,"pk_status":xxx,"status_msg":"","timestamp":xxxxxxxxxx,"data":{"is_followed":xxx,"uname":"xxx","face":"xxx","uid":xxx,"room_id":xxx,"season_id":xxx,"pre_timer":xxx,"pk_votes_name":"","end_win_task":null,"battle_type":xxx,"match_type":xxx}}
{"cmd":"PK_BATTLE_PRE_NEW","pk_id":xxx,"pk_status":xxx,"status_msg":"","timestamp":xxxxxxxxxx,"data":{"is_followed":xxx,"uname":"xxx","face":"xxx","uid":xxx,"room_id":xxx,"season_id":xxx,"pre_timer":xxx,"pk_votes_name":"PK值","end_win_task":null,"battle_type":xxx,"match_type":xxx,"battle_sub_type":0},"template_id":"multi_conn_grid"}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":xxx,"pk_id":xxx,"timestamp":xxxxxxxxxx,"data":{"battle_type":xxx,"match_type":xxx,"battle_sub_type":0,"uname":"xxx","face":"xxx","uid":xxx,"room_id":xxx,"season_id":xxx,"pre_timer":xxx,"pk_votes_name":"PK值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PRE_NEW","pk_status":xxx,"pk_id":xxx,"timestamp":xxxxxxxxxx,"data":{"battle_type":xxx,"match_type":xxx,"uname":"xxx","face":"xxx","uid":xxx,"room_id":xxx,"season_id":xxx,"pre_timer":xxx,"pk_votes_name":"乱斗值","end_win_task":null},"roomid":xxx}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":xxx,"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":xxx,"uid":xxx,"uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"vision_desc":xxx,"votes":xxx},"match_info":{"assist_info":[{xxx}],"best_uname":"xxx","room_id":xxx,"vision_desc":xxx,"votes":xxx},"trace_id":"{128bit}"},"pk_id":xxx,"pk_status":xxx,"send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_PROCESS_NEW","data":{"battle_type":xxx,"init_info":{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":xxx,"uid":xxx,"uinfo":xxx,"uname":"xxx"}],"best_uname":"xxx","room_id":xxx,"vision_desc":xxx,"votes":xxx},"match_info":{"assist_info":null,"best_uname":"","room_id":xxx,"vision_desc":xxx,"votes":xxx},"trace_id":"xxxxxxxxxxxxxfffffff"},"pk_id":xxx,"pk_status":xxx,"send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_PUNISH_END","data":{"battle_sub_type":0,"battle_type":xxx},"pk_id":xxx,"pk_status":xxx,"send_time":xxx,"status_msg":"","template_id":"multi_conn_grid","timestamp":xxx}
{"cmd":"PK_BATTLE_SETTLE_V2","pk_id":xxx,"pk_status":401,"settle_status":1,"timestamp":xxx,"data":{"pk_id":"xxx","season_id":66,"pk_type":2,"result_type":2,"result_info":{"total_score":xxx,"pk_votes":xxx,"pk_votes_name":"PK值","pk_extra_value":0},"level_info":{"uid":"455592866","first_rank_name":"青铜萌新","second_rank_num":2,"first_rank_img":"https://i0.hdslb.com/bfs/live/bd6ca767900adbda7cd7148db06f72726bef7813.png","second_rank_icon":"https://i0.hdslb.com/bfs/live/1f8c2a959f92592407514a1afeb705ddc55429cd.png"},"assist_list":[{"id":xxx,"uname":"xxx","face":"x","score":60},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx},{"id":xxx,"uname":"xxx","face":"xxx","score":xxx}],"star_light_msg":""}}
{"cmd":"PK_BATTLE_SETTLE","pk_id":xxx,"pk_status":401,"settle_status":1,"timestamp":xxx,"data":{"battle_type":2,"result_type":2,"star_light_msg":""},"roomid":"xxx"}
{"cmd":"PK_BATTLE_START_NEW","data":{"battle_sub_type":0,"battle_type":xxx,"final_conf":{"end_time":xxx,"start_time":xxx,"switch":xxx},"final_hit_votes":0,"init_info":{"date_streak":xxx,"room_id":AAAA},"match_info":{"date_streak":xxx,"room_id":BBBB},"pk_countdown":xxx,"pk_end_time":xxx,"pk_frozen_time":xxx,"pk_start_time":xxx,"pk_votes_add":0,"pk_votes_name":"PK值","pk_votes_type":0,"star_light_msg":""},"pk_id":xxx,"pk_status":xxx,"roomid":"xxx","send_time":xxx,"timestamp":xxx}
{"cmd":"PK_BATTLE_START_NEW","pk_id":xxx,"pk_status":xxx,"timestamp":xxx,"data":{"battle_type":xxx,"final_hit_votes":0,"pk_start_time":xxx,"pk_frozen_time":xxx,"pk_end_time":xxx,"pk_votes_type":0,"pk_votes_add":0,"pk_votes_name":"乱斗值","star_light_msg":"","pk_countdown":xxx,"final_conf":{"switch":xxx,"start_time":xxx,"end_time":xxx},"init_info":{"room_id":xxx,"date_streak":xxx},"match_info":{"room_id":xxx,"date_streak":xxx}},"roomid":"xxx"}
{"cmd":"PK_BATTLE_VIDEO_PUNISH_BEGIN","pk_id":"xxx","pk_status":xxx,"timestamp":xxx,"data":{"battle_type":xxx,"init_info":{"room_id":xxx,"votes":xxx,"winner_type":-1,"best_uname":"xxx"},"match_info":{"room_id":xxx,"votes":xxx,"winner_type":xxx,"best_uname":"xxx"},"video_punish":{"duration":xxx,"punish_name":"惩罚"}}}
{"cmd":"PK_BATTLE_VIDEO_PUNISH_END","pk_id":"xxx","pk_status":xxx,"timestamp":xxx}
{"cmd":"PK_INFO","data":{"audience_open":false,"invite_pk_resp":null,"members":[{"assist_info":[{"award_content":"","face":"xxx","is_mystery":false,"rank":1,"uid":xxx,"uname":"xxx"},{"award_content":"","face":"xxx","is_mystery":false,"rank":2,"uid":xxx,"uname":"xxx"}],"capsules":null,"date_streak":0,"face":"xxx","golds":xxx,"group_id":0,"is_follow":0,"is_latest_streak":false,"is_winner":1,"pk_cards":null,"pk_multiple_status":0,"power":"","rank":1,"room_id":xxx,"status":xxx,"uid":xxx,"uname":"xxx","votes":0,"votes_text":"0"},{"assist_info":null,"capsules":null,"date_streak":0,"face":"xxx","golds":0,"group_id":0,"is_follow":0,"is_latest_streak":false,"is_winner":0,"pk_cards":null,"pk_multiple_status":0,"power":"","rank":2,"room_id":xxx,"status":3,"uid":xxx,"uname":"xxx","votes":0,"votes_text":"0"}],"mill_timestamp":xxx,"pk_basic":{"biz_session_id":"xxx","end_time":xxx,"init_id":xxx,"init_uid":xxx,"main_page":"xxx","muti_pk_type":4,"pk_id":xxx,"punish_end_time":xxx,"punish_text":"惩罚","satellite_info":null,"season_id":82,"sprint_duration":10,"start_time":xxx,"status":xxx,"status_msg":"","sub_type":xxx,"template_id":"multi_conn_grid","type":6},"pk_group":null,"pk_match_info":null,"pk_play":{"dm_conf":{"bg_color":"#72C5E2","font_color":"#FFE10B"},"pk_play_text":"比拼伪音","pk_punish_text":"大冒险","pk_text_enabled":true,"pk_text_hash":xxx,"pre_duration":10},"timestamp":xxx}}
```
---
### ROOM_REFRESH
[TOP](#直播弹幕)  
文档更新：2024-11-01  
TODO!  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ROOM_REFRESH" |
| time		| num	| |
```json
{"cmd":"ROOM_REFRESH","time":xxx}
```
---
### WIDGET_WISH_INFO
[TOP](#直播弹幕)  
文档更新：2025-07-28  
礼物星球  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "WIDGET_WISH_INFO" "WIDGET_WISH_INFO_V2" |
| data		| obj	| |
#### WIDGET_WISH_INFO__data
| key		| type	| value	|
|-|-|-|
| data		| xxx	| |
```json
{
	"cmd":"WIDGET_WISH_INFO_V2",
	"data":{
		"sid":xxx,
		"wish":[
			{"gift_id":xxx,"target_num":xxx,"current_num":xxx,"gift_img":"https://s1.hdslb.com/bfs/live/xxx.png","gift_price":xxx,"gift_name":"xxx","wish_status":1},
			{"gift_id":10003,"target_num":xxx,"gift_img":"https://i0.hdslb.com/bfs/activity-plat/static/20220125/7f8dc1e417a6c1d6a509a66770dc060e/ohMHzbhJdN.png","gift_price":198000,"gift_name":"舰长","wish_status":1,"type":1}
		],
		"jump_url":"https://live.xxx.com/p/html/bilili-page-gift-wishes-mix-planet/user.html?...",
		"wish_status":1,"card_text":"主播今日心愿还未完成","modal_text":"今日心愿礼物","button_text":"去助力","show_time":5,"ts":xxx,"tid":xxx,
		"wish_status_info":[
			{"wish_status_msg":"礼物星球待点亮","wish_status_img":"https://i0.hdslb.com/bfs/live/e507f8b101289b2ce6741880a28304215a65f5bf.png","wish_status":-1},
			{"wish_status_msg":"今日心愿暂未达成","wish_status_img":"https://i0.hdslb.com/bfs/live/e507f8b101289b2ce6741880a28304215a65f5bf.png","wish_status":1},
			{"wish_status_msg":"今日心愿已达成","wish_status_img":"https://i0.hdslb.com/bfs/live/e507f8b101289b2ce6741880a28304215a65f5bf.png","wish_status":2,"wish_status_desc":"已完成"}
		],
		"daily_default":true,"wish_name":"xxx",
		"anchor_jump_url":"https://live.xxx.com/p/html/bilili-page-gift-wishes-mix-planet/anchor.html?..."
	}
}
```
---
### OTHER_SLICE_LOADING_RESULT
[TOP](#直播弹幕)  
文档更新：2024-12-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OTHER_SLICE_LOADING_RESULT" |
| data		| obj	| |
#### OTHER_SLICE_LOADING_RESULT__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"OTHER_SLICE_LOADING_RESULT","data":{"data":[{"start_time":xxx,"end_time":xxx,"stream":"","type":xxx,"ban_ec":false}],"live_key":"xxx"}}
```
---
### ANCHOR_LOT_NOTICE
[TOP](#直播弹幕)  
文档更新：2024-11-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "ANCHOR_LOT_NOTICE" |
| data		| obj	| |
#### ANCHOR_LOT_NOTICE__data
| key			| type	| value	|
|-|-|-|
| notice_type	| xxx	| |
| lottery_card	| xxx	| |
```json
{"cmd":"ANCHOR_LOT_NOTICE","data":{"lottery_card":{"icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积","show_time":30,"button_text":"去发奖"},"notice_type":1}}
{"cmd":"ANCHOR_LOT_NOTICE","data":{"lottery_card":{"show_time":30,"button_text":"去发奖","icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积"},"notice_type":1}}
{"cmd":"ANCHOR_LOT_NOTICE","data":{"notice_type":1,"lottery_card":{"button_text":"去发奖","icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积","show_time":30}}}
{"cmd":"ANCHOR_LOT_NOTICE","data":{"notice_type":1,"lottery_card":{"icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积","show_time":30,"button_text":"去发奖"}}}
{"cmd":"ANCHOR_LOT_NOTICE","data":{"notice_type":1,"lottery_card":{"show_time":30,"button_text":"去发奖","icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积"}}}
{"cmd":"ANCHOR_LOT_NOTICE","data":{"notice_type":1,"lottery_card":{"title":"发天选有助于人气累积","show_time":30,"button_text":"去发奖","icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png"}}}
{"data":{"lottery_card":{"icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积","show_time":30,"button_text":"去发奖"},"notice_type":1},"cmd":"ANCHOR_LOT_NOTICE"}
{"data":{"notice_type":1,"lottery_card":{"icon":"https://i0.hdslb.com/bfs/live/95970204111233f181fc28622502aaf1a9359b9a.png","title":"发天选有助于人气累积","show_time":30,"button_text":"去发奖"}},"cmd":"ANCHOR_LOT_NOTICE"}
```
---
### RECALL_DANMU_MSG
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RECALL_DANMU_MSG" |
| data		| obj	| |
#### RECALL_DANMU_MSG__data
| key			| type	| value	|
|-|-|-|
| recall_type	| num	| |
| data			| num	| |
```json
{"cmd":"RECALL_DANMU_MSG","data":{"recall_type":2,"target_id":xxx}}
```
```javascript
enum recall_type={NOTHING:0,DANMAKU:1,USER:2,ALL:3}
```
---
### OTHER_SLICE_SETTING_CHANGED
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "OTHER_SLICE_SETTING_CHANGED" |
| data		| obj	| |
#### OTHER_SLICE_SETTING_CHANGED__data__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"OTHER_SLICE_SETTING_CHANGED","data":{"data":{"uid":xxx,"allow_other_edit":1}}}
```
---
### TAB_LONG_LIVE_CHANGE
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "TAB_LONG_LIVE_CHANGE" |
| data		| obj	| |
#### TAB_LONG_LIVE_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"TAB_LONG_LIVE_CHANGE","data":{"old_room_id":xxx,"new_room_id":yyy,"scatter_time":xxx}}
```
---
### CNY_SESSION_CHANGE
[TOP](#直播弹幕)  
文档更新：2025-01-01  
2025春节专用  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "CNY_SESSION_CHANGE" |
| data		| obj	| |
---
### UNIVERSAL_EVENT_GIFT_V2
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "UNIVERSAL_EVENT_GIFT_V2" |
| data		| obj	| |
```json
{"cmd":"UNIVERSAL_EVENT_GIFT_V2","data":{"biz_session_id":"xxx","interact_channel_id":"xxx","interact_template":{"template_id":"multi_conn_grid","show_interact_ui":false,"layout_id":"left1_right1"},"members":[{"uid":xxx,"uname":"xxx","face":"xxx","position":0,"join_time":xxx,"link_id":"xxx","gender":1,"room_id":xxx,"fans_num":0,"display_name":"本房主播","biz_extra_data":{"multi_conn":{"price":xxx,"price_text":"xxx"}}},{"uid":xxx,"uname":"xxx","face":"xxx","position":1,"join_time":xxx,"link_id":"xxx","gender":0,"room_id":xxx,"fans_num":0,"display_name":"xxx","biz_extra_data":{"multi_conn":{"price":xxx,"price_text":"xxx"}}}],"stream_control":null,"version":xxx,"session_status":1,"business_label":"universal_multi_conn","invoking_time":2,"members_version":xxx,"room_status":1,"system_time_unix":xxx,"room_owner":xxx,"session_start_at":"xxx-xxx-xxx xxx:xxx:xxx","session_start_at_ts":xxx,"room_start_at":"xxx-xxx-xxx xxx:xxx:xxx","room_start_at_ts":xxx,"trace_id":"xxx","biz_extra_data":{"multi_conn":{"show_score":1,"support_full_zoom":2}},"channel_users":[xxx,xxx]}}
{"cmd":"UNIVERSAL_EVENT_GIFT_V2","data":{"biz_session_id":"xxx","interact_channel_id":"xxx","interact_template":{"template_id":"multi_conn_grid","show_interact_ui":true,"layout_id":"left1_right1"},"members":[{"uid":xxx,"uname":"xxx","face":"xxx","position":0,"join_time":xxx,"link_id":"xxx","gender":1,"room_id":xxx,"fans_num":0,"display_name":"本房主播","biz_extra_data":{"multi_conn":{"price":xxx,"price_text":"xxx"}}},{"uid":xxx,"uname":"xxx","face":"xxx","position":1,"join_time":xxx,"link_id":"xxx","gender":0,"room_id":xxx,"fans_num":0,"display_name":"xxx","biz_extra_data":{"multi_conn":{"price":xxx,"price_text":"xxx"}}}],"stream_control":null,"version":xxx,"session_status":1,"business_label":"universal_multi_conn","invoking_time":2,"members_version":xxx,"room_status":1,"system_time_unix":xxx,"room_owner":xxx,"session_start_at":"xxx-xxx-xxx xxx:xxx:xxx","session_start_at_ts":xxx,"room_start_at":"xxx-xxx-xxx xxx:xxx:xxx","room_start_at_ts":xxx,"trace_id":"xxx","biz_extra_data":{"multi_conn":{"show_score":1,"support_full_zoom":1}},"channel_users":[xxx,xxx]}}
```
---
### RADIO_BACKGROUND
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "RADIO_BACKGROUND" |
| data		| obj	| |
#### RADIO_BACKGROUND__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"RADIO_BACKGROUND","data":{"background_url":"https://i0.hdslb.com/bfs/live/5712fbec7dcda4a9509a47001172aab352782dc2.png","background_type":0,"video_url":""}}
```
---
### master_qn_strategy_chg
[TOP](#直播弹幕)  
文档更新：2025-01-01  
```json
{"cmd":"master_qn_strategy_chg","data":"{\"mtime\":xxx,\"scatter\":[0,300]}"}
{"mtime":xxx,"scatter":[0,300]}
```
---
### PLAYURL_RELOAD
[TOP](#直播弹幕)  
文档更新：2025-07-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PLAYURL_RELOAD" |
| data		| obj	| |
#### PLAYURL_RELOAD__data
| key			| type	| value	|
|-|-|-|
| reload_option	| obj	| |
| playurl		| obj	| |
```json
{
	"cmd":"PLAYURL_RELOAD",
	"data":{
		"reload_option":{"reload_stream_name":[],"reload_format":[],"scatter":3000},
		"playurl":{
			"cid":xxx,
			"g_qn_desc":[
				{"qn":30000,"desc":"杜比","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":null},
				{"qn":20000,"desc":"4K","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":null},
				{"qn":10000,"desc":"原画","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":{"detail_desc":{"desc":"1080P 原画","tag":["高帧率"]},"brief_desc":{"desc":"1080P","badge":"原画"}}},
				{"qn":10000,"desc":"原画","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":{"detail_desc":{"desc":"1080P 原画"},"brief_desc":{"desc":"1080P","badge":"原画"}}},
				{"qn":400,"desc":"蓝光","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":{"detail_desc":{"desc":"1080P 蓝光"},"brief_desc":{"desc":"1080P"}}},
				{"qn":250,"desc":"超清","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":{"detail_desc":{"desc":"720P 超清"},"brief_desc":{"desc":"720P"}}},
				{"qn":250,"desc":"超清","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":null},
				{"qn":150,"desc":"高清","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":null},
				{"qn":80,"desc":"流畅","hdr_desc":"","attr_desc":null,"hdr_type":0,"media_base_desc":null}
			],
			"stream":[
				{
					"protocol_name":"http_stream",
					"format":[
						{"format_name":"flv","codec":[{"codec_name":"xxx","current_qn":xxx,"accept_qn":...,"base_url":"","url_info":[],"hdr_qn":null,"dolby_type":0,"attr_name":"","hdr_type":0,"drm":false}],"master_url":""}
					]
				},
				{
					"protocol_name":"http_hls",
					"format":[
						{"format_name":"fmp4","codec":[{"codec_name":"xxx","current_qn":xxx,"accept_qn":...,"base_url":"","url_info":[],"hdr_qn":null,"dolby_type":0,"attr_name":"","hdr_type":0,"drm":false},],"master_url":""},
						{"format_name":"ts","codec":[{"codec_name":"xxx","current_qn":xxx,"accept_qn":...,"base_url":"","url_info":[],"hdr_qn":null,"dolby_type":0,"attr_name":"","hdr_type":0,"drm":false}],"master_url":""}
					]
				}
			],
			"p2p_data":{"p2p":false,"p2p_type":0,"m_p2p":false,"m_servers":null},"dolby_qn":null
		}
	}
}
{
	"http_stream": {
		"flv": {
			"codec_name": ["avc","hevc"], // one-of 
		}
	},
	"http_hls": {
		"fmp4": {
			"codec_name": ["av1","avc","hevc"], // one-of 
		},
		"ts": {
			"codec_name": ["avc","hevc"], // one-of 
		}
	},
	"#ALL":{
		"current_qn": [10000,400,250], // one-of 
		"accept_qn": [...] // from top to end [start : -1] eg:[10000],[10000,250],[10000,400,250],[400,250],[250]
	}
}```
---
### HALF_SCREEN_TRIGGER
[TOP](#直播弹幕)  
文档更新：2025-01-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "HALF_SCREEN_TRIGGER" |
| data		| obj	| |
#### HALF_SCREEN_TRIGGER__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"HALF_SCREEN_TRIGGER","data":{"title":"开百万福袋 来必得","half_screen_url":"https://www.xxx.com/blackboard/era/anniversary16-lottery.html?-Abrowser=live&is_live_half_webview=1&hybrid_rotate_d=1&is_cling_player=1&hybrid_half_ui=1,3,100p,70p,0,1,30,100;2,2,375,100p,0,1,30,100;3,3,100p,70p,0,1,30,100;4,2,375,100p,0,1,30,100;5,3,100p,70p,0,1,30,100;6,3,100p,70p,0,1,30,100;7,3,100p,70p,0,1,30,100;8,3,100p,70p,0,1,30,100&pc_ui=375,626,17181a,2&hybrid_biz=2025-626-activity-lottery-page&room_id=544641&uid=8047632#/anniversary16-lottery","scatter_seconds":15}}
```
---
### PROGRAM_CHANGE
[TOP](#直播弹幕)  
文档更新：2025-07-10  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "PROGRAM_CHANGE" |
| data		| obj	| |
#### PROGRAM_CHANGE__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"PROGRAM_CHANGE","data":{"room_id":5440,"link":""}}
```
---
### VOICE_JOIN_SWITCH
[TOP](#直播弹幕)  
文档更新：2025-07-28  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "VOICE_JOIN_SWITCH" |
| data		| obj	| |
| room_id	| num	| |
#### VOICE_JOIN_SWITCH__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"VOICE_JOIN_SWITCH","data":{"room_id":xxx,"room_status":0,"root_status":0,"conn_type":0,"anchor_uid":0},"room_id":xxx}
{"cmd":"VOICE_JOIN_SWITCH_V2","data":{"room_id":xxx,"room_status":0,"root_status":xxx,"conn_type":xxx,"anchor_uid":xxx},"room_id":xxx}
```
---
### XXXXXXXXXXXX
[TOP](#直播弹幕)  
文档更新：2025-07-01  
| key		| type	| value	|
|-|-|-|
| cmd		| str	| "XXXXXXXXXXXX" |
| data		| obj	| |
#### XXXXXXXXXXXX__data
| key		| type	| value	|
|-|-|-|
| data	| xxx	| |
```json
{"cmd":"XXXXXXXXXXXX","data":{}}
```
---

### others
[TOP](#直播弹幕)  
| key				| type	| value	|
|-|-|-|
| guard_level		| num	| 大航海等级 <br> 0:无 <br> 1:总督GOVERNOR <br> 2:提督PREFECT <br> 3:舰长CAPTAIN |
| privilege_type	| num	| ！待确定 2:提督 3:舰长 |
| lot_status		| num	| 抽奖状态 0:开始 1:正在抽奖 2:开奖 |
| identities		| ...	| 身份 1:"Normal" 2:"管理员" 3:"粉丝" 4:"Vip" 5:"SVip" 6:"舰长" 7:"提督" 8:"总督" 22:"" |

### 粉丝勋章medal_info
[TOP](#直播弹幕)  
| key					| type		| value	| 备注 |
|-|-|-|-|
| anchor_roomid			| num		| 主播 短直播间ID |
| anchor_uname			| str		| 主播名称 |
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

### PUBLIC_uinfo
[TOP](#直播弹幕)  
| key						| type		| value	|
|-|-|-|
| base						| obj		| |
| uid						| num/str	| uid |
| medal						| null/obj	| |
| wealth					| null/obj	| |
| title						| null/obj	| 活动头衔 |
| guard						| null/obj	| |
| uhead_frame				| null/obj	| |
| guard_leader				| null/obj	| 舰队指挥官 |
#### PUBLIC_uinfo__wealth
| key						| type		| value	|
|-|-|-|
| level						| num		| |
| dm_icon_key				| str		| |
#### PUBLIC_uinfo__title
| key						| type		| value	|
|-|-|-|
| old_title_css_id			| str		| |
| title_css_id				| str		| |
#### PUBLIC_uinfo__guard
| key						| type		| value	|
|-|-|-|
| expired_str				| str		| 过期时间 |
| level						| num		| [大航海等级](#others) |
#### PUBLIC_uinfo__guard_leader
| key						| type		| value	|
|-|-|-|
| is_guard_leader			| bool		| |
#### PUBLIC_uinfo__uhead_frame
| key						| type		| value	|
|-|-|-|
| id						| num		| |
| frame_img					| str		| |
#### PUBLIC_uinfo__medal
| key						| type		| value	|
|-|-|-|
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
| user_receive_count		| num		| |
| v2_medal_color_start		| str		| #RRGGBBAA |
| v2_medal_color_end		| str		| #RRGGBBAA |
| v2_medal_color_border		| str		| #RRGGBBAA |
| v2_medal_color_text		| str		| #RRGGBBAA |
| v2_medal_color_level		| str		| #RRGGBBAA |
#### PUBLIC_uinfo__base
| key						| type		| value	|
|-|-|-|
| face						| obj		| 头像(URL) |
| is_mystery				| bool		| |
| name						| str		| 昵称 |
| name_color				| num		| |
| name_color_str			| str		| #RRGGBB |
| risk_ctrl_info			| null/obj	| |
| origin_info				| obj		| |
| official_info				| obj		| 主站: 认证信息 |
##### PUBLIC_uinfo__base__origin_info
| key						| type		| value	|
|-|-|-|
| face						| obj		| 头像(URL) |
| name						| str		| 昵称 |
##### PUBLIC_uinfo__base__risk_ctrl_info
| key						| type		| value	|
|-|-|-|
| face						| obj		| 头像(URL) |
| name						| str		| 昵称 |
##### PUBLIC_uinfo__base__official_info
| key						| type		| value	|
|-|-|-|
| role						| num		| 0:无 7:个人认证 3:机构认证 |
| title						| str		| 认证说明 |
| desc						| str		| |
| type						| num		| -1:无 0:个人认证 1:机构认证 |
#### PUBLIC_uinfo_json
```json
"xxx__uinfo":{
	"uid":xxx,
	"base":{
		"name":"xxx",
		"face":"xxx",
		"name_color":0,
		"is_mystery":false,
		"origin_info":{"face":"xxx","name":"xxx"},
		"risk_ctrl_info":{"face":"xxx","name":"xxx"},
		"official_info":null,
		"official_info":{"role":0,"desc":"","title":"","type":-1},
		"official_info":{"role":7,"desc":"","title":"bilibili直播高能主播","type":0},
		"official_info":{"role":7,"desc":"","title":"专栏优质UP主","type":0},
		"official_info":{"role":1,"desc":"","title":"bilibili 知名〇〇UP主、直播高能主播","type":0},
		"official_info":{"role":1,"desc":"","title":"bilibili 知名〇〇UP主","type":0},
		"official_info":{"role":1,"desc":"","title":"bilibili 知名UP主","type":0},
	},
	"medal":{
		"name":"粉丝团",
		"level":xx,
		"color_start":xxx,"color_end":xxx,"color_border":xxx,"color":xxx,
		"id":0,
		"typ":0,
		"is_light":x,
		"ruid":xxx,
		"guard_level":x,
		"score":xxx,
		"guard_icon":"https://i0.hdslb.com/bfs/live/xxx.png",
		"honor_icon":"",
		"v2_medal_color_border":"#XXXXXXXX",
		"v2_medal_color_end":"#XXXXXXXX",
		"v2_medal_color_level":"#XXXXXXXX",
		"v2_medal_color_start":"#XXXXXXXX",
		"v2_medal_color_text":"#FFFFFFFF",
		"user_receive_count":0,
	},
	"wealth":{"level":xxx,"dm_icon_key":""},
	"title":{"old_title_css_id":"","title_css_id":""},
	"guard":{"level":xxx,"expired_str":"20xx-xx-xx 23:59:59"},
	"uhead_frame":null,
	"uhead_frame":{"id":xxx,"frame_img":"https://i0.hdslb.com/bfs/live/xxx.png"},
	"guard_leader":{"is_guard_leader":false}
}
```

### medal_score
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
| LVL	| medal_color | medal_color_border | medal_color_end | medal_color_start |
| - | -: | -: | -: | -: |
| gray		| 12632256	| 12632256	| 12632256	| 12632256	|
| 0			| 0 | 0 | 0 | 0 |
| 1 - 4		| 6067854	| 6067854	| 6067854	| 6067854	|
| 5 - 8		| 6126494	| 6126494	| 6126494	| 6126494	|
| 9 -12		| 9272486	| 9272486	| 9272486	| 9272486	|
| 13-16		| 12478086	| 12478086	| 12478086	| 12478086	|
| 17-20		| 13081892	| 13081892	| 13081892	| 13081892	|
| 21-24	无	| 1725515	| 1725515	| 5414290	| 1725515	|
| 21-24 舰	| 1725515	| 1725515	| 5414290	| 6809855	|
| 21-24 提	| 1725515	| 1725515	| 5414290	| ????????	|
| 21-24 总	| -	| -	| -	| -	|
| 25-28	无	| 398668	| 398668	| 6850801	| 398668	|
| 25-28 舰	| 398668	| 398668	| 6850801	| 6809855	|
| 25-28 提	| 398668	| 398668	| 6850801	| 16771156	|
| 25-28 总	| 398668	| 398668	| 6850801	| 16771156	|
| 29-32	无	| 2951253	| 2951253	| 10329087	| 2951253	|
| 29-32 舰	| 2951253	| 2951253	| 10329087	| 6809855	|
| 29-32 提	| 2951253	| 2951253	| 10329087	| 6809855	|
| 29-32 总	| 2951253	| 2951253	| 10329087	| 6809855	|
| 33-36	无	| 7996451	| 7996451	| 15304379	| 7996451	|
| 33-36 舰	| 7996451	| 7996451	| 15304379	| 6809855	|
| 33-36 提	| 7996451	| 7996451	| 15304379	| 16771156	|
| 33-36 总	| 7996451	| 7996451	| 15304379	| 16771156	|
| 37-40	无	| 16736523	| 16736523	| 16765060	| 16736523	|
| 37-40 舰	| 16736523	| 16736523	| 16765060	| 6809855	|
| 37-40 提	| 16736523	| 16736523	| 16765060	| 16771156	|
| 37-40 总	| 16736523	| 16736523	| 16765060	| 16771156	|

### medal_color_v2
| LVL	| v2_medal_color_start | v2_m-c-end | v2_m-c-border | v2_m-c-text | v2_m-c-level |
| - | -: | -: | -: | -: | -: |
| GRAY	| #00000000	| #00000000	| #00000000	| #FFFFFFFF	| #00000000	|
| 0		| #00000000	| #00000000	| #00000000	| #FFFFFFFF	| #00000000	|
| 1 - 4	| #5762A799	| #5762A799	| #5762A799	| #FFFFFFFF	| #000B7099	|
| 5 - 8	| #5866C799	| #5866C799	| #5866C799	| #FFFFFFFF	| #000B7099	|
| 9 -12	| #596FE099	| #596FE099	| #596FE099	| #FFFFFFFF	| #000B7099	|
| 13-16	| #C85DC499	| #C85DC499	| #C85DC499	| #FFFFFFFF	| #59005699	|
| 17-20	| #DC6B6B99	| #DC6B6B99	| #DC6B6B99	| #FFFFFFFF	| #81001F99	|
| 21-24	| #43B3E3CC	| #43B3E3CC	| #5FC7F4FF	| #FFFFFFFF	| #00308C99	|
| 25-28	| #4775EFCC	| #4775EFCC	| #58A1F8FF	| #FFFFFFFF	| #000B7099	|
| 29-32	| #9660E5CC	| #9660E5CC	| #D47AFFFF	| #FFFFFFFF	| #6C00A099	|
| 33-36	| #BE4960CC	| #BE4960CC	| #F18087FF	| #FFFFFFFF	| #91007199	|
| 37-40	| #FF842BCC	| #FF842BCC	| #FFCE20FF	| #FFFFFFFF	| #C2000099	|

### UNIXts
```
UNIXts(UTC+8)
120 000 0000	2008-01-11 05:20:00
130 000 0000	2011-03-13 15:06:40
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
173 000 0000	2024-10-27 11:33:20
174 000 0000	2025-02-20 05:20:00
175 000 0000	2025-06-15 23:06:40
176 000 0000	2025-10-09 16:53:20

180 000 0000	2027-01-15 16:00:00
```
