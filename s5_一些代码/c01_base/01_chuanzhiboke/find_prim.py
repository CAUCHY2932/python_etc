# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 22:52 
"""

__author__ = 'young'


def find_prim_num(start, end):
    """
    :parameter start
    :parameter end
    :return: list
    """
    lst = []
    if end <= start:
        return []
    if start < 2:
        start = 2
    for item in range(2, end + 1):
        for i in range(2, item + 1):
            if item % i == 0:
                break
        if i == item:
            lst.append(i)
    return lst


lst_demo = find_prim_num(2, 200)
print(lst_demo)

lst_demo2= find_prim_num(-3,190)
print(lst_demo2)

lst_demo3= find_prim_num(90, 23)
print(lst_demo3)