#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

# 图片保存

import requests


headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/69.0.3497.92 Safari/537.36'
    }


def image_save(url, path):
    print('正在保存图片--》' + url)
    img_res = requests.get(url, headers=headers)
    with open(path, 'wb')as img_f:
        img_f.write(img_res.content)
