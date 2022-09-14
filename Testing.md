# 测试数据
## Proto:DanmakuElem
| json-name  | id   | 数据类型 | protobuf-name | - |
| ---------- | ---: | ------: | :------------ | ------: |
| id         |  1   | int64   | id            |  |
| progress   |  2   | int32   | progress      |  |
| mode       |  3   | int32   | mode          |  |
| fontsize   |  4   | int32   | fontsize      |  |
| color      |  5   | uint32  | color         |  |
| midHash    |  6   | string  | midHash       |  |
| content    |  7   | string  | content       |  |
| ctime      |  8   | int64   | ctime         |  |
| weight     |  9   | int32   | weight        |  |
| action     | 10   | string  | action        |  |
| pool       | 11   | int32   | pool          |  |
| idStr      | 12   | string  | idStr         |  |
| attr       | 13   | int32   | attr          |  |
| usermid    | 14   | ?int64  | usermid       | 测试 |
| likes      | 15   | ?int??  | likes         | 测试 |
| test16     | 16   | ?int??  | test16        | reply-to-dmid-1 测试：？ |
| test17     | 17   | ?int??  | test17        | reply-to-dmid-2 测试：？ |
| replyCount | 18   | ?int??  | reply_count   | 测试 |
| test19     | 19   | ?       | test19        | 正在测试 |
| test20     | 20   | string  | test20        | reply-to-dmid-str-1 测试：？ |
| test21     | 21   | string  | test21        | reply-to-dmid-str-2 测试：？ |
| animation  | 22   | string  | animation     |  |
| test23     | 23   | ?       | test23        | ? |

### protobuf:
```JSON
{"elems": [
	{
		"id": "1234567890123456789",    // 01:  int64 弹幕ID
		"progress": 1,                  // 02:  int32 弹幕出现时间 空:0
		"mode": 1,                      // 03:  int32 弹幕类型
		"fontsize": 25,                 // 04:  int32 弹幕字号
		"color": 16777215,              // 05: uint32 弹幕颜色 RGB24 空:0 [1,16777215]
		"midHash": "XXXXXXXX",          // 06: string 发送者mid hash (CRC32 mid)
		"content": "*****",             // 07: string 弹幕内容
		"ctime": "123456789",           // 08:  int64 发送时间
		"weight": 11,                   // 09:  int32 屏蔽等级 [1,11]
		"action": "",                   // 10: string "airborne:时间(毫秒)" "picture:图像url(图片弹幕)"
		"pool": 1,                      // 11:  int32 弹幕池
		"idStr": "1234567890123456789", // 12: string 弹幕ID
		"attr": 1,                      // 13:  int32 弹幕属性位
		"usermid": "1234567890",        // 14: ?int64 发送者mid
		"likes": 0,                     // 15: ?int?? 点赞数量
		"test16": "",                   // 16:  int64 test16 === test17  !! 指向另一个弹幕 id [first:2021-08-15][last: 2021-11-30]
		"test17": "",                   // 17:  int64 test16 === test17  !! 指向另一个弹幕 id
		"replyCount": "",               // 18: ?int??                    !! 被指向次数
		"test19": "",                   // 19: ?????? -
		"test20": "",                   // 20: string test20 === test21  !! 指向另一个弹幕 idStr
		"test21": "",                   // 21: string test20 === test21  !! 指向另一个弹幕 idStr
		"animation": "",                // 22: string[json] id:[20004(ohh)(图片弹幕),20016,20018(NFT)]
		"test23": ""                    // 23: ?????? -
	}
	// ......
	]
}
```
## animation
| key            | type   | value     | xxxxxxxxx |
| :------------- | -----: | --------: | :-------- |
| id             | num    |           | 20004:图片弹幕<br>20016:?<br>20018:NFT弹幕 |
| cid            | num    | 0         |           |
| advanced_block | num    | 0         |           |
| mime           | str    | ("image") |           |
| resource       | str    | `url`     |           |
| scale          | num    | 1         | id==20004 |

