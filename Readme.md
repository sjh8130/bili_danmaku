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
输出文件：`****.xml`  
`for /r . %a in (*.json) do convert_to_xml.py "%a"`  

## Json:
```JS
{"elems": [
    {
        "id": "1234567890123456789",        // 弹幕ID
        "progress": 1,                      // 弹幕出现时间
        "mode": 1,                          // 弹幕类型
        "fontsize": 25,                     // 弹幕字号
        "color": 16777215,                  // 弹幕颜色
        "midHash": "XXXXXXXX",              // 发送者mid hash (CRC32 mid)
        "content": "*****",                 // 弹幕内容
        "ctime": "123456789",               // 发送时间
        "weight": 11,                       // 屏蔽等级 [1,11]
        "action": ""                        // .
        "pool": 1                           // 弹幕池
        "idStr": "1234567890123456789",     // 弹幕ID
        "attr": 1,                          // 弹幕属性位
        "usermid": "1234567890",            // 发送者mid
        "zanCount": "0",                    // 点赞数量
        "test16": "",                       // int test16 === test17
        "test17": "",                       // int test16 === test17
        "test18": "",                       // .
        "test19": "",                       // .
        "test20": "",                       // string test20 === test21
        "test21": "",                       // string test20 === test21
        "animation": "",                    // .
        "test23": ""                        // .
    }
    // ......
    ]
}
```

## 参考来源：  

[bilibili-API-collect]( https://github.com/SocialSisterYi/bilibili-API-collect )
1.	protobuf解码 [bilibili-API-collect::danmaku_proto.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_proto.md )
2.	XML格式 [bilibili-API-collect::danmaku_xml.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_xml.md )