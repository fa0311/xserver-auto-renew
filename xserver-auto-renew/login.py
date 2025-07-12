import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from .settings import LoginSettings

if __name__ == "__main__":
    env = LoginSettings()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get("https://secure.xserver.ne.jp/xapanel/login/xvps/")
    driver.find_element(By.ID, "memberid").send_keys(env.username)
    driver.find_element(By.ID, "user_password").send_keys(env.password)
    driver.execute_script("loginFunc()")

    while driver.current_url != "https://secure.xserver.ne.jp/xapanel/xvps/index":
        driver.implicitly_wait(10)

    cookies = driver.get_cookies()
    with open("cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=4)
