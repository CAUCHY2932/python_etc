# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/28 11:14
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import matplotlib.pyplot as plt
import numpy as np


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


def gen_interval():
    lst = [np.random.randint(10, 1000) for _ in range(1000)]
    print(lst)


def gen_normal():
    pass


if __name__ == '__main__':
    gen_interval()
