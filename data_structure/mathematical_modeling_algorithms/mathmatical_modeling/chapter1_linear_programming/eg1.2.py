# -*- coding=utf-8 -*-
"""
    2019/3/13 10:17
    author:young
"""

from scipy import optimize as op
import numpy as np

c = np.array([2, 3, -5])
A_ub = np.array([[-2, 5, -1], [1, 3, 1]])
b_ub = np.array([-10, 12])
A_eq = np.array([[1, 1, 1]])
b_eq = np.array([7])

x1 = (0, 7)
x2 = (0, 7)
x3 = (0, 7)

res = op.linprog(-c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(x1, x2, x3))

print(res)

"""
重点关注的就是第一行和最后一行了，第一行是整个结果，
最后一行是每个x的结果。为什么第一行是负的呢？原来这个函数其实是求最小值的，那么求最大值，怎么办呢？
很简单，仔细观察的人应该发现，之前的函数里面，我写的是-c，而不是c。那么这个函数的出来的结果其实就是-c的最小值，
但很明显这恰恰是c最大值的相反数。那么答案就是14.57了，以上。 

"""
