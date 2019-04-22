# -*- coding:utf-8 -*-

"""
    2019/4/22 22:30 by young
"""
import random
import string


def gen_random_str(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


print(gen_random_str(19))
