# coding: utf-8

from common import consts, setting
from tools.api_tool_run_all import API_Run
from tools.public_tool_log import logger

# 执行全部测试流程
logger = logger(setting.API_LOG_PATH)
if __name__ == '__main__':
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
    try:
        if consts.DELETE_ON_OFF:
            # 删除旧的测试结果数据
            A.delete_old_file()
        else:
            logger.info("【consts.DELETE_ON_OFF == FALSE】，不开启删除旧的测试结果数据")
    except Exception as e:
        logger.error(f"判断是否开启删除测试结果数据功能异常：{e}")
    # 执行测试
    A.run_test()
    try:
        if consts.SAVE_ON_OFF:
            # 生成测试报告
            A.run_allure_report()
        else:
            logger.info("【consts.SAVE_ON_OFF == FALSE】，不开启生成报告功能")
    except Exception as e:
        logger.error(f"判断是否开启生成报告功能异常：{e}")

    try:
        if consts.ZIP_ON_OFF:
            # 压缩报告
            A.run_zip()
        else:
            logger.info("【consts.ZIP_ON_OFF == FALSE】，不开启压缩报告功能")
    except Exception as e:
        logger.error(f"判断是否开启压缩报告功能异常：{e}")

    try:
        if consts.EMAIL_ON_OFF:
            # 发送邮件
            A.run_email()
        else:
            logger.info("【consts.EMAIL_ON_OFF == FALSE】，不开启发送邮件功能")
    except Exception as e:
        logger.error(f"判断是否开启发送邮件功能异常：{e}")

    try:
        if consts.OPEN_REPORY_ON_OFF:
            # 打开allure报告
            A.open_report()
        else:
            logger.info("【consts.OPEN_REPORY_ON_OFF == FALSE】，不开启自动打开报告功能")
    except Exception as e:
        logger.error(f"判断是否开启自动打开报告功能异常：{e}")

    try:
        if consts.DINGDING_NEWS_ON_OFF:
            # 发送钉钉消息
            A.send_dingding()
        else:
            logger.info("【consts.DINGDING_NEWS_ON_OFF == FALSE】，不开启发送钉钉消息功能")
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
