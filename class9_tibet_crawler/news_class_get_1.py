import os
from class9_tibet_crawler import urlSave

news_name_list = ['政务', '农牧', '法律', '科教', '文学艺术', '宗教', '医学', '历史地理', '生态旅游']
news_url_list = ['zw', 'nmtd', 'fz', 'kjws', 'wxys', 'zxyzj', 'zyzy', 'lsdl', 'stly']
news_class_url = urlSave.read('./url_1')
news_name_url_list = []
k = 0
for num, i in enumerate(news_class_url):
    one_class_url_list = []
    class_path = os.path.join('D:\英雄时刻\save_url_1', news_name_list[num])
    if not os.path.exists(class_path):
        os.makedirs(class_path)
    for j in i:
        k += 1
        url_document_path = os.path.join(class_path, 'url{}'.format(k))
        urlSave.save(j,url_document_path)
#         selector = etree.HTML(download(j))
#         url_list_1 = selector.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div[1]/span[1]/a/@href')
#         if url_list_1 is not None:
#             for one_url_list_1 in url_list_1:
#                 one_class_url_list.append(j + one_url_list_1[2:])
#         url_list_2 = selector.xpath('/html/body/div[4]/div[1]/div[3]/div/script/text()')
#         page_num = re.findall(r'\d+',url_list_2[0])[0]
#         if page_num is not None:
#             for k in range(1, int(page_num)):
#                 k_html = etree.HTML(download(j+'index_{}.html'.format(k)))
#                 url_list_3 = selector.xpath('/html/body/div[4]/div[1]/div[2]/ul/li/div[1]/span[1]/a/@href')
#                 if url_list_3 is not None:
#                     for one_url_list_3 in url_list_3:
#                         one_class_url_list.append(j + one_url_list_3[2:])
#         news_name_url_list.append(one_class_url_list)
# urlSave.save(news_name_url_list, './url_2')
# get_text(news_name_url_list,'D:\英雄时刻')
