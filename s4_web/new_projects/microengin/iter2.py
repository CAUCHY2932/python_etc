# coding:utf-8


def get_value(max):
    """
    测试生成器
    """
    import random
    ls = list(range(10))
    print(ls, end=',')
    for _ in range(max):
        yield ls[random.randint(0, 9)]

for i in get_value(10):
    print(i)
