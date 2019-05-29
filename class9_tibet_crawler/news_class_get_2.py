import os
import re
from lxml import etree
from class9_tibet_crawler.WebDownload import download
from class9_tibet_crawler import urlSave

news_name_list = ['政务', '农牧', '法律', '科教', '文学艺术', '宗教', '医学', '历史地理', '生态旅游']
news_url_list = ['zw', 'nmtd', 'fz', 'kjws', 'wxys', 'zxyzj', 'zyzy', 'lsdl', 'stly']
num = 0
for class_name in news_name_list:
    class_path = os.path.join('D:\英雄时刻\save_url_1', class_name)
    class_path_1 = os.path.join('D:\英雄时刻\save_url_2', class_name)
    if not os.path.exists(class_path_1):
        os.makedirs(class_path_1)
    if os.listdir(class_path) is not None:
        for one_url in os.listdir(class_path):
            one_url_path = urlSave.read(os.path.join(class_path, one_url))
            urlSave.save([one_url_path, one_url_path], os.path.join(class_path_1, 'url{}'.format(num)))
            num += 1
            selector = etree.HTML(download(one_url_path))
            url_list_2 = selector.xpath('/html/body/div[4]/div[1]/div[3]/div/script/text()')
            page_num = None
            if len(url_list_2) != 0:
                page_num = re.findall(r'\d+', url_list_2[0])[0]
            if page_num is not None:
                for k in range(1, int(page_num)):
                    urlSave.save([one_url_path, one_url_path + 'index_{}.html'.format(k)], os.path.join(class_path_1, 'url{}'.format(num)))
                    num += 1
            os.remove(os.path.join(class_path, one_url))
