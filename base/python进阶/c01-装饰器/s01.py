# coding:utf-8

__author__ = 'young'

import functools


def log(func):
    def wrapper(*args, **kwargs):
        # 这里可以添加想要增加功能的代码段
        print('my name is %s' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('这是装饰函数')

now()
print(now.__name__)

# 如果不做特殊处理，可以看到名字已经发生改变，通过内置段functools可以处理
