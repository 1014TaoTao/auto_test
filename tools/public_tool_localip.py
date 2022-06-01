#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/3/20 15:36
@Author  : ZhangTAO
@File    : public_tool_localip.py
@Software: PyCharm
"""
import socket


# 获取本机ip
def get_host_ip() -> str:
    """
    查询本机ip地址
    :return:
    """
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# if __name__ == '__main__':
#     print(get_host_ip())
