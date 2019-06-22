# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:24
    create by young
"""
"""
定义函数的顺序
------------------------
def func_print(args_str):
    print(args_str)


func_print('hello')


------------------------

func_print('hello')


def func_print(args_str):
    print(args_str)


会出现以下错误，说明程序是顺序执行脚本文件的，
NameError: name 'func_print' is not defined

优秀的编程方式是，先统一引入模块，定义类和函数，最后统一进行调用执行
引入
定义
和执行部分，统一分割开来
"""


def func_print(args_str):
    """
    传入一个字符串。并将其打印出来
    :param args_str:
    :return:
    """
    print(args_str)


func_print('hello')
