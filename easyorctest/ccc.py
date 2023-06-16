import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pathlib import Path
from character import change_to_character, make_reader
from threading import Thread
import time

# class Showing(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         # self.img = tk.PhotoImage(file=r"C:\Users\yanhy\Desktop\捕获22.PNG")
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.img = tk.PhotoImage(file=r"C:\Users\yanhy\Desktop\捕获22.PNG")
#         self.img_wig = tk.Label(self, image=self.img)
#         self.img_wig.pack()


# 最外层窗口设置
root = tk.Tk()
root.title('图片文字识别程序                    联系：410889472@qq.com')
window_x = root.winfo_screenwidth()
window_y = root.winfo_screenheight()
WIDTH = 1200
HEIGHT = 750
x = (window_x - WIDTH) / 2  # 水平居中
y = (window_y - HEIGHT) / 3  # 垂直偏上
root.geometry(f'{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}')
root.resizable(width=False, height=False)

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
Row_space = 15
File_url_list = []
Img_type = ['.jpg', '.jpeg', '.png', '.gif']
Split_symbol = ' '                               # 间隔符。
Save_dir = Path.cwd().joinpath('img_to_word')
if Save_dir.is_dir():
    pass
else:
    Path.mkdir(Save_dir)

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》

def test():
    print(f'{Row_space=}')


def choose_file():       # 获取导入的图片路径地址
    global show_img, img_label, text, File_url_list
    filenames = filedialog.askopenfilenames()
    if len(filenames) == 1 and len(File_url_list) == 0:       # 单张图片导入，显示图片
        if Path(filenames[0]).suffix.lower() in Img_type:     # 判断是否图片类型
            File_url_list = list(filenames)
            try:
                if text.winfo_exists():
                    text.destroy()
            except NameError as e:
                print(f'choose_file提示：张图片导入错误>>> {e}')
            try:
                if img_label.winfo_exists():
                    img_label.destroy()
            except NameError as e:
                print(f'choose_file提示：单张图片导入错误>>> {e}')
            img = Image.open(File_url_list[0]).resize((560, 660))
            # print(img.size)
            show_img = ImageTk.PhotoImage(image=img)
            img_label = tk.Label(f_left, image=show_img)
            img_label.pack()
        else:
            print('导入的是非图像格式')
    else:                                     # 多张图片导入，显示列表。
        try:
            if img_label.winfo_exists():
                img_label.destroy()
        except NameError as e:
            print(f'提示：多张图片导入错误>>> {e}')
        try:
            if text.winfo_exists():
                text.destroy()
        except NameError as e:
            print(f'提示：多张图片导入错误>>> {e}')
        text = tk.Text(f_left, spacing1=5, spacing3=5)
        text.pack(fill='both', expand=True)


        for i in filenames:
            if Path(i).suffix.lower() in Img_type:
                File_url_list.append(i)
            else:
                pass
        File_url_list = set(File_url_list)
        for i in list(File_url_list):       # 把文件写入到文本框中
            text.insert('end', str(list(File_url_list).index(i)+1) + ": " + i + "\n")
        File_url_list = list(File_url_list)
    print(f'{File_url_list=}')


def choose_dir():
    global show_img, img_label, text, File_url_list
    directoryname = filedialog.askdirectory()
    print(f'{directoryname=}')
    try:
        if img_label.winfo_exists():
            img_label.destroy()
    except NameError as e:
        print(f'choose_dir提示：多张图片导入错误>>> {e}')
    try:
        if text.winfo_exists():
            text.destroy()
    except NameError as e:
        print(f'choose_dir提示：多张图片导入错误>>> {e}')
    text = tk.Text(f_left, spacing1=5, spacing3=5)
    text.pack(fill='both', expand=True)

    for i in Path(directoryname).iterdir():       # 获取文件夹下的所有文件。
        if Path(i).suffix.lower() in Img_type:
            File_url_list.append(i.as_posix())    # as_posix() 把Path型转为字符串。
        else:
            pass
    File_url_list = set(File_url_list)
    for i in list(File_url_list):  # 把文件写入到文本框中
        text.insert('end', str(list(File_url_list).index(i) + 1) + ": " + i + "\n")
    File_url_list = list(File_url_list)
    print(f'{File_url_list=}')


def clear_file_list():
    global File_url_list
    File_url_list.clear()
    try:
        if img_label.winfo_exists():
            img_label.destroy()
    except NameError as e:
        print(f'clear_file_list提示：清空错误>>> {e}')
    try:
        if text.winfo_exists():
            text.destroy()
    except NameError as e:
        print(f'clear_file_list提示：清空错误错误>>> {e}')


def get_entry1():       # 设置换行间距变量值
    global Row_space
    num = entry1.get()
    if num.isdigit():
        if int(num) > 0:
            Row_space = int(num)
    else:
        entry1.delete(0, "end")
        entry1.insert(0, 15)
        Row_space = 15


def set_split_symbol():
    global Split_symbol
    Split_symbol = entry2.get()
    print(f'{Split_symbol=}')


