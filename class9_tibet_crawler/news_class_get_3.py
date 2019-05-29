from lxml import etree
import os
from class9_tibet_crawler.WebDownload import download
from class9_tibet_crawler import urlSave

news_name_list = ['政务', '农牧', '法律', '科教', '文学艺术', '宗教', '医学', '历史地理', '生态旅游']

all_path = 'D:\英雄时刻\save_url_2'
all_path_1 = 'D:\英雄时刻\save_url_3'
for class_name in news_name_list:
    class_path = os.path.join(all_path, class_name)
    class_path_1 = os.path.join(all_path_1, class_name)
    if not os.path.exists(class_path_1):
        os.makedirs(class_path_1)
    if os.listdir(class_path) is not None:
        for one_url_path_name in os.listdir(class_path):
            one_url = urlSave.read(os.path.join(class_path, one_url_path_name))
            selector = etree.HTML(download(one_url[1]))
            url_list_1 = selector.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div[1]/span[1]/a/@href')
            if len(url_list_1) != 0:
                for num, one_url_list_1 in enumerate(url_list_1):
                    url_1 = one_url[0] + one_url_list_1[2:]
                    urlSave.save(url_1, os.path.join(class_path_1, '{}_{}'.format(one_url_path_name, num)))
            os.remove(os.path.join(class_path, one_url_path_name))