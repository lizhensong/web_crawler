#!usr\bin\python3
# -*-encoding:utf-8-*-

__author__ = 'wolf li'

from lxml import etree
import time
import telnetlib
# 验证某个ip是否可用

from class6_proxy_ip.GetIpProxies.WebDownload import download
from class6_proxy_ip.GetIpProxies.CSVUtils import write_csv_file_list


# 批量获取高匿代理ip
def ip_opera(html_page):
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
    data_list = []
    for j in range(ip_number):
        print('第{}个，ip号：{}，端口号：{}'.format(j, agency_ip[j], agency_port[j]))
        test_info = ip_test(agency_ip[j], agency_port[j])
        if test_info:
            data_list.append([agency_protocol[j].lower(), agency_protocol[j].lower()+'://'+agency_ip[j]+':'+agency_port[j]])
    write_csv_file_list('./ip.csv', data=data_list)


# 验证获取到的代理IP是否可用
def ip_test(verify_ip, verify_ip_port):
    print('正在验证此代理IP是否可用......')
    try:
        telnetlib.Telnet(verify_ip, verify_ip_port, timeout=1)
    except Exception as e:
        print('此代理IP不可用')
        print('-------------------------')
        return None
    else:
        print('此代理IP可用')
        print('-------------------------')
        return 'ok'


if __name__ == '__main__':
    print('---------- 高匿代理ip获取 ----------')
    page_start = int(input('请输入您想获取的开始页:'))
    page_end = int(input('请输入您想获取的结束页:'))
    referer = 'http://www.xicidaili.com/'
    for i in range(page_start, page_end + 1):
        print('正在处理第{}页的内容（请耐心等候）......'.format(i))
        now_url = 'http://www.xicidaili.com/nn/'+str(i)
        html = download(now_url, referer)
        referer = now_url
        ip_opera(html)
        print('第{}页代理获取完毕！'.format(i))
        print('------------------------------------')
        time.sleep(2)
