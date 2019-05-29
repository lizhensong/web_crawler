from lxml import etree
from class9_tibet_crawler.WebDownload import download
from class9_tibet_crawler import urlSave

news_name_list = ['政务', '农牧', '法律', '科教', '文学艺术', '宗教', '医学', '历史地理', '生态旅游']
news_url_list = ['zw', 'nmtd', 'fz', 'kjws', 'wxys', 'zxyzj', 'zyzy', 'lsdl', 'stly']
news_class_url = ['http://tb.xzxw.com/' + x for x in news_url_list]
news_name_url_list = []
for i in news_class_url:
    one_class_url_list = []
    selector = etree.HTML(download(i))
    url_list_1 = selector.xpath('/html/body/div[3]/div/ul/li/a/@href')
    if url_list_1 is not None:
        for one_url_list_1 in url_list_1:
            one_class_url_list.append(i + one_url_list_1[1:])
    url_list_2 = selector.xpath('//*[@id="nav_ul"]/a/@href')
    if url_list_2 is not None:
        for one_url_list_2 in url_list_2:
            one_class_url_list.append(i + one_url_list_2[1:])
    news_name_url_list.append(one_class_url_list)

urlSave.save(news_name_url_list, './url_1')