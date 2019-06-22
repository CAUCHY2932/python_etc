# -*- coding:utf-8 -*-

"""
    2019/4/2 17:14 by young
"""
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier


text1 = 'I like the movie so much!'
text2 = 'That is a good movie.'
text3 = 'This is a great one.'
text4 = 'That is a really bad movie.'
text5 = 'This is a terrible movie.'


def proc_text(text):
    """

    预处理文本
    :param text:
    :return:
    """
    # 分词
    raw_words = nltk.word_tokenize(text)
    # 词形归一化
    wordnet_lematizer = WordNetLemmatizer()
    words = [wordnet_lematizer.lemmatize(raw_word) for raw_word in raw_words]

    # 去除停用词
    filtered_words = [word for word in words if word not in stopwords.words()]

    # True 表示在该词在文本中，为了使用nltk中的分类器
    return {word: True for word in filtered_words}

# 构造训练样本
train_data = [
    [proc_text(text1), 1],
    [proc_text(text2), 1],
    [proc_text(text3), 1],
    [proc_text(text4), 0],
    [proc_text(text5), 0],
]

# 训练模型
nb_model = NaiveBayesClassifier.train(train_data)

# 测试模型
text6 = 'That is a bad one.'


# print(nb_model.classify(proc_text(text6)))
text7 = 'we are happy.'
print(nb_model.classify(proc_text(text7)))
