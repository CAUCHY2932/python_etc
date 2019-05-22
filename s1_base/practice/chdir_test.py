# coding:utf-8

import os

filePath=''

if not os.path.exists('testDir'):
	os.mkdir('testDir')


pwdDir=os.getcwd()
print('current dir is {}'.format(pwdDir))

os.chdir('testDir')


if not os.path.exists('sub_testDir'):
	os.mkdir('sub_testDir')

os.chdir('sub_testDir')
#for item in range(10):
#	with open('{}.txt'.format(item),'w') as f:
#		f.write('this is my {} file!'.format(item))

#for item in range(10):
#	with open('{}.txt'.format(item),'w') as f:
#		f.write('this is my {} file!'.format(item))
	

print('*'*30)
pwdDir=os.getcwd()
print('current dir is {}'.format(pwdDir))
fileList=os.listdir('./')
for item in fileList:
	print(item)
	os.rename(item,'new-{}'.format(item))
	print('{} has been changed!'.format(item))

fileList=os.listdir('./')
for item in fileList:
	print(item)
