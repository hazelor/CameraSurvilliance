#coding=utf-8
__author__ = 'guoxiao'


import logging
import tornado
from tornado.options import options
from base import baseHandler
from util.commons import *
from util import dbtool

class AboutHandler(baseHandler):
    def get(self):
        return self.render('about.html')


class HomeHandler(baseHandler):
    def get(self):
        basic_config_dict = {}
        basic_config_dict['device_name'] = ''
        basic_config_dict['device_id'] = ''
        basic_config_dict['device_type'] = ''
        basic_config_dict['channel_number'] = ''
        basic_config_dict['storage'] = ''
        basic_config_dict['used_storage'] = ''
        get_basic_conf_value(basic_config_dict)
        allitems = dbtool.get_imgs(1, 0)
        total_num = dbtool.get_imgs_count()
        basic_config_dict['img_num'] = total_num
        newest_img = allitems
	if len(allitems)>1:
		newest_img = allitems[0]
	else:
		newest_img = []
        return self.render('home.html',
                           page_name = 'home',
                           basic_config_dict = basic_config_dict,
                           newest_img = newest_img
                           )
