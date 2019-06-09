# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lashen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(684, 402)
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit.setGeometry(QtCore.QRect(110, 110, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 170, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 230, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog1)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 290, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog1)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog1)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 72, 15))
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog1)
        self.tabWidget.setGeometry(QtCore.QRect(320, 60, 251, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 221, 221))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(480, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog1)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog"))
        self.label.setText(_translate("Dialog1", "灰度拉伸参数"))
        self.label_2.setText(_translate("Dialog1", "第一点x"))
        self.label_3.setText(_translate("Dialog1", "第一点y"))
        self.label_4.setText(_translate("Dialog1", "第二点x"))
        self.label_5.setText(_translate("Dialog1", "第二点y"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog1", "变化曲线"))
        self.pushButton.setText(_translate("Dialog1", "显示变化曲线"))
        self.pushButton_2.setText(_translate("Dialog1", "确认转化"))

