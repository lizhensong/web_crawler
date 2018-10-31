#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li.csv'

import mysql.connector
from class2_mysql_modul.file_py.db_connect.ConfigReader import ConfigReader


def connect_pool():
    cr = ConfigReader('D:\Python_Work_Space\web_crawler\class2_mysql_modul\config\db.ini')
    conf = cr.get_mysql_info()
    return mysql.connector.connect(
        host=conf.get('host'),
        port=conf.get('port'),
        user=conf.get('user'),
        password=conf.get('password'),
        database=conf.get('database')
    )
