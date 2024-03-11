'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:50
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:17:38
FilePath: \pytest_auto_uitest_apitest\tools\yaml_tools\ui_tool_read_yaml.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding:utf-8 -*-
import os

import yaml

from common import setting
from tools.logs_tools.public_tool_log import logger

logger = logger(setting.UI_LOG_PATH)


class Element:
    """获取元素"""

    def __init__(self, element_path):
        self.element_path = element_path
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
#     element_path = r'E:\pytest_auto_uitest_apitest\case\ui\yaml_data\test.yaml'
#     search = Element(element_path)
#     print(search['搜索框'])
#     print(search['搜索按钮'])
#     css = search['管理员']
#     by = css[0].strip()
#     print(by)
