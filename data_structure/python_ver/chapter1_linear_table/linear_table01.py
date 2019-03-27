# -*- coding:utf-8 -*-
"""
create by young on 2019-03-17 20:48 
"""

__author__ = 'young'


class LinearTable:
    """
    线性表的顺序表示
    """
    def __init__(self, max_size=50, length=0):
        """

        :param max_size: 线性表的最大长度
        :param length: 当前的最大长度
        """
        self.max_size = max_size
        self.data = [0 for _ in range(self.max_size)]
        self.length = length

    def insert(self, i, e):
        """

        :param i:第i个位置
        :param e:插入的元素
        :return: 是否成功插入
        """
        if i < 1 or i > self.length:
            return False
        if self.length > self.max_size:
            return False
        for item in range(self.length, i+1, -1):
            self.data[item] = self.data[item-1]
        self.data[i-1] = e
        self.length += 1
        return True

    def delete(self, i, e):
        """

        :param i:删除第i个位置的元素
        :param e: 删除的元素的值
        :return:
        """
        if i<1 or i > self.length:
            return False
        e = self.data[i-1]
        for item in range(i, self.length):
            self.data[item-1] = self.data[item]
        self.length -= 1
        return e

    def locate_elem(self, e):
        """

        :param e: 需要寻找的元素
        :return: 找到的元素的位置
        """
        for item in range(0, self.length):
            if self.data[item] == e:
                return item+1
        return 0    # 查找失败

    # def


lst = LinearTable(10, 5)
lst.insert(2, 6)
print(lst.length, lst.data, lst.max_size)

a = lst.locate_elem(6)
print(lst.length, lst.data, lst.max_size, a)

lst.delete(2, 6)
print(lst.length, lst.data, lst.max_size)
