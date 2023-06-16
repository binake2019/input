import pyautogui as pag
import os
import time

path = "d:\input2"

os.chdir(path)

def center(box):
    if not box:
        return 0,0
    x = box.left+ box.width/2
    y = box.top+ box.height/2
    return x,y

def clickUp(box):
    x,y = center(box)
    pag.moveTo(x,y,0.5)
    pag.click()

##pag.FAILSAFE = False
##box = pag.locateOnScreen('pic\\tijiao.png',confidence=0.8)
##print(box)
##x,y = center(box)
##pag.moveTo(x,y,0.5)
##clickUp(box)
##
##t = pag.locateAllOnScreen('pic\\duigou.png',confidence=0.97)
##t = list(t)
##print(len(t),"个对勾")
box = pag.locateOnScreen('pic\\logo.png',confidence=0.8)
x0,y0 = center(box)
t = pag.locateOnScreen('pic\jia.png',confidence=0.8)
print(t)
sd = 0.5
                
if pag.locateOnScreen('pic\jia.png',confidence=0.8):
    pag.click(x0,y0+72,duration=sd)
    time.sleep(0.5)
    box = pag.locateOnScreen('pic\shi.png',confidence=0.9)
    clickUp(box)
    pag.click(x0,y0+72,duration=sd)
