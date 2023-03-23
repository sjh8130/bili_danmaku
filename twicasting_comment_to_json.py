import sys
import time
import bs4
import lxml
import json
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

if "#" in sys.argv[1]:
	user = sys.argv[1].split("#")[0]
	movie_id = sys.argv[1].split("#")[1]
else:
	user = sys.argv[1]
	movie_id = sys.argv[2]
try:
	pages = int(sys.argv[3])
except:
	pages = 2

TWITCASTING_URL_JP = "ja.twitcasting.tv"
TWITCASTING_URL_EN = "en.twitcasting.tv"
TWITCASTING_URL_GL = "twitcasting.tv"
TWITCASTING_URL = TWITCASTING_URL_EN
headers = {
	'Host': TWITCASTING_URL,
	'Connection': 'keep-alive',
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"
}


def downloader(page, retry_times=0):
	url = f"https://{TWITCASTING_URL}/{user}/moviecomment/{movie_id}-{page}"
	print(url, retry_times)
	try:
		content = requests.get(url=url, headers=headers, verify=False, timeout=30).content
	except KeyboardInterrupt:
		print("BREAK")
		return "BREAK"
	except:
		content = downloader(page, retry_times+1)
	return content


out = {"comment": [], "info": {"user": user, "movie_id": int(movie_id), "title": ""}}
page = 0
while (page <= int(pages)):
	# a = open(f"twicasting_{user}_{movie_id}_{page}.html", encoding="utf-8").read()
	a = downloader(page)
	if a == "BREAK":
		break
	b = list(bs4.BeautifulSoup(a, "lxml").select(".tw-comment-history-item", limit=999))
	# out["info"]["title"] = str(bs4.BeautifulSoup(a, "lxml").title.contents[0]).replace(" Comment - TwitCasting", "").replace(" コメント - ツイキャス", "")
	if page == 0:
		out["info"]["title"] = str(bs4.BeautifulSoup(a, "lxml").select(".tw-basic-page-header-path", limit=1)[0].contents[3].contents[1].contents[0]).rstrip(" ")
		pages = int(bs4.BeautifulSoup(a, "lxml").select(".tw-pager", limit=1)[0].contents[-1].contents[0])
	for i in b:
		out["comment"].append({
			"id": int(i.attrs['data-comment-id']),
			"time": int(time.mktime(time.strptime(i.select(".tw-comment-history-item__info__date")[0].attrs['datetime'], '%a, %d %b %Y %H:%M:%S %z'))),
			"content": str(i.select(".tw-comment-history-item__content__text")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
			"user_id": i.select(".tw-comment-history-item__details__user-link")[0].attrs['href'][1:],
			"username": str(i.select(".tw-comment-history-item__details__user-link")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
			"user_img": ("https:"+i.select(".tw-comment-history-item__user__icon")[0].attrs['src']).replace("https:https://", "https://")
		})
	page += 1

open(f"twicasting_{user}_{movie_id}.json", "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":"), indent="\t"))
