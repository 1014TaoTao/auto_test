#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/29 16:37
@Author  : ZhangTAO
@File    : ui_tool_run.py
@Software: PyCharm
"""

from common import setting
from common import ui_consts
from common.ui_consts import DINGDING_NEWS_ON_OFF
from tools.common_tools.public_tool_run_all import Run
from tools.logs_tools.public_tool_log import logger
from tools.system_tools import public_tool_project_check

logger = logger(setting.UI_LOG_PATH)


def ui_run():
    """
    执行前确认pytest.ini文件中testpath的路径
    """
    # =================UI测试====================#

    U = Run()

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
            logger.info("打开删除旧报告功能")
            # 删除旧的测试结果数据
            U.delete_old_file(
                log_path=setting.UI_LOG_PATH,
                REPORT_RESULT_PATH=setting.UI_REPORT_RESULT_PATH
            )
        else:
            logger.info("【DELETE_ON_OFF == off】，不开启删除旧的测试结果数据")
    except Exception as e:
        raise f"判断是否开启删除测试结果数据功能异常：{e}"

    # 执行测试
    U.run_test(log_path=setting.UI_LOG_PATH)

    try:
        if ui_consts.SAVE_ON_OFF == 'on':
            logger.info("打开生成报告功能")
            # 生成测试报告
            U.run_allure_report(
                log_path=setting.UI_LOG_PATH,
                REPORT_RESULT_PATH=setting.UI_REPORT_RESULT_PATH,
                REPORT_END_PATH=setting.UI_REPORT_END_PATH,
                REPORT_HISTORY_PATH=setting.UI_REPORT_HISTORY_PATH,
                RESULT_HISTORY_PATH=setting.UI_RESULT_HISTORY_PATH,
                StartEnvironmentFilePath=setting.UI_StartEnvironmentFilePath,
                EndEnvironmentFile=setting.UI_EndEnvironmentFile,
                StartEnvironmentFileXMLPath=setting.UI_StartEnvironmentFileXMLPath,
                EndEnvironmentXMLFile=setting.UI_EndEnvironmentXMLFile,
                StartExcutorJson=setting.UI_StartExcutorJson,
                EndExcutorJson=setting.UI_EndExcutorJson
            )
        else:
            logger.info("【SAVE_ON_OFF == off】，不开启生成报告功能")
    except Exception as e:
        raise f"判断是否开启生成报告功能异常：{e}"

    # 发送邮件
    try:
        if ui_consts.EMAIL_ON_OFF == 'on':
            logger.info("打开发送邮件功能")
            # 发送邮件
            U.run_email(
                REPORT_END_PATH=setting.UI_REPORT_END_PATH,
                dirpath=setting.UI_REPORT_END_PATH,
                outFullName=setting.UI_FILE_LIST_PATH,
                log_path=setting.UI_LOG_PATH,
                file_list=setting.UI_FILE_LIST
            )
        else:
            logger.info("【EMAIL_ON_OFF == off】，不开启发送邮件功能")
    except Exception as e:
        raise f"判断是否开启发送邮件功能异常：{e}"

    # 打开报告
    try:
        if ui_consts.OPEN_REPORY_ON_OFF == 'on':
            logger.info("打开自动打开测试报告功能")
            # 打开allure报告
            U.open_report(
                log_path=setting.UI_LOG_PATH,
                REPORT_END_PATH=setting.UI_REPORT_END_PATH
            )
        else:
            logger.info("【OPEN_REPORY_ON_OFF == off】，不开启自动打开报告功能")
    except Exception as e:
        raise f"判断是否开启自动打开报告功能异常：{e}"

    # 发送钉钉执行消息
    try:
        if DINGDING_NEWS_ON_OFF == 'on':
            # 发送钉钉消息
            U.send_dingding(
                REPORT_END_PATH=setting.UI_REPORT_END_PATH,
                log_path=setting.UI_LOG_PATH,
                title='UI自动化',
                ENVIRONMENT=ui_consts.ENVIRONMENT,
                TESTER=ui_consts.TESTER)
        else:
            logger.info("【DINGDING_NEWS_ON_OFF == off】，不开启发送钉钉消息功能")
    except Exception as e:
        raise f"【发送钉钉消息功能异常：{e}】"

    logger.info('==========< 结束 UI自动化项目 测试 >===========')
