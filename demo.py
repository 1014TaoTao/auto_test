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

resp = {'code': 200, 'body': {'code': 1, 'msg': '成功', 'data': {'total': 1, 'list': [
    {'id': 9, 'name': 'Beijing-node-06', 'code': 'KN000009', 'userName': 'root',
     'specData': {'vendor': 'Intel', 'cpuModel': 'Xeon', 'cpuSpeed': '3.00GHz', 'cpuCores': 64.0, 'memory': '252GB',
                  'disk': '300.0GB', 'os': 'CentOS 7.6.1810 3.10.0-1062.12.1.el7.x86_64'}, 'ip': '192.168.0.35',
     'monitorUrl': 'http://192.168.0.30:30090', 'linkClusterId': 3, 'linkClusterName': 'Beijing-cluster-01',
     'monitorStatus': 3, 'status': 2, 'enableFlag': 1, 'tenantId': None, 'createUser': None, 'updateUser': None}]},
                              'ext': {}},
        'text': '{"code":1,"msg":"成功","data":{"total":1,"list":[{"id":9,"name":"Beijing-node-06","code":"KN000009","userName":"root","specData":{"vendor":"Intel","cpuModel":"Xeon","cpuSpeed":"3.00GHz","cpuCores":64.0,"memory":"252GB","disk":"300.0GB","os":"CentOS 7.6.1810 3.10.0-1062.12.1.el7.x86_64"},"ip":"192.168.0.35","monitorUrl":"http://192.168.0.30:30090","linkClusterId":3,"linkClusterName":"Beijing-cluster-01","monitorStatus":3,"status":2,"enableFlag":1,"tenantId":null,"createUser":null,"updateUser":null}]},"ext":{}}',
        'time_consuming': 72.999, 'time_total': 0.072999,
        'headers': {'Server': 'nginx/1.17.0', 'Date': 'Mon, 21 Feb 2022 13:53:06 GMT',
                    'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked',
                    'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'X-Content-Type-Options': 'nosniff',
                    'X-XSS-Protection': '1; mode=block',
                    'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache',
                    'Expires': '0', 'X-Frame-Options': 'DENY', 'Referrer-Policy': 'no-referrer',
                    'Content-Encoding': 'gzip'}}

# str_list_01 = 'list'
# str_list_02 = 'id'

# print(resp['body']['data'][str_list_01][0][str_list_02])
# json_resp = json.dumps(resp)
json_resp = str(resp['body'])
# print(json_resp)
# print(type(json_resp))
try:
    str_info = 'id '
    value = re.search(f'{str_info:}.*?(?=,)', json_resp).group().replace(f"{str_info}", "").replace("': ", "")
    print(value)
except:
    print("匹配失败")

# code=re.findall('code":(.*?),"message',r2.text)#r2.text是需要提取的数据
# code=re.findall('id":(.+?),"schoolId',r2.text)#注意这里是用(.+?),中间省略的内容用.+?代替


# # 通过正则获取"id":value列表
# datalist = re.findall(r'\"id\":.*?(?=,)', data)
