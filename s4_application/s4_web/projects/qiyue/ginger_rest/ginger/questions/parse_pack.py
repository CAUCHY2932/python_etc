# -*-encoding:utf-8 -*-
"""
    2019/4/20 5:06
    create by young
"""

"""
测试解包功能

demo_tuple = (2, 3, 4, 5, 65, 'ji', 9.08, True)

a, b, c = demo_tuple

print(a)
print(b)
print(c)

ValueError: too many values to unpack (expected 3)

更换之后即可

demo_tuple = (2, 3, 4, 5, 65, 'ji', 9.08, True)

a, b, *c = demo_tuple

print(a)
print(b)
print(c)
"""

demo_tuple = (2, 3, 4, 5, 65, 'ji', 9.08, True)

a, b, *c = demo_tuple

print(a)
print(b)
print(c)
