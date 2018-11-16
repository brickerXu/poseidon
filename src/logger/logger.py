# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/10
# @file logger.py

"""
用于项目的log输出
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from os import path

from common import directory
from common import constants


class Logger(object):
    def __init__(self):
        self.logger_debug = self.__init_logger__(logging.DEBUG, path.join(directory.log_dir, 'debug.log'))
        self.logger_error = self.__init_logger__(logging.ERROR, path.join(directory.log_dir, 'error.log'))
        self.logger_info = self.__init_logger__(logging.INFO, path.join(directory.log_dir, 'info.log'))
        self.logger_warning = self.__init_logger__(logging.WARNING, path.join(directory.log_dir, 'warning.log'))

    def info(self, tag, log):
        message = self.__format_log__(tag, log)
        self.logger_info.info(message)

    def debug(self, tag, log):
        message = self.__format_log__(tag, log)
        self.logger_debug.debug(message)

    def error(self, tag, log):
        message = self.__format_log__(tag, log)
        self.logger_error.error(message)

    def warning(self, tag, log):
        message = self.__format_log__(tag, log)
        self.logger_warning.warning(message)

    @staticmethod
    def __format_log__(tag, log):
        return '[{}] {}'.format(tag, log)

    def __init_logger__(self, level, file):
        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(name)s] [%(filename)s] %(message)s",
            datefmt="%Y/%m/%d %X"
        )

        # 创建handler
        ch = logging.StreamHandler()
        trfh = TimedRotatingFileHandler(file, when='D', interval=1, backupCount=7, encoding=constants.DEFAULT_CHARSET)
        trfh_all = TimedRotatingFileHandler(path.join(directory.log_dir, 'all.log'), when='D', interval=1, backupCount=7, encoding=constants.DEFAULT_CHARSET)
        # 为handler指定输出格式，注意大小写
        trfh.setFormatter(formatter)
        trfh_all.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger_new = logging.getLogger(self.__get_level_name__(level))
        logger_new.setLevel(level)
        # 为logger添加的日志处理器
        logger_new.addHandler(trfh)
        logger_new.addHandler(trfh_all)
        logger_new.addHandler(ch)
        return logger_new

    @staticmethod
    def __get_level_name__(level):
        if logging.CRITICAL == level:
            return 'CRITICAL'
        elif logging.ERROR == level:
            return 'ERROR'
        elif logging.WARNING == level:
            return 'WARNING'
        elif logging.INFO == level:
            return 'INFO'
        elif logging.DEBUG == level:
            return 'DEBUG'
        else:
            return 'NONE'

logger = Logger()