# coding:utf-8


class DemoIterator:
    """
    测试迭代器
    """
    def __init__(self, container):
        self.container = container
        self.length = len(self.container)
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.length -= 1
        self.index += 1
        if self.length > 0:
            return self.container[self.index]
        else:
            raise StopIteration

lst = list(range(15))
di = DemoIterator(lst)
for i in di:
    print(i, end=', ')
