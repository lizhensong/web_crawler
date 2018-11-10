#!usr\bin\python3
# -*-encoding:utf-8-*-

__author__ = 'wolf li'

from lxml import etree

from class6_proxy_ip.UseIpProxies.WebDownload import WebDownload
from class6_proxy_ip.UseIpProxies.MkDir import mkdir


def opera_article(html):
    selector = etree.HTML(html)
    article_title = selector.xpath('//*[@id="activity-name"]/text()')[0].strip()
    article_content = selector.xpath('string(//*[@id="js_content"])').strip()
    return [article_title, article_content]


def opera_wei_xin_list(html_info, article_num):
    selector = etree.HTML(html_info[0])
    gong_zhong_hao_info_all = selector.xpath('//li[starts-with(@id,"sogou_vr_")]')
    for gong_zhong_hao_info in gong_zhong_hao_info_all:

        gong_zhong_hao_url = gong_zhong_hao_info.xpath('div/div[2]/p[1]/a/@href')[0]
        gong_zhong_hao_name = gong_zhong_hao_info.xpath('string(div/div[2]/p[1]/a)')
        gong_zhong_hao_introduce = gong_zhong_hao_info.xpath('string(dl[1]/dd)')

        mkdir('./{}'.format(gong_zhong_hao_name))
        print('开始向文件写入数据...')
        with open('./{}/{}'.format(gong_zhong_hao_name, gong_zhong_hao_name+'.txt'), 'w', encoding='utf-8')\
                as file_introduce:
            file_introduce.write(gong_zhong_hao_introduce)
            file_introduce.write('\r\n')

        referer = html_info[1]
        web_download = WebDownload(gong_zhong_hao_url, referer=referer)
        gong_zhong_hao_html_info = web_download.download()
        article_selector = etree.HTML(gong_zhong_hao_html_info[0])
        article_url_list = article_selector.xpath('//*[starts-with(@id,"WXAPPMSG")]/div/h4/@hrefs')
        for i in range(article_num):
            article_url = 'https://mp.weixin.qq.com'+article_url_list[i]
            referer = gong_zhong_hao_html_info[1]
            web_download = WebDownload(article_url, referer=referer)
            article_html_info = web_download.download()
            article_info = opera_article(article_html_info[0])
            print('开始向文件写入数据...')
            with open('./{}/{}'.format(gong_zhong_hao_name, article_info[0] + '.txt'), 'w', encoding='utf-8') \
                    as file_introduce:
                file_introduce.write(article_info[1])
                file_introduce.write('\r\n')


def spider_wei_xin():
    print('---------- 微信公众号获取 ----------')
    page_start = int(input('请输入您想获取的开始页:'))
    page_end = int(input('请输入您想获取的结束页:'))
    article_num = int(input('请输入您每个公众号想要的文章数:'))
    referer = 'https://weixin.sogou.com/'
    for i in range(page_start, page_end + 1):
        print('正在处理第{}页的内容（请耐心等候）......'.format(i))
        now_url = 'https://weixin.sogou.com/weixin'
        params = {
            'query': 'python',
            '_sug_type_': '',
            's_from': 'input',
            '_sug_': 'n',
            'type': '1',
            'page': str(i),
            'ie': 'utf8'
        }
        web_download = WebDownload(now_url, params=params, referer=referer)
        html_info = web_download.download()
        opera_wei_xin_list(html_info, article_num)
        referer = html_info[1]
        print('第{}页信息获取完毕！'.format(i))
        print('------------------------------------')


if __name__ == '__main__':
    spider_wei_xin()
