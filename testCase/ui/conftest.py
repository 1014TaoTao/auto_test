# -*- coding: utf-8 -*-

import pytest
import logging

from basepage.base import Page
from basepage.browser import select_browser
from config import setting
from tools.element_check_tool import ElementPack

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
    if driver is None:
        driver = select_browser()
        Page(driver).max_window()
        Page(driver).implicitly_wait(30)

    logging.info(f"ui自动化，校验元素定位data格式【START】！")
    search = ElementPack(element_path=setting.UI_YAML_PATH)
    search.inspect_element()

    yield driver

    Page(driver).quit()


# 失败截图放在allure报告中
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    out = yield
    res = out.get_result()

    if res.when == 'call' and res.failed:
        if hasattr(driver, 'get_screenshot_as_png'):
            file_name = f"{res.nodeid.replace('::', '_').replace('/', '_')}.png"
            res._metadata.update({'image': file_name})
            driver.get_screenshot_as_file(
                f"{setting.UI_FAIL_IMG_PATH}/{file_name}")
