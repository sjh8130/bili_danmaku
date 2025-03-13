import json
import ssl
import sys
import time

import bs4
import lxml
import requests

from my_lib.file_writer import write_file

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("config.json", "r", -1, "utf-8") as fp:
    config = json.load(fp)
del fp

_TWITCASTING_URL_JP = "ja.twitcasting.tv"
_TWITCASTING_URL_EN = "en.twitcasting.tv"
_TWITCASTING_URL_GL = "twitcasting.tv"


def _downloader(
    page: int | str,
    host,
    user,
    movie_id,
    session: requests.Session,
) -> bytes:
    retry_count = 0
    if page in [0, "0"]:
        page = ""
    else:
        page = f"-{page}"
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


def _get_user_and_movie_id():
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


def _main(user, movie_id, host):
    session = requests.Session()
    I_page_count = 0
    LD_comment: list[dict] = []
    D_out = {
        "comment": LD_comment,
        "info": {
            "user": user,
            "movie_id": int(movie_id),
            "title": "",
            "url": f"https://{host}/{user}/movie/{movie_id}",
        },
    }
    I_current_page = 0
    while True:
        # a = open(f"twitcasting_{_user}_{_movie_id}_{page}.html", encoding="utf-8").read()
        page = _downloader(
            page=I_current_page,
            host=host,
            user=user,
            movie_id=movie_id,
            session=session,
        )
        if page == b"BREAK":
            break
        comments = list(
            bs4.BeautifulSoup(page, "lxml").select(
                ".tw-comment-history-item", limit=999
            )
        )
        # _out["info"]["title"] = str(bs4.BeautifulSoup(a, "lxml").title.contents[0]).replace(" Comment - TwitCasting", "").replace(" コメント - ツイキャス", "")
        if I_current_page == 0:
            D_out["info"]["title"] = str(bs4.BeautifulSoup(page, "lxml").select(".tw-basic-page-header-path", limit=1)[0].contents[3].contents[1].contents[0]).strip()  # type: ignore[index,attr-defined]
            I_page_count = int(bs4.BeautifulSoup(page, "lxml").select(".tw-pager", limit=1)[0].contents[-1].contents[0])  # type: ignore[attr-defined]
            print(I_page_count)
        for comment in comments:
            LD_comment.append(
                {
                    "type": "comment",
                    "id": int(comment.attrs["data-comment-id"]),
                    "message": str(
                        comment.select(".tw-comment-history-item__content__text")[
                            0
                        ].contents[0]
                    )
                    .strip("\n")
                    .strip("\t")
                    .strip(),
                    "createdAt": int(
                        time.mktime(
                            time.strptime(
                                comment.select(".tw-comment-history-item__info__date")[
                                    0
                                ].attrs["datetime"],
                                "%a, %d %b %Y %H:%M:%S %z",
                            )
                        )
                    ),
                    "author": {
                        "id": comment.select(
                            ".tw-comment-history-item__details__user-link"
                        )[0].attrs["href"][1:],
                        "name": str(
                            comment.select(
                                ".tw-comment-history-item__details__user-link"
                            )[0].contents[0]
                        )
                        .strip("\n")
                        .strip("\t")
                        .strip(),
                        "profileImage": (
                            "https:"
                            + comment.select(".tw-comment-history-item__user__icon")[
                                0
                            ].attrs["src"]
                        ).replace("https:https://", "https://"),
                    },
                }
            )
        I_current_page += 1
        if I_current_page >= I_page_count or I_current_page >= 100:
            break
    session.close()
    out_data = (
        json.dumps(D_out, ensure_ascii=False, separators=(",", ":"), indent="\t")
        .replace("\n\t\t\t\t", "")
        .replace("\n\t\t\t", "")
        .replace("\n\t\t}", "}")
    )
    write_file(f"twitcasting_{user}_{movie_id}.json", out_data)


if __name__ == "__main__":
    user, movie_id = _get_user_and_movie_id()
    _main(user, movie_id, _TWITCASTING_URL_GL)
