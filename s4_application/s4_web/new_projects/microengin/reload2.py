# coding:utf-8

from functools import reduce
class Judge(list):
    """
    用来测试重载比较方法
    这里为什么不把他放到初始化里，而是直接放到类的继承中呢
    """

    def __lt__(self, other):
        """
        以各元素算术和比较依据
        
        """
        s, t = 0, 0
        for c in self:
            s += c
        for c in other:
            t += c
        return True if s < t else False


class Judge2:
    """
    测试如果在init语句中使用这种方法会出现哪些问题

    """
    def __init__(self, list):
        self.list = list

    def __lt__(self, other):
        # s, t = 0, 0
        # a = reduce(sum, self.list)
        # b = reduce(sum, other)
        
        return True if sum(self.list) < sum(other) else False

        

# ls = Judge([6, 7, 8, 9, 80])
# lt = Judge([6, 7, 3, 8, 9])
ls2 = Judge2([6, 7, 8, 9, 80])
lt2 = Judge2([6, 7, 3, 8, 9])

print(ls2<lt2)


