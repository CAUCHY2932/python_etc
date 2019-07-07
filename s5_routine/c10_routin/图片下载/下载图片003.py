# coding:utf-8

import requests
import re
import os


def download_img(url):
    # url='http://jnc.fyun.online/JNC2017/?fileid=2018-10-20/201810201628431136.jpg&filename=X-YHBB20180934441136-1.jpg'
    try:
        # 获取文件名
        pattern=re.compile('filename=(.*)')
        file_name=re.search(pattern, url).group(1)
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        response=requests.get(url, headers=headers)
        response.encoding=response.apparent_encoding
        with open('./photos/{file_name}'.format(file_name=file_name),'wb')as f:
            f.write(response.content)
        print('{file_name} has been downloaded!\n'.format(file_name=file_name))
    except Exception as e:
        print('error :{}'.format(e))


# def main():
#     # 如果目标文件夹不存在，就新建
#     if not os.path.exists('./photos'):
#         os.makedirs('./photos')
#     # 读取图片地址序列
#     try:
#         with open('./图片地址序列.txt', 'r')as f:
#             file_name_list=f.readlines()
#         for order_num, item in enumerate(file_name_list):
#             print('{} is downloading'.format(order_num))
#             download_img(item)
#     except Exception as e:
#         print('error: {}'.format(e))

# if __name__=="__main__":
#     main()

# url='http://jnc.fyun.online/JNC2017/?fileid=2018-10-20/20181020131057325.jpg&filename=X-YHBB20181029880325-3.jpg'


# # url=''
# download_img(url)



with open('./图片地址序列.txt', 'r')as f:
    file_name_list=f.readlines()
for order_num, item in enumerate(file_name_list):
    print('{} is downloading'.format(order_num))
    # download_img(item)
    print(item)
    print(type(item))
    
