# -*- coding:utf-8 -*-

"""
    2019/4/18 9:24 by young
"""


import pandas as pd


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


if __name__ == "__main__":
    """
    进行测试
    """
    jw = JncWriter()
    # pd.read_csv()
    # pd.re
