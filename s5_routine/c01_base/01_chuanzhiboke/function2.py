# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 19:53 
"""

__author__ = 'young'

# += 不会创建新对象，+会创建新对象
# 如果不是作为函数，都不会出现这种情况，函数都是引用，另外就是+=不创建新对象，对引用的可变类型进行了改变

def self_add(val):
    val += val


def self_add2(val):
    val = val+val


print('-'*10)
a_int = 100
print('add1自增前值是:{}'.format(a_int))
self_add(a_int)
print('add1自增后值是:{}'.format(a_int))
print('-'*10)

print('-'*10)
a_lst = [1, 2]
print('add1自增前值是:{}'.format(a_lst))
self_add(a_lst)
print('add1自增后值是:{}'.format(a_lst))
print('-'*10)

print('-'*10)
a_int = 100
print('add2自增前值是:{}'.format(a_int))
self_add2(a_int)
print('add2自增后值是:{}'.format(a_int))
print('-'*10)

print('-'*10)
a_lst = [1, 2]
print('add2自增前值是:{}'.format(a_lst))
self_add2(a_lst)
print('add2自增后值是:{}'.format(a_lst))
print('-'*10)
