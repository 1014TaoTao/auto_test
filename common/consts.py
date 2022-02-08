# -*- coding: utf-8 -*-

from common.readConfigYaml import Config

C = Config()

# 接口响应时间list，单位毫秒
STRESS_LIST = []

# 接口执行结果list
RESULT_LIST = []

# 选择执行环境:['environment_195', 'environment_115', 'environment_120', 'environment_43_13']
# 如果要切换环境，只需要修改索引下标值
ENVIRONMENT = C.get_environment()[1]
# print(ENVIRONMENT)
APIHOST = C.get_apihoet(ENVIRONMENT)
BASEHOST = C.get_basehost(ENVIRONMENT)
LOGINHOST = C.get_loginHost(ENVIRONMENT)
USERNAME = C.get_login_username(ENVIRONMENT)[0]  # 登录时会通过username作为断言，不然就将登录失败
LOGINDATA = C.get_login_info(ENVIRONMENT).get('zhangtao')  # 不同的测试人员需要修改对应得data的key

# 登录人名称
TESTER = C.get_testers()[0]
# print(TESTER)

"""
接口全局变量
[0]为开启
[1]为关闭
"""
# 是否开启删除历史报告功能,字符串列表转换eval
DELETE_ON_OFF = C.get_delete_report_on_off()[1]
# 是否开启生成报告功能
SAVE_ON_OFF = C.get_run_report_on_off()[0]
# 是否开启压缩报告功能
ZIP_ON_OFF = C.get_zip__report_on_off()[1]
# 是否开启发送邮件功能
EMAIL_ON_OFF = C.get_send_email_on_off()[1]
# 运行结束是否直接打开报告
OPEN_REPORY_ON_OFF = C.get_open_report_on_off()[1]
# 控制台输出日志
LOG_CONTROL_ON_OFF = C.get_log_control_on_off()[0]
# 发送钉钉
DINGDING_NEWS_ON_OFF = C.get_send_dingding_news_on_off()[0]
