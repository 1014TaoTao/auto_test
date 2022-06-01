# coding:utf-8
# ==============================
#        日志类的封装
# ==============================
import datetime
import logging
import os


class LoggerHandler(object):
    """ 日志操作 """
    _logger_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, log_path, log_name, file_name, logger_level, stream_level='info', file_level='warning', ):
        """
        :param log_path:
        :param log_name:
        :param file_name:
        :param logger_level:
        :param stream_level:
        :param file_level:
        """
        self.log_name = log_name
        self.file_name = file_name
        self.logger_level = self._logger_level.get(logger_level, 'debug')
        self.stream_level = self._logger_level.get(stream_level, 'info')
        self.file_level = self._logger_level.get(file_level, 'warning')
        # 创建日志对象
        self.logger = logging.getLogger(self.log_name)
        # 设置日志级别
        self.logger.setLevel(self.logger_level)

        if not self.logger.handlers:
            # 设置日志输出格式
            # u'[时间]:%(asctime)s-[线程]:%(thread)s:%(threadName)s-[进程]:%(process)d-[级别]:%(levelname)s-[文件]:%(filename)s-[路径]:%(pathname)s-[模块]:%(module)s-[函数]:%(funcName)s-[行号]:%(lineno)d-[信息]:%(message)s'
            formatter = logging.Formatter(
                u'[时间]:%(asctime)s-[级别]:%(levelname)s-[文件]:%(filename)s-[信息]:%(message)s'
            )

            f_file = logging.FileHandler(self.file_name, encoding='utf-8')  # 文件输出
            f_file.setLevel(self.file_level)  # 文件输出等级
            f_file.setFormatter(formatter)  # 文件输出格式
            self.logger.addHandler(f_file)  # 输入文件

            # 设置日志输出流
            f_stream = logging.StreamHandler()  # 控制台输出
            f_stream.setLevel(self.stream_level)  # 控制台输出等级
            f_stream.setFormatter(formatter)  # 控制台输出格式
            self.logger.addHandler(f_stream)

    @property
    def get_logger(self):
        """
        :return:
        """
        return self.logger


def logger(log_path):
    """
    :param log_path:
    :return:
    """
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return LoggerHandler(
        log_path=log_path,
        log_name="DEFAULT",
        logger_level="debug",
        stream_level="debug",
        file_level="info",
        # file_name = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log')
        file_name=os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
    ).get_logger
