__author__ = 'guoxiao'

import os
import socket
import fcntl
import struct
import shutil
from dbtool import db_truncate
from marcos import *
import ConfigParser
# import statvfs

def getPWDDir():
    return os.getcwd()

# def getUPPERDir():
#     return os.path.dirname(os.getcwd())

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def disk_stat():
    hd={}
    disk = os.statvfs("/")
    hd['available'] = (disk.f_bsize * disk.f_bavail)/(1024*1024*1024)
    hd['capacity'] = (disk.f_bsize * disk.f_blocks)/(1024*1024*1024)
    hd['used'] = hd['capacity']-hd['available']
    return hd

def clear_data():
    pwd = getPWDDir()
    captured_dir = os.path.join(pwd, CAPTURED_DIR)
    thunmbnail_dir = os.path.join(pwd, THUMBNAIL_DIR)
    download_dir = os.path.join(pwd, DOWNLOAD_DIR)
    if os.path.isdir(download_dir):
        shutil.rmtree(download_dir)
    if os.path.isdir(thunmbnail_dir):
        shutil.rmtree(thunmbnail_dir)
    if os.path.isdir(captured_dir):
        shutil.rmtree(captured_dir)
    db_truncate()


def get_basic_conf_value(kw):
    # conf_dir = os.path.join(getPWDDir(), '/conf/device_conf.ini')
    conf_dir = getPWDDir() + '/conf/device_conf.ini'
    # print conf_dir
    read_conf(conf_dir, kw)
    kw['storage'] = str(disk_stat()['available'])
    kw['used_storage'] = str(disk_stat()['used'])
    # return

def set_basic_conf_value(kw):
    conf_dir = getPWDDir() + '/conf/device_conf.ini'
    # print conf_dir
    write_conf(conf_dir, kw)
    # kw['storage'] = str(disk_stat()['available'])

def read_conf(conf_dir, kw):
    config = ConfigParser.ConfigParser()
    config.read(conf_dir)
    kw['device_name'] = config.get('conf', 'device_name')
    kw['device_id'] = config.get('conf', 'device_id')
    kw['device_type'] = config.get('conf', 'device_type')
    kw['channel_number'] = config.get('conf', 'channel_number')

def write_conf(conf_dir, kw):
    config = ConfigParser.ConfigParser()
    # print conf_dir
    config.read(conf_dir)
    fp = open(conf_dir, 'w')
    # print kw['device_name']
    # print kw['device_id']
    config.set('conf', 'device_name', kw['device_name'])
    config.set('conf', 'device_id', kw['device_id'])
    # device_type = config.get('conf', 'device_type')
    # channel_number = config.get('conf', 'channel_number')
    config.write(fp)
    fp.close()

def set_device_time(time_str):
    command = "sudo date -s "+"\""+time_str+"\""
    # print command
    os.system(command)
