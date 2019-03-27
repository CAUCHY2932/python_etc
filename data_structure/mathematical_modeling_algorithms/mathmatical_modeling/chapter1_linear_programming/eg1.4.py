# -*- coding=utf-8 -*-
"""
    2019/3/13 13:37
    author:young
"""

import numpy as np
from scipy import optimize as op

c_origin = np.array([1, 2, 3, 4])
c = np.hstack((c_origin, c_origin))
b = np.array([-2, -1, -1 / 2])
A = np.array([[1, -1, -1, 1], [1, -1, 1, -3], [1, -1, -2, 3]])
a = np.hstack((A, -A))
u1 = u2 = u3 = u4 = v1 = v2 = v3 = v4 = (0, None)

res = op.linprog(c, A_ub=a, b_ub=b, bounds=(u1, u2, u3, u4, v1, v2, v3, v4))
print(res)

