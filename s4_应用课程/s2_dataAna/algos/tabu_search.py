# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/8 12:00
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
"""
n阶矩阵进行计算
非对称方式

旅行商问题


"""
import numpy as np

vector1 = []
vector2 = []
vector3 = []
vector4 = []

vectors = [vector1,
           vector2,
           vector3,
           vector4]


def tabu(vectors):
    mat = np.array(vectors)

    tabu_list = []
    tabu_item = []

    # vectors[]
