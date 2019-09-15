# coding:utf-8
import contextlib


class MyResource:
    """
    测试上下文管理器
    """

    def __enter__(self):
        """这里必须返回对象本身"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def print_str(self):
        print('helloworld!')


def run_cls():
    with MyResource() as mr:
        mr.print_str()


class MyResource2(object):
    """测试上下文管理器2"""
    def __init__(self, name=None):
        if name:
           self.name = 'mr2'
        else:
            self.name = name
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @contextlib.contextmanager
    def print_str2(self):
        print('start')
        yield self
        print('end')

    def process(self):
        print(self)


def run_cls3():
    with MyResource2(name='zhangsan').print_str2() as mrp2:
        mrp2.process()


@contextlib.contextmanager
def con():
    print('start')
    yield
    print('end')


def run_1():
    with con() as c:
        print('process')


if __name__ == '__main__':
    # run_1()
    run_cls3()
    pass
