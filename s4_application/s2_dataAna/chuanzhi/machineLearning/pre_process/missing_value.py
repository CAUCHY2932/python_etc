# -*- coding:utf-8 -*-

"""
    2019/4/3 11:39 by young
"""
from sklearn.preprocessing import Imputer
import sklearn
import numpy as np
from sklearn import impute
from sklearn.decomposition import PCA


imp = Imputer(missing_values='NaN',
              strategy='mean',
              verbose=0)

imp.fit([[1, 2],
         [np.nan, 3],
         [7, 6]])
X = [[np.nan, 2],
     [6, np.nan],
     [7, 6]]
print(imp.transform(X))
