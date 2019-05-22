# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 21:34 
"""

__author__ = 'young'


g_gen = (x*2 for x in range(5))

print(g_gen)
print(next(g_gen))
print(next(g_gen))
print('-'*10)
for i in g_gen:
    print(i)

# 尾递归

