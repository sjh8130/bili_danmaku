# bili_danmu

## main.py 下载弹幕
使用方法:  
`main.py "av号"`  
`main.py "bv号"`  
`main.py "av号网址"`  
`main.py "bv号网址"`  

输出文件: `BV号_av号_分P_cid_主标题_[分隔符]_分P标题.json`  

## convert_to_xml.py 转换为主站格式XML
使用方法:  
`convert_to_xml.py "BV**_av**_P**_cid_***.json"`  
输出文件：`****.xml`  

参考来源：  

[bilibili-API-collect]( https://github.com/SocialSisterYi/bilibili-API-collect )
1.	protobuf解码[bilibili-API-collect::danmaku_proto]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_proto.md )
2.	XML格式[bilibili-API-collect::danmaku_xml.md]( https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku_xml.md )