# 列表推导(条件筛选)
# map和filter
a = [x**2 for x in range(10) if x % 2 == 0]
print(a)
# 集合推导
b = {x**2 for x in range(10) if x%2==0}
print(b)
# 元组推导(生成器)，可迭代
c = (x**2 for x in range(10) if x%2==0)
print(c)

# 字典推导
d = {k:v for k, v in zip(range(10), range(6, 23))}
print(d)
demo_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
e = [k for k, v in demo_dict.items()]
print(e)
