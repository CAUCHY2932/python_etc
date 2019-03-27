# -*- coding:utf-8 -*-

"""
    2019/4/4 15:41 by young
"""


lst_demo = list(range(20))

lst_copy = lst_demo

for item in lst_demo:
    if item % 3 == 0:
        lst_copy.remove(item)

print('lst_copy is {}'.format(lst_copy))
print('lst_demo is {}'.format(lst_demo))
"""
result:
lst_copy is [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
lst_demo is [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
说明是引用，会动态改变值

"""

lst_demo2 = list(range(20))

lst_copy2 = lst_demo2.copy()

for item in lst_demo2:
    if item % 3 == 0:
        lst_copy2.remove(item)

print('lst_copy2 is {}'.format(lst_copy2))
print('lst_demo2 is {}'.format(lst_demo2))
