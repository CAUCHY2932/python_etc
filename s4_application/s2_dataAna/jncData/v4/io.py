# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/30 12:01
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
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


class JncWriter(object):
    """
    继承pandas类的方法和属性
    实现写操作
    """
    def __init__(self):
        pass

    @classmethod
    def to_csv(cls,
               file_name,
               content,
               encoding='utf-8'):

        with open(file_name, 'w', encoding=encoding) as f:
            f.write(content)

    @classmethod
    def to_sql(cls):
        pass

    @classmethod
    def to_txt(cls,
               file_name,
               content,
               encoding='utf-8'):

        with open(file_name, 'w', encoding=encoding) as f:
            f.write(content)

    @classmethod
    def to_binary(cls,
                  file_name,
                  content,
                  encoding='utf-8'):

        with open(file_name, 'w', encoding=encoding) as f:
            f.write(content)

    @classmethod
    def to_excel(cls,
                 file_name):

        pd.ExcelWriter(file_name)
