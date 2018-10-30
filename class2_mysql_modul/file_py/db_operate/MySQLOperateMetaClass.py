#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li'

from class2_mysql_modul.file_py.db_operate.MySQLdbORM import Field


class ModelMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        table_name = attrs.get('__table__') or name
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        # 表名
        attrs['__table__'] = table_name
        return type.__new__(mcs, name, bases, attrs)
