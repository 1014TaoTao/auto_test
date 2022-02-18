#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml

from common import setting
from tools.public_tool_log import logger

logger = logger(setting.UI_LOG_PATH)


class Element:
    """获取元素"""

    def __init__(self):
        self.element_path = setting.UI_YAML_PATH
        if not os.path.exists(self.element_path):
            logger.error("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性
        通过特殊方法__getitem__实现调用任意属性，读取yaml中的值。
        这样我们就实现了定位元素的存储和调用。
        """
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        logger.error("中不存在关键字：{}".format(self, item))

# if __name__ == '__main__':
#     search = Element()
#     print(search['搜索框'])
#     print(search['搜索按钮'])
#     css = search['管理员']
#     by = css[0].strip()
#     print(by)
