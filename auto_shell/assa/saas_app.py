#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 10:12
@Author  : ZhangTAO
@File    : saas_app.py
@Software: PyCharm
"""
"""
应用管理-查询应用下线状态，并改为上线状态
"""

from tools.api_tool_request import Requests

down_app_data = {}


# saas应用中心-应用管理 根据应用id查询应用
def query_app(base_url: str, id: int, headers: dict) -> list:
    # 查询kube下线应用
    url = f'{base_url}/uaa/v1/api/app'
    data = {
        # "id": 2500,
        "id": id,
        "pageSize": 10,
        "pageNo": 1,
    }
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    data_list = res.json()['data']['list']
    return data_list


# saas应用中心-应用管理 查询kube下线应用
def query_down_app(data_list: list) -> dict:
    # 查询kube下线应用
    for i in data_list:
        # 0为下线状态，1为上线状态
        if i['enableFlag'] == 0:
            down_app_data[i['id']] = i['name']
        if 'children' in i.keys():
            query_down_app(i['children'])
    return down_app_data


# saas应用中心-应用管理 单个应用下线
def single_down_app(base_url: str, app_id: int, headers: dict) -> str:
    url = f'{base_url}/uaa/v1/api/app/{app_id}/enable'
    data = {
        "enableFlag": 0,
    }
    res = Requests().send_request(url=url, method='patch', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    print(f"{app_id} 应用下线成功 \n")
    return res.json()


# saas应用中心-应用管理 单个应用上线
def single_up_app(base_url: str, app_id: int, headers: dict) -> str:
    url = f'{base_url}/uaa/v1/api/app/{app_id}/enable'
    data = {
        "enableFlag": 1,
    }
    res = Requests().send_request(url=url, method='patch', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    print(f"{app_id} 应用下线成功 \n")
    return res.json()


# saas应用中心-应用管理 单个应用下线
def some_down_app(base_url: str, down_dict: dict, headers: dict):
    for app_id in down_dict.keys():
        single_down_app(base_url, app_id, headers)


# saas应用中心-应用管理 单个应用上线
def some_up_app(base_url: str, down_dict: dict, headers: dict):
    for app_id in down_dict.keys():
        single_up_app(base_url, app_id, headers)


if __name__ == '__main__':
    headers = {
        'Authorization': 'Bearer e24ff395-ff7c-4802-9a17-9e9cdcd0602e'
    }
    base_url = 'http://10.0.34.13:10000'
    id = 2500
    # 查询id为2500应用下所有的已下线应用
    print(query_down_app(query_app(base_url, id, headers)))

    # down_dict = query_down_app(query_app(base_url, id, headers))
    # some_up_app(base_url, down_dict, headers)
