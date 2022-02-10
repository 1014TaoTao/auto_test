# coding:utf-8
# ==============================
#         请求的封装
# ==============================

import requests

from common import setting, consts
from tools.public_tool_log import logger


class Requests:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)
        # 源码中最新版requests内做了Session前置，所以此处无需做前置处理了
        self.session = requests.Session()

    def send_get(self, url, data=None, headers=None):
        # if headers is None:
        #     res = self.session.get(url=url, params=params)
        # elif params is None:
        #     res = self.session.get(url=url, headers=headers)
        # elif headers is None and params is None:
        #     res = self.session.get(url=url)
        # else:
        #     res = self.session.get(url=url, params=params, headers=headers)
        # return res
        try:
            res = self.session.get(url=url, params=data, headers=headers)
            return res
        except Exception as e:
            raise f"GET请求异常:{e}"

    def send_post(self, url, data=None, headers=None):
        # if headers is None:
        #     res = self.session.post(url=url, data=data, json=None)
        # elif data is None:
        #     res = self.session.post(url=url, headers=headers, json=None)
        # elif headers is None and data is None:
        #     res = self.session.post(url=url)
        # else:
        #     res = self.session.post(url=url, data=data, headers=headers, json=None)
        # return res
        try:
            res = self.session.post(url=url, data=data, headers=headers, json=data, files=data)
            return res
        except Exception as e:
            raise f"POST请求异常:{e}"

    def send_put(self, url, data=None, headers=None):
        # if headers is None:
        #     res = self.session.put(url=url, data=data)
        # elif data is None:
        #     res = self.session.put(url=url, headers=headers)
        # elif headers is None and data is None:
        #     res = self.session.put(url=url)
        # else:
        #     res = self.session.put(url=url, data=data, headers=headers)
        # return res
        try:
            res = self.session.put(url=url, data=data, headers=headers, json=data, files=data)
            return res
        except Exception as e:
            raise f"PUT请求异常:{e}"

    def send_patch(self, url, data=None, headers=None):
        try:
            res = self.session.patch(url=url, data=data, headers=headers, json=data, files=data)
            return res
        except Exception as e:
            raise f"PUT请求异常:{e}"

    def send_delete(self, url, data, headers=None):
        # if headers is None:
        #     res = self.session.delete(url=url, data=data)
        # elif data is None:
        #     res = self.session.delete(url=url, headers=headers)
        # elif headers is None and data is None:
        #     res = self.session.delete(url=url)
        # else:
        #     res = self.session.delete(url=url, data=data, headers=headers)
        # return res
        try:
            res = self.session.delete(url=url, data=data, headers=headers, json=data, files=data)
            return res
        except Exception as e:
            raise f"DELETE请求异常:{e}"

    def send_request(self, method, url, data, headers):
        try:
            global res
            self.logger.info(f"【开始发送请求...】")
            self.logger.info(f"【请求类型Method:{method}】")
            self.logger.info(f"【请求地址Url: {url}】")
            self.logger.info(f"【请求头Headers: {headers}】")
            self.logger.info(f"【请求数据Data: {data}】")
            if not url.startswith('http:'):
                url = '%s%s' % ('http://', url)
            if method == 'GET':
                res = self.send_get(url=url, data=data, headers=headers)
            elif method == 'POST':
                res = self.send_post(url=url, data=data, headers=headers)
            elif method == 'PUT':
                res = self.send_put(url=url, data=data, headers=headers)
            elif method == 'DELETE':
                res = self.send_delete(url=url, data=data, headers=headers)
            elif method == 'PATCH':
                res = self.send_patch(url=url, data=data, headers=headers)

            self.logger.info(f"【请求结束，开始处理响应结果...】")

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
            response_dicts['text'] = res.text
            # 响应毫秒时间
            time_consuming = res.elapsed.microseconds / 1000  # 毫秒为单位
            response_dicts['time_consuming'] = time_consuming
            # 响应秒时间
            time_total = res.elapsed.total_seconds()  # 秒为单位
            response_dicts['time_total'] = time_total

            consts.STRESS_LIST.append(time_consuming)
            # 响应头
            response_dicts['headers'] = res.headers
            # 响应cookie
            # response_dicts['cookie'] = res.cookies
            self.logger.info(f"【请求响应结果为: {response_dicts}】")
            return response_dicts
        except Exception as e:
            return f"发送请求异常:{e}"

# if __name__ == '__main__':
#     url = "http://192.168.0.122:18603/uaa/oauth/token"
#     data = {
#         "mobile": 15382112620,
#         "password": "e64b78fc3bc91bcbc7dc232ba8ec59e0",
#         "account_type": "mobile",
#         "grant_type": "password",
#         "scope": "trust",
#         "client_secret": "2c27867ba8b35dedbde7361f8ffb704d",
#         "client_id": "saas_op",
#     }
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
#         'Content-Type': 'application/json;charset=UTF-8',
#     }
#     response = Requests().send_request(method="GET", url=url, headers=headers, data=data)
#     print(response)
