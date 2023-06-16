import pyautogui as pag
import os
import pyperclip


pag.PAUSE = 3


root = r"C:\Users\Administrator\Pictures\test"

dinfo = dict()

for fname in os.listdir(os.path.join(root,"常涛")):
    os.chdir(os.path.join(root,"常涛"))
    print(fname)
    if "身份证" in fname:
        dinfo["id"] = fname
        continue
    if "体检" in fname:
        dinfo["bc"] = fname
        continue
    if "学历" in fname:
        dinfo["xl"] = fname
        continue
    if "申请" in fname:
        dinfo["sq"] = fname
        continue
    if "照片" in fname:
        dinfo["zp"] = fname
        continue

# 收集文件名和绝对路径
print(dinfo)
dpath = os.getcwd()

# 点击添加附件
ps = (619,327)
pag.click(ps)

pag.click(498,311) # 点击上传

pag.click(380,51) #选择路径

pyperclip.copy(dpath) # 输入路径
pag.hotkey('ctrl','v')
pag.press('enter')

pag.click(484,665)
pyperclip.copy(dinfo['id']) # 输入路径
pag.hotkey('ctrl','v')
pag.press('enter')



