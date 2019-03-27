# -*- coding:utf-8 -*-

"""
    2019/4/3 14:01 by young
"""

from sklearn import datasets


# iris
iris_data = datasets.load_iris()
# print(data.target)
print(iris_data.keys())
# print(data.feature_names)
# print(data.target_names)
# digit
digits_data = datasets.load_digits()
print(digits_data.keys())
print(digits_data.data.shape)
print(type(digits_data.data))
print(digits_data.images)

# boston
boston_data = datasets.load_boston()
# print(boston_data.data)
print('boston\'s feature names are {}'.format('/'.join([
    name for name in boston_data.feature_names
])))

# diabetes
diabetes_data = datasets.load_diabetes()
print(len(diabetes_data.feature_names))


# 生成本地数据
X, y = datasets.samples_generator.make_classification(n_samples=100000,
                                               n_features=20,
                                               n_informative=2,
                                               n_redundant=10,
                                               random_state=42)
print(X, y)
