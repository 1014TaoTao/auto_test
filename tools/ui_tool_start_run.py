#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/29 16:37
@Author  : ZhangTAO
@File    : ui_tool_start_run.py
@Software: PyCharm
"""

from common import setting
from common import ui_consts

from tools import public_tool_project_check
from tools.public_tool_log import logger
from tools.ui_tool_run_all import UI_Run

logger = logger(setting.UI_LOG_PATH)


def ui_run():
    """
    执行前确认pytest.ini文件中testpath的路径
    """
    # =================UI测试====================#

    U = UI_Run()

    logger.info(r"""
                 _   _ ___   _       _      _____       _   
                | | | |_ _| /_\ _  _| |_ __|_   _|__ __| |_ 
                | |_| || | / _ \ || |  _/ _ \| |/ -_|_-<  _|
                 \___/|___/_/ \_\_,_|\__\___/|_|\___/__/\__|

                  Starting      ...     ...     ...
                """
                )

    logger.info('==========< 开始 UI自动化项目 测试 >===========')
    # 打印系统和python的版本信息
    public_tool_project_check.system_project(log_path=setting.UI_LOG_PATH)
    logger.info(f"【本次执行环境为:{ui_consts.ENVIRONMENT},执行人员：{ui_consts.TESTER}】")

    try:
        if ui_consts.DELETE_ON_OFF == 'on':
            # 删除旧的测试结果数据
            U.delete_old_file()
        else:
            logger.info("【DELETE_ON_OFF == off】，不开启删除旧的测试结果数据")
    except Exception as e:
        logger.error(f"判断是否开启删除测试结果数据功能异常：{e}")

    # 执行测试
    U.run_test()

    try:
        if ui_consts.SAVE_ON_OFF == 'on':
            # 生成测试报告
            U.run_allure_report()
        else:
            logger.info("【SAVE_ON_OFF == off】，不开启生成报告功能")
    except Exception as e:
        logger.error(f"判断是否开启生成报告功能异常：{e}")

    # 发送邮件
    try:
        if ui_consts.EMAIL_ON_OFF == 'on':
            # 发送邮件
            U.run_email()
        else:
            logger.info("【EMAIL_ON_OFF == off】，不开启发送邮件功能")
    except Exception as e:
        logger.error(f"判断是否开启发送邮件功能异常：{e}")

    # 打开报告
    try:
        if ui_consts.OPEN_REPORY_ON_OFF == 'on':
            # 打开allure报告
            U.open_report()
        else:
            logger.info("【OPEN_REPORY_ON_OFF == off】，不开启自动打开报告功能")
    except Exception as e:
        logger.error(f"判断是否开启自动打开报告功能异常：{e}")

    logger.info('==========< 结束 UI自动化项目 测试 >===========')
