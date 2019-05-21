# -*- coding:utf-8 -*-

"""
    2019/4/16 9:26 by young
"""


storage = {}
print('initial dict is {}'.format(storage))

storage['ident'] = {}
print('after add ident dict is {}'.format(storage))

storage['ident']['name'] = 'value'
print('after add ident and name dict is {}'.format(storage))

del storage['ident']['name']

print('after del ident\'s name dict is {}'.format(storage))
# del dict_demo[key] # 是删除某个键值对
