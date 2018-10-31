#!usr\bin\python3
# -*- encoding: UTF-8 -*-

__author__ = 'Wolf li.csv'

from class2_mysql_modul.file_py.db_connect import MySQLConnect


def select_table(sql, args, size=None):
    try:
        db = MySQLConnect.connect_pool()
        cur = db.cursor()
        cur.execute(sql, args)
        if size:
            rs = cur.fetchmany(size)
        else:
            rs = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if db:
            db.close()
    return rs


def update_table(sql, args):
    try:
        db = MySQLConnect.connect_pool()
        cur = db.cursor()
        cur.execute(sql, args)
        affected_rowcount = cur.rowcount
        db.commit()
    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if db:
            db.close()
    return affected_rowcount
