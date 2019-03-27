# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 11:59 
"""

__author__ = 'young'

from collections import Iterable, Iterator

print(isinstance([], Iterable))

# list 虽然可迭代，但不是迭代器

# 使用iter()函数可以将其变成迭代器
b = isinstance([], Iterator)
a = isinstance(iter([]), Iterator)
print(a)
print(b)
"""

    凡是可作用于 for 循环的对象都是 Iterable 类型；
    凡是可作用于 next() 函数的对象都是 Iterator 类型
    集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。

"""

