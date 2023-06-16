# 测试文件是否完整

import os


def dct(root):
    comd1 = ['xl','tj','sq','sf']
    comd2 = ['sf','tj','sq']
    flag = 0    

    for name in os.listdir(root):
        ls = os.listdir(os.path.join(root,name))
        p_docx = os.path.join(root,name,name+".docx")
        if os.path.exists(p_docx):
            msg = 'xc' # getinfo(p_docx)
        else:
            print(name ,"缺少 同名docx文件,请检查")
            

        if msg == 'xc':
            for i in comd1:
                if i+'.jpg' not in ls:
                    print(name,'缺失:',i+'.jpg 文件')
                    flag = 1
                    
        if msg == 'aq':
            for i in comd1:
                if i+'.jpg' in ls:
                    continue
                else:
                    print(name,'缺失:',i+'.jpg 文件')
                    flag = 1
    return flag
