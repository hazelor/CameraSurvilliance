#!/usr/bin/env python
# coding=utf-8

import os
import sys
import tornado.web
import tornado.ioloop
from handler import *
import tornado.options
from tornado.options import define,options
tornado.options.parse_command_line()

import routes

def create_app():
    settings = {
        'static_path':'src/static',
        'template_path':'src/template',
        'xsrf_cookies':False,
    }
    return tornado.web.Application(routes)

if __name__ == "__main__":
    app = create_app()
    app.listen(options.port)