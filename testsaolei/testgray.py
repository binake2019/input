import cv2
import os
import numpy as np
import easyocr

# 确认上述地址是否存在
##src = cv2.imread('AAAA.png')
##cv2.namedWindow("3",1)
##cv2.imshow("3", src)
##cv2.waitKey(20)
##gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
##cv2.namedWindow("binary",1)
##cv2.imshow("binary", gray)
##cv2.waitKey(100)
##
##etVal, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
##cv2.namedWindow("threshold",cv2.WINDOW_AUTOSIZE)
##cv2.imshow("threshold", threshold)
##cv2.waitKey(0)

##th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
##                            cv2.THRESH_BINARY,11,2) 
##th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
##                            cv2.THRESH_BINARY,11,2)
##
##cv2.namedWindow('a',1)
##cv2.imshow('a',th2)
##
##cv2.namedWindow('b',1)
##cv2.imshow('b',th3)

path = 'bbb.PNG'
img = cv2.imread(path)
##copyimg = img[0:100,0:100]
##cv2.imshow('1',copyimg)
##copyimg2 = img[50:100,0:100]
##cv2.imshow('2',copyimg2)
##hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 色彩空间转换为hsv，便于分离
##lower_hsv = np.array([0, 0, 30])  # 提取颜色的低值
##high_hsv = np.array([180, 43, 250])  # 提取颜色的高值
##mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
##cv2.namedWindow('1',1)
##cv2.imshow('1',mask)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
etVal,threshold = cv2.threshold(gray,127, 255, cv2.THRESH_BINARY_INV)
##cv2.namedWindow('2',1)
##cv2.imshow('2',threshold)

##th1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)
##cv2.namedWindow('3',1)
##cv2.imshow('3',th1)


#检测轮廓
# ret, thresh = cv2.threshold(cv2.cvtColor(img, 127, 255, cv2.THRESH_BINARY))

contours, hier = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#print(contours)
##cnt = contours[4]
##dst = cv2.drawContours(img,cnt,-1,(0,0,255),3)
##cv2.imshow('dst',dst)
cv2.imshow('yuan',img)


for i in range(len(list(contours))):
    cnt = contours[i]

##    jd = 0.05
##    epsilon  = jd*cv2.arcLength(cnt,True)
##    approx = cv2.approxPolyDP(cnt, epsilon, True)

    x, y ,w ,h  = cv2.boundingRect(cnt)
    print(x,y,w,h)
    #dst = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    #dst = cv2.drawContours(img,[approx],-1,(0,0,255),3)
    #ROIname = 'ROI{num}'.format(num=i)
    ROI = img[y:y+h,x:x+w]
    name = str(i)+"_test.png"
    cv2.imwrite(name,ROI)
    #ROI = img[x:x+w,y:y+h]
    cv2.imshow(str(i),ROI)


    print ("面积",cv2.contourArea(cnt))
    print ("周长",cv2.arcLength(cnt,True))

    
##reader = easyocr.Reader(['ch_sim','en'])

##for i in range(10):    
##    name = str(i)+"_test.png"
##    result = reader.readtext(name)
##    print(result)    




    
# 轮廓提取、属性、近似轮廓、边界矩形和外接圆
 
# 转二进制图像
def ToBinray():
    global imgray, binary
    # 1、灰度图
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('imgray', imgray)
 
    # 2、二进制图像
    ret, binary = cv.threshold(imgray, 127, 255, 0)
    # 阈值 二进制图像
    cv.imshow('binary', binary)
 
 
# 提取轮廓
def GetContours():
    global contours
    # 1、根据二值图找到轮廓
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
 
    # 2、画出轮廓
    dst = img.copy()
    dst = cv.drawContours(dst, contours, -1,                (0, 0, 255), 3)
    #                           轮廓     第几个(默认-1：所有)   颜色       线条厚度
 
    cv.imshow('contours', dst)
 
 
# 获取轮廓信息
def GetContours_Attrib():
    # 画出第一个轮廓
    cnt = contours[0]
    dst = img.copy()
    dst = cv.drawContours(dst, cnt, -1, (0, 0, 255), 3)
    cv.imshow('contour0', dst)
 
    # 获取轮廓面积
    area = cv.contourArea(cnt)
    print("轮廓面积：", area)
 
    # 周长（True表示合并）
    perimeter = cv.arcLength(cnt, True)
    print("轮廓周长：", perimeter)
 
 
# 轮廓近似
def GetApprox():
    # 1、取外围轮廓
    cnt = contours[0]
 
    # 2、设置精度（从轮廓到近似轮廓的最大距离）
    epsilon = 0.01 * cv.arcLength(cnt, True)
    #                            轮廓  闭合轮廓还是曲线
 
    # 3、获取近似轮廓
    approx = cv.approxPolyDP(cnt, epsilon,          True)
    #                             近似度(这里为5%)   闭合轮廓还是曲线
 
    # 4、绘制轮廓
    dst = img.copy()
    dst = cv.drawContours(dst, [approx], -1, (0, 0, 255), 3)
 
    # 显示
    cv.imshow("apporx", dst)
 
 
# 获取边界矩形
def BoundingRect():
    # 1、取外围轮廓
    cnt = contours[0]
 
    # 2、获取正方形坐标长宽
    x, y, w, h = cv.boundingRect(cnt)
 
    # 3、画出矩形
    dst = img.copy()
    dst = cv.rectangle(dst, (x,y),(x+w,y+h), (0,0,255), 3)
 
    # 显示
    cv.imshow("rect", dst)
 
 
# 获取外接圆
def Circle():
    # 1、获取第一个轮廓
    cnt = contours[0]
 
    # 2、获取外接圆
    (x, y), radius = cv.minEnclosingCircle(cnt)
    # 坐标   半径
 
    # 3、画圆
    dst = img.copy()
    dst = cv.circle(dst, (int(x), int(y)), int(radius), (0, 0, 255), 3)
 
    # 显示
    cv.imshow("circle", dst)
 
## 
##if __name__ == '__main__':
##    img = cv.imread('Resource/contour.jpg')
##    cv.imshow('img', img)
## 
##    ToBinray()              #转二进制
## 
##    GetContours()           #提取轮廓
## 
##    GetContours_Attrib()    #获取轮廓信息
## 
##    GetApprox()             #轮廓近似
## 
##    BoundingRect()          #边界矩形
## 
##    Circle()                #外接圆
## 
##    cv.waitKey(0)
