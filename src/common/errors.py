# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file errors.py

class PoseidonError(Exception):
    def __init__(self, message='', error_labels=None):
        super(PoseidonError, self).__init__(message)
        self._error_labels = set(error_labels or [])