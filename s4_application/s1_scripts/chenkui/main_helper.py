# coding:utf-8


import pandas as pd
import numpy as np


df = pd.read_excel('./拆分物流码模板.xlsx')
df['取件物流码'] = [x.split(',') for x in df['取件物流码']]

np_ob = np.array(df)

py_list = np_ob.tolist()

print(type(py_list))

# print('-'*100)
# print(py_list)

new_list = []
for item in py_list:
    for i in item[-1]:
        new_list.append(item[:-1]+[i])

# print(new_list)
for i in new_list:
    print(i)