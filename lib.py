import cv2
from PIL import Image
import math
import numpy as np
from scipy import ndimage
from scipy import signal
from matplotlib import pyplot as plt
from math import *

# grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 将图像进行转化后处理
# img = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)

#迭代法
def Diedai(img=[]):
    grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    t=int((np.max(grayImage)+np.min(grayImage))/2)
    pret=0
    width,height=grayImage.shape
    sumq,sumh=0,0
    numq,numh=0,0
    while True:
        for i in range(height):
            for j in range(0,width):
                if grayImage[i][j]>t:
                    sumq+=grayImage[i][j]
                    numq+=1
                else:
                    sumh += grayImage[i][j]
                    numh += 1
        t=int(((sumq/numq)+(sumh/numh))/2)
        if pret==t:
            break
        pret=t
    return t;

# OTSU
def OTSU(img=[]):
    grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width, height = grayImage.shape
    threhold=0
    graynum={}
    for i in range(256):
        graynum[i]=0
    for i in range(height):
        for j in range(width):
            graynum[grayImage[i][j]]+=1
    gmax=0
    g,w1,w2,u1,u2,u1sum,u2sum=0,0,0,0,0,0,0
    for i in range(256):
        g,  u1, u2, u1sum, u2sum = 0, 0, 0, 0, 0,
        w1, w2=1,1
        for j in range(256):
            if j<=i:
                w1+=graynum[j]
                u1sum+=j*graynum[j]
            else:
                w2 += graynum[j]
                u2sum += j * graynum[j]
        u1=u1sum/w1
        u2=u2sum/w2
        g=float(w1*w2*pow((u1-u2),2))
        if g>gmax:
            gmax=g
            threhold=i
    return threhold

#2*2纹理化
def betrue(img=[]):
    #修改参数t可以改变范围，maxlminl仍需修改
    grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width, height = grayImage.shape
    maxl,minl=0,0
    t=2
    for i in range(0,height,1):
        for j in range(0,width,1):
            if i%t==0 and j%t==0:
                maxl=max(grayImage[i][j],grayImage[i+1][j],grayImage[i][j+1],grayImage[i+1][j+1])
                minl=min(grayImage[i][j],grayImage[i+1][j],grayImage[i][j+1],grayImage[i+1][j+1])
                temp=(maxl+minl)/2
                for k in range(t):
                    for m in range(t):
                        if grayImage[i+k][j+m]>temp:
                            grayImage[i + k][j + m]=255
                        else:
                            grayImage[i + k][j + m] = 0
    for i in range(height%t):
        for j in range(width):
            grayImage[height-i-1][j]=0
    for i in range(height):
        for j in range(width%t):
            grayImage[height][j-i-1]=0
    img = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)
    return img

#自适应阈值处理
def beyourself(img=[]):
    #修改参数t可以改变范围，maxlminl仍需修改
    imageList = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width, height = imageList.shape
    maxl,minl,temp=0,255,0
    for i in range(0,int(height/2),1):
        for j in range(0,int(width/2),1):
            if imageList[i][j]>maxl:
                maxl=imageList[i][j]
            if imageList[i][j]<minl:
                minl=imageList[i][j]
    temp = (maxl+minl)/2
    for i in range(0,int(height/2),1):
        for j in range(0,int(width/2),1):
            if imageList[i][j] > temp:
                imageList[i][j] = 255
            else:
                imageList[i][j] = 0

    maxl, minl, temp = 0, 255, 0
    for i in range( int(height / 2),height, 1):
        for j in range(0, width, 1):
            if imageList[i][j] > maxl:
                maxl = imageList[i][j]
            if imageList[i][j] < minl:
                minl = imageList[i][j]
    temp = (maxl + minl) / 2
    for i in range( int(height / 2),height, 1):
        for j in range(0, width, 1):
            if imageList[i][j] > temp:
                imageList[i][j] = 255
            else:
                imageList[i][j] = 0

    maxl, minl, temp = 0, 255, 0
    for i in range(0, height, 1):
        for j in range(int(width/2),width, 1):
            if imageList[i][j]>maxl:
                maxl=imageList[i][j]
            if imageList[i][j]<minl:
                minl=imageList[i][j]
    temp = (maxl + minl) / 2
    for i in range(0, height, 1):
        for j in range(int(width/2),width, 1):
            if imageList[i][j] > temp:
                imageList[i][j] = 255
            else:
                imageList[i][j] = 0

    maxl, minl, temp = 0, 255, 0

    for i in range(int(height / 2), height, 1):
        for j in range(int(width / 2), width, 1):
            if imageList[i][j]>maxl:
                maxl=imageList[i][j]
            if imageList[i][j]<minl:
                minl=imageList[i][j]

    temp = (maxl + minl) / 2
    for i in range(int(height/2),height, 1):
        for j in range(int(width/2),width, 1):
            if imageList[i][j] > temp:
                imageList[i][j] = 255
            else:
                imageList[i][j] = 0

    img = cv2.cvtColor(imageList, cv2.COLOR_GRAY2BGR)
    return img


