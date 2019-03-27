# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 12:07 
"""

__author__ = 'young'

# 引用函数


def t1():
    print('---in test func---')


t1()
ret = t1

print(id(ret))
print(id(t1))

ret()


