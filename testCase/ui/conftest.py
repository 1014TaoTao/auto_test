# -*- coding: utf-8 -*-

import allure
import pytest

from common import setting
from tools.public_tool_log import logger
from basepage.base import Page
from basepage.browser import select_browser
from tools import public_tool_project_check
from tools.ui_tool_elenium_check import inspect_element

logger = logger(setting.UI_LOG_PATH)
driver = None

# -----------------------------全局初始化--------------------------------------------
# 当autouse=False时，测试用例需要传入参数，为True时，不需要传入参数
'''
fixture的作用范围:
    fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
        -function：每一个函数或方法都会调用
        -class：每一个类调用一次，一个类中可以有多个方法
        -module：每一个.py文件调用一次，该文件内又有多个function和class
        -session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
'''


@pytest.fixture(scope="session", autouse=True)
def init_project():
    global driver
    with allure.step("检查系统信息"):
        logger.info('==========< 开始 UI自动化项目 测试 >===========')
        # 打印系统和python的版本信息
        public_tool_project_check.system_project(log_path=setting.UI_LOG_PATH)
    with allure.step("打开游览器并最大化"):
        if driver is None:
            driver = select_browser()
            Page(driver).max_window()
            Page(driver).implicitly_wait(30)
    with allure.step("定位元素检查"):
        logger.info(f"ui自动化，校验元素定位data格式【START】！")
        inspect_element()
        yield driver
    with allure.step("关闭浏览器"):
        Page(driver).quit()
        logger.info('==========< 结束 UI自动化项目 测试 >===========')


# 失败截图放在allure报告中
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    out = yield
    res = out.get_result()

    if res.when == 'call' and res.failed:
        if hasattr(driver, 'get_screenshot_as_png'):
            with allure.step("添加用例失败截图"):
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)
