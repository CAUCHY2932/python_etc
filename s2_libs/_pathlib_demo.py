# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 14:06
也可以使用os.walk或是os.listdir, os.path.xxx
"""
from pathlib import Path
import shutil


def copy_file_from_to(from_path, to_path):
    shutil.copy(from_path, to_path)


def out_put_files(filename):
    """打印指定目录下的所有文件
    :param filename:
    :return:
    """
    for i in Path(filename).rglob('*'):
        print(i)


def out_put_files_of_t(filename, t):
    """打印指定目录下的所有符合正则规则的文件
    :param filename:
    :param t: type，文件类型
    :return:
    """
    for i in Path(filename).rglob('*.%s' % t):
        print(i)


def list_subdir(filename):
    """列举子文件夹
    :param filename:
    :return:
    """
    return [x for x in Path(filename).iterdir() if x.is_dir()]


def is_dir_of_file(filename):
    return Path(filename).is_dir()


def is_exits_of_file(filename):
    return Path(filename).exists()


if __name__ == '__main__':
    # out_put_files('/Users/young/codes')
    # out_put_files_of_t('/Users/young/codes', 'py')
    l_file = list_subdir('/Users/young/codes')
    for i in l_file:
        print(i)
    pass
