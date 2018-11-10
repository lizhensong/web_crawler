#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

# 页面下载

import requests
import time
import random

from class6_proxy_ip.UseIpProxies.GetIp import get_ip_list


class WebDownload(object):
    def __init__(self, url, params=None, referer=None):
        self.url = url
        self.params = params
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/69.0.3497.92 Safari/537.36'
        }
        if referer:
            self.headers['Referer'] = referer

    def __new__(cls, *args, **kwargs):
        if not hasattr(WebDownload, "_instance"):
            WebDownload._instance = super().__new__(cls)
            cls.ip_list = get_ip_list()
        return WebDownload._instance

    def download(self):
        print('正在下载页面--》' + self.url)
        time.sleep(1)
        res = requests.get(self.url, params=self.params, proxies=random.choice(self.ip_list), headers=self.headers)
        return [res.text, res.url]
