# -*- coding:utf-8 -*-

"""
    2019/4/22 15:39 by young
"""


def read_some():
    with open('./test_read.txt', 'r')as f:
        content = f.read(3) # 读取一部分内容
        # 在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取
        print('file pointer position is {}'.format(f.tell()))
        return content


"""
seek() 方法用于移动文件读取指针到指定位置。
seek(offset, whence)有2个参数：
offset:偏移量，whence:方向。
whence：是可选参数，默认值为 0。
给offset参数一个定义，表示要从哪个位置开始偏移；
0代表从文件开头开始算起，
1代表从当前位置开始算起，
2代表从文件末尾算起。
二进制打开，读
"""


def read_file_from_local(filename):
    fl = open(filename, 'r')
    for item in range(10):
        print('content is "{}"'.format(fl.readline()))
        print('file pointer position is {}\n'.format(fl.tell()))
        print()


read_file_from_local('./test_read.txt')


def go_to_test_file_seek():
    with open('./test_read.txt', 'r') as f:
        f.seek(36)
        print(f.readline())


go_to_test_file_seek()


"""
由此可见，使用file的seek函数，可以有效的进行读写，记录文件上次的读写位置（通过写入文件日志）




"""