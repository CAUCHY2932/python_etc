# -*-coding:utf-8-*-

import requests



# setting
relative_base_url='http://www.jnc.com.cn/cn/pages/topicNewsList.xml?&pid='
pageNum=''




def getContent(url):
    """
    传入网址，输出解析的网页内容
    :return:
    """
    headers={
        "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:62.0) Gecko/20100101 Firefox/62.0",

    }
    response=requests.get(url=url,headers=headers)
    if response.status_code==200:
        response.encoding = response.apparent_encoding
        responseText=response.text
    return responseText

def writToText(fileText, fileName):
    """
    传入文本内容，文件名字，写入到文件中
    :return:
    """
    filePath='./{fileName}'.format(fileName=fileName)
    with open(filePath, 'w') as f:
        f.write()

def main():
    for i in range(1,8):
        url=relative_base_url+i
        text=getContent(url)
        writToText("{}.txt".format(i))



    pass


if __name__ == '__main__':
    main()




