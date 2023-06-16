import pyautogui as pag
import pyperclip
import time
from xpinyin import Pinyin
import xlrd_get
import xlwt_write
import datetime



def lei(s):
    return '地面'

def center(box):
    if not box:
        return 0,0
    x = box.left+ box.width/2
    y = box.top+ box.height/2
    return x,y

def input(ls):
    for i in ls:
        pass

def clickUp(box):
    x,y = center(box)
    pag.moveTo(x,y,0.5)
    pag.click()
#屏幕大小 720*1280*240

def getTwo(s):
    if '窗户' in s:
        pag.click(x0+100,y0+121,duration=sd)
        pyperclip.copy('窗')
        pag.hotkey('ctrl','v')
        pag.hotkey('enter')
        return 'chuanghu.png'
    if '窗台' in s:
        pag.click(x0+100,y0+121,duration=sd)
        pyperclip.copy('窗')
        pag.hotkey('ctrl','v')
        pag.hotkey('enter')
        return 'chuangtai.png'
    if '地' in s:
        pag.click(x0+100,y0+121,duration=sd)
        pyperclip.copy('地')
        pag.hotkey('ctrl','v')
        pag.hotkey('enter')
        return 'dimian.png'
    if '墙' in s:
        pag.click(x0+100,y0+121,duration=sd)
        pyperclip.copy('墙')
        pag.hotkey('ctrl','v')
        pag.hotkey('enter')
        return 'qiangmian.png'

    return 'dimian.png'

def luru(ls):# [区域，位置，责任单位,问题描述]
    print("*****",ls)
    gnfq = (x0,y0+190)

    pag.click(gnfq,duration=sd)

    if pag.locateOnScreen(ls[0],confidence=0.8):
        box = pag.locateOnScreen(ls[0],confidence=0.8)
    else:
        pag.scroll(-200)
        box = pag.locateOnScreen(ls[0],confidence=0.8)
    clickUp(box)

    ls[1] = getTwo(ls[2])
    box = pag.locateOnScreen(ls[1],confidence=0.9)
    clickUp(box)

    reg_qita = (int(x0+104),int(y0+144),134,544)
    print(reg_qita)
    if pag.locateOnScreen('qita.png',region=reg_qita,confidence=0.8):
        box = pag.locateOnScreen('qita.png',region=reg_qita,confidence=0.8)
    else:
        pag.move(150,0,0.5)
        pag.scroll(-800)
        pag.scroll(-800)
        box = pag.locateOnScreen('qita2.png',region=reg_qita,confidence=0.8)
    clickUp(box)

    zrdw = (x0,y0+363)
    pag.click(zrdw,duration=sd)

    gx = (x0+330 , y0+65 )
    tj = (x0+290 , y0+65 )
    quanbu = (x0+50,y0+662)

    pag.click(gx,duration=sd)
    time.sleep(1.5)
    pag.click(quanbu,duration=sd)
    
    t = pag.locateAllOnScreen('duigou.png',confidence=0.95)
    t = list(t)
    print(len(t),"个对勾")
    for box in t:
        clickUp(box)

    box = pag.locateOnScreen(ls[3],confidence=0.7)
    clickUp(box)

    pag.click(tj,duration=sd)

    pag.moveTo(x0,y0+500)
    pag.click()
    pyperclip.copy(ls[2])
    pag.hotkey('ctrl','v')


#______________________________________读取数据-------------------

ls_data = xlrd_get.getall('数据.xlsx')
ls_in = []
ls_not = []
ls_one = ['入户门','玄关','客厅','客厅阳台','餐厅','厨房','过道','主卧','次卧','公卫','主卫','其他','工作阳台','书房','外立面']

idd = '0'
pag.PAUSE = 0.8
sd = 0.2
pag.FAILSAFE = False

for i in ls_data:
    box = pag.locateOnScreen('logo.png',confidence=0.8)
    x0,y0 = center(box)
    print(i)
    try:
        inputs = []
        p = Pinyin()
        num = str(int(i[0])) +str(int(i[1]))+str(int(i[2]))
        print(num,"*",idd)
        if idd != num:
            idd = num
            hao = str(int(i[0])) +"号楼"+str(int(i[1]))+"单元"+str(int(i[2]))
            #pag.alert(text=hao,title='录入',button='OK')
            flag = pag.confirm(text=hao+",请点对应户号点确定，结束点取消。",title='即将录入：',buttons=['OK','Cancel'])
            if flag == 'Cancel':
                break
            pag.moveTo(x0,y0,0.5)
            pag.click()
            box = pag.locateOnScreen('new.png',confidence=0.8)
            clickUp(box)

        if i[3] in ls_one:
            inputs.append(p.get_pinyin(i[3],'')+'.png')
        else:
            for s in ls_one:
                if s in i[4]:
                    p = Pinyin()
                    inputs.append(p.get_pinyin(s,'')+'.png')
                    break
            ls_not.append(i)
            continue

        inputs.append("")
        inputs.append(i[4])
        
        inputs.append(p.get_pinyin(i[5],'')+'.png')
        
        luru(inputs)
        ls_in.append(i)
               
    except Exception as e:
        ls_not.append(i)
        while not pag.locateOnScreen('jia.png',confidence=0.8):
            pag.click(x0+25,y0+62,duration=sd)
        print(e)

xlwt_write.writexls('本次录入_异常内容.xls',ls_not)
xlwt_write.writexls('本次录入_已录内容.xls',ls_in)
