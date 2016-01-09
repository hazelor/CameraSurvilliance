#coding=utf-8
__author__ = 'guoxiao'

import tornado,tornado.web
import re
import os
from tornado.options import options
from util import dbtool
from util.marcos import *
from util.motion import *
from util.commons import *
from base import baseHandler
from util import zip_tool
import time
# import subprocess

class PreviewHandler(baseHandler):
    def get(self):
        current_page = self.get_argument('page','')
        if current_page:
            current_page = int(current_page)
        else:
            current_page = 1

        total_num = dbtool.get_imgs_count()
        page_num = total_num/PAGE_NUMBER+1
        start_num = (current_page-1)*PAGE_NUMBER+1

        if page_num<current_page:
            current_page = page_num

        allitems = dbtool.get_imgs(PAGE_NUMBER, (current_page-1)*PAGE_NUMBER)

        #get the start and end page num
        if current_page>3:
            start_page_num = current_page-3
        else:
            start_page_num = 1

        end_page_num = start_page_num+6
        if end_page_num>page_num:
            end_page_num = page_num
            start_page_num = end_page_num-6
            if start_page_num<1:
                start_page_num = 1

        end_num  = start_num+len(allitems)-1



        #get tb_rows

        return self.render('preview.html',
                           page_name  = 'preview',
                           current_page = current_page,
                           page_num = page_num,
                           total_num = total_num,
                           start_num = start_num,
                           end_num = end_num,
                           start_page_num = start_page_num,
                           end_page_num = end_page_num,
                           allitems = allitems)

class DownloadHandler(baseHandler):
    def get(self):
        #  stop motion service
        motion_stop()
        time.sleep(2)
        # zip  operation
        folder_name = os.path.join(getPWDDir(),CAPTURED_DIR)
        # print folder_name
        zip_file_name = dbtool.create_nowTime_strip()+'.zip'
        zip_dir = os.path.join(getPWDDir(),DOWNLOAD_DIR, zip_file_name)
        # print zip_dir
        zip_tool.zip_images(folder_name, zip_dir)
        # start motion service
        motion_start()
        # self.write('test.rar')
        self.write(zip_file_name)




class thumbnailModule(tornado.web.UIModule):
    def render(self, tb):
        return self.render_string('thumbnail.html',tb=tb)
