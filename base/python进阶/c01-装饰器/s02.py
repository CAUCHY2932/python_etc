# coding:utf-8

__author__ = 'young'

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 这里可以添加想要增加功能的代码段
        print('my name is %s' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('这是装饰函数')

print(now.__name__)
