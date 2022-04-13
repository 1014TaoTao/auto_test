#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 22:34
@Author  : ZhangTAO
@File    : saas_role.py
@Software: PyCharm
"""
"""
用户中心-角色管理-角色授权

"""
from tools.api_tool_request import Requests

headers = {
    'Authorization': 'Bearer 5e319bec-9d82-440b-93d5-612ca3e5a29d'
}


# 角色查询
# saas用户中心-用户管理 根据用户名称查询应用
def query_role_id(base_url: str) -> int:
    # 查询kube下线应用
    url = f'{base_url}/uaa/v1/api/role'
    data = {
        "pageNo": 1,
        "pageSize": 10,
        "appId": 2500,
        "name": "kube管理员"
    }
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    if res.json()['msg'] != '未经授权的访问':
        for i in res.json()['data']['list']:
            role_id = i['id']
            return role_id
    else:
        return res.json()['msg']


# 获取分配菜单
def get_role_menu_tree(base_url: str, role_id: int) -> list:
    url = f'{base_url}/uaa/v1/api/role/{role_id}/func/tree'

    res = Requests().send_request(url=url, method='get', parametric_key='json', headers=headers, data=None,
                                  file=None, )
    menu_data_list = res.json()['data']
    return menu_data_list


# 递归获取角色的id添加到列表
menu_id_list = []


def get_role_menu_tree_id_list(menu_data_list: list):
    for i in menu_data_list:
        menu_id_list.append(i['id'])
        if 'children' in i.keys():
            get_role_menu_tree_id_list(i['children'])

    return menu_id_list


# 分配菜单功能
def commit_role_menu(base_url: str, role_id: int, menu_id_list: list):
    url = f'{base_url}/uaa/v1/api/role/{role_id}/func'

    res = Requests().send_request(url=url, method='post', parametric_key='json', headers=headers, data=menu_id_list,
                                  file=None, )
    return res.json()
