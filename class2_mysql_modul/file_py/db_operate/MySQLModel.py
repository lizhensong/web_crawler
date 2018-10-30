#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li'

from class2_mysql_modul.file_py.db_operate.MySQLOperateMetaClass import ModelMetaclass
from class2_mysql_modul.file_py.db_operate.MySQLOperateBasic import select_table
from class2_mysql_modul.file_py.db_operate.MySQLOperateBasic import update_table


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def find(self, args=None, where=None, order=None, size=None):
        sql = ["select (%s) from %s"]
        args = str(args)
        if args is None:
            args = '*'
        args = [args].append(self.__table__)
        if where:
            sql.append('where')
            sql.append(where)
        if order:
            sql.append('order by')
            sql.append(order)
        return select_table(' '.join(sql), args, size)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)'
        args_all = list()
        args_all.append(self.__table__)
        args_all.append(','.join(fields))
        args_all.append(','.join([str(i) for i in args]))
        rows = update_table(sql, args_all)
        if rows != 1:
            print('failed to insert record: affected rows: %s'.format(rows))
