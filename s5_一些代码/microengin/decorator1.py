# coding:utf-8


"""
一个函数，更新其功能
要么重新编写函数，补充功能，

不改变函数功能，增补一个装饰器给他
"""
def f1():
    pass

f1 = staticmethod(f1)

@staticmethod
def f2():
    pass
