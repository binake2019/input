#
import xlrd_get
import pyautogui as pag
import pyperclip
import time




def write(data,ls):
    
    pag.PAUSE = 1
    x,y = (288,188)
    hd = 20
    sd = 1
    pag.click(x,y,duration=sd)
    pag.click()
    pag.write(data[0])#房号

    pag.move(0,hd)
    pag.click()
    pag.write(data[1])#身份证号

    pag.move(0,4*hd)
    pag.click()
    pyperclip.copy(data[6])#详细地址
    pag.hotkey('ctrl','v')
    
    pag.click(x+250,y+hd)
    pyperclip.copy(data[2])
    pag.hotkey('ctrl','v')#姓名

    pag.move(0,2*hd)
    pag.click()
    count = 99
    if '族' not in data[5]:
        mz = data[5] + "族"
    else:
        mz = data[5]
    if mz in ls:
        count = str(ls.index(mz) + 1)
        if len(count) == 1:
            count = str(0) + str(count)
    pag.write(count)
    time.sleep(1)
    pag.press('enter')
    pag.move(-50,0)
    pag.click()#民族
        
    pyperclip.copy(data[5])
    pag.hotkey('ctrl','v')

    end = (631,403)
    pag.moveTo(end)
    
ls = xlrd_get.getall('123导出人口信息查询的户籍人口_平庄镇.xlsx')
ls_jieguo = []

f = open('minzu.txt','r',encoding='utf-8')
s = f.readlines()
ls_mz = s[0].split('、')


for i in ls:
    try:
        data = ['','','','','','','']

        data[0] = str(int(i[0])) # 房间号
        data[1] = str(i[12]) #身份证号
        data[2] = i[6] #姓名
        data[5] = i[8] #民族
        data[6] = str(i[1])+str(i[2])+str(i[3]) #详址
        print(data)
        ls_jieguo.append(data)
    except:
        pass

for data in ls_jieguo:
    if data[0] == '房间号':
        continue
    write(data,ls_mz)
