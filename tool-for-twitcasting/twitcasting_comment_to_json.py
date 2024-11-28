import sys
import time
import json
import ssl

import bs4
import lxml
import requests

from my_lib.file_writer import write_file

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]

if "#" in sys.argv[1]:
    _user = sys.argv[1].split("#")[0]
    _movie_id = sys.argv[1].split("#")[1].split("_")[0]
elif "twitcasting.tv" in sys.argv[1]:  # movie URL
    _user = sys.argv[1].split("/")[3]
    _movie_id = sys.argv[1].split("/")[5]
else:
    _user = sys.argv[1]
    _movie_id = sys.argv[2]
_page_count = 2

_TWITCASTING_URL_JP = "ja.twitcasting.tv"
_TWITCASTING_URL_EN = "en.twitcasting.tv"
_TWITCASTING_URL_GL = "twitcasting.tv"
_TWITCASTING_URL = _TWITCASTING_URL_EN
_headers = {
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Host": _TWITCASTING_URL,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52",
}

_session = requests.Session()


def _downloader(page: int | str):
    retry_count = 0
    url = f"https://{_TWITCASTING_URL}/{_user}/moviecomment/{_movie_id}-{page}"
    while True:
        try:
            response = _session.get(url, headers=_headers, verify=False, timeout=30)
            response.raise_for_status()
            return response.content
        except KeyboardInterrupt:
            print("BREAK")
            return b"BREAK"
        except Exception as e:
            retry_count += 1
            print(f"Error fetching {url}: {e}, {retry_count}")
            time.sleep(1)
        if retry_count > 5:
            raise


_out = {
    "comment": [],
    "info": {
        "user": _user,
        "movie_id": int(_movie_id),
        "title": "",
        "url": f"https://{_TWITCASTING_URL_GL}/{_user}/movie/{_movie_id}",
    },
}
_current_page = 0
_end = False
while not _end:
    # a = open(f"twitcasting_{_user}_{_movie_id}_{page}.html", encoding="utf-8").read()
    page = _downloader(_current_page)
    if page == b"BREAK":
        break
    comments = list(bs4.BeautifulSoup(page, "lxml").select(".tw-comment-history-item", limit=999))
    # _out["info"]["title"] = str(bs4.BeautifulSoup(a, "lxml").title.contents[0]).replace(" Comment - TwitCasting", "").replace(" コメント - ツイキャス", "")
    if _current_page == 0:
        _out["info"]["title"] = str(bs4.BeautifulSoup(page, "lxml").select(".tw-basic-page-header-path", limit=1)[0].contents[3].contents[1].contents[0]).rstrip(" ")  # type: ignore[index,attr-defined]
        _page_count = int(bs4.BeautifulSoup(page, "lxml").select(".tw-pager", limit=1)[0].contents[-1].contents[0])  # type: ignore[attr-defined]
        print(_page_count)
    for comment in comments:
        _out["comment"].append(  # type: ignore[attr-defined]
            {
                "type": "comment",
                "id": int(comment.attrs["data-comment-id"]),
                "message": str(comment.select(".tw-comment-history-item__content__text")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
                "createdAt": int(
                    time.mktime(
                        time.strptime(
                            comment.select(".tw-comment-history-item__info__date")[0].attrs["datetime"],
                            "%a, %d %b %Y %H:%M:%S %z",
                        )
                    )
                ),
                "author": {
                    "id": comment.select(".tw-comment-history-item__details__user-link")[0].attrs["href"][1:],
                    "name": str(comment.select(".tw-comment-history-item__details__user-link")[0].contents[0]).lstrip("\n").lstrip("\t").lstrip(" ").rstrip(" "),
                    "profileImage": ("https:" + comment.select(".tw-comment-history-item__user__icon")[0].attrs["src"]).replace("https:https://", "https://"),
                },
            }
        )
    _current_page += 1
    if _page_count >= _current_page:
        _end = True
_session.close()
out_data = json.dumps(_out, ensure_ascii=False, separators=(",", ":"), indent="\t").replace("\n\t\t\t\t", "").replace("\n\t\t\t", "").replace("\n\t\t}", "}")

write_file(f"twitcasting_{_user}_{_movie_id}.json", out_data)
