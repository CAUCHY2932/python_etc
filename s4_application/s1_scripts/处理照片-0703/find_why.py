import os


lst = os.listdir('./tmp')

img_list = ''

with open('success.csv') as f:
    fr = f.readlines()

# for item in lst:
#     print(item.strip())
# n = 0
# for item in fr:
#     # print(item.strip())
#     if item.strip() in lst:
#         n = n + 1
#         print(f'[error]-{n}', item.strip())
print(len(lst))


print(len(set(fr)))
