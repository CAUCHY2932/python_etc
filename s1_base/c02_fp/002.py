# coding=utf8

import functools

# a=int('20', base=8)
# print(a)

def int2(x,base=2):
    return int(x,base)

print(int2('10001010'))




# 偏函数

int8=functools.partial(int,base=8)

transferTo8=int8('132421432')
print(transferTo8)