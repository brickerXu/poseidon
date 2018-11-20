# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/13
# @file export_service.py

import time
import xlrd
import urllib3
import traceback
import os
import threading
from xlutils.copy import copy
from xlwt import Workbook
from os import path

from mongo import Mongo
from mongo import MongoDisconnectError, DatabaseNotFoundError
from config import mongoConfig
from utils import *
from logger import logger
from common import directory
from bean import Record

TAG = 'export_service'


class Export(threading.Thread):
    def __init__(self, output_obj):
        threading.Thread.__init__(self)
        self.output_obj = output_obj
        self.file = None
        self.csv_dir = None

    def __init_mongo__(self):
        self.__output__('连接MongoDB...')
        self.mongoDb = Mongo(host=mongoConfig.get_host(), port=mongoConfig.get_port())
        if not self.mongoDb.connect:
            raise MongoDisconnectError()
        self.__output__('MongoDB连接成功!')

    '''
    开始工作
    '''

    def run(self):
        try:
            self.execting = True
            self.__init_mongo__()
            file_name = str(time.time())
            self.file = path.join(directory.export_dir, '%s.xlsx' % file_name)
            self.csv_dir = path.join(directory.export_dir, file_name)
            self.__write_execl_head__()
            logger.debug(TAG, '开始工作')
            if is_null(self.file):
                self.__output__('没有选择文件...')
            self.export_all()
        except MongoDisconnectError:
            logger.debug(TAG, '数据库无法连接')
            self.__output__('数据库无法连接!!!')
        except DatabaseNotFoundError:
            logger.debug(TAG, '无法找到数据库')
            self.__output__('无法找到数据库!!!')
        finally:
            self.execting = False

    def export_all(self):
        self.__output__('导出所有数据...')
        db_name = mongoConfig.get_name()
        if db_name is None:
            self.__output__('请配置数据库!!!')
            return
        collections = self.mongoDb.get_collections(db_name)
        self.__output__('共查找到%d个集合' % len(collections))
        for collection_name in collections:
            self.__output__('开始处理集合:%s' % collection_name)
            collection = self.mongoDb.get_collection(db_name, collection_name)
            for data in collection.find():
                self.handle_data(data)
        self.__output__('处理完成：excel:%s,csv:%s' % (self.file, self.csv_dir))

    def handle_data(self, data):
        if data is None:
            self.__output__("数据为None")
            return
        if 'testCases' in data.keys():
            self.__output__("存在testCases")
            task_id = data['taskid']
            sub_task_id = data['subtaskid']
            sub_sub_task_id = data['subsubtaskid']
            logger.debug(TAG, '数据:%s' % data)
            for step_infos in data['testCases']:
                step_infos = step_infos['stepInfos']
                self.__output__("处理步骤信息，共需处理%d个步骤" % len(step_infos))
                count = 0
                for step_info in step_infos:
                    if 'action' in step_info.keys():
                        action = step_info['action']
                        if 'dataAcquisition' == action and 'extensionFile' in step_info.keys() and not is_null(
                                step_info['extensionFile']):
                            record = Record()
                            record.task_id = task_id
                            record.sub_task_id = sub_task_id
                            record.sub_sub_task_id = sub_sub_task_id
                            record.step_id = step_info['stepId']
                            record.extension_file_url = step_info['extensionFile']
                            self.__handle_record(record)
                            count += 1
                self.__output__("步骤信息处理完成, 找到%d条可用数据" % count)

    def __handle_record(self, record):
        self.__output__('下载文件:%s' % record.extension_file_url)
        record.extension_file_path = self.__download__(record.extension_file_url)
        if record.extension_file_path is None:
            self.__output__('文件下载失败')
            return
        self.__output__('记录数据')
        self.__write_excel__(record)
        self.__output__('记录完成')

    def __write_excel__(self, record):
        rexcel = xlrd.open_workbook(self.file)
        rows = rexcel.sheets()[0].nrows
        excel = copy(rexcel)
        sheet = excel.get_sheet(0)
        row = rows
        sheet.write(row, 0, record.task_id)
        sheet.write(row, 1, record.sub_task_id)
        sheet.write(row, 2, record.sub_sub_task_id)
        sheet.write(row, 3, record.step_id)
        sheet.write(row, 4, record.extension_file_url)
        sheet.write(row, 5, record.extension_file_path)
        excel.save(self.file)

    def __write_execl_head__(self):
        book = Workbook()
        sheet1 = book.add_sheet('data')
        sheet1.write(0, 0, '任务id')
        sheet1.write(0, 1, '子任务id')
        sheet1.write(0, 2, '子子任务id')
        sheet1.write(0, 3, '步骤id')
        sheet1.write(0, 4, '数据文件URL')
        sheet1.write(0, 5, '本地文件路径')
        book.save(self.file)

    def __download__(self, url):
        # 获取文件名称,组装路径
        filename = url[url.rfind(r'/') + 1:len(url)]
        if not path.exists(self.csv_dir):
            os.makedirs(self.csv_dir)
        filePath = path.join(self.csv_dir, filename)
        try:
            http = urllib3.PoolManager()
            f = http.request('GET', url)
            with open(filePath, "wb") as d:
                d.write(f.data)
            return filePath
        except:
            exc = traceback.format_exc()
            logger.error(TAG, u'文件下载失败,url:%s' % url, exc)
            return None

    def __output__(self, string):
        logger.debug(TAG, string)
        if self.output_obj is not None:
            self.output_obj.output(string)
