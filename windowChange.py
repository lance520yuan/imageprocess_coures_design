# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowChange.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(676, 441)
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(50, 180, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 180, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 240, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog2)
        self.tabWidget.setGeometry(QtCore.QRect(310, 60, 311, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 301, 251))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(180, 310, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.label.setText(_translate("Dialog2", "下限"))
        self.label_2.setText(_translate("Dialog2", "上限"))
        self.label_3.setText(_translate("Dialog2", "窗口变化参数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog2", "变化曲线"))
        self.pushButton.setText(_translate("Dialog2", "显示曲线"))
        self.pushButton_2.setText(_translate("Dialog2", "确定"))

