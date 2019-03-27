# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 22:15 
"""

__author__ = 'young'


for column in range(1,10):
    for row in range(1,column+1):
        print('{}x{}={}'.format(column, row, column*row), end='\t')
    print()




