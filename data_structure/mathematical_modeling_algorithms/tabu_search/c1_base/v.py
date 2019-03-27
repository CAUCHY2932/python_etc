# -*- coding=utf-8 -*-
"""
    2019/3/13 9:18
    author:young
"""


class V:

    def __init__(self, i=0, m=0):
        self.i = i
        self.m = m
        self.val = 0

    @property
    def value(self):
        return self.val

    @value.setter
    def value(self, v):
        if not isinstance(v, int):
            raise ValueError('error!')
        self.val = v
