# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 15:48
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from collections import namedtuple

WI = namedtuple('WorkInfo', ['工作内容',
                             '单次工作时长',
                             '频次'])

july = WI(['爬虫', '数据分析'], 8, 15)

print(july)
