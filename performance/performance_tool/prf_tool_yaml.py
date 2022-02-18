# coding:utf-8
from string import Template

import yaml

from common import setting
from performance.performance_tool.config import params
from tools.public_tool_log import logger

logger = logger(setting.PRF_LOG_PATH)

class YamlPack:
    # yaml文件全部内容
    def __init__(self):
        self.yaml_path = setting.PRF_YAML_PATH
        # 读取yaml内容
        with open(self.yaml_path, encoding="utf-8") as f:
            re = Template(f.read()).substitute(params)
            yaml.safe_load(re)

    # Test目录下的全部用例
    def get_case(self):
        test_list = []
        with open(self.yaml_path, encoding="utf-8") as f:
            re = Template(f.read()).substitute(params)
            data = yaml.safe_load(re)
        case = data["Case"]
        for a in case:
            for k, v in a.items():
                if k == "Test":
                    test_list.append(v)
        return test_list

    # 获取用例名称
    def get_case_name(self):
        data = self.get_case()
        url_li = []
        for i in data:
            if "name" not in i.keys():
                i["name"] = "NULL"
            for k, v in i.items():
                if "name" == k:
                    url_li.append(v)
        return url_li

    # 获取请求方式
    def get_method(self):
        data = self.get_case()
        method_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "method":
                    method_li.append(v)
        return method_li

    # 获取请求地址
    def get_url(self):
        data = self.get_case()
        url_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "URL":
                    url_li.append(v)
        return url_li

    # 获取请求headers信息
    def get_headers(self):
        data = self.get_case()
        headers_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "headers":
                    headers_li.append(v)
        return headers_li

    # 获取请求参数
    def get_data(self):
        data = self.get_case()
        params_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "data":
                    params_li.append(v)
        return params_li

    # 获取验证全部内容
    def get_expected(self):
        data = self.get_case()
        validate_li = []
        for i in data:

            re = i["expected"]
            validate_li.append(re)
        return validate_li

    # 列表转为字典dict(zip(list1,list2))
    def test_data(self):
        name = self.get_case_name()
        method = self.get_method()
        url = self.get_url()
        headers = self.get_headers()
        data = self.get_data()
        validate = self.get_expected()

        all_data = [(a, b, c, d, e, f) for a, b, c, d, e, f in
                zip(name, method, url, headers, data, validate)]  # 长度相同的几个列表组合成一个
        return all_data


if __name__ == '__main__':
    G = YamlPack()

    print(G.get_case())
