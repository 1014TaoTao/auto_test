# coding:utf-8
# ==============================
#         生成报告的封装
# ==============================
import os
import shutil
import subprocess

from common import setting
from tools.public_tool_log import logger


class TestManager:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)

    def run_bat(self, file):
        """
        :param file:
        :return:
        """
        self.logger.info("【开始执行run_bat】")
        p = subprocess.Popen("cmd.exe /c" + file, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while curline != b'':
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)

    def del_old_result(self):
        """
        :return:
        """
        self.logger.info("【开始删除旧的结果集……】")
        if os.path.exists(setting.API_REPORT_RESULT_PATH):
            shutil.rmtree(setting.API_REPORT_RESULT_PATH)

    def generate_report(self):
        """
        :return:
        """
        self.logger.info("【开始生成报告……】")
        if not os.path.exists(setting.API_REPORT_RESULT_PATH):
            os.mkdir(setting.API_REPORT_RESULT_PATH)
        if not os.path.exists(setting.API_REPORT_END_PATH):
            os.mkdir(setting.API_REPORT_END_PATH)
        os.system(f"allure generate {setting.API_REPORT_RESULT_PATH} -o {setting.API_REPORT_END_PATH} --clean")

        # 复制history文件夹，在本地生成趋势图
        files = os.listdir(setting.API_REPORT_HISTORY_PATH)
        # 如果不存在则先创建文件夹
        if not os.path.exists(setting.API_RESULT_HISTORY_PATH):
            os.mkdir(setting.API_RESULT_HISTORY_PATH)
        self.logger.info("【复制history文件夹】")
        for file in files:
            shutil.copy(os.path.join(setting.API_REPORT_HISTORY_PATH, file), setting.API_RESULT_HISTORY_PATH)

        # 复制environment.properties文件夹，在本地生成测试环境
        self.logger.info("【开始复制 environment.properties文件到allure_result下】")
        shutil.copy(setting.API_StartEnvironmentFilePath, setting.API_EndEnvironmentFile)
        self.logger.info("开始复制 environment.xml文件到allure_result下")
        shutil.copy(setting.API_StartEnvironmentFileXMLPath, setting.API_EndEnvironmentXMLFile)

        # 复制 executor.json文件夹，在本地生成测试环境
        self.logger.info("【开始复制 executor.json文件到allure_result下】")
        shutil.copy(setting.API_StartExcutorJson, setting.API_EndExcutorJson)

    def run_allure_server(self):
        """
        :return:
        """
        self.logger.info("【启动allure服务！】")
        os.system(f"allure open {setting.API_REPORT_RESULT_PATH}")


if __name__ == '__main__':
    # 复制environment.properties文件夹，在本地生成测试环境
    print("【开始复制 environment.properties文件到allure_result下】")
    shutil.copy(setting.API_StartEnvironmentFilePath, setting.API_EndEnvironmentFile)
    print("开始复制 environment.xml文件到allure_result下")
    shutil.copy(setting.API_StartEnvironmentFileXMLPath, setting.API_EndEnvironmentXMLFile)

    # 复制 executor.json文件夹，在本地生成测试环境
    print("【开始复制 executor.json文件到allure_result下】")
    shutil.copy(setting.API_StartExcutorJson, setting.API_EndExcutorJson)