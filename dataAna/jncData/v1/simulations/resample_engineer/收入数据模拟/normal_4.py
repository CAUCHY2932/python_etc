# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/28 11:42
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import numpy as np


mu, sigma, sample_no = 5500, 3000, 10000
np.random.seed(0)
# for item in range(1000):
#     print(np.random.normal(mu, sigma, 1000))
gen_lst = np.random.normal(mu, sigma, sample_no)


filtered = filter(lambda x: 2500 < x < 25000, gen_lst)
# print(filtered)
# for item in filtered:
#     print(item)
print(list(filtered))
# counter = 1
# while counter <= 1000:
#     print()
