import ddddocr
import pyautogui as pag

##img = pag.screenshot(region=(608,621,100,37))
##img.save('yan1.png')

ocr = ddddocr.DdddOcr()
with open('yan.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)


print(res)
