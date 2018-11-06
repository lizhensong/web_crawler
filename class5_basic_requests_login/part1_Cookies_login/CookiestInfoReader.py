#!usr\bin\python3
# -*-encoding:utf-8 -*-

__author__ = 'wolf li'

# 从cookies文件中读取cookies数据


def get_cookies_info(path):
    if path is None or len(path) < 1:
        raise ValueError('The config ini file path required')
    cookies_info = {}
    with open(path, 'r')as f:
        cookies = f.read()
    for k_v in cookies.split(';'):
        # split 函数中1表示分割次数
        k, v = k_v.split('=', 1)
        cookies_info[k.strip()] = v.replace('"', '')
    return cookies_info
