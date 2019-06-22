# coding:utf-8


class DemoException(Exception):
    """
    异常类测试
    """
    def __init__(self, name, msg='自定义异常'):
        self.name = name
        self.msg = msg

try:
    raise DemoException("脚本错误")

except DemoException as e:
    print('{}异常的报警是{}'.format(e.name, e.msg))
    

    