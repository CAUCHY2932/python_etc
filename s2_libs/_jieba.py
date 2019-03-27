# -*- coding:utf-8 -*-
import jieba


def all_cut():
    """全模式"""
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式


def precise_cut():
    """精确模式，默认是精确模式"""
    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))


def search_engine():
    """搜索引擎模式"""
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
    print(", ".join(seg_list))
