#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 9:55
@Author  : ZhangTAO
@File    : job_shell.py
@Software: PyCharm
"""
from tools.api_tool_request import Requests

if __name__ == '__main__':
    # 创建镜像仓库
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer 6b37084a-bc09-4982-9eba-900b1ef8287c'
    }

    url = 'http://10.0.34.13:10007/kube/v1/api/argo/task'

    data = {
        "name": "张涛创建三方测试05",
        "flowId": "5b0786e4751848c7a4c8be859085b9d4",
        "originalId": "oj.task.i.287036935841771520",
        "originalName": "三维3",
        "description": "张涛创建三方测试05",
        "queueName": "test_queue",
        "priority": "100",
        "paramList": [
            {
                "name": "msg",
                "value": "hello",
                "description": "打印信息"
            },
            {
                "name": "time",
                "value": "10",
                "description": "时间"
            }
        ],
        "extensions": {
            "app_code": "KF00001",
            "app_code_biz": "KF00002"
        }
    }
    res = Requests().send_request(url=url, method='post', parametric_key='json', data=data, headers=headers, file=None)
    print(res.json())
