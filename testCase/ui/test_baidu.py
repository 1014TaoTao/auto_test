# -*- coding: utf-8 -*-
import allure
import pytest

from common import setting
from pages.baidu.baidu import BaiDu
from tools.ui_tool_read_yaml import Element

search = Element(element_path=setting.UI_YAML_PATH)


# 通过使用pytest.mark.usefixtures方法后，测试类包含的每个用例都会执行前置和后置内容。

# @pytest.mark.parametrize("url", ["https://www.baidu.com"])
@pytest.mark.usefixtures('init_project')
@allure.description("百度测试用例")
@allure.title("百度测试用例测试标题")
@allure.severity(allure.severity_level.BLOCKER)
@allure.link(url="https://www.baidu.com/", name="allure.link：超链接")
@allure.issue(url="https://www.baidu.com/", name='allure.issue：BUG地址')  # bug链接
@allure.testcase(url="https://www.baidu.com/", name='allure.testcase：测试用例地址')
@allure.feature("feature一级标签:百度测试用例")
class TestBaiDu:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.epic('test_01')
    @allure.description("test_01")
    @allure.story("story二级标签:test_01")
    def test_01(self, init_project):
        with allure.step("输入关键词"):
            text = "测试01"
            BaiDu(init_project).sousuo(text)
        with allure.step("断言"):
            result = BaiDu(init_project).titie_is_value("{0}_百度搜索".format(text))
        assert result == "pass"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.epic('test_02')
    @allure.description("test_02")
    @allure.story("story二级标签:test_02")
    def test_02(self, init_project):
        with allure.step("输入关键词"):
            text = "测试02"
            BaiDu(init_project).sousuo(text)
        with allure.step("断言"):
            result = BaiDu(init_project).titie_is_value("{0}_百度搜索".format(text))
        assert result == "pass"
