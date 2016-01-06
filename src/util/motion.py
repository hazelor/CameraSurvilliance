#!/usr/bin/env python
# coding=utf-8

__author__ = 'guoxiao'

import urllib2
import re
from marcos import *

def set_snapshot_interval(interval):
    url = "http://127.0.0.1:8080/0/config/set?snapshot_interval=" + interval
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    flag = re.search(r'Done',res.read()).group()
    if flag == 'Done':
        return RES_SUCESS
    else:
        return RES_FAIL


def get_snapshot_interval():
    url = "http://127.0.0.1:%s/0/config/get?query=snapshot_interval",[MOTION_CTRL_PORT]
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    interval = re.search(r'\d+',res).group()
    return interval