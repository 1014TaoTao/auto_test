# -*- coding: utf-8 -*-#
import pytest

from tools.common_tools.public_tool_manager import Manager
from tools.email_tools.public_tool_email import EmailPack
from tools.logs_tools.public_tool_log import logger
from tools.send_news_tools.public_tool_dingding import DingTalk
from tools.zip_tools.public_tool_zip import ZipPath


class Run:

    # 删除旧的测试结果数据
    def delete_old_file(self, log_path, REPORT_RESULT_PATH):
        """
        :return:
        """

        Manager().del_old_result(log_path, REPORT_RESULT_PATH)

    # 执行测试
    def run_test(self, log_path):
        """
        :return:
        """
        logger(log_path).info("开始==>执行测试用例")
        pytest.main()
        logger(log_path).info("完成==>执行测试用例")

    # 生成测试报告
    def run_allure_report(self,
                          log_path,
                          REPORT_RESULT_PATH,
                          REPORT_END_PATH,
                          REPORT_HISTORY_PATH,
                          RESULT_HISTORY_PATH,
                          StartEnvironmentFilePath,
                          EndEnvironmentFile,
                          StartExcutorJson,
                          EndExcutorJson
                          ):
        """
        :return:
        """

        Manager().generate_report(
            log_path,
            REPORT_RESULT_PATH,
            REPORT_END_PATH,
            REPORT_HISTORY_PATH,
            RESULT_HISTORY_PATH,
            StartEnvironmentFilePath,
            EndEnvironmentFile,
            StartExcutorJson,
            EndExcutorJson
        )  # 生成测试报告

    # 发送邮件
    def run_email(self, REPORT_END_PATH, dirpath, outFullName, log_path, file_list):
        """
        :return:
        """

        ZipPath().zipDir(log_path, dirpath, outFullName)

        EmailPack(REPORT_END_PATH).send_default_email(log_path, file_list)

    # 自动打开测试报告
    def open_report(self, log_path, REPORT_END_PATH):
        """
        :return:
        """
        Manager().run_allure_server(log_path, REPORT_END_PATH)

    # 发送钉钉消息
    def send_dingding(self, REPORT_END_PATH, log_path, title, ENVIRONMENT: str, TESTER: str):
        """
        :return:
        """

        DingTalk(REPORT_END_PATH).send_dingding(log_path, title, ENVIRONMENT, TESTER)
        logger(log_path).info("完成==>发送钉钉报告")
