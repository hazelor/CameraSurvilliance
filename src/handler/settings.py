#coding=utf-8
__author__ = 'guoxiao'

import tornado
from tornado.options import options
from base import baseHandler
from util.motion import *
from util.commons import *
import time
# from util.conf import *
# import shutil
from util.marcos import *
import time

class SettingHandler(baseHandler):
    def get(self,input = 'basic'):
        if input:
            sub_page_name = input
        else:
            sub_page_name = 'basic'


        if sub_page_name == 'basic':
            return self.render_basic()
        if sub_page_name == 'monitor':
            return self.render_monitor()
        if sub_page_name == 'reboot':
            device_reboot()
            return
        if sub_page_name == 'time_synchronize':
            time = self.get_argument('time')
            set_device_time(time)
            return
        if sub_page_name == 'save_basic_config':
            # print 'here'
            return self.save_basic_config()
        if sub_page_name == 'save_monitor_config':
            return self.save_monitor_config()
        if sub_page_name == 'clear':
            return self.clear_data()
        return self.send_error(404)

    def post(self):
        pass
    def render_basic(self):

        return self.render('setting.html',
                           page_name = 'settings',
                           sub_page_name = 'basic')


    def render_monitor(self):
        return self.render('setting.html',
                           page_name = 'settings',
                           sub_page_name = 'monitor')

    def save_basic_config(self):
        config_dict = {}
        if self.get_argument('type') == 'device_info':
            config_dict['device_name'] = self.get_argument('device_name')
            config_dict['device_id'] = self.get_argument('device_id')
            set_basic_conf_value(config_dict)
        return


    def save_monitor_config(self):
        config_dict = dict()
        if self.get_argument('type') == 'video':
            resolution = str(self.get_argument('resolution'))
            config_dict['width'],config_dict['height'] = resolution.split(',')[0],resolution.split(',')[1]
            # print resolution+'\n'
            # print type(resolution)
            frame_rate = self.get_argument('framerate')
            config_dict['framerate'] = frame_rate
            # print frame_rate+'\n'
            rotate = self.get_argument('rotate')
            config_dict['rotate'] = rotate
            # print rotate+'\n'
            brightness = self.get_argument('brightness')
            config_dict['brightness'] = brightness
            # print brightness+'\n'
            contrast = self.get_argument('contrast')
            config_dict['contrast'] = contrast
            # print contrast+'\n'
            saturation = self.get_argument('saturation')
            config_dict['saturation'] = saturation
            # print saturation+'\n'
        else:
            config_dict['snapshot_interval'] = str(int(self.get_argument('snapshot_interval'))*60*60)
            # print  config_dict['snapshot_interval']

        # is_success = set_motion_conf_value(config_dict)
        set_motion_conf_value(config_dict)
        motion_restart()
        time.sleep(8)
        # return self.write(is_success)

    def clear_data(self):
        # time.sleep(10)
        clear_data()


class RebootHandler(baseHandler):
    def get(self):
        device_reboot()


# class ClearHandler(baseHandler):
#     def get(self):
#         clear_data()
#         return

class SaveBasicConfigHandler(baseHandler):
    def get(self):
        config_dict = {}
        if self.get_argument('type') == 'device_info':
            config_dict['device_name'] = self.get_argument('device_name')
            config_dict['device_id'] = self.get_argument('device_id')
            set_basic_conf_value(config_dict)
        return

class DeviceTimeHandler(baseHandler):
    @tornado.web.asynchronous
    def get(self):
        device_time =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.write(device_time)
        self.finish()
        # self.get_data(callback=self.on_finish)
    # def get_data(self, callback):
    #     if self.request.connection.stream.closed():
    #         return
    #     device_time =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    #     callback(device_time)
    # def on_finish(self, data):


class TimeSynchronizeHandler(baseHandler):
    def get(self):
        time = self.get_argument('time')
        set_device_time(time)



class setting_monitorModule(tornado.web.UIModule):
    def render(self):
        return self.render_string("setting_monitor.html")
    def embedded_javascript(self):
        monitor_config_dict = dict()
        monitor_config_dict['width'] = ''
        monitor_config_dict['height'] = ''
        monitor_config_dict['framerate'] = ''
        monitor_config_dict['rotate'] = ''
        monitor_config_dict['brightness'] = ''
        monitor_config_dict['contrast'] = ''
        monitor_config_dict['saturation'] = ''
        monitor_config_dict['snapshot_interval'] = ''
        res = get_motion_conf_value(monitor_config_dict)
        if res == RES_SUCESS:
            # print config_dict['snapshot_interval']
            return self.render_string("setting_monitor.js",width=monitor_config_dict['width'], height=monitor_config_dict['height'], framerate=monitor_config_dict['framerate'],
                                  rotate=monitor_config_dict['rotate'], brightness=monitor_config_dict['brightness'], contrast=monitor_config_dict['contrast'],
                                  saturation=monitor_config_dict['saturation'], snapshot_interval=str(int(monitor_config_dict['snapshot_interval'])/60/60))
        else:
            return self.render_string("setting_monitor.js",width="", height="", framerate="",
                                  rotate="", brightness="", contrast="",
                                  saturation="", snapshot_interval="")

class setting_basicModule(tornado.web.UIModule):
    def render(self):
        return self.render_string("setting_basic.html")
    def embedded_javascript(self):
        basic_config_dict = {}
        basic_config_dict['device_name'] = ''
        basic_config_dict['device_id'] = ''
        basic_config_dict['device_type'] = ''
        basic_config_dict['channel_number'] = ''
        basic_config_dict['storage'] = ''
        basic_config_dict['used_storage'] = ''
        get_basic_conf_value(basic_config_dict)
        basic_config_dict['storage'] =basic_config_dict['storage']+'GB'
        return self.render_string("setting_basic.js", device_name=basic_config_dict['device_name'],
                                  device_id=basic_config_dict['device_id'], device_type=basic_config_dict['device_type'],
                                  channel_number=basic_config_dict['channel_number'], storage=basic_config_dict['storage'], )
