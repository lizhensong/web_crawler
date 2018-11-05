#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

# 运行主程序，初始化线程池
# 多线程爬取文件

from multiprocessing.dummy import Pool

from class4_basic_crawler.SpiderHouse import spider_house


if __name__ == '__main__':
    pool = Pool(4)
    house_url = ['https://shenzhen.qfang.com/sale/f'+str(x) for x in range(1, 2)]
    pool.map(spider_house, house_url)
    pool.close()
    # 等待所有线程结束
    pool.join()
