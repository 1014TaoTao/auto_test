# coding:utf-8
# ==============================
#         请求的封装
# ==============================

import requests

from common import setting
from tools.public_tool_log import logger


class Requests:
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)
        # 源码中最新版requests内做了Session前置，所以此处无需做前置处理了
        self.session = requests.Session()

    def send_get(self, url, data=None, headers=None, *args, **kwargs):
        """
        :param url:
        :param params:
        :param headers:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            if headers is None:
                res = self.session.get(url=url, params=data)
            elif data is None:
                res = self.session.get(url=url, headers=headers)
            elif headers is None and data is None:
                res = self.session.get(url=url)
            else:
                res = self.session.get(url=url, params=data, headers=headers)
            return res
        except Exception as e:
            raise f"GET请求异常:{e}"

    def send_post(self, url, data=None, headers=None, *args, **kwargs):
        """
        :param url:
        :param data:
        :param headers:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            if headers is None:
                response = self.session.post(url=url, json=data)
            elif data is None:
                response = self.session.post(url=url, headers=headers)
            elif headers is None and data is None:
                response = self.session.post(url=url)
            else:
                response = self.session.post(url=url, json=data, headers=headers)
            return response
        except Exception as e:
            raise f"POST请求异常:{e}"

    def send_put(self, url, data=None, headers=None, *args, **kwargs):
        """
        :param url:
        :param data:
        :param headers:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            if headers is None:
                res = self.session.put(url=url, json=data)
            elif data is None:
                res = self.session.put(url=url, headers=headers)
            elif headers is None and data is None:
                res = self.session.put(url=url)
            else:
                res = self.session.put(url=url, json=data, headers=headers)
            return res
        except Exception as e:
            raise f"PUT请求异常:{e}"

    def send_patch(self, url, data=None, headers=None, *args, **kwargs):
        """
        :param url:
        :param data:
        :param headers:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            if headers is None:
                res = self.session.patch(url=url, json=data)
            elif data is None:
                res = self.session.patch(url=url, headers=headers)
            elif headers is None and data is None:
                res = self.session.patch(url=url)
            else:
                res = self.session.patch(url=url, json=data, headers=headers)
            return res
        except Exception as e:
            raise f"PATCH请求异常:{e}"

    def send_delete(self, url, data=None, headers=None, *args, **kwargs):
        """
        :param url:
        :param data:
        :param headers:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            if headers is None:
                res = self.session.delete(url=url, json=data)
            elif data is None:
                res = self.session.delete(url=url, headers=headers)
            elif headers is None and data is None:
                res = self.session.delete(url=url)
            else:
                res = self.session.delete(url=url, json=data, headers=headers)
            return res
        except Exception as e:
            raise f"DELETE请求异常:{e}"

    def send_request(self, method, url, data=None, headers=None, *args, **kwargs):
        """
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param args:
        :param kwargs:
        :return:
        """
        global res
        try:
            self.logger.info(u"【请求开始...start】")
            self.logger.info(f"【请求类型Method:{method}】")
            self.logger.info(f"【请求地址Url: {url}】")
            self.logger.info(f"【请求头Headers: {headers}】")
            self.logger.info(f"【请求数据Data: {data}】")

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
            self.logger.info(f"【请求结束...end】")
            # print(res.status_code)
            return res

        except Exception as e:
            return f"发送请求异常:{e}"


# if __name__ == '__main__':
    # url = "http://192.168.0.115:10007/kuberegistry/v1/api/repository"
    #
    # headers = {
    #     'Content-Type': 'application/json;charset=UTF-8',
    #     'Authorization': 'Bearer a5244cdb-d41e-4046-bf62-bd4ca5511d8c'
    # }
    #
    # data = {"tagSet": ["分析工具"], "imageName": "zhangtao_test_001", "groupId": 495, "tenantId": 1, "description": "张涛测试"}
    #
    # res = Requests().send_post(url=url, data=data, headers=headers)
    # print(res.status_code)
