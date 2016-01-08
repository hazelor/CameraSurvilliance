#!/usr/bin/env python
# coding=utf-8

from handler import *
handlers = [
    #about login
    #about main page
    (r"/", HomeHandler),
    #about preview picture page
    (r"/preview",PreviewHandler),
    #about video survilliance page
    (r"/video",VideoHandler),
    #about setting page
    (r"/setting",SettingHandler),
    (r"/setting/(\w+)",SettingHandler),
    # (r"/save_config", SaveConfigHandler),
]

modules = {'monitor':setting_monitorModule}
