import xlrd
import os

#获取value所在的表格位置
def getps(path,value):
    if os.path.exists (path):

        list_ps = []
        
        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():        
            sheet = workbook.sheet_by_name(name)
            list_sheet = []
            list_sheet.append(name)
            for row in range(sheet.nrows):
                if value in sheet.row_values(row):
                    a = row
                    b = sheet.row_values(row).index(value)
                    list_sheet.append((a,b))
            list_ps.append(list_sheet)
            return list_ps
    else:
        print("文件路径错误")

#获取含有value的所有行
def getvl(path,value):
    if os.path.exists (path):
        list_value = []
        list_ps = []

        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(name)
            list_sheet = []
            list_sheet.append(name)
            for row in range(sheet.nrows):
                #模糊搜索
                for v_r in sheet.row_values(row):
                    if value in str(v_r):
                        a = row
                        b = sheet.row_values(row).index(v_r)
                        list_sheet.append((a,b))
                        break
            list_ps.append(list_sheet)
        #取数据
        for name in list_ps:
            sheet = workbook.sheet_by_name(name[0])
            for pos in name[1:]:
                list_value.append(sheet.row_values(pos[0]))
        return list_value
    else:
        print("文件路径错误")

#获取不含有value的所有行
def getnovl(path,value):
    if os.path.exists (path):
        list_value = []
        list_ps = []

        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(name)
            list_sheet = []
            list_sheet.append(name)
            for row in range(sheet.nrows):
                #模糊搜索
                biaozhi=0
                for v_r in sheet.row_values(row):
                    if value in str(v_r):
                        biaozhi=1
                        break
                if ( biaozhi == 0) :
                    a = row
                    b = sheet.row_values(row).index(v_r)
                    list_sheet.append((a,b))
            list_ps.append(list_sheet)
        #取数据
        for name in list_ps:
            sheet = workbook.sheet_by_name(name[0])
            for pos in name[1:]:
                list_value.append(sheet.row_values(pos[0]))
        return list_value
    else:
        print("文件路径错误")


#获取col列含有[value1,value2,....]的所有行
def get_col_lv(path, col, lv):
    list_value = []
    if os.path.exists (path) and type(col) == int and type(lv) == list:
        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(name)
            for row in range(sheet.nrows):
                if sheet.row_values(row)[col] in lv:                    
                    list_value.append(sheet.row_values(row))
    else:
        print("参数错误")
    return list_value

#获取col列不含有[value1,value2,....]的所有行
def get_col_nolv(path, col, lv):
    list_value = []
    if os.path.exists (path) and type(col) == int and type(lv) == list:
        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(name)
            for row in range(sheet.nrows):
                if sheet.row_values(row)[col] not in lv:                    
                    list_value.append(sheet.row_values(row))
    else:
        print("参数错误")
    return list_value

#获取col列不含value的所有行
def get_col_novl(path, col, value):
    if os.path.exists (path):
        list_value = []
        list_ps = []

        workbook = xlrd.open_workbook (path)
        for name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(name)
            list_sheet = []
            list_sheet.append(name)
            # 如果col是列名称，转换为列数字
            if isinstance(col, str):
                col = sheet.row_values(0).index(col)
            for row in range(sheet.nrows):
                if value not in sheet.row_values(row)[col]:
                    a = row
                    b = col
                    list_sheet.append((a,b))
            list_ps.append(list_sheet)
        #取数据
        for name in list_ps:
            sheet = workbook.sheet_by_name(name[0])
            for pos in name[1:]:
                list_value.append(sheet.row_values(pos[0]))
        return list_value
    else:
        print("文件路径错误")

#获取col的所有值
def getcol(path, col):
    list_value = []
    workbook = xlrd.open_workbook(path)
    for name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(name)
        # 如果col是列名称，转换为列数字
        if isinstance(col, str):
            col = sheet.row_values(0).index(col)
        list_value = sheet.col_values(col)

    return list_value

#获取表格所有行
def getall(path):
    list_value = []
    workbook = xlrd.open_workbook(path)
    for name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(name)
        for row in range(sheet.nrows):
            list_value.append(sheet.row_values(row))
    return list_value
