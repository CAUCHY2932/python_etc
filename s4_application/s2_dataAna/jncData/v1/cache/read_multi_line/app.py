# coding:utf-8

import pandas as pd
from cut_file import split_file


def go():
    """
    进行文件切割
    """

    split_file('common_features_test.csv',
               './features_copy',
               chunk_size=50,
               return_files=20
               )

    # split_file('sample_skeleton_test.csv', 
    #         './skeleton',
    #         chunk_size=500,
    #         return_files=20
    # )


def test_lines(file_name, lines=20):
    """
    读取file_name，并返回lines行的数据
    """
    with open(file_name, 'rb') as f:
        fr = (f.readline() for _ in range(lines))
        fprint = ''.join(fr)
    print(fprint)
    return fprint


def pandas_read(encoding):
    """
    pandas读取数据
    """
    data = pd.read_csv('common_features_test.csv',
                       nrows=3,
                       header=None,
                       encoding=encoding)
    print(data)


def read_bin(file_name, chunk=2018):
    with open(file_name, 'rb') as fb:
        f = fb.read(chunk)
    print(f.decode('ascii'))


def print_illegol():
    str_ill = b'\0x02'
    str_ill_2 = b'\0x03'
    print(str_ill.decode('ascii'))
    print(str_ill_2.decode('ascii'))


def read_asc(file_name, lines=100):
    with open(file_name, 'r') as f:
        fr = (f.readline() for _ in range(lines))
        fprint = ''.join(fr)
    print(fprint)

    pass


if __name__ == "__main__":
    go()
    # fprint = test_lines(
    #         'common_features_test.csv',
    #         lines=10,
    # )
    # with open('1.txt', 'w') as f:
    #     f.write(fprint)
    # pandas_read(encoding='utf-8')
    # read_bin('common_features_test.csv')
    # print_illegol()
