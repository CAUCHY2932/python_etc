
# 装饰器和闭包

def deco(func):
    def wrapp():
        print('开始装饰')
        func()
        print("装饰结束")
    return wrapp


@deco
def func():
    print('函数主体')
    # return None

func()