# coding:utf-8


"""
装饰器设计实例
"""

def bar(foo):
    def wrapper(a):
        print("{:*^20}".format('BEGIN'))
        foo(a)
        print("{:*^20}".format('END'))
    return wrapper


@bar
def printA(a):
    print('这是变量{}'.format(a))

printA('python')