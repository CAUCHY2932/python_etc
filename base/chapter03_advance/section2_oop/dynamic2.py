# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 20:37 
"""
import types

__author__ = 'young'


# class Person(object):
class Person:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print('eat food')


def run(self, speed):
    print('%s在移动，速度是%d km/h'%(self.name, speed))


P = Person('老王', 24)

P.eat()

P.run = types.MethodType(run, P)
P.run(190)



