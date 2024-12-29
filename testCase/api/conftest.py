# -*- coding: utf-8 -*-

import datetime
import time
import os
import shutil
import pytest
import pytest_html
import pytest_html.extras
from pytest_metadata.plugin import metadata_key
import logging

from common import consts
from config import setting
from tools.email_tool import EmailPack
from tools.dingding_tool import DingTalkPack

# 常量定义
TEST_TYPE: str = consts.TEST_TYPE
ENVIRONMENT: str = consts.ENVIRONMENT
TESTER: str = consts.TESTER


@pytest.fixture(scope="session", name="init_session", autouse=True)
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
    
    yield
    
    logging.info(f"========== {TEST_TYPE} 自动化测试结束 ==========")

@pytest.fixture(scope="module", name="init_module", autouse=True)
def init_module():
    logging.info("模块-前-执行")
    yield
    logging.info("模块-后-执行")

@pytest.fixture(scope="class", name="init_class", autouse=True)
def init_class():
    logging.info("类-前-执行")
    yield
    logging.info("类-后-执行")

@pytest.fixture(scope="function", name="init_test_case", autouse=True)
def init_function():
    logging.info("方法-前-执行")
    yield
    logging.info("方法-后-执行")

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """处理测试报告"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        extras = getattr(report, 'extras', [])
        if os.path.exists(setting.LOG_PATH):
            extras.append(pytest_html.extras.url(setting.LOG_PATH, name="查看详细日志"))
        report.extras = extras

