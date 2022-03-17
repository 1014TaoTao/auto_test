#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/12 10:28
@Author  : ZhangTAO
@File    : api_tool_reponse.py
@Software: PyCharm
"""

from common import setting
from tools.public_tool_log import logger


class Response:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)

    def result(self, res):
        """
        :param res:
        :return:
        """
        try:
            response_dicts = dict()
            # 响应状态码
            response_dicts['code'] = res.status_code
            # 响应body
            try:
                response_dicts['body'] = res.json()
            except Exception as e:
                self.logger.error("【获取响应data异常: {0}】".format(e))
                response_dicts['body'] = ''
            # 响应txt
            # response_dicts['text'] = res.text
            # 响应毫秒时间
            time_consuming = res.elapsed.microseconds / 1000  # 毫秒为单位
            response_dicts['time_consuming'] = time_consuming
            # 响应秒时间
            time_total = res.elapsed.total_seconds()  # 秒为单位
            response_dicts['time_total'] = time_total

            # consts.STRESS_LIST.append(time_consuming)
            # 响应头
            # response_dicts['headers'] = res.headers
            # 响应cookie
            # response_dicts['cookie'] = res.cookies
            self.logger.info(f"【请求响应结果为: {response_dicts}】")
            return response_dicts
        except Exception as e:
            self.logger.error(f"处理数据异常：{e}")
