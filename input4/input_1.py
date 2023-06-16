import easyocr
import cv2 as cv


#reader = easyocr.Reader(['ch_sim','en'])
#result = reader.readtext('1.png',mag_ratio=2,batch_size=8,detail=0)

path = '1.png'

img = cv.imread(path)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

#etVal,th = cv.threshold(gray,230,255,cv.THRESH_BINARY)
th = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,
                          cv.THRESH_BINARY,5,-5)

cv.imshow('th',th)

contours, hier = cv.findContours(th,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    s = cv.contourArea(cnt)
    if s >100:
        
        #dst = cv.drawContours(img,dst,-1,(0,255,0),1)
        dst = cv.rectangle(img, (x,y),(x+w,y+h), (0,0,255), 3)
        cv.imshow('cnt',dst)
        cv.waitKey(300)
