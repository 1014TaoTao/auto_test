#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/14 13:01
@Author  : ZhangTAO
@File    : pipeline.py
@Software: PyCharm
"""
# 代码模式创建算元
from tools.requests_tools.api_tool_request import Requests

base_url = 'http://10.0.34.13:10007'
headers = {
    'Authorization': 'Bearer d1bd3bf0-3ead-4707-9b3f-97c5778731fb',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


# 添加表单算链
def add_form_pipeline():
    url = f'{base_url}/kube/v1/api/tekton/pipeline'
    data = {
        "pipelineInfo": {
            "labels": {
                "category": "pipeline-form"
            },
            "name": "zt-pipeline-form-02",
            "description": "pipeline-description",
            "namespace": "default"
        },
        "pipelineParams": [
            {
                "name": "pipeline-params",
                "description": "pipeline-params-description",
                "defaultValue": "100"
            },
            {
                "name": "message",
                "type": "string",
                "description": "test-params-description",
                "id": "79640bda2801400d833587ff53f1f22a",
                "defaultValue": "hello world"
            }
        ],
        "workspaces": [
            {
                "name": "workspace",
                "mountPath": "/workspace",
                "readOnly": False,
                "optional": False,
                "id": "79640bda2801400d833587ff53f1f22a"
            }
        ],
        "graphDefinition": "[{\"position\":{\"x\":624,\"y\":288},\"size\":{\"width\":212,\"height\":60},\"view\":\"vue-shape-view\",\"shape\":\"vue-shape\",\"id\":\"b66e29ef-74e3-4648-ba0f-dd938322a420\",\"data\":{\"id\":\"79640bda2801400d833587ff53f1f22a\",\"name\":\"zt-task-form-01-ofyqla\",\"description\":\"task-description\",\"task\":{\"apiVersion\":\"tekton.dev/v1beta1\",\"kind\":\"Task\",\"metadata\":{\"name\":\"zt-task-form-01-ofyqla\",\"namespace\":\"default\",\"labels\":{\"category\":\"zt-task-form\"}},\"spec\":{\"description\":\"task-description\",\"workspaces\":[{\"name\":\"workspace\",\"mountPath\":\"/workspace\",\"readOnly\":false,\"optional\":false,\"id\":\"79640bda2801400d833587ff53f1f22a\"}],\"params\":[{\"name\":\"message\",\"type\":\"string\",\"default\":\"hello world\",\"description\":\"test-params-description\",\"id\":\"79640bda2801400d833587ff53f1f22a\",\"isOpened\":true}],\"steps\":[{\"name\":\"test-step\",\"image\":\"docker/whalesay\",\"imagePullPolicy\":\"Always\",\"env\":[],\"onError\":\"stopAndFail\",\"command\":[\"cowsay\"],\"args\":[\"$(params.message)\"],\"resources\":{\"requests\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"},\"limits\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"}}}],\"conditions\":[{\"input\":\"a\",\"operator\":\"in\",\"values\":\"[a,b]\"}]}},\"baseInfor\":{\"category\":\"zt-task-form\",\"createTime\":\"2022-04-26 05:29:39\",\"createUser\":5643,\"description\":\"task-description\",\"namespace\":\"default\"},\"condition\":[],\"isClick\":false,\"isEdit\":false},\"component\":\"start-node\",\"ports\":{\"groups\":{\"top\":{\"position\":\"top\",\"attrs\":{\"circle\":{\"r\":4,\"magnet\":\"passive\",\"stroke\":\"#0F4FF0\",\"strokeWidth\":1,\"fill\":\"#fff\"}}},\"bottom\":{\"position\":\"bottom\",\"attrs\":{\"circle\":{\"r\":4,\"magnet\":true,\"stroke\":\"#0F4FF0\",\"strokeWidth\":1,\"fill\":\"#fff\"}}}},\"items\":[{\"id\":\"port1\",\"group\":\"top\"},{\"id\":\"port2\",\"group\":\"bottom\"}]},\"zIndex\":1,\"runAfter\":[]}]"
    }

    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


# 调试表单算链
def debug_form_pipeline():
    url = f'{base_url}/kube/v1/api/tekton/pipelineRun'
    data = {
        "pipelineId": "81dafc2707dc43be8d70aea08840ae66",
        "namespace": "default",
        "name": "zt-pipeline-form-02",
        "params": [
            {
                "name": "pipeline-params",
                "description": "pipeline-params-description",
                "value": "100"
            },
            {
                "id": "79640bda2801400d833587ff53f1f22a",
                "name": "message",
                "description": "test-params-description",
                "value": "hello world"
            }
        ],
        "storageList": [
            {
                "emptyDir": {
                    "medium": "Normal",
                    "sizeLimit": ""
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


# 添加代码算链
def add_code_pipeline():
    url = f'{base_url}/kube/v1/api/tekton/pipeline/professional'
    data = {
      "labels": {
        "category": "pipeline-code"
      },
      "name": "zt-pipeline-code-02",
      "description": "pipeline-description",
      "namespace": "default",
      "template": "{\"apiVersion\":\"tekton.dev/v1beta1\",\"kind\":\"Pipeline\",\"metadata\":{\"name\":\"zt-pipeline-form-02\",\"namespace\":\"default\",\"labels\":{\"category\":\"pipeline-form\"}},\"spec\":{\"description\":\"pipeline-description\",\"params\":[{\"name\":\"pipeline-params\",\"description\":\"pipeline-params-description\",\"default\":\"100\"},{\"id\":\"79640bda2801400d833587ff53f1f22a\",\"name\":\"message\",\"description\":\"test-params-description\",\"default\":\"hello world\"}],\"workspaces\":[{\"id\":\"79640bda2801400d833587ff53f1f22a\",\"name\":\"workspace\",\"optional\":false}],\"tasks\":[{\"name\":\"zt-task-form-01-ofyqla\",\"params\":[{\"name\":\"message\",\"value\":\"$(params.message)\"}],\"workspaces\":[{\"name\":\"workspace\",\"workspace\":\"workspace\"}],\"taskSpec\":{\"metadata\":{\"labels\":{\"tekton.dev/task\":\"zt-task-form-01-ofyqla\"}},\"description\":\"task-description\",\"workspaces\":[{\"name\":\"workspace\",\"mountPath\":\"/workspace\",\"readOnly\":false,\"optional\":false,\"id\":\"79640bda2801400d833587ff53f1f22a\"}],\"params\":[{\"name\":\"message\",\"type\":\"string\",\"default\":\"hello world\",\"description\":\"test-params-description\",\"id\":\"79640bda2801400d833587ff53f1f22a\"}],\"steps\":[{\"name\":\"test-step\",\"image\":\"docker/whalesay\",\"imagePullPolicy\":\"Always\",\"env\":[],\"onError\":\"stopAndFail\",\"command\":[\"cowsay\"],\"args\":[\"$(params.message)\"],\"resources\":{\"requests\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"},\"limits\":{\"memory\":\"1Gi\",\"cpu\":\"1\",\"nvidia.com/gpu\":\"0\"}}}]}}]}}"
    }

    method = 'post'
    res = Requests().send_request(url=url, method=method, parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


# 调试代码算链
def debug_code_pipeline():
    url = f'{base_url}/kube/v1/api/tekton/pipelineRun'
    data = {
      "pipelineId": "646461ac9c0f4893beff6080d1dc07ee",
      "namespace": "default",
      "name": "zt-pipeline-code-02",
      "params": [
        {
          "name": "pipeline-params",
          "description": "pipeline-params-description",
          "value": "100"
        },
        {
          "id": "79640bda2801400d833587ff53f1f22a",
          "name": "message",
          "description": "test-params-description",
          "value": "hello world"
        }
      ],
      "storageList": [
        {
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
    print(debug_code_pipeline())

