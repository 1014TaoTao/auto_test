# -*- coding: utf-8 -*-#

import os

from tools.random_tool import ContextPack


banner = """
  __    _    _____  ___  _____  ____  __  _____ 
 / /\  | | |  | |  / / \  | |  | |_  ( (`  | |  
/_/--\ \_\_/  |_|  \_\_/  |_|  |_|__ _)_)  |_|  
"""
# ===================公共配置======================
# 项目的根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 项目配置文件
CONFIG_INI = os.path.join(BASE_PATH, "config", "Config.ini")
# 用例所需测试文件路径
CASE_PATH = os.path.join(BASE_PATH, "case")
# log路径
LOG_PATH = os.path.join(BASE_PATH, "logs", ContextPack().get_day_time + '.log')

# 项目测试报告
REPORT_PATH = os.path.join(BASE_PATH, "reports")
# 项目测试报告路径
HTML_REPORT_PATH = os.path.join(
    REPORT_PATH, ContextPack().get_day_time + '.html')

# ===================API配置======================
# api数据路径
API_EXCEL_FILE = os.path.join(CASE_PATH, "api", "test.xlsx")

# ===================UI配置======================
# UI数据文件
UI_YAML_PATH = os.path.join(CASE_PATH, "ui", 'test.yaml')
# UI配置文件路径
UI_IMG_PATH = os.path.join(REPORT_PATH, "img")
# 正常截图文件位置：
UI_OR_IMG_PATH = os.path.join(UI_IMG_PATH, "ordinary")
# 断言截图存放位置
UI_ASS_IMG_PATH = os.path.join(UI_IMG_PATH, "assert")
# 失败截图存放位置
UI_FAIL_IMG_PATH = os.path.join(UI_IMG_PATH, "fail")
# driver驱动路径
DRIVER = os.path.join(BASE_PATH, "driver", "chromedriver.exe")

# ===================PRE配置======================
# per数据文件
PER_YAML_PATH = os.path.join(CASE_PATH, "per", 'test.yaml')
# per配置文件路径
LOCUST_CONFIG_PATH = os.path.join(BASE_PATH, "locust.conf")
