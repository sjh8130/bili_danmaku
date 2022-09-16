#!/usr/bin/python3
import requests
import json
import math
import time
import sys
import tarfile
import io

x={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",'origin':"https://www.bilibili.com",'referer':"https://www.bilibili.com"}
def o(b,c):
	d=requests.get(b,headers=x)
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
		for c in b["subtitle"]["list"]:o(b=c["subtitle_url"],c=["0","Subs",f"{c['id']}_{c['lan']}","bcc"])
		for d in b["pages"]:
			e=str(d["cid"])
			f=int(d["duration"])
			g=math.ceil(f/360)
			o(b=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={e}',c=[e,"BAS","INFO","bin"])
			print(f"1000000000|{r}|av00000000|PX/{len(b['pages'])}|{e}|{f}|{g}|title|ptitle")
			for h in range(g):
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={e}&segment_index={str(h+1)}',c=[e,"Danmaku",str(h+1),"bin"])
				o(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={e}&segment_index={str(h+1)}',c=[e,"Danmaku",str(h+1)+"_B1","bin"])
			i={}
			i["elems"]=["Embedded"]
			i["commandDms"]=[]
			i["info"]={}
			i["info"]["Ver"]="V5_20220916"
			i["info"]["owner"]=b['owner']
			i["info"]["bvid"]=b['bvid']
			i["info"]["avid"]=b['aid']
			i["info"]["V_Name"]=b["title"]
			i["info"]["pubdate"]=int(b["pubdate"])
			i["info"]["i_ctime"]=b['ctime']
			i["info"]["P_Name"]=d["part"]
			i["info"]["cid"]=e
			i["info"]["duration"]=f
			i["info"]["segment_count"]=g
			i["info"]["danmaku_count"]=0
			i["info"]["danmaku_web_reported"]=b['stat']['danmaku']
			i["info"]["danmaku_proto_reported"]=0
			i["info"]["File_Create_Time"]=time.time().__trunc__()
			i["info"]["File_Create_Time_Start"]=0
			i["info"]["is_live_record"]=False
			i["Ver_Var"]="Embedded"
			j=bytes(json.dumps(i,ensure_ascii=False,separators=(',',':')),encoding="utf-8")
			k=tarfile.TarInfo(f"{r}_{e}.json")
			k.size=len(j)
			k.mtime=time.time().__trunc__()
			a.addfile(tarinfo=k,fileobj=io.BytesIO(j))
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
		p()
		print("With args")
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
