# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'torato.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_torato(object):
    def setupUi(self, torato):
        torato.setObjectName("torato")
        torato.resize(481, 264)
        self.lineEdit = QtWidgets.QLineEdit(torato)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(torato)
        self.label.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(torato)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 411, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(torato)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(torato)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(torato)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 140, 81, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(torato)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(torato)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 200, 81, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(torato)
        self.radioButton.setGeometry(QtCore.QRect(220, 60, 115, 19))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(torato)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 140, 115, 19))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(torato)
        self.radioButton_3.setGeometry(QtCore.QRect(220, 210, 115, 19))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(torato)
        self.pushButton.setGeometry(QtCore.QRect(370, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(torato)
        QtCore.QMetaObject.connectSlotsByName(torato)

    def retranslateUi(self, torato):
        _translate = QtCore.QCoreApplication.translate
        torato.setWindowTitle(_translate("torato", "Dialog"))
        self.label.setText(_translate("torato", "旋转角度"))
        self.label_2.setText(_translate("torato", "提示：非90度旋转整数倍数可能出现部分区域删除现象"))
        self.label_3.setText(_translate("torato", "图像编辑"))
        self.label_4.setText(_translate("torato", "放大倍数"))
        self.label_5.setText(_translate("torato", "缩小倍数"))
        self.pushButton.setText(_translate("torato", "确认"))

