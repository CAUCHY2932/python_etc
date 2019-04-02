# -*- coding:utf-8 -*-

"""
    2019/4/2 16:03 by young
"""
# 词性标注

# import nltk
from nltk import word_tokenize, pos_tag

words = word_tokenize('python '
                           'is a widely used programming language.')
# 需要下载 averaged_perceptron_tagger
print(pos_tag(words))
