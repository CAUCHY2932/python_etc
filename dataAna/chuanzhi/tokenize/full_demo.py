# -*- coding:utf-8 -*-

"""
    2019/4/2 16:24 by young
"""

import nltk
from nltk.tokenize import WordPunctTokenizer


sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
paragraph = 'The first time I heard that song was in Hawaii on radio. I was just a kid, and I loved it very much! What a fantastic song!'

# 分词
sentences = sent_tokenizer.tokenize(paragraph)
print(sentences)

sentence = "Are you old enough to remember Michael Jackson attending. the Grammy with Brooke Shields and Webster sat on his lap during the show?"

# 分词
words = WordPunctTokenizer().tokenize(sentence.lower())
print(words)
