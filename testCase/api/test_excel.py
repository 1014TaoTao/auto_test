# coding:utf-8

import allure
import pytest

from common import setting, consts
from tools import public_tool_project_check
from tools.api_tool_excel import ExcelPack
from tools.api_tool_login import Login
from tools.public_tool_log import logger

logger = logger(setting.API_LOG_PATH)


def run_setup():
    """
    :return:
    """
    with allure.step("检查系统信息"):
        logger.info('==========< 开始 API自动化项目 测试 >===========')
        # 打印系统和python的版本信息
        public_tool_project_check.api_sys_project(log_path=setting.API_LOG_PATH)
        logger.info(f"【本次执行环境为:{consts.ENVIRONMENT},执行人员：{consts.TESTER}】")
        try:
            Login().api_login()
        except Exception as e:
            logger.error(f"【登录写入token异常：{e}】")
        result = ExcelPack(file_name=setting.API_EXCEL_FILE, sheet_id=setting.sheet_id).run_excel_case()
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
