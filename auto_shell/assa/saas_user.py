#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 18:05
@Author  : ZhangTAO
@File    : saas_user.py
@Software: PyCharm
"""
"""
用户授权

"""
from tools.requests_tools.api_tool_request import Requests


# saas用户中心-用户管理 根据用户名称查询应用
def query_user_list(base_url: str, user_name: str, headers: dict) -> int:
    # 查询kube下线应用
    url = f'{base_url}/am/v1/api/user'
    data = {
        "pageNo": 1,
        "pageSize": 10,
        "type": 2,
        "search": "orgUsers",
        "name": user_name
    }
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    if res.json()['data']['list'][0]['name'] == user_name:
        user_id = res.json()['data']['list'][0]['id']
        return user_id


# saas用户中心-用户管理-授权 获取授权列表
def get_auth_user_list(base_url: str, user_id: int, headers: dict) -> list:
    # 查询kube下线应用
    url = f'{base_url}/uaa/v1/api/role/user/{user_id}/assign'
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=None,
                                  file=None, )
    auth_id_list = []
    for i in res.json()['data']:
        auth_id_list.append(i.get('id'))
    return auth_id_list


# saas用户中心-用户管理-授权 取消授权
def cancel_auth_user_list(base_url: str, auth_id_list: list, user_id: int, headers: dict):
    # 查询kube下线应用
    url = f'{base_url}/uaa/v1/api/role/user/{user_id}'
    data = auth_id_list
    res = Requests().send_request(url=url, method='post', parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()


# saas用户中心-用户管理-授权 确认授权
def confirm_auth_user_list(base_url: str, auth_id_list: list, user_id: int, headers: dict):
    # 查询kube下线应用
    url = f'{base_url}/uaa/v1/api/role/user/{user_id}'
    data = auth_id_list
    res = Requests().send_request(url=url, method='post', parametric_key='json', headers=headers, data=data,
                                  file=None, )
    return res.json()



