# -*- coding: utf-8 -*-

import pytest

from common import consts, setting
from tools.log_tool import logger
from tools import server_check_tool

from tools.public_tool_manager import Manager
from tools.emaili_tool import EmailPack
from tools.public_tool_dingding import DingTalk
from tools.public_tool_zip import ZipPath
"""
    执行前确认pytest.ini文件中testpath的路径
"""


class RunTest:

    def __init__(self, type_test):
        self.type_test = type_test

        if self.type_test in ['API', 'Api', 'api']:
            self.log_path = setting.API_LOG_PATH
            self.logger = logger(self.log_path)
            self.REPORT_RESULT_PATH = setting.API_REPORT_RESULT_PATH
            self.REPORT_END_PATH = setting.API_REPORT_END_PATH
            self.REPORT_HISTORY_PATH = setting.API_REPORT_HISTORY_PATH
            self.RESULT_HISTORY_PATH = setting.API_RESULT_HISTORY_PATH
            self.StartEnvironmentFilePath = setting.API_StartEnvironmentFilePath
            self.EndEnvironmentFile = setting.API_EndEnvironmentFile
            self.StartEnvironmentFileXMLPath = setting.API_StartEnvironmentFileXMLPath
            self.EndEnvironmentXMLFile = setting.API_EndEnvironmentXMLFile
            self.StartExcutorJson = setting.API_StartExcutorJson
            self.EndExcutorJson = setting.API_EndExcutorJson
            self.dirpath = setting.API_REPORT_END_PATH
            self.outFullName = setting.API_FILE_LIST_PATH
            self.file_list = setting.API_FILE_LIST

            self.logger.info(r"""
                                          _         _        _           _
                          __ _ _ __ (_)  / \\  _   _| |_ __ _| |_ __  ___| |_
                         / _` | '_ \\| | / _ \\| | | | |_/ _ \\| |/ _ \\/ __| __|
                        | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
                         \\__,_| .__/|_/_/   \\_\\___/ \\__\\___/ \\_\\___||___/\\__|
                              |_|
                              Starting      ...     ...     ...
                            """
                             )
        elif self.type_test in ['UI', 'Ui', 'ui']:
            self.log_path = setting.UI_LOG_PATH
            self.logger = logger(self.log_path)
            self.REPORT_RESULT_PATH = setting.UI_REPORT_RESULT_PATH
            self.REPORT_END_PATH = setting.UI_REPORT_END_PATH
            self.REPORT_HISTORY_PATH = setting.UI_REPORT_HISTORY_PATH
            self.RESULT_HISTORY_PATH = setting.UI_RESULT_HISTORY_PATH
            self.StartEnvironmentFilePath = setting.UI_StartEnvironmentFilePath
            self.EndEnvironmentFile = setting.UI_EndEnvironmentFile
            self.StartEnvironmentFileXMLPath = setting.UI_StartEnvironmentFileXMLPath
            self.EndEnvironmentXMLFile = setting.UI_EndEnvironmentXMLFile
            self.StartExcutorJson = setting.UI_StartExcutorJson
            self.EndExcutorJson = setting.UI_EndExcutorJson
            self.dirpath = setting.UI_REPORT_END_PATH
            self.outFullName = setting.UI_FILE_LIST_PATH
            self.file_list = setting.UI_FILE_LIST

            self.logger.info(r"""
                         _   _ ___   _       _      _____       _   
                        | | | |_ _| /_\ _  _| |_ __|_   _|__ __| |_ 
                        | |_| || | / _ \ || |  _/ _ \| |/ -_|_-<  _|
                         \___/|___/_/ \_\_,_|\__\___/|_|\___/__/\__|

                          Starting      ...     ...     ...
                        """
                             )
        else:
            raise "请输入正确的自动化测试类型['API', 'Api', 'api','UI', 'Ui', 'ui']"

        self.title = self.type_test

        self.ENVIRONMENT: str = consts.ENVIRONMENT
        self.TESTER: str = consts.TESTER告

    def run(self):
        self.logger.info(f'==========< 开始 {self.title}自动化 测试 >===========')

        # 打印系统和python的版本信息
        server_check_tool.sys_project(log_path=self.log_path)

        self.logger.info(f"【本次执行环境为:{self.ENVIRONMENT},执行人员：{self.TESTER}】")

        # 删除旧的测试结果数据
        Manager().del_old_result(log_path=self.log_path, REPORT_RESULT_PATH=self.REPORT_RESULT_PATH)

        # 执行测试
        logger(log_path=self.log_path).info("开始==>执行测试用例")
        args = [__file__,
                 "--report=_report.html",   # 指定报告文件名
                 '--title=test_report 测试报告',    # 指定报告标题
                 '--tester=Phoenixy',   # 指定报告中的测试者
                 '--desc=报告描述信息',   # 指定报告中的项目描述
                 '--template=1',    # 指定报告模板样式（1 or 2）
                 '-W', "ignore:Module already imported:pytest.PytestWarning"
                 ]
        pytest.main(args)
        logger(log_path=self.log_path).info("完成==>执行测试用例")

        # 生成测试报告
        Manager().generate_report(
            log_path=self.log_path,
            REPORT_RESULT_PATH=self.REPORT_RESULT_PATH,
            REPORT_END_PATH=self.REPORT_END_PATH,
            REPORT_HISTORY_PATH=self.REPORT_HISTORY_PATH,
            RESULT_HISTORY_PATH=self.RESULT_HISTORY_PATH,
            StartEnvironmentFilePath=self.StartEnvironmentFilePath,
            EndEnvironmentFile=self.EndEnvironmentFile,
            StartExcutorJson=self.StartExcutorJson,
            EndExcutorJson=self.EndExcutorJson
        )

        # 发送邮件
        ZipPath().zipDir(log_path=self.log_path, dirpath=self.dirpath, outFullName=self.outFullName)
        EmailPack(REPORT_END_PATH=self.REPORT_END_PATH).send_default_email(log_path=self.log_path, file_list=self.file_list)

        # 打开allure报告
        # Manager().run_allure_server(log_path=self.log_path, REPORT_END_PATH=self.REPORT_END_PATH)

        # 发送钉钉消息
        self.send_dingding(
            REPORT_END_PATH=self.REPORT_END_PATH,
            log_path=self.log_path,
            title=self.title,
            ENVIRONMENT=self.ENVIRONMENT,
            TESTER=self.TESTER
        )
        DingTalk(REPORT_END_PATH=self.REPORT_END_PATH).send_dingding(log_path=self.log_path, ENVIRONMENT=self.ENVIRONMENT, TESTER=self.TESTER)
        logger(log_path=self.log_path).info("完成==>发送钉钉报告")

        self.logger.info(f'==========< 结束 {self.title}自动化 测试 >===========')
