# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/28 11:16
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import numpy as np


# # print(np.random.uniform(2500, 25000))
# # 生成特定区间的标准正态分布
# for item in range(1000):
#     print(np.random.uniform(2500, 25000))
#
#
# print('-'*100)
#
#
# # 生成特定区间的随机整数
# for item in range(1000):
#     print(np.random.randint(10, 100))


# 生成特定区间的正态分布
mu, sigma, sample_no = 0, 0.1, 1000
np.random.seed(0)
# for item in range(1000):
#     print(np.random.normal(mu, sigma, 1000))
print(np.random.normal(mu, sigma, sample_no))
