# -*- coding=utf-8 -*-
"""
    2019/3/14 16:35
    author:young
"""

from sympy import *

init_printing()
# 定义符号常量x 与 f(x) g(x)。这里的f g还可以用其他字母替换，用于表示函数
x = Symbol('x')
f, g = symbols('f g', cls=Function)

# 用diffeq代表微分方程： f''(x) − 2f'(x) + f(x) = sin(x)
diffeq = Eq(f(x).diff(x, x) - 2 * f(x).diff(x) + f(x), sin(x))
# 调用dsolve函数,返回一个Eq对象，hint控制精度
print(dsolve(diffeq, f(x), hint='1st_linear'))
