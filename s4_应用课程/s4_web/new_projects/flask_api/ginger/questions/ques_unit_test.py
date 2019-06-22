# -*-encoding:utf-8 -*-
"""
    2019/4/20 6:59
    create by young
"""


"""
如果每次进行测试后续步骤，需要重复前面的内容
可以通过单元测试的内容进行有效的测试
"""

import unittest


class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    pass

