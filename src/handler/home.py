#coding=utf-8
__author__ = 'guoxiao'


import logging
import tornado
from tornado.options import options
from base import baseHandler

class AboutHandler(baseHandler):
    def get(self):
        return self.render('about.html')


class HomeHandler(baseHandler):
    def get(self):

        return self.render('home.html',
                           page_name = 'home'
                           )