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
    'Authorization': 'Bearer 03f4369f-fccf-43f4-a7e8-bda282f84569'
}


# 用户组查询 user_group_name=kube\SAAS 一般数据绑定
def query_user_group_id_list(base_url: str, user_group_name_list: list) -> list:
    print("查用用户组列表，返回用户组列表id")
    # 查询kube下线应用
    group_id_list = []
    for user_group_name in user_group_name_list:
        url = f'{base_url}/am/v1/api/group'
        data = {
            "pageNo": 1,
            "pageSize": 100,
            "name": user_group_name
        }
        res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                      file=None, )
        if res.json()['msg'] != '未经授权的访问':
            for user_group_id in res.json()['data']['list']:
                group_id_list.append(user_group_id['id'])
        else:
            print(res.json()['msg'])
    return group_id_list


# 关联用户-按用户-查找用户
def get_user_id_list(base_url: str, group_id_list: list, user_name: str) -> list:
    print("关联用户-按用户-查找用户：获取用户列表id")
    global user_id
    user_id_list = []
    for group_id in group_id_list:
        url = f'{base_url}/am/v1/api/group/user/list/{group_id}'
        # tenantId为1时指的是选中状态
        data = {
            "pageNo": 1,
            "pageSize": 100,
            "tenantId": 1,
            "searchContent": user_name
        }
        res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                      file=None, )
        if res.json()['msg'] != '未经授权的访问':
            if res.json()['data']['list'][0]['name'] == user_name:
                user_id = res.json()['data']['list'][0]['id']
                user_id_list.append(user_id)
            else:
                print(f'关联用户-按用户-查找用户，没有找到该用户：{user_name}')
        else:
            print(res.json()['msg'])
    return user_id_list


# 关联用户-按用户-绑定用户
def bind_user_id(base_url: str, group_id_list: list, user_id_list: list):
    url = f'{base_url}/am/v1/api/group/user/batch'
    group_id_user_id = dict(zip(group_id_list, user_id_list))
    num = 0
    for group_id, user_id in group_id_user_id.items():
        data = [{"groupId": group_id, "tenantId": 1, "userId": user_id}]
        res = Requests().send_request(url=url, method='post', parametric_key='json', headers=headers, data=data,
                                      file=None, )
        num += 1
        print(f"=============={num}=================")
        print(res.json())
