# coding:utf-8
# ==============================
#         请求的封装
# ==============================
from typing import MutableMapping
from typing.io import IO

import requests

from common import setting
from tools.logi_tool import logger


class Requests:

    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)
        # 源码中最新版requests内做了Session前置，所以此处无需做前置处理了
        """
        单例模式保证测试过程中使用的都是一个session对象
        """
        self.session = requests.Session()

    def send_request(self,
                     url: str,
                     method: str,
                     parametric_key: str,
                     headers: dict = None,
                     data: dict = None,
                     file: MutableMapping[str, IO] = None):
        """
        :param url: 请求url
        :param method: 请求方法
        :param parametric_key: 入参关键字， params(查询参数类型，明文传输，一般在url?参数名=参数值), data(一般用于form表单类型参数), json(一般用于json类型请求参数)
        :param headers: 请求头
        :param data: 参数数据，默认等于None
        :param file: 文件对象
        :return: 返回res对象
        """
        try:
            self.logger.info(u"【请求开始...start】")
            self.logger.info(f"【请求类型Method: {method}】")
            self.logger.info(f"【请求地址Url: {url}】")
            self.logger.info(f"【请求头Headers: {headers}】")
            self.logger.info(f"【请求数据Data: {data}】")
            self.logger.info(f"【上传文件File: {file}】")
            if parametric_key == 'params':
                res = self.session.request(
                    method=method,
                    url=url,
                    params=data,
                    headers=headers)
            elif parametric_key == 'data':
                res = self.session.request(
                    method=method,
                    url=url,
                    data=data,
                    files=file,
                    headers=headers)
            elif parametric_key == 'json':
                res = self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    files=file,
                    headers=headers)
            else:
                self.logger.error(ValueError(
                    'parametric_key为params、json、data,不可以是其他类型'))
                res = None
            return res
        except Exception as e:
            self.logger.error(f"发送请求异常:{e}")

if __name__ == '__main__':
    """
    上传文件调试
    """
    # 示例：kube应用中心上传应用图片和上传应用模板
    url = 'http://10.0.34.13:10007/kube/v1/api/helmChart/import'
    headers = {
        'Authorization': 'Bearer 6b37084a-bc09-4982-9eba-900b1ef8287c'
    }
    file = [
        ('file', ('gitea-1.9.1.tgz', open('G:\auto_test\data\gitea-1.9.1.tgz', 'rb'),'application/gzip'))
    ]
    res = Requests().send_request(url=url, method='post', parametric_key='data', headers=headers, file=file, data=None)
    print(res.json())
