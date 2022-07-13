#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 选择浏览器
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from common import setting
from tools.logs_tools.public_tool_log import logger

success = "SUCCESS"
fail = "FAIL   "
logger = logger(setting.UI_LOG_PATH)


def select_browser(browser=setting.BROWSER, remote_address=None):
    driver = None
    start_time = time.time()
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    try:
        if remote_address is None:  # web端
            if browser == "chrome" or browser == "Chrome":
                # driver = webdriver.Chrome(service=Service(setting.DRIVER))
                options = webdriver.ChromeOptions()
                # options.add_argument('start-maximized')
                # 无头模式：启动浏览器进程，但不会显示出来
                # options.add_argument('--headless')
                # options.add_argument('--disable-gpu')
                # 新版本的去掉警告（70以上版本）
                options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
                options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去掉黄条
                driver = webdriver.Chrome(options=options, service=Service(setting.DRIVER))

            elif browser == "firefox" or browser == "Firefox":
                driver = webdriver.Firefox()
            elif browser == "internet explorer" or browser == "ie":
                driver = webdriver.Ie()
            elif browser == "opera":
                driver = webdriver.Opera()
            elif browser == "edge":
                driver = webdriver.Edge()
        else:  # 移动端
            if browser == "RChrome":
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub',
                                          desired_capabilities=dc)
            elif browser == "RIE":
                dc['browserName'] = 'internet explorer'
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub',
                                          desired_capabilities=dc)
            elif browser == "RFirefox":
                dc['browserName'] = 'firefox'
                dc['marionette'] = False
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub',
                                          desired_capabilities=dc)
        logger.info(
            "{0}==> 开启浏览器: {1}, 共花费 {2} 秒".format(success, browser, "%.4f" % (time.time() - start_time)))

    except Exception:
        raise NameError("没有找到 {0} 浏览器,请确认 'ie','firefox',"
                        "'chrome','RChrome','RIe' or 'RFirefox'是否存在或名称是否正确.".format(browser))
    return driver
