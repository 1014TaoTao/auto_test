#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/14 12:58
@Author  : ZhangTAO
@File    : operator.py
@Software: PyCharm
"""
# 表单模式创建算子
from tools.requests_tools.api_tool_request import Requests

base_url = 'http://10.0.34.13:10007'
headers = {
    'Authorization': 'Bearer a3ca7b79-eb7d-4f12-adf3-99474d5946ee',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


# 添加表单算子
def add_form_operator():
    url = f'{base_url}/kube/v1/api/argo/operator'
    data = {
        "workspaceList": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": False
            },
            {
                "name": "zt-workspace-01",
                "mountPath": "/path",
                "readOnly": True
            }
        ],
        "argoOperatorStepList": [
            {
                "name": "zt-step",
                "commandList": [
                    "echo"
                ],
                "argList": [
                    "hello world"
                ],
                "activeDeadlineSeconds": "86400",
                "imagePullPolicy": "Always",
                "retryPolicy": "Never",
                "limit": 0,
                "resources": {
                    "memory": "1Gi",
                    "cpu": "1",
                    "gpu": "0"
                },
                "env": {
                    "zt-env": "hello world"
                },
                "image": "registry.cn-qingdao.aliyuncs.com/tektondev/pipeline-webhook:v1.0"
            }
        ],
        "argoParams": {
            "argoInputParamList": [
                {
                    "name": "zt-input-params",
                    "value": "hello java",
                    "description": "this is description for my zt-input-params.",
                    "index": 0
                }
            ],
            "argoOutputParamList": [
                {
                    "name": "zt-output-params",
                    "description": "this is description for my zt-output-params.",
                    "value": "hello python",
                    "index": 1
                }
            ],
            "argoInputArtifactList": [],
            "argoOutputArtifactList": []
        },
        "name": "zt-form-test-operator-02",
        "description": "this is description for my zt-form-test-operator-02",
        "category": "zt-form-group",
        "namespace": "default",
        "tabType": "my"
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


# 调试表单算子
def add_debuug_form_operator():
    url = f'{base_url}/kube/v1/api/argo/operator/debug'
    data = {
        "id": "b062975ed14346878814b0cbac8785f0",
        "argoOperatorStepList": [
            {
                "name": "zt-step",
                "image": "registry.cn-qingdao.aliyuncs.com/tektondev/pipeline-webhook:v1.0",
                "imageFromKube": None,
                "imagePullPolicy": "Always",
                "activeDeadlineSeconds": "86400",
                "limit": "0",
                "retryPolicy": "Never",
                "env": {
                    "zt-env": "hello"
                },
                "commandList": [
                    "echo"
                ],
                "argList": [
                    "hello zhangtao"
                ],
                "resources": {
                    "cpu": "1",
                    "memory": "1Gi",
                    "gpu": "0"
                }
            }
        ],
        "argoParams": {
            "argoInputParamList": [
                {
                    "index": "0",
                    "name": "zt-input-params",
                    "value": "hello zhangtao",
                    "valueFrom": None,
                    "description": "this is  description for my zt-input-params.",
                    "openStatus": None
                }
            ],
            "argoInputArtifactList": [
                {
                    "index": "2",
                    "name": "zt-input-artfact",
                    "path": "/tmp/hello.txt",
                    "mode": None,
                    "argoS3Artifact": {
                        "key": "tmp/hello.txt"
                    },
                    "argoHttpArtifact": None,
                    "argoGitArtifact": None
                }
            ],
            "argoOutputParamList": [
                {
                    "index": "1",
                    "name": "zt-output-params",
                    "value": "hello zhangtao",
                    "valueFrom": None,
                    "description": "this is description for my zt-output-params.",
                    "openStatus": None
                }
            ],
            "argoOutputArtifactList": [
                {
                    "index": "3",
                    "name": "zt-output-artifact",
                    "path": "/tmp/hello.txt",
                    "mode": None,
                    "argoS3Artifact": {
                        "key": "tmp/hello.txt"
                    },
                    "argoHttpArtifact": None,
                    "argoGitArtifact": None
                }
            ]
        },
        "workspaceList": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": None
            },
            {
                "name": "zt-workspace",
                "mountPath": "/workspace/hello.txt",
                "readOnly": None
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
            },
            {
                "name": "zt-workspace",
                "emptyDir": {
                    "medium": "Normal",
                    "sizeLimit": 1
                },
                "hostPath": None,
                "storageClass": None
            }
        ],
        "hostNetwork": False
    }
    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


if __name__ == '__main__':
    print(add_form_operator())
