# -*- coding:utf-8 -*-

"""
    2019/4/16 9:54 by young
"""


demo_text1 = """nihao\n
wode
"""
demo_text2 = """nihao\n
wode"""
demo_text3 = """nihao\nwode\n"""

print('demo_text{} lines is {}'.format(1, len(demo_text1)))
print('demo_text{} lines is {}'.format(2, len(demo_text2)))
print('demo_text{} lines is {}'.format(3, len(demo_text3)))

file_name = 'test_data.txt'
with open(file_name, 'r') as f:
    # fr = f.read()
    frl = f.readlines()
# print(fr)
print(len(frl))


