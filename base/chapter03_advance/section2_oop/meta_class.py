# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 19:22 
"""

__author__ = 'young'


class ObjectCreate(object):
    pass


my_object = ObjectCreate()
print(my_object)


def echo(o):
    print(o)


echo(my_object)
print(hasattr(ObjectCreate, 'new_attribute'))
# print(ObjectCreate.new_attribute)


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

Test2 = type('Test2', (), {})
print(Test2)
print(Test2())

MyDogClass = type('MyDog', (), {})
print(MyDogClass)

help(MyDogClass)

age = 35
print(age.__class__)



