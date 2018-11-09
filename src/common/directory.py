# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file directory.py

"""
目录结构管理文件
"""

import sys,os
import poseidon

class Directory():
    def __init__(self):
        self.__getRootDir__()

    '''
    获取根目录
    '''
    def __getRootDir__(self):
        setupPyPath = os.path.abspath("../setup.py")
        if os.path.exists(setupPyPath):
            self.BASE_DIR = os.path.dirname(setupPyPath)
        else:
            self.BASE_DIR = os.path.dirname(sys.argv[0])

directory = Directory()
