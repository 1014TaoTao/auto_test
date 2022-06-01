# -*- coding: utf-8 -*-#
import glob
import os

# ===================公共配置======================
# 项目的根目录-
# \pytest_auto_uitest_apitest
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if not os.path.exists(BAT_FILE):
#     raise FileNotFoundError("请确保pytest_auto_uitest_ap文件存在！")

# 项目配置文件
CONFIG_YAML = os.path.join(BASE_PATH, "config", "Config.yaml")
CONFIG_INI = os.path.join(BASE_PATH, "config", "Config.ini")

# 上传文件路径
upload_file = os.path.join(BASE_PATH, "data")

# 项目数据文件路径
DATA_PATH = os.path.join(BASE_PATH, "case")

# ===================API配置======================

# log路径
API_LOG_PATH = os.path.join(BASE_PATH, "logs", "api_logs")

# api数据路径
TEST_CASE_LIST = glob.glob(f"{DATA_PATH}/api/excel_data/*.xls")
API_EXCEL_FILE = os.path.join(DATA_PATH, "api", "excel_data", "kube.xls")
sheet_id = 0
API_SQL_FILE = os.path.join(DATA_PATH, "api", 'sql_data', 'test.sql')
API_YAML_PATH = os.path.join(DATA_PATH, "api", 'yaml_data', 'test.yaml')

# 项目测试报告
API_REPORT_PATH = os.path.join(BASE_PATH, "report", "api_report")

# api项目测试报告
API_REPORT_RESULT_PATH = os.path.join(API_REPORT_PATH, "allure_result")
API_REPORT_END_PATH = os.path.join(API_REPORT_PATH, "allure_report")
html_reposrt_path = os.path.join(API_REPORT_END_PATH, 'index.html')
API_REPORT_HISTORY_PATH = os.path.join(API_REPORT_PATH, "allure_report", "history")
API_RESULT_HISTORY_PATH = os.path.join(API_REPORT_PATH, "allure_result", "history")

# api项目压缩文件路径
API_FILE_LIST_PATH = os.path.join(API_REPORT_PATH, "API_report.zip")  # 要压缩文件名称
API_REPORT_DIR = os.path.join(API_REPORT_PATH, "report", "allure_report")  # 要压缩文件路径
API_FILE_LIST = [os.path.join(API_REPORT_PATH, "API_report.zip")]  # 邮件附件列表，格式为列表

# allure环境配置信息
API_StartEnvironmentFilePath = os.path.join(BASE_PATH, "report", "environment.properties")
API_StartEnvironmentFileXMLPath = os.path.join(BASE_PATH, "report", "environment.xml")
API_StartExcutorJson = os.path.join(BASE_PATH, "report", "executor.json")

# allure环境信息复制位置
API_EndEnvironmentXMLFile = os.path.join(API_REPORT_PATH, "allure_result", "environment.xml")
API_EndEnvironmentFile = os.path.join(API_REPORT_PATH, "allure_result", "environment.properties")
API_EndExcutorJson = os.path.join(API_REPORT_PATH, "allure_result", "executor.json")

# token存放位置
TOKEN_FILE = os.path.join(DATA_PATH, "api", "token.txt")

# pyqt5生成的执行环境信息存放位置
PYQT5_FILE = os.path.join(DATA_PATH, "api", "pyqt5.txt")

# allure执行结果信息存放位置
PROMETHEUSDATA = os.path.join(API_REPORT_END_PATH, "export", "prometheusData.txt")

# ===================UI配置======================
# 日志地址
UI_LOG_PATH = os.path.join(BASE_PATH, "logs", "ui_logs")

# UI数据文件
UI_EXCEL_FILE = os.path.join(DATA_PATH, "ui", "excel_data", "test.xls")
UI_SQL_FILE = os.path.join(DATA_PATH, "ui", 'sql_data', 'test.sql')
UI_YAML_DIR = os.path.join(DATA_PATH, "ui", 'yaml_data')
UI_YAML_PATH = os.path.join(DATA_PATH, "ui", 'yaml_data', 'test.yaml')

# ui测试报告路径
UI_REPORT_PATH = os.path.join(BASE_PATH, "report", "ui_report")

UI_REPORT_RESULT_PATH = os.path.join(UI_REPORT_PATH, "allure_result")
UI_REPORT_END_PATH = os.path.join(UI_REPORT_PATH, "allure_report")

UI_REPORT_HISTORY_PATH = os.path.join(UI_REPORT_PATH, "allure_report", "history")
UI_RESULT_HISTORY_PATH = os.path.join(UI_REPORT_PATH, "allure_result", "history")

UI_FILE_LIST_PATH = os.path.join(UI_REPORT_PATH, "UI_report.zip")  # 要压缩文件名称
UI_REPORT_DIR = os.path.join(UI_REPORT_PATH, "report", "allure_report")  # 要压缩文件路径

UI_FILE_LIST = [os.path.join(UI_REPORT_PATH, "UI_report.zip")]  # 邮件附件列表，格式为列表

UI_StartEnvironmentFilePath = os.path.join(BASE_PATH, "report", "environment.properties")
UI_StartEnvironmentFileXMLPath = os.path.join(BASE_PATH, "report", "environment.xml")
UI_StartExcutorJson = os.path.join(BASE_PATH, "report", "executor.json")

UI_EndEnvironmentFile = os.path.join(UI_REPORT_PATH, "allure_result", "environment.properties")
UI_EndEnvironmentXMLFile = os.path.join(UI_REPORT_PATH, "allure_result", "environment.xml")
UI_EndExcutorJson = os.path.join(UI_REPORT_PATH, "allure_result", "executor.json")

UI_IMG_PATH = os.path.join(UI_REPORT_PATH, "img")
# 正常截图文件位置：
UI_OR_IMG_PATH = os.path.join(UI_IMG_PATH, "ordinary")
# 断言截图存放位置
UI_ASS_IMG_PATH = os.path.join(UI_IMG_PATH, "assert")
# 失败截图存放位置
UI_FAIL_IMG_PATH = os.path.join(UI_IMG_PATH, "fail")
# driver驱动路径
DRIVER = os.path.join(BASE_PATH, "driver", "chromedriver.exe")
BROWSER = "Chrome"
chrome_app = r"C:\Program Files\Google\Chrome\Application"  # 需要修改
chrome_reg = r"SOFTWARE\Google\Chrome\BLBeacon"  # win chrome注册表地址


# ===================PRE配置======================
# 日志地址
PER_LOG_PATH = os.path.join(BASE_PATH, "logs", "prf_logs")

# per数据文件
PER_YAML_PATH = os.path.join(DATA_PATH, "prf", 'yaml_data', 'test.yaml')

# per配置文件路径
PER_CONFIG_PATH = os.path.join(BASE_PATH, "locust.conf")


# ===================public配置======================
jenkins_url = "http://250.25.250.250:9000/"
reprot_url = "http://localhost:63342/pytest_auto_uitest_apitest/report/api_report/allure_report/index.html"
at_mobiles_list = [15382112620]