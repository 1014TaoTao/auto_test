# -*- coding: utf-8 -*-
import os

from common import setting
from common.readConfigYaml import Config



TESTCASEPATH = setting.API_EXCEL_FILE

C = Config()


# 选择执行环境:['environment_195', 'environment_115', 'environment_120', 'environment_43_13']
# 如果要切换环境，只需要修改索引下标值
ENVIRONMENT: str = C.get_environment()[1]
# ENVIRONMENT: str = os.environ['']

APIHOST: str = C.get_apihoet(ENVIRONMENT)

APIHOSTPORT: str = C.get_environment_port(ENVIRONMENT)[7]
BASEHOST: str = C.get_basehost(ENVIRONMENT)
LOGINHOST: str = C.get_loginHost(ENVIRONMENT)

LOGINUSER: str = C.get_login_user_title(ENVIRONMENT)[0]
USERNAME: str = C.get_login_username(ENVIRONMENT, LOGINUSER)
LOGINDATA: dict = C.get_login_data(ENVIRONMENT, LOGINUSER)  # 不同的测试人员需要修改对应得data的key

# 登录人名称
TESTER: str = C.get_testers()[0]

# 接口响应时间list，单位毫秒
STRESS_LIST = []
# 接口执行结果list
RESULT_LIST = []

# if __name__ == '__main__':
# print('TESTCASEPATH', (TESTCASEPATH))
# print('ENVIRONMENT', (ENVIRONMENT))
# print('LOGINUSER', LOGINUSER)
# print('APIHOSTPORT', APIHOSTPORT)
# print('APIHOST', (APIHOST))
# print('BASEHOST', (BASEHOST))
# print('LOGINHOST', (LOGINHOST))
# print('USERNAME', (USERNAME))
# print('LOGINDATA', (LOGINDATA))
# print('TESTER', TESTER)
#
# print(DELETE_ON_OFF)
# print(SAVE_ON_OFF)
# print(EMAIL_ON_OFF)
# print(OPEN_REPORY_ON_OFF)
# print(DINGDING_NEWS_ON_OFF)
