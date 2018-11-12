# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/8
# @file poseidon.py


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from ui.poseidon import Ui_poseidon

import sys


class MyWindow(QMainWindow, Ui_poseidon):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('../../favicon.ico'))


'''
程序主入口
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    poseidon = MyWindow()
    poseidon.show()
    sys.exit(app.exec_())