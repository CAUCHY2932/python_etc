# -*- coding:utf-8 -*-

"""
    2019/4/18 10:06 by young
"""


import random as rd
import numpy as np


class Simulator(object):
    """


    """

    def __init__(self):
        pass

    @classmethod
    def rand_chars(cls):
        pass

    @classmethod
    def rand_time(cls):
        pass

    @classmethod
    def rand_name(cls):
        pass

    @classmethod
    def rand_addr(cls):
        pass

    @classmethod
    def rand_num(cls):
        pass

    @staticmethod
    def gen_normal_age_list(mu=5500, sigma=3000, sample_no=100000, filter_range_start=2500, filter_range_end=25000):
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

    @staticmethod
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

    @classmethod
    def get_property_num(cls, n):
        """
        生成指定长度的列表
        :param n:
        :return:
        """
        lst = cls.gen_normal_list_2(sample_no=n)
        times = 0
        while len(lst) < n:
            lst.extend(cls.gen_normal_list_2(sample_no=n))
            times += 1
        return lst, times
