# 
## DanmakuElem
| id	| type		| protobuf-name	| -- |
| -:	| -:		| :-			| :- |
|  1	| int64		| id			| 弹幕ID |
|  2	| int32		| progress		| 弹幕出现时间 |
|  3	| int32		| mode			| 弹幕类型 |
|  4	| int32		| fontsize		| 弹幕字号 |
|  5	| uint32	| color			| 弹幕颜色 RGB24 |
|  6	| string	| midHash		| 发送者mid hash (CRC32) |
|  7	| string	| content		| 弹幕内容 |
|  8	| int64		| ctime			| 发送时间 |
|  9	| int32		| weight		| 屏蔽等级 |
| 10	| string	| action		| `airborne:[time]`<br>`picture:图像url`(图片弹幕) |
| 11	| int32		| pool			| 弹幕池 |
| 12	| string	| idStr			| 弹幕ID(string) |
| 13	| int32		| attr			| 弹幕属性位 |
| 14	| ?int64	| usermid		| 发送者mid |
| 15	| ?int??	| *likes*		| 点赞数量 |
| 16	| ?int??	| *test16*		| 弹幕评论，默认为num:0`first:2021-08-07` |
| 17	| ?int??	| *test17*		| 弹幕评论，默认为num:0`last: 2022-09-05` |
| 18	| ?int??	| *reply_count*	| 弹幕评论数量 |
| 19	| ?			| *test19*		| ? |
| 20	| string	| *test20*		| 弹幕评论，默认为str:"0" |
| 21	| string	| *test21*		| 弹幕评论，默认为str:"0" |
| 22	| string	| animation		| json |
| 23	| ?			| *test23*		| ? |

### Danmaku:animation
| key				| type	| value		| |
| :-				| -:	| -:		| :- |
| id				| num	| 			| 20004: 图片弹幕<br>20016: ?<br>20018: NFT弹幕 |
| cid				| num	| 0			| |
| advanced_block	| num	| 0			| |
| animation_attr	| num	| 0			| first:2022-11-07 |
| mime				| str	| "image"	| |
| resource			| str	| **url**	| |
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

// NFT弹幕
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
| :-		| -:	| -:		| :-	|
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

### command:类型
| command (7)	| content	|
| :-			| -			|
| #ACTORFOLLOW# | "合作up主" |
| #ATTENTION#	| "关注弹幕" |
| #GRADE#		| "哔瓣评分" |
| #LINK#		| **自定义内容** |
| #RESERVE#		| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#			| **自定义内容** |
| #VOTE#		| "投票弹幕" |

### ACTORFOLLOW:合作up主
| key					| type	| value	| 备注	|
| :-					| -		| -		| :-	|
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_01] |
| mid					| num	| **合作up主 mid** |
| midstr				| str	| **合作up主 mid string** |
| face					| str	| **合作up主 头像 URL** |

### ATTENTION:关注
| key					| type	| value | 备注 |
| :-					| -		| -	| :- |
| duration				| num	| |
| posX					| float	| |
| posY					| float	| |
| icon					| str	| [url][url_02] |
| type					| num	| 2 |
| arc_type				| num	| 0 |

### GRADE:评分
| key					| type	| value	| 备注	|
| :-					| -		| -		| :-	|
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
| skin_unselected		| str	| skin1: [url][url_04]<br>skin2: [url][url_05] |
| skin_selected			| str	| skin1: [url][url_06]<br>skin2: [url][url_07] |
| skin_font_color		| str	| color<br>skin1: "`#FFB112`"<br>skin2: "`#FA5555`" |
| summary_duration		| num	| 6000 |
| shrink_icon			| str	| [url][url_08] |
| shrink_title			| str	| "推荐" |
| show_status			| num	| 0 |

### LINK:链接
| key					| type	| value	| 备注	|
| :-					| -		| -		| :-	|
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

