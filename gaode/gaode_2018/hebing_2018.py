# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/24 10:36
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import os
import pandas as pd


path = './datasets/hebing'
file_name = './union.csv'

# # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
# try:
#     for i in range(1, len(file_list)):
#         path = Path + file_list[i]
#         print(path, '    path is ok')
#         df = pd.read_csv(path)
#         df.to_csv(SaveFile_Path + SaveFile_Name, encoding="utf_8", index=False, header=False, mode='a+')
#
# # 异常处理
# except OverflowError:
#     print('wrong', path)
# if not os.path.exists(path):
#     os.mkdir(path)


for item in os.listdir(path):
    df = pd.read_csv(os.path.join(path, item))
    df.to_csv(file_name, encoding='utf_8', index=False, header=False, mode='a+')
    print('{} have been processed'.format(item))

