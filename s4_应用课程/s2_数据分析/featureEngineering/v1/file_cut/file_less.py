# -*- coding:utf-8 -*-

"""
    2019/4/12 17:17 by young
"""


import os


def split_file(file_name, dist_dir, chunk_size=100000, encoding='utf-8'):
    """

    :param file_name:
    :param dist_dir:
    :param chunk_size:
    :param encoding:
    :return:
    """
    # 判断文件
    # os.path.ex
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    # 判断文件类型
    _, suffix = os.path.splitext(file_name)
    part_num = 0

    with open(file_name, 'r', encoding=encoding) as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_num += 1
            file_part_name = os.path.join(dist_dir, ('part%04d' % part_num)+suffix)
            with open(file_part_name, 'w', encoding='utf-8') as f_part:
                f_part.write(chunk)


split_file('data1.txt', 'data_split')


# import sys,os
#
# kilobytes = 1024
# megabytes = kilobytes*1000
# chunksize = int(200*megabytes)#default chunksize
#
# def split(fromfile,todir,chunksize=chunksize):
#     if not os.path.exists(todir):#check whether todir exists or not
#         os.mkdir(todir)
#     else:
#         for fname in os.listdir(todir):
#             os.remove(os.path.join(todir,fname))
#     partnum = 0
#     inputfile = open(fromfile,'rb')#open the fromfile
#     while True:
#         chunk = inputfile.read(chunksize)
#         if not chunk:             #check the chunk is empty
#             break
#         partnum += 1
#         filename = os.path.join(todir,('part%04d'%partnum))
#         fileobj = open(filename,'wb')#make partfile
#         fileobj.write(chunk)         #write data into partfile
#         fileobj.close()
#     return partnum
# if __name__=='__main__':
#         fromfile  = input('File to be split?')
#         todir     = input('Directory to store part files?')
#         chunksize = int(input('Chunksize to be split?'))
#         absfrom,absto = map(os.path.abspath,[fromfile,todir])
#         print('Splitting',absfrom,'to',absto,'by',chunksize)
#         try:
#             parts = split(fromfile,todir,chunksize)
#         except:
#             print('Error during split:')
#             print(sys.exc_info()[0],sys.exc_info()[1])
#         else:
#             print('split finished:',parts,'parts are in',absto)