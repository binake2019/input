import pyautogui as pag
import pyperclip
import time
from xpinyin import Pinyin
import xlrd_get
import xlwt_write
import datetime


time.sleep(5)
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
#屏幕大小 手机版1080*1920

def getTwo(s):
    dic ={'保洁':[],
          '吊柜':[],
          '地暖':[],
          '地柜':[],
          '地面':['地'],
          '墙面':['墙'],
          '天花':[],
          '屋面':[],
          '推拉门':[],
          '新风系统':[],
          '电器':['电'],
          '空调机位':[],
          '窗台':['飘'],
          '窗帘盒':[],
          '窗户':['窗'],
          '排水系统':['地漏'],
          '美缝':[],
          '楼梯':[],
          '太阳能':[],
          '平开门':['门','把手'],
          '护栏':['栏杆'],
          '五金洁具':[],
          '入户门':[],
          '淋浴屏':['浴']
##          '':[],
##          '':[],
##          '':[],
##          '':[],
##          '':[],
        }
    for key in dic.keys():
        if key in s:
            return key
        else:
            for i in dic[key]:
                if i in s:
                    return key    
    return '其他'

def luru(ls):# [区域，位置，责任单位,问题描述]
    print("*****",ls)
    gnfq = pag.locateOnScreen('pic\\gongnengfenqu.png',confidence=0.8)

    pag.click(center(gnfq),duration=sd)

    if pag.locateOnScreen("pic\\one\\"+ls[0],confidence=0.8):
        box = pag.locateOnScreen("pic\\one\\"+ls[0],confidence=0.8)
    else:
        pag.scroll(-200)
        box = pag.locateOnScreen("pic\\one\\"+ls[0],confidence=0.8)
    clickUp(box)

    if ls[1] == "qita.png":
        if pag.locateOnScreen("pic\\two\\qita1.png",confidence=0.8):
            box = pag.locateOnScreen("pic\\two\\qita1.png",confidence=0.8)
        elif pag.locateOnScreen("pic\\two\\qita2.png",confidence=0.8):
            box = pag.locateOnScreen("pic\\two\\qita2.png",confidence=0.8)
        else:
            pag.moveTo(x0+240 ,y0+240 ,duration=sd)
            pag.scroll(-200)
            pag.scroll(-200)
            if pag.locateOnScreen("pic\\two\\qita1.png",confidence=0.8):
                box = pag.locateOnScreen("pic\\two\\qita1.png",confidence=0.8)
            else :
                box = pag.locateOnScreen("pic\\two\\qita2.png",confidence=0.8)
        
    else:
        if pag.locateOnScreen("pic\\two\\"+ls[1],confidence=0.8):
            box = pag.locateOnScreen("pic\\two\\"+ls[1],confidence=0.8)
        else:
            pag.scroll(-200)
            pag.scroll(-200)
            box = pag.locateOnScreen("pic\\two\\"+ls[1],confidence=0.8)
    clickUp(box)

    reg_qita = (int(x0+157),int(y0+183),190,800)
    #print(reg_qita)
    if pag.locateOnScreen('pic\\three\\qita1.png',region=reg_qita,confidence=0.8):
        box = pag.locateOnScreen('pic\\three\\qita1.png',region=reg_qita,confidence=0.8)
    else:
        pag.move(150,0,0.5)
        pag.scroll(-400)
        pag.scroll(-400)
        box = pag.locateOnScreen('pic\\three\\qita2.png',region=reg_qita,confidence=0.8)
    clickUp(box)

    time.sleep(0.5)
    while pag.locateOnScreen('pic\\qingshaohou.png',confidence=0.8):
        print("等待提交中")
        time.sleep(3)

    zrdw = pag.locateOnScreen('pic\\zerendanwei.png',confidence=0.8)
    pag.click(center(zrdw),duration=sd)

    gx = pag.locateOnScreen('pic\\gengxin.png',confidence=0.8)
    tj = pag.locateOnScreen('pic\\tijiao.png',confidence=0.8)
    quanbu = pag.locateOnScreen('pic\\quanbu.png',confidence=0.8)

    pag.click(center(gx),duration=sd)
    time.sleep(1.5)
    pag.click(center(quanbu),duration=sd)
    
    t = pag.locateAllOnScreen('pic\\duigou.png',confidence=0.97)
    t = list(t)
    #print(len(t),"个对勾")
    for box in t:
        clickUp(box)

    box = pag.locateOnScreen("pic\\zrdw\\"+ls[3],confidence=0.7)
    clickUp(box)

    pag.click(tj,duration=sd)
    while pag.locateOnScreen('pic\\qingshaohou.png',confidence=0.8):
        print("等待提交中")
        time.sleep(2)
    
    pag.moveTo(x0,y0+600)
    pag.click()
    pyperclip.copy(ls[2])
    pag.hotkey('ctrl','v')

    box = pag.locateOnScreen('pic\\tijiao.png',confidence=0.8)
    clickUp(box)
    time.sleep(0.5)
    while pag.locateOnScreen('pic\\qingshaohou.png',confidence=0.8):
        print("等待提交中")
        time.sleep(5)



