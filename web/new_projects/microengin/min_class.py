# coding:utf-8


class EmptyClass:
    pass

a = EmptyClass()
a.name = "老李"
a.age = 50
a.family = ['儿子','女儿','小李','耳力']
print(a.family)
print(a.__dict__)
print(__name__)