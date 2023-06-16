import pyautogui as pag
import os
import pyperclip
import xlrd_get
import time
import sys

pag.PAUSE = 1
os.chdir('c:\\qian\\')

print("请打开录入界面，5秒后开始录入")
for i in range(5,0,-1):
    print(i)
    time.sleep(1.5)

print("读入表格内容")
lsdata = xlrd_get.getall('data.xlsx')

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for d in lsdata:

    # 检测截图是否保存完整
    print("检测定位图完整性")
    for index in range(len(d)):
        print(alphabet[index],index+1)
        pha = alphabet[index]
        name = pha+'.png'
        name1 = pha + '1.png'
        if name not in os.listdir() and  name1 not in os.listdir():
            print("缺少",pha,"列对应的定位图")
            time.sleep(3)
            sys.exit()
        else:
            print(pha, "列定位图 存在")
    if 'save.png' in os.listdir():
        print("保存 定位图存在" )
    else:
        print("缺少 save.png 定位图")
        time.sleep(3)
        sys.exit()

    print("检测通过，开始录入")
    
        
    for c in range(len(d)):
        pha = alphabet[index] # 列字母        
        # @表示点击
        if "@" in str(d[c]):
            count = d[c][1:]
            name = pha+ str(count)+'.png'
            box = pag.locateOnScreen(name)
            ps = (box.left + 10,box.top + 10)
            pag.click(ps)

        # # 表示多选
        elif "#" in str(d[c]):
            name = pha+'.png'
            dc = int(d[c][1:])
            box = pag.locateCenterOnScreen(name)
            pag.click(box)
            if dc > 0 :
                pag.press('down',presses=dc)
                pag.press('enter')
            else:
                pag.press('end')
                pag.press('up',presses=(abs(dc)-1))
                pag.press('enter')           
    
        # 以上两种之外的，都是文本输入
        else:
            box = pag.locateCenterOnScreen(name)
            if box:
                pag.click(box)
                pyperclip.copy(d[c])
                pag.hotkey('ctrl','v')
            else:
                print("未找到",name)
    box = pag.locateCenterOnScreen('save.png')
    pag.click(box)
        

