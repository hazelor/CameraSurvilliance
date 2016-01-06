#!/usr/bin/env python
# coding=utf-8


__author__ = 'guoxiao'


import mysql.connector
import time
from marcos import *

def create_engine(user, password, database, is_auto_commit=False, host='127.0.0.1', port=3306, **kw):
    params = dict(user=user, password=password, database=database, host=host, port=port)
    defaults = dict(use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=is_auto_commit)
    for k, v in defaults.iteritems():
        params[k] = kw.pop(k, v)
    params.update(kw)
    params['buffered'] = True
    engine = mysql.connector.connect(**params)
    return engine


def create_nowTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def add_caputuredimg(filename,thumbnail_filename):
    conn = create_engine(DB_USER, DB_USER_PASSWORD, DB_NAME, is_auto_commit=True)
    cursor = conn.cursor()
    cursor.execute('insert into %s (image_path, thumbnail_path, date) values (%s, %s, %s)', [DB_IAMGE_TABLE_NAME,filename, thumbnail_filename, create_nowTime()])
    cursor.close()
    conn.close()