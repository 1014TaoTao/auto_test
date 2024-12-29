# -*- coding:utf-8 -*-

import os
import yaml
import time
from selenium.webdriver.common.by import By
import logging


class ElementPack:
    """获取元素"""

    def __init__(self, element_path):
        self.element_path = element_path
        if not os.path.exists(self.element_path):
            logging.error(f"{self.element_path} 文件不存在！")
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
        logging.error(f"中不存在关键字：{item}")

    def validate_elements(self):
        """审查所有的元素是否正确"""
        # 元素定位的类型
        LOCATE_MODE = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'id': By.ID,
            'class': By.CLASS_NAME
        }
        start_time = time.time()

        for k, v in self.data.items():
            pattern, value = v.split('==')
            if pattern not in LOCATE_MODE:
                raise AttributeError(f'【{k}】元素没有指定类型')
            if pattern == 'xpath':
                assert '//' in value, f'【{k}】元素xpath类型与值不配'
            if pattern == 'css':
                assert '//' not in value, f'【{k}】元素css类型与值不配'
            if pattern in ('id', 'name', 'class'):
                assert value, f'【{k}】元素类型与值不匹配'
        end_time = time.time()

        logging.info(f"ui自动化，校验元素定位data格式【END！用时 %.3f秒！" %
                     (end_time - start_time))
