#coding=utf-8
__author__ = 'guoxiao'

import os
import ConfigParser
from Singleton import Singleton
from commons import getPWDDir
from marcos import *

import urllib2
import re

class dev_setting(Singleton):


    def read_dev_conf(self):
        self.dev_dict = {}
        self.dev_conf_path = os.path.join(getPWDDir() ,DEV_CONF_PATH)
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.dev_conf_path)

        #read dev info

        pass

    def get_dev_conf(self):
        return self.dev_dict

    def save_dev_conf(self):
        for key,value in self.dev_dict.items():
            self.cf.set("dev",key,value)
        self.cf.write(open(self.dev_conf_path,"w"))