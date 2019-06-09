# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 600, 600))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 170, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(672, 230, 101, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 290, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 350, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 410, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionlarge = QtWidgets.QAction(MainWindow)
        self.actionlarge.setObjectName("actionlarge")
        self.actionsmaller = QtWidgets.QAction(MainWindow)
        self.actionsmaller.setObjectName("actionsmaller")
        self.actiontotation = QtWidgets.QAction(MainWindow)
        self.actiontotation.setObjectName("actiontotation")
        self.actionhistnormal = QtWidgets.QAction(MainWindow)
        self.actionhistnormal.setObjectName("actionhistnormal")
        self.actionreopen = QtWidgets.QAction(MainWindow)
        self.actionreopen.setObjectName("actionreopen")
        self.actionchange = QtWidgets.QAction(MainWindow)
        self.actionchange.setObjectName("actionchange")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setObjectName("actionopen_2")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionreopen)
        self.menu_2.addAction(self.actionchange)
        self.menu_3.addAction(self.actionopen_2)
        self.menu_3.addAction(self.actionclose)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "阈值变化"))
        self.pushButton_2.setText(_translate("MainWindow", "窗口变换"))
        self.pushButton_3.setText(_translate("MainWindow", "灰度拉伸"))
        self.pushButton_4.setText(_translate("MainWindow", "直方图均衡化"))
        self.pushButton_5.setText(_translate("MainWindow", "滤镜"))
        self.pushButton_6.setText(_translate("MainWindow", "应用"))
        self.pushButton_7.setText(_translate("MainWindow", "canny算子"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "几何变化"))
        self.menu_3.setTitle(_translate("MainWindow", "开启闭合"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionlarge.setText(_translate("MainWindow", "large"))
        self.actionsmaller.setText(_translate("MainWindow", "smaller"))
        self.actiontotation.setText(_translate("MainWindow", "totation"))
        self.actionhistnormal.setText(_translate("MainWindow", "histnormal"))
        self.actionreopen.setText(_translate("MainWindow", "reopen"))
        self.actionchange.setText(_translate("MainWindow", "change"))
        self.actionopen_2.setText(_translate("MainWindow", "open"))
        self.actionclose.setText(_translate("MainWindow", "close"))

class Dialog_main(QtWidgets.QDialog):
    """对QDialog类重写，实现一些功能"""

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

