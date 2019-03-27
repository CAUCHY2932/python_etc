# -*- coding:utf-8-*-

# 合并多个文件到一个文件中去


__author__='yang'



import pandas as pd
import os


filePath= './works'
if os.path.exists('./worked'):
    os.mkdir('./worked')
savePath='./worked'
saveFileName='sum.csv'

fileList=os.listdir(filePath)

df=pd.read_csv("{}/{}".format(filePath,fileList[0]))
try:
    for i in fileList[1:]:
        print('{} is ok'.format(i))
        df=pd.read_csv('{0}/{1}'.format(filePath,i))

        df.to_csv('{0}/{1}'.format(savePath,saveFileName),encoding='utf-8', header=False, index=False, mode='a+')
except Exception as e:
    print('error:{}'.format(e))
