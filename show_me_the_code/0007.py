# -*- coding:utf-8 -*-

"""
    2019/4/4 16:20 by young
"""
"""
有个目录，里面是你自己写过的程序，
统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来
"""

"""
思路
每一个换行符，就会多一行
"""


def count_lines(file_name):
    """
    注意，参数名不要有大写
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        fl = f.readlines()
    return len(fl)
