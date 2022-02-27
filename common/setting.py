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

# ------------------ 项目配置文件 -----------------------
CONFIG_YAML = os.path.join(BASE_PATH, "config", "Config.yaml")

# ------------------ 项目数据文件 -----------------------
DATA_PATH = os.path.join(BASE_PATH, "case")
TEST_CASE_LIST = glob.glob(f"{DATA_PATH}/api/excel_data/*.xls")
API_EXCEL_FILE = os.path.join(DATA_PATH, "api", "excel_data", "kube.xls")

sheet_id = 0
API_SQL_FILE = os.path.join(DATA_PATH, "api", 'sql_data', 'test.sql')
API_YAML_PATH = os.path.join(DATA_PATH, "api", 'yaml_data', 'test.yaml')

# ------------------ 项目测试报告 -----------------------
API_REPORT_PATH = os.path.join(BASE_PATH, "report", "api_report")

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

TOKEN_FILE = os.path.join(DATA_PATH, "api", "token.txt")
PYQT5_FILE = os.path.join(DATA_PATH, "api", "pyqt5.txt")

PROMETHEUSDATA = os.path.join(API_REPORT_END_PATH, "export", "prometheusData.txt")
