#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/24 15:15
@Author  : ZhangTAO
@File    : demo.py
@Software: PyCharm
"""
import math

resp = {'code': 200, 'body': {'code': 1, 'msg': '成功', 'data': {'total': 1, 'list': [{'id': 9, 'name': 'Beijing-node-06', 'code': 'KN000009', 'userName': 'root', 'specData': {'vendor': 'Intel', 'cpuModel': 'Xeon', 'cpuSpeed': '3.00GHz', 'cpuCores': 64.0, 'memory': '252GB', 'disk': '300.0GB', 'os': 'CentOS 7.6.1810 3.10.0-1062.12.1.el7.x86_64'}, 'ip': '192.168.0.35', 'monitorUrl': 'http://192.168.0.30:30090', 'linkClusterId': 3, 'linkClusterName': 'Beijing-cluster-01', 'monitorStatus': 3, 'status': 2, 'enableFlag': 1, 'tenantId': None, 'createUser': None, 'updateUser': None}]}, 'ext': {}}, 'text': '{"code":1,"msg":"成功","data":{"total":1,"list":[{"id":9,"name":"Beijing-node-06","code":"KN000009","userName":"root","specData":{"vendor":"Intel","cpuModel":"Xeon","cpuSpeed":"3.00GHz","cpuCores":64.0,"memory":"252GB","disk":"300.0GB","os":"CentOS 7.6.1810 3.10.0-1062.12.1.el7.x86_64"},"ip":"192.168.0.35","monitorUrl":"http://192.168.0.30:30090","linkClusterId":3,"linkClusterName":"Beijing-cluster-01","monitorStatus":3,"status":2,"enableFlag":1,"tenantId":null,"createUser":null,"updateUser":null}]},"ext":{}}', 'time_consuming': 72.999, 'time_total': 0.072999, 'headers': {'Server': 'nginx/1.17.0', 'Date': 'Mon, 21 Feb 2022 13:53:06 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0', 'X-Frame-Options': 'DENY', 'Referrer-Policy': 'no-referrer', 'Content-Encoding': 'gzip'}}
list_01 = "['list'][0]['id']"
# print(list_01)
print(resp['body']['data'].get(eval(list_01)))
# for i in resp['body']['data']['list'][0]['id']:
#     print(i)
# for case_info in list_01:
#     # print(case_info)
#     print(resp['body']['data']['list'])
#     # print(resp['body']['data'])
#     math.val