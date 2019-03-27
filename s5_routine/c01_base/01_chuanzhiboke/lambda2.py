# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 20:53 
"""

__author__ = 'young'


def func(a, b, opt):

    return opt(a, b)


print(func(3, 5, lambda x, y: x+y))


