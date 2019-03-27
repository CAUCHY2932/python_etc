# -*- coding:utf-8 -*-
"""
create by young on 2019-03-15 21:39 
"""

__author__ = 'young'


# 尾递归
# 非波拉契数列
def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        print(b)
        a, b = b, a + b
        n += 1

    return 'done'


print(fib(5))

print('-'*10)


def fib_generator(times):
    n = 0
    a, b = 0, 1
    while  n<times:
        yield b
        a, b = b, a+b
        n +=1

    return 'done'


print(fib_generator(5))
for item in fib_generator(7):
    print(item)


print('-'*10)

g = fib_generator(8)
while True:
    try:
        x = next(g)
        print('value:%d'%x)
    except StopIteration as e:
        print('生成器返回值：%s'%e.value)
        break
