# coding:utf-8

import allure
import pytest

from common import setting, consts
from tools.excel_tools.api_tool_excel import ExcelPack
from tools.common_tools.api_tool_login import Login
from tools.logs_tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


def run_setup():
    """
    :return:
    """
    with allure.step("token执行初始化"):
        TESTCASEPATH = consts.TESTCASEPATH
        BASEHOST = consts.BASEHOST
        LOGINHOST = consts.LOGINHOST
        LOGINDATA = consts.LOGINDATA
        USERNAME = consts.USERNAME
        APIHOST = consts.APIHOST
        ENVIRONMENTPORT = consts.ENVIRONMENTPORT

        try:
            Login(BASEHOST, LOGINHOST, LOGINDATA, USERNAME).api_login()
        except Exception as e:
            logger.error(f"【登录写入token异常：{e}】")
        result = ExcelPack(file_name=TESTCASEPATH, sheet_id=setting.sheet_id).run_excel_case(APIHOST, ENVIRONMENTPORT,
                                                                                             BASEHOST, LOGINHOST,
                                                                                             LOGINDATA, USERNAME)
        return result


@allure.description("excel接口测试")  # 项目描述
@allure.link(url="https://njqa.zgyjyx.net/api", name="allure.link：超链接")  # 项目地址
@allure.issue(url="https://njqa.zgyjyx.net/api", name='allure.issue：BUG地址')  # bug链接
@allure.testcase(url="https://njqa.zgyjyx.net/api", name='allure.testcase：测试用例地址')  # 测试用例地址
@allure.feature("feature一级标签:excel接口测试")  # 一级标签
@allure.story("story二级标签:excel接口测试")  # 二级标签
@allure.title("excel接口测试")  # 用例标题
class TestExcel:
    @pytest.mark.parametrize("result", run_setup())
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.epic('excel接口测试')
    def test_excel(self, result):
        """
        :param result:
        :return:
        """
        allure.dynamic.description(f"{str(result['title'])} {str(result['method'])} {str(result['url'])}")
        allure.dynamic.title(str(result['title']))
        with allure.step(u"测试结果：{0}".format(str(result['result']))):
            allure.attach(u"测试结果：{0}".format(str(result['result'])), "测试结果")

        with allure.step(u"用例名称：{0}".format(str(result['title']))):
            allure.attach(u"用例名称：{0}".format(str(result['title'])), "用例名称")

        with allure.step(u"请求方式：{0}".format(str(result['method']))):
            allure.attach(u"请求方式：{0}".format(str(result['method'])), "请求方式")

        with allure.step(u"请求地址：{0}".format(str(result['url']))):
            allure.attach(u"请求地址：{0}".format(str(result['url'])), "请求地址")

        with allure.step(u"请求头 ：{0}".format(str(result['headers']))):
            allure.attach(u"请求头 ：{0}".format(str(result['headers'])), "请求头")

        with allure.step(u"请求参数：{0}".format(str(result['data']))):
            allure.attach(u"请求参数：{0}".format(str(result['data'])), "请求参数")

        with allure.step(u"请求断言：{0}".format(str(result['status_code']))):
            allure.attach(u"请求断言：{0}".format(str(result['status_code'])), "code请求断言")

        with allure.step(u"请求断言：{0}".format(str(result['expected_msg']))):
            allure.attach(u"请求断言：{0}".format(str(result['expected_msg'])), "msg请求断言")

        with allure.step(u"请求断言：{0}".format(str(result['expected_data']))):
            allure.attach(u"请求断言：{0}".format(str(result['expected_data'])), "data请求断言")

        with allure.step(u"响应结果：{0}".format(str(result['res']))):
            allure.attach(u"响应结果：{0}".format(str(result['res'])), "响应结果")

        with allure.step("断言"):
            assert result["result"] == "pass"
