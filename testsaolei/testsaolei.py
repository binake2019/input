import cv2 as cv
import pyautogui as pag
import torch
import matplotlib.pyplot as plt
from torch import nn,optim
import torch.nn.functional as F
import os
import time


time.sleep(2)
d = 25

def restart():
    pag.click(330,185)
    pag.click(148,222)
    
def isEnd():
    box = pag.locateOnScreen('end.png',region=(320,172,28,28))
    if box:
        print("win")
        return 1
    else:
        print("not win")
        return 0

def isWin():
    box = pag.locateOnScreen('win.png',region=(30,162,48,48))
    if box:
        return 1
    else:
        return 0 

def getScreen():
    image = pag.screenshot(region=(119,157,430,470))
    image.save('minefields.png')

    img = cv.imread('minefields.png')
    return img

def getCenter(cnt):
    x = int(cv.moments(cnt)['m10']/cv.moments(cnt)['m00'])
    y = int(cv.moments(cnt)['m01']/cv.moments(cnt)['m00'])
    return x,y

def getNum(ps):
    ls = [-1,1,2,3,4,5,8]
    reg = (ps[0] - 13,ps[1] - 13,27,27)
    num = 0
    for i in ls:
        box = pag.locateOnScreen(str(i)+'.png',region=reg)
        if box:
            num = i
            break
    return num


def getPS(np):
        
    p1 = (np[0] - d , np[1] - d)
    p2 = (np[0]     , np[1] - d)
    p3 = (np[0] + d , np[1] - d)
        
    p4 = (np[0] - d , np[1])
    #p5 = np
    p6 = (np[0] + d , np[1])
        
    p7 = (np[0] - d , np[1] +d)
    p8 = (np[0]     , np[1] +d)
    p9 = (np[0] + d , np[1] +d)
        
    return p1,p2,p3,p4,p6,p7,p8,p9
    
def getXL(np):
    ls = []
    #pag.moveTo(100,100)
    ls1 = getPS(np)
    for i in ls1:
        ls.append(getNum(i))
    return ls

def getTure(ls):
    ps = pag.position()
    ls_ps = getPS(ps)
    for i in len(ls):
        if ls[i] == -1:
            pag.click(ls_ps[i])

def isMine(ps):
    pag.click(ps)
    pag.moveTo(100,100)
    if pag.locateOnScreen('redmine.png',region=(ps[0]-d,ps[1]-d,d*2,d*2)):
        print("这个方块是雷")
        return 1
    else:
        print("不是雷")
        return 0
#----------------------------------------


pag.PAUSE = 0.1
pag.moveTo(100,100)

def checkTwo():
    t = pag.locateAllOnScreen('-1.png')
    lst = list(t)
    lst.reverse()
    for box in lst:
        ps = (int(box.left+d/2), int(box.top+ d/2))
        ls = getXL(ps)
        cc = 0
        for m in ls:
            if 8 > m > 0:
                cc = cc +1 
        if cc >2:
            return(ps)


def checkThree():
    t = pag.locateAllOnScreen('8.png')
    for box in t:
        ps = (int(box.left+d/2), int(box.top+ d/2))
        ls = getXL(ps)
        return(ps)



    
#点开一个未打开的方框,返回该方框为中心的9个格子信息.
def checkOne():
    img = getScreen()
    ##cv.imshow('minefields',img)

    # 灰度图
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ##cv.imshow('gray',gray)

    th1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY,5,2)
    #cv.imshow('th1',th1)

    contours,hier = cv.findContours(th1,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)


    d = 25 # 方块边长

    for cnt in contours:
        if isEnd():
            print("踩雷结束")
            break
        dst = img.copy()
        dst = cv.drawContours(dst,cnt,-1,(0,255,0),1)

        x,y,w,h = cv.boundingRect(cnt)
        dst = cv.rectangle(dst,(x,y), (x+w,y+h),(0,0,255),2)
        area = w*h

        if 410 > area > 380:
            cv.waitKey(200)
            a,b = getCenter(cnt)
            np = (119+a+5,157+b+5)
            ls = getXL(np)
            return(np)
            cc = 0
            for m in ls:
                if  m > 0:
                    cc = cc +1 
            if cc >2:
                return(np)

            


# 初始化

class Net(nn.Module):
    def __init__(self,hidden_in,hidden_num,outputs):
        super(Net,self).__init__()
        self.hidden = nn.Linear(hidden_in,hidden_num)
        self.out = nn.Linear(hidden_num,outputs)

    def forward(self,x):
        x = F.relu(self.hidden(x))
        x = self.out(x)
        x = F.softmax(x)
        return x

#创建net
if os.path.exists('net.pkl'):
    net = torch.load('net.pkl')
else:
    net = Net(hidden_in=8,hidden_num=10,outputs=2)


#定义交叉熵函数
criterion = nn.CrossEntropyLoss ()
#定义优化器
optimizer = optim.SGD(net.parameters(),lr =0.05)