#______________________________________读取数据-------------------

ls_data = xlrd_get.getall('数据.xlsx')
ls_in = []
ls_not = []
dict_one = {'入户门':[],
          '玄关':[],
          '客厅':[],
          '客厅阳台':['景观阳台','阳台','生活阳台'],
          '餐厅':[],
          '厨房':[],
          '过道':[],
          '主卧':[],
          '次卧':['儿童房','书房','老人房'],
          '公卫':['次卫'],
          '主卫':[],
          '其他':[],
          '工作阳台':[],
          '书房':[],
          '外立面':[]}

idd = '0'
pag.PAUSE = 0.6
sd = 0.1
pag.FAILSAFE = False

for i in ls_data:
    box = pag.locateOnScreen('pic\\logo.png',confidence=0.8)
    x0,y0 = center(box)
    print(i)
    try:
        inputs = []
        p = Pinyin()
        num = str(int(i[0])) + str(int(i[1])) + str(int(i[2]))
        print(num,"*",idd)
        if idd != num:
            idd = num
            if pag.locateOnScreen('pic\jia.png',confidence=0.8):
                pag.click(x0,y0+72,duration=sd)
                time.sleep(0.5)
                box = pag.locateOnScreen('pic\shi.png',confidence=0.9)
                clickUp(box)
                pag.click(x0,y0+72,duration=sd)

            hao = str(int(i[0])) +"号楼"+str(i[1])+"单元"+str(int(i[2]))
            #pag.alert(text=hao,title='录入',button='OK')
            flag = pag.confirm(text=hao+",请点对应户号点确定，结束点取消。",title='即将录入：',buttons=['OK','Cancel'])
            if flag == 'Cancel':
                break
            pag.moveTo(x0,y0,0.5)
            pag.click()
            if pag.locateOnScreen('pic\\new1.png',confidence=0.7):                
                box = pag.locateOnScreen('pic\\new1.png',confidence=0.7)
            else:
                box = pag.locateOnScreen('pic\\new2.png',confidence=0.7)
            clickUp(box)

        if i[3] == "":
            for key in dict_one.keys():
                if key in i[4]:
                    inputs.append(p.get_pinyin(key,'')+'.png')
                    break
                for ss in dict_one[key]:
                    if ss in i[4]:
                        inputs.append(p.get_pinyin(key,'')+'.png')
                        break
                if len(inputs) == 1:
                    break
        else:
            for key in dict_one.keys():                
                if key in i[3]:
                    inputs.append(p.get_pinyin(key,'')+'.png')
                    break
                if i[3] in dict_one[key]:
                    inputs.append(p.get_pinyin(key,'')+'.png')
                    break
                
        if len(inputs) == 0:
            inputs.append('qita.png')

        inputs.append(p.get_pinyin(getTwo(i[4]),'')+'.png')
        inputs.append(i[4])
        
        inputs.append(p.get_pinyin(i[5],'')+'.png')
        
        luru(inputs)
        ls_in.append(i)
        print("提交完成")       
    except Exception as e:
        ls_not.append(i)
##        while not pag.locateOnScreen('pic\\jia.png',confidence=0.8):
##            if pag.locateOnScreen('pic\\new1.png',confidence=0.8) or pag.locateOnScreen('pic\\new2.png',confidence=0.8):
##                break
##            pag.click(x0,y0+72,duration=sd)
        print(e)

        xlwt_write.writexls('本次录入_异常内容.xls',ls_not)
        xlwt_write.writexls('本次录入_已录内容.xls',ls_in)
xlwt_write.writexls('本次录入_异常内容.xls',ls_not)
xlwt_write.writexls('本次录入_已录内容.xls',ls_in)
