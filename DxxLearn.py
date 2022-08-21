import requests
import os

import DxxLogin

headers = {
    "Host": "m.bjyouth.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6303004c)",
    "Cookie": "Cookie",
    "Referer": "https://m.bjyouth.net/qndxx/index.html"
}

def AchieveHistory():
    url = 'https://m.bjyouth.net/dxx/history'
    res = requests.get(url, headers=headers).json()
    for item in res['data']['data']:
        Historyid = item['id']
        url = f'https://m.bjyouth.net/dxx/history-detail?id={Historyid}'
        requests.get(url, headers=headers).json()


def GetNewCourseid():
    url = 'https://m.bjyouth.net/dxx/course'
    res = requests.get(url, headers=headers).json()
    return res['newCourse']['id']

def AchieveDXX(newCourseid, Orgid):
    url = f"https://m.bjyouth.net/dxx/check?id={newCourseid}&org_id={Orgid}"
    return requests.get(url, headers=headers)

def main():
    print('[info] Start Dxx Login')
    Orgid, Cookies = DxxLogin.main()
    headers['Cookie'] = Cookies

    print('[info] Start Learn History')
    AchieveHistory()

    print('[info] Start Dxx')
    AchieveDXX(GetNewCourseid(), Orgid)

    print('[info] Finish All')

if __name__ == '__main__':
    main()
