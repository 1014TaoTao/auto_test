#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/14 13:01
@Author  : ZhangTAO
@File    : task.py
@Software: PyCharm
"""

# 代码模式创建算元
from tools.requests_tools.api_tool_request import Requests

base_url = 'http://10.0.34.13:10007'
headers = {
    'Authorization': 'Bearer d1bd3bf0-3ead-4707-9b3f-97c5778731fb',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


# 添加表单算元
def add_form_task():
    url = f'{base_url}/kube/v1/api/tekton/task'
    data = {
        "labels": {
            "category": "zt-task-form"
        },
        "name": "zt-task-form-01",
        "namespace": "default",
        "description": "task-description",
        "workspaces": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": False
            }
        ],
        "steps": [
            {
                "name": "test-step",
                "command": [
                    "cowsay"
                ],
                "args": [
                    "$(params.message)"
                ],
                "timeout": "0s",
                "imagePullPolicy": "Always",
                "env": [],
                "imageType": 2,
                "onError": "stopAndFail",
                "image": "docker/whalesay",
                "resources": {
                    "limits": {
                        "memory": "1",
                        "cpu": "1",
                        "gpu": "0"
                    },
                    "requests": {
                        "memory": "1",
                        "cpu": "1",
                        "gpu": "0"
                    }
                }
            }
        ],
        "params": [
            {
                "name": "message",
                "default": "hello world",
                "description": "test-params-description"
            }
        ]
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()['data']['id']


# 调试表单算元
def debuug_form_task():
    url = f'{base_url}/kube/v1/api/tekton/taskRun'
    data = {
        # "id": "adbb23c968514b42864c5ff7125c030b",
        "id": f"{add_form_task()}",
        "name": "zt-task-form-01",
        "description": "task-description",
        "category": "zt-task-form",
        "labels": {
            "category": "zt-task-form"
        },
        "namespace": "default",
        "template": "{\"apiVersion\":\"tekton.dev/v1beta1\",\"kind\":\"Task\",\"metadata\":{\"name\":\"zt-task-form-01\",\"namespace\":\"default\",\"labels\":{\"category\":\"zt-task-form\"}},\"spec\":{\"description\":\"zt-task-form-01\",\"workspaces\":[{\"name\":\"workspace\",\"mountPath\":\"/workspace\",\"readOnly\":false,\"optional\":false}],\"params\":[{\"name\":\"message\",\"type\":\"string\",\"default\":\"hello world\",\"description\":\"test-params-description\"}],\"steps\":[{\"name\":\"test-step\",\"image\":\"docker/whalesay\",\"imagePullPolicy\":\"Always\",\"env\":[],\"onError\":\"stopAndFail\",\"command\":[\"cowsay\"],\"args\":[\"$(params.message)\"],\"resources\":{\"requests\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"},\"limits\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"}}}]}}",
        "workspaces": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": False,
                "optional": False,
                "description": None
            }
        ],
        "params": [
            {
                "name": "message",
                "type": "string",
                "description": "test-params-description",
                "default": "hello world"
            }
        ],
        "steps": [
            {
                "name": "test-step",
                "image": "docker/whalesay",
                "imageType": 2,
                "imagePullPolicy": "Always",
                "env": [],
                "timeout": "0s",
                "onError": "stopAndFail",
                "command": [
                    "cowsay"
                ],
                "args": [
                    "$(params.message)"
                ],
                "resources": {
                    "requests": {
                        "cpu": "1",
                        "memory": "1",
                        "gpu": "0"
                    },
                    "limits": {
                        "cpu": "1",
                        "memory": "1",
                        "gpu": "0"
                    }
                }
            }
        ],
        "createUser": 5627,
        "createType": "general",
        "tenantId": 1,
        "taskRunParams": [
            {
                "name": "message",
                "value": "hello world"
            }
        ],
        "storageList": [
            {
                "name": "workspace",
                "emptyDir": {
                    "medium": "Normal",
                    "sizeLimit": 1
                },
                "hostPath": None,
                "storageClass": None
            }
        ]
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


# 添加代码算元
def add_code_task():
    url = f'{base_url}/kube/v1/api/tekton/task/professional'
    data = {
        "name": "zt-task-code-01",
        "description": "task-description",
        "namespace": "default",
        "labels": {
            "category": "zt-task-code"
        },
        "template": "{\"apiVersion\":\"tekton.dev/v1beta1\",\"kind\":\"Task\",\"metadata\":{\"name\":\"zt-task-form-02\",\"namespace\":\"default\",\"labels\":{\"category\":\"zt-task-form\"}},\"spec\":{\"description\":\"zt-task-form-01\",\"workspaces\":[{\"name\":\"workspace\",\"mountPath\":\"/workspace\",\"readOnly\":false,\"optional\":false}],\"params\":[{\"name\":\"message\",\"type\":\"string\",\"default\":\"hello world\",\"description\":\"test-params-description\"}],\"steps\":[{\"name\":\"test-step\",\"image\":\"docker/whalesay\",\"imagePullPolicy\":\"Always\",\"env\":[],\"onError\":\"stopAndFail\",\"command\":[\"cowsay\"],\"args\":[\"$(params.message)\"],\"resources\":{\"requests\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"},\"limits\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"}}}]}}"
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()['data']['id']


# 调试代码算元
def debuug_code_task():
    url = f'{base_url}/kube/v1/api/tekton/taskRun'
    data = {
        "id": "bf00e5a429834d14a3386024efdbbe72",
        # "id": f"{add_form_task()}",
        "name": "zt-task-code-01",
        "description": "zt-task-code",
        "category": "zt-task-code",
        "labels": {
            "category": "zt-task-code"
        },
        "namespace": "default",
        "template": "{\"apiVersion\":\"tekton.dev/v1beta1\",\"kind\":\"Task\",\"metadata\":{\"name\":\"zt-task-code-01\",\"namespace\":\"default\",\"labels\":{\"category\":\"zt-task-code\"}},\"spec\":{\"description\":\"zt-task-code\",\"workspaces\":[{\"name\":\"workspace\",\"mountPath\":\"/workspace\",\"readOnly\":false,\"optional\":false}],\"params\":[{\"name\":\"message\",\"type\":\"string\",\"default\":\"hello world\",\"description\":\"test-params-description\"}],\"steps\":[{\"name\":\"test-step\",\"image\":\"docker/whalesay\",\"imagePullPolicy\":\"Always\",\"env\":[],\"onError\":\"stopAndFail\",\"command\":[\"cowsay\"],\"args\":[\"$(params.message)\"],\"resources\":{\"requests\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"},\"limits\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"}}}]}}",
        "workspaces": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": False,
                "optional": None,
                "description": None
            }
        ],
        "params": [
            {
                "name": "message",
                "type": "string",
                "description": "test-params-description",
                "default": "hello world"
            }
        ],
        "steps": [
            {
                "name": "test-step",
                "image": "docker/whalesay",
                "imageType": 2,
                "imagePullPolicy": "Always",
                "env": [],
                "timeout": "0s",
                "onError": "stopAndFail",
                "command": [
                    "cowsay"
                ],
                "args": [
                    "$(params.message)"
                ],
                "resources": {
                    "requests": {
                        "cpu": "1",
                        "memory": "1",
                        "gpu": "0"
                    },
                    "limits": {
                        "cpu": "1",
                        "memory": "1",
                        "gpu": "0"
                    }
                }
            }
        ],
        "createUser": 5643,
        "createType": "professional",
        "tenantId": 1,
        "taskRunParams": [
            {
                "name": "message",
                "value": "hello world"
            }
        ],
        "storageList": [
            {
                "name": "workspace",
                "emptyDir": {
                    "medium": "Normal",
                    "sizeLimit": 1
                },
                "hostPath": None,
                "storageClass": None
            }
        ]
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


if __name__ == '__main__':
    print(debuug_form_task())
