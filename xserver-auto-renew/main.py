from urllib.parse import urlencode, urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By

from .settings import Settings

if __name__ == "__main__":
    env = Settings()

    driver = webdriver.Chrome()

    driver.get("https://secure.xserver.ne.jp/xapanel/login/xvps/")
    driver.find_element(By.CSS_SELECTOR, "#memberid").send_keys(env.username)
    driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys(env.password)
    driver.execute_script("loginFunc()")

    while True:
        driver.implicitly_wait(1)
        url = urlparse(driver.current_url)
        if url.hostname == "secure.xserver.ne.jp":
            if url.path == "/xapanel/myaccount/loginauth/index":
                form1 = driver.find_element(By.CSS_SELECTOR, ".twoStepAuthBox")
                form1.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
                code = input("Code: ")
                form2 = driver.find_element(By.CSS_SELECTOR, ".twoStepAuthBox")
                form2.find_element(By.CSS_SELECTOR, "#auth_code").send_keys(code)
                form2.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            if url.path == "/xapanel/xvps/index":
                break

    table = driver.find_element(By.CSS_SELECTOR, "#serverContract")
    for tr in table.find_elements(By.CSS_SELECTOR, "tr"):
        if len(tr.find_elements(By.CSS_SELECTOR, ".freeServerIco")) > 0:
            target = tr.find_element(By.CSS_SELECTOR, "[data-memo-target]")
            id = target.get_attribute("data-memo-target")

            params = {"id_vps": id}
            update_url = f"https://secure.xserver.ne.jp/xapanel/xvps/server/freevps/extend/index?{urlencode(params)}"

            driver.get(update_url)

            while True:
                driver.implicitly_wait(1)
                # TODO
