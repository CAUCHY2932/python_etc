# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/16 15:10
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import re
# {1, 8}
# pattern = re.compile(r'\d{1,4}')
#
# str_demo = 'sdkfjslj9879lkjg34we'
#
# ret = re.search(pattern, str_demo)
# print(ret)
# 匹配版本号

import re
ver_num = '[1-9]\d{1,3}([.][1-9]\d{1,3}){1,2}'
# 什么时候加r，什么时候不加r
# 尽量不加r


lst_ver_num = ['89.89.05',
               '90.556.67',
               '56.4m.78']

for item in lst_ver_num:
    match = re.search(ver_num, item)
    if match is not None:
        print('have match {}'.format(match.group()))

# re.sub

