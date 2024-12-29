# -*- coding: utf-8 -*-

import pytest

from config import setting
from basepage.pages.baidu.baidu import BaiDu
from tools.element_check_tool import ElementPack

search = ElementPack(element_path=setting.UI_YAML_PATH)


# 通过使用pytest.mark.usefixtures方法后，测试类包含的每个用例都会执行前置和后置内容。
# @pytest.mark.parametrize("url", ["https://www.baidu.com"])
@pytest.mark.usefixtures('init_project')
class TestBaiDu:

    def test_01(self, init_project):
        text = "测试01"
        BaiDu(init_project).sousuo(text)
        result = BaiDu(init_project).titie_is_value("{0}_百度搜索".format(text))
        assert result == "pass"

    def test_02(self, init_project):
        text = "测试02"
        BaiDu(init_project).sousuo(text)
        result = BaiDu(init_project).titie_is_value("{0}_百度搜索".format(text))
        assert result == "pass"
