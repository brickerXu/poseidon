# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/13
# @file poseidon.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog

from ui.poseidon import Ui_poseidon
from logger.logger import logger

TAG = 'window_poseidon'

class Poseidon(QMainWindow, Ui_poseidon):
    def __init__(self, parent=None):
        logger.info(TAG, '加载主窗体')
        super(Poseidon, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()
    def __init_ui__(self):
        self.btn_choose_file.clicked.connect(self.__btn_choose_file_click__)
        self.btn_start.clicked.connect(self.__btn_start_click__)

    def __btn_choose_file_click__(self):
        openfile_name, openfile_type = QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls)')
        logger.debug(TAG, 'file_name:{}, file_type:{}'.format(openfile_name, openfile_type))
        self.edit_choose_file.setText(openfile_name)
        self.edit_output.append('选择文件：%s'%openfile_name)

    def __btn_start_click__(self):
        logger.debug(TAG, '开始执行...')
        self.edit_output.append('开始执行...')
