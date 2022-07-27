# -*- coding: utf-8 -*-

from common import setting, consts
from tools.common_tools.public_tool_run_all import Run
from tools.logs_tools.public_tool_log import logger
from tools.system_tools import public_tool_project_check

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
        self.TESTER: str = consts.TESTER

    def run(self):
        self.logger.info(f'==========< 开始 {self.title}自动化 测试 >===========')

        R = Run()

        # 打印系统和python的版本信息
        public_tool_project_check.sys_project(log_path=self.log_path)

        self.logger.info(f"【本次执行环境为:{self.ENVIRONMENT},执行人员：{self.TESTER}】")

        # 删除旧的测试结果数据
        # R.delete_old_file(
        #     log_path=self.log_path,
        #     REPORT_RESULT_PATH=self.REPORT_RESULT_PATH
        # )

        # 执行测试
        R.run_test(log_path=self.log_path)

        # 生成测试报告
        R.run_allure_report(
            log_path=self.log_path,
            REPORT_RESULT_PATH=self.REPORT_RESULT_PATH,
            REPORT_END_PATH=self.REPORT_END_PATH,
            REPORT_HISTORY_PATH=self.REPORT_HISTORY_PATH,
            RESULT_HISTORY_PATH=self.RESULT_HISTORY_PATH,
            StartEnvironmentFilePath=self.StartEnvironmentFilePath,
            EndEnvironmentFile=self.EndEnvironmentFile,
            StartEnvironmentFileXMLPath=self.StartEnvironmentFileXMLPath,
            EndEnvironmentXMLFile=self.EndEnvironmentXMLFile,
            StartExcutorJson=self.StartExcutorJson,
            EndExcutorJson=self.EndExcutorJson
        )

        # 发送邮件
        # R.run_email(
        #     REPORT_END_PATH=self.REPORT_END_PATH,
        #     dirpath=self.dirpath,
        #     outFullName=self.outFullName,
        #     log_path=self.log_path,
        #     file_list=self.file_list
        # )

        # 打开allure报告
        # R.open_report(
        #     log_path=self.log_path,
        #     REPORT_END_PATH=self.REPORT_END_PATH
        # )

        # 发送钉钉消息
        R.send_dingding(
            REPORT_END_PATH=self.REPORT_END_PATH,
            log_path=self.log_path,
            title=self.title,
            ENVIRONMENT=self.ENVIRONMENT,
            TESTER=self.TESTER
        )

        self.logger.info(f'==========< 结束 {self.title}自动化 测试 >===========')
