# coding:utf-8
# ==============================
#         生成报告的封装
# ==============================
import os
import shutil
import subprocess

from tools.logs_tools.public_tool_log import logger


class Manager:
    def __init__(self):
        pass

    def run_bat(self, log_path, file):
        """
        :param file:
        :return:
        """
        logger(log_path).info("开始执行run_bat")
        p = subprocess.Popen("cmd.exe /c" + file, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = p.stdout.readline()
        while curline != b'':
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)

    def del_old_result(self, log_path, REPORT_RESULT_PATH):
        """
        :param REPORT_RESULT_PATH:
        :return:
        """
        logger(log_path).info("开始==>删除旧数据")
        if os.path.exists(REPORT_RESULT_PATH):
            shutil.rmtree(REPORT_RESULT_PATH)
        logger(log_path).info("完成==>删除旧数据")

    def del_old_screenshot(self, log_path, IMG_PATH):
        """
        :param IMG_PATH:
        :return:
        """
        logger(log_path).info("开始==>删除旧截图")
        if os.path.exists(IMG_PATH):
            shutil.rmtree(IMG_PATH)
        logger(log_path).info("完成==>删除旧截图")

    def generate_report(self,
                        log_path,
                        REPORT_RESULT_PATH,
                        REPORT_END_PATH,
                        REPORT_HISTORY_PATH,
                        RESULT_HISTORY_PATH,
                        StartEnvironmentFilePath,
                        EndEnvironmentFile,
                        StartEnvironmentFileXMLPath,
                        EndEnvironmentXMLFile,
                        StartExcutorJson,
                        EndExcutorJson):
        """
        :param REPORT_RESULT_PATH:
        :param REPORT_END_PATH:
        :param REPORT_HISTORY_PATH:
        :param RESULT_HISTORY_PATH:
        :param StartEnvironmentFilePath:
        :param EndEnvironmentFile:
        :param StartEnvironmentFileXMLPath:
        :param EndEnvironmentXMLFile:
        :param StartExcutorJson:
        :param EndExcutorJson:
        :return:
        """
        logger(log_path).info("开始==>生成测试报告")


        # 复制environment.properties文件夹，在本地生成测试环境
        logger(log_path).info("开始复制 environment.properties文件到allure_result下")
        shutil.copy(StartEnvironmentFilePath, EndEnvironmentFile)

        logger(log_path).info("开始复制 environment.xml文件到allure_result下")
        shutil.copy(StartEnvironmentFileXMLPath, EndEnvironmentXMLFile)

        # 复制 executor.json文件夹，在本地生成测试环境
        logger(log_path).info("开始复制 executor.json文件到allure_result下")
        shutil.copy(StartExcutorJson, EndExcutorJson)

        if not os.path.exists(REPORT_RESULT_PATH):
            os.mkdir(REPORT_RESULT_PATH)
        if not os.path.exists(REPORT_END_PATH):
            os.mkdir(REPORT_END_PATH)
        os.system(f"allure generate {REPORT_RESULT_PATH} -o {REPORT_END_PATH}")

        # 复制history文件夹，在本地生成趋势图
        files = os.listdir(REPORT_HISTORY_PATH)

        # 如果不存在则先创建文件夹
        if not os.path.exists(RESULT_HISTORY_PATH):
            os.mkdir(RESULT_HISTORY_PATH)
        logger(log_path).info("复制history文件夹")
        for file in files:
            shutil.copy(os.path.join(REPORT_HISTORY_PATH, file), RESULT_HISTORY_PATH)

        logger(log_path).info("完成==>生成测试报告")

    def run_allure_server(self, log_path,REPORT_END_PATH):
        """
        :param REPORT_END_PATH:
        :return:
        """
        logger(log_path).info("开始==>打开测试报告")
        os.system(f"allure open {REPORT_END_PATH}")
