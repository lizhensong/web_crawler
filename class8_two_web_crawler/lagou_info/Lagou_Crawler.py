#!usr\bin\python3
# -*-coding:utf-8-*-

__author__ = 'wolf li'

# 对拉勾网的爬虫的实现（网页版）。

from class8_two_web_crawler.lagou_info.SpiderProxyIp import SpiderProxyIp
import requests
import csv
import random


# 将数据写入CSV文件,head传入list，data传入list包list，每个list一行
def write_csv_file_list(path, open_method='w', head=None, data=None):
    print('正在保存数据')
    try:
        # 如果不指定newline='',则每写入一行将有一空行被写入
        with open(path, open_method, newline='', encoding='utf-8')as csv_file:
            writer = csv.writer(csv_file)
            if head is not None:
                writer.writerow(head)
            if data is not None:
                # 多行
                # writer.writerows(data)
                # 单行
                for row in data:
                    writer.writerow(row)
        print('Write a CSV file to path-->{} is Successful'.format(path))
    except Exception as e:
        raise e


def download(url, data, page_num, referer=None):
    if page_num <= len(ip_list):
        x = page_num - 1
    else:
        x = page_num % len(ip_list) - 1
    ip = ip_list[x]
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/69.0.3497.92 Safari/537.36'    }

    print('正在下载页面--》'+url)
    if referer:
        headers['Referer'] = referer
    try:
        res = requests.post(url, proxies=ip, data=data, headers=headers, timeout=2)
        return res.json()
    except:
        print('请求失败处理。。。')
        ip_list.remove(ip)
        if len(ip_list) <= 1:
            ip_list.extend(SpiderProxyIp().get_ip_list())
        download(url, data, page_num, referer)


def spider(html_json):
    print(html_json)
    one_list = []
    for comp in html_json['content']['positionResult']['result']:
        item = [
            comp['positionName'], comp['workYear'], comp['education'],
            comp['createTime'], comp['city'], comp['companyShortName'], comp['salary']
        ]
        print(item)
        one_list.append(item)
    write_csv_file_list('./test.csv', 'a', data=one_list)
    write_csv_file_list('./test.csv', 'a', data=[[i]])


if __name__ == '__main__':
    write_csv_file_list('./test.csv')
    ip_list = SpiderProxyIp().get_ip_list()
    web_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    referer_url =\
        'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90'
    web_data = {'first': 'false', 'pn': None, 'kd': '数据分析'}
    i = 1
    for i in range(1, 31):
        web_data['pn'] = i
        html = download(web_url, web_data, i, referer=referer_url)
        spider(html)
