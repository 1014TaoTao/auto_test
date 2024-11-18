# -*- encoding: utf-8 -*-

import platform

from tools.public_tool_log import logger


class OperationSystemPython:

    def __init__(self):
        pass

    # 检测操作系统
    def platform_system(self, log_path) -> str:
        """
        :return:
        """
        oper_system = platform.system()
        logger(log_path).info(
            '【{0} - {1}】'.format(oper_system, platform.architecture()))
        return oper_system

    # python 版本号
    def python_version(self, log_path) -> str:
        """
        :return:
        """
        python_version = platform.python_version()
        logger(log_path).info('【python - {0}】'.format(python_version))
        return python_version


def sys_project(log_path: str = None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython().platform_system(log_path)
    OperationSystemPython().python_version(log_path)
