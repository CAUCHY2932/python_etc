# coding=utf8

def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

# 删除一个序列中的空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','bedf','sdf fefw','2345',None,'  '])))