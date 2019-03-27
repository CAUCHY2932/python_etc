# -*- coding=utf-8 -*-
"""
    2019/3/13 11:22
    author:young
"""

import numpy as np
from scipy import optimize as op

f = np.array([2, 3, 1])

a = np.array([[-1, -4, -2], [-3, -2, 0]])
b = np.array([-8, -6])
# A_eq = np.array([0, 0, 0])
# b_eq = np.array([0])
x1 = (0, None)
x2 = (0, None)
x3 = (0, None)

res = op.linprog(c=f, A_ub=a, b_ub=b, bounds=[x1, x2, x3])
print(res)
