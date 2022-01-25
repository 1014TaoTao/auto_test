#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/25
# @Author  : Mcen (mmocheng@163.com)
# @Name    : log_conf
# coding=utf-8
"""
定义执行日志
"""
import os
import logging,time
from logging.handlers import TimedRotatingFileHandler
from base.element_path import Element

class Logger(object):
    def __init__(self, logger_name='framework'):
        self.LOG_PATH = Element().LOG_PATH

        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        log_date = time.strftime("%Y-%m-%d")
        self.log_file_name = log_date + '_run_logging.log'
        self.backup_count = 5
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(self.LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()