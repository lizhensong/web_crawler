#!usr\bin\python3
# -*-encoding:utf-8 -*-

__author__ = 'wolf li'

# 构造表单post提交，登录豆瓣，
# 使用session保持登录后返回的cookies。
# 登录如果有验证，弹出验证图片，人工识别，输入，提交。

import requests
from lxml import etree
# 导入PIL包处理图片，现在为pillow模块。
from PIL import Image
from io import BytesIO

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/69.0.3497.92 Safari/537.36'
    }
data = {
    'source': 'index_nav',
    'form_email': '965234670@qq.com',
    'form_password': 'lizhensong123456'
}
url = 'https://www.douban.com/accounts/login'
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)

captcha = html.xpath('//*[@id="captcha_image"]/@src')
if captcha:
    captcha_url = captcha[0]
    captcha_img = requests.get(captcha_url, headers=headers)
    img = Image.open(BytesIO(captcha_img.content))
    img.show()
    captcha_text = input(u'请输入验证码：')
    captcha_id = captcha_url.split('=')[1].split('&')[0]
    data['captcha-solution'] = captcha_text
    data['captcha-id'] = captcha_id

ses = requests.session()
res = ses.post('https://www.douban.com/accounts/login', data=data, headers=headers)

print(res.text)
