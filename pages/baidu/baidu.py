#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from basepage.base import Page
from tools.ui_tool_read_yaml import Element

search = Element()


class BaiDu(Page):

    def sousuo(self, text):
        """输入搜索"""
        url = "https://www.baidu.com/"
        self.open_url(url)
        sousuokuang = search['搜索框']
        sousuobutton = search['搜索按钮']
        self.type_input(sousuokuang, text)
        self.click(sousuobutton)

# if __name__ == '__main__':
#     driver = select_browser()
#     BaiduPage01(driver).start()
#     BaiduPage01(driver).query_baidu()
#     BaiduPage01(driver).final()
