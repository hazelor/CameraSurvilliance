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
    (r"/download", DownloadHandler),
    (r"/reboot", RebootHandler),
    # (r"/setting/clear", ClearHandler)
    (r"/save_basic_config", SaveBasicConfigHandler),
    (r"/device_time", DeviceTimeHandler),
    (r"/time_synchronize", TimeSynchronizeHandler),
]

modules = {'monitor':setting_monitorModule,
           'basic':setting_basicModule,}
