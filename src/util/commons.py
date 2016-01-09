__author__ = 'guoxiao'

import os
import socket
import fcntl
import struct
import shutil
from dbtool import db_truncate
from marcos import *

def getPWDDir():
    return os.getcwd()

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
    hd['available'] = disk.f_bsize * disk.f_bavail
    hd['capacity'] = disk.f_bsize * disk.f_blocks
    hd['used'] = disk.f_bsize * disk.f_bfree
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
