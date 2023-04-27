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
	movie_id = sys.argv[1].split("#")[1].split("_")[0]
elif "twitcasting.tv" in sys.argv[1]:	# movie URL
	user = sys.argv[1].split("/")[3]
	movie_id = sys.argv[1].split("/")[5]
else:
	user = sys.argv[1]
	movie_id = sys.argv[2]
page_count = 2

TWITCASTING_URL_JP = "ja.twitcasting.tv"
TWITCASTING_URL_EN = "en.twitcasting.tv"
TWITCASTING_URL_GL = "twitcasting.tv"
TWITCASTING_URL = TWITCASTING_URL_EN
headers = {
	'Host': TWITCASTING_URL,
	'Connection': 'keep-alive',
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"
}

session = requests.Session()


def downloader(page, retries=0):
	url = f"https://{TWITCASTING_URL}/{user}/moviecomment/{movie_id}-{page}"
	print(url, "Retries:", retries)
	try:
		time.sleep(0.5)
		content = session.request(method='GET', url=url, headers=headers, verify=False, timeout=30).content
	except KeyboardInterrupt:
		print("BREAK")
		return "BREAK"
	except:
		content = downloader(page, retries+1)
	return content


out = {"comment": [], "info": {"user": user, "movie_id": int(movie_id), "title": "", "url": f"https://{TWITCASTING_URL}/{user}/movie/{movie_id}"}}
page_num = 0
while (page_num <= int(page_count)):
	# a = open(f"twitcasting_{user}_{movie_id}_{page}.html", encoding="utf-8").read()
	page = downloader(page_num)
	if page == "BREAK":
		break
	comments = list(bs4.BeautifulSoup(page, "lxml").select(".tw-comment-history-item", limit=999))
	# out["info"]["title"] = str(bs4.BeautifulSoup(a, "lxml").title.contents[0]).replace(" Comment - TwitCasting", "").replace(" コメント - ツイキャス", "")
	if page_num == 0:
		out["info"]["title"] = str(bs4.BeautifulSoup(page, "lxml").select(".tw-basic-page-header-path", limit=1)[0].contents[3].contents[1].contents[0]).rstrip(" ")
		page_count = int(bs4.BeautifulSoup(page, "lxml").select(".tw-pager", limit=1)[0].contents[-1].contents[0])
		print(page_count)
	for comment in comments:
		out["comment"].append({
			"id": int(comment.attrs['data-comment-id']),
			"time": int(time.mktime(time.strptime(comment.select(".tw-comment-history-item__info__date")[0].attrs['datetime'], '%a, %d %b %Y %H:%M:%S %z'))),
			"content": str(comment.select(".tw-comment-history-item__content__text")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
			"user_id": comment.select(".tw-comment-history-item__details__user-link")[0].attrs['href'][1:],
			"username": str(comment.select(".tw-comment-history-item__details__user-link")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
			"user_img": ("https:"+comment.select(".tw-comment-history-item__user__icon")[0].attrs['src']).replace("https:https://", "https://")
		})
	page_num += 1
session.close()
open(f"twitcasting_{user}_{movie_id}.json", "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":"), indent="\t").replace("\n\t\t\t", "").replace("\n\t\t}", "}"))
