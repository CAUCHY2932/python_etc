# 基类中的__init__方法
class Rectangle:
    def area(self):
        # return self.length * self.width
    
"""
    虽然这种延迟赋值的实现方式在python中是合法的，但是却给调用者带来了潜在的困惑，因为要尽量避免这种用法
    延迟初始化属性的设计在某种情形下可能会有用，可是这样也可能会导致非常糟糕的设计。


"""
class Card:
    pass


class NumberCard(Card):
    pass


