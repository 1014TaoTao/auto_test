
# -*- coding: utf-8 -*-

from basepage.base import Page
from common import setting
from tools.ui_tool_read_yaml import Element

search = Element(element_path=setting.UI_YAML_PATH)


class BaiDu(Page):

    def sousuo(self, text):
        """输入搜索"""
        url = "https://www.baidu.com/"
        self.open_url(url)
        sousuokuang = search['搜索框']
        sousuobutton = search['搜索按钮']
        self.text_input(sousuokuang, text)
        self.click(sousuobutton)

# if __name__ == '__main__':
#     driver = select_browser()
#     BaiduPage01(driver).start()
#     BaiduPage01(driver).query_baidu()
#     BaiduPage01(driver).final()
