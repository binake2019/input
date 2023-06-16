# 分为：迟到 、早退、脱岗
import mkdir
import os
import xlrd_get
import xlrd
import xlwt_write
import datetime 
import pickle

start = datetime.datetime.now()
time = start.strftime("%Y%m%d_%H%M%S")

# 2022年3月1日更新，只保留迟到、早退功能。
# 保存数据 加载完的数据会形成一个.pkl的包在结果文件目录里，更新数据时删除即可
def save_dict(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# 加载数据
def load_dict(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# 统计迟到早退 函数
def late_or_early(ls,date):
    a=0 # 不迟到
    b=0 # 不早退
    first_in = ""
    last_out = ""
    try:
        ls = sorted(ls)

        #迟到、早退时间段
        late = [date+" 08:30:00",date+" 09:30:00"]
        early = [date+" 16:30:00",date+" 17:30:00"]
        #print(late,early)
        #找出第一个“进”记录

        for i in ls:
            if i[1] == "进":
                first_in = i[0]
                break
        #找出最后一个“出”记录

        for i in sorted(ls,reverse=True):
            if i[1] == "出":
                last_out = i[0]
                break
        if late[0] < first_in <late[1]:
           a = 1 
        if early[0] < last_out <early[1]:
            b = 1
        return a,b,first_in,last_out
    except Exception as e:
        print("迟到早退函数异常",e)
        return a,b,first_in,last_out

        
# _______________________________________程序从这里开始_____________________________________________________________


# 统计的门禁数据筛选，这里全部时西门的数据
ls_ximen = ['（A）西大门行人小门-出',
            '（A）西门二通道出',
            '（A）西门二通道进',
            '（A）西门三通道出',
            '（A）西门三通道进',
            '（A）西门四通道出',
            '（A）西门四通道进',
            '（A）西门五通道出',
            '（A）西门五通道进',
            '（A）西门一通道出',
            '（A）西门一通道进',
            '（B）西大门行人小门-进']
path_data_ren = 'D:\\综合处脚本\\门禁考勤\\72号院西大门数据\\人员'
path_data_che = 'D:\\综合处脚本\\门禁考勤\\72号院西大门数据\\车辆'
path_jieguo = 'D:\\综合处脚本\\门禁考勤\\门禁分析结果'
mkdir.mk(os.path.join(path_jieguo, time))  # 加入一个文件夹，用于存放每一次的跑的结果


# 加载人员数据
dic_data = dict()  # {编号：所有门禁数据}
dic_ren = dict()  # 数据结构:{[姓名,所在群]：D}  D={日期:[门禁数据1,2,3....]}
name1 = 'data'
name2 = 'ren'
os.chdir(path_jieguo)
list_renyuan = []

#读取数据
for path in os.listdir(path_data_ren):
    os.chdir(path_data_ren)
    list_tem = xlrd_get.get_col_lv(path, 1, ls_ximen)
    for i in list_tem:
        list_renyuan.append([i[4], i[0], i[9],i[6],i[3]])
#处理数据
for i in list_renyuan:
    # print(i)
    name = i[0]
    date = i[1][:10]
    cmp = i[3]
    k_id = i[4]
    key = name+"@"+cmp+"@"+k_id 
    if key not in dic_ren.keys():
        dic_ren[key] = dict()
    if date not in dic_ren[key].keys():
        dic_ren[key][date] = []
    dic_ren[key][date].append([i[1], i[2]])

##for i in dic_ren.keys():
##    for j in dic_ren[i].keys():
##        for k in sorted(dic_ren[i][j]):
##            print(k)
##    break

# 开始判断迟到早退
list_jieguo = [["姓名","日期","所在群","类型","打卡时间","工卡号"]]
for key in dic_ren.keys():
    ls = key.split("@")
    name = ls[0]
    cmp = ls[1]
    k_id = ls[2]
    for date in dic_ren[key].keys():
        result = late_or_early(dic_ren[key][date],date)
        if result[0]:
            list_jieguo.append([name,date,cmp,"迟到",result[2],k_id])
        if result[1]:
            list_jieguo.append([name,date,cmp,"早退",result[3]],k_id)


path_jieguo = os.path.join(path_jieguo, time, '迟到早退明细.xls')
xlwt_write.writexls(path_jieguo,list_jieguo)
print("共耗时：",(datetime.datetime.now() - start).seconds,"秒")
