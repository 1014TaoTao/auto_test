# -*- coding: utf-8 -*-

import datetime
import logging
import os
import shutil
import time
import pytest
import pytest_html
import pytest_html.extras
from pytest_metadata.plugin import metadata_key

from basepage.base import Page
from basepage.browser import select_browser
from common import consts
from config import setting
from tools.element_check_tool import ElementPack
from tools.email_tool import EmailPack
from tools.dingding_tool import DingTalkPack

driver = None
# 常量定义
TEST_TYPE: str = consts.TEST_TYPE
ENVIRONMENT: str = consts.ENVIRONMENT
TESTER: str = consts.TESTER


@pytest.fixture(scope="session", autouse=True)
def init_session():
    """会话级别的测试初始化和结果收集"""
    if TEST_TYPE not in ['API', 'UI']:
        raise ValueError("请输入正确的自动化测试类型['API','UI']")
    
    if consts.DELETE_ON_OFF == 'True':
        if os.path.exists(setting.REPORT_PATH):
            shutil.rmtree(setting.REPORT_PATH)
        logging.info("历史报告数据清理完成")
    
    logging.info(f"{setting.banner}\n"
                f"开始执行 {TEST_TYPE} 自动化测试\n"
                f"测试环境: {ENVIRONMENT}\n"
                f"测试人员: {TESTER}")
    
    global driver
    if driver is None:
        driver = select_browser(browser=consts.BROWSER)
        Page(driver).max_window()
        Page(driver).implicitly_wait(30)

    logging.info(f"ui自动化，校验元素定位data格式【START】！")
    search = ElementPack(element_path=setting.UI_YAML_PATH)
    search.validate_elements()

    yield driver

    Page(driver).quit()
    logging.info(f"========== {TEST_TYPE} 自动化测试结束 ==========")

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集终端测试结果"""
    stats = terminalreporter.stats
    result = {
        'total': terminalreporter._numcollected,
        'passed': len(stats.get('passed', [])),
        'failed': len(stats.get('failed', [])),
        'skipped': len(stats.get('skipped', [])),
        'error': len(stats.get('error', [])),
        'success_rate': f"{((len(stats.get('passed', [])) / terminalreporter._numcollected * 100) if terminalreporter._numcollected else 0):.2f}%",
        'duration': f'{round(time.time() - terminalreporter._sessionstarttime, 2)}秒',
        'reprot_url': consts.REPORT_URL,
        'jenkins_url': consts.JENKINS_URL
    }
    
    logging.info(f"总用例数: {result['total']} | 通过: {result['passed']}| 失败: {result['failed']} | 跳过: {result['skipped']} | 错误: {result['error']} | 成功率: {result['success_rate']} | 总耗时: {result['duration']}")

    # 发送邮件
    if consts.EMAIL_ON_OFF == 'True':
        EmailPack().send_default_email(
            title=TEST_TYPE,
            environment=ENVIRONMENT,
            tester=TESTER,
            **result
        )
    
    # 发送钉钉消息
    if consts.DINGDING_ON_OFF== 'True':
        DingTalkPack().send_dingding(
            title=TEST_TYPE,
            environment=ENVIRONMENT,
            tester=TESTER,
            **result
        )

def pytest_html_report_title(report):
    """设置报告标题"""
    report.title = f"{TEST_TYPE}自动化测试报告"

def pytest_configure(config):
    """测试配置"""
    config.stash[metadata_key].update({
        "项目名称": f"{TEST_TYPE} 自动化测试",
        "测试类型": TEST_TYPE,
        "测试环境": ENVIRONMENT,
        "测试人员": TESTER,
        "开始时间": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    })

# 失败截图放在allure报告中
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    report = outcome.get_result()

    # if report.when == 'call' and report.failed:
    if report.when == 'call' and report.failed:
        extras = getattr(report, 'extras', [])

        # 添加日志访问到link列
        if os.path.exists(setting.LOG_PATH):
            extras.append(pytest_html.extras.url(setting.LOG_PATH, name="查看详细日志"))

        # 添加截图
        screen_img = driver.get_screenshot_as_base64()
        if screen_img is not None:
            # 当失败用例，截图返回的是None时，不会添加到报告中
            html = """
                    <div>
                        <img 
                            src="data:image/png;base64,%s" 
                            alt="screenshot" 
                            style="width:600px;height:300px;" 
                            align="right"/>
                    </div>
                """ % screen_img
            extras.append(pytest_html.extras.html(html))

        report.extras = extras
