# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/30 11:45
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import numpy as np
from scipy import stats


class BaseStatistics(object):
    """
    基本统计函数，使用numpy和scipy两个库进行高级封装
    包含：
    ----
    mean:
    平均值
    ----
    median:
    中位数
    ----
    mode_num:
    众数
    ---

    """

    @staticmethod
    def mean(input_list):
        ret = np.mean(input_list)
        return ret

    @staticmethod
    def median(input_list):
        ret = np.median(input_list)
        return ret

    @staticmethod
    def mode_num(input_list):
        ret = stats.mode(input_list)[0][0]
        return ret
