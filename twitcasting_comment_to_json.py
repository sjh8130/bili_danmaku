import json
import ssl
import sys
import time
from pathlib import Path

import bs4
import requests

from my_lib.file_writer import write_file

ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with Path("config.json").open(encoding="utf-8") as fp:
    config = json.load(fp)
del fp

_TWITCASTING_URL_JP = "ja.twitcasting.tv"
_TWITCASTING_URL_EN = "en.twitcasting.tv"
_TWITCASTING_URL_GL = "twitcasting.tv"


def _downloader(
    page: int | str,
    host: str,
    user: str,
    movie_id: str,
    session: requests.Session,
) -> bytes:
    retry_count = 0
    page = "" if page in {0, "0"} else f"-{page}"
    url = f"https://{host}/{user}/moviecomment/{movie_id}{page}"
    while True:
        try:
            response = session.get(
                url=url,
                headers={
                    "Accept-Encoding": config["ae"],
                    "Connection": "keep-alive",
                    "Host": host,
                    "User-Agent": config["ua"],
                },
                verify=False,
                timeout=30,
            )
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


def _get_user_and_movie_id() -> tuple[str, str]:
    if "#" in sys.argv[1]:
        user = sys.argv[1].split("#")[0]
        movie_id = sys.argv[1].split("#")[1].split("_")[0]
    elif "twitcasting.tv" in sys.argv[1]:  # movie URL
        user = sys.argv[1].split("/")[3]
        movie_id = sys.argv[1].split("/")[5]
    else:
        user = sys.argv[1]
        movie_id = sys.argv[2]
    return user, movie_id


def _main(user: str, movie_id: str, host: str) -> None:
    session = requests.Session()
    page_count = 0
    comment_list: list[dict] = []
    out = {
        "comment": comment_list,
        "info": {
            "user": user,
            "movie_id": int(movie_id),
            "title": "",
            "url": f"https://{host}/{user}/movie/{movie_id}",
        },
    }
    current_page = 0
    while True:
        page = _downloader(
            page=current_page,
            host=host,
            user=user,
            movie_id=movie_id,
            session=session,
        )
        if page == b"BREAK":
            break
        downloaded_comments = list(bs4.BeautifulSoup(page, "lxml").select(".tw-comment-history-item", limit=999))
        if current_page == 0:
            out["info"]["title"] = str(bs4.BeautifulSoup(page, "lxml").select(".tw-basic-page-header-path", limit=1)[0].contents[3].contents[1].contents[0]).strip()  # type: ignore[index,attr-defined]
            page_count = int(bs4.BeautifulSoup(page, "lxml").select(".tw-pager", limit=1)[0].contents[-1].contents[0])  # type: ignore[attr-defined]
            print(page_count)
        for comment in downloaded_comments:
            comment_list.append(
                {
                    "type": "comment",
                    "id": int(comment.attrs["data-comment-id"]),  # type: ignore
                    "message": str(comment.select(".tw-comment-history-item__content__text")[0].contents[0]).strip("\n").strip("\t").strip(),
                    "createdAt": int(time.mktime(time.strptime(comment.select(".tw-comment-history-item__info__date")[0].attrs["datetime"], "%a, %d %b %Y %H:%M:%S %z"))),  # type: ignore
                    "author": {
                        "id": comment.select(".tw-comment-history-item__details__user-link")[0].attrs["href"][1:],
                        "name": str(comment.select(".tw-comment-history-item__details__user-link")[0].contents[0]).strip("\n").strip("\t").strip(),
                        "profileImage": ("https:" + comment.select(".tw-comment-history-item__user__icon")[0].attrs["src"]).replace("https:https://", "https://"),  # type: ignore
                    },
                },
            )
        current_page += 1
        if current_page >= page_count or current_page >= 100:
            break
    session.close()
    out_data = json.dumps(out, ensure_ascii=False, separators=(",", ":"), indent="\t").replace("\n\t\t\t\t", "").replace("\n\t\t\t", "").replace("\n\t\t}", "}")
    write_file(f"twitcasting_{user}_{movie_id}.json", out_data)


if __name__ == "__main__":
    user, movie_id = _get_user_and_movie_id()
    _main(user, movie_id, _TWITCASTING_URL_GL)
