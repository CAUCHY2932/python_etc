# coding:utf-8

from hdfs3 import HDFileSystem

hdfs=HDFileSystem(host='localhost',port=8020)

hdfs.ls('/user/data')
hdfs.put('local-file')