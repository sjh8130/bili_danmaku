#!/usr/bin/python3
import os
import requests
import json
import time
import sys
import tarfile
import io

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"
x={'User-Agent':USER_AGENT,'origin':"https://www.bilibili.com",'referer':"https://www.bilibili.com","Connection":"keep-alive"}

def v(b,x=x,d=0):
	print(f"[NET] {b}")
	if d==9:return b""
	try:c=requests.get(b.replace("http://","https://"),headers=x,timeout=10).content
	except:c=v(b,d=d+1)
	return c
def o(b,c,x=x):
	d=v(b,x)
	e=tarfile.TarInfo(c)
	e.size=len(d)
	e.mtime=time.time().__trunc__()
	a.addfile(tarinfo=e,fileobj=io.BytesIO(d))
	return d

def p():
	global a
	with tarfile.open(name=r+".tar",mode="w",bufsize=4194304)as a:
		y={'Host':"api.bilibili.com","Connection":"keep-alive",'Accept':"application/json, text/plain, */*",'User-Agent':USER_AGENT,'origin':"https://www.bilibili.com",'referer':f"https://www.bilibili.com/video/{r}/",'Accept-Encoding':"gzip, deflate, br",}
		b=json.loads(o(b=f"https://api.bilibili.com/x/web-interface/view?bvid={r}",c=f"[{r}]_[0]_[Video]_[INFO].json"))["data"]
		o(b=f"https://api.bilibili.com/x/web-interface/view/detail?bvid={r}",c=f"[{r}]_[0]_[Video]_[INFO_Detail].json")
		for d in b["subtitle"]["list"]:o(b=d["subtitle_url"],c=f"[{r}]_[0]_[Subs]_[{d['id']}_{d['lan']}].bcc")
		for e in b["pages"]:
			f=str(e["cid"])
			g=int(e["duration"])
			h=(g/360).__ceil__()
			o(b=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={f}',c=f"[{r}]_[{f}]_[BAS]_[INFO].bin",x=y)
			print(f"{b['pubdate']}|{r}|av00000000|PXX/{len(b['pages'])}|{f}|{g}|{h}|title|ptitle")
			for i in range(h):
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={f}&segment_index={str(i+1)}',c=f"[{r}]_[{f}]_[Danmaku]_[{i+1}].bin",x=y)
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={f}&segment_index={str(i+1)}',c=f"[{r}]_[{f}]_[Danmaku]_[{i+1}]_B1.bin",x=y)
			j={}
			j["elems"]=["Embedded"]
			j["commandDms"]=[]
			j["info"]={}
			j["info"]["Ver"]="V6_20230601_Embedded"
			j["info"]["owner"]=b['owner']
			j["info"]["bvid"]=b['bvid']
			j["info"]["avid"]=b['aid']
			j["info"]["V_Name"]=b["title"]
			j["info"]["pubdate"]=b["pubdate"]
			j["info"]["ctime"]=b['ctime']
			j["info"]["P_Name"]=e["part"]
			j["info"]["duration"]=g
			j["info"]["cid"]=f
			j["info"]["segment_count"]=h
			j["info"]["danmaku_count"]=0
			j["info"]["danmaku_web_reported"]=b['stat']['danmaku']
			j["info"]["danmaku_proto_reported"]=0
			j["info"]["File_Create_Time"]=time.time().__trunc__()
			j["info"]["File_Create_Time_Start"]=0
			j["info"]["is_live_record"]=False
			k=bytes(json.dumps(j,ensure_ascii=False,separators=(',',':')),encoding="utf-8")
			l=tarfile.TarInfo(f"{r}_{f}.json")
			l.size=len(k)
			l.mtime=time.time().__trunc__()
			a.addfile(tarinfo=l,fileobj=io.BytesIO(k))
		a.close()

def q():
	try:
		a=requests.get("https://api.bilibili.com/x/series/archives?mid=508963009&series_id=91398&only_normal=true&sort=desc&pn=1&ps=10",x,timeout=20).content
	except:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":"+str(s)+",\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		print("ERR",time.time().__trunc__())
	if json.loads(a)["code"]!=0:print(f"[NET]:Error {time.time().__trunc__}")
	return a

if __name__=='__main__':
	try:
		r=sys.argv[1]
		print("With args")
		p()
		sys.exit()
	except IndexError:pass
	s=t=u=0
	while True:
		t=json.loads(q())["data"]["archives"][0]
		if s!=t["aid"]:
			print(f"{t['pubdate']}|{t['bvid']}")
			s=t["aid"]
			if u==0:u=1
			elif t==0:u=0
			else:
				print(f"{int(time.time().__trunc__())}:{t['bvid']}")
				r=t['bvid']
				p()
				os.system("/root/aliyunpan/aliyunpan upload /root/work /")
		time.sleep(15)
