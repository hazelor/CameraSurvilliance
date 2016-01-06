__author__ = 'guoxiao'

import os

STATIC_DIR = "/static"

TEMPLATE_DIR = "/template"

IMG_DIR = os.path.join(STATIC_DIR, "/img")

THUMBNAIL_DIR = os.path.join(IMG_DIR, "/thumbnail")

CAPTURED_DIR = os.path.join(IMG_DIR, "/captured")



#about db
DB_USER = 'guoxiao'

DB_USER_PASSWORD = 'guoxiao'

DB_NAME = 'camera_image'

DB_IAMGE_TABLE_NAME = 'image_thumbNail'


#about res

RES_SUCESS = 0
RES_FAIL = 1


#about motion

MOTION_CTRL_PORT = 8080
MOTION_VIDEO_PORT = 8081