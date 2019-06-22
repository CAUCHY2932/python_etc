# -*- coding:utf-8 -*-

"""
    2019/4/22 17:09 by young
"""
import pickle
import random
import string

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


def file_read_continue2(file_name, read_num, value_file):
    """read data from a file, give a read num, and write
    file pointer to value file

    :param file_name: a file waiting for read
    :param read_num: a num want to read from file
    :param value_file: a file to store file pointer
    :return:
    """
    with open(file_name, 'r') as f:
        file_pointer, k = 0, 0

        line, file_pointer, k = f.readline(), f.tell(), k + 1

        dump_to_pickle({
            'fp': file_pointer,
        }, value_file)

        while k <= read_num and line:
            yield line
            line, file_pointer, k = f.readline(), f.tell(), k + 1
            dump_to_pickle({
                'fp': file_pointer,
            }, value_file)


def file_seek_read(file_name, read_num, value_file):

    file_pointer = load_from_pickle(value_file).get('fp', 0)
    with open(file_name, 'r') as f:
        f.seek(file_pointer)
        k = 0

        line, k = f.readline(), k + 1
        while k <= read_num and line:
            yield line
            line, file_pointer, k = f.readline(), f.tell(), k + 1
            dump_to_pickle({
                'fp': file_pointer,
            }, value_file)


def dump_to_pickle(kv_dict, file_name):
    with open(file_name, 'wb') as pf:
        return pickle.dump(kv_dict, pf)


def load_from_pickle(file_name):
    with open(file_name, 'rb') as pf:
        return pickle.load(pf)


def gen_random_str(length):
    """
    生成任意长度的字符串
    :param length: 字符串长度
    :return:
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def main_func():
    with open('./fake_data.csv', 'a') as f:
        for item in range(100000):
            f.write(gen_random_str(20) + '\n')


def gen_order_data():
    with open('./order_data.csv', 'w') as f:
        for item in range(100000):
            order = '{0:0>16}'.format(item)
            f.write(order + '\n')
            print(order)


def go(read_file_name, value_file):
    lines = file_read_continue2(read_file_name, read_num=100000, value_file=value_file)
    k = 0
    for line in lines:
        print(line)
        k += 1
        print('have print {} record'.format(k))


def go_continue(read_file_name, value_file):
    lines = file_seek_read(read_file_name, read_num=10000, value_file=value_file)
    k = 0
    for line in lines:
        print(line)
        k += 1
        print('has print {} record'.format(k))


if __name__ == "__main__":
    # main_func()
    # go('./order_data.csv', './temp.txt')
    go_continue('./order_data.csv', './temp.txt')
    # gen_order_data()
    pass
