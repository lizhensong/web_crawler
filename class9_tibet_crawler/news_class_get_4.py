from lxml import etree
import os
from class9_tibet_crawler.WebDownload import download
from class9_tibet_crawler import urlSave

news_name_list = ['政务', '农牧', '法律', '科教', '文学艺术', '宗教', '医学', '历史地理', '生态旅游']

all_path = 'D:\英雄时刻\save_url_3'
all_text_path = 'D:\英雄时刻\save_text'
for class_name in news_name_list:
    class_path = os.path.join(all_path, class_name)
    class_text_path = os.path.join(all_text_path, class_name)
    if not os.path.exists(class_text_path):
        os.makedirs(class_text_path)
    if os.listdir(class_path) is not None:
        for one_url_path_name in os.listdir(class_path):
            one_url = urlSave.read(os.path.join(class_path, one_url_path_name))
            selector = etree.HTML(download(one_url), etree.HTMLParser(encoding='utf-8'))
            url_list_1 = selector.xpath('string(/html/body/div[4]/div[1]/div[2]/ul/li[2]/div[2]/div[1])').strip()
            if len(url_list_1) != 0:
                one_document_path = os.path.join(class_text_path, '{}.txt'.format(one_url_path_name))
                with open(one_document_path, 'w', encoding='utf-8') as f:
                    f.write(url_list_1)
            os.remove(os.path.join(class_path, one_url_path_name))
