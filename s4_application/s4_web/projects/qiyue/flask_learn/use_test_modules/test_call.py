# -*- coding:utf-8 -*-

"""
    2019/4/16 10:05 by young
"""


class ProxyTestModule(object):
    """测试werkzeng的代理"""
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


p = ProxyTestModule()
user = p('user')
