# -*-coding:utf-8 -*-
# os.path.splittxt()
# os.listdir()
# os.getcwd()
# os.rename()

import os


def changeSingle(fileName,suffixPre,suffixAfter):
    """
    fileName指的是文件名
    suffix指的是后缀名
    """
    partion= os.path.splitext(fileName)
    print(partion)

    if partion[1]=='.'+suffixPre:
        nameNew=partion[0]+'.'+suffixAfter

def changeFileName
files=os.listdir('')