#窗变化
def change_window(img=[],top=int,bottom=int):
    imageList = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width,height=imageList.shape
    for i in range(height):
        for j in range(width):
            if imageList[i][j]>top:
                imageList[i][j]=255
            elif imageList[i][j]<bottom:
                imageList[i][j]=0
    img=cv2.cvtColor(imageList, cv2.COLOR_GRAY2BGR)
    return img
#灰度拉伸
def change_lahsen(img=[],x1=0,y1=1,x2=1,y2=1):
    imageList = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width, height = imageList.shape
    for i in range(height):
        for j in range(width):
            img=imageList[i][j]
            if img <= x1:
                imageList[i][j]=int(img * float(float(y1) / x1))
            elif x1 < img <= x2:
                imageList[i][j]=int((img - x1) * float((float(y2) - y1) / (x2 - x1)) + y1)
            else:
                imageList[i][j]=int(float((255 - float(y2)) / (255 - x2)) * (img - x2) + y2)

    img = cv2.cvtColor(imageList, cv2.COLOR_GRAY2BGR)
    return img

def hist_nomarl(img=[]):
    imageList = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    width, height = imageList.shape
    imm=imageList.ravel()
    num=[]
    for i in range(256):
        num.append(0)
    for i in range(imm.size):
        num[imm[i]]+=1
    j=255
    while j>=0:
        num[j]=sum(num[0:j+1])

        num[j]/=imm.size
        j-=1
    for i in range(height):
        for j in range(width):
            imageList[i][j]=int(num[imageList[i][j]]*255+0.5)

    img = cv2.cvtColor(imageList, cv2.COLOR_GRAY2BGR)
    return img


def filter_change(img=[], filterMode=[],beto=0):
    imageList = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    temp = np.sum(filterMode)
    if temp==1:
        dst = cv2.filter2D(img, -1, kernel=filterMode)
    elif temp==-1:
        width, height = imageList.shape
        for i in range(height):
            for j in range(width):
                imageList[i][j] =255-imageList[i][j]
        dst = cv2.cvtColor(imageList, cv2.COLOR_GRAY2BGR)
    elif temp==0:

        dst = cv2.filter2D(img, -1, kernel=filterMode)
    else:
        s=np.array(filterMode, dtype="float32")
        s/=temp
        dst = cv2.filter2D(img, -1, kernel=s)
    return dst

#对图像做编辑操作

def change_roit(img,flag,num):
    height, width = img.shape[:2]
    if flag==1:

        degree = num
        # 旋转后的尺寸
        heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
        widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

        matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)

        matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
        matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步

        imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
    elif flag==2:
        imgRotation=cv2.resize(img,(height*num,width*num),interpolation=cv2.INTER_CUBIC)
    elif flag==3:
        imgRotation=cv2.resize(img,(int(height/num),int(width/num)),interpolation=cv2.INTER_CUBIC)
    else:
        imgRotation=img
    return imgRotation

