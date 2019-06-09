# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'use.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Useit(object):
    def setupUi(self, Useit):
        Useit.setObjectName("Useit")
        Useit.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Useit)
        self.pushButton.setGeometry(QtCore.QRect(260, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Useit)
        self.lineEdit.setGeometry(QtCore.QRect(100, 90, 221, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Useit)
        QtCore.QMetaObject.connectSlotsByName(Useit)

    def retranslateUi(self, Useit):
        _translate = QtCore.QCoreApplication.translate
        Useit.setWindowTitle(_translate("Useit", "Dialog"))
        self.pushButton.setText(_translate("Useit", "确认"))

