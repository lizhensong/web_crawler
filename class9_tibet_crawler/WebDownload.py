#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

# 页面下载

import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/69.0.3497.92 Safari/537.36'
    }


def download(url):
    print('正在下载页面--》'+url)
    res = requests.get(url, headers=headers)
    return res.content
