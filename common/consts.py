# -*- coding: utf-8 -*-

from tools.api_tool_read_pyqt_txt import read_pyqt5_txt

all_data = read_pyqt5_txt()
# print(all_data)
TESTCASEPATH = all_data.get('testcase_path')
ENVIRONMENT = all_data.get('emvironment')
LOGINUSER = all_data.get('login_user')
APIHOST = all_data.get('api_host')
BASEHOST = all_data.get('base_host')
LOGINHOST = all_data.get('login_host')
USERNAME = all_data.get('login_usernaem')
LOGINDATA = all_data.get('login_data')
TESTER = all_data.get('tester')

# print(TESTCASEPATH)
# print(ENVIRONMENT)
# print(LOGINUSER)
# print(APIHOST)
# print(BASEHOST)
# print(LOGINHOST)
# print(USERNAME)
# print(LOGINDATA)



# # 接口响应时间list，单位毫秒
# from common.readConfigYaml import Config
#
STRESS_LIST = []

# 接口执行结果list
RESULT_LIST = []
#
# C = Config()
# # 选择执行环境:['environment_195', 'environment_115', 'environment_120', 'environment_43_13']
# # 如果要切换环境，只需要修改索引下标值
# ENVIRONMENT = C.get_environment()[1]
# APIHOST = C.get_apihoet(ENVIRONMENT)
# BASEHOST = C.get_basehost(ENVIRONMENT)
# LOGINHOST = C.get_loginHost(ENVIRONMENT)
# USERNAME = C.get_login_username(ENVIRONMENT, 'zhangtao115')
# LOGINDATA = C.get_login_data(ENVIRONMENT, 'zhangtao115')  # 不同的测试人员需要修改对应得data的key
#
# """
# 接口全局变量
# [0]为开启
# [1]为关闭
# """
# # 登录人名称
# TESTER = C.get_testers()[0]
# # 控制台输出日志
# LOG_CONTROL_ON_OFF = C.get_log_control_on_off()[0]
