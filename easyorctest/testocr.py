import easyocr

#reader = easyocr.Reader(['ch_sim','en'],gpu=False)
reader = easyocr.Reader(['en'],gpu=False)
#result = reader.detect('fff.PNG',mag_ratio=2,min_size=1)
result = reader.readtext('test.png',mag_ratio=2,batch_size=8,min_size=1,detail=0)

#print(result)

print("".join(result))
