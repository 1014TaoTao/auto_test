#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/24 15:15
@Author  : ZhangTAO
@File    : demo.py
@Software: PyCharm
"""
import json
import re

resp = {"code": 1, "msg": "成功",
        "data": {"id": 4164, "name": "消息中心", "label": "消息中心", "authFlag": 1, "type": 1, "funcType": 1,
                 "funcCategory": -1, "code": "message_center_tenant", "url": "http://192.168.0.115:20012",
                 "icon": "icon-xiaoxi300", "sequence": 195, "tags": "", "children": [
                {"id": 7547, "name": "公告管理", "label": "公告管理", "authFlag": 1, "type": 2, "funcType": 2,
                 "funcCategory": -1, "code": "announcement_management", "url": "/notice", "icon": "", "sequence": 199,
                 "tags": "", "children": [
                    {"id": 7548, "name": "查看公告", "label": "查看公告", "authFlag": 1, "type": 2, "funcType": 2,
                     "funcCategory": -1, "code": "view_announcement_management", "url": "/check-notice", "icon": "",
                     "sequence": 200, "tags": "", "children": [
                        {"id": 7550, "name": "公告详情", "label": "公告详情", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "detail_view_announcement", "url": "", "icon": "", "sequence": 200,
                         "tags": ""}]},
                    {"id": 7549, "name": "发布公告", "label": "发布公告", "authFlag": 1, "type": 2, "funcType": 2,
                     "funcCategory": -1, "code": "publish_announcement_management", "url": "/send-notice", "icon": "",
                     "sequence": 199, "tags": "", "children": [
                        {"id": 7552, "name": "新建公告", "label": "新建", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "add_publish_announcement", "url": "", "icon": "", "sequence": 200,
                         "tags": ""},
                        {"id": 7553, "name": "修改公告", "label": "修改", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "update_publish_announcement", "url": "", "icon": "",
                         "sequence": 199, "tags": ""},
                        {"id": 7551, "name": "公告详情", "label": "公告详情", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "detail_publish_announcement", "url": "", "icon": "",
                         "sequence": 198, "tags": ""},
                        {"id": 7554, "name": "上下线公告", "label": "发布,下线", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "on-offline_publish_announcement", "url": "", "icon": "",
                         "sequence": 197, "tags": ""},
                        {"id": 7645, "name": "删除公告", "label": "删除", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "del_publish_announcement", "url": "", "icon": "", "sequence": 1,
                         "tags": ""}]}]},
                {"id": 4299, "name": "消息管理", "label": "消息管理", "authFlag": 1, "type": 2, "funcType": 2,
                 "funcCategory": -1, "code": "message_management_menu_tenant", "url": "/news",
                 "icon": "icon-shuxingchaxun", "sequence": 199, "tags": "", "children": [
                    {"id": 7537, "name": "我的消息", "label": "我的消息", "authFlag": 1, "type": 2, "funcType": 2,
                     "funcCategory": -1, "code": "my_message_management", "url": "/total", "icon": "", "sequence": 200,
                     "tags": "", "children": [
                        {"id": 7539, "name": "全部消息tab", "label": "全部消息", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "all_my_message", "url": "", "icon": "", "sequence": 200,
                         "tags": ""},
                        {"id": 7540, "name": "未读消息tab", "label": "未读消息", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "unread_my_message", "url": "/unread", "icon": "", "sequence": 199,
                         "tags": ""},
                        {"id": 7541, "name": "已读消息tab", "label": "已读消息", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "read_my_message", "url": "/read", "icon": "", "sequence": 198,
                         "tags": ""},
                        {"id": 7542, "name": "标记已读", "label": "标记已读", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "mark_read_my_message", "url": "", "icon": "", "sequence": 197,
                         "tags": ""},
                        {"id": 7543, "name": "删除消息", "label": "删除", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "del_my_message", "url": "", "icon": "", "sequence": 196,
                         "tags": ""}]},
                    {"id": 7538, "name": "发送消息", "label": "发送消息", "authFlag": 1, "type": 2, "funcType": 2,
                     "funcCategory": -1, "code": "send_message_management", "url": "/manager", "icon": "",
                     "sequence": 199, "tags": "", "children": [
                        {"id": 7544, "name": "新建消息", "label": "新建", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "add_message_send", "url": "", "icon": "", "sequence": 200,
                         "tags": ""},
                        {"id": 7546, "name": "消息详情", "label": "消息详情", "authFlag": 1, "type": 3, "funcType": 3,
                         "funcCategory": -1, "code": "detail_message_send", "url": "", "icon": "", "sequence": 198,
                         "tags": ""}]}]}]}}

# str_list_01 = 'list'
# str_list_02 = 'id'

# print(resp['body']['data'][str_list_01][0][str_list_02])
# json_resp = json.dumps(resp)
json_resp = str(resp)
# print(json_resp)
# print(type(json_resp))
try:
    str_info = r'children": [{"id'
    value = re.search(f'{str_info:}.*?(?=,)', json_resp).group().replace(f"{str_info}", "").replace("': ", "")
    print(value)
except:
    print("匹配失败")

# code=re.findall('code":(.*?),"message',r2.text)#r2.text是需要提取的数据
# code=re.findall('id":(.+?),"schoolId',r2.text)#注意这里是用(.+?),中间省略的内容用.+?代替


# # 通过正则获取"id":value列表
# datalist = re.findall(r'\"id\":.*?(?=,)', data)
