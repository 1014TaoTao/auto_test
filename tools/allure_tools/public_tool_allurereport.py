#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/3/20 14:40
@Author  : ZhangTAO
@File    : public_tool_allurereport.py
@Software: PyCharm
"""
import json

from common.setting import API_REPORT_END_PATH
import os


class AllureFileClean:
    """allure 报告数据清洗，提取业务需要得数据"""

    @classmethod
    def _getAllFiles(cls, REPORT_END_PATH) -> list:
        """
        :return:
        """
        """ 获取所有 test-case 中的 json 文件 """
        filename = []
        # 获取所有文件下的子文件名称
        # for root, dirs, files in os.walk(API_REPORT_END_PATH + '/data/test-cases'):
        for root, dirs, files in os.walk(REPORT_END_PATH + '/data/test-cases'):
            for filePath in files:
                path = os.path.join(root, filePath)
                filename.append(path)
        return filename

    def getTestCases(self, REPORT_END_PATH) -> list:
        """
        :return:
        """
        """ 获取所有 allure 报告中执行用例的情况"""
        # 将所有数据都收集到files中
        files = []
        for i in self._getAllFiles(REPORT_END_PATH):
            with open(i, 'r', encoding='utf-8') as fp:
                date = json.load(fp)
                files.append(date)
        return files

    def getFailedCase(self, REPORT_END_PATH) -> list:
        """
        :return:
        """
        """ 获取到所有失败的用例标题和用例代码路径"""
        errorCase = []
        for i in self.getTestCases(REPORT_END_PATH):
            if i['status'] == 'failed' or i['status'] == 'broken':
                errorCase.append((i['name'], i['fullName']))
        return errorCase

    def getFailedCasesDetail(self, REPORT_END_PATH) -> str:
        """
        :return:
        """
        """ 返回所有失败的测试用例相关内容 """
        Data = self.getFailedCase(REPORT_END_PATH)
        # 判断有失败用例，则返回内容
        if len(Data) >= 1:
            values = "失败用例:\n"
            values += "        **********************************\n"
            for i in Data:
                values += "        " + i[0] + ":" + i[1] + "\n"
            return values
        else:
            # 如果没有失败用例，则返回False
            return ""

    @classmethod
    def getCaseCount(cls, REPORT_END_PATH) -> dict:
        """
        :return:
        """
        """ 统计用例数量 """
        file_name = REPORT_END_PATH + '/history/history-trend.json'
        with open(file_name, 'r', encoding='utf-8') as fp:
            date = json.load(fp)[0]['data']
        return date


class CaseCount:
    def __init__(self):
        self.AllureData = AllureFileClean()

    def passCount(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例成功数"""
        return self.AllureData.getCaseCount(REPORT_END_PATH)['passed']

    def failedCount(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例失败数"""
        return self.AllureData.getCaseCount(REPORT_END_PATH)['failed']

    def brokenCount(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例异常数"""
        return self.AllureData.getCaseCount(REPORT_END_PATH)['broken']

    def skippedCount(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例跳过数"""
        return self.AllureData.getCaseCount(REPORT_END_PATH)['skipped']

    def totalCount(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例总数"""
        return self.AllureData.getCaseCount(REPORT_END_PATH)['total']

    def passRate(self, REPORT_END_PATH):
        """
        :return:
        """
        """用例成功率"""
        # 四舍五入，保留2位小数
        try:
            passRate = round((self.passCount(REPORT_END_PATH) + self.skippedCount(REPORT_END_PATH)) / self.totalCount(
                REPORT_END_PATH) * 100, 2)

            return str(passRate) + '%'
        except ZeroDivisionError:
            return "0.00%"

# if __name__ == '__main__':
#     data = AllureFileClean().getCaseCount()
#     print(data)
