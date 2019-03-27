# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 12:10 
"""

__author__ = 'young'


def t(number):

    def t_in(number_in):
        print('in test_in 函数， number_in is %d' % number_in)
        return number+number_in
    return t_in


ret = t(20)
print(ret)
print(ret(4))


