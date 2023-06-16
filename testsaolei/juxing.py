import cv2 as cv
import easyocr 
import pyautogui as pag

pic_path = 'fang.PNG'

img = cv.imread(pic_path)

#cv.imshow('yuantu',img)

des_img = img[100:,110:]
##cv.imshow('a',des_img)

# 灰度图
gray = cv.cvtColor(des_img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)



##etVal,th1 = cv.threshold(gray,150,255,cv.THRESH_BINARY)
##cv.imshow('th1',th1)

th1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY,5,2)
cv.imshow('th1',th1)

##th2 = cv.copyMakeBorder(th1,20,20,20,20,cv.BORDER_DEFAULT)
##cv.imshow('th2',th2)

contours,hier = cv.findContours(th1,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

i = 1
reader = easyocr.Reader(['ch_sim','en'])
for cnt in contours:
    dst = des_img.copy()
    #dst = cv.drawContours(dst,cnt,-1,(0,0,255),1)
##    cv.imshow("rect",dst)
##    cv.waitKey(500)
    #area = cv.contourArea(cnt)
    
    x,y,w,h = cv.boundingRect(cnt)
    dst = cv.rectangle(dst,(x,y), (x+w,y+h),(0,0,255),1)
    #cc = cv.arcLength(dst, True)
    area = w*h

    if 3300 > area > 2000:

        #print(area)
        dst = cv.drawContours(dst,cnt,-1,(0,0,255),1)
        #cv.imshow("rect",dst)

        ROI = dst[y+1:y+h-1,x+1:x+w-1]
        name = str(i)+"_rect.png"
        cv.imwrite(name,ROI)
        i = i + 1
        cv.waitKey(500)
##print(i-1)
##
        result = reader.readtext(ROI,mag_ratio=3,batch_size=8,min_size=2,detail=0)
        s = "".join(result)
        print(s)
        if s == "2-2704":
            box = pag.locateOnScreen(name,confidence=0.85)
            pag.moveTo(box.left+20,box.top+20,duration=1)
            break







    
