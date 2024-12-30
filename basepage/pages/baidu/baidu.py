
# -*- coding: utf-8 -*-

from basepage.base import Page
from config import setting
from tools.element_check_tool import ElementPack

search = ElementPack(element_path=setting.UI_YAML_PATH)


class BaiDu(Page):

    def sousuo(self, text):
        """输入搜索内容，点击搜索按钮，判断搜索结果"""
        url = "https://www.baidu.com/"
        self.open_url(url)
        sousuokuang = search['搜索框']
        sousuobutton = search['搜索按钮']
        self.text_input(sousuokuang, text)
        self.click(sousuobutton)
        result = self.titie_is_value("{0}_百度搜索".format(text))
        return result

# if __name__ == '__main__':
#     driver = select_browser()
#     BaiduPage01(driver).start()
#     BaiduPage01(driver).query_baidu()
#     BaiduPage01(driver).final()
