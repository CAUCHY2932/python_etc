# -*- coding:utf-8 -*-
"""
create by young on 2019-03-17 15:34 
"""

__author__ = 'young'


class Func:

    def __init__(self):
        pass

    def __str__(self):
        return '这是一个函数方法'

    def __del__(self):
        print('删除了一个对象')


print(Func)

print(Func())
a = Func()
b = Func()

print('正在删除a')
del a

print('正在删除b')
del b
