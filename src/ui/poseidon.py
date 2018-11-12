# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poseidon.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_poseidon(object):
    def setupUi(self, poseidon):
        poseidon.setObjectName("poseidon")
        poseidon.setWindowModality(QtCore.Qt.WindowModal)
        poseidon.resize(792, 600)
        self.centralwidget = QtWidgets.QWidget(poseidon)
        self.centralwidget.setObjectName("centralwidget")
        self.lab_choose_file = QtWidgets.QLabel(self.centralwidget)
        self.lab_choose_file.setGeometry(QtCore.QRect(20, 20, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_choose_file.setFont(font)
        self.lab_choose_file.setObjectName("lab_choose_file")
        self.edit_choose_file = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_choose_file.setGeometry(QtCore.QRect(100, 20, 461, 30))
        self.edit_choose_file.setReadOnly(True)
        self.edit_choose_file.setObjectName("edit_choose_file")
        self.btn_choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choose_file.setGeometry(QtCore.QRect(580, 20, 90, 30))
        self.btn_choose_file.setObjectName("btn_choose_file")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(680, 20, 90, 30))
        self.btn_start.setObjectName("btn_start")
        self.edit_output = QtWidgets.QTextEdit(self.centralwidget)
        self.edit_output.setGeometry(QtCore.QRect(20, 60, 750, 500))
        self.edit_output.setReadOnly(True)
        self.edit_output.setObjectName("edit_output")
        poseidon.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(poseidon)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 792, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        poseidon.setMenuBar(self.menuBar)
        self.action_tuichu = QtWidgets.QAction(poseidon)
        self.action_tuichu.setObjectName("action_tuichu")
        self.action_shezhi = QtWidgets.QAction(poseidon)
        self.action_shezhi.setObjectName("action_shezhi")
        self.menu.addAction(self.action_shezhi)
        self.menu.addAction(self.action_tuichu)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(poseidon)
        QtCore.QMetaObject.connectSlotsByName(poseidon)

    def retranslateUi(self, poseidon):
        _translate = QtCore.QCoreApplication.translate
        poseidon.setWindowTitle(_translate("poseidon", "poseidon"))
        self.lab_choose_file.setText(_translate("poseidon", "选择文件:"))
        self.btn_choose_file.setText(_translate("poseidon", "选择"))
        self.btn_start.setText(_translate("poseidon", "开始"))
        self.menu.setTitle(_translate("poseidon", "文件"))
        self.action_tuichu.setText(_translate("poseidon", "退出"))
        self.action_shezhi.setText(_translate("poseidon", "设置"))

