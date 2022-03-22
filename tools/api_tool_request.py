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
        """
        单例模式保证测试过程中使用的都是一个session对象
        """
        self.session = requests.Session()

    def send_request(self,
                     url,
                     method,
                     parametric_key,
                     headers=None,
                     data=None,
                     file=None):
        """
            :param method: 请求方法
            :param url: 请求url
            :param parametric_key: 入参关键字， params(查询参数类型，明文传输，一般在url?参数名=参数值), data(一般用于form表单类型参数), json(一般用于json类型请求参数)
            :param data: 参数数据，默认等于None
            :param file: 文件对象
            :param header: 请求头
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
                self.logger.error(ValueError('可选关键字为params, json, data'))
                raise ValueError('可选关键字为params, json, data')
            return res
        except Exception as e:
            return f"发送请求异常:{e}"


if __name__ == '__main__':
    # url = "http://192.168.0.115:10007/kuberegistry/v1/api/repository"
    #
    # headers = {
    #     'Content-Type': 'application/json;charset=UTF-8',
    #     'Authorization': 'Bearer 6317f32b-c5a7-4a82-8958-456ce06857eb'
    # }
    #
    # data = {"tagSet": ["分析工具"], "imageName": "zhangtao_test_001", "groupId": 495, "tenantId": 1, "description": "张涛测试"}
    #
    # res = Requests().send_post(url=url, data=data, headers=headers)
    # print(res.status_code)
    #
    # url = 'http://10.0.34.13:10007/kube/v1/api/argo/task'
    # data = {
    #     "name": "张涛创建三方测试05",
    #     "flowId": "5b0786e4751848c7a4c8be859085b9d4",
    #     "originalId": "oj.task.i.287036935841771520",
    #     "originalName": "三维3",
    #     "description": "张涛创建三方测试05",
    #     "queueName": "test_queue",
    #     "priority": "100",
    #     "paramList": [
    #         {
    #             "name": "msg",
    #             "value": "hello",
    #             "description": "打印信息"
    #         },
    #         {
    #             "name": "time",
    #             "value": "10",
    #             "description": "时间"
    #         }
    #     ],
    #     "extensions": {
    #         "app_code": "KF00001",
    #         "app_code_biz": "KF00002"
    #     }
    # }
    # res = Requests().send_post(url=url, data=data, headers=headers)
    # print(res.json())
    url = 'http://10.0.34.13:10007/kube/v1/api/helmChart/import'
    headers = {
        'Authorization': 'Bearer d536d274-5b6c-4c4a-bba4-10622b6c8bbd'
    }
    import os
    from common.setting import upload_file

    file = {
        "file": open(r'G:\pytest_auto_uitest_apitest\data\gitea-1.9.1.tgz', 'rb'),
    }
    res = Requests().send_request(url=url, method='post', parametric_key='json', headers=headers, file=file, data=None)
    print(res.json())