### RESERVE:预约
| key                   | type	| value	| 备注	|
| :-                    | -		| -		| :-	|
| msg                   | str	| "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| reserve_type          | num	| 1: 视频<br>2: 直播 |
| reserve_id            | num	| id |
| live_stime            | num	| UnixTimeStamp | `reserve_type=2` |
| arc_stime             | num	| UnixTimeStamp | `reserve_type=2` |
| stime                 | num	| UnixTimeStamp | `reserve_type=2` |
| posX					| float	| |
| posY					| float	| |
| duration				| num	| 5000 |
| icon                  | str	| [url][url_11] |
| reserve_count			| num	| **预约人数** |
| reserve_state			| num	| 1 |
| user_state			| bool 	| **预约状态** | 需要登录 |
| live_state			| num	| 0: <br> 1:直播中 <br> 2:直播结束 |
| premiere_state        | num	| 0 |
| live_popularity_count | num	| 0 |
| live_popularity_str   | str	| 直播 :"`x.y万人气`" / "`x人看过`/ "`x.y万人看过`"  |
| premiere_online_count | num	| 0 |
| premiere_view         | num	| 0 |
| jump_url              | str	| **视频/直播回放 URL**<br>**直播间URL** |
| mid                   | num	| **目标视频 UP主mid** |
| live_stime_format     | str	| 视频: ""<br>直播: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| arc_stime_format      | str	| 视频: ""<br>直播: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| stime_format          | str	| 视频: ""<br>直播: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| live_lottery          | bool 	| `true` |
| desc                  | str	| "" |
| shrink_icon           | str	| [url][url_12] |
| shrink_title          | str	| "预约" |
| show_status           | num	| 0 |

### UP:带有【UP】的~~普通~~弹幕
| key					| type	| value	|
| :-					| -		| -		|
| icon					| str	| **UP主头像URL** |

### VOTE:投票
| key					| type	| value | 备注	|
| :-					| -		| -		| :-	|
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

#### VOTE:options
| key					| type	| value	|
| :-					| -		| -		|
| idx					| num	| start:1 |
| desc					| str	| **选项内容** |
| cnt					| num	| 0? |
| has_self_def			| bool	| false? |

### posX,posY
| key	| min	| max	|
| :-	| -:	| -:	|
| posX	|   118 |   549 |
| posY	|  80.5 |   889 |

## Live
| name | desc |
| :- | - |
| LIVE								| |
| SEND_GIFT							|送礼物|
| ONLINE_RANK_V2					|高能用户TOP7|
| ONLINE_RANK_TOP3					|高能用户前三恭喜|
| ONLINE_RANK_COUNT					| |
| INTERACT_WORD						|进入直播间|
| HOT_RANK_CHANGED_V2				|人气榜排名更改|
| HOT_RANK_CHANGED					|人气榜排名更改|
| WATCHED_CHANGE					|xx人数|
| ROOM_REAL_TIME_MESSAGE_UPDATE		| |
| LIKE_INFO_V3_CLICK				| |
| LIKE_INFO_V3_UPDATE				| |
| HOT_ROOM_NOTIFY					| |
| ENTRY_EFFECT						| 进入直播间特效 |
| STOP_LIVE_ROOM_LIST				| |
| GUARD_BUY							| 舰长购买 |
| USER_TOAST_MSG					| |
| NOTICE_MSG						| |
| HOT_RANK_SETTLEMENT_V2			| 荣登限时热门榜总榜 |
| LIVE | |
| LIVE | |
| LIVE | |
| LIVE | |

### LIVE
| key				| type	| value |
| :- | - | - |
| cmd				| str	| "LIVE" |
| live_key			| str	| ?*int64* |
| voice_background	| str	| ?"" |
| sub_session_key	| str	| `f"{live_key}sub_time:{live_time}"` |
| live_platform		| str	| ?"live_mng" |
| live_model		| num	| ?0 |
| live_time*		| num	| 开播时间UnixTimeStamp(秒) |
| roomid			| num	| 房间号 |
```json
{
	"cmd": "LIVE",
	"live_key": "123456789012345678",
	"voice_background": "",
	"sub_session_key": "123456789012345678sub_time:1234567890",
	"live_platform": "events_broadcast",
	"live_model": 0,
	"live_time": 1234567890, // 仅在开播时存在
	"roomid": 12345
}
```

