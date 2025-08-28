import dataclasses
import datetime
import json
import re
import ssl
import sys
import time
from pathlib import Path

import bs4
import requests
from loguru import logger

ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("../config.json", encoding="utf-8") as fp:
    config = json.load(fp)
del fp
AE = config["ae"]
UA = config["ua"]
log = logger.bind(user="nekohouse-downloader")


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
    soup = bs4.BeautifulSoup(response.content, ["lxml"])
    # Extract the post content
    content_tag = soup.select_one("div.scrape__content")
    p.content = content_tag.decode_contents().strip() if content_tag else ""
    # Extract additional items (like media attachments)
    attachment_links = soup.select("a.scrape__attachment-link, div.fileThumb")
    p.items = ["https://nekohouse.su" + itm.attrs["href"] for itm in attachment_links]  # pyright: ignore[reportOperatorIssue]
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
    try:
        total = int(soup.select(".paginator")[0].small.contents[0].strip().split(" ")[-1])  # pyright: ignore[reportAttributeAccessIssue, reportOptionalMemberAccess]
    except AttributeError:
        total = 0
    posts = []
    for itm in soup.select(".post-card.post-card--preview.post-card--scrape"):
        post_id = itm.a["href"].split("/")[-1]  # pyright: ignore[reportOptionalSubscript, reportAttributeAccessIssue]
        pub_time = time.mktime(time.strptime(itm.footer.time["datetime"], "%Y-%m-%d %H:%M:%S%z"))  # pyright: ignore[reportOptionalMemberAccess, reportArgumentType, reportOptionalSubscript]
        thumb = "https://nekohouse.su" + itm.select(".post-card__image")[0].attrs["src"]  # pyright: ignore[reportOperatorIssue]
        title = itm.header.text.strip()  # pyright: ignore[reportOptionalMemberAccess]
        posts.append(Post(platform=pl, user_id=user_id, post_id=post_id, pub_time=pub_time, thumb=thumb, title=title))
    return UserPage(total=total, posts=posts)


def _aria2_downloader(path: Path, url: str) -> None:
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
                "dir": str(path),
                "remote-time": "true",
                "user-agent": UA,
            },
        ],
    }
    session.post("http://127.0.0.1:6800/jsonrpc", json=param)


def _get_users(p, u) -> tuple[str, str]:
    U = "https://nekohouse.su/api/creators"
    F = Path("Z:\\creators").resolve()
    H = {
        "Accept-Encoding": AE,
        "Connection": "keep-alive",
        "Host": "nekohouse.su",
        "Referer": "https://nekohouse.su/",
        "User-Agent": UA,
    }
    data: list[dict]
    if not F.exists():
        response = session.get(U, headers=H, verify=False)
        data = response.json()
        with F.open("w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False)
    else:
        with F.open(encoding="utf-8") as fp:
            data = json.load(fp)
    for itm in data:
        if (u == itm["name"] or u == itm["user_id"]) and p == itm["service"]:
            return (itm.get("user_id", ""), itm.get("name", ""))
    return ("", "")


def _get_posts_file(bp: Path, p: Post) -> None:
    logger.info(f"[getPostsFile] {p.platform} {p.post_id} {p.title}")
    tz = datetime.timezone(datetime.timedelta(milliseconds=0))
    date = datetime.datetime.fromtimestamp(p.pub_time, tz).strftime("%Y%m%d")
    path = bp / f"[{date}] [{p.post_id}] {_escape_path(p.title)}"
    for i in p.items:
        _aria2_downloader(path, i)


def main() -> None:
    argv = sys.argv
    if len(argv) == 1:
        print(f"{argv[0]} <service> <user_id/user_name> [max_pn] [base_path] ")
        print(f"{argv[0]} <url> [max_pn] [base_path] ")
        return
    if argv[1].startswith("https"):
        t = [_ for _ in argv[1].split("/") if _]
        service = t[2]
        user_id, user_name = _get_users(service, t[4])
        del t
        try:
            max_pn = int(argv[2])
        except IndexError:
            max_pn = -1
        try:
            base_path = Path(argv[3]).resolve() / f"{service}[{user_name}]"
        except IndexError:
            base_path = Path.cwd() / f"[{service}]{user_name}"
    else:
        service = argv[1]
        try:
            max_pn = int(argv[3])
        except IndexError:
            max_pn = -1
        user_id, user_name = _get_users(service, argv[2])
        try:
            base_path = Path(argv[4]).resolve() / f"{service}[{user_name}]"
        except IndexError:
            base_path = Path.cwd() / f"[{service}]{user_name}"
    item_count = 2
    page_num = 0
    try:
        while True:
            user_page = _get_user_page(service, user_id, page_num)
            item_count = max(item_count, user_page.total)
            for pn2 in range(len(user_page.posts)):
                user_page.posts[pn2] = _get_posts_page(user_page.posts[pn2])
                _get_posts_file(base_path, user_page.posts[pn2])
            page_num += 1
            print(f"[{service}]{user_name}: ")
            if page_num >= max_pn > 0:
                break
            if (page_num + 1) * 50 > item_count:
                break
            time.sleep(30)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    session = requests.Session()
    try:
        main()
    except Exception as e:
        logger.exception(e)
