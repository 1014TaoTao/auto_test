# coding: utf-8

from common import setting
from tools import public_tool_project_check
from tools.api_tool_run_all import API_Run
from tools.public_tool_log import logger

# 执行全部测试流程
logger = logger(setting.API_LOG_PATH)


def run_api(ENVIRONMENT, TESTER, DELETE_ON_OFF, SAVE_ON_OFF, EMAIL_ON_OFF, OPEN_REPORY_ON_OFF, DINGDING_NEWS_ON_OFF):
    """
        执行强确认pytest.ini文件中testpath的路径
    """
    # =================API测试====================#

    A = API_Run()

    logger.info("""
                              _         _        _           _
              __ _ _ __ (_)  / \\  _   _| |_ __ _| |_ __  ___| |_
             / _` | '_ \\| | / _ \\| | | | |_/ _ \\| |/ _ \\/ __| __|
            | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
             \\__,_| .__/|_/_/   \\_\\___/ \\__\\___/ \\_\\___||___/\\__|
                  |_|
                  Starting      ...     ...     ...
                """)

    logger.info('==========< 开始 API自动化项目 测试 >===========')
    # 打印系统和python的版本信息
    public_tool_project_check.api_sys_project(log_path=setting.API_LOG_PATH)
    logger.info(f"【本次执行环境为:{ENVIRONMENT},执行人员：{TESTER}】")

    try:
        if DELETE_ON_OFF == 'on':
            # 删除旧的测试结果数据
            A.delete_old_file()
        else:
            logger.info("【DELETE_ON_OFF == off】，不开启删除旧的测试结果数据")
    except Exception as e:
        logger.error(f"判断是否开启删除测试结果数据功能异常：{e}")
    # 执行测试
    A.run_test()
    try:
        if SAVE_ON_OFF == 'on':
            # 生成测试报告
            A.run_allure_report()
        else:
            logger.info("【SAVE_ON_OFF == off】，不开启生成报告功能")
    except Exception as e:
        logger.error(f"判断是否开启生成报告功能异常：{e}")

    # 发送邮件
    try:
        if EMAIL_ON_OFF == 'on':
            # 发送邮件
            A.run_email()
        else:
            logger.info("【EMAIL_ON_OFF == off】，不开启发送邮件功能")
    except Exception as e:
        logger.error(f"判断是否开启发送邮件功能异常：{e}")

    # 打开报告
    try:
        if OPEN_REPORY_ON_OFF == 'on':
            # 打开allure报告
            A.open_report()
        else:
            logger.info("【OPEN_REPORY_ON_OFF == off】，不开启自动打开报告功能")
    except Exception as e:
        logger.error(f"判断是否开启自动打开报告功能异常：{e}")

    # 发送钉钉执行消息
    try:
        if DINGDING_NEWS_ON_OFF == 'on':
            # 发送钉钉消息
            A.send_dingding()
        else:
            logger.info("【DINGDING_NEWS_ON_OFF == off】，不开启发送钉钉消息功能")
    except Exception as e:
        logger.error(f"判断是否开启发送钉钉消息功能异常：{e}")

    logger.info('==========< 结束 API自动化项目 测试 >===========')

    # =================UI测试====================#
    # U = UI_Run()
    # 删除旧的测试结果数据
    # U.delete_old_file()
    # 删除旧的测截图
    # U.del_old_img()
    # 执行测试
    # U.run_test()
    # # 生成测试报告
    # U.run_allure_report()
    # 压缩报告
    # U.run_zip()
    # 发送邮件
    # U.run_email()
    # 打卡allure报告
    # U.open_report()

# if __name__ == '__main__':
#     run()
