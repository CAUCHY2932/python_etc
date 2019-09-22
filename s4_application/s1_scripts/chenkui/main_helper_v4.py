# coding:utf-8
import pandas as pd
import numpy as np

def split_table():
    print("[提示]--请输入要拆分的路径名--\n")
    a = input(r'[提示]--如：c:\user\lvyangyang\desktop\拆分物流码模块.xlsx'+'\n').strip()
    if not a:
        print('请输入文件名！\n')
        return None
    try:
        print('[提示]-正在进行读取...\n')
        df = pd.read_excel(a)
        print('[成功]-读取完成')
    except Exception as e:
        print('[错误]-你输入的路径不合法或格式不正确，请重新确认！\n', e)
        return None

    print('[提示]-您拆分的表的字段如下:\n')
    column_list = [column for column in df]
    for index, name in enumerate(column_list):
        print('{}: {}'.format(index, name))

    try:
        print('[提示]-请输入要拆分的某个字段:\n')
        split_column = input('如: 0: 办事处，要拆分办事处，就输入0\n').strip()
        if not split_column:
            return None
        print('[处理]-正在进行字段拆分...\n')
        split_column_index = column_list[eval(split_column)]
        df[split_column_index] = [x.split(',') for x in df[split_column_index]]
    except Exception as e:
        print('[错误]-拆分字段错误，请确定字段内容是否合法\n', e)
        return None

    print('[处理]-正在进行后处理...\n')
    # 转换成列表
    py_list = np.array(df).tolist()

    # 生成器
    new_list = (item[:-1]+[i] for item in py_list for i in item[-1])

    print('[完成]-已经完成处理，前十条结果如下：\n')
    print(column_list)
    n = 1
    for i in new_list:
        print(i)
        n = n + 1
        if n > 10:
            return None


if __name__ == "__main__":
    split_table()
