# -*- coding: utf-8 -*-#
import glob
import os

# ------------------ 项目的根目录 -----------------------
# \pytest_auto_uitest_apitest
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if not os.path.exists(BAT_FILE):
#     raise FileNotFoundError("请确保pytest_auto_uitest_ap文件存在！")

# ------------------ log ----------------------------
API_LOG_PATH = os.path.join(BASE_PATH, "logs", "api_logs")
UI_LOG_PATH = os.path.join(BASE_PATH, "logs", "ui_logs")
PRF_LOG_PATH = os.path.join(BASE_PATH, "logs", "prf_logs")

# ------------------ 项目配置文件 -----------------------
CONFIG_INI = os.path.join(BASE_PATH, "config", "Config.ini")
CONFIG_YAML = os.path.join(BASE_PATH, "config", "Config.yaml")

# ------------------ 项目数据文件 -----------------------
DATA_PATH = os.path.join(BASE_PATH, "case")
TEST_CASE_LIST = glob.glob(f"{DATA_PATH}/api/excel_data/*.xls")
API_EXCEL_FILE = os.path.join(DATA_PATH, "api", "excel_data", "demo01.xls")

sheet_id = 0
API_SQL_FILE = os.path.join(DATA_PATH, "api", 'sql_data', 'test.sql')
API_YAML_PATH = os.path.join(DATA_PATH, "api", 'yaml_data', 'test.yaml')

UI_EXCEL_FILE = os.path.join(DATA_PATH, "ui", "excel_data", "test.xls")
UI_SQL_FILE = os.path.join(DATA_PATH, "ui", 'sql_data', 'test.sql')
UI_YAML_DIR = os.path.join(DATA_PATH, "ui", 'yaml_data')
UI_YAML_PATH = os.path.join(DATA_PATH, "ui", 'yaml_data', 'test.yaml')

PRF_YAML_PATH = os.path.join(DATA_PATH, "prf", 'yaml_data', 'test.yaml')

# ------------------ bat文件相关 -----------------------
API_BAT_FILE = os.path.join(BASE_PATH, "bat", "generate_report.bat")
API_RUN_SERVER_FILE = os.path.join(BASE_PATH, "bat", "run_allure_server.bat")

# ------------------ 项目测试报告 -----------------------
API_REPORT_PATH = os.path.join(BASE_PATH, "report", "api_report")
UI_REPORT_PATH = os.path.join(BASE_PATH, "report", "ui_report")
# ------------------ api项目测试报告 -----------------------
API_REPORT_RESULT_PATH = os.path.join(API_REPORT_PATH, "allure_result")
API_REPORT_END_PATH = os.path.join(API_REPORT_PATH, "allure_report")
html_reposrt_path = os.path.join(API_REPORT_END_PATH, 'index.html')
API_REPORT_HISTORY_PATH = os.path.join(API_REPORT_PATH, "allure_report", "history")
API_RESULT_HISTORY_PATH = os.path.join(API_REPORT_PATH, "allure_result", "history")
API_FILE_LIST_PATH = os.path.join(API_REPORT_PATH, "zip", "report.zip")  # 要压缩文件名称
API_REPORT_DIR = os.path.join(API_REPORT_PATH, "report", "allure_report")  # 要压缩文件路径
API_FILE_LIST = [os.path.join(API_REPORT_PATH, "zip", "report.zip")]  # 邮件附件列表，格式为列表
API_StartEnvironmentFilePath = os.path.join(BASE_PATH, "environment.properties")
API_StartExcutorJson = os.path.join(BASE_PATH, "executor.json")
API_EndEnvironmentFile = os.path.join(API_REPORT_PATH, "allure_result", "environment.properties")
API_EndExcutorJson = os.path.join(API_REPORT_PATH, "allure_result", "executor.json")
# ------------------ ui项目测试报告 -----------------------
UI_REPORT_RESULT_PATH = os.path.join(UI_REPORT_PATH, "allure_result")
UI_REPORT_END_PATH = os.path.join(UI_REPORT_PATH, "allure_report")
UI_REPORT_HISTORY_PATH = os.path.join(UI_REPORT_PATH, "allure_report", "history")
UI_RESULT_HISTORY_PATH = os.path.join(UI_REPORT_PATH, "allure_result", "history")
UI_FILE_LIST_PATH = os.path.join(UI_REPORT_PATH, "zip", "report.zip")  # 要压缩文件名称
UI_REPORT_DIR = os.path.join(UI_REPORT_PATH, "report", "allure_report")  # 要压缩文件路径
UI_FILE_LIST = [os.path.join(UI_REPORT_PATH, "zip", "report.zip")]  # 邮件附件列表，格式为列表
UI_StartEnvironmentFilePath = os.path.join(BASE_PATH, "environment.properties")
UI_StartExcutorJson = os.path.join(BASE_PATH, "executor.json")
UI_EndEnvironmentFile = os.path.join(UI_REPORT_PATH, "allure_result", "environment.properties")
UI_EndExcutorJson = os.path.join(UI_REPORT_PATH, "allure_result", "executor.json")
UI_IMG_PATH = os.path.join(UI_REPORT_PATH, "img")
# 正常截图文件位置：
UI_OR_IMG_PATH = os.path.join(UI_IMG_PATH, "ordinary")
# 断言截图存放位置
UI_ASS_IMG_PATH = os.path.join(UI_IMG_PATH, "assert")
# 失败截图存放位置
UI_FAIL_IMG_PATH = os.path.join(UI_IMG_PATH, "fail")
# ------------------ driver ----------------------------
DRIVER = os.path.join(BASE_PATH, "driver", "chromedriver.exe")
BROWSER = "Chrome"
chrome_app = r"C:\Users\Zhang\AppData\Local\Google\Chrome\Application"  # 需要修改
chrome_reg = r"SOFTWARE\Google\Chrome\BLBeacon"  # win chrome注册表地址

PRF_CONFIG_PATH = os.path.join(BASE_PATH, "performance", "locust.conf")

TOKEN_FILE = os.path.join(DATA_PATH, "api", "token.txt")
PYQT5_FILE = os.path.join(DATA_PATH, "api", "pyqt5.txt")

PROMETHEUSDATA = os.path.join(API_REPORT_END_PATH, "export", "prometheusData.txt")
