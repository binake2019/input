
from threading import Thread
import time
import psutil
import keyboard
import pyautogui as pag

def hao():
    while True:
        keyboard.wait('p')
        msg = input("暂停,继续请按enter")
        if msg == 'd':
            break
        elif msg == 'e':
            sys.exit(0)

def sing(num, name):
    for i in range(num):
        print(name,i)
        print("---i am sing ooo~")
        pag.click(100*i,500)
        time.sleep(1)
        
 
 
def dance(num, name):
    for i in range(num):
        print(name,i)
        print("i am dance lll~")
        time.sleep(1)
 
 
if __name__ == '__main__':
    sing_process = Thread(target=sing, args=(10, "猪猪"))
    dance_process = Thread(target=dance, kwargs={"name": "珊珊", "num": 16})
    hao = Thread(target=hao)

    hao.start()
    sing_process.start()
    dance_process.start()

##    sing_process.join()
##    dance_process.join()
    hao.join()
    print("main")

else:
    print ("****")

