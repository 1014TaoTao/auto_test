#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
Created on:2020/4/1310:50
@author:
"""
import os, random, requests
from requests_toolbelt import MultipartEncoder
from base.get_token import GetToken
from base.get_params import GetParams
from config.config import Config
from utils.Request import Request
from base.consts import PROJECT_NAME


class Upload():

    expected_code = int(Config().get_conf('assertCode', 'success_code'))

    def operate_header(self,loginHost=None):
        """
        重新处理头部
        :param key:
        :return:
        """
        if loginHost is None:
            loginHost_t = Config().loginHost_user
        else:
            loginHost_t = loginHost

        GetToken().generate_token(loginHost_t)
        token = GetToken().get_token()

        headers = {'Content-Type': 'multipart/form-data;boundary=---------------------------40330817512826770152245118989'}
        headers['Authorization'] = token
        return headers

    def uploadImg(self, url, appBiz, appCode, tenantId, path, img_path, img_name):
        """
        :param img_path:图片的路径
        :param img_name:图片的名称
        """
        #获取项目根目录
        project_name = PROJECT_NAME
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find(project_name) + len(project_name)]

        headers = Upload().operate_header()
        # 生成可用于multipart/form-data上传的数据
        files = MultipartEncoder(
            fields={"appBiz": (None, appBiz), "appCode": (None, appCode), "tenantId": (None, tenantId),
                    "path": (None, path),
                    "file": (img_name, open(rootPath + img_path + img_name, "rb"), 'application/octet-stream')},
            boundary='---------------------------40330817512826770152245118989')
        res = Request().post_request(url=url, header=headers, data=files)
        return res


    def uploadFile(self, url, file_name, file_path):

        headers = Upload().operate_header()

        #获取项目根目录
        project_name = PROJECT_NAME
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find(project_name) + len(project_name)]

        # 生成可用于multipart/form-data上传的数据
        files = MultipartEncoder(
            fields={"file": (file_name, open(rootPath + file_path + file_name, "rb"), 'application/octet-stream')},
            boundary='---------------------------40330817512826770152245118989')
        res = Request().post_request(url=url, header=headers, data=files)
        return res


if __name__ == '__main__':
    url = "http://192.168.0.115:18603/drone3d/v1/drone3dfile/importLatitudeAndLongitude"
    u = Upload()
    res = u.uploadFile(url=url, file_path="/params/file/", file_name="导入坐标(经纬度)Excel模板(1).xlsx")
    print(res)
