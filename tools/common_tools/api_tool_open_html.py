#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/16 12:43
@Author  : ZhangTAO
@File    : api_tool_open_html.py
@Software: PyCharm
"""
import webbrowser


class OpenHtml:
    def __init__(self):
        pass

    def see_html(self):
        url = r'http://localhost:63342/pytest_auto_uitest_apitest/report/api_report/allure_report/index.html'
        webbrowser.open(url)
#
# if __name__ == '__main__':
#     OpenHtml().see_html()
