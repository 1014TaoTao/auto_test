#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 9:11
@Author  : ZhangTAO
@File    : build.py
@Software: PyCharm
"""
import os

base_path = os.path.dirname(os.path.abspath(__file__))

ico_path = os.path.join(base_path, "../ico", "favico.ico")

os.system(f'pyinstaller -D -w -i  {ico_path} main.py')
# os.system(f'pyinstaller api_main.py')
