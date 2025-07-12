import json
import re
from typing import Any

import requests

from .settings import Settings


def get_user_agent():
    res = requests.get(
        "https://raw.githubusercontent.com/fa0311/latest-user-agent/main/header.json"
    )
    headers = res.json()["chrome"]
    headers.update(
        {
            "host": None,
            "connection": None,
            "accept-encoding": None,
            "accept-language": "ja",
        }
    )
    return headers


def set_cookies(cookies: Any, session: requests.Session):
    for cookie in cookies:
        session.cookies.set(
            cookie["name"],
            cookie["value"],
            domain=cookie.get("domain"),
            path=cookie.get("path"),
            secure=cookie.get("secure", False),
        )


if __name__ == "__main__":
    env = Settings()

    session = requests.Session()
    session.headers.update(get_user_agent())
    with open("cookies.json", "r", encoding="utf-8") as f:
        cookies = json.load(f)
    set_cookies(cookies, session)

    res1 = session.get(
        "https://secure.xserver.ne.jp/xapanel/xvps/server/freevps/extend/index",
        params={
            "id_vps": env.id_vps,
        },
    )

    pattern = r'<input type="hidden" name="uniqid" value="(?P<uniqid>[^"]+)" />'
    match = re.search(pattern, res1.text)
    assert match is not None
    uniqid = match.group("uniqid")

    res2 = session.post(
        "https://secure.xserver.ne.jp/xapanel/xvps/server/freevps/extend/do",
        # "https://secure.xserver.ne.jp/xapanel/xvps/server/freevps/extend/conf",
        data={
            "uniqid": uniqid,
            "ethna_csrf": "",
            "id_vps": env.id_vps,
        },
        files={},
    )

    if "利用期限の更新手続きが完了しました。" in res2.text:
        print("Done!")
    elif "利用期限の1日前から更新手続きが可能です。" in res2.text:
        print("Failed, please try again a day before.")
    else:
        raise RuntimeError("Failed to renew VPS")
