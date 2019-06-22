# coding:utf-8-*-

with open('./unupload.csv', 'r') as f:
    list_file=f.readlines()

for item in list_file:
    print(item)