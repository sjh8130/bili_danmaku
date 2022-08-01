# bili_danmu

## download.py 下载弹幕
使用方法:  
`download.py "av号|bv号|av号网址|bv号网址"`  
输出文件:  
`[发布时间][BVid][avid][选集][cid]主标题.json.gz`  
`[发布时间][BVid][avid][选集][cid]主标题_分P标题.json.gz`

## json_to_xml.py 转换为XML
使用方法:  
`json_to_xml.py ****.json`  
`json_to_xml.py ****.json.gz`  
`proto_to_xml.py ****.bin`  
输出文件：  
`****.xml`  

`for /r . %a in (*.json) do convert_to_xml.py "%a"`  

## 参考来源：  

[bilibili-API-collect]( https://github.com/SocialSisterYi/bilibili-API-collect )
-	protobuf解码 [bilibili-API-collect::danmaku_proto.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_proto.md )
-	XML格式 [bilibili-API-collect::danmaku_xml.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_xml.md )
