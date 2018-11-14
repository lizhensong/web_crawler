#!usr\bin\python3
# -*-encoding:utf-8-*-
# 免费代理太不好用了！！！！！

__author__ = 'wolf li'

from lxml import etree
import requests
import telnetlib
from multiprocessing.dummy import Pool


class SpiderProxyIp:
    def __init__(self):
        self.data_list = []

    # 批量获取高匿代理ip
    def ip_opera(self, html_page):
        selector = etree.HTML(html_page)
        # 获取代理ip
        agency_ip = selector.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
        # 获取代理ip的端口号
        agency_port = selector.xpath('//*[@id="ip_list"]/tr/td[3]/text()')
        # 获取代理ip的类型
        agency_protocol = selector.xpath('//*[@id="ip_list"]/tr/td[6]/text()')
        # 高匿代理ip页面中所列出的ip数量
        ip_number = len(agency_ip)
        print('{}个ip需要验证（请耐心等候）......'.format(ip_number))
        pool = Pool(4)
        for i in range(ip_number):
            pool.apply_async(self.ip_test, (agency_protocol[i], agency_ip[i], agency_port[i]))
        pool.close()
        # 等待所有线程结束
        pool.join()

    # 验证获取到的代理IP是否可用
    def ip_test(self, verify_protocol, verify_ip, verify_ip_port):
        print('ip号：{}，端口号：{}'.format(verify_ip, verify_ip_port))
        print('正在验证此代理IP是否可用......')
        if verify_protocol.lower == 'http':
            return None
        try:
            telnetlib.Telnet(verify_ip, verify_ip_port, timeout=1)
        except Exception as e:
            print('此代理IP不可用')
            print('-------------------------')
            return None
        else:
            print('此代理IP可用')
            print('-------------------------')
            self.data_list.append(
                {verify_protocol.lower(): verify_protocol.lower() + '://' + verify_ip + ':' + verify_ip_port}
            )
            return 'ok'

    # 获取代理ip主程序
    def get_ip_list(self):
        print('---------- 高匿代理ip获取 ----------')
        url = 'http://www.xicidaili.com/nn/'
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/69.0.3497.92 Safari/537.36'
        }
        html = requests.get(url, headers=headers).text
        self.ip_opera(html)
        print('------------代理获取完毕！-----------')
        return self.data_list


if __name__ == '__main__':
    spider_ip = SpiderProxyIp()
    print(spider_ip.get_ip_list())
