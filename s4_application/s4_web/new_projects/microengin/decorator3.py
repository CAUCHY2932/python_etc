# coding:utf-8


"""
装饰器设计实验
"""
def bar(foo):
    def wrapper(a):
        print('尝试一些新的东西')
        return foo(a)
    return wrapper

@bar
def printB(a):
    print('这是变量{}'.format(a))

printB('nihao')