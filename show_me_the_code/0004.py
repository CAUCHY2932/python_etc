# -*- coding:utf-8 -*-

"""
    2019/4/4 14:26 by young
"""
"""
 任一个英文的纯文本文件，统计其中的单词出现的个数

"""

# filter()
# map()
# reduce()
# lambda
def count_word(fileName):
    """

    :param fileName: 文件名
    :return: 返回一个字典，键是单词，值是次数
    """
    # with open(fileName, 'r') as f:
    #     fr_lines = f.readlines()
    # lines = [
    #     line.strip('\n') for line in fr_lines
    # ]
    #
    with open(fileName, 'r') as f:
        fr = f.read()

    word_list = fr.split(' ')
    # a = {}
    # for item in word_list:
    #     if a.get(item):
    #         a[item] += 1
    #     else:
    #         a[item] = 1

    # a ={
    #
    # }
    # 这里想要使用字典推导，但是处理逻辑复杂：
    # 需要判断是否含有某个键
    a = {}
    for item in word_list:
        a[item] = a[item] + 1 if a.get(item) else 1

    return a

str_demo ="""
    hello, this is a demo string to say hello to you!
    if you have heard, please give me a response so that I can process
    expected.
"""
with open('./str_demo.txt', 'a+') as f:
    f.write(str_demo)

print(count_word('./str_demo.txt'))
