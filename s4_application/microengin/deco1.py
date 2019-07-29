# coding:utf-8


class DemoClass:
    """
    测试属性约束
    """
    def __init__(self, name):
        self.name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            value = 30
        self._age = value

dc1 = DemoClass("老李")
dc1.age = -100
print(dc1.age)
