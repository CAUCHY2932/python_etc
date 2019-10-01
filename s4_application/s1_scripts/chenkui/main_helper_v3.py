# coding:utf-8
import pandas as pd
import numpy as np


print("[提示]--请输入要拆分的路径名--\n")
a = input(r'[提示]--如：c:\user\lvyangyang\desktop\拆分物流码模块.xlsx'+'\n').strip()

print('[提示]-正在进行读取...\n')
df = pd.read_excel(a)

print('[提示]-您拆分的表的字段如下:\n')
column_list = [column for column in df]
print(column_list)

print('[处理]-正在进行字段拆分...\n')
df['取件物流码'] = [x.split(',') for x in df['取件物流码']]

print('[处理]-正在进行后处理...\n')
# 转换成列表
py_list = np.array(df).tolist()

# 生成器
new_list = (item[:-1]+[i] for item in py_list for i in item[-1])

# # 列表推导
# new_list = [item[:-1]+[i] for item in py_list for i in item[-1]]

# for item in py_list:
#     for i in item[-1]:
#         new_list.append(item[:-1]+[i])

# print(new_list)
print('[完成]-已经完成处理，结果如下：\n')
print(column_list)
for i in new_list:
    print(i)
