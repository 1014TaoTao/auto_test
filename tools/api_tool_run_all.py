# -*- coding: utf-8 -*-#

import pytest

from common import setting
from tools.api_tool_manager import TestManager
from tools.public_tool_dingding import DingTalk
from tools.public_tool_email import EmailPack
from tools.public_tool_log import logger
from tools.public_tool_zip import zip_path


class API_Run:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)

    # 删除旧的测试结果数据
    def delete_old_file(self):
        """
        :return:
        """
        delete_history = TestManager().del_old_result()
        self.logger.info("【完成==>删除旧的测试结果数据】")
        return delete_history

    # 执行测试
    def run_test(self):
        """
        :return:
        """
        run = pytest.main()
        return run

    # 生成测试报告
    def run_allure_report(self):
        """
        :return:
        """
        allure_report = TestManager().generate_report()  # 生成测试报告
        self.logger.info("【完成==>生成测试报告】")
        return allure_report

    # 发送邮件
    def run_email(self):
        """
        :return:
        """
        zip_path().zipDir(setting.API_REPORT_END_PATH, setting.API_FILE_LIST_PATH)
        self.logger.info("【完成==>压缩报告】")
        send_email = EmailPack(setting.API_REPORT_END_PATH).send_default_email(setting.API_LOG_PATH, setting.API_FILE_LIST,setting.API_REPORT_END_PATH)
        self.logger.info("【完成==>发送邮件】")
        return send_email

    # 自动打开测试报告
    def open_report(self):
        """
        :return:
        """
        self.logger.info("【开始==>打开测试报告】")
        open_allure_report = TestManager().run_allure_server()
        return open_allure_report

    # 发送钉钉消息
    def send_dingding(self, ENVIRONMENT, TESTER):
        """
        :return:
        """
        self.logger.info("【开始==>发送钉钉消息】")
        send_dingding_news = DingTalk().send_dingding(ENVIRONMENT, TESTER)
        return send_dingding_news
