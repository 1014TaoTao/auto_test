# -*- coding: utf-8 -*-

# 选择浏览器
import time
import logging
from selenium import webdriver


success = "SUCCESS"
fail = "FAIL"

def select_browser(browser, remote_address=None):
    driver = None
    start_time = time.time()
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    
    try:
        if remote_address is None:  # web端
            if browser in ["chrome", "Chrome"]:
                options = webdriver.ChromeOptions()
                options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
                options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去掉黄条
                driver = webdriver.Chrome(options=options)
            elif browser in ["firefox", "Firefox"]:
                driver = webdriver.Firefox()
            elif browser in ["ie", "IE"]:
                driver = webdriver.Ie()
            elif browser in ["edge", "Edge"]:
                driver = webdriver.Edge()
        else:  # 移动端
            if browser == "RChrome":
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub', desired_capabilities=dc)
            elif browser == "RIE":
                dc['browserName'] = 'internet explorer'
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub', desired_capabilities=dc)
            elif browser == "RFirefox":
                dc['browserName'] = 'firefox'
                dc['marionette'] = False
                driver = webdriver.Remote(command_executor='https://' + remote_address + '/wd/hub', desired_capabilities=dc)
        
        logging.info("{0}==> 开启浏览器: {1}, 共花费 {2} 秒".format(success, browser, "%.4f" % (time.time() - start_time)))

    except Exception:
        raise NameError("没有找到 {0} 浏览器,请确认 'ie','firefox', 'chrome','RChrome','RIe' or 'RFirefox'是否存在或名称是否正确.".format(browser))
    
    return driver
