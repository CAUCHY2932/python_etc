# coding:utf-8


class MyResource:
    """
    测试上下文管理器
    """

    def __enter__(self):
        """这里必须返回对象本身"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def printStr(self):
        print('helloworld!')


with MyResource() as mr:
    mr.printStr()