def cannyDo(img=[]):
    sigma1 = sigma2 = 1
    sum = 0

    gaussian = np.zeros([5, 5])
    for i in range(5):
        for j in range(5):
            gaussian[i, j] = math.exp(-1 / 2 * (np.square(i - 3) / np.square(sigma1)  # 生成二维高斯分布矩阵
                                                + (np.square(j - 3) / np.square(sigma2)))) / (
                                         2 * math.pi * sigma1 * sigma2)
            sum = sum + gaussian[i, j]

    gaussian = gaussian / sum

    # print(gaussian)

    # step1.高斯滤波
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    W, H = gray.shape
    new_gray = np.zeros([W - 5, H - 5])
    for i in range(W - 5):
        for j in range(H - 5):
            new_gray[i, j] = np.sum(gray[i:i + 5, j:j + 5] * gaussian)  # 与高斯矩阵卷积实现滤波
    # plt.imshow(new_gray, cmap="gray")

    # step2.增强 通过求梯度幅值
    W1, H1 = new_gray.shape
    dx = np.zeros([W1 - 1, H1 - 1])
    dy = np.zeros([W1 - 1, H1 - 1])
    d = np.zeros([W1 - 1, H1 - 1])
    for i in range(W1 - 1):
        for j in range(H1 - 1):
            dx[i, j] = new_gray[i, j + 1] - new_gray[i, j]
            dy[i, j] = new_gray[i + 1, j] - new_gray[i, j]
            d[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))  # 图像梯度幅值作为图像强度值

    # plt.imshow(d, cmap="gray")

    # setp3.非极大值抑制 NMS
    W2, H2 = d.shape
    NMS = np.copy(d)
    NMS[0, :] = NMS[W2 - 1, :] = NMS[:, 0] = NMS[:, H2 - 1] = 0
    for i in range(1, W2 - 1):
        for j in range(1, H2 - 1):

            if d[i, j] == 0:
                NMS[i, j] = 0
            else:
                gradX = dx[i, j]
                gradY = dy[i, j]
                gradTemp = d[i, j]

                # 如果Y方向幅度值较大
                if np.abs(gradY) > np.abs(gradX):
                    weight = np.abs(gradX) / np.abs(gradY)
                    grad2 = d[i - 1, j]
                    grad4 = d[i + 1, j]
                    # 如果x,y方向梯度符号相同
                    if gradX * gradY > 0:
                        grad1 = d[i - 1, j - 1]
                        grad3 = d[i + 1, j + 1]
                    # 如果x,y方向梯度符号相反
                    else:
                        grad1 = d[i - 1, j + 1]
                        grad3 = d[i + 1, j - 1]

                # 如果X方向幅度值较大
                else:
                    weight = np.abs(gradY) / np.abs(gradX)
                    grad2 = d[i, j - 1]
                    grad4 = d[i, j + 1]
                    # 如果x,y方向梯度符号相同
                    if gradX * gradY > 0:
                        grad1 = d[i + 1, j - 1]
                        grad3 = d[i - 1, j + 1]
                    # 如果x,y方向梯度符号相反
                    else:
                        grad1 = d[i - 1, j - 1]
                        grad3 = d[i + 1, j + 1]

                gradTemp1 = weight * grad1 + (1 - weight) * grad2
                gradTemp2 = weight * grad3 + (1 - weight) * grad4
                if gradTemp >= gradTemp1 and gradTemp >= gradTemp2:
                    NMS[i, j] = gradTemp
                else:
                    NMS[i, j] = 0

    # plt.imshow(NMS, cmap = "gray")

    # step4. 双阈值算法检测、连接边缘
    W3, H3 = NMS.shape
    DT = np.zeros([W3, H3])
    # 定义高低阈值
    TL = 0.2 * np.max(NMS)
    TH = 0.3 * np.max(NMS)
    for i in range(1, W3 - 1):
        for j in range(1, H3 - 1):
            if (NMS[i, j] < TL):
                DT[i, j] = 0
            elif (NMS[i, j] > TH):
                DT[i, j] = 255
            elif ((NMS[i - 1, j - 1:j + 1] < TH).any() or (NMS[i + 1, j - 1:j + 1]).any()
                  or (NMS[i, [j - 1, j + 1]] < TH).any()):
                DT[i, j] = 255
    DT=np.array(DT,np.int)
    cv2.imwrite("canny.jpg",DT)
    qim=cv2.imread("canny.jpg")
    return qim

