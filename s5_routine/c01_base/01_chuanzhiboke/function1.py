# -*- coding:utf-8 -*-


a_int = 90


def self_add(val):
    val += val


self_add(a_int)
print(a_int)

a_list = [1, 2]


def self_append(lst):
    lst += lst


self_append(a_list)
print(a_list)
