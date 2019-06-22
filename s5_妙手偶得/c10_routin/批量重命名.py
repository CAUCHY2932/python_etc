# coding:utf-8
# 批量文件重命名

import os


def fileRename():
    fileFolder=input('请输入待处理文件的文件夹：\n')
    filePath='./{}'.format(fileFolder)
    if not os.path.exists(filePath) :
        print('输入的文件夹不存在，请重新输入：')
        fileRename()
    else:
        fileList=os.listdir(filePath)
        fileNewType=input('请输入新文件类型：\n')
        for item in fileList:
            try:
                fileSplit=os.path.splitext(item)
                pre,suffix=fileSplit
                newDir='{}/{}.{}'.format(filePath,pre,fileNewType)
                oldDir='{}/{}'.format(filePath,item)
                os.rename(oldDir,newDir)
                print('{}\t已被修改为-->\t{}'.format(oldDir,newDir))
            except Exception as e:
                print('find error: {}'.format(e))
    return None

# def main():
#     fileRename()


if __name__=='__main__':
    fileRename()
