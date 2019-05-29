#!usr\bin\python3
# -*- encoding:utf-8 -*-

__author__ = 'wolf li'

# 爬取深圳Q房网数据：小区名称、特点、户型、面积、租金，
# 登记经济人姓名、服务年限、历史成交套数，房源图片。

from lxml import etree

from class9_tibet_crawler.WebDownload import download
from class9_tibet_crawler.urlSave import image_save
from class3_CSV_modul.CSVUtils import write_csv_file_dict


def spider_house(url):
    selector = etree.HTML(download(url))
    house_list = selector.xpath('//*[@id="cycleListings"]/ul/li')
    for house in house_list:

        apartment_name = house.xpath('div[1]/p[1]/a/text()')[0].replace('/', '')
        image_url = house.xpath('a/img/@data-original')[0].strip()
        image_save(image_url, './Q_fang_image/{}.jpg'.format(apartment_name))

        house_url = (
                'https://shenzhen.qfang.com'
                + house.xpath('div[1]/p[1]/a/@href')[0].strip()
        )
        house_info = etree.HTML(download(house_url))
        house_yard = house_info.xpath('//*[@id="headInfo"]/div/div[2]/div[2]/ul/li[1]/p/a/text()')[0]
        house_module = house_info.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[1]/div/ul/li[1]/div/text()')[0]
        house_area = house_info.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[1]/div/ul/li[3]/div/text()')[0]
        house_money = house_info.xpath('//*[@id="headInfo"]/div/div[2]/p/span/text()')[0]
        house_feature = house_info.xpath('string(//*[@id="hsEvaluation"]/ul)').strip()

        house_broker_url = (
                'https://shenzhen.qfang.com'
                + house_info.xpath('//*[@id="headInfo"]/div/div[2]/div[4]/p/a/@href')[0].strip()
        )
        house_broker_info = etree.HTML(download(house_broker_url))
        house_broker_name = house_broker_info.xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/p[1]/text()')[0]
        house_broker_year = house_broker_info.xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/div[3]/span[2]/em/text()'
        )[0]
        house_broker_count = house_broker_info.xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/div[2]/p[1]/span[2]/em/text()'
        )[0]

        item_key = ['房源图片', '小区名称', '户型', '面积', '价格（万元）', '经纪人名字', '经纪人年限（年）', '经纪人成交数（套）']
        item_value = [
            '{}.jpg'.format(apartment_name),
            house_yard, house_module, house_area, house_money,
            house_broker_name, house_broker_year, house_broker_count
        ]
        house_dict = dict(zip(item_key, item_value))
        write_csv_file_dict('./Q_fang_info.csv', 'a', item_key, [house_dict])
