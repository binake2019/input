from pathlib import Path
import easyocr


file_url = r'识别图片.jpg'    # 需识别的图片
split_symbol = ' '          # 默认空格为分隔符
row_space = 15              # 默认字符高度为15px，当识别出来的字符间距超过这个数值时会换行。


def make_reader():
    # 将模型加载到内存中。模型文件地址 C:\Users\用户\.EasyOCR\model
    reader = easyocr.Reader(['ch_sim', 'en'])
    return reader


def change_to_character(file_url, reader, split_symbol=' ', row_space=15, save_dir='.'):
    with open(file_url, "rb") as img:
        img_b = img.read()
    result = reader.readtext(img_b)

    result.sort(key=lambda x: x[0][0][1])  # 按竖直方向，进行排序==>进行分行处理。
    # for i in result:
    #     print(i)
    # print('='*100)

    # 按行进行分组
    content = []
    item = [result[0]]  # 首先放入第一个元素
    for i in result[1:]:
        if row_space >= i[0][0][1] - item[-1][0][0][1] >= 0:
            item.append(i)
        else:
            content.append(item)
            item = [i]
    content.append(item)

    filemane = Path(file_url).name.split('.')[0]
    with open(f'{save_dir}/{filemane}.txt', "w", encoding='utf8') as t:
        for i in content:                     # i 为每一行的内容
            i.sort(key=lambda x: x[0][0][0])  # 对每行的内容进行先后排序
            for r in i:
                # print(r)
                t.write(r[1] + split_symbol)
            t.write("\n")
    return content


if __name__ == "__main__":
    change_to_character(file_url,  make_reader())
