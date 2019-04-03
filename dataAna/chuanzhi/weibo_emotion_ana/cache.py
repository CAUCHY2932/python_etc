# -*- coding:utf-8 -*-

"""
    2019/4/3 10:12 by young
"""


import json
# load 是从文件中载入字节流转换成Python对象，loads是从字符串载入并转换为Python对象
with open('./chinese_stopwords.json', 'r', encoding='utf-8') as json_file_str:
    str_demo = json.load(json_file_str)
print(type(str_demo))
print(str_demo)



with open('./chinese_stopwords.json', 'r', encoding='utf-8') as json_file_str:
    str_demo = json.loads(json_file_str.read())
print(type(str_demo))
print(str_demo)
print(len(str_demo))
