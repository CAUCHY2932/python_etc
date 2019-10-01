# -*-encoding:utf-8 -*-
"""
    2019/4/20 1:03
    create by young
"""
from contextlib import contextmanager


class MyResource(object):
    # def __enter__(self):
    #     pass
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     pass

    def query(self):
        print('query data')


@contextmanager
def make_my_resource():
    print('connect to resource')
    yield MyResource() # 这里不要用return ，要用yield
    print('close resource connection')


with make_my_resource() as r:
    r.query()
