#!/usr/bin/python3
import os
import requests
import json
import math
import time
import sys
import tarfile
import io

x={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",'origin':"https://www.bilibili.com",'referer':"https://www.bilibili.com"}
def v(b):
	try:c=requests.get(b,headers=x)
	except:v(b)
	return c
def o(b,c):
	d=v(b)
	print(f"[NET]:HTTP {d.status_code}\t{b}")
	e=tarfile.TarInfo(f"[{r}]_[{c[0]}]_[{c[1]}]_[{c[2]}].{c[3]}")
	e.size=len(d.content)
	e.mtime=time.time().__trunc__()
	a.addfile(tarinfo=e,fileobj=io.BytesIO(d.content))
	return d.content

def p():
	global a
	with tarfile.open(name=r+".tar",mode="w",bufsize=4194304)as a:
		b=json.loads(o(b=f"https://api.bilibili.com/x/web-interface/view?bvid={r}",c=["0","Video","INFO","json"]))["data"]
		o(b=f"https://api.bilibili.com/x/web-interface/view/detail?bvid={r}",c=["0","Video","INFO_Detail","json"])
		c=b["pubdate"]
		for d in b["subtitle"]["list"]:o(b=d["subtitle_url"].replace("http://", "https://"),c=["0","Subs",f"{d['id']}_{d['lan']}","bcc"])
		for e in b["pages"]:
			f=str(e["cid"])
			g=int(e["duration"])
			h=math.ceil(g/360)
			o(b=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={f}',c=[f,"BAS","INFO","bin"])
			print(f"{c}|{r}|av00000000|PXX/{len(b['pages'])}|{f}|{g}|{h}|title|ptitle")
			for i in range(h):
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={f}&segment_index={str(i+1)}',c=[f,"Danmaku",str(i+1),"bin"])
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={f}&segment_index={str(i+1)}',c=[f,"Danmaku",str(i+1)+"_B1","bin"])
			j={}
			j["elems"]=["Embedded"]
			j["commandDms"]=[]
			j["info"]={}
			j["info"]["Ver"]="V4_20220911_Embedded"
			j["info"]["owner"]=b['owner']
			j["info"]["bvid"]=b['bvid']
			j["info"]["avid"]=b['aid']
			j["info"]["V_Name"]=b["title"]
			j["info"]["pubdate"]=int(c)
			j["info"]["i_ctime"]=b['ctime']
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
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":0,\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		# a=requests.get("https://api.bilibili.com/x/series/archives?mid=xxxx&series_id=yyyy&only_normal=true&sort=desc&pn=1&ps=10",headers).content
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
		time.sleep(15)
