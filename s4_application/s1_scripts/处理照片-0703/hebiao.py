# coding:utf-8
import os
file_name = 'success'

lst = os.listdir('./{}'.format(file_name))
print(lst)


def write_to_file(lst_index):
    with open('./{}.csv'.format(file_name),'a+')as f:
        for i in lst_index:
            f.write(i)


for item in lst:
    with open('./{}/{}'.format(file_name, item),'r')as f:
        write_to_file(f.readlines())





