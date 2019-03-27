# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 20:31 
"""

__author__ = 'young'


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


P = Person('小明', '24')
P.sex = 'male'
print(P.sex)

# P1 = Person('小丽', '25')
# print(P1.sex)

