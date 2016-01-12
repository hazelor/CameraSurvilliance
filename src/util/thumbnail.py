#!/usr/bin/env python
# coding=utf-8

from dbtool import add_caputuredimg
from marcos import THUMBNAIL_DIR
from commons import getPWDDir
import os,sys
import Image

__author__ = 'guoxiao'

THUMBNAIL_SIZE = 150

def make_thumbnail(image_filepath):
    filename = image_filepath.split('/')[-1]
    img = Image.open(image_filepath)
    width, height = img.size
    if width > height:
        delta = (width - height) / 2
        box = (delta, 0, width - delta, height)
        region = img.crop(box)
    elif height > width:
        delta = (height - width) / 2
        box = (0, delta, width, height - delta)
        region = img.crop(box)
    else:
        region = img

    thumbnail = region.resize((THUMBNAIL_SIZE, THUMBNAIL_SIZE), Image.ANTIALIAS)
    thumbnail_filename = filename.split('.')[0]+'_tb.jpg'
    thumbnail_filepath = os.path.join(getPWDDir(),THUMBNAIL_DIR)
    if not os.path.isdir(thumbnail_filepath):
        os.makedirs(thumbnail_filepath)
    thumbnail_filepath = os.path.join(thumbnail_filepath,thumbnail_filename)
    thumbnail.save(thumbnail_filepath, quality = 100)
    # mysql operation
    add_caputuredimg(filename,thumbnail_filename, width, height)


if __name__ == '__main__':
    make_thumbnail(sys.argv[1])