# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/10
# @file config.py

"""
配置管理工具文件
包含配置的读取，与修改
"""

import configparser
import os
from os import path

from common.constants import *
from common.directory import directory
from utils.util import *

"""
配置服务基础父类
关于配置的读取与写入
"""
class Config(object):
    def __init__(self, config_path):
        # 初始化配置文件
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, DEFAULT_CHARSET)

    def add_config(self, section, key, value):
        pass

    def remove_config(self, section, key):
        pass

    def update_config(self, section, key, value):
        pass

    def get_config(self, section, key):
        if section in self.config.sections() and key in self.config.options(section):
            return self.config.get(section, key)
        return None


"""
项目全局配置处理类
"""
class PoseidonConfig(Config):
    def __init__(self):
        super(PoseidonConfig, self).__init__(directory.poseidon_config_path)

"""
Mongo数据库配置管理类
"""
class MongoConfig(Config):
    def __init__(self):
        super(MongoConfig, self).__init__(directory.mongo_config_path)
        self.SECTION = 'default'
    def get_host(self):
        return self.config.get(self.SECTION, 'db_host')
    def get_port(self):
        port = self.config.get(self.SECTION, 'db_port')
        if is_number(port):
            return int(port)
        else:
            return None
    def get_name(self):
        return self.config.get(self.SECTION, 'db_name')