# 
## DanmakuElem
| json-name  | id   | type    | protobuf-name | -- |
| -          |   -: |      -: | :-            | :- |
| id         |  1   | int64   | id            | 弹幕ID |
| progress   |  2   | int32   | progress      | 弹幕出现时间 |
| mode       |  3   | int32   | mode          | 弹幕类型 |
| fontsize   |  4   | int32   | fontsize      | 弹幕字号 |
| color      |  5   | uint32  | color         | 弹幕颜色 RGB24 |
| midHash    |  6   | string  | midHash       | 发送者mid hash (CRC32) |
| content    |  7   | string  | content       | 弹幕内容 |
| ctime      |  8   | int64   | ctime         | 发送时间 |
| weight     |  9   | int32   | weight        | 屏蔽等级 |
| action     | 10   | string  | action        | `airborne:[time]`<br>`picture:图像url`(图片弹幕) |
| pool       | 11   | int32   | pool          | |
| idStr      | 12   | string  | idStr         | 弹幕ID(string) |
| attr       | 13   | int32   | attr          | 弹幕属性位 |
| usermid    | 14   | ?int64  | usermid       | 发送者mid |
| likes      | 15   | ?int??  | *likes*       | 点赞数量 |
| test16     | 16   | ?int??  | *test16*      | reply-to-dmid-1 `first:2021-08-07` |
| test17     | 17   | ?int??  | *test17*      | reply-to-dmid-2 `last: 2022-09-05` |
| replyCount | 18   | ?int??  | *reply_count* | |
| test19     | 19   | ?       | *test19*      | ? |
| test20     | 20   | string  | *test20*      | reply-to-dmid-str-1 |
| test21     | 21   | string  | *test21*      | reply-to-dmid-str-2 |
| animation  | 22   | string  | *animation*   | json |
| test23     | 23   | ?       | *test23*      | ? |

### Danmaku:animation
| key            | type   | value     | xxxxxxxxx |
| :-             |     -: |        -: | :-        |
| id             | num    |           | 20004: 图片弹幕<br>20016: ?<br>20018: NFT弹幕 |
| cid            | num    | 0         |           |
| advanced_block | num    | 0         |           |
| animation_attr | num    | 0         | first:2022-11-07 |
| mime           | str    | "image"   |           |
| resource       | str    | **url**   |           |
| scale          | num    | 1         | id==20004 |

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
| name      | id   | type   | desc  |
| :-        |   -: |     -: | :-    |
| id        |  1   | int64  | 弹幕id |
| oid       |  2   | int64  | 视频cid |
| mid       |  3   | int64  | 发送者mid |
| command   |  4   | string | #ACTORFOLLOW# 合作up主<br>#ATTENTION# 关注<br>#GRADE# 评分<br>#LINK# 链接<br>#RESERVE# 预约<br>#UP#<br>#VOTE# 投票 |
| content   |  5   | string | 互动弹幕正文 |
| progress  |  6   | int32  | 出现时间 |
| ctime     |  7   | string | 创建时间 yyyy-MM-dd HH:mm:ss |
| mtime     |  8   | string | 发布时间 yyyy-MM-dd HH:mm:ss |
| extra     |  9   | string | json |
| idStr     | 10   | string | 弹幕id str类型 |

### command:类型
| command (7)   | content   |
| :-            | -         |
| #ACTORFOLLOW# | "合作up主" |
| #ATTENTION#   | "关注弹幕" |
| #GRADE#       | "哔瓣评分" |
| #LINK#        | **自定义内容** |
| #RESERVE#     | "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#          | **自定义内容** |
| #VOTE#        | "投票弹幕" |

### ACTORFOLLOW:合作up主
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-   |
| duration              | num   | |
| posX                  | float | |
| posY                  | float | |
| icon                  | str   | [url][url_01] |
| mid                   | num   | **合作up主 mid** |
| midstr                | str   | **合作up主 mid string** |
| face                  | str   | **合作up主 头像 URL** |

### ATTENTION:关注
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-  |
| duration              | num   | |
| posX                  | float | |
| posY                  | float | |
| icon                  | str   | [url][url_02] |
| type                  | num   | 2 |
| arc_type              | num   | 0 |

