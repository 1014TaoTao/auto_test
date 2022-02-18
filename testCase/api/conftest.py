# # -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         conftest
# Description:
# Author:       ZhangTao
# Date:         2021/1/15
# -------------------------------------------------------------------------------
# import allure
# import pytest
#
# from common import setting, consts
# from tools import public_tool_project_check
# from tools.api_tool_excel import ExcelPack
# from tools.api_tool_headers import headersPack
# from tools.public_tool_log import logger
# from tools.api_tool_login import Login

#
# -----------------------------全局初始化--------------------------------------------
# logger = logger(setting.API_LOG_PATH)

"""
    @allure.feature # 用于定义被测试的功能，被测产品的需求点
    @allure.story # 用于定义被测功能的用户场景，即子功能点
    @allure.severity #用于定义用例优先级
    @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
    @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址
    @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
    @pytest.ini.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
    allure.environment(environment=env) #用于定义environment
    
    fixture作用范围
    fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
    - function函数级（测试用例）==> 每一个函数或方法都会调用
    - class类级（测试类）==>  每一个类调用一次，一个类可以有多个方法
    - module模块级（测试模块—py文件）==> 每一个.py文件调用一次，该文件内又有多个function和class
    - session会话级（整个测试执行会话）==> 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""


# @pytest.fixture(scope="session", autouse=True)
# @pytest.fixture()
# def api_init_project():
#     with allure.step("检查系统信息"):
#         logger.info('==========< 开始 API自动化项目 测试 >===========')
#         # 打印系统和python的版本信息
#         public_tool_project_check.api_sys_project(log_path=setting.API_LOG_PATH)
#         logger.info(f"【本次执行环境为:{consts.ENVIRONMENT},执行人员：{consts.TESTER}】")
#         try:
#             Login().api_login()
#         except Exception as e:
#             logger.error(f"【登录写入token异常：{e}】")
#         result = ExcelPack(file_name=setting.API_EXCEL_FILE, sheet_id=setting.sheet_id).run_excel_case()
#         return result


# def many_user_login():
#
