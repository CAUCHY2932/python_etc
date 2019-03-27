# coding:utf-8

import os

import shutil



old_file_path='./temp'

new_file_path='./new'
# list_text=[]
with open('./123.txt','r') as f:
    list_text=[x for x in f.read()]


file_list=os.listdir(old_file_path)
for item in list_text:
    if item in file_list:
        try:
            old_path='{}/{}'.format(old_file_path,item)
            new_path='{}/{}'.format(new_file_path,item)
            shutil.move(old_path,new_path)
        except Exception as e:
            print('error:{}'.format(e))
    else:
        pass