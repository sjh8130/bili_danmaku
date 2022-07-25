# bili_danmu

## download.py 下载弹幕
使用方法:  
`download.py "av号|bv号|av号网址|bv号网址" [开关]`  
输出文件:  
`[发布时间][BVid][avid][选集][cid]主标题.json.gz`  
`[发布时间][BVid][avid][选集][cid]主标题_分P标题.json.gz`  

`876543210 开关`  
`________1` 计时器  
`_______1_` 错误停机  
`______1__` 无弹幕停机  
`_____1___` 日志  
`____1____` 输出 其他信息到 XML 文件  
`___1_____` 不输出 Json  
`__1______` 不输出 XML  
`_1_______` 输出 Protobuf 二进制文件  
`1________` 模拟运行  

## convert_to_xml.py 转换为XML
使用方法:  
`convert_to_xml.py ****.json"`  
`convert_to_xml.py ****.json.gz"`  
输出文件：  
`****.xml`  

`for /r . %a in (*.json) do convert_to_xml.py "%a"`  

## Json:
```JS
{"elems": [
    {
        "id": "1234567890123456789",        // 01:  int64 弹幕ID
        "progress": 1,                      // 02:  int32 弹幕出现时间  空:0 
        "mode": 1,                          // 03:  int32 弹幕类型
        "fontsize": 25,                     // 04:  int32 弹幕字号
        "color": 16777215,                  // 05: uint32 弹幕颜色      空:0 [1,16777215]
        "midHash": "XXXXXXXX",              // 06: string 发送者mid hash (CRC32 mid)
        "content": "*****",                 // 07: string 弹幕内容
        "ctime": "123456789",               // 08:  int64 发送时间
        "weight": 11,                       // 09:  int32 屏蔽等级 [1,11]
        "action": ""                        // 10: string 已知:["airborne:毫秒"]
        "pool": 1                           // 11:  int32 弹幕池
        "idStr": "1234567890123456789",     // 12: string 弹幕ID
        "attr": 1,                          // 13:  int32 弹幕属性位
        "usermid": "1234567890",            // 14: ?int?? 发送者mid
        "zanCount": "0",                    // 15: ?int?? 点赞数量
        "test16": "",                       // 16:  int64 test16 === test17  !! 指向另一个弹幕 id
        "test17": "",                       // 17:  int64 test16 === test17  !! 指向另一个弹幕 id
        "test18": "",                       // 18: string                    !! 被指向次数
        "test19": "",                       // 19: ?????? -
        "test20": "",                       // 20: string test20 === test21  !! 指向另一个弹幕 idStr
        "test21": "",                       // 21: string test20 === test21  !! 指向另一个弹幕 idStr
        "animation": "",                    // 22: string -
        "test23": ""                        // 23: ?????? -
    }
    // ......
    ]
}
```

## 16,17,18,20,21 参考样本 
~~弹幕的弹幕~~
```XML
<d p="264.42900,1,25,16777215,145XX47321,0,XXXXXXXX,1XXXXXXXX7,9">****!</d>
<d p="271.04100,1,25,16777215,162XX37965,0,XXXXXXXX,5XXXXXXXX91973376,11">****!</d>
<d/>
<d p="223.90800,1,25,16777215,154XX13409,0,XXXXXXXX,108XXXXXXXX162500,11">bgm***</d>
<d p="232.39600,1,25,16777215,162XX37915,0,XXXXXXXX,534XXXXXXXX356160,11">谢谢***</d>
<d/>
<d p="0.00000,1,45,16777215,14XX098318,1,XXXXXXXX,3XXXXXXXX3,11">text </d><!-- 高赞 -->
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
{"id":"1XXXXXXXX7","ctime":"145XX47321","idStr":"1XXXXXXXX7","test18":"1"},
{"id":"5XXXXXXXX91973376","ctime":"162XX37965","idStr":"5XXXXXXXX91973376","test16":"1XXXXXXXX7","test17":"1XXXXXXXX7"},
{"id":"5XXXXXXXX91973376","ctime":"1629037965","idStr":"5XXXXXXXX91973376","test16":"1XXXXXXXX7","test17":"1XXXXXXXX7","test20":"1XXXXXXXX7","test21":"1XXXXXXXX7"},
{},
{"id":"108XXXXXXXX162500","ctime":"154XX13409","idStr":"108XXXXXXXX162500","zanCount":1,"test18":"1"},
{"id":"534XXXXXXXX356160","ctime":"162XX37915","idStr":"534XXXXXXXX356160","test16":"108XXXXXXXX162500","test17":"108XXXXXXXX162500"},
{"id":"534XXXXXXXX356160","ctime":"162XX37915","idStr":"534XXXXXXXX356160","test16":"108XXXXXXXX162500","test17":"108XXXXXXXX162500","test20":"108XXXXXXXX162500","test21":"108XXXXXXXX162500"},
{},
{"id":"3XXXXXXXX3","ctime":"14XX098318","idStr":"3XXXXXXXX3","attr":4,"zanCount":2359,"test18":"7"},
{"id":"521XXXXXXXX935559","ctime":"16XX694229","idStr":"521XXXXXXXX935559","zanCount":2,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"534XXXXXXXX481728","ctime":"16XX955781","idStr":"534XXXXXXXX481728","zanCount":2,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"535XXXXXXXX911360","ctime":"16XX204771","idStr":"535XXXXXXXX911360","zanCount":1,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"536XXXXXXXX569984","ctime":"16XX443490","idStr":"536XXXXXXXX569984","zanCount":1,"test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"537XXXXXXXX886272","ctime":"16XX684458","idStr":"537XXXXXXXX886272","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"540XXXXXXXX711104","ctime":"16XX237458","idStr":"540XXXXXXXX711104","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{"id":"581XXXXXXXX414080","ctime":"16XX998765","idStr":"581XXXXXXXX414080","test16":"3XXXXXXXX3","test17":"3XXXXXXXX3"},
{}]
```
```
https://app.bilibili.com/
2017-12-14  Android5.20.0   弹幕点赞功能上线，为精彩弹幕点赞
2018-01-30  iPhone5.22.1

2018-09-21  Android5.32.0   轻点弹幕即可点赞、举报！你看这个弹幕，真的很漂亮哦！（警告）
2018-09-18  iPhone5.32.0
2018-10-26  iPad2.0

2021-04-08  Android6.22.0   高赞弹幕支持海报分享，一键分享我的高光时刻
2021-04-08  iPhone6.22.0
```
## 参考来源：  

[bilibili-API-collect]( https://github.com/SocialSisterYi/bilibili-API-collect )
1.	protobuf解码 [bilibili-API-collect::danmaku_proto.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_proto.md )
2.	XML格式 [bilibili-API-collect::danmaku_xml.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_xml.md )