### SEND_GIFT
送礼物，实时
| key	| type | value |
| :- | - | - |
| cmd	| str	| "SEND_GIFT" |
| data	| obj	| |
#### SEND_GIFT:data(54)
| key					| type	| value | 备注 |
| :- | - | - | - |
| action				| str	| "投喂" |
| **batch_combo_id**	| str	| `f"batch:gift:combo_id:{uid}:{主播uid}:{giftId}:{时间TimeStamp}"` | 时间示例: 1669376481.0755 |
| **batch_combo_id**	| str	| UUID | |
| **batch_combo_send**	| null	| 第一次为 null |
| **batch_combo_send**	| obj	| 其余为 上一个`batch_combo_id` |
| beatId				| str	| "0" |
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
| :- | - | - |
| cmd	| str	| "ONLINE_RANK_V2" |
| data	| obj	| |
#### ONLINE_RANK_V2:data
| key		| type | value |
| :- | - | - |
| list		| arr | |
| rank_type	| str | "gold-rank" |
#### ONLINE_RANK_V2:data:list:(7)obj
| key			| type	| value |
| :- | - | - |
| uid			| num | uid |
| face			| str | 头像URL |
| score			| str | 贡献值 |
| uname			| str | 用户名 |
| rank			| num | 排名(1-7) |
| guard_level	| num | 舰长等级 |

### ONLINE_RANK_TOP3
排行榜前三(左)，实时
| key	| type	| value |
| :- | - | - |
| cmd	| str	| "ONLINE_RANK_TOP3" |
| data	| obj	| |
#### ONLINE_RANK_TOP3:data
| key		| type	| value |
| :- | - | - |
| dmscore	| num	| 112 |
| list		| arr	| |
#### ONLINE_RANK_TOP3:data:list:(1)obj
| key		| type	| value |
| :- | - | - |
| msg		| str	| `f"恭喜 <%{用户名}%> 成为高能用户"` |
| rank		| num	| 排名(1-3) |

### ONLINE_RANK_COUNT
约每5秒发送一次
| key | type | value |
| :- | - | - |
| cmd	| str	| "ONLINE_RANK_COUNT" |
| data	| obj	| |
#### ONLINE_RANK_COUNT:data
| key	| type	| value |
| :- | - | - |
| count | num	| 最大值约为10000[1-100xx] |

