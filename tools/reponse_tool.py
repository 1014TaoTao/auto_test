# -*- coding: utf-8 -*-

import logging


class Response:
    def __init__(self):
        pass

    def result(self, res) -> dict:
        """
        :param res:
        :return:
        """
        try:
            response_dicts = dict()
            # 响应状态码
            response_dicts['code'] = int(res.status_code)
            # 响应body
            response_dicts['body'] = str(res.json())
            # 响应秒时间
            response_dicts['time_total'] = res.elapsed.total_seconds()  # 秒为单位

            logging.info(f"【请求响应结果为: {response_dicts}】")
            return response_dicts
        except Exception as e:
            logging.error(f"响应结果处理异常：{e}")
