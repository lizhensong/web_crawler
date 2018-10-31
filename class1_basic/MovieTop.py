#!usr\bin\python3
# -*- coding: UTF-8 -*-

__author__ = 'Wolf Li'

import requests
import re
import mysql.connector

from class3_CSV_modul.CSVUtils import write_csv_file_dict


class MovieTop:
    def __init__(self):
        self.start = 0
        self.param = '&filter='
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/69.0.3497.92 '
                'Safari/537.36'
        }
        self.movie_list = []
        self.file_path = 'D:\movie_spider.txt'

    def get_page(self):
        try:
            url = 'https://movie.douban.com/top250?start='+str(self.start)
            req = requests.get(url, headers=self.headers)
            page = req.text
            page_num = (self.start+25)//25
            print('正在抓取第{}页数据...'.format(page_num))
            self.start += 25
            return page
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'reason'):
                print('抓取失败，失败原因{}'.format(e.reason))

    def get_movie_info(self):
        pattern = re.compile(u'<em.*?class="".*?>(.*?)</em>.*?'
                             + u'<span.*?class="title".*?>(.*?)</span>.*?'
                             + u'<span.*?class="title".*?>&nbsp;/&nbsp;(.*?)</span>.*?'
                             + u'<span.*?class="other".*?>&nbsp;/&nbsp;(.*?)</span>.*?'
                             + u'<p.*?class="".*?>.*?导演:(.*?)&nbsp;&nbsp;&nb.*?'
                             + u'<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?'
                             + u'<span.*?class="rating_num".*?property="v:average".*?>(.*?)</span>.*?'
                             + u'<span>(.*?)人评价</span>.*?'
                             + u'<span.*?class="inq".*?>(.*?)</span>.*?', re.S)
        while self.start <= 175:
            page = self.get_page()
            movies = pattern.findall(page)
            for movie in movies:
                self.movie_list.append({
                    '电影排名': movie[0],
                    '电影名称': movie[1],
                    '外文名称': movie[2],
                    '电影别名': movie[3],
                    '导演姓名': movie[4],
                    '上映年份': str(movie[5]).lstrip(),
                    '制作国家/地区': movie[6],
                    '电影类别': str(movie[7]).rstrip(),
                    '电影评分': movie[8],
                    '参评人数': movie[9],
                    '简短影评': movie[10]
                })

    def write_csv(self):
        print('开始向CSV中写入数据...')
        header = ['电影排名', '电影名称', '外文名称', '电影别名', '导演姓名', '上映年份', '制作国家/地区', '电影类别', '电影评分', '参评人数', '简短影评']
        write_csv_file_dict('D:\Python_Work_Space\web_crawler\class1_basic\movie.csv', header, self.movie_list)

    def write_text(self):
        print('开始向文件写入数据...')
        with open(self.file_path, 'w', encoding='utf-8')as file_top:
            for movie in self.movie_list:
                for movie_info in movie:
                    file_top.write(movie_info+':'+movie[movie_info]+'\r\n')
                file_top.write('\r\n')

    def db_connect(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root123456',
            database='lzs_test'
        )
        cursor = db.cursor()
        cursor.execute('DROP TABLE IF EXISTS douban_comment')
        cursor.execute("CREATE TABLE douban_comment "
                       "(id INT AUTO_INCREMENT PRIMARY KEY, "
                       "movieRank VARCHAR(255),"
                       "movieName VARCHAR(255),"
                       "movieEnglishName VARCHAR(255),"
                       "movieOtherName VARCHAR(255),"
                       "movieDirector VARCHAR(255),"
                       "movieYear VARCHAR(255),"
                       "movieCounty VARCHAR(255),"
                       "movieType VARCHAR(255),"
                       "movieScore VARCHAR(255),"
                       "movieNum VARCHAR(255),"
                       "movieShortFilm VARCHAR(255)"
                       ")")
        insert_str = "insert into douban_comment" \
                     "(movieRank,movieName,movieEnglishName,movieOtherName,movieDirector," \
                     "movieYear,movieCounty,movieType,movieScore,movieNum,movieShortFilm)" \
                     "values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') "

        try:
            for movie in self.movie_list:
                movie_info_list = []
                for movie_info in movie:
                    movie_info_list.append(movie[movie_info])
                insert_sql = insert_str.format(*movie_info_list)
                print(insert_sql)
                cursor.execute(insert_sql)
            db.commit()
        except Exception as e:
            print(e)

    def main(self):
        print('开始从豆瓣电影抓取数据...')
        self.get_movie_info()
        self.write_csv()
        # self.write_text()
        # self.db_connect()
        print('数据抓取完成')


if __name__ == '__main__':
    start = MovieTop()
    start.main()
