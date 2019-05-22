# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 21:26 
"""

__author__ = 'young'


class Person:
    __slots__ = ('name', 'age')

# __slots__ 定义的属性仅对当前实例起作用，对继承对子类不起作用


P = Person()
P.name = 'LaoWang'
P.age = 89

# P.score = 10


class Test(Person):
    pass


t = Test()

t.score = 100
print(t.score)

