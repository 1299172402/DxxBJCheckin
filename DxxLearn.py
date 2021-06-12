import requests
import json
import os
import time

Cookie = os.environ["cookies"]

headers = {
    "Host": "m.bjyouth.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303004c)",
    "Cookie": Cookie,
    "Referer": "https://m.bjyouth.net/qndxx/index.html"
}

def GetIndex():
    url = "https://m.bjyouth.net/dxx/index"
    return json.loads(requests.get(url, headers=headers).text)

def GetMyInfo():
    url = "https://m.bjyouth.net/dxx/my"
    return json.loads(requests.get(url, headers=headers).text)

def AchieveDXX():
    url = "https://m.bjyouth.net/dxx/check?id=45&org_id=3574566"
    return requests.get(url, headers=headers)

def GetMyLearned():
    url = "https://m.bjyouth.net/dxx/my-integral"
    return json.loads(requests.get(url, headers=headers).text)

def CheckCourse():
    res = GetIndex()
    title_new = res["newCourse"]["title"]

    res = GetMyLearned()
    title_latest = res["data"][0]["title"]

    if title_latest!=title_new:
        print(f"未学习最新一期")
        raise ValueError("NOT Learned")
    else:
        print(f"最新的 {title_latest} 已完成")

def main():
    print(GetIndex())
    print(GetMyLearned())
    AchieveDXX()
    time.sleep(10)
    CheckCourse()

if __name__ == '__main__':
    main()
