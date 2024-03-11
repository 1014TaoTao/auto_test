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
# ENVIRONMENT: str = C.get_environment_type()[0]
# API_HOST: str = C.get_api_host()[0]
# TESTER: str = C.get_testers()[0]


LOGIN_URL: str = C.get_login_url(ENVIRONMENT)
LOGIN_DATA: dict = C.get_login_data(ENVIRONMENT)
LOGIN_HEADERS: dict = C.get_login_headers(ENVIRONMENT)
LOGIN_USERNAME: str = C.get_login_username(ENVIRONMENT)
