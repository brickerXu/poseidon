# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/13
# @file poseidon.py

import time
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QTextCursor

from ui import Ui_poseidon
from logger import logger
from service import Export

TAG = 'window_poseidon'

class Poseidon(QMainWindow, Ui_poseidon):
    def __init__(self, parent=None):
        logger.info(TAG, '加载主窗体')
        super(Poseidon, self).__init__(parent)
        self.setupUi(self)
        self.__init_ui__()
        self.open_dir = None
        self.export = None
    def __init_ui__(self):
        self.action_shezhi.triggered.connect(self.__menu_setting_click__)
        self.btn_choose_file.clicked.connect(self.__btn_choose_file_click__)
        self.btn_start.clicked.connect(self.__btn_start_click__)

    def __menu_setting_click__(self):
        QMessageBox.information(self, "提示", "暂不支持该功能！", QMessageBox.Yes)

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
        if self.export is not None and self.export.execting:
            QMessageBox.information(self, "提示", "正在导出，请勿重复操作！", QMessageBox.Yes)
            return
        logger.debug(TAG, '开始执行...')
        self.output('开始执行...')
        self.export = Export(self)
        # 父进程关闭后，子进程也会关闭
        # 否则子进程会继续执行
        self.export.setDaemon(True)
        self.export.start()

    def warning_box(self, message):
        QMessageBox.warning(self, "警告", message, QMessageBox.Yes)

    def output(self, string):
        # 插入数据
        self.edit_output.append(string)
        # 将光标移动到最后一行，滚动条自动滚动
        self.edit_output.moveCursor(QTextCursor.End)
        # time.sleep(0.1)
