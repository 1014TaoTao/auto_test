#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from basepage.base import Page

from tools.yaml_tools.ui_tool_read_yaml import Element

search = Element(element_path=r'E:\pytest_auto_uitest_apitest\case\ui\yaml_data\kube_login.yaml')

"""
镜像仓库页面
"""


class Login(Page):

    # 创建镜像仓库
    def login(self):
        url = r'http://10.0.34.13:10004/login'
        self.max_window()

        self.open_url(url)
        input_user = search['用户名输出框']
        input_password = search['密码输入框']
        button_ok = search['登陆按钮']
        # # 输入用户名
        self.text_input(input_user, '15382112620')
        # # 输入密码
        self.text_input(input_password, 'Admin123')
        # # 点击登陆
        self.click(button_ok)
        # 得到背景和滑块的item, 以及滑动按钮

        sider = search['滑块']
        mubiao = search['滑块背景']
        self.background_item = self.drag_and_drop(el_css=sider, ta_css=mubiao)


if __name__ == '__main__':
    # from tools.common_tools.api_tool_login import UiLogin
    # UiLogin().ui_login()
    from basepage.browser import select_browser

    driver = select_browser()
    Login(driver).login()

    # import requests
    # response = requests.get(r'http://10.0.34.13:10004/bcs/v1/pubapi/captcha/slider')
    # print(response.json()['data']['uid'])

# driver = webdriver.Chrome()
# js = 'window.localStorage.setItem("token", "token值")'
# driver.execute_script(js)
