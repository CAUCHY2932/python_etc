# coding=utf8

# 构造一个从3开始的奇数序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield

# lst_odd=(x for i in )

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it= _odd_iter()
    while True:
        n=next(it)
        yield n
        it = filter(_not_divisible(n), it)
# 打印1000以内的素数

for n in primes():
    if n<1000:
        print(n)
    else:
        break