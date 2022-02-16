#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/16 16:57
@Author  : ZhangTAO
@File    : get_all_info.py
@Software: PyCharm
"""
from api_auto_test import Ui_ApiAutoTool


class GetInfo(Ui_ApiAutoTool):
    def __init__(self):
        super(GetInfo).__init__()

    def get_all_info(self):
        all_data = self.runButton_info()
        print(all_data)


if __name__ == '__main__':
    g = GetInfo()
    g.get_all_info()