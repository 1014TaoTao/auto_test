#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 10:04
@Author  : ZhangTAO
@File    : 上传文件调试.py
@Software: PyCharm
"""
from tools.api_tool_request import Requests

if __name__ == '__main__':
    # 示例：kube应用中心上传应用图片和上传应用模板
    url = 'http://10.0.34.13:10007/kube/v1/api/helmChart/import'
    headers = {
        'Authorization': 'Bearer 6b37084a-bc09-4982-9eba-900b1ef8287c'
    }
    file = [
        ('file', (
            'gitea-1.9.1.tgz', open('G:\pytest_auto_uitest_apitest\data\gitea-1.9.1.tgz', 'rb'),
            'application/gzip'))
    ]
    res = Requests().send_request(url=url, method='post', parametric_key='data', headers=headers, file=file, data=None)
    print(res.json())

    #################################################################

    url = 'http://10.0.34.13:10007/fp/v1/file/upload'
    headers = {
        'Authorization': 'Bearer 6b37084a-bc09-4982-9eba-900b1ef8287c',
    }
    file = [
        ('file', ('gitea_image.png', open('G:/pytest_auto_uitest_apitest/data/gitea_image.png', 'rb'), 'image/png'))
    ]
    data = {
        "appCode": "kube",
        "appBiz": "picture",
        "path": 0
    }
    res = Requests().send_request(url=url, method='post', parametric_key='data', headers=headers, data=data, file=file)
    print(res.json())