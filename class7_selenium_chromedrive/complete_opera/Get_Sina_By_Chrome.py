#!usr\bin\python3
# -*-coding:utf-8-*-

__author__ = 'wolf li'

# 1.登录新浪微博 。2.获取微博首页信息（发布者，url，内容）。
# 3.将进行定时刷新爬取，并去重。
# 使用selenium配合谷歌的无头浏览器chrome headless操作。
# 此程序使用的是显示等待，在需要元素出现时就会获取这个元素。


from selenium import webdriver
# 显示等待需要的三个包
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
# 导入PIL包处理图片，现在为pillow模块。
from PIL import Image
from io import BytesIO
# 导入hashlib，其是一个提供了一些流行hash算法的python标准库。
import hashlib


def login():
    driver.get('https://weibo.com/')
    # 这俩个设置在无头浏览器中不起作用。
    # 直接设置窗口最大化。
    # driver.maximize_window()
    # 可以设置窗口的长宽。
    # driver.set_window_size(1920, 1880)
    # 截屏可以进行无头浏览器测试
    # driver.get_screenshot_as_file("D:/登陆页面.png")
    username = wait.until(EC.presence_of_element_located((By.ID, 'loginname')))
    username.send_keys(UserName)
    password = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
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
    all_weibo = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'WB_detail')))
    for weibo in all_weibo:
        pub_id = weibo.find_element_by_xpath('div[1]/a[1]').text
        pub_id_url = weibo.find_element_by_xpath('div[1]/a[1]').get_attribute('href')
        pub_content = weibo.find_element_by_xpath('div[4]').text
        print(pub_id, '--->', pub_id_url, '\n', pub_content)
        # 计算爬取的内容的摘要（MD5的值），**传入的字符串必须编码为二进制形式。
        hash_content = hashlib.md5(pub_content.encode('utf-8')).hexdigest()
        if hash_content not in is_dup:
            print('写入')
            is_dup.add(hash_content)


if __name__ == '__main__':
    UserName = '15104664187'
    PassWord = '94380596ZHenSong'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/69.0.3497.92 Safari/537.36'
    }
    # 设置浏览器的无头模式。
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--headless')
    # 谷歌文档提到需要加上这个属性来规避bug。禁用 GPU 硬件加速，防止出现bug
    chrome_option.add_argument('--disable-gpu')
    # 设置窗口大小
    chrome_option.add_argument('window-size=1920,1080')
    # 隐藏滚动条, 应对一些特殊页面
    # chrome_option.add_argument('--hide-scrollbars')
    # 不加载图片, 提升速度
    # chrome_option.add_argument('blink-settings=imagesEnabled=false')

    # 初始化webdriver,使用chrome_headless浏览器，需要加载其驱动，传参为驱动地址。
    driver = webdriver.Chrome('D:/2345Downloads/chromedriver.exe', options=chrome_option)

    # 设置显式等待。
    wait = WebDriverWait(driver, 20)
    login()
    # 多次爬取，要去重。
    # 使用哈希算法（摘要算法）--》其可以将不同长度的字符串变为定长的摘要。内容只要有一点点改变，摘要都会变化。
    # 使用的是MD5摘要算法，它可以得到一个128bit的串，然后使用set去重。
    is_dup = set()
    while True:
        spider()
        # 5分钟爬取一次
        time.sleep(300)
