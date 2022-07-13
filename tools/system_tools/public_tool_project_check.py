# -*- encoding: utf-8 -*-

import platform
import winreg

from common import setting
from tools.logs_tools.public_tool_log import logger


class OperationSystemPython:

    def __init__(self):
        pass
    # 检测操作系统
    def platform_system(self,log_path) -> str:
        """
        :return:
        """
        oper_system = platform.system()
        logger(log_path).info('【{0} - {1}】'.format(oper_system, platform.architecture()))
        return oper_system

    # python 版本号
    def python_version(self,log_path) -> str:
        """
        :return:
        """
        python_version = platform.python_version()
        logger(log_path).info('【python - {0}】'.format(python_version))
        return python_version

    # chrome 版本号
    def chrome_ersion(self,log_path) -> str:
        """
        :return:
        """
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, setting.chrome_reg)
        version = winreg.QueryValueEx(key, "version")[0]  # 查询注册表chrome版本号
        logger(log_path).info('【{0} - {1}】'.format(setting.BROWSER, version))
        logger(log_path).info('【chromedriver.exe - {0}】'.format(setting.DRIVER))
        return version


def api_sys_project(log_path: str = None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython().platform_system(log_path)
    OperationSystemPython().python_version(log_path)


def system_project(log_path: str = None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython().platform_system(log_path)
    OperationSystemPython().chrome_ersion(log_path)
    OperationSystemPython().python_version(log_path)
