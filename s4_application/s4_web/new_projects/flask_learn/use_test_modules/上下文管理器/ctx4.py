# -*-encoding:utf-8 -*-
"""
    2019/4/20 1:13
    create by young
"""
from contextlib import contextmanager

"""
我们有时候只是想在执行一段程序前后各执行一段代码，
contextmanager
如果我们想要使用的类不是一个上下文管理器，而且是已经开发好的一个类，直接对源码进行更改是非常不合适的
这时候就可以使用contextmanager包装成一个上下文管理器

class MyResource(object):
    def __init__(self, name):
        self.name = name
        pass

    def query(self):
        print('query {} data'.format(self.name))


@contextmanager
def mask(name):
    print('before code execute we can do ...')
    yield MyResource(name=name)
    print('after code execute we can do ...')



with mask('nihao') as mr:
    mr.query()
"""


@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》')


with book_mark():
    print('且将生活一饮而尽', end='')
