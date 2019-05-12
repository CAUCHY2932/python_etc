# coding:utf-8

__author__ = 'young'

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 这里可以添加想要增加功能的代码段
            print('my addition string is %s'%text)
            print('my name is %s' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('haha')
def now():
    print('这是装饰函数')

print(now.__name__)
now()
