# -*- encoding: utf-8 -*-

import platform
import winreg

from common import setting
from tools.public_tool_log import logger


class OperationSystemPython:
    def __init__(self, log_path: str):
        """
        :param log_path:
        """
        self.logger = logger(log_path)

    # 检测操作系统
    def platform_system(self) -> str:
        """
        :return:
        """
        oper_system = platform.system()
        self.logger.info('【{0} - {1}】'.format(oper_system, platform.architecture()))
        return oper_system

    # python 版本号
    def python_version(self) -> str:
        """
        :return:
        """
        python_version = platform.python_version()
        self.logger.info('【python - {0}】'.format(python_version))
        return python_version

    # chrome 版本号
    def chrome_ersion(self) -> str:
        """
        :return:
        """
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, setting.chrome_reg)
        version = winreg.QueryValueEx(key, "version")[0]  # 查询注册表chrome版本号
        self.logger.info('【{0} - {1}】'.format(setting.BROWSER, version))
        self.logger.info('【chromedriver.exe - {0}】'.format(setting.DRIVER))
        return version


def api_sys_project(log_path: str = None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython(log_path).platform_system()
    OperationSystemPython(log_path).python_version()


def system_project(log_path: str = None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython(log_path).platform_system()
    OperationSystemPython(log_path).chrome_ersion()
    OperationSystemPython(log_path).python_version()
