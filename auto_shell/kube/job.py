#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 9:55
@Author  : ZhangTAO
@File    : job.py
@Software: PyCharm
"""
from tools.requests_tools.api_tool_request import Requests

base_url = r'http://10.0.34.13:10007'

# num = 0
if __name__ == '__main__':
    # 创建镜像仓库
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer 1ea2a075-eff7-40e4-b418-76dfc17d038d'
    }

    url = base_url + '/kube/v1/api/argo/task'
    for i in range(1, 51):
        # KUBE的任务
        # data = {
        #   "name": f"zt-test-{i}",
        #   "flowId": "da0a067baedd4d4481e3ab2913e3b9bf",
        #   "priority": 1000,
        #   "description": "",
        #   "originalName": "kube",
        #   "paramList": []
        # }

        # 三方的任务
        data = {
            "name": f"张涛创建三方测试{i}",
            "flowId": "5b0786e4751848c7a4c8be859085b9d4",
            "originalId": "oj.task.i.287036935841771520",
            "originalName": "三维",
            "description": "张涛创建三方测试01",

            "appCode": "3D_modeling",
            "appBiz": "kube_3dmodel",
            "key": "lUAmQPKIxUEBYspSFGyouctwDjRScznvdtyOCptDpGWpisYQbF",
            "queueName": "model.kube.updatetask",

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
        res = Requests().send_request(url=url, method='post', parametric_key='json', data=data, headers=headers,
                                      file=None)
        print(res.json())
