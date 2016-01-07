#coding=utf-8
__author__ = 'guoxiao'

import tornado
from tornado.options import options
from base import baseHandler

class SettingHandler(baseHandler):
    def get(self,input = 'basic'):
        if input:
            sub_page_name = input
        else:
            sub_page_name = 'basic'

        return self.render('setting.html',
                           page_name = 'settings',
                           sub_page_name = sub_page_name)


