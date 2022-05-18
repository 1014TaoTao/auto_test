# -*- coding: utf-8 -*-
'''
@Time    : 2022/5/16 15:18
@Author  : ranxiaomin
@File    : dataWarehouse.py
@Software: PyCharm
'''

from tools.api_tool_request import Requests

# 获取token
def get_token(base_url: str, headers: dict)-> str:
    url = f'{base_url}/uaa/oauth/token'
    data = {
        "mobile": '18603015137',
        "password": '737cec5e3ca2a2fb367fbedf4965fbc6',
        "account_type": 'mobile',
        "grant_type":'password',
        "scope":'trust',
        "client_secret":'2c27867ba8b35dedbde7361f8ffb704d',
        "client_id":'saas_cp'
    }
    res = Requests().send_request(url=url, method='get', parametric_key='params', headers=headers, data=data,
                                  file=None, )
    token = res.json()['access_token']
    print(token)
    return token
if __name__ == '__main__':
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    base_url = 'http://192.168.0.197:18603'
    token=get_token(base_url, headers)
    print(token)