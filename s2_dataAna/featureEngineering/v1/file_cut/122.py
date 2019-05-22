# -*- coding:utf-8 -*-

"""
    2019/4/12 16:21 by young
"""

import pandas as pd

data = pd.read_csv('UserBehavior.csv',
                   nrows=100000,
                   header=None,
                   )

data.columns=[
       'User_ID',
       'Item_ID',
       'Category_ID',
       'Behavior_type',
       'Timestamp']

# # print(data.head())
print(data.tail())
# print(data.columns)
# print(data)