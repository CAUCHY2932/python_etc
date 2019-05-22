# -*- coding:utf-8 -*-

"""
    2019/4/18 9:23 by young
"""


import pandas as pd


class JncReader(object):
    """
    TODO
    ---
    继承pandas类的相关功能，并重写部分功能
    限制其属性(failure)
    ---
    常规方法
    自己进行方法重写

    """

    def __init__(self):
        pass

    @classmethod
    def read_csv(cls,
                 file_name,
                 encoding='utf-8'):

        with open(file_name, 'r', encoding=encoding) as f:
            return f.read()

    @classmethod
    def read_excel(cls,
                   file_name):

        return pd.read_excel(file_name)

    @classmethod
    def read_txt(cls,
                 file_name):

        with open(file_name, 'r') as f:
            return f.read()

    @classmethod
    def read_binary(cls,
                    file_name):

        with open(file_name, 'rb') as f:
            return f.read()
