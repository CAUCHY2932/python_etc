from collections import Counter
import string
import random


ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

# print('ran_str', ran_str)

random_str_ls = [(x, ran_str) for x in range(100)]

demo_ls = [(x, str(y)) for x, y in zip(range(10), range(6, 16))]
demo_ls_2 = [
    (1, 'a'),
    (1, 'a'),
    (3, 'b'),
    (4, 'b'),
    (1, 'a'),
    (1, 'b'),
]

new_ls = random_str_ls + random_str_ls[:4] + random_str_ls[2:8] + random_str_ls[3:18]
wc = Counter(new_ls)

a = wc.most_common(5)
print(a)
print(type(a))

# print(string.ascii_letters)
