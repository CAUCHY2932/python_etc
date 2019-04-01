# coding:utf-8
import random

import numpy as np


rand_lst = [random.randint(1, 10) for _ in range(100)]

print(rand_lst)


# product normal distribution

print(np.random.normal(loc=0, scale=100))
normal_lst = [np.random.normal(loc=0.0, scale=20.0) for _ in range(30)]
print(normal_lst)