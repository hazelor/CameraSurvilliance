#coding=utf-8
__author__ = 'guoxiao'

import tornado
from tornado.options import options
from base import baseHandler
from util.commons import get_ip_address
from util.marcos import *
class VideoHandler(baseHandler):
    def get(self):
        video_url = get_ip_address('eth2')
        video_url = 'http://%s:%s'%(video_url,MOTION_VIDEO_PORT)
        return self.render('video.html',
                           page_name = 'video',
                           video_url = video_url)


