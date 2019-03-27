# coding:utf-8


class DemoClass:
    """
    定义名称修饰
    单下划线是约定，可以调用，无特殊功能
    双下划线不是约定，而是功能性的，私有的是无法调用的
    双下划线开头和结尾的属性或是方法无任何特殊功能，名字不被修改
    部分名称是保留属性或保留方法
    """
    def __init__(self, name):
        self.name = name
        self._nick = name + '同志'

    def getNick(self):
        return self._nick

dc1 = DemoClass("老李")
print(dc1.name)
print(dc1._nick)
print(dc1.getNick())