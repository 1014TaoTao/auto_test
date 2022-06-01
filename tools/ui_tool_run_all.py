# -*- coding: utf-8 -*-#

import pytest

from tools.ui_tool_manager import ReportManager
from common import setting
from tools.public_tool_zip import zip_path
from tools.public_tool_email import EmailPack
from tools.public_tool_log import logger


class UI_Run:
    def __init__(self):
        self.logger = logger(setting.UI_LOG_PATH)

    # 删除旧的测试结果数据
    def delete_old_file(self):
        ReportManager().del_old_result()
        self.logger.info("完成==>删除旧的测试结果数据")

    # 删除旧得照片
    def del_old_img(self):
        ReportManager().del_old_screenshot()
        self.logger.info("完成==>删除旧的测试截图")

    # 执行测试
    def run_test(self):
        self.logger.info("开始==>执行测试用例")
        pytest.main()

    # 生成测试报告
    def run_allure_report(self):
        ReportManager().generate_report()  # 生成测试报告
        self.logger.info("完成==>生成测试报告")

    # 发送邮件
    def run_email(self):
        zip_path().zipDir(setting.UI_REPORT_END_PATH, setting.UI_FILE_LIST_PATH)
        self.logger.info("【完成==>压缩报告】")
        EmailPack().send_default_email(setting.UI_LOG_PATH, setting.UI_FILE_LIST)
        self.logger.info("完成==>发送邮件")

    # 自动打开测试报告
    def open_report(self):
        self.logger.info("开始==>打开测试报告")
        ReportManager().run_allure_server()
