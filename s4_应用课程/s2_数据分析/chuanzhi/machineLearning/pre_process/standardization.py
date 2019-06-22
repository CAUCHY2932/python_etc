# -*- coding:utf-8 -*-

"""
    2019/4/3 11:32 by young
"""
# 使得处理过的数据均值为0， 标准差为1

import numpy as np
from sklearn.preprocessing import StandardScaler


X_train = np.array(
    [[1., -1., 2.],
     [2., 0., 0.],
     [0., 1., -1.]])
std = StandardScaler()
X_train_std = std.fit_transform(X_train)
print(X_train_std)
