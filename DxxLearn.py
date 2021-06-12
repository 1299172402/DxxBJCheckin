import requests
import json
import os

Cookie = os.environ["cookies"]

headers = {
    "Host": "m.bjyouth.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303004c)",
    "Cookie": Cookie,
    "Referer": "https://m.bjyouth.net/qndxx/index.html"
}

def AchieveDXX():
    url = "https://m.bjyouth.net/dxx/check?id=45&org_id=3574566"
    return requests.get(url, headers=headers)

def main():
    AchieveDXX()

if __name__ == '__main__':
    main()
