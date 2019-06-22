# -*- coding: utf-8 -*-
import oss2
import os

# ---------------------------setting---------------------------------
# 当前待上传图片的文件夹
currentFolder='upload'
# 需要上传到的bucket
uploadBucket='jncpic'
# 需要上传到的阿里云的子目录
bucketFolder='jzzl201901'
config = {}

config['AccessKeyId']=''
config['AccessKeySecret']=''
config['endpoint']=''


# ---------------------------setting---------------------------------



def upload_pic(fileName, relativePath, BucketName, folderName):
    AccessKeyId=config.get(AccessKeyId)
    AccessKeySecret=config.get(AccessKeySecret)
    endpoint=config.get(endpoint)
    # BucketName=BucketName
    # fileName='20180607203719 - 副本.jpg'
    localFile='./{relativePath}/{fileName}'.format(relativePath=relativePath,fileName=fileName)
    # folderName=bucketFolder
    objectName='{folderName}/{fileName}'.format(folderName=folderName,fileName=fileName)
    try:
        auth = oss2.Auth(AccessKeyId, AccessKeySecret)
        bucket = oss2.Bucket(auth, endpoint, BucketName)
        bucket.put_object_from_file(objectName, localFile)
        print('-*-'*40)
        print('{fileName} has been upload!'.format(fileName=fileName))
    except Exception as e:
        with open('./unupload.csv', 'a+') as f:
            f.write(fileName+'\n')
        print('出错了')
        print(e)


# def errorHandler(fileName):
#     with open('./unupload.csv', 'a+') as f:
#         f.write(fileName+'\n')

def main():
    relativePath=currentFolder
    fielPath='./{relativePath}'.format(relativePath=relativePath)
    list_file=os.listdir(fielPath)
    print('-'*100)
    print('folder have {} files!'.format(len(list_file)))
    print('-'*100)

    n=0
    for item in list_file:
        print(item)
        upload_pic(item, relativePath, uploadBucket, bucketFolder)
        # errorHandler(item)
        n+=1
        print('@'*80)
        print('having upload {}!'.format(n))

if __name__=='__main__':
    main()