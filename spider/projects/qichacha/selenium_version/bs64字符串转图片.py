# import os,base64 
# strs='''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\n\n\n\n\n \n\n\n'''
 
# imgdata=base64.b64decode(strs)
# file=open('1.jpg','wb')
# file.write(imgdata)
# file.close()
 
import os
import base64
import re


strs='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'


imgdata=base64.b64decode(strs)
file=open('1.jpg','wb')
file.write(imgdata)
file.close()


# pattern = re.compile('.*?<img src="(.*?)">.*?',re.S)
# ret=re.search(pattern,content).group(1)
# print(ret)