```json
图片弹幕
{
	"id": "110xxxxxxxxxxxxx632",
	"progress": 361534,
	"mode": 1,
	"fontsize": 25,
	"color": 16777215,
	"midHash": "********",
	"content": "[ohh]",
	"ctime": "1659xxxxx",
	"weight": 10,
	"action": "picture:i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png?scale=1.00",
	"idStr": "110xxxxxxxxxxxxx632",
	"attr": 256,
	"usermid": "****",
	"animation": "{\"id\":20004,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/feed-admin/d831cbae67aee1a8fe1cc463fb23c9110ee46807.png\",\"scale\":1}"
},
NFT弹幕？
{
	"id":"113xxxxxxxxxxxxx240",
	"progress":28007,
	"midHash":"68xxxx8b",
	"content":"好耶！",
	"ctime":"1661861515",
	"attr":2048,
	"usermid":"19xxx77",
	"animation":"{\"id\":20018,\"cid\":0,\"advanced_block\":0,\"mime\":\"image\",\"resource\":\"i0.hdslb.com/bfs/baselabs/xxxxxxxx.png\"}"
},

```

## commandDms
| name      | id   | type   | desc  |
| :-------- | ---: | -----: | :---- |
| id        |  1   | int64  | 弹幕id |
| oid       |  2   | int64  | 对象视频cid |
| mid       |  3   | int64  | 发送者mid |
| command   |  4   | string | #ACTORFOLLOW#<br>#ATTENTION#<br>#GRADE#<br>#LINK#<br>#RESERVE#<br>#UP#<br>#VOTE# |
| content   |  5   | string | 互动弹幕正文 |
| progress  |  6   | int32  | 出现时间 |
| ctime     |  7   | string | 创建时间 yyyy-MM-dd HH:mm:ss |
| mtime     |  8   | string | 发布时间 yyyy-MM-dd HH:mm:ss |
| extra     |  9   | string | 扩展json数据 |
| idStr     | 10   | string | 弹幕id str类型 |
### command:类型
| command (7)   | content   |
| :------------ | --------- |
| #ACTORFOLLOW# | "合作up主" |
| #ATTENTION#   | "关注弹幕" |
| #GRADE#       | "哔瓣评分" |
| #LINK#        | **自定义内容** |
| #RESERVE#     | "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| #UP#          | **自定义内容** |
| #VOTE#        | "投票弹幕" |
### ACTORFOLLOW:合作up主
| key      | type  | value |
| :------- | ----- | ----- |
| duration | num   | |
| posX     | float | |
| posY     | float | |
| icon     | str   | http://i0.hdslb.com/bfs/album/19cc369845a2709464f3df9c38bbdea019619acd.png |
| mid      | num   | **合作up主 mid** |
| midstr   | str   | **合作up主 mid string** |
| face     | str   | **合作up主 头像 URL** |
### ATTENTION:关注弹幕
| key      | type  | value |
| :------- | ----- | ----- |
| duration | num   | |
| posX     | float | |
| posY     | float | |
| icon     | str   | http://i0.hdslb.com/bfs/album/ea58d134636f05ddc208a13889dd054ae45eb6ef.png |
| type     | num   | 2 |
| arc_type | num   | 0 |
### GRADE:哔*评分
| key              | type  | value |
| :--------------- | ----- | ----- |
| msg              | str   | "哔瓣评分" |
| skin             | num   | **1,2** |
| posX             | float | |
| posY             | float | |
| grade_id         | num   | id |
| duration         | num   | 5000? |
| icon             | str   | http://i0.hdslb.com/bfs/b/d1f96d0ad5341b214663b62e0de32dcbf776f894.png |
| mid_score        | num   | |
| count            | num   | |
| avg_score        | float | |
| skin_unselected  | str   | skin1: http://i0.hdslb.com/bfs/b/1d8fc3daf9201d70189a3778e605d2acf9cae7e9.png<br>skin2: http://i0.hdslb.com/bfs/b/a00a37f4a1f419a42f04f535147d21ac96f27a79.png |
| skin_selected    | str   | skin1: http://i0.hdslb.com/bfs/b/ee3aca3dbc22087341cf312d71a1354af527e444.png<br>skin2: http://i0.hdslb.com/bfs/b/c7d3e7d452e4ff5caf719a8e422eca10e5caad1f.png |
| skin_font_color  | str   | color(HTML)<br>skin1: "`#FFB112`"<br>skin2: "`#FA5555`" |
| summary_duration | num   | 6000 |
| shrink_icon      | str   | http://i0.hdslb.com/bfs/b/7e947f8e64c7802a16de7ebec8a8e290160ec668.png |
| shrink_title     | str   | "推荐" |
| show_status      | num   | 0 |
### LINK:链接
| key          | type  | value |
| :----------- | ----  | ----- |
| aid          | num   | **目标视频avid** |
| title        | str   | **目标视频标题** |
| icon         | str   | http://i0.hdslb.com/bfs/archive/03ef3f34944e0f78b1b4050fc3f9705d1fa905e3.png |
| bvid         | str   | **目标视频bvid** |
| posX         | float | |
| posY         | float | |
| arc_pic      | str   | **目标视频封面** |
| arc_duration | num   | **目标视频时长** |
| shrink_icon  | str   | http://i0.hdslb.com/bfs/b/44338bca6bb98a34da40698beb4ee7d19aea92a6.png |
| shrink_title | str   | "视频" |
| show_status  | num   | 0 |
| duration     | num   | |
| arc_type     | num   | 0 |
### RESERVE:预约
| key                   | type  | value | 备注 |
| :-------------------- | ----- | ----- | ---: |
| msg                   | str   | "预告：**自定义内容**"<br>"直播预约：**自定义内容**" |
| reserve_type          | num   | 1: 视频<br>2: 直播 |
| reserve_id            | num   | id |
| live_stime            | num   | UnixTimeStamp | 仅存在于`reserve_type=2` |
| arc_stime             | num   | UnixTimeStamp | 仅存在于`reserve_type=2` |
| stime                 | num   | UnixTimeStamp | 仅存在于`reserve_type=2` |
| posX                  | float | |
| posY                  | float | |
| duration              | num   | 5000 |
| icon                  | str   | http://i0.hdslb.com/bfs/b/4312fb7b155646fc6fd5f6f8a6a07a062d82587c.png |
| reserve_count         | num   | **预约人数** |
| reserve_state         | num   | 1 |
| user_state            | bool  | false? |
| live_state            | num   | video: 0<br>live: 2 ? |
| premiere_state        | num   | 0 |
| live_popularity_count | num   | 0 |
| live_popularity_str   | str   | live :"`x.y万人气`" "`xxx人看过`"  |
| premiere_online_count | num   | 0 |
| premiere_view         | num   | 0 |
| jump_url              | str   | **视频URL(直播回放URL)** |
| mid                   | num   | **目标视频 UP主mid** |
| live_stime_format     | str   | video:""<br>live: "`?(yyyy-)MM-dd HH:mm`" |
| arc_stime_format      | str   | video:""<br>live: "`?(yyyy-)MM-dd HH:mm`" |
| stime_format          | str   | video:""<br>live: "`?(yyyy-)MM-dd HH:mm`" |
| live_lottery          | bool  | |
| desc                  | str   | "" |
| shrink_icon           | str   | http://i0.hdslb.com/bfs/b/a4b1c7f03e687f680f7c3629c530e3fdd77d63ed.png |
| shrink_title          | str   | "预约" |
| show_status           | num   | 0 |
### UP:带有【UP】的~~普通~~弹幕
| key   | type | value |
| :---- | ---- | ----- |
| icon  | str  | *UP主头像URL* |
### VOTE:投票弹幕
| key          | type  | value |
| :----------- | ----- | ----- |
| vote_id      | num   | id |
| question     | str   | **投票问题** |
| cnt          | num   | **投票人数** |
| options      | array | **选项** |
| icon         | str   | http://i0.hdslb.com/bfs/album/5ec559dbd4d54f8c1e76021d52eb9807de94bfb9.png |
| my_vote      | num   | **我的选项** |
| pub_dynamic  | bool  | |
| posX         | float | |
| posY         | float | |
| duration     | num   | |
| shrink_icon  | str   | http://i0.hdslb.com/bfs/b/2eec72efb74244eed5c2f28ce5628de4e9f9c9e8.png |
| shrink_title | str   | "投票" |
| show_status  | num   | 0 |
#### VOTE::options
| key          | type  | value |
| :----------- | ----- | ----- |
| idx          | num   | start:1 |
| desc         | str   | **选项内容** |
| cnt          | num   | 0? |
| has_self_def | bool  | false? |
### posX,posY
| key      | min  | max |
| :----    | ---- | --- |
| posX     | 118  | 549 |
| posY     | 80.5 | 889 |

