# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(796, 400)
        self.pushButton = QtWidgets.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(330, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(140, 350, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(600, 350, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog3)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 251, 261))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog3)
        self.label_4.setGeometry(QtCore.QRect(470, 50, 271, 241))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Dialog"))
        self.pushButton.setText(_translate("Dialog3", "点击转化"))
        self.label.setText(_translate("Dialog3", "原直方图"))
        self.label_2.setText(_translate("Dialog3", "新直方图"))

