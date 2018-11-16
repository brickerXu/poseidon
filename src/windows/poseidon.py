# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/13
# @file poseidon.py

from os import path
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from ui import Ui_poseidon
from logger import logger
from utils import *
from service import export
from mongo import MongoDisconnectError, DatabaseNotFoundError

TAG = 'window_poseidon'

class Poseidon(QMainWindow, Ui_poseidon):
    def __init__(self, parent=None):
        logger.info(TAG, '加载主窗体')
        super(Poseidon, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()
        self.open_dir = None
    def __init_ui__(self):
        self.btn_choose_file.clicked.connect(self.__btn_choose_file_click__)
        self.btn_start.clicked.connect(self.__btn_start_click__)

    def __btn_choose_file_click__(self):
        QMessageBox.information(self, "提示", "暂不支持该功能！", QMessageBox.Yes)
        '''
        暂不实现选择文件功能
        :return:
        '''
        # open_dir = './'
        # if not is_null(self.open_dir):
        #     open_dir = self.open_dir
        # openfile_name, openfile_type = QFileDialog.getOpenFileName(self, '选择文件', open_dir, 'Excel files(*.xlsx , *.xls)')
        # if is_null(openfile_name):
        #     logger.debug(TAG, '未选择文件')
        # else:
        #     self.open_dir = path.dirname(openfile_name)
        #     logger.debug(TAG, 'file_name:{}, file_type:{}'.format(openfile_name, openfile_type))
        #     self.edit_choose_file.setText(openfile_name)
        #     self.edit_output.append('选择文件：%s'%openfile_name)
        #     export.file = openfile_name

    def __btn_start_click__(self):
        logger.debug(TAG, '开始执行...')
        self.output('开始执行...')
        try:
            export.start(self)
        except MongoDisconnectError:
            logger.debug(TAG, '数据库无法连接')
            QMessageBox.warning(self, "警告", "数据库无法连接！", QMessageBox.Yes)
        except DatabaseNotFoundError:
            logger.debug(TAG, '无法找到数据库')
            QMessageBox.warning(self, "警告", "无法找到数据库！", QMessageBox.Yes)

    def output(self, string):
        self.edit_output.append(string)
