# coding:utf-8

import os

import shutil



old_file_path='./temp'

new_file_path='./new'
# list_text=[]
with open('./123.txt','r') as f:
    list_text=[x for x in f.readlines()]



# lst=[os.path.splitext(y)[0] for y in file_list]
list_file=[os.path.splitext(y) for y in os.listdir(old_file_path)]

# print(list_file)
# for item in lst:
#     print(item)
# file_name_list=[y os.path.splitext(x) for x in os.listdir(old_file_path)]
# n=1
for item in list_text:
    # print(item)
    for item_2 in list_file:
        if item.strip()==item_2[0].strip():
            # print(item,item_2)
            move_item='{}{}'.format(item_2[0],item_2[1])

            try:
                old_path='{}/{}'.format(old_file_path,move_item)
                new_path='{}/{}'.format(new_file_path,move_item)
                print(old_path)
                print(new_path)
                shutil.move(old_path,new_path)
                print('{} has been moved'.format(move_item))
            except Exception as e:
                print('error:{}'.format(e))


#     for pre, suffix in list_file:
#         # print(pre)
#         print(len(pre.strip()),len(item.strip()))
#         n+=1
        
#         # if n==100:
#         #     exit(0)
#         # if pre==item:
#         #     print(pre)
#         # if item in item_2[0]:
#         #     print(item,item_2)

# print('#'*100)
# print(n)




    # if item in list_file:
    #     try:
    #         old_path='{}/{}'.format(old_file_path,item)
    #         new_path='{}/{}'.format(new_file_path,item)
    #         print(old_path)
    #         print(new_path)
    #         shutil.move(old_path,new_path)
    #         print('{} has been moved'.format(item))
    #     except Exception as e:
    #         print('error:{}'.format(e))
    # else:
    #     pass