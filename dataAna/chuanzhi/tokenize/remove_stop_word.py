# -*- coding:utf-8 -*-

"""
    2019/4/2 16:11 by young
"""


from nltk.corpus import stopwords
from nltk import word_tokenize

words_origin = 'python is a widely used programming language.'
words = word_tokenize(words_origin)
filtered_words = [word for word in words if word not in stopwords.words('english')]

print('原始词:', words)

print('去除停用词后:', filtered_words)

