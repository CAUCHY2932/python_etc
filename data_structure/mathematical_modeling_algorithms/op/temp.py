# -*- coding=utf-8 -*-
"""
    2019/3/11 20:30
    author:young
"""
import os


with open('file.csv', 'a') as temp_file:
    for item in os.listdir():
        with open(item, 'r') as f:
            for i in f.readlines():
                temp_file.write(i)



