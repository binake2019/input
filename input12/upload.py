import pyautogui as pag
import os
import pyperclip


pag.PAUSE = 1

### 上传照片
##box = pag.locateCenterOnScreen('xzwj.png',confidence=0.9)
##if box :
##    pag.click(box)
##    
##else:
##    print("找不到")
##
##fname = '常涛照片.jpg'
##path = r'C:\Users\Administrator\Pictures\test\常涛'
##
##box = pag.locateCenterOnScreen('open.png',confidence=0.9)
##if box:
##    pag.click(box)
##    pyperclip.copy(path)
##    pag.hotkey('alt','d')
##    pag.hotkey('ctrl','v')
##    pag.press('enter')
##
##    box = pag.locateCenterOnScreen('filename.png',confidence=0.9)
##    if box:
##        pag.click(box.x+100,box.y)
##        pyperclip.copy(fname)
##        pag.hotkey('ctrl','v')
##        pag.press('enter')
##    else:
##        print("找不到文件名窗口")
##else:
##    print("未找到 打开窗口")


# 上传学历证明
box = pag.locateCenterOnScreen('id_add.png',confidence=0.9)
if box:
    pag.click(box.x - 50  ,box.y) # 点选方框
    pag.click(box.x + 100 ,box.y) # 点选添加
    box = pag.locateCenterOnScreen('xgzl_add.png',confidence=0.9)# 点 选择文件 
    if box:
        pag.click(box.x - 30 ,box.y)

        fname = '常涛身份证.jpg'
        path = r'C:\Users\Administrator\Pictures\test\常涛'

        box = pag.locateCenterOnScreen('open.png',confidence=0.9) #点击 地址栏
        if box:
            pag.click(box)
            pyperclip.copy(path)
            pag.hotkey('alt','d')
            pag.hotkey('ctrl','v')
            pag.press('enter')

            box = pag.locateCenterOnScreen('filename.png',confidence=0.9)# 输入文件名
            if box:
                pag.click(box.x+100,box.y)
                pyperclip.copy(fname)
                pag.hotkey('ctrl','v')
                pag.press('enter')
            else:
                print("找不到文件名窗口")
        else:
            print("未找到 打开窗口")
    else:
        print("未找到相关资料的上传")

    box = pag.locateCenterOnScreen('upload.png',confidence=0.9)
    if box :
        pag.click(box)
    else:
        print("未找到 上传")
else:
    print("未找到身份证上传")



