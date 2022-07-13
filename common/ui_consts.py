#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/29 16:15
@Author  : ZhangTAO
@File    : ui_consts.py
@Software: PyCharm
"""
from common import setting
from common.readConfigIni import Config

"""
接口全局变量
"""
# =============UI自动化环境配置=================


C = Config(setting.CONFIG_INI)

ENVIRONMENT = 'test环境'

BASEHOST = C.basehost_43_13
LOGINHOST = C.loginHost_43_13
LOGININFO: dict = eval(C.loginInfo_43_13)
USERNAME = C.loginusername_43_13
TESTER = C.testers
DELETE_ON_OFF = C.delete_on_off
# print(DELETE_ON_OFF)
SAVE_ON_OFF = C.save_on_off
# print(SAVE_ON_OFF)
EMAIL_ON_OFF = C.send_on_off
# print(EMAIL_ON_OFF)
OPEN_REPORY_ON_OFF = C.open_on_off
# print(OPEN_REPORY_ON_OFF)
DINGDING_NEWS_ON_OFF = C.log_control_on_off
# print(DINGDING_NEWS_ON_OFF)
