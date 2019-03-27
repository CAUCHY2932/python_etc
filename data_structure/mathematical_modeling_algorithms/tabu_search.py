# 禁忌搜索算法

import random
# 初始化禁忌表为空
def v(func):
    """
        parameters func
        :return func.value
    """
    return func.value

class V:
    def __init__(self, function):
        self.function = None
        self.value = 0
        # return self.value

    # def func(self):

    #     return self.value
    # pass
# func1='nihao'
# a = V(func1)
# a.value=9
# print(a.value)
class H:
    def __init__(self):
        self.set = {}

class S:
    def __init__(self):
        pass

class C:
    def __init__(self):
        pass

class L:
    def __init__(self, i, m):
        self.i = i
        self.m = m
        self._tabu_value = 0

    @property
    def value(self):
        return self._tabu_value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('error')
        self._tabu_value = val


    # def map(self):
    #     return self.tabu_value


    pass
l=L(9,5)
# print(L(9,4).value)
l.value=90
print(l.value)



# H = set()
# E = 100
# e = random.randint(1, E)
# k = (e-1)/(E-1)
# V().value=0



