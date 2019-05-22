# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/28 10:19
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import matplotlib.pyplot as plt
# from matplotlib.pyplot import hist, plot, xlabel, ylabel, show
import numpy as np
# from pylab import *
"""
利用Box-Muller变换生成高斯分布随机数的方法可以总结为以下步骤：
1.生成两个随机数 U1,U2∼U[0,1]U1​,U2​∼U[0,1]
2.令 R=−2ln(u1)−−−−−−−√R=−2ln(u1​)
​, θ=2πU2θ=2πU2​
3.z0=Rcosθ,z1=Rsinθz0​=Rcosθ,z1​=Rsinθ


"""


def sample():
    x = np.random.rand()
    y = np.random.rand()
    r = np.sqrt((-2) * np.log(x))
    theta = 2 * np.pi * y
    z = r * np.cos(theta)
    # or z = r * np.sin(theta)
    return z


def sample_n_times(n=100000):
    lst = [sample() for _ in range(n)]
    y = np.reshape(lst, n)
    plt.hist(y, normed=1, fc='c')

    x = np.arange(-4, 4, 0.1)
    plt.plot(x, 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x ** 2), 'g', lw=6)
    plt.xlabel('x', fontsize=24)
    plt.ylabel('p(x)', fontsize=24)

    plt.show()


sample_n_times()
