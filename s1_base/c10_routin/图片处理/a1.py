import os
import pandas as pd

pdGet = pd.read_excel('./handled.xlsx')

# 处理单个sheet表
# data = pd.read_excel('for_python.xlsx','Sheet2')

# print(pdGet)
print(type(pdGet))

# pdHandle=pd.DataFrame(pdGet)
# print(pdHandle)

# print(pdHandle.head())