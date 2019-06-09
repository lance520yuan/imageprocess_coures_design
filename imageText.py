import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets

from imageUi import Ui_MainWindow
from half import Ui_Dialog
from lashen import Ui_Dialog1
from windowChange import Ui_Dialog2
from Hist import Ui_Dialog3
from lib import *
from filter import Ui_Dialog4
from torato import Ui_torato
from use import Ui_Useit

import cv2
from PIL import Image
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

class MainWindow():
    imagePaths = ""
    imageList =[]# 二维的图像列表
    hideLayoutTag = -1
    bitcount = 0
    filterMode = np.zeros((3,3),int)
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.raw_image = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.action_connect()
        MainWindow.show()
        sys.exit(app.exec_())
    #设置算子


    def action_connect(self):
        #编辑窗口
        #打开
        self.ui.actionopen.triggered.connect(self.open_file)
        #存储
        self.ui.actionsave.triggered.connect(self.save_file)
        #重新打开
        self.ui.actionreopen.triggered.connect(self.reopen)
        #开启
        self.ui.actionopen_2.triggered.connect(self.open)
        #闭合
        self.ui.actionclose.triggered.connect(self.close)
        #右侧按钮们
        self.ui.pushButton.clicked.connect(self.half)
        self.ui.pushButton_2.clicked.connect(self.Bewindow)
        self.ui.pushButton_3.clicked.connect(self.Lashen)
        self.ui.pushButton_4.clicked.connect(self.Hist)
        self.ui.pushButton_5.clicked.connect(self.filter)
        self.ui.actionchange.triggered.connect(self.roIt)
        self.ui.pushButton_6.clicked.connect(self.useit)
        self.ui.pushButton_7.clicked.connect(self.cannyMylove)

    def useit(self):

        Dialog = QtWidgets.QDialog()
        self.ui_9 = Ui_Useit()
        self.ui_9.setupUi(Dialog)
        self.ui_9.pushButton.clicked.connect(self.Use_doit)
        Dialog.show()
        Dialog.exec_()

    def Use_doit(self):
        g = cv2.cvtColor(self.imageList, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(g, 236, 255, 0)
        img, cts, hi = cv2.findContours(th, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0, len(cts)):
            x, y, w, h = cv2.boundingRect(cts[i])
            cv2.rectangle(self.imageList, (x, y), (x + w, y + h), (0, 0, 100), 1)
        self.ui_9.lineEdit.setText(str(len(cts)-1))
        self.show_image()

    def open(self):
        kernel = np.ones((5, 5), np.uint8)
        self.imageList= cv2.morphologyEx(self.imageList, cv2.MORPH_OPEN,kernel)
        self.show_image()

    def close(self):
        kernel = np.ones((5, 5), np.uint8)
        self.imageList=cv2.morphologyEx(self.imageList, cv2.MORPH_CLOSE, kernel)
        self.show_image()

    def cannyMylove(self):
        self.imageList=cannyDo(self.imageList)
        self.show_image()


#旋转放大缩小
    def roIt(self):
        Dialog = QtWidgets.QDialog()
        self.ui_7=Ui_torato()
        self.ui_7.setupUi(Dialog)
        self.init_roit()
        self.ui_7.pushButton.clicked.connect(self.doit)
        Dialog.show()
        Dialog.exec_()
#旋转放大缩小处理
    def doit(self):
        flag=0
        du=0
        if self.ui_7.radioButton.isChecked():
            flag=1
            du=int(self.ui_7.lineEdit.text())
        if self.ui_7.radioButton_2.isChecked():
            flag=2
            du = int(self.ui_7.lineEdit_2.text())
        if self.ui_7.radioButton_3.isChecked():
            flag=3
            du = int(self.ui_7.lineEdit_3.text())
        self.imageList=change_roit(self.imageList,flag,du)
        self.show_image()

#初始化角度

    def init_roit(self):
        self.ui_7.lineEdit.setText(str(90))
        self.ui_7.lineEdit_2.setText(str(1))
        self.ui_7.lineEdit_3.setText(str(1))

#滤镜操作
    def filter(self):
        Dialog = QtWidgets.QDialog()
        self.ui_6 = Ui_Dialog4()
        self.ui_6.setupUi(Dialog)
        self.init_filter()
        self.ui_6.pushButton_5.clicked.connect(self.setMath)
        self.ui_6.pushButton_3.clicked.connect(self.preLook)
        self.ui_6.pushButton_4.clicked.connect(self.atLook)
        self.ui_6.pushButton.clicked.connect(self.savetxt)
        self.ui_6.pushButton_2.clicked.connect(self.loadtxt)
        Dialog.show()
        Dialog.exec_()

#设置保存算子
    def savetxt(self):
        fname = QFileDialog.getSaveFileName(None, '打开文件', './', "Text Files (*.txt)")
        if fname[0]:
            file=open(fname[0],"a")
            a=[]
            file.write(str(int(self.ui_6.lineEdit_10.text())))
            file.write("\n")
            file.write(str(int(self.ui_6.lineEdit_11.text())))
            file.write("\n")
            for i in range(3):
                for j in range(3):
                    file.write(str(int(self.filterMode[i][j])))
                    file.write('\n')
            file.close()
#加载存储的算子
    def loadtxt(self):
        fname= QFileDialog.getOpenFileName(None,'打开文件', './', "Text Files (*.txt)")
        if fname[0]:
            file = open(fname[0], "r")
            self.ui_6.lineEdit_10.setText(file.readline())
            self.ui_6.lineEdit_11.setText(file.readline())
            for i in range(3):
                for j in range(3):
                    self.filterMode[i][j]=int(file.readline())
            file.close()
            self.ui_6.lineEdit.setText(str(self.filterMode[0][0]))
            self.ui_6.lineEdit_2.setText(str(self.filterMode[0][1]))
            self.ui_6.lineEdit_3.setText(str(self.filterMode[0][2]))
            self.ui_6.lineEdit_4.setText(str(self.filterMode[1][0]))
            self.ui_6.lineEdit_5.setText(str(self.filterMode[1][1]))
            self.ui_6.lineEdit_6.setText(str(self.filterMode[1][2]))
            self.ui_6.lineEdit_7.setText(str(self.filterMode[2][0]))
            self.ui_6.lineEdit_8.setText(str(self.filterMode[2][1]))
            self.ui_6.lineEdit_9.setText(str(self.filterMode[2][2]))

#显示图像缩率图
    def preLook(self):
        self.imageList=filter_change(self.imageList,self.filterMode,int(self.ui_6.lineEdit_10.text()))

        self.show_image()

        img_cv = cv2.cvtColor(self.imageList, cv2.COLOR_RGB2BGR)
        img_width, img_height, t = self.imageList.shape
        qimg = QImage(img_cv.data, img_width, img_height, QImage.Format_RGB888)
        pix = QPixmap(qimg)
        self.ui_6.label_3.setPixmap(pix)

#回复图像初始状态
    def atLook(self):
        self.reopen()
        img_cv = cv2.cvtColor(self.imageList, cv2.COLOR_RGB2BGR)
        img_width, img_height, t = self.imageList.shape
        qimg = QImage(img_cv.data, img_width, img_height, QImage.Format_RGB888)
        pix = QPixmap(qimg)
        self.ui_6.label_3.setPixmap(pix)

#根据按钮点选更改模板
    def setMath(self):
        if self.ui_6.radioButton_6.isChecked():
            if self.ui_6.radioButton_8.isChecked():
                self.ui_6.lineEdit.setText("1")
                self.ui_6.lineEdit_2.setText("0")
                self.ui_6.lineEdit_3.setText("-1")
                self.ui_6.lineEdit_4.setText("2")
                self.ui_6.lineEdit_5.setText("0")
                self.ui_6.lineEdit_6.setText("-2")
                self.ui_6.lineEdit_7.setText("1")
                self.ui_6.lineEdit_8.setText("0")
                self.ui_6.lineEdit_9.setText("-1")
            elif self.ui_6.radioButton_9.isChecked():
                self.ui_6.lineEdit.setText("1")
                self.ui_6.lineEdit_2.setText("2")
                self.ui_6.lineEdit_3.setText("1")
                self.ui_6.lineEdit_4.setText("0")
                self.ui_6.lineEdit_5.setText("0")
                self.ui_6.lineEdit_6.setText("0")
                self.ui_6.lineEdit_7.setText("-1")
                self.ui_6.lineEdit_8.setText("-2")
                self.ui_6.lineEdit_9.setText("-1")
        if self.ui_6.radioButton_7.isChecked():
            if self.ui_6.radioButton_8.isChecked():
                self.ui_6.lineEdit.setText("-1")
                self.ui_6.lineEdit_2.setText("-1")
                self.ui_6.lineEdit_3.setText("-1")
                self.ui_6.lineEdit_4.setText("0")
                self.ui_6.lineEdit_5.setText("0")
                self.ui_6.lineEdit_6.setText("0")
                self.ui_6.lineEdit_7.setText("1")
                self.ui_6.lineEdit_8.setText("1")
                self.ui_6.lineEdit_9.setText("1")
            elif self.ui_6.radioButton_9.isChecked():
                self.ui_6.lineEdit.setText("-1")
                self.ui_6.lineEdit_2.setText("0")
                self.ui_6.lineEdit_3.setText("1")
                self.ui_6.lineEdit_4.setText("-1")
                self.ui_6.lineEdit_5.setText("0")
                self.ui_6.lineEdit_6.setText("1")
                self.ui_6.lineEdit_7.setText("-1")
                self.ui_6.lineEdit_8.setText("0")
                self.ui_6.lineEdit_9.setText("1")
        if self.ui_6.radioButton.isChecked():
            self.ui_6.lineEdit.setText("0")
            self.ui_6.lineEdit_2.setText("0")
            self.ui_6.lineEdit_3.setText("0")
            self.ui_6.lineEdit_4.setText("0")
            self.ui_6.lineEdit_5.setText("-1")
            self.ui_6.lineEdit_6.setText("0")
            self.ui_6.lineEdit_7.setText("0")
            self.ui_6.lineEdit_8.setText("0")
            self.ui_6.lineEdit_9.setText("0")

        elif self.ui_6.radioButton_2.isChecked():
            self.ui_6.lineEdit.setText("1")
            self.ui_6.lineEdit_2.setText("1")
            self.ui_6.lineEdit_3.setText("1")
            self.ui_6.lineEdit_4.setText("1")
            self.ui_6.lineEdit_5.setText("1")
            self.ui_6.lineEdit_6.setText("1")
            self.ui_6.lineEdit_7.setText("1")
            self.ui_6.lineEdit_8.setText("1")
            self.ui_6.lineEdit_9.setText("1")

        elif self.ui_6.radioButton_3.isChecked():
            self.ui_6.lineEdit.setText("1")
            self.ui_6.lineEdit_2.setText("2")
            self.ui_6.lineEdit_3.setText("1")
            self.ui_6.lineEdit_4.setText("2")
            self.ui_6.lineEdit_5.setText("4")
            self.ui_6.lineEdit_6.setText("2")
            self.ui_6.lineEdit_7.setText("1")
            self.ui_6.lineEdit_8.setText("2")
            self.ui_6.lineEdit_9.setText("1")


        elif self.ui_6.radioButton_4.isChecked():
            self.ui_6.lineEdit.setText("0")
            self.ui_6.lineEdit_2.setText("-1")
            self.ui_6.lineEdit_3.setText("0")
            self.ui_6.lineEdit_4.setText("-1")
            self.ui_6.lineEdit_5.setText("5")
            self.ui_6.lineEdit_6.setText("-1")
            self.ui_6.lineEdit_7.setText("0")
            self.ui_6.lineEdit_8.setText("-1")
            self.ui_6.lineEdit_9.setText("0")


        elif self.ui_6.radioButton_5.isChecked():
            self.ui_6.lineEdit.setText("-1")
            self.ui_6.lineEdit_2.setText("-1")
            self.ui_6.lineEdit_3.setText("-1")
            self.ui_6.lineEdit_4.setText("0")
            self.ui_6.lineEdit_5.setText("0")
            self.ui_6.lineEdit_6.setText("0")
            self.ui_6.lineEdit_7.setText("1")
            self.ui_6.lineEdit_8.setText("1")
            self.ui_6.lineEdit_9.setText("1")

        self.filterMode[0][0] = int(self.ui_6.lineEdit.text())
        self.filterMode[0][1] = int(self.ui_6.lineEdit_2.text())
        self.filterMode[0][2] = int(self.ui_6.lineEdit_3.text())
        self.filterMode[1][0] = int(self.ui_6.lineEdit_4.text())
        self.filterMode[1][1] = int(self.ui_6.lineEdit_5.text())
        self.filterMode[1][2] = int(self.ui_6.lineEdit_6.text())
        self.filterMode[2][0] = int(self.ui_6.lineEdit_7.text())
        self.filterMode[2][1] = int(self.ui_6.lineEdit_8.text())
        self.filterMode[2][2] = int(self.ui_6.lineEdit_9.text())

    def init_filter(self):

        self.ui_6.lineEdit.setText("0")
        self.ui_6.lineEdit_2.setText("0")
        self.ui_6.lineEdit_3.setText("0")
        self.ui_6.lineEdit_4.setText("0")
        self.ui_6.lineEdit_5.setText("0")
        self.ui_6.lineEdit_6.setText("0")
        self.ui_6.lineEdit_7.setText("0")
        self.ui_6.lineEdit_8.setText("0")
        self.ui_6.lineEdit_9.setText("0")

        self.filterMode[0][0]=int(self.ui_6.lineEdit.text())
        self.filterMode[0][1]=int(self.ui_6.lineEdit_2.text())
        self.filterMode[0][2]=int(self.ui_6.lineEdit_3.text())
        self.filterMode[1][0]=int(self.ui_6.lineEdit_4.text())
        self.filterMode[1][1]=int(self.ui_6.lineEdit_5.text())
        self.filterMode[1][2]=int(self.ui_6.lineEdit_6.text())
        self.filterMode[2][0]=int(self.ui_6.lineEdit_7.text())
        self.filterMode[2][1]=int(self.ui_6.lineEdit_8.text())
        self.filterMode[2][2] = int(self.ui_6.lineEdit_9.text())
        self.ui_6.lineEdit_10.setText(str(1))
        self.ui_6.lineEdit_11.setText(str(128))



#直方图均衡化
    def Hist(self):
        Dialog = QtWidgets.QDialog()
        self.ui_5 = Ui_Dialog3()
        self.ui_5.setupUi(Dialog)
        self.show_nowHist()
        self.ui_5.pushButton.clicked.connect(self.change_hist)
        Dialog.show()
        Dialog.exec_()

    def change_hist(self):
        self.imageList=hist_nomarl(self.imageList)
        img = cv2.cvtColor(self.imageList, cv2.COLOR_RGB2GRAY)

        plt.figure(figsize=((self.ui_5.label_4.width() - 10) / 100, (self.ui_5.label_4.width() - 60) / 100),
                   frameon=False)
        plt.hist(img.ravel(), bins=256, range=[0, 256], density=1, facecolor='blue', alpha=0.5)
        plt.savefig('plot.png', bbox_inches="tight", transparent=True, dpi=100)

        pix = QPixmap("plot.png")
        self.ui_5.label_4.setPixmap(pix)
        self.show_image()

#显示现在直方图
    def show_nowHist(self):
        img=cv2.cvtColor(self.imageList, cv2.COLOR_RGB2GRAY)

        plt.figure(figsize=((self.ui_5.label_3.width() - 10) / 100, (self.ui_5.label_3.width() - 60) / 100),frameon=False)
        plt.hist(img.ravel(), bins=256, range=[0, 256], density=1, facecolor='blue', alpha=0.5)
        plt.savefig('plot.png', bbox_inches="tight", transparent=True, dpi=100)

        pix = QPixmap("plot.png")
        self.ui_5.label_3.setPixmap(pix)

#灰度拉伸
    def Lashen(self):
        Dialog = QtWidgets.QDialog()
        self.ui_4 = Ui_Dialog1()
        self.ui_4.setupUi(Dialog)
        self.init_lashen()
        self.ui_4.pushButton.clicked.connect(self.draw_lashen)
        self.ui_4.pushButton_2.clicked.connect(self.chang_lashen)
        Dialog.show()
        Dialog.exec_()

#灰度拉伸修改
    def chang_lashen(self):
        x1, y1, x2, y2 = int(self.ui_4.lineEdit.text()), int(self.ui_4.lineEdit_2.text()), int(self.ui_4.lineEdit_3.text()), int(self.ui_4.lineEdit_4.text())
        self.imageList=change_lahsen(self.imageList,x1,y1,x2,y2)
        self.show_image()

#初始化灰度拉伸
    def init_lashen(self):
        self.ui_4.lineEdit.setText(str(10))
        self.ui_4.lineEdit_2.setText(str(10))
        self.ui_4.lineEdit_3.setText(str(240))
        self.ui_4.lineEdit_4.setText(str(240))

#绘制灰度拉伸图片
    def draw_lashen(self):
        x=[]
        y=[]
        x1,y1,x2,y2= int(self.ui_4.lineEdit.text()),int(self.ui_4.lineEdit_2.text()),int(self.ui_4.lineEdit_3.text()),int(self.ui_4.lineEdit_4.text())
        for i in range(256):
            x.append(i)
            if i<=x1:
                y.append(int(i*float(y1/x1)))
            elif x1<i<=x2:
                y.append(int((i-x1)*float((y2-y1)/(x2-x1))+y1))
            else:
                y.append(int(float((255-y2)/(255-x2))*(i-x2)+y2))
        plt.figure(figsize=((self.ui_4.label_6.width() - 10) / 100, (self.ui_4.label_6.width() - 60) / 100), frameon=False)
        plt.plot(x, y)
        plt.savefig('plot.png', bbox_inches="tight", transparent=True, dpi=100)
        pix = QPixmap("plot.png")
        self.ui_4.label_6.setPixmap(pix)

#灰度窗口化

    def Bewindow(self):
        Dialog = QtWidgets.QDialog()
        self.ui_3=Ui_Dialog2()
        self.ui_3.setupUi(Dialog)
        self.init_window()
        self.ui_3.pushButton.clicked.connect(self.windowDraw)
        self.ui_3.pushButton_2.clicked.connect(self.do_window)
        Dialog.show()
        Dialog.exec_()

#执行运算
    def do_window(self):
        self.imageList=change_window(self.imageList,int(self.ui_3.lineEdit_2.text()),int(self.ui_3.lineEdit.text()))
        self.show_image()

#窗口化初始化
    def windowDraw(self):
        top=int(self.ui_3.lineEdit_2.text())
        bottom=int(self.ui_3.lineEdit.text())
        x=[]
        y=[]
        for i in range(256):
            x.append(i)
            if i<bottom:
                y.append(0)
            elif i>top:
                y.append(255)
            else:
                y.append(i)
        plt.figure(figsize=((self.ui_3.label_4.width() - 10) / 100, (self.ui_3.label_4.width() - 60) / 100), frameon=False)
        plt.plot(x, y)
        plt.savefig('plot.png', bbox_inches="tight", transparent=True, dpi=100)
        pix = QPixmap("plot.png")
        self.ui_3.label_4.setPixmap(pix)

    def init_window(self):
        self.ui_3.lineEdit.setText(str(10))
        self.ui_3.lineEdit_2.setText(str(240))

#二值化
    def half(self):
        Dialog = QtWidgets.QDialog()
        self.ui_2 = Ui_Dialog()
        self.ui_2.setupUi(Dialog)
        self.init_linetext()
        self.ui_2.pushButton.clicked.connect(self.chose)
        self.ui_2.pushButton_2.clicked.connect(self.changeit)
        self.ui_2.pushButton_3.clicked.connect(self.haf_draw)
        Dialog.show()
        Dialog.exec_()


    def init_linetext(self):
        self.ui_2.lineEdit.setText(str(128))

    #选择算法
    def chose(self):
        if self.ui_2.radioButton.isChecked():
            a = Diedai(self.imageList)
            self.ui_2.lineEdit.setText(str(a))
        elif self.ui_2.radioButton_2.isChecked():
            a = OTSU(self.imageList)
            self.ui_2.lineEdit.setText(str(a))

    def haf_draw(self):
        a = int(self.ui_2.lineEdit.text())
        x = []
        y = []
        for i in range(255):
            x.append(i)
        for j in range(255):
            if j > a:
                y.append(255)
            else:
                y.append(0)

        plt.figure(figsize=((self.ui_2.label_2.width() - 10) / 100, (self.ui_2.label_2.width() - 60) / 100),frameon=False)
        plt.plot(x, y)
        plt.savefig('plot.png', bbox_inches="tight", transparent=True, dpi=100)
        pix = QPixmap("plot.png")
        self.ui_2.label_2.setPixmap(pix)


    #中值算法
    def changeit(self):
        img_width, img_height,t= self.imageList.shape
        if self.ui_2.radioButton_3.isChecked():
            self.imageList=beyourself(self.imageList)
        else:
            a=int(self.ui_2.lineEdit.text())
            for i in range(img_height):
                for j in range(img_width):
                    if self.imageList[i][j][0] >a:
                        self.imageList[i][j]=[255,255,255]
                    else:
                        self.imageList[i][j] = [0,0,0]
        self.show_image()



    def save_file(self):
        fname = QFileDialog.getSaveFileName(None, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        if fname[0]:
            cv2.imwrite(fname[0], self.imageList)



    def show_image(self):
        img_cv = cv2.cvtColor(self.imageList, cv2.COLOR_RGB2BGR)
        img_width, img_height, t = self.imageList.shape
        ratio_img = img_width/img_height
        ratio_scene = self.ui.graphicsView.width()/self.ui.graphicsView.height()
        if self.bitcount == 24:
            qimg = QImage(img_cv.data, img_width, img_height, QImage.Format_RGB888)
        else:
            qimg = QImage(img_cv.data, img_width, img_height, QImage.Format_Grayscale8)

        self.scene = QGraphicsScene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)

        self.ui.graphicsView.setScene(self.scene)

    def open_file(self):

        fname, _ = QFileDialog.getOpenFileName(None, 'Open file', '.','Image Files(*.jpg *.bmp *.png *.jpeg *.rgb *.tif)')

        self.imagePaths = ""
        self.imageList = []
        self.imagePaths = fname
        self.readIamge()

        if (self.imageList[0][0].size == 3):
            self.bitcount = 24
        else:
            self.bitcount = 8
        self.imageList = cv2.resize(self.imageList, (600, 600), interpolation=cv2.INTER_CUBIC)
        self.show_image()

    def readIamge(self):
        path = self.imagePaths
        #img=cv2.imread(path)
        self.imageList = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
        # img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    def reopen(self):
        self.readIamge()
        self.imageList = cv2.resize(self.imageList, (600, 600), interpolation=cv2.INTER_CUBIC)
        self.show_image()



if __name__ == "__main__":
    MainWindow()
