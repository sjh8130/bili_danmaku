#!/usr/bin/python3
import requests
import json
import math
import time
import sys
import tarfile
import io

x={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",'origin':"https://www.bilibili.com",'referer':"https://www.bilibili.com"}
def p(b,c):
	d=requests.get(b,headers=x)
	print(f"[NET]:HTTP {d.status_code}\t{b}")
	e=tarfile.TarInfo(f"[{s}]_[{c[0]}]_[{c[1]}]_[{c[2]}].{c[3]}")
	e.size=len(d.content)
	e.mtime=time.time().__trunc__()
	a.addfile(tarinfo=e,fileobj=io.BytesIO(d.content))
	return d.content

def q():
	global a
	with tarfile.open(name=s+".tar.gz",mode="w:gz",bufsize=4194304)as a:
		b=json.loads(p(b=f"https://api.bilibili.com/x/web-interface/view?bvid={s}",c=["0","Video","INFO","json"]))["data"]
		p(b=f"https://api.bilibili.com/x/web-interface/view/detail?bvid={s}",c=["0","Video","INFO_Detail","json"])
		c=b["title"]
		d=b["pubdate"]
		for e in b["subtitle"]["list"]:p(b=e["subtitle_url"],c=["0","Subs",f"{e['id']}_{e['lan']}","bcc"])
		for f in b["pages"]:
			g=str(f["cid"])
			h=int(f["duration"])
			i=math.ceil(h/360)
			j=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={g}'
			p(b=j,c=[g,"BAS","INFO","bin"])
			k=str(f["part"])
			print(f"{d}|{s}|av00000000|PXX/{len(b['pages'])}|{g}|{h}|{i}|{c}|{k}")
			for l in range(i):
				try:p(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={g}&segment_index={str(l+1)}',c=[g,"Danmaku",str(l+1),"bin"])
				except json.decoder.JSONDecodeError:pass
				try:p(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={g}&segment_index={str(l+1)}',c=[g,"Danmaku",str(l+1)+"_B1","bin"])
				except json.decoder.JSONDecodeError:pass
			m={}
			m["elems"]=["Embedded"]
			m["commandDms"]=[]
			m["info"]={}
			m["info"]["owner"]=b['owner']
			m["info"]["bvid"]=b['bvid']
			m["info"]["avid"]=b['aid']
			m["info"]["V_Name"]=c
			m["info"]["pubdate"]=int(d)
			m["info"]["i_ctime"]=b['ctime']
			m["info"]["P_Name"]=k
			m["info"]["duration"]=h
			m["info"]["cid"]=g
			m["info"]["segment_count"]=i
			m["info"]["danmaku_count"]=0
			m["info"]["danmaku_web_reported"]=b['stat']['danmaku']
			m["info"]["danmaku_proto_reported"]=0
			m["info"]["File_Create_Time"]=time.time().__trunc__()
			m["info"]["is_live_record"]=False
			m["File_Ver"]="V3_20220819_Embedded"
			n=json.dumps(m,ensure_ascii=False,separators=(',',':'))
			o=tarfile.TarInfo(f"{s}_{g}.json")
			o.size=len(n)
			o.mtime=time.time().__trunc__()
			a.addfile(tarinfo=o,fileobj=io.BytesIO(bytes(n,encoding="utf-8")))
		a.close()

def r():
	try:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":0,\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		# a=requests.get("https://api.bilibili.com/x/series/archives?mid=xxxx&series_id=yyyy&only_normal=true&sort=desc&pn=1&ps=10",headers).content
	except:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":"+str(t)+",\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		print("ERR",time.time().__trunc__())
	if json.loads(a)["code"]!=0: print(f"[NET]:Error {time.time().__trunc__}")
	return a

if __name__=='__main__':
	try:
		s=sys.argv[1]
		q()
		print("With args")
		sys.exit()
	except IndexError:pass
	t=u=v=0
	while True:
		u=json.loads(r())["data"]["archives"][0]
		if t!=u["aid"]:
			print(f"{u['pubdate']}|{u['bvid']}")
			t=u["aid"]
			if v==0:v=1
			elif u==0:v=0
			else:
				print(f"{int(time.time().__trunc__())}:{u['bvid']}")
				s=u['bvid']
				q()
		time.sleep(15)
