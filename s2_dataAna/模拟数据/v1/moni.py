# coding:utf-8

from faker import Faker

fake = Faker(locale='zh_CN')


from faker import Faker


# fake=Faker() #默认生成美国英文数据
fake=Faker(locale='zh_CN')

# 地址类
print("地址类".center(20,"-"))
print(fake.address())#海南省成市丰都深圳路p座 425541
print(fake.street_address())#深圳街X座
print(fake.street_name())#长沙路
print(fake.city_name(),fake.city())#兰州 贵阳市  (相差“市”)
print(fake.province())#陕西省


#公司类：
print("公司类".center(20,"-"))
print(fake.company())#惠派国际公司信息有限公司
print(fake.company_suffix())#网络有限公司
print(fake.company_prefix())#鑫博腾飞

#个人信息类
print("个人信息类".center(20,"-"))
print(fake.name())#东浩
print(fake.simple_profile())
#{'username': 'leihan', 'name': '武帅', 'sex': 'F', 'address': '吉林省淮安市双滦家街C座 210434', 'mail': 'lishao@hotmail.com', 'birthdate': '1988-11-12'}
print(fake.user_name(),fake.password(special_chars=False))#ajiang zI2QbHy02p

#文章类
print("文章类".center(20,"-"))
print(fake.word())#当前
print(fake.words(3))#['欢迎', '支持', '图片']
print(fake.sentence(3))#精华有关一些.
print(fake.paragraph())#大家电话空间一起操作图片要求.上海发展到了之间用户也是的人.必须记者关系介绍注册.用户时候投资发布.