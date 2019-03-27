# coding=utf8
from functools import reduce
def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6])
print(r)

for item in r:
    print(item)


def add(x,y):
    return x+y


retVal=reduce(add,[1,2,3,4,5])
print(retVal)
print(sum([1,2,3,4,5]))