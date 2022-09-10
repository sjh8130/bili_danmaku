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
	e=tarfile.TarInfo(f"[{t}]_[{c[0]}]_[{c[1]}]_[{c[2]}].{c[3]}")
	e.size=len(d.content)
	e.mtime=time.time().__trunc__()
	a.addfile(tarinfo=e,fileobj=io.BytesIO(d.content))
	return d.content

def q(a,b,c=""): return p(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={a}&segment_index={b}',c=[a,"Danmaku",b+c,"bin"])

def r():
	global a
	with tarfile.open(name=t+".tar.gz",mode="w:gz",bufsize=4194304)as a:
		b=json.loads(p(b=f"https://api.bilibili.com/x/web-interface/view?bvid={t}",c=["0","Video","INFO","json"]))["data"]
		p(b=f"https://api.bilibili.com/x/web-interface/view/detail?bvid={t}",c=["0","Video","INFO_Detail","json"])
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
			print(f"{d}|{t}|av00000000|PXX/{len(b['pages'])}|{g}|{h}|{i}|{c}|{k}")
			for l in range(i):
				try:q(g,str(l+1))
				except json.decoder.JSONDecodeError:pass
				try:q(g,str(l+1),"_B1")
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
			o=tarfile.TarInfo(f"{t}_{g}.json")
			o.size=len(n)
			o.mtime=time.time().__trunc__()
			a.addfile(tarinfo=o,fileobj=io.BytesIO(bytes(n,encoding="utf-8")))
		a.close()

def s():
	try:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":0,\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		# a=requests.get("https://api.bilibili.com/x/series/archives?mid=xxxx&series_id=yyyy&only_normal=true&sort=desc&pn=1&ps=10",headers).content
	except:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":"+str(u)+",\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		print("ERR",time.time().__trunc__())
	if json.loads(a)["code"]!=0: print(f"[NET]:Error {time.time().__trunc__}")
	return a

if __name__=='__main__':
	try:
		t=sys.argv[1]
		r()
		print("With args")
		sys.exit()
	except IndexError:pass
	u=v=w=0
	while True:
		v=json.loads(s())["data"]["archives"][0]
		if u!=v["aid"]:
			print(f"{v['pubdate']}|{v['bvid']}")
			u=v["aid"]
			if w==0:w=1
			elif v==0:w=0
			else:
				print(f"{int(time.time().__trunc__())}:{v['bvid']}")
				t=v['bvid']
				r()
		time.sleep(15)
