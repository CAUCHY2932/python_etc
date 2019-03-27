# -*- coding=utf-8 -*-
"""
    2019/3/11 15:04
    author:young
"""
import os
import shutil
import pandas as pd
from config_constructure import destination_folder, success_file, failed_file




def func_2(file_path, order_num, distinct_folder):
    """
        定义一个函数，用来选择文件路径下的第一个文件，复制，重命名，移动到指定文件夹
        传递路径，和单号命名
    :return:
    """
    # origin_path = file_path
    origin_order_num = order_num
    try:
        if os.path.isfile(file_path):
            _, suffix = os.path.splitext(file_path)
            new_file_name = order_num.strip() + suffix
            new_file_path = os.path.join(destination_folder, new_file_name)
            shutil.copyfile(file_path, new_file_path)
            print('have copy a file which named {} to destination'.format(new_file_name))
            with open(success_file, 'a+') as f:
                f.write(new_file_name+'\n')
            return True

        elif os.path.isdir(file_path):
            file = os.listdir(file_path)
            if file and file[0]:
                _, suffix = os.path.splitext(file[0])
                new_file_name = order_num.strip() + suffix
                new_file_path = os.path.join(destination_folder, new_file_name)
                shutil.copyfile(os.path.join(file_path, file[0]), new_file_path)
                print('have copy a file which named {} to destination'.format(new_file_name))
                with open(success_file, 'a+') as f:
                    f.write(new_file_name+'\n')
                return True
            else:
                with open(failed_file, 'a+') as f:
                    f.write(origin_order_num+'\n')
                return False
        else:
            with open(failed_file, 'a+') as f:
                f.write(origin_order_num+'\n')
            print('[find-error]-{}'.format(file_path))
            return False
    except Exception as e:
        with open(failed_file, 'a+') as f:
            f.write(origin_order_num+'\n')
        print('[error]-{}'.format(e))
        return False

# def get_suffix(file_name, new_name):
#     pre, suffix = os.path.splitext(file_name)
#     return str(new_name.strip()) + suffix


def read_excel(file_name):
    data = pd.read_excel(file_name)
    df = pd.DataFrame(data)
    df_transfer = df.T
    for item in df_transfer:
        yield df_transfer[item]['path'], df_transfer[item]['order_num']


def run():
    """判断文件夹是否存在"""
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)


def go():

    run()
    tup = read_excel('./1.xls')
    total, success_num, failed_num = 0, 0, 0
    for item in tup:
        status = func_2(item[0], item[1], destination_folder)
        if status:
            success_num += 1
        else:
            failed_num += 1
        total += 1
    print('have transmit {} files!\n success num is {},\n failed num is {}\n'.format(total, success_num, failed_num))
    pass


if __name__ == "__main__":
    go()
        