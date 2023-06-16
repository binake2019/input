import xlwt
import os
import xlsxwriter

def writexls(path,list_value):
  if os.path.exists(path):
    os.remove(path)
  elif '.xlsx' in path:
    wookbook = xlsxwriter.Workbook(path)
    sheet1 = wookbook.add_worksheet('Sheet1')
    for i in range(len(list_value)):
      try:
        sheet1.write_row(i,0,list_value[i])
      except:
        pass
    wookbook.close()
    print("生成文件成功：", path)
  else:
    workbook = xlwt.Workbook ("utf-8")
    my_sheet = workbook.add_sheet("Sheet1")

    i = 0
    for row in list_value:
      j = 0
      for col in row:
        my_sheet.write(i,j,col)
        j += 1
      i += 1
    workbook.save (path)
    print("生成文件成功：",path)

