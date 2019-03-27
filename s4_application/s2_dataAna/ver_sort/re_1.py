import re

"""
?:匹配的子组不作为结果输出（不被捕获）
"""

def find_ver(version_num):

    pattern_str = '(?:[1-9]\d|[1-9])(\.(?:[1-9]\d|\d)){1,2}'

    pattern = re.compile(pattern_str)

    ret = re.match(pattern, version_num)
    return ret


# ret = find_ver('9a1.0b.c1')

# print(ret.group())
def print_result(version_num):
    print('{} \'s result is {}'.format(version_num, find_ver(version_num)))
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))

print_result('0.09.1')
# print_result('1a.b.2')
print_result('9.8.7')
# print_result('9.5a.9b')
print_result('30.6.1')
# print(find_ver('30.3.4').group(1))
# print_result('90b.3')
print_result('8.9.0')

print(find_ver('80.9.8'))
pattern_str = '(?:[1-9]\d|[1-9])(\.(?:[1-9]\d|\d)){1,2}'
print(re.findall(pattern_str, '2.3.4'))
