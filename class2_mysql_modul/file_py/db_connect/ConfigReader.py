#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li.csv'

import configparser


class ConfigReader:
    def __init__(self, path):
        if path is None or len(path) < 1:
            raise ValueError('The config ini file path required')
        else:
            self.conf = configparser.ConfigParser()
            self.conf.read(path)

    def get_mysql_info(self):
        mysql_info = dict(
            host=self.conf.get('MySQL', 'host'),
            port=self.conf.get('MySQL', 'port'),
            user=self.conf.get('MySQL', 'user'),
            password=self.conf.get('MySQL', 'password'),
            database=self.conf.get('MySQL', 'database'),
        )
        return mysql_info
