#!/usr/bin/python3
import socket
import requests
import json
import math
import time
import sys
import tarfile
import io
import urllib3
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",'origin':"https://www.bilibili.com",'referer':"https://www.bilibili.com"}
def s(b,c):
	time.sleep(0.03)
	d=requests.get(b,headers=headers)
	print(f"[NET]:HTTP {d.status_code}\t{b}")
	e=tarfile.TarInfo(f"[{w}]_[{c[0]}]_[{c[1]}]_[{c[2]}].{c[3]}")
	e.size=len(d.content)
	e.mtime=time.time().__trunc__()
	a.addfile(tarinfo=e,fileobj=io.BytesIO(d.content))
	return d.content

def t(a,b,c=""):
	return s(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={a}&segment_index={b}',c=[a,"Danmaku",b+c,"bin"])

def u():
	global a
	with tarfile.open(name=f"{w}.tar.xz",mode="w:xz",bufsize=4194304)as a:
		b=f"https://api.bilibili.com/x/web-interface/view?bvid={w}"
		c=f"https://api.bilibili.com/x/web-interface/view/detail?bvid={w}"
		d=s(b=b,c=["0","Video","INFO","json"])
		s(b=c,c=["0","Video","INFO_Detail","json"])
		e=json.loads(d)["data"]
		f=e["title"]
		g=e["pubdate"]
		for h in e["subtitle"]["list"]:s(b=h["subtitle_url"],c=["0","Subs",f"{h['id']}_{h['lan']}","bcc"])
		for i in e["pages"]:
			j=str(i["cid"])
			k=int(i["duration"])
			l=math.ceil(k/360)
			m=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={j}'
			s(b=m,c=[j,"BAS","INFO","bin"])
			n=str(i["part"])
			print(f"{g}|{w}|av00000000|PXX/{len(e['pages'])}|{j}|{k}|{l}|{f}|{n}")
			for o in range(l):
				try:t(j,str(o+1))
				except json.decoder.JSONDecodeError:pass
				try:t(j,str(o+1),"_B1")
				except json.decoder.JSONDecodeError:pass
			p={}
			p["elems"]=["Embedded"]
			p["commandDms"]=[]
			p["info"]={}
			p["info"]["owner"]=e['owner']
			p["info"]["bvid"]=e['bvid']
			p["info"]["avid"]=e['aid']
			p["info"]["V_Name"]=f
			p["info"]["pubdate"]=int(g)
			p["info"]["i_ctime"]=e['ctime']
			p["info"]["P_Name"]=n
			p["info"]["duration"]=k
			p["info"]["cid"]=j
			p["info"]["segment_count"]=l
			p["info"]["danmaku_count"]=0
			p["info"]["danmaku_web_reported"]=e['stat']['danmaku']
			p["info"]["danmaku_proto_reported"]=0
			p["info"]["File_Create_Time"]=time.time().__trunc__()
			p["info"]["is_live_record"]=False
			p["File_Ver"]="V3_20220819_Embedded"
			q=json.dumps(p,ensure_ascii=False,separators=(',',':'))
			r=tarfile.TarInfo(f"{w}_{j}.json")
			r.size=len(q)
			r.mtime=time.time().__trunc__()
			a.addfile(tarinfo=r,fileobj=io.BytesIO(bytes(q,encoding="utf-8")))
		a.close()
		
def v():
	try:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":0,\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		# a=requests.get("https://api.bilibili.com/x/series/archives?mid=xxxx&series_id=yyyy&only_normal=true&sort=desc&pn=1&ps=10",headers).content
	except:
		a="{\"code\":0,\"data\":{\"archives\":[{\"aid\":"+str(y)+",\"pubdate\":1,\"bvid\":\"BV0000000000\"}]}}"
		print("ERR",time.time().__trunc__())
	if json.loads(a)["code"]!=0: print(f"[NET]:Error {int(time.time())}")
	return a

if __name__=='__main__':
	try:
		w=sys.argv[1]
		u()
		print("With args")
		sys.exit()
	except IndexError:pass
	y=z=a1=0
	while True:
		z=json.loads(v())["data"]["archives"][0]
		if y!=z["aid"]:
			print(f"{z['pubdate']}|{z['bvid']}")
			y=z["aid"]
			if a1==0:a1=1
			elif z==0:a1=0
			else:
				print(f"{int(time.time().__trunc__())}:{z['bvid']}")
				w=z['bvid']
				u()
		time.sleep(10)
