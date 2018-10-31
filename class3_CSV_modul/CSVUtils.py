#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li.csv'

# CSV文件操作工具

import csv


# 将数据写入CSV文件,head传入list，data传入list包list，每个list一行
def write_csv_file_list(path, head=None, data=None):
    try:
        # 如果不指定newline='',则每写入一行将有一空行被写入
        with open(path, 'w', newline='', encoding='utf-8')as csv_file:
            writer = csv.writer(csv_file)
            if head is not None:
                writer.writerow(head)
            if data is not None:
                # 多行
                # writer.writerows(data)
                # 单行
                for row in data:
                    writer.writerow(row)
        print('Write a CSV file to path-->{} is Successful'.format(path))
    except Exception as e:
        print(e)


# 将数据从CSV文件读出****read读取只能遍历一次，遍历后它里边的属性就没了。
def read_csv_file_list(path):
    try:
        with open(path)as csv_file:
            reader = csv.reader(csv_file, encoding='utf-8')
            print('Read from a CSV file in path-->{} is Successful'.format(path))
            # 获取每一行和行号
            # for row in reader:
            #     # 行号从1开始
            #     print(reader.line_num, row)
            # list(reader)是一个list包list集。
            print(list(reader))
            return list(reader)
    except Exception as e:
        print(e)


# 将数据写入CSV文件,head传入list(list中是data数据中dict的key，将写在第一行)，
# data传入list包dict，每个dict一行，会自动去除key。
def write_csv_file_dict(path, head=None, data=None):
    try:
        with open(path, 'w', newline='', encoding='utf-8')as csv_file:
            writer = csv.DictWriter(csv_file, head)
            writer.writeheader()
            if data is not None:
                # writer.writerows(data)
                for row in data:
                    writer.writerow(row)
        print('Write a CSV file to path-->{} is Successful'.format(path))
    except Exception as e:
        print(e)


# 使用DictReader可以像操作字典那样获取数据，把表的第一行（一般是标头）作为key。
# 可访问每一行中那个某个key对应的数据。
def read_csv_file_dict(path):
    try:
        with open(path)as csv_file:
            reader = csv.DictReader(csv_file, encoding='utf-8')
            print('Read from a CSV file in path-->{} is Successful'.format(path))
            # 获取每一行和行号
            # for row in reader:
            #     # 行号从1开始
            #     print(reader.line_num, row)
            # list(reader)是一个list包list集。
            print(list(reader))
            return list(reader)
    except Exception as e:
        print(e)
