#!usr\bin\python3
# -*-encoding:utf-8 -*-

__author__ = 'wolf li'

# 直接使用已经登录的cookies，获取页面

import requests

from class5_basic_requests_login.part1_Cookies_login.CookiestInfoReader import get_cookies_info

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/69.0.3497.92 Safari/537.36'
    }


res = requests.get('https://www.douban.com/', headers=headers, cookies=get_cookies_info('./cookies.ini'))

print(res.text)

