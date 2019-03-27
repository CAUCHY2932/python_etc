# -*- coding:utf-8 -*-

"""
显示目录树结构
"""

from sys import argv

import os


def fileCntTree(curPath):
    """
    汇总当前目录下的文件数
    :param curPath:
    :return:
    """
    return sum([len(files) for root, dirs, files in os.walk(curPath)])


def dirsTree(startPath):
    for root, dirs, files in os.walk(startPath):
        fileCount =  fileCntTree(root)
        level=root.replace(startPath, '').count(os.sep)






        indent = '| '*1*level+"|___"
        print('{}{} -r:{}'.format(indent, os.path.split(root)[1], fileCount))

        for file in files:
            indent ="| "*1 *(level+1)+"|____"
            print('{}{}'.format(indent, file))




if __name__=="__main__":
    # path=argv[1]
    # path=input('input your column:\n')
    path='./'
    dirsTree(path)
