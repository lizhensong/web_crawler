#!usr\bin\python3
# -*-coding:utf-8-*-

__author__ = 'wolf li'

# 1.登录新浪微博 。2.获取微博首页信息（发布者，url，内容）。
# 3.下一个程序将进行定时刷新爬取，并去重。
# 使用的是selenium配合chrome浏览器操作。（动态网页抓取基本方法）。
# 下一个程序将使用selenium配合谷歌的无头浏览器chrome headless操作。
# 此程序使用的是隐式等待，会在浏览器加载结束才获取元素。（显示等待比其好）
# selenium查找元素的时候，有element和elements的区别。


from selenium import webdriver
import time
import requests
# 导入PIL包处理图片，现在为pillow模块。
from PIL import Image
from io import BytesIO

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login():
    driver.get('https://weibo.com/')
    # 直接设置窗口最大化。
    driver.maximize_window()
    # 可以设置窗口的长宽。
    # driver.set_window_size(1920, 1880)
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, 'loginname')))
    username.send_keys(UserName)
    username = driver.find_element_by_xpath('//*[@id="loginname"]')
    username.send_keys(UserName)
    password = driver.find_element_by_name('password')
    password.send_keys(PassWord)
    # 网页要测试到写入账号，密码才可能弹出验证窗口。
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input[@disabled]')
    except Exception as e:
        captcha_url = driver.find_element_by_xpath(
            '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img'
        ).get_attribute('src')
        captcha_img = requests.get(captcha_url, headers=headers)
        img = Image.open(BytesIO(captcha_img.content))
        img.show()
        captcha_text = input(u'请输入验证码：')
        captcha = driver.find_element_by_name('verifycode')
        captcha.send_keys(captcha_text)
    submit = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
    print('准备登录。。。')
    submit.click()


def spider():
    driver.get('https://weibo.com/')
    all_weibo = driver.find_elements_by_class_name('WB_detail')
    for weibo in all_weibo:
        pub_id = weibo.find_element_by_xpath('div[1]/a[1]').text
        pub_id_url = weibo.find_element_by_xpath('div[1]/a[1]').get_attribute('href')
        pub_content = weibo.find_element_by_xpath('div[4]').text
        print(pub_id, '--->', pub_id_url, '\n', pub_content)


if __name__ == '__main__':
    UserName = '15104664187'
    PassWord = '94380596ZHenSong'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/69.0.3497.92 Safari/537.36'
    }

    # 初始化webdriver,使用chrome浏览器，需要加载其驱动，传参为驱动地址。
    driver = webdriver.Chrome('D:/2345Downloads/chromedriver.exe')
    # 设置隐式等待，对全局的webdriver定义的对象都起作用。
    # 隐式等待会在浏览器加载结束才获取元素。
    driver.implicitly_wait(10)
    login()
    spider()
