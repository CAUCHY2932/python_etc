# -*- coding:utf-8 -*-
"""
    create by young on 2018/12/26 15:51
"""
import os
__author__ = 'young'


# 对os.walk进行二次封装

def traversal_file(file_path,file_operate_type):
    """


    :param file_path:
    :return:
    """
    # for item in file_path:

    # file_path_generator=os.walk(file_path)
    # dirpath, dirnames, filenames=os.walk(file_path)
    for item in os.walk(file_path):
        dirpath, dirnames, filenames=item   #解包
        for file_name in filenames:

            file_abspath=os.path.join(dirpath,file_name)
            # operate
            a=file_operate_type
    pass





def file_rename():
    """

        对一个文件进行重命名
    :return:
    """
    pass


def file_docToDocx():
    pass


def file_docToPdf():
    pass