def do_change():
    if File_url_list:
        v.set("文字提取中,请稍后……")
        button_do.config(state='disable')        # 使按钮不可用。
        # ========================================
        def main():
            reader = make_reader()
            for i in File_url_list:
                content = change_to_character(i, reader, row_space=Row_space, split_symbol=Split_symbol, save_dir=Save_dir)
                read_text.delete(1.0, "end")
                for c in content:  # i 为每一行的内容
                    c.sort(key=lambda x: x[0][0][0])  # 对每行的内容进行先后排序
                    for r in c:
                        # print(r)
                        read_text.insert('end', r[1] + Split_symbol)
                    read_text.insert('end', "\n")
            v.set("文字提取结束。")
            button_do.config(state='normal')     # 恢复按钮可用。
        # ========================================
        t = Thread(target=main, daemon=True)
        t.start()

    else:
        v.set("请先选择图片！")


def join_file():
    v.set("文件开始合并。")
    filst = list(Path(Save_dir).iterdir())      # 获取文件夹中所有的文本文件。
    with open(f'{Save_dir}/合并文件.txt', 'w', encoding='utf8') as join_f:
        for f in filst:
            with open(f, 'r', encoding='utf8') as r_f:
                read_con = r_f.read()
            join_f.write(f.name+'\n'+read_con + '\n\n')
    time.sleep(1)
    v.set("文件合并完毕。")


# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
f_top = tk.Frame(root, height=65, width=1100, bd=1, relief="flat")  # "sunken" "raised"，"groove" 或 "ridge"
f_top.pack_propagate(False)  # 如果不加这个参数，当Frame框架中加入部件时，会自动变成底层窗口，自身的特性会消失。
f_top.pack(side='top', pady=5)

f_left = tk.Frame(root, height=660, width=560, bd=1, relief="groove")
f_left.pack_propagate(False)
f_left.pack(side='left', padx=20)

f_right = tk.Frame(root, height=660, width=560, bd=1, relief="groove")
f_right.pack_propagate(False)
f_right.pack(side='left', padx=20)

read_text = tk.Text(f_right, spacing1=5, spacing3=5)
read_text.pack(fill='both', expand=True)


# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
button_choose_file = tk.Button(f_top, text='选择图片', command=choose_file)
button_choose_file.pack(side='left', padx=10, ipadx=5)

button_choose_file = tk.Button(f_top, text='选择文件夹', command=choose_dir)
button_choose_file.pack(side='left', padx=10, ipadx=5)

button_clear_file = tk.Button(f_top, text='清空选择', bg='#FFEF2F', command=clear_file_list)
button_clear_file.pack(side='left', padx=5, ipadx=5)

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
f_row_content = tk.Frame(f_top, height=50, width=300, bg="#D1D4D0", relief="flat")  # "sunken" "raised"，"groove" 或 "ridge"
f_row_content.pack_propagate(False)
f_row_content.pack(side='left', padx=15)

button_set_row_height = tk.Button(f_row_content, text='设置行间距', command=get_entry1)
button_set_row_height.pack(side='left', ipadx=3, padx=3)

entry1 = tk.Entry(f_row_content, font=('', 18), width=3)
entry1.insert(0, 15)
entry1.pack(padx=5, side='left')

tk.Label(f_row_content, justify='left', text='填入像素值，设置换行间距。\n默认15个像素。').pack(side='left')

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
f_split = tk.Frame(f_top, height=50, width=215, bg="#D1D4D0", relief="flat")  # "sunken" "raised"，"groove" 或 "ridge"
f_split.pack_propagate(False)
f_split.pack(side='left', padx=4)

button_split = tk.Button(f_split, text='设置分隔符', command=set_split_symbol)
button_split.pack(side='left', ipadx=3, padx=3)

entry2 = tk.Entry(f_split, font=('', 18), width=3)
entry2.insert(0, ' ')
entry2.pack(padx=5, side='left')

tk.Label(f_split, justify='left', text='默认一个空格').pack(side='left')

# 《《《《《《《《《《《《《《《《《《《《《《  提取 合并文件  》》》》》》》》》》》》》》》》》》》》》》》》》
button_do = tk.Button(f_top, text='开始提取', bg='#4AB0FF', command=do_change)
button_do.pack(side='left', padx=10, ipadx=2)

button_join = tk.Button(f_top, text='合并文件', command=join_file)
button_join.pack(side='left', padx=5, ipadx=2)

v = tk.StringVar()
v.set('info……')
tk.Label(f_top, bg='#2EBD1D', justify='left', textvariable=v).pack(side='left')

# 《《《《《《《《《《《《《《《《《《《《《《  右键菜单  》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
def copy_text():
    read_text.event_generate("<<Copy>>")

menubar = tk.Menu(tearoff=False)
# root['menu'] = menubar      # 没有把这个 菜单部件 加入到 root 窗口的菜单属性中，所以它不会在root窗口的顶部显示。
menubar.add_command(label='复制', command=copy_text)

def show_menu(event):
    """用 菜单部件 的 post 方法展示菜单"""
    menubar.post(event.x_root, event.y_root)

read_text.bind('<Button-3>', show_menu)
# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》

root.mainloop()

