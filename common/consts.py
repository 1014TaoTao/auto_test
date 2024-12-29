# -*- coding: utf-8 -*-

# 获取Jenkins选项参数(切记参数名称不可以使用中文)
# import os
# TEST_TYPE = os.environ['TESTTYPE']
# ENVIRONMENT: str = os.environ['ENVIRONMENT']
# API_HOST: str = os.environ['APIHOST']
# TESTER: str = os.environ['TESTER']

from tools import ini_tool
from config import setting

CONFIG = ini_tool.Config(setting.CONFIG_INI)

# 登录人名称
TEST_TYPE = CONFIG.get_config("environment", "type")
ENVIRONMENT = CONFIG.get_config("environment", "name")
API_HOST = CONFIG.get_config("environment", "host")
TOKEN = CONFIG.get_config("environment", "token")

TESTER = CONFIG.get_config("testers", "tester")

DELETE_ON_OFF = CONFIG.get_config('common', 'delete_on_off')
EMAIL_ON_OFF = CONFIG.get_config('common', 'email_on_off')
DINGDING_ON_OFF = CONFIG.get_config('common', 'dingding_on_off')
REPORT_URL = CONFIG.get_config("common", "report_url")
JENKINS_URL = CONFIG.get_config("common", "jenkins_url")

DINGDING_SECRET = CONFIG.get_config("dingding", "secret")
DINGDING_WEBHOOK = CONFIG.get_config("dingding", "webhook")
DINGDING_AT_MOBILES = CONFIG.get_config("dingding", "at_mobiles")

EMAIL_FROMADDR = CONFIG.get_config('email', 'sender')
EMAIL_PASSWORD = CONFIG.get_config('email', 'password')
EMAIL_TOADDRS = CONFIG.get_config('email', 'receiver')
EMAIL_SERVER_HOST = CONFIG.get_config('email', 'smtp_server')

BROWSER = CONFIG.get_config("browser", "type")

MYSQL_HOST = CONFIG.get_config("mysql", "host")
MYSQL_PORT = CONFIG.get_config("mysql", "port")
MYSQL_USER = CONFIG.get_config("mysql", "user")
MYSQL_PASSWORD = CONFIG.get_config("mysql", "password")
MYSQL_DB = CONFIG.get_config("mysql", "db")
MYSQL_CHARSET = CONFIG.get_config("mysql", "charset")

REDIS_HOST = CONFIG.get_config("redis", "host")
REDIS_PORT = CONFIG.get_config("redis", "port")
