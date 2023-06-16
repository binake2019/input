
import pyautogui as pag
import pyperclip
import time

    
while True:

    time.sleep(5)
    #reg_input = (356,220,800,400)
##    t = pag.locateOnScreen('input.png',confidence=0.7)
##    if not t:
##        pag.alert(text='未检测到录入界面',title='提示消息',button='OK')
##        break
        
    pag.PAUSE = 1
    step = 10

    pag.scroll(200)
    #1
    ps1_1 = (490,447)
    ps1_2 = (524,523)

    pag.moveTo(ps1_1)
    pag.click(interval=0.1,clicks=3,button='left')
    pag.hotkey('ctrl','c')
    s1 = pyperclip.paste()
    s1 = s1[s1.rfind(',')+1:]
    pag.moveTo(ps1_2)

    pag.click()
    pag.write(s1)
    pag.move(0,14,1)
    pag.click()

    #2
    ps2 = (1239,542)
    pag.moveTo(ps2)
    pag.click()



    #3
    ps3 = (234,630)
    pag.moveTo(ps3)
    pag.click()
    pag.write('222039')
    pag.move(0,14,1)
    pag.click()

    #4
    ps4_1 = (572,346)
    ps4_2 = (480,601)
    pag.moveTo(ps4_1)
    pag.click(interval=0.1,clicks=3,button='left')
    pag.hotkey('ctrl','c')
    pag.moveTo(ps4_2)
    pag.click()
    pag.hotkey('ctrl','v')

    #5
    ps5 = (729,603)
    pag.moveTo(ps5)
    pag.click()
    pyperclip.copy('涉及我国出口的其他运输方式的其他服务')
    pag.hotkey('ctrl','v')

    #6
    ps6 = (1227,189)
    pag.moveTo(ps6)
    pag.click()

    #7
    ps7 =(735,453)
    pag.moveTo(ps7)
    pag.click()

    reg =(197,259,60,29)
    if not pag.locateOnScreen('1.png',region=reg,confidence=0.7):
        pag.alert(text='运行完成',title='提示消息',button='OK')
        break

    #8
    ps8 =(353,271)
    pag.moveTo(ps8)
    pag.click()




