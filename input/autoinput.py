
import pyautogui as pag
import pyperclip
import time

while True:

    time.sleep(5)
    reg_input = (362,226,120,40)
    if not pag.locateAllOnScreen('input.png',region=reg,confidence=0.9):
        pag.alert(text='未检测到录入界面',title='提示消息',button='OK')
        break
        
    pag.PAUSE = 1
    step = 10

    pag.scroll(200)
    #1
    ps1_1 = (700,504)
    ps1_2 = (805,566)

    pag.moveTo(ps1_1,duration=0.5)
    pag.click(interval=0.1,clicks=3,button='left')
    pag.hotkey('ctrl','c')
    s1 = pyperclip.paste()
    s1 = s1[s1.rfind(',')+1:]
    pag.moveTo(ps1_2,duration=0.5)

    pag.click()
    pag.write(s1)
    pag.move(0,14,1)
    pag.click()

    #2
    ps2 = (1731,585)
    pag.moveTo(ps2,duration=0.5)
    pag.click()



    #3
    ps3 = (439,638)
    pag.moveTo(ps3,duration=0.5)
    pag.click()
    pag.write('222039')
    pag.move(0,14,1)
    pag.click()

    #4
    ps4_1 = (838,415)
    ps4_2 = (717,639)
    pag.moveTo(ps4_1,duration=0.5)
    pag.click(interval=0.1,clicks=3,button='left')
    pag.hotkey('ctrl','c')
    pag.moveTo(ps4_2,duration=0.5)
    pag.click()
    pag.hotkey('ctrl','v')

    #5
    ps5 = (1063,638)
    pag.moveTo(ps5,duration=0.5)
    pag.click()
    pyperclip.copy('涉及我国出口的其他运输方式的其他服务')
    pag.hotkey('ctrl','v')

    #6
    ps6 = (1752,277)
    pag.moveTo(ps6,duration=0.5)
    pag.click()

    #7
    ps7 = (1029,604)
    pag.moveTo(ps7,duration=0.5)
    pag.click()

    reg = (380,347,76,29)
    if not pag.locateAllOnScreen('1.png',region=reg,confidence=0.9):
        pag.alert(text='运行完成',title='提示消息',button='OK')
        break

    #8
    ps8 = (623,359)
    pag.moveTo(ps8,duration=0.5)
    pag.click()




