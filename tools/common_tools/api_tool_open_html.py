'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:50
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:09:56
FilePath: \pytest_auto_uitest_apitest\tools\common_tools\api_tool_open_html.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-

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
