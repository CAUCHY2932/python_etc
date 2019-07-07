# coding:utf-8
"""
测试一些问题
"""

class NewList(list):
    """
    运算符重载
    """
    def __add__(self, other):
        result = []
        for i in range(len(self)):
            try:
                result.append(self[i] + other[i])
            except Exception as e:
                result.append(self[i])
        return result


ls = NewList([1, 2, 3, 4, 5])
lt = NewList([2, 3, 4, 5, 6, 7, 8, 9])
print(ls + lt)              