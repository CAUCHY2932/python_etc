# -*- coding:utf-8 -*-

"""
    2019/4/12 13:28 by young
"""


class Reader:
    """
    读取对象
    """
    def __init__(self):
        pass

    def __str__(self):
        return 'read object'

    def read_sql(self):
        pass

    def read_txt(self):
        with open() as f:
            fr = f.read()
        return fr

    def read_csv(self):
        pass

    def read_excel(self):
        pass

    def read_binary_content(self):
        pass

    pass


read = Reader()
print(read)
