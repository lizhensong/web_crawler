#!usr\bin\python3
# -*-encoding:utf-8-*-

__author__ = 'wolf li'

# 创建目录

import os


def mkdir(path):

    is_exists = os.path.exists(path)
    if is_exists:
        print(path + '目录已存在')
        return False
    else:
        os.makedirs(path)

        print(path + '创建成功')
        return True
