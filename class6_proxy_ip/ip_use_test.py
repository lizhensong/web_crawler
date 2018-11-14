from class6_proxy_ip.UseIpProxies.GetIp import get_ip_list

import requests


def download():
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/69.0.3497.92 Safari/537.36'
    }
    ip_list = get_ip_list()

    for ip in ip_list:
        print('应该为--》{}'.format(ip))
        # 返回实际ip
        res = requests.get('http://icanhazip.com', headers=headers, proxies=ip)
        print('实际为--》{}'.format(res.text))


if __name__ == '__main__':
    download()
