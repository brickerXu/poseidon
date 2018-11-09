# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file errors.py

from common import PoseidonError

'''
数据库无法连接异常
'''
class MongoDisconnectError(PoseidonError):
    def __init__(self, message='MongoDB is Disconnect', error_labels=None):
        if error_labels is None:
            error_labels = ("MongoDisconnectError",)
        super(MongoDisconnectError, self).__init__(message, error_labels=error_labels)

'''
数据库不存在异常
'''
class DatabaseNotFoundError(PoseidonError):
    def __init__(self, message='Database Not Found', error_labels=None):
        if error_labels is None:
            error_labels = ("DatabaseNotFoundError",)
        super(DatabaseNotFoundError, self).__init__(message, error_labels=error_labels)
'''
集合不存在异常
'''
class CollectionNotFoundError(PoseidonError):
    def __init__(self, message='Collection Not Found', error_labels=None):
        if error_labels is None:
            error_labels = ("CollectionNotFoundError",)
        super(CollectionNotFoundError, self).__init__(message, error_labels=error_labels)

