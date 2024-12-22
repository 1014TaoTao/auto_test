# coding:utf-8
import yaml

from common import setting
from tools.logi_tool import logger
from tools.api_tool_request import Requests


class YamlPack:
    # yaml文件全部内容
    def __init__(self):
        self.logger = logger(setting.API_LOG_PATH)
        self.pass_num = 0
        self.fail_num = 0
        self.yaml_path = setting.API_YAML_PATH
        # 读取yaml内容
        with open(self.yaml_path, 'rb') as f:
            yaml.safe_load(f)

    # Test目录下的全部用例
    def get_case(self) -> list:
        """
        :return:
        """
        test_list = []
        with open(self.yaml_path, 'rb') as f:
            data = yaml.safe_load(f)
        case = data["Case"]
        for a in case:
            for k, v in a.items():
                if k == "Test":
                    test_list.append(v)
        return test_list

    # 获取用例名称
    def get_case_name(self) -> list:
        """
        :return:
        """
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
    def get_method(self) -> list:
        """
        :return:
        """
        data = self.get_case()
        method_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "method":
                    method_li.append(v)
        return method_li

    # 获取请求地址
    def get_url(self) -> list:
        """
        :return:
        """
        data = self.get_case()
        url_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "URL":
                    url_li.append(v)
        return url_li

    # 获取请求headers信息
    def get_headers(self) -> list:
        """
        :return:
        """
        data = self.get_case()
        headers_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "headers":
                    headers_li.append(v)
        return headers_li

    # 获取请求参数
    def get_data(self) -> list:
        """
        :return:
        """
        data = self.get_case()
        params_li = []
        for i in data:
            re = i["request"]
            for k, v in re.items():
                if k == "data":
                    params_li.append(v)
        return params_li

    # 获取验证全部内容
    def get_expected(self) -> list:
        """
        :return:
        """
        data = self.get_case()
        validate_li = []
        for i in data:
            re = i["expected"]
            validate_li.append(re)
        return validate_li

    # 列表转为字典dict(zip(list1,list2))
    def test_data(self) -> list:
        """
        :return:
        """
        name = self.get_case_name()
        method = self.get_method()
        url = self.get_url()
        headers = self.get_headers()
        data = self.get_data()
        validate = self.get_expected()

        all_data = [(a, b, c, d, e, f) for a, b, c, d, e, f in
                    zip(name, method, url, headers, data, validate)]  # 长度相同的几个列表组合成一个
        return all_data

    def req_yaml(self) -> list:
        """
        :return:
        """
        global set_case
        all_case = []
        for i in self.get_case():
            case_name = i["name"]
            method = i["request"]["method"]
            url = i["request"]["url"]
            headers = i["request"]["headers"]
            data = i["request"]["params"]
            expected = i["expected"]

            # 发请求
            self.logger.info(f"【测试用例：{case_name}】===============>> 【start】")
            res = Requests().send_request(url=url, method=method, data=data, headers=headers)

            ex = str(expected).replace("{", "").replace("}", "")
            # print(ex)
            if ex in str(res):  # 写是否通过
                self.logger.info(
                    f"【断言SUCCESS】期望结果: (%s) 【in】 实际结果: (%s)" % (ex, res))
                self.logger.info(f"【实际响应结果输出完成：(%s)】" % res)
                self.logger.info(
                    f"【测试用例：{case_name}】===============>> 【PASS！】\n")
                self.pass_num += 1
                result = "pass"
            else:
                self.logger.error(
                    f"【断言FAIL】期望结果: (%s) 【not in】 实际结果: (%s)" % (ex, res))
                self.logger.info(f"【实际响应结果输出完成：(%s)】" % res)
                self.logger.info(
                    f"【测试用例：{case_name}】===============>> 【FAIL！】\n")
                self.fail_num += 1
                result = "fail"

            set_case = {
                "result": result,
                "title": case_name,
                "method": method,
                "url": url,
                "headers": headers,
                "data": data,
                "expected": expected,
                "res": res
            }
            all_case.append(set_case)

        all_num = self.pass_num + self.fail_num
        # round四舍五入函数
        success_rate = round(self.pass_num / all_num, 3) * 100
        failure_rate = round(self.fail_num / all_num, 3) * 100

        res_str = f"【本次共执行{all_num}条用例】-【测试通过的有{self.pass_num}条】-【测试失败的有{self.fail_num}条】-【成功率为{success_rate}%】-【失败率为{failure_rate}%】"
        self.logger.info(f"【本次测试的测试结果为:{res_str}】\n")

        return all_case

# if __name__ == '__main__':
#     G = YamlPack()
#     print(G.req_yaml())
