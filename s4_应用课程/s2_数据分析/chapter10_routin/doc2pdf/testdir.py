# -*- coding:utf-8 -*-
"""
    create by young on 2018/12/26 15:35
"""

__author__ = 'young'

import os

# print(os.listdir('c:/'))
# print(type(os.listdir('c:/')))
#
# print(os.walk('c:/'))
#
# print(type(os.walk("c:/")))
path=r"C:\Users\29320\Downloads\Clove318r"
# for item in os.walk(path):
    # print(item)

    # os.walk()



print(list(os.walk(path)))