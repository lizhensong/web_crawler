#!usr\bin\python3
# -*-encoding:utf-8-*-

__author__ = 'wolf li'

# 返回一个代理ip列表

from class6_proxy_ip.GetIpProxies.CSVUtils import read_csv_file_list


def get_ip_list():
    ip_list = read_csv_file_list('D:\Python_Work_Space\web_crawler\class6_proxy_ip\GetIpProxies\ip.csv')
    ip_dict_list = []
    for ip in ip_list:
        ip_dict_list.append({ip[0]: ip[1]})
    return ip_dict_list


if __name__ == '__main__':
    get_ip_list()
