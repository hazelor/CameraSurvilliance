#coding=utf-8
__author__ = 'guoxiao'

import zipfile
import os
# from marcos import *

def zip_images(folder_name, zip_dir):
    path, filename = os.path.split(zip_dir)
    if not os.path.isdir(path):
        os.makedirs(path)
    z = zipfile.ZipFile(zip_dir, 'w')
    if os.path.isdir(folder_name):
        for d in os.listdir(folder_name):
            z.write(folder_name+os.sep+d, d)
            # z.write(d)
    z.close()