# -*- coding:utf-8 -*-

"""
    2019/4/3 10:27 by young
"""
import sklearn


"""
    特征预处理
        单个特征：归一化，标准化，缺失值
    多个特征
        降维
            pca
"""

# sklearn.feature_extraction.DictVectorizer(sparse=True)

# fit_transform()
from sklearn.feature_extraction.text import CountVectorizer
content = ["life is short,i like python","life is too long,i dislike python"]
vectorizer = CountVectorizer()
print(vectorizer.fit_transform(content).toarray())
