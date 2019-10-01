# -*- coding:utf-8 -*-

"""
    2019/4/22 17:09 by young
"""
import pickle

"""
file.tell()指明文件的指针
file.seek()寻找文件的位置
file.seek(0)找到文件的头


"""


def file_read_continue(file_name, read_num):
    with open(file_name, 'r') as f:
        file_pointer, k = 0, 0

        line, file_pointer, k = f.readline(), f.tell(), k + 1
        while k <= read_num and line:
            yield line
            line, file_pointer, k = f.readline(), f.tell(), k + 1


def dump_to_pickle(kv_dict, file_name):
    with open(file_name, 'wb') as pf:
        return pickle.dump(kv_dict, pf)


def load_from_pickle(file_name):
    with open(file_name, 'rb') as pf:
        return pickle.load(pf)
