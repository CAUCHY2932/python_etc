# -*- coding:utf-8 -*-

"""
    2019/4/2 16:17 by young
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# 原始文本
raw_text = 'Life is like a box of chocolates, You never know what you \'re gonna get.'
# 分词
raw_words = nltk.word_tokenize(raw_text)
# 词形归一化
wordnet_lematizer = WordNetLemmatizer()
words = [wordnet_lematizer.lemmatize(raw_word) for raw_word in raw_words]
# 去除停用词
filtered_words = [word for word in words if word not in stopwords.words('english')]


print('原始文本:', raw_text)
print('预处理结果:', filtered_words)
