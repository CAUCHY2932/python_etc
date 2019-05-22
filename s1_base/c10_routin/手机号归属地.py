# coding:utf-8
# 查找手机号归属地
# 依赖模块
# pip install phone
from phone import Phone

phoneNum=input('请输入手机号:\n')
p=Phone()
phoneInfo=p.find(phoneNum)
print(phoneInfo)

try:
    phone=phoneInfo['phone']
    province=phoneInfo['province']
    city=phoneInfo['city']
    zipCode=phoneInfo['zip_code']
    areaCode=phoneInfo['area_code']
    phoneType=phoneInfo['phone_type']
    print('-'*40)
    print('手机号：\t\t{}'.format(phone))
    print('所在省份：\t\t{}'.format(province))
    print('所在城市：\t\t{}'.format(city))
    print('邮编：\t\t\t{}'.format(zipCode))
    print('地区座机代码：\t\t{}'.format(areaCode))
    print('运营商类型：\t\t{}'.format(phoneType))
    print('-'*40)

except Exception as e:
    print('find error:{}'.format(e))
    pass