# 训练
def pretrain(model,criterion,optimizer):
    #正确次数
    rt = 0
    tt = 0
    f = open('traindata.txt','a',encoding='utf-8')
    for ii in [8]:
        for box in pag.locateAllOnScreen(str(ii)+'.png'):
            print("-"*15)
            ps = (int(box.left+d/2), int(box.top+ d/2))
            ls = getXL(ps)
            inputs = torch.tensor(ls, dtype=torch.float)
            inputs = inputs.unsqueeze(0)
            output = model(inputs)
            pre_y = torch.max(output,1)[1].numpy()
            print("预测结果",pre_y)

            if ii == 8:
                flag = 1
            else:
                flag = 0
            target = torch.tensor([flag], dtype=torch.long)
            lsw = []
            for a in ls:
                lsw.append(str(a))
            lsw.append(str(flag))
            f.write(",".join(lsw))
            f.write("\n")

            # ls 为输入数据，flag为结果

            #print("output_size",output.size())


            if pre_y[0] == flag:
                print("预测正确")
                rt = rt + 1
            loss = criterion(output,target)
            print("loss",loss)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            tt = tt + 1
    f.close()
    torch.save(model,'net.pkl')
    print("正确率",rt/tt)


# 训练
def train(model,criterion,optimizer,epochs):
    #正确次数
    rt = 0
    f = open('traindata.txt','a',encoding='utf-8')
    for i in range(epochs):
        print("-"*15)
        if isEnd():
            restart()
        time.sleep(0.5)
        if i%3 == 0:
            ps = checkTwo()
        else:
            ps = checkOne()
        ls = getXL(ps)
        inputs = torch.tensor(ls, dtype=torch.float)
        inputs = inputs.unsqueeze(0)
        output = model(inputs)
        pre_y = torch.max(output,1)[1].numpy()
        print("预测结果",pre_y)
##        if pre_y[0] == 1:
##            pag.click(ps,button='right')
##            continue
        flag = isMine(ps)    
        target = torch.tensor([flag], dtype=torch.long)
        #print('target_size',target.size())
        lsw = []
        for a in ls:
            lsw.append(str(a))
        lsw.append(str(flag))
        f.write(",".join(lsw))
        f.write("\n")

        # ls 为输入数据，flag为结果

        #print("output_size",output.size())


        if pre_y[0] == flag:
            print("预测正确")
            rt = rt + 1
        loss = criterion(output,target)
        print("loss",loss)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    f.close()
    torch.save(model,'net.pkl')
    print("正确率",rt/epochs)

def check(num,ps):
    flag = 0

    ls = getXL(ps)
    if -1 not in ls:
        return 0
    pag.moveTo(ps)
    ls_ps = getPS(ps)
    count1 = ls.count(-1)
    count2 = ls.count(8)
    count = count1 + count2
    print("当前数字",num,"count",count)

    #清除安全块
    if count2 == num and count1 > 0:
        for i in range(len(ls)):
            if ls[i] == -1:
                pag.click(ls_ps[i])
                print("清除一个安全块")
                flag = 1
    #标记雷
    if count == num:
        print("发现",num,"颗雷")
        for i in range(len(ls)):
            if ls[i] == -1:
                pag.click(ls_ps[i],button='right')
                flag =1
    return flag
    

def normalTest():
    nextflag = 0
    nextps = 0
    while not isWin():
        stopflag = 0 
        pag.click(148,222)
        if isEnd():
            print("game over,restart")
            restart()
        if nextflag:
            ps = nextps
        else:
            ps = pag.locateCenterOnScreen('-1.png',region=(119,157,430,470)) 
        pag.moveTo(ps)
        ls = getXL(ps)
        ls_ps = getPS(ps)
        if -1 not in ls:
            pag.click(ps,button='right')
            continue
        for i in range(len(ls)):
            if 8> ls[i] >0:
                newps = ls_ps[i]
                stopflag = check(ls[i],newps)
                if stopflag == 1:
                    break
        if stopflag == 1:
            continue
            
        #证明没有可以逻辑推理的方块,在相邻块中移动到下一个
        if stopflag == 0:
            pag.moveTo(ps)
            for i in range(len(ls)):
                if ls[i] == -1:
                    temls = getXL(ls_ps[i])
                    temps = getPS(ls_ps[i])
                    for ii in range(len(temls)):
                        if 8> temls[ii] > 0:
                            nextps = ls_ps[i]
                            nextflag = 1
                            print("移动到相邻的块")
                            break
                if nextflag == 1 :
                    break
            if nextflag == 0:# 蒙一个
                print("蒙一个")
                pag.click(pag.locateCenterOnScreen('-1.png'))
                                    

#train(net,criterion,optimizer,20)

def normalTest1():
    while not isWin():
        stopflag = 0
        for i in [5,4,3,2,1]:
            for box in pag.locateAllOnScreen(str(i)+'.png',region=(119,157,430,470)):
                ps = (int(box.left+d/2)-3, int(box.top+ d/2)-3)
                stopflag = check(i,ps)      
        

normalTest1()


















        
