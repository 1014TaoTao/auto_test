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
HTML_REPORT_PATH = os.path.join(REPORT_PATH, ContextPack().get_day_time + '.html')

# ===================API配置======================
# api数据路径
API_EXCEL_FILE = os.path.join(CASE_PATH, "api", "case.xlsx")
API_YAML_PATH = os.path.join(CASE_PATH, "api", 'case.yaml')

# ===================UI配置======================
# UI数据文件
UI_YAML_PATH = os.path.join(CASE_PATH, "ui", 'case.yaml')
# UI截图路径
UI_IMG_PATH = os.path.join(REPORT_PATH, "img")


