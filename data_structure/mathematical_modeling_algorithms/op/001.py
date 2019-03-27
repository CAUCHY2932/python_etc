# -*- coding=utf-8 -*-
"""
    2019/3/11 15:04
    author:young
"""
import os
import shutil
import pandas as pd


def func(file_path, order_num, distinct_folder):
    """
        定义一个函数，用来选择文件路径下的第一个文件，复制，重命名，移动到指定文件夹
        传递路径，和单号命名
    :return:
    """

    path = os.listdir(file_path)
    if path and path[0]:
        shutil.copyfile(file_path + path[0], distinct_folder + order_num)


#
# def file_is_exists(function):
#     def wrapper():
#
#         print('')
#         function()
#     return wrapper


# demo
# def read_excel(file_name):
#     data=pd.read_excel(file_name)
#     df = pd.DataFrame(data)
#     # print(df.T)
#     for item in df.T:
#         print(df.T[item]['order_num'])


def read_excel(file_name):
    data = pd.read_excel(file_name)
    df = pd.DataFrame(data)
    df_transfer = df.T
    for item in df_transfer:
        # print(df_transfer[item])
        yield df_transfer[item]['path'], df_transfer[item]['order_num']


def run():
    """判断文件夹是否存在"""
    distinct_folder = 'D:/temporary'
    if not os.path.exists(distinct_folder):
        os.mkdir(distinct_folder)


if __name__ == "__main__":
    # run()
    tup = read_excel('./1.xls')
    # print(tup)
    for item in tup:
        print(item)