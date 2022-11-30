'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:20
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:05:19
FilePath: \pytest_auto_uitest_apitest\common\consts.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-

import os

from common import setting
from common.readConfigYaml import Config

TESTCASEPATH = setting.API_EXCEL_FILE

# 获取Jenkins选项参数(切记参数名称不可以使用中文)
ENVIRONMENT: str = os.environ['ENVIRONMENT']
API_HOST: str = os.environ['APIHOST']
TESTER: str = os.environ['TESTER']

C = Config()
# 登录人名称
# TESTER: str = C.get_testers()[0]
# API_HOST: str = C.get_api_host()[0]
# 如果要切换环境，只需要修改索引下标值
# [op,cp]
# ENVIRONMENT: str = C.get_environment_type()[0]
LOGIN_URL: str = C.get_login_url(ENVIRONMENT)
LOGIN_DATA: dict = C.get_login_data(ENVIRONMENT)
LOGIN_HEADERS: dict = C.get_login_headers(ENVIRONMENT)
LOGIN_USERNAME: str = C.get_login_username(ENVIRONMENT)
