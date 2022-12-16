import os

from common import setting

REPORT_END_PATH = setting.API_REPORT_END_PATH

os.system(f"allure open {REPORT_END_PATH}")