# -*-encoding:utf-8 -*-
"""
    2019/4/20 1:08
    create by young
"""


class MyResource(object):
    # 使用contextmanager并没有简化一些内容
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def query(self):
        print('query data')


with MyResource() as r:
    r.query()
