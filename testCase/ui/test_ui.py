# -*- coding: utf-8 -*-

import pytest

from config import setting
from basepage.pages.baidu.baidu import BaiDu
from tools.element_check_tool import ElementPack

search = ElementPack(element_path=setting.UI_YAML_PATH)


@pytest.mark.usefixtures('init_session')
class TestUI:

    def test_01(self, init_session):
        result = BaiDu(init_session).sousuo(text="测试01")
        assert result == "fail", ("百度搜索失败")

    def test_02(self, init_session):
        result = BaiDu(init_session).sousuo(text="测试02")
        assert result == "pass", ("百度搜索失败")
