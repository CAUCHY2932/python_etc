# -*- coding:utf-8 -*-

"""
    2019/4/22 11:02 by young
"""


def read_line_record(file_name, line_num):
    k = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while k < line_num and line:
            yield line
            k += 1
            line = f.readline()


records_less = read_line_record('./test.txt', 2)
records_fit = read_line_record('./test.txt', 6)
records_more = read_line_record('./test.txt', 100)


def print_record(records):
    k = 1
    for item in records:
        print('the {0:0>12}th record is {1}'.format(k, item))
        k += 1


if __name__ == "__main__":
    print_record(records_less)
    print('-'*20)
    print_record(records_fit)
    print('-'*20)
    print_record(records_more)
