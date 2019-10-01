# -*- coding:utf-8 -*-

"""
    2019/4/2 15:46 by young
"""


import nltk
from nltk.corpus import brown

print(brown.categories())

print('共有{}个句子'.format(len(brown.sents())))
print('共有{}个单词'.format(len(brown.words())))
