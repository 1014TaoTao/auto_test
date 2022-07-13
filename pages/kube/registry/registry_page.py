#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from basepage.base import Page
from tools.yaml_tools.ui_tool_read_yaml import Element

search = Element()

"""
镜像仓库页面
"""


class Registry(Page):

    # 打开镜像仓库页面
    def __int__(self):
        url = r'/mirroring'
        self.open_url(url)

    # 创建镜像仓库
    def create_repostry(self):
        pass

    # 仓库详情
    def details__repostry(self):
        pass

    # 上传镜像 并添加仓库
    def uplaod_image(self):
        pass

