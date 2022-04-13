#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/12 23:45
@Author  : ZhangTAO
@File    : saas_user_group.py
@Software: PyCharm
"""
"""
用户中心-用户组管理-管理用户

"""

from tools.api_tool_request import Requests

headers = {
    'Authorization': 'Bearer a5ba080f-b309-4830-adfb-126d3a8c423f'
}


# 用户组查询 user_group_name=kube\SAAS 一般数据绑定
def query_user_group(base_url: str, user_group_name: str) -> int:
    # 查询kube下线应用
    url = f'{base_url}/am/v1/api/group'
    data = {
        "pageNo": 1,
        "pageSize": 10,
        "name": user_group_name
    }
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    for i in res.json()['data']['list']:
        role_id = i['id']
        return role_id
