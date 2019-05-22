# -*- coding: utf-8 -*-
import oss2
import os

config={}

config['AccessKeyId'] = ''
config['AccessKeySecret'] = ''
config['endpoint'] = ''

def upload_pic(fileName, relativePath):
    AccessKeyId = config.get(AccessKeyId)
    AccessKeySecret = config.get(AccessKeySecret)
    endpoint=config.get(endpoint)
    BucketName='jnctest'
    localFile='./{relativePath}/{fileName}'.format(relativePath=relativePath,fileName=fileName)
    folderName='testUpload'
    objectName='{folderName}/{fileName}'.format(folderName=folderName,fileName=fileName)
    try:
        auth = oss2.Auth(AccessKeyId, AccessKeySecret)
        bucket = oss2.Bucket(auth, endpoint, BucketName)
        bucket.put_object_from_file(objectName, localFile)
        print('-*-'*80)
        print('{fileName} has been upload!'.format(fileName=fileName))
    except Exception as e:
        print('出错了')
        print(e)


def main():
    relativePath='upload'
    fielPath='./{relativePath}'.format(relativePath=relativePath)
    list_file=os.listdir(fielPath)
    n=0
    for item in list_file:
        print(item)
        upload_pic(item,relativePath)
        n+=1
        print('@'*80)
        print('having upload {}!'.format(n))

def print_a():
        print('hello')


if __name__=='__main__':
    main()