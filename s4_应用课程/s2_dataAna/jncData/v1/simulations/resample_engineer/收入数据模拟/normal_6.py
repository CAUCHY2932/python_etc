# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/28 11:42
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import numpy as np
import matplotlib.pyplot as plt


def gen_normal_list(mu=5500, sigma=3000, sample_no=100000):
    """
    通过预测，sigma为3000时，效果较好
    :param mu: 均值
    :param sigma: 方差
    :param sample_no: 生成的样本数
    :return: 样本序列
    """
    np.random.seed(0)
    gen_lst = np.random.normal(mu, sigma, sample_no)

    filtered = filter(lambda x: 2500 < x < 25000, gen_lst)
    return [int(i) for i in filtered]


def sample_n_times(n=10000000):
    lst = gen_normal_list(sample_no=n)
    # y = np.reshape(lst, n)
    y = np.array(lst)
    plt.hist(y, normed=1, fc='c')

    plt.show()


def gen_normal_list_2(mu=5500, sigma=3000, sample_no=100000):
    """
    通过预测，sigma为3000时，效果较好
    :param mu: 均值
    :param sigma: 方差
    :param sample_no: 生成的样本数
    :return: 样本序列
    """
    rnd = np.random.randint(0, 1)
    np.random.seed(rnd)
    gen_lst = np.random.normal(mu, sigma, sample_no)

    # filtered = [int(x) if 2500 < x < 25000 else 0 for x in gen_lst]
    object_user_list = filter(lambda x: 8000 < x < 15000, gen_lst)
    return [int(item) for item in object_user_list]


def sample_n_times_2(n=10000000):
    lst = gen_normal_list_2(sample_no=n)
    y = np.array(lst)
    plt.hist(y, normed=1, fc='c')

    plt.show()


def get_property_num(n):
    """
    生成指定长度的列表
    :param n:
    :return:
    """
    lst = gen_normal_list_2(sample_no=n)
    times = 0
    while len(lst) < n:
        lst.extend(gen_normal_list_2(sample_no=n))
        times += 1
    return lst, times


if __name__ == '__main__':
    # sample_n_times()
    lst, times = get_property_num(10000)
    print(times)
    print(len(lst))