### GRADE:评分
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-  |
| msg                   | str   | "哔瓣评分" |
| skin                  | num   | 1<br>2 |
| posX                  | float | |
| posY                  | float | |
| grade_id              | num   | id |
| duration              | num   | 5000? |
| icon                  | str   | [url][url_03] |
| mid_score             | num   | |
| count                 | num   | |
| avg_score             | float | |
| skin_unselected       | str   | skin1: [url][url_04]<br>skin2: [url][url_05] |
| skin_selected         | str   | skin1: [url][url_06]<br>skin2: [url][url_07] |
| skin_font_color       | str   | color<br>skin1: "`#FFB112`"<br>skin2: "`#FA5555`" |
| summary_duration      | num   | 6000 |
| shrink_icon           | str   | [url][url_08] |
| shrink_title          | str   | "推荐" |
| show_status           | num   | 0 |

### LINK:链接
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-   |
| aid                   | num   | **目标视频avid** |
| title                 | str   | **目标视频标题** |
| icon                  | str   | [url][url_09] |
| bvid                  | str   | **目标视频bvid** |
| posX                  | float | |
| posY                  | float | |
| arc_pic               | str   | **目标视频封面** |
| arc_duration          | num   | **目标视频时长** |
| shrink_icon           | str   | [url][url_10] |
| shrink_title          | str   | "视频" |
| show_status           | num   | 0 |
| duration              | num   | |
| arc_type              | num   | 0 |
| jump_url              | str   | "" |

### RESERVE:预约
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-   |
| msg                   | str   | "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| reserve_type          | num   | 1: 视频<br>2: 直播 |
| reserve_id            | num   | id |
| live_stime            | num   | UnixTimeStamp | `reserve_type=2` |
| arc_stime             | num   | UnixTimeStamp | `reserve_type=2` |
| stime                 | num   | UnixTimeStamp | `reserve_type=2` |
| posX                  | float | |
| posY                  | float | |
| duration              | num   | 5000 |
| icon                  | str   | [url][url_11] |
| reserve_count         | num   | **预约人数** |
| reserve_state         | num   | 1 |
| user_state            | bool  | **预约状态** | 需要登录 |
| live_state            | num   | 0: <br> 1:直播中 <br> 2:直播结束 |
| premiere_state        | num   | 0 |
| live_popularity_count | num   | 0 |
| live_popularity_str   | str   | live :"`x.y万人气`" / "`x人看过`/ "`x.y万人看过`"  |
| premiere_online_count | num   | 0 |
| premiere_view         | num   | 0 |
| jump_url              | str   | **视频URL**<br>**直播回放URL**<br>**直播URL** |
| mid                   | num   | **目标视频 UP主mid** |
| live_stime_format     | str   | video: ""<br>live: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| arc_stime_format      | str   | video: ""<br>live: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| stime_format          | str   | video: ""<br>live: "`?(yyyy-)MM-dd HH:mm`" / "`今天HH:mm`" |
| live_lottery          | bool  | `true` |
| desc                  | str   | "" |
| shrink_icon           | str   | [url][url_12] |
| shrink_title          | str   | "预约" |
| show_status           | num   | 0 |

### UP:带有【UP】的~~普通~~弹幕
| key                   | type  | value |
| :-                    | -     | -   - |
| icon                  | str   | **UP主头像URL** |

### VOTE:投票
| key                   | type  | value | 备注 |
| :-                    | -     | -     | :-   |
| vote_id               | num   | id |
| question              | str   | **投票问题** |
| cnt                   | num   | **投票人数** |
| options               | array | **选项** |
| icon                  | str   | [url][url_13] |
| my_vote               | num   | **我的选项** |
| pub_dynamic           | bool  | |
| posX                  | float | |
| posY                  | float | |
| duration              | num   | |
| shrink_icon           | str   | [url][url_14] |
| shrink_title          | str   | "投票" |
| show_status           | num   | 0 |

#### VOTE::options
| key                   | type  | value |
| :-                    | -     | -     |
| idx                   | num   | start:1 |
| desc                  | str   | **选项内容** |
| cnt                   | num   | 0? |
| has_self_def          | bool  | false? |

### posX,posY
| key      | min  | max |
| :-       | -    | -   |
| posX     | 118  | 549 |
| posY     | 80.5 | 889 |

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
