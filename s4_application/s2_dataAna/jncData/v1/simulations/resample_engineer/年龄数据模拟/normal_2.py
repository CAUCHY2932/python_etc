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
    np.random.seed(0)
    gen_lst = np.random.normal(mu, sigma, sample_no)

    filtered = [int(x) if 2500 < x < 25000 else 0 for x in gen_lst]
    return filtered


def gen_normal_list_3(mu=5500, sigma=3000, sample_no=100000, filter_range_start=2500, filter_range_end=25000):
    """
    通过预测，sigma为3000时，效果较好
    :param mu: 均值
    :param sigma: 方差
    :param sample_no: 生成的样本数
    :param filter_range_start:过滤左区间
    :param filter_range_end:过滤右区间
    :return: 样本序列
    """
    np.random.seed(0)
    gen_lst = np.random.normal(mu, sigma, sample_no)

    filtered = [int(x) if filter_range_start < x < filter_range_end else 0 for x in gen_lst]
    return filtered


def sample_n_times_2(n=10000000):
    lst = gen_normal_list_2(sample_no=n)
    y = np.array(lst)
    plt.hist(y, normed=1, fc='c')

    plt.show()


if __name__ == '__main__':
    # sample_n_times()
    lst = gen_normal_list_3(mu=32, sigma=10, sample_no=10000, filter_range_start=20, filter_range_end=85)
    print(lst)
