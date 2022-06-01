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


class PyqtTxtPack:
    def __init__(self):
        pass

    def write_pyqt5_txt(self, info_dict: dict):
        """
        :return:
        """
        try:
            with open(setting.PYQT5_FILE, "w", encoding="utf-8") as f:
                f.write(str(info_dict))
                logger.info(f"【写入pyqt5_txt成功：{info_dict}】")
            f.close()
        except Exception as e:
            logger.error(f"【写入pyqt5_txt异常！{e}】")

    def read_pyqt5_txt(self):
        """
        :return:
        """
        try:
            with open(file=setting.PYQT5_FILE, mode='r', encoding="utf-8") as f:
                info_str = f.read()
                if len(info_str) != 0:
                    return eval(info_str)
                else:
                    logger.error(f"【读取pyqt5_txt为:空】")
            f.close()
        except Exception as e:
            logger.error(f"【读取pyqt5_txt异常！{e}】")

    # 清空pyqt5_txt
    def clear_pyqt5_txt(self):
        """
        :return:
        """
        try:
            with open(file=setting.PYQT5_FILE, mode="w+", encoding="utf-8") as f:
                logger.error(f"【清空pyqt5_txt完成】")
                f.close()
        except Exception as e:
            logger.error(f"【清空pyqt5_txt异常！{e}】")
