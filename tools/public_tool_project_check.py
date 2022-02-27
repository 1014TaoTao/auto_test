# -*- encoding: utf-8 -*-

import platform

from tools.public_tool_log import logger


class OperationSystemPython:
    def __init__(self, log_path):
        """
        :param log_path:
        """
        self.logger = logger(log_path)

    # 检测操作系统
    def platform_system(self):
        """
        :return:
        """
        oper_system = platform.system()
        self.logger.info('【{0} - {1}】'.format(oper_system, platform.architecture()))
        return oper_system

    # python 版本号
    def python_version(self):
        """
        :return:
        """
        python_version = platform.python_version()
        self.logger.info('【python - {0}】'.format(python_version))
        return python_version


def api_sys_project(log_path=None):
    """
    :param log_path:
    :return:
    """
    OperationSystemPython(log_path).platform_system()
    OperationSystemPython(log_path).python_version()
