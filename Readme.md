# bili_danmu

## main.py 下载弹幕
使用方法:  
`main.py "av号"`  
`main.py "bv号"`  
`main.py "av号网址"`  
`main.py "bv号网址"`  

输出文件: `BV号_av号_分P_cid_主标题_[分隔符]_分P标题.json`  
输出内容:
```json
{"elems": [{"id": "123123","mode": 1,"fontsize": 25,"color": 16777215,"midHash": "ffffffff","content": "弹幕内容","ctime": "1640966400","weight": 2,"pool": 1,"idStr": "123123","attr": 2},{"id": "4566456","progress": 1000,"mode": 1,"fontsize": 25,"midHash": "ffffffff","content": "弹幕内容","ctime": "1609430400","weight": 1,"idStr": "4566456","attr": 2}......]}
===================
{
	"elems": [
		{
			"id": "123123",
			"mode": 1,
			"fontsize": 25,
			"color": 16777215,
			"midHash": "ffffffff",
			"content": "弹幕内容",
			"ctime": "1640966400",
			"weight": 2,
			"pool": 1,
			"idStr": "123123",
			"attr": 2
		},
		{
			"id": "4566456",
			"progress": 1000,
			"mode": 1,
			"fontsize": 25,
			"midHash": "ffffffff",
			"content": "弹幕内容",
			"ctime": "1609430400",
			"weight": 1,
			"idStr": "4566456",
			"attr": 2
		}
		......
	]
}
```

## convert_to_xml.py 转换为主站格式XML
使用方法:  
`convert_to_xml.py "BV**_av**_P**_cid_***.json"`  
输出文件：`****.xml`  
输出内容：
```XML
<?xml version="1.0" encoding="UTF-8"?>
<i>
	<chatserver>chat.bilibili.com</chatserver>
	<chatid>****cid****</chatid>
	<mission>0</mission>
	<maxlimit>8000</maxlimit>
	<state>0</state>
	<real_name>0</real_name>
	<source>k-v</source>
	<d p="0.00000,1,25,16777215,1640966400,1,ffffffff,123123,1">弹幕内容</d>
	<d p="1.00000,1,25,0,1609430400,0,ffffffff,4566456,0">弹幕内容</d>
	......
</i>
```

参考来源：  

[bilibili-API-collect]( https://github.com/SocialSisterYi/bilibili-API-collect )
1.	protobuf解码[bilibili-API-collect::danmaku_proto]( https://github.com/SocialSisterYi/bilibili-API-collect/danmaku/danmaku_proto.md )
2.	XML格式[bilibili-API-collect::danmaku_xml.md]( https://github.com/SocialSisterYi/bilibili-API-collect/danmaku/danmaku_xml.md )