# coding:utf-8

import pandas as pd 

data = pd.read_excel('./1.xls', nrows=2)
print(data)
data.to_excel('./001.xls')
