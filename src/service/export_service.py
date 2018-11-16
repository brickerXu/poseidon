# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/13
# @file export_service.py

import xlwt
from os import path

from mongo import Mongo
from mongo import MongoDisconnectError
from config import mongoConfig
from utils import *
from logger import logger

TAG = 'export_service'


class Export(object):
    def __init__(self):
        self.file = None
        self.output_obj = None

    def __init_mongo__(self):
        self.mongoDb = Mongo(host=mongoConfig.get_host(), port=mongoConfig.get_port())

    '''
    开始工作
    '''

    def start(self, output_obj):
        self.__init_mongo__()
        self.output_obj = output_obj
        logger.debug(TAG, '开始工作')
        if not self.mongoDb.connect:
            raise MongoDisconnectError()
        if is_null(self.file):
            self.__output__('没有选择文件...')
        self.export_all()

    def export_all(self):
        self.__output__('导出所有数据...')
        collections = self.mongoDb.get_collections(mongoConfig.get_name())
        print(collections)
        self.__output__('共查找到%d个集合' % len(collections))
        for collection_name in collections:
            self.__output__('开始处理集合:%s'%collection_name)
            collection = self.mongoDb.get_collection(mongoConfig.get_name(), collection_name)
            print(collection.find_one())


    def __save_excel__(self):
        pass

    def __output__(self, string):
        logger.debug(TAG, string)
        if self.output_obj is not None:
            self.output_obj.output(string)

export = Export()
