#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/13 16:43
@Author  : ZhangTAO
@File    : saas_main.py
@Software: PyCharm
"""
import saas_app
import saas_user
import saas_role
import saas_user_group

# 批量上线

headers = {
    'Authorization': 'Bearer e24ff395-ff7c-4802-9a17-9e9cdcd0602e'
}
base_url = 'http://10.0.34.13:10000'
id = 2500
user_name = '张涛'
user_group_name_list = ['SAAS', 'kube']


# 查询id为2500应用下所有的已下线应用
down_dict = saas_app.query_down_app(saas_app.query_app(base_url, id, headers))
# 批量上线
saas_app.some_up_app(base_url, down_dict, headers)


# 获取用户id
user_id = saas_user.query_user_list(base_url, user_name, headers)
# 授权列表id
auth_id_list = saas_user.get_auth_user_list(base_url, user_id, headers)
# 执行用户批量授权
saas_user.confirm_auth_user_list(base_url, auth_id_list, user_id, headers)


# 角色id查询
role_id = saas_role.query_role_id(base_url)
# 分配菜单列表
menu_data_list = saas_role.get_role_menu_tree(base_url, role_id)
# 分配菜单id列表
menu_id_list = saas_role.get_role_menu_tree_id_list(menu_data_list)
# 提交分配菜单
saas_role.commit_role_menu(base_url, role_id, menu_id_list)


# 用户组id列表
group_id_list = saas_user_group.query_user_group_id_list(base_url, user_group_name_list)
# 用户id列表
user_id_list = saas_user_group.get_user_id_list(base_url, group_id_list, user_name)
# 批量用户组关联用户
saas_user_group.bind_user_id(base_url, group_id_list, user_id_list)