## 16,17,18,20,21 参考样本
~~弹幕的弹幕~~
```XML
<d p="264.42900,1,25,16777215,145XX47321,0,XXXXXXXX,1XXXXXXXX7,9">****!</d>
<d p="271.04100,1,25,16777215,162XX37965,0,XXXXXXXX,5XXXXXXXX91973376,11">****!</d>
<d/>
<d p="223.90800,1,25,16777215,154XX13409,0,XXXXXXXX,108XXXXXXXX162500,11">bgm***</d>
<d p="232.39600,1,25,16777215,162XX37915,0,XXXXXXXX,534XXXXXXXX356160,11">谢谢***</d>
<d/>
<d p="0.00000,1,45,16777215,14XX098318,1,XXXXXXXX,3XXXXXXXX3,11">text </d>
<d p="1.80800,1,25,16777215,16XX694229,0,XXXXXXXX,521XXXXXXXX935559,11">什么啊= =</d>
<d p="5.53800,1,25,16777215,16XX955781,0,XXXXXXXX,534XXXXXXXX481728,11">怎么整成这么大的弹幕？</d>
<d p="4.63800,1,25,16777215,16XX204771,0,XXXXXXXX,535XXXXXXXX911360,11">？？？</d>
<d p="4.79800,1,25,16777215,16XX443490,0,XXXXXXXX,536XXXXXXXX569984,11">？</d>
<d p="3.41800,1,25,16777215,16XX684458,0,XXXXXXXX,537XXXXXXXX886272,11">这是高级弹幕</d>
<d p="4.98400,1,25,16777215,16XX237458,0,XXXXXXXX,540XXXXXXXX711104,11">？怎么这么大？</d>
<d p="5.39800,1,25,16777215,16XX998765,0,XXXXXXXX,581XXXXXXXX414080,11">好大</d>
```
```JSON
[
{"id":"1XXXXXXXX7","ctime":"145XX47321","idStr":"1XXXXXXXX7","replyCount":1},
{"id":"5XXXXXXXX91973376","ctime":"162XX37965","idStr":"5XXXXXXXX91973376","test16":"1XXXXXXXX7","test17":"1XXXXXXXX7"},
{"id":"5XXXXXXXX91973376","ctime":"1629037965","idStr":"5XXXXXXXX91973376","test16":"1XXXXXXXX7","test17":"1XXXXXXXX7","test20":"1XXXXXXXX7","test21":"1XXXXXXXX7"},

{"id":"108XXXXXXXX162500","ctime":"154XX13409","idStr":"108XXXXXXXX162500","likes":1,"replyCount":1},
{"id":"534XXXXXXXX356160","ctime":"162XX37915","idStr":"534XXXXXXXX356160","test16":"108XXXXXXXX162500","test17":"108XXXXXXXX162500"},
{"id":"534XXXXXXXX356160","ctime":"162XX37915","idStr":"534XXXXXXXX356160","test16":"108XXXXXXXX162500","test17":"108XXXXXXXX162500","test20":"108XXXXXXXX162500","test21":"108XXXXXXXX162500"},

{"id":"3XXXXXXXX3","ctime":"14XX098318","idStr":"3XXXXXXXX3","attr":4,"likes":2359,"replyCount":7},
{"id":"521XXXXXXXX935559","ctime":"16XX694229","idStr":"521XXXXXXXX935559","likes":2,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"534XXXXXXXX481728","ctime":"16XX955781","idStr":"534XXXXXXXX481728","likes":2,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"535XXXXXXXX911360","ctime":"16XX204771","idStr":"535XXXXXXXX911360","likes":1,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"536XXXXXXXX569984","ctime":"16XX443490","idStr":"536XXXXXXXX569984","likes":1,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"537XXXXXXXX886272","ctime":"16XX684458","idStr":"537XXXXXXXX886272","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"540XXXXXXXX711104","ctime":"16XX237458","idStr":"540XXXXXXXX711104","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"581XXXXXXXX414080","ctime":"16XX998765","idStr":"581XXXXXXXX414080","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
]
```
