# -*- coding:utf-8 -*-

"""
    2019/4/4 13:13 by young
"""
"""
    做为 Apple Store App 独立开发者，你要搞限时促销，
    为你的应用生成激活码（或者优惠券），
    使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random
import string

def gen_str(num):
    """
    随机生成num位的激活码
    :param num: 位数
    :return: 生成的字符串
    """
    # 字符串测试
    # lst_of_chars = [
    #     chr(i) for i in range(97, 123)
    # ]
    # print(string.ascii_uppercase)
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(lst_of_chars)

    # list_of_chars = [
    #     i for i in string.ascii_letters
    # ] + list(range(10))

    # list_of_chars = list(string.ascii_letters) + list(
    #     range(10)
    # )

    # 这里要保证每个数字都是字符类型，不然join会报错
    # list_of_chars = list(string.ascii_letters)+ [
    #     str(i) for i in range(10)
    # ]
    # 改进版
    list_of_chars = list(string.ascii_letters + string.digits)
    list_rand = random.sample(list_of_chars, num)
    return ''.join(list_rand)

def go(loop_num, str_length):
    gen_lst = [
        gen_str(str_length)
        for _ in range(loop_num)
    ]
    return gen_lst

if __name__ == "__main__":
    lst = go(200, 23)
    for item in lst:
        print(item)

