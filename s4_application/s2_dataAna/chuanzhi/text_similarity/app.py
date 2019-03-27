# -*- coding:utf-8 -*-

"""
    2019/4/2 17:25 by young
"""

import nltk
from nltk import FreqDist



text1 = 'I like the movie so much '
text2 = 'That is a good movie '
text3 = 'This is a great one '
text4 = 'That is a really bad movie '
text5 = 'This is a terrible movie'

text = ''.join([
    text1,
    text2,
    text3,
    text4,
    text5,
])
words = nltk.word_tokenize(text)
freq_dist = FreqDist(words)
# print(freq_dist)
print(freq_dist['is'])

# 取出常用的n=5个单词
n = 5
most_common_words = freq_dist.most_common(n)
print(most_common_words)

def lookup_pos(most_common_words):
    """
    查找常用单词的位置
    :param most_common_words:
    :return:
    """
    result = {}
    pos = 0
    for word in most_common_words:
        result[word[0]] = pos
        pos += 1

        return result

# 记录位置
std_pos_dict = lookup_pos(most_common_words)
print(std_pos_dict)

# 新文本
new_text = 'That one is a good movie. This is so good!'
# 初始化向量
freq_vec = [0] * n
# 分词
new_words = nltk.word_tokenize(new_text)

# 在常用单词列表上计算词频
for new_word in new_words:
    if new_word in list(std_pos_dict.keys()):
        freq_vec[std_pos_dict[new_word]] += 1

print(freq_vec)
