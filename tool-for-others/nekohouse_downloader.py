import dataclasses
import datetime
import json
import logging
import os
import ssl
import sys
import time

import bs4
import lxml
import re
import requests

# Setup SSL and logging
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]

AE = "gzip, deflate, br, zstd"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("nekohouse-downloader")
logger.setLevel(logging.ERROR)


@dataclasses.dataclass
class Post:
    content: str = ""
    items: list = dataclasses.field(default_factory=list)
    platform: str = ""
    post_id: str = ""
    pub_time: float = 0.0
    thumb: str = ""
    title: str = ""
    user_id: str = ""
    username: str = ""


@dataclasses.dataclass
class UserPage:
    total: int = 0
    posts: list[Post] = dataclasses.field(default_factory=list)


def _escape_html(s: str) -> str:
    return re.sub(r"[<>\"&']", "_", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("&", "&amp;").strip()


def _escape_path(s: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", s).strip()


def _get_posts_page(p: Post) -> Post:
    url = f"https://nekohouse.su/{p.platform}/user/{p.user_id}/post/{p.post_id}"
    headers = {
        "Accept-Encoding": AE,
        "Connection": "keep-alive",
        "Host": "nekohouse.su",
        "Referer": f"https://nekohouse.su/{p.platform}/user/{p.user_id}",
        "User-Agent": UA,
    }

    logger.info(f"[getPostsPage] {p.platform} {p.user_id} {p.post_id}")
    response = session.get(url, headers=headers, verify=False)
    soup = bs4.BeautifulSoup(response.content, "lxml")

    # Extract the post content
    content_tag = soup.select_one("div.scrape__content")
    p.content = content_tag.decode_contents().strip() if content_tag else ""

    # Extract additional items (like media attachments)
    attachment_links = soup.select("a.scrape__attachment-link, div.fileThumb")
    p.items = ["https://nekohouse.su" + itm.attrs["href"] for itm in attachment_links]

    return p


def _get_user_page(pl: str, user_id: str, pn: int) -> UserPage:
    offset = f"?o={pn * 50}" if pn > 0 else ""
    url = f"https://nekohouse.su/{pl}/user/{user_id}{offset}"
    headers = {
        "Accept-Encoding": AE,
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "nekohouse.su",
        "Referer": f"https://nekohouse.su/{pl}/user/{user_id}",
        "User-Agent": UA,
    }

    logger.info(f"[getUserPage] {pl} {user_id} {pn}")
    response = session.get(url, headers=headers, verify=False)
    soup = bs4.BeautifulSoup(response.content, "lxml")

    total = int(soup.select(".paginator")[0].small.contents[0].strip().split(" ")[-1])  # type: ignore[union-attr]
    posts = []
    for itm in soup.select(".post-card.post-card--preview.post-card--scrape"):
        post_id = itm.a["href"].split("/")[-1]  # type: ignore[union-attr,index]
        pub_time = time.mktime(time.strptime(itm.footer.time["datetime"], "%Y-%m-%d %H:%M:%S%z"))  # type: ignore[arg-type,union-attr,index]
        thumb = "https://nekohouse.su" + itm.select(".post-card__image")[0].attrs["src"]
        title = itm.header.text.strip()  # type: ignore[union-attr]
        posts.append(
            Post(
                platform=pl,
                user_id=user_id,
                post_id=post_id,
                pub_time=pub_time,
                thumb=thumb,
                title=title,
            )
        )

    return UserPage(total=total, posts=posts)


def _aria2_downloader(path: str, url: str):
    logger.info(f"[aria2Downloader] {path} {url}")
    if not isinstance(url, str):
        logger.error(f"[aria2Downloader] {url}")
    param = {
        "method": "aria2.addUri",
        "id": f"nekohouse_downloader_{time.time()}",
        "params": [
            "token:AAAAA",
            [url],
            {
                "dir": path,
                "remote-time": "true",
                "user-agent": UA,
            },
        ],
    }
    session.post("http://127.0.0.1:6800/jsonrpc", json=param)


def _get_users(p, u) -> tuple[str, str]:
    U = "https://nekohouse.su/api/creators"
    F = "Z:\\creators"
    H = {
        "Accept-Encoding": AE,
        "Connection": "keep-alive",
        "Host": "nekohouse.su",
        "Referer": f"https://nekohouse.su/",
        "User-Agent": UA,
    }
    data: list[dict]
    if not os.path.exists(F):
        response = session.get(U, headers=H, verify=False)
        data = response.json()
        with open(F, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False)
    else:
        with open(F, "r", encoding="utf-8") as fp:
            data = json.load(fp)

    for itm in data:
        if (u == itm["name"] or u == itm["user_id"]) and p == itm["service"]:
            return itm.get("user_id", ""), itm.get("name", "")
    return "", ""


def _get_posts_file(bp: str, p: Post):
    logger.info(f"[getPostsFile] {p.platform} {p.post_id} {p.title}")
    date = datetime.datetime.fromtimestamp(p.pub_time).strftime("%Y%m%d")
    path = os.path.join(bp, f"[{date}] [{p.post_id}] {_escape_path(p.title)}")
    for i in p.items:
        _aria2_downloader(path, i)


def main():
    argv = sys.argv
    if len(argv) == 1:
        print(f"{argv[0]} <service> <user_id/user_name> [max_pn] [base_path] ")
        print(f"{argv[0]} <url> [max_pn] [base_path] ")
        return
    if argv[1].startswith("https"):
        _t = [_ for _ in argv[1].split("/") if _]
        service = _t[2]
        user_id, user_name = _get_users(service, _t[4])
        del _t
        try:
            max_pn = int(argv[2])
        except:
            max_pn = -1

        try:
            base_path = argv[3] + f"/{service}[{user_name}]"
        except:
            base_path = os.path.abspath(".") + f"/[{service}]{user_name}"
    else:
        service = argv[1]
        try:
            max_pn = int(argv[3])
        except:
            max_pn = -1
        user_id, user_name = _get_users(service, argv[2])
        try:
            base_path = argv[4] + f"/{service}[{user_name}]"
        except:
            base_path = os.path.abspath(".") + f"/[{service}]{user_name}"
    item_count = 2
    page_num = 0
    try:
        while True:
            user_page = _get_user_page(service, user_id, page_num)
            item_count = user_page.total
            for pn2 in range(user_page.posts.__len__()):
                user_page.posts[pn2] = _get_posts_page(user_page.posts[pn2])
                _get_posts_file(base_path, user_page.posts[pn2])
            page_num += 1
            if page_num >= max_pn and max_pn > 0:
                break
            if (page_num + 1) * 50 > item_count:
                break
            time.sleep(30)
    except KeyboardInterrupt:
        pass
    raise


if __name__ == "__main__":
    session = requests.Session()
    main()
