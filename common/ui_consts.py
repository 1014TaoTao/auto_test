#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/29 16:15
@Author  : ZhangTAO
@File    : ui_consts.py
@Software: PyCharm
"""
from common.readConfigIni import Config
from common import setting

"""
接口全局变量
[0]为开启
[1]为关闭
"""
# =============UI自动化环境配置=================


C = Config(setting.CONFIG_INI)

ENVIRONMENT = 'test环境'
TESTER = C.testers
DELETE_ON_OFF = C.delete_on_off
SAVE_ON_OFF = C.save_on_off
EMAIL_ON_OFF = C.send_on_off
OPEN_REPORY_ON_OFF = C.open_on_off
DINGDING_NEWS_ON_OFF = C.log_control_on_off