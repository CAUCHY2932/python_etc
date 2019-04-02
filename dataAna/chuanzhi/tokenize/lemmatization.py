# -*- coding:utf-8 -*-

"""
    2019/4/2 15:58 by young
"""
# 词形归并
from nltk.stem import WordNetLemmatizer


wordnet_lematizer = WordNetLemmatizer()
print(wordnet_lematizer.lemmatize('cats'))
print(wordnet_lematizer.lemmatize('boxes'))
print(wordnet_lematizer.lemmatize('are'))
print(wordnet_lematizer.lemmatize('went'))
print(wordnet_lematizer.lemmatize('go'))

print('-'*20)

# 指明词性可以更准确地进行lemma
print(wordnet_lematizer.lemmatize('are', pos='v'))
print(wordnet_lematizer.lemmatize('went', pos='v'))
