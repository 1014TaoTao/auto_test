#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/16 22:16
@Author  : ZhangTAO
@File    : api_tool_read_pyqt_txt.py
@Software: PyCharm
"""

from common import setting
from tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


def read_pyqt5_txt():
    """
    :return:
    """
    try:
        with open(file=setting.PYQT5_FILE, mode='r') as f:
            info_str = f.read()
            logger.info(f"【读取pyqt5_txt成功：{info_str}】")
        return eval(info_str)
    except Exception as e:
        logger.error(f"【读取pyqt5_txt异常！{e}】")

# print(read_pyqt5_txt())