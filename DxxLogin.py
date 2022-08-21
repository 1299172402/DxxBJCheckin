import re
import os

from playwright.sync_api import sync_playwright

import ocr

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

Orgid = ''
cookies = ''

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    while True:
        LoginURL = 'https://m.bjyouth.net/site/login'
        page.goto(LoginURL)
        page.locator('//*[@id="username"]').fill(USERNAME)
        page.locator('//*[@id="password"]').fill(PASSWORD)
        page.locator('//*[@id="verifyCode-image"]').screenshot(path='verifyCode.png')
        verifyCode = ocr.main('verifyCode.png')
        page.locator('//*[@id="verifyCode"]').fill(verifyCode)
        page.locator('//*[@id="loginform"]/ul/li[4]/button').click()
        page.wait_for_timeout(1000)
        if page.url != 'https://m.bjyouth.net/site/login':
            break
    
    global Orgid
    MyOrgURL = 'https://m.bjyouth.net/mine/my-org'
    page.goto(MyOrgURL)
    OrgName = page.locator('//*[@id="item1"]/div/div/div[1]/ul/li/div/div[1]').text_content()
    Orgid = re.search(r'\(\d+\)', OrgName).group()
    Orgid = Orgid[1:-1]

    global cookies
    cookies = context.cookies()
    for item in cookies:
        if item['name'] == 'PHPSESSID':
            cookies = f'PHPSESSID={item["value"]}'

    context.close()
    browser.close()

def main():
    with sync_playwright() as playwright:
        run(playwright)
    return Orgid, cookies

if __name__ == '__main__':
    main()
