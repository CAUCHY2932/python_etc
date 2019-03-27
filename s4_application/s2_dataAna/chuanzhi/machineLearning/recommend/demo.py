# -*- coding:utf-8 -*-

"""
    2019/4/3 14:24 by young
"""
import math


# 评分函数
def RMSE(records):
    return math.sqrt(sum([
        (rui - pui) for u, i, rui, pui in records
    ]))

def MAE(records):
    return sum([
        abs(rui - pui) for u, i, rui, pui in records
    ])/float(len(records))


# TopN推荐
def precisionRecall(test, N):
    hit = 0
    n_recall = 0
    n_precision = 0
    for user, items in test.items():
        rank = Recommend(user, N)
        hit += len(rank & items)
        n_recall += len(items)
        n_precision += N
    return [
        hit / (1.0 * n_recall),
        hit / (1.0 * n_precision),
    ]

