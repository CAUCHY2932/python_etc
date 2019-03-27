# -*- coding=utf-8 -*-
"""
    2019/3/13 9:04
    author:young
"""

"""
    禁忌搜索，现代启发算法
    
    
    禁忌表
    禁忌长度
    候选解
    特赦准则
    终止准则
    邻域
    禁忌对象
"""


class H:

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


