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
        TestManager().del_old_result()
        self.logger.info("【完成==>删除旧的测试结果数据】")

    # 执行测试
    def run_test(self):
        """
        :return:
        """
        pytest.main()

    # 生成测试报告
    def run_allure_report(self):
        """
        :return:
        """
        TestManager().generate_report()  # 生成测试报告
        self.logger.info("【完成==>生成测试报告】")

    # 发送邮件
    def run_email(self):
        """
        :return:
        """
        zip_path().zipDir(setting.API_REPORT_END_PATH, setting.API_FILE_LIST_PATH)
        self.logger.info("【完成==>压缩报告】")
        EmailPack().send_default_email(setting.API_LOG_PATH,setting.API_FILE_LIST,)
        self.logger.info("【完成==>发送邮件】")

    # 自动打开测试报告
    def open_report(self):
        """
        :return:
        """
        self.logger.info("【开始==>打开测试报告】")
        TestManager().run_allure_server()

    # 发送钉钉消息
    def send_dingding(self, ENVIRONMENT: str, TESTER: str):
        """
        :return:
        """
        self.logger.info("【开始==>发送钉钉消息】")
        DingTalk().send_dingding(ENVIRONMENT, TESTER)


if __name__ == '__main__':
    A = API_Run()
    A.run_email()
