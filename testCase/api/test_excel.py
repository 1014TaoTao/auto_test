# coding:utf-8

from typing import Union, List, Dict, Tuple, Any

import allure
import pytest

from common import setting, consts
from tools.common_tools.api_tool_login import Login
from tools.excel_tools.api_tool_excel import ExcelPack
from tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


def run_setup() -> list:
    """
    :return:
    """
    with allure.step("token执行初始化"):
        TESTCASEPATH: str = consts.TESTCASEPATH
        APIHOST: str = consts.API_HOST

        try:
            Login().api_login()
        except Exception as e:
            logger.error(f"【登录写入token异常：{e}】")
        result = ExcelPack(file_name=TESTCASEPATH,
                           sheet_id=setting.sheet_id).run_excel_case(APIHOST)
        return result


@allure.description("excel接口测试")  # 项目描述
@allure.link(url="https://njqa.zgyjyx.net/api", name="allure.link：超链接")  # 项目地址
# bug链接
@allure.issue(url="https://njqa.zgyjyx.net/api", name='allure.issue：BUG地址')
# 测试用例地址
@allure.testcase(url="https://njqa.zgyjyx.net/api", name='allure.testcase：测试用例地址')
@allure.feature("feature一级标签:excel接口测试")  # 一级标签
@allure.story("story二级标签:excel接口测试")  # 二级标签
@allure.title("excel接口测试")  # 用例标题
class TestExcel:
    @pytest.mark.parametrize('args', run_setup())
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.epic('excel接口测试')
    def test_excel(self, args):
        """
        :param args:
        :return:
        """
        allure.dynamic.description(
            f"{str(args['title'])} {str(args['method'])} {str(args['url'])}")
        allure.dynamic.title(str(args['title']))
        with allure.step(u"测试结果：{0}".format(str(args['result']))):
            allure.attach(u"测试结果：{0}".format(str(args['result'])), "测试结果")

        with allure.step(u"用例名称：{0}".format(str(args['title']))):
            allure.attach(u"用例名称：{0}".format(str(args['title'])), "用例名称")

        with allure.step(u"请求方式：{0}".format(str(args['method']))):
            allure.attach(u"请求方式：{0}".format(str(args['method'])), "请求方式")

        with allure.step(u"请求地址：{0}".format(str(args['url']))):
            allure.attach(u"请求地址：{0}".format(str(args['url'])), "请求地址")

        with allure.step(u"请求头 ：{0}".format(str(args['headers']))):
            allure.attach(u"请求头 ：{0}".format(str(args['headers'])), "请求头")

        with allure.step(u"请求参数：{0}".format(str(args['data']))):
            allure.attach(u"请求参数：{0}".format(str(args['data'])), "请求参数")

        with allure.step(u"请求断言：{0}".format(str(args['status_code']))):
            allure.attach(u"请求断言：{0}".format(
                str(args['status_code'])), "code请求断言")

        with allure.step(u"请求断言：{0}".format(str(args['expected_msg']))):
            allure.attach(u"请求断言：{0}".format(
                str(args['expected_msg'])), "msg请求断言")

        with allure.step(u"请求断言：{0}".format(str(args['expected_data']))):
            allure.attach(u"请求断言：{0}".format(
                str(args['expected_data'])), "data请求断言")

        with allure.step(u"响应结果：{0}".format(str(args['res']))):
            allure.attach(u"响应结果：{0}".format(str(args['res'])), "响应结果")

        with allure.step("断言"):
            assert args["result"] == "pass"