### INTERACT_WORD
进入直播间、关注通知，实时
| key | type	| value |
| :- | - | - |
| cmd	| str	| "INTERACT_WORD" |
| data	| obj	| |
#### INTERACT_WORD:data
| key				| type	| value |
| :- | - | - |
| contribution		| obj	| |
| core_user_type	| num	| 大部分为0?[0-5] |
| dmscore			| num	| |
| fans_medal		| obj	| [粉丝牌信息](#粉丝牌信息medal_info) |
| identities		| arr	| |
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
#### INTERACT_WORD:score
msg_type=1: UnixTimeStamp
msg_type=2: 关注时间UnixTimeStamp
#### INTERACT_WORD:core_user_type
1:LV6+,30总督,年度大会员,UL25+，1300follow，55fan  
2:LV6 ,年度大会员,UP40,2.5Mfan,个人认证,百大  
2:LV6 ,年度大会员,30总督,3wfan, 主播28+舰长,25舰长
#### INTERACT_WORD:data:contribution
| key | type	| value |
| :- | - | - |
| grade | num	| 0,1,2,3 |
#### INTERACT_WORD:data:identities
```
[1]
[3,1]
"privilege_type": 3, "identities": [6, 1]
```

### HOT_RANK_CHANGED_V2
计时器每半小时(1800秒)重置一次，计时重置后，约每15秒或(N*15)秒发送一次
| key | type | value |
| :- | - | - |
| cmd	| str	| "HOT_RANK_CHANGED_V2" |
| data	| obj	| |
#### HOT_RANK_CHANGED_V2:data
| key			| type	| value |
| :- | - | - |
| rank			| num	| 排名[1-50] |
| trend			| num	| 0 |
| countdown		| num	| 倒计时[1-1786]|
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
| :- | - | - |
| cmd	| str	| "HOT_RANK_CHANGED" |
| data	| obj	| |
#### HOT_RANK_CHANGED:data
| key			| type	| value |
| :- | - | - |
| rank			| num	| 排名[1-50] |
| trend			| num	| ? |
| countdown		| num	| 倒计时[1-1795]|
| timestamp		| num	| UnixTimeStamp(秒) |
| web_url		| str	| 排行榜URL |
| live_url		| str	| 排行榜URL |
| blink_url		| str	| 排行榜URL |
| live_link_url	| str	| 排行榜URL |
| pc_link_url	| str	| 排行榜URL |
| icon			| str	| 热门:[图像][url_15] <br> 手游:[图像][url_16] |
| area_name		| str	| 分区名称(大分区) |
| rank_desc		| str	| "" |

### WATCHED_CHANGE
约每5秒发送一次
| key | type | value |
| :- | - | - |
| cmd	| str	| "WATCHED_CHANGE" |
| data	| obj	| |
#### WATCHED_CHANGE:data
| key			| type	| value |
| :- | - | - |
| num			| num	| 人数 |
| text_small	| str	| num\<10000:"num" <br> "x.y万" |
| text_large	| str	| num\<10000:"num人看过" <br> "x.y万人看过" |

### ROOM_REAL_TIME_MESSAGE_UPDATE
约每60秒发送一次，更新关注数、粉丝团人数
| key | type | value |
| :- | - | - |
| cmd	| str	| "ROOM_REAL_TIME_MESSAGE_UPDATE" |
| data	| obj	| |
#### ROOM_REAL_TIME_MESSAGE_UPDATE:data
| key			| type	| value |
| :- | - | - |
| roomid		| num	| 直播间ID |
| fans			| num	| 关注 |
| red_notice	| num	| -1? |
| fans_club		| num	|  |

### LIKE_INFO_V3_CLICK
点赞(移动端 双击屏幕)，实时，和`LIKE_INFO_V3_UPDATE`同时发送，实时
| key | type | value |
| :- | - | - |
| cmd	| str	| "LIKE_INFO_V3_CLICK" |
| data	| obj	| |
#### LIKE_INFO_V3_CLICK:data
| key				| type	| value |
| :- | - | - |
| show_area			| num	| 0,1 |
| msg_type			| num	| 6 |
| like_icon			| str	| [图标][img_16]|
| uid				| num	| |
| like_text			| str	| "为主播点赞了" |
| uname				| str	| |
| uname_color		| str	| "" |
| identities		| arr	| |
| fans_medal		| obj	| |
| contribution_info	| obj	| |
| dmscore			| num	| 20 |
#### LIKE_INFO_V3_CLICK:data:contribution_info
| key | type | value |
| :- | - | - |
| grade | num | 0 |

### LIKE_INFO_V3_UPDATE
点赞(移动端 双击屏幕)，实时，和`LIKE_INFO_V3_CLICK`同时发送，实时
| key | type | value |
| :- | - | - |
| cmd	| str	| "LIKE_INFO_V3_UPDATE" |
| data	| obj	| |
#### LIKE_INFO_V3_UPDATE:data
| key | type	| value |
| :- | - | - |
| click_count	| num | |

### HOT_ROOM_NOTIFY
***description***
| key | type | value |
| :- | - | - |
| cmd	| str	| "HOT_ROOM_NOTIFY" |
| data	| obj	| |
#### HOT_ROOM_NOTIFY:data
| key					| type | value |
| :- | - | - |
| threshold				| num | 10000 |
| ttl					| num | 300 |
| exit_no_refresh		| num | 1 |
| random_delay_req_v2	| obj | **固定值** |
#### HOT_ROOM_NOTIFY:data:random_delay_req_v2
| key	| type | value |
| :- | - | - |
| path	| str | |
| delay	| num | |
```json
{"cmd":"HOT_ROOM_NOTIFY","data":{"threshold":10000,"ttl":300,"exit_no_refresh":1,"random_delay_req_v2":[{"path":"/live/getRoundPlayVideo","delay":10},{"path":"/xlive/web-room/v1/index/getOffLiveList","delay":120000}]}}
```

### ENTRY_EFFECT
欢迎舰长、提督、(?)进入直播间，实时(高精度)
| key | type | value |
| :- | - | - |
| cmd	| str	| "ENTRY_EFFECT" |
| data	| obj	| |
#### ENTRY_EFFECT:data(28)
| key						| type | value | |
| :- | - | - | - |
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
| icon_list					| arr	| ~~`copy_writing_v2`内有`"<^icon^>"`时，数组有值 id=136:1,2 id=137:3 identities=22,33:1~~ |
| max_delay_time			| num	| 7 |
| trigger_time				| num	| UnixTimeStamp(皮秒?) |
| identities				| num	| `copy_writing_v2`内有`"<^icon^>,舰长"`时为`33`<br>有`"<^icon^>"`时为`22`<br>`提督`为`7`<br>`舰长`为`6` |
| effect_silent_time		| float	| 0 |
| effective_time_new		| num	| Tag_1 |
| web_dynamic_url_webp		| str	| Tag_1 |
| web_dynamic_url_apng		| str	| Tag_1 |
| mobile_dynamic_url_webp	| str	| Tag_1 |
#### ENTRY_EFFECT:data:id
前缀:`https://i0.hdslb.com/bfs/live/mlive/` 后缀:`.png`**Tag_2**
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
#### ENTRY_EFFECT:data:web_dynamic_url_XXX
前缀:`https://i0.hdslb.com/bfs/live/mlive/`
| XXX	|web_dynamic_url_webp|web_dynamic_url_apng|mobile_dynamic_url_webp| effective_time_new |
|-|-|-|-| -: |
|	1	|`eac404ec584e3b672cc087d86b32700105171c4f.webp`|`0bfc494ce9c02a2ea4d982e9b346d0c7e732f3c0.vnd.mozilla.apng`|`eac404ec584e3b672cc087d86b32700105171c4f.webp`|3
|	2	|`5007b1f4546c137dfbb72316b9744c808902aeb3.webp`|`ed4b66c18a31663b8ebadce6a968fbb4f86f6bd8.apng`|`5007b1f4546c137dfbb72316b9744c808902aeb3.webp`|3.1
|	3	|`15bfdcf4a72f8ba1c8b45a99b6c9e9f53a25e8e1.webp`|`db7f605bc2bf8f6f98d30be134bc653e0a3f4296.vnd.mozilla.apng`|`2c952f4aeb7fef8bd753a468da9c357745fc1402.webp`|4.4
|	4	|`9f1ae49431c526a24f9e87b1b6a898b1028ec645.webp`|`f068957a37d9bd6ec0f3e7907be6db63ae2cfe89.vnd.mozilla.apng`|`9f1ae49431c526a24f9e87b1b6a898b1028ec645.webp`|4.4
|	5	||||
|	6	||||
|	7	||||
|	8	||||
|	9	||||
|	10|	|||

### STOP_LIVE_ROOM_LIST
约每30秒发送一次，推送很多直播间ID?
| key | type | value |
| :- | - | - |
| cmd	| str	| "STOP_LIVE_ROOM_LIST" |
| data	| obj	| |
#### STOP_LIVE_ROOM_LIST:data
| key			| type | value |
| :- | - | - |
| room_id_list	| arr |  |

### GUARD_BUY
舰长购买，实时
| key | type | value |
| :- | - | - |
| cmd	| str	| "GUARD_BUY" |
| data	| obj	| |
#### GUARD_BUY:data(9)
| key			| type | value |
| :- | - | - |
| uid			| num | uid |
| username		| str |  |
| guard_level	| num | [guard_level](#others) |
| num			| num | 1 |
| price			| num | 价格*1000 |
| gift_id		| num | 10003:"舰长" 10002:"提督" 10001:"总督" |
| gift_name		| str |  |
| start_time	| num | start_time=end_time 购买时间 UnixTimeStamp(秒) |
| end_time		| num | start_time=end_time 购买时间 UnixTimeStamp(秒) |

### USER_TOAST_MSG
舰长购买通知，实时，显示在聊天区
| key | type | value |
| :- | - | - |
| cmd	| str	| "USER_TOAST_MSG" |
| data	| obj	| |
#### USER_TOAST_MSG:data(23)
| key					| type	| value |
| :- | - | - |
| anchor_show			| bool	| true |
| color					| str	| "舰长":"#00D1F1" "提督":"#E17AFF" "总督": |
| dmscore				| num	| 90 |
| effect_id				| num	| 397 |
| end_time				| num	| start_time=end_time 购买时间 UnixTimeStamp(秒) |
| face_effect_id		| num	| "舰长":44 "提督":43 "总督": |
| gift_id				| num	| 10003:"舰长" 10002:"提督" 10001:"总督" |
| guard_level			| num	| [guard_level](#others) |
| is_show				| num	| 0 |
| num					| num	| 1? |
| op_type				| num	| 3:PC? 2:iOS 1:Android? |
| payflow_id			| str	| 订单号(25) |
| price					| num	| 价格*1000 连续订阅舰长138，iOS连续订阅舰长158，舰长198，提督1998 |
| role_name				| str	| "舰长" "提督" "总督" |
| room_effect_id		| num	| "舰长":590 "提督":591 "总督": |
| start_time			| num	| start_time=end_time 购买时间 UnixTimeStamp(秒) |
| svga_block			| num	| 0 |
| target_guard_count	| num	| 主播总舰长数 |
| toast_msg				| str	| `f"<%{用户名}%> 自动续费了舰长"` <br> `f"<%{用户名}%> 开通了(舰长|提督|总督)，今天是TA陪伴主播的第{}天"` |
| uid					| num	| uid |
| unit					| str	| "月" |
| user_show				| bool	| true |
| username				| str	| 用户名 |

### NOTICE_MSG
滚动横幅，实时
| key			| type | value |
| :- | - | - |
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
#### NOTICE_MSG:full
| key			| type | value |
| :- | - | - |
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
#### NOTICE_MSG:half
| key			| type | value |
| :- | - | - |
| head_icon		| str	| |
| tail_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| time			| num	| |
#### NOTICE_MSG:side
| key			| type	| value |
| :- | - | - |
| head_icon		| str	| |
| background	| str	| |
| color			| str	| |
| highlight		| str	| |
| border		| str	| |
#### NOTICE_MSG:scatter
| key	| type | value |
| :- | - | - |
| min	| num | 0 |
| max	| num | 0 |
#### NOTICE_MSG:例
<detail>
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
</detail>

### HOT_RANK_SETTLEMENT_V2
每30分(1800秒 `HH:25:05, HH:55:05`)广播一次，荣登限时热门榜总榜topxx
| key | type | value |
| :- | - | - |
| cmd	| str	| "HOT_RANK_SETTLEMENT_V2" |
| data	| obj	| |
#### HOT_RANK_SETTLEMENT_V2:data
| key		| type | value |
| :- | - | - |
| rank		| num	| 排名 |
| uname		| str	| 主播用户名 |
| face		| str	| 主播头像URL |
| timestamp	| num	| UnixTimeStamp(秒) `HH:25:05 HH:55:05` |
| icon		| str	| url_15 |
| area_name	| str	| 分区名称 |
| url		| str	|  |
| cache_key	| str	| 随机值(128bit) |
| dm_msg	| str	| `f"恭喜主播 <% {uname} %> 荣登限时热门榜{总}榜top{rank}! 即将获得热门流量推荐哦！"` `f"恭喜主播 <% {uname} %> 荣登限时热门榜总榜榜首!"` `f"恭喜主播 <% {uname} %> 荣登限时热门榜总榜top{rank}!"` |
```python
url = f"https://live.bilibili.com/p/html/live-app-hotrank/result.html?is_live_half_webview=1&hybrid_half_ui=1,5,250,200,f4eefa,0,30,0,0,0;2,5,250,200,f4eefa,0,30,0,0,0;3,5,250,200,f4eefa,0,30,0,0,0;4,5,250,200,f4eefa,0,30,0,0,0;5,5,250,200,f4eefa,0,30,0,0,0;6,5,250,200,f4eefa,0,30,0,0,0;7,5,250,200,f4eefa,0,30,0,0,0;8,5,250,200,f4eefa,0,30,0,0,0&areaId=0&cache_key={cache_key}"
```
### INTERACT_WORD
| key | type | value |
| :- | - | - |
| cmd	| str	| "XXXXXXXXXXX" |
| data	| obj	| |
#### SEND_GIFT:data
| key                   | type | value |
| :- | - | - |
| data |  | |

### others
| key				| type	| value |
| :- | - | - |
| dmscore			| num	| 偶数? |
| guard_level		| num	| 舰长等级 <br> 0:无 <br> 1:总督 <br> 2:提督 <br> 3:舰长 |
| privilege_type	| num	| 2:提督 3:舰长 |
face:`http(s)?://i[0-3].hdslb.com/bfs/(face|baselabs)/[0-9a-f]{40}.(jpg|png|gif|webp)`  
face:`http(s)?://i0.hdslb.com/bfs/face/member/noface.jpg`

### 粉丝牌信息medal_info
| key					| type	| value | 备注 |
| :-					| - | - | - |
| anchor_roomid			| num	| 0 |
| anchor_uname			| str	| "" |
| guard_level			| num	| [舰长等级](#others) |
| icon_id				| num	| 0 |
| is_lighted			| num	| 0: <br> 1: 最近有直播间互动 |
| medal_color			| num	| int(HEX:RGB24) | [medal_color](#medal_color)
| medal_color_border	| num	| int(HEX:RGB24) |
| medal_color_end		| num	| int(HEX:RGB24) |
| medal_color_start		| num	| int(HEX:RGB24) |
| medal_level			| num	| 粉丝牌 等级 |
| medal_name			| str	| 粉丝团 称号 |
| special				| str	| "" |
| target_id				| num	| 主播uid |

### medal_color
| medal_level	| medal_color | medal_color_border | medal_color_end | medal_color_start | 备注 |
| -:			| -: | -: | -: | -: | :- |
| is_lighted=0	| 12632256	| 12632256	| 12632256	| 12632256	|未互动，灰
|     0　　		| 0 | 0 | 0 | 0 |
|  1- 4　　		| 6067854	| 6067854	| 6067854	| 6067854	|
|  5- 8　　		| 6126494	| 6126494	| 6126494	| 6126494	|
|  9-12　　		| 9272486	| 9272486	| 9272486	| 9272486	|紫
| 13-16　　		| 12478086	| 12478086	| 12478086	| 12478086	|洋红
| 17-20　　		| 13081892	| 13081892	| 13081892	| 13081892	|金
| 21-24	无　	| 1725515	| 1725515	| 5414290	| 1725515	|
| 21-24 舰长	| 1725515	| 1725515	| 5414290	| 6809855	|
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
[url_15]:https://i0.hdslb.com/bfs/live/b4961bcfba56a26b69c35690dfcbdabbeb973c64.png
[url_16]:https://i0.hdslb.com/bfs/live/23678e3d90402bea6a65251b3e728044c21b1f0f.png