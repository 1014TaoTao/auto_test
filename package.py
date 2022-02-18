#!/usr/bin/python3
# coding=utf-8
import os

# 判断是否安装requests
try:
    import requests

    print("已检测到requests模块,无需安装OK...")
except:
    print("未检测到requests模块，现在开始安装......")
    os.system('pip install requests')

# 判断是否安装openpyxl
try:
    import openpyxl

    print("已检测到openpyxl模块,无需安装OK...")
except:
    print("未检测到openpyxl模块，现在开始安装......")
    os.system('pip install openpyxl')

# 判断是否安装configparser
try:
    import configparser

    print("已检测到configparser模块,无需安装OK...")
except:
    print("未检测到configparser模块，现在开始安装......")
    os.system('pip install configparser')
