#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
@Time    : 2022/3/16 15:36
@Author  : ZhangTAO
@File    : yaml_read.py
@Software: PyCharm
"""
from string import Template

import yaml

from common import setting
from common.readConfigIni import Config
from tools.common_tools.api_tool_headers import read_token


class YamlPack:
    # yaml文件全部内容
    def __init__(self):
        variable = {
            'host': Config(setting.CONFIG_INI).apihost_43_13,
            'token': read_token()
        }
        self.yaml_path = setting.PER_YAML_PATH
        with open(self.yaml_path, encoding="utf-8") as f:
            re = Template(f.read()).substitute(variable)
            self.data = yaml.safe_load(re)

    # Test目录下的全部用例
    def _get_case(self) -> list:
        test_list = []
        case = self.data["Case"]
        for a in case:
            for k, v in a.items():
                if k == "Test":
                    test_list.append(v)
        return test_list

    # 获取用例名称
    def _get_case_name(self) -> list:
        data = self._get_case()
        url_li = []
        for i in data:
            if "name" not in i.keys():
                i["name"] = "NULL"
            for k, v in i.items():
                if "name" == k:
                    url_li.append(v)
        return url_li

    # 获取请求方式
    def _get_method(self) -> list:
        data = self._get_case()
        method_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "method":
                    method_li.append(v)
        return method_li

    # 获取请求地址
    def _get_url(self) -> list:
        data = self._get_case()
        url_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "url":
                    url_li.append(v)
        return url_li

    # 获取请求headers信息
    def _get_headers(self) -> list:
        data = self._get_case()
        headers_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "headers":
                    headers_li.append(v)
        return headers_li

    # 获取请求参数
    def _get_data(self) -> list:
        data = self._get_case()
        params_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "data":
                    params_li.append(v)
        return params_li

    # 获取验证全部内容
    def _get_expected(self) -> list:
        data = self._get_case()
        validate_li = []
        for i in data:
            re = i["expected"]
            validate_li.append(re)
        return validate_li

    # 列表转为字典dict(zip(list1,list2))
    def test_data(self) -> list:
        name = self._get_case_name()
        method = self._get_method()
        url = self._get_url()
        headers = self._get_headers()
        data = self._get_data()
        expected = self._get_expected()
        all_data = [dict(zip(['name', 'method', 'url', 'headers', 'data', 'expected'], [a, b, c, d, e, f])) for
                    a, b, c, d, e, f in
                    zip(name, method, url, headers, data, expected)]  # 长度相同的几个列表组合成一个

        return all_data

# if __name__ == '__main__':
#
#     G = YamlPack()
#
#     print(G.test_data())
