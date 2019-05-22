# -*- coding:utf-8 -*-

"""
    2019/4/3 14:36 by young
"""
from recsys import prediction_algorithms


import os, sys


class RecommendSystem(object):
    """

    """
    def __init__(self, filename, sep, **format):
        self.filename = filename
        self.sep = sep
        self.format = format

        # 训练参数
        self.k = 100
        self.min_values = 10
        self.post_normalize = True

        self.svd = prediction_algorithms.SVD()

        # 判断是否加载
        self.is_load = False

        # 添加数据处理

import recsys
print(recsys.version)
