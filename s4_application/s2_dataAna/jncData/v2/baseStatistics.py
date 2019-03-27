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

    def __init__(self, colour):
        self._color = colour

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
