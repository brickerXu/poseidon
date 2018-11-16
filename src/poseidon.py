# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/8
# @file poseidon.py

import sys
from PyQt5.QtWidgets import QApplication

from windows import Poseidon

'''
程序主入口
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    poseidon = Poseidon()
    poseidon.show()
    sys.exit(app.exec_())