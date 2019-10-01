# -*- coding=utf-8 -*-
"""
    2019/3/11 15:04
    author:young
"""
import os
import shutil
import pandas as pd
from config_new import destination_folder, true_file, error_file
import time


def func(file_path, order_num, distinct_folder):
    """
        定义一个函数，用来选择文件路径下的第一个文件，复制，重命名，移动到指定文件夹
        传递路径，和单号命名
    :return:
    """
    # try:
    #     path = os.listdir('./'+file_path)
    #
    #     if path and path[0]:
    #         new_path_name = get_suffix(path, order_num)
    #         new_path = os.path.join(distinct_folder, new_path_name)
    #         shutil.copyfile(file_path + path[0], new_path)
    # except Exception as e:
    #     print(e)

    # try:
    origin_path = file_path
    origin_order_num = order_num

    if file_path[-1]!='/':
        str_split=file_path.split('/')[:-1]
        file_path='/'.join(str_split)+'/'
    try:
        path = os.listdir(file_path)
    except Exception as e:
        with open(error_file, 'a+')as ferror:
            ferror.write("{},{}".format(origin_order_num, origin_path )+ '\n')
        print('[filepath-error]', e)
        return None
    if path and path[0]:
        new_path_name = get_suffix(path[0], order_num)
        try:
            new_path = os.path.join(destination_folder, new_path_name)
        except Exception as e:
            print(e)
        try:
            shutil.copyfile(file_path + path[0], new_path)
            print('[success]-have copy a file which named {} to distinction'.format(path[0]))
            with open(true_file, 'a+') as f:
                f.write(new_path_name + '\n')
        except Exception as e:
            with open(error_file, 'a+')as ferror:
                ferror.write("{},{}".format(origin_order_num, origin_path )+ '\n')
            print('[error]-', e)
            pass


def get_suffix(file_name, new_name):
    pre, suffix = os.path.splitext(file_name)
    return str(new_name.strip()) + suffix


def read_excel(file_name):
    data = pd.read_excel(file_name)
    df = pd.DataFrame(data)
    df_transfer = df.T
    for item in df_transfer:
        # print(df_transfer[item])
        yield df_transfer[item]['path'], df_transfer[item]['order_num']


def run():
    """判断文件夹是否存在"""
    # destination_folder = 'D:/temporary'
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)


if __name__ == "__main__":
    run()
    tup = read_excel('./1.xls')
    n=0
    for item in tup:
        # destination_folder = 'D:/temporary'
        # print(item[0], item[1])
        func(item[0], item[1], destination_folder)
        n+=1
    print('have transmit {} files!'.format(n))
    # print(tup)
    # for item in tup:
    #     print(item)
