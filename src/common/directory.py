# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file directory.py

"""
目录结构管理文件
"""

import sys
import os
from os import path

class Directory(object):
    def __init__(self):
        self.__getRootDir__()
        self.log_dir = path.join(self.base_dir, 'logs')
        if not path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.config_dir = path.join(self.base_dir, 'config')
        if not path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        self.poseidon_config_path = path.join(self.config_dir, 'poseidon.ini')
        if not path.exists(self.poseidon_config_path):
            file = open(self.poseidon_config_path, 'w')
            file.close()
        self.mongo_config_path = path.join(self.config_dir, 'mongo.ini')
        if not path.exists(self.mongo_config_path):
            file = open(self.mongo_config_path, 'w')
            file.close()
        self.export_dir = path.join(self.base_dir, 'export')
        if not path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    '''
    获取根目录
    '''
    def __getRootDir__(self):
        setup_path = path.abspath("../setup.py")
        if path.exists(setup_path):
            self.base_dir = path.dirname(setup_path)
        else:
            self.base_dir = path.dirname(sys.argv[0])

directory = Directory()
