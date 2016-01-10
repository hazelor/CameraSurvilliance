#!/usr/bin/env python
# coding=utf-8

__author__ = 'guoxiao'

import urllib2
import re
from marcos import *
import subprocess

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

def get_motion_conf_value(kw):
    get_ctrl_url = CTRL_URL %{'ctrl_port':MOTION_CTRL_PORT}
    for k in kw.iterkeys():
        tmp_get_ctrl_url = get_ctrl_url
        tmp_get_ctrl_url += "get?query=" + k
        # print  tmp_get_ctrl_url
        # get_ctrl_url = MOTION_CTRL_PORT +"get?query="+conf_item
        req = urllib2.Request(tmp_get_ctrl_url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        res = re.search(r'(\d+)',res).group()
        # print type(res)
        # print res
        kw[k] = res
    return

def set_motion_conf_value(kw):
    set_ctrl_url = CTRL_URL %{'ctrl_port':MOTION_CTRL_PORT}
    # set_ctrl_url = CTRL_URL %MOTION_CTRL_PORT
    # set_str = str()
    for k, v in kw.iteritems():
        # tmp_set_ctrl_url = str(set_ctrl_url)
        tmp_set_ctrl_url = set_ctrl_url
        tmp_set_ctrl_url += "set?%s=%s"%(k,v)
        # print tmp_set_ctrl_url
        req = urllib2.Request(tmp_set_ctrl_url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        flag = re.search(r'[Dd]one',res).group().lower()

        if flag == 'done':
            pass
        else:
            # print 'here' + k
            return str(RES_FAIL)
    set_ctrl_url += "writeyes"
    # print set_ctrl_url
    req = urllib2.Request(set_ctrl_url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    flag = re.search(r'[Dd]one',res).group().lower()
    if flag == 'done':
        pass
    else:
        # print 'here write'
        return str(RES_FAIL)
        # print  tmp_set_ctrl_url
    # set_ctrl_url += "set?%s"%(set_str)
    # req = urllib2.Request(set_ctrl_url)
    # res_data = urllib2.urlopen(req)
    # res = res_data.read()
    # flag = re.search(r'Done',res).group()
    return str(RES_SUCESS)

def motion_start():
    # subprocess.Popen('sudo -s', shell=True, stdout=subprocess.PIPE)
    # subprocess.Popen(SUDO_PASSWORD, shell=True, stdout=subprocess.PIPE)
    subprocess.Popen(MOTION_START_COMMAND, shell=True, stdout=subprocess.PIPE)



def motion_stop():
    motion_quit_url = MOTION_QUIT_URL %{'ctrl_port':MOTION_CTRL_PORT}
    req = urllib2.Request(motion_quit_url)
    urllib2.urlopen(req)


def motion_restart():
    motion_restart_url = MOTION_RESTART_URL %{'ctrl_port':MOTION_CTRL_PORT}
    req = urllib2.Request(motion_restart_url)
    urllib2.urlopen(req)

def device_reboot():
    subprocess.Popen('sudo reboot', shell=True, stdout=subprocess.PIPE)
