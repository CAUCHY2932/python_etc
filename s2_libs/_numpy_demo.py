# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/15 15:23
"""
import numpy as np


# 生成任意随机数据
def gen_random_data(row, column):
    data = np.random.randn(row, column)
    print(data)


if __name__ == "__main__":
    gen_random_data(4, 6)
