# coding:utf-8

# chr将ASCII转换为字符
# ord将字符转换为ASCII


# 用户输入字符
c = input("请输入一个字符: ")
 
# 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: ")) # 10进制转换
a = int(input("请输入一个ASCII码: "), 16) # 16进制转换

 
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
print(type(chr(a)))
print(type(ord(c)))

