__author__ = 'guoxiao'

import os

STATIC_DIR = "/static"

TEMPLATE_DIR = "/template"

IMG_DIR = "static/img"

THUMBNAIL_DIR = "static/img/thumbnail"

CAPTURED_DIR = "static/img/captured"

DEV_CONF_PATH = "conf/dev.conf"

DOWNLOAD_DIR = "static/download"

#about db
DB_USER = 'root'

DB_USER_PASSWORD = ''

DB_NAME = 'camera_image'

DB_IAMGE_TABLE_NAME = 'image_thumbNail'


#about res

RES_SUCESS = 0
RES_FAIL = 1

#about img page
PAGE_NUMBER = 16
#about motion

CTRL_URL = r'http://localhost:%(ctrl_port)s/0/config/'
MOTION_RESTART_URL = r'http://localhost:%(ctrl_port)s/0/action/restart'
MOTION_QUIT_URL = R'http://localhost:%(ctrl_port)s/0/action/quit'

MOTION_CTRL_PORT = 8080
MOTION_VIDEO_PORT = 8081
MOTION_START_COMMAND = 'motion'


WIDTH_CONF = 'width'
HEIGHT_CONF = 'height'
ROTATE_CONF = 'rotate'
SNAPSHORT_INTERVAL_CONF = 'snapshot_interval'
BRIGHTNESS_CONF = 'brightness'
CONTRAST_CONF = 'contrast'
SATURATION_CONF = 'saturation'
HUE_CONF = 'hue'
