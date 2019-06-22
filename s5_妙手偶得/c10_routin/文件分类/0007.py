# coding:utf-8
# 移除某个文件夹内文件名在文本文件中的文件

import os
file_path=''
load_text_path=''
lst_file=os.listdir(file_path)
lst_file_strip=[x.strip() for x in lst_file]
# lst_null=[]
# for item in file_path:
#     item=item.strip()
#     lst_null.append(item)

with open(load_text_path,'r') as f:
    file_load=f.readlines()
file_strip=[x.strip() for x in file_load]
for item_1 in file_strip:
    for item_2 in lst_file_strip:

        if item_==item2:
            print(item_1)
