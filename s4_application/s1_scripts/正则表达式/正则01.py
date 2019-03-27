# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/5 11:22
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import re


with open('./html-01.html', mode='r') as fr:
    txt_content = fr.read()

# print(txt_content)


result = re.search(r'<script class="J_auto-load"(.*?)/script>', txt_content, re.S)
print(result.group())

lst_of_result = re.findall(r'<a.*?/a>', result.group(), re.S)

# print(lst_of_result)

for item in lst_of_result:
    print(item)
