# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 20:02 
"""

__author__ = 'young'



"""
+= 不会创建新对象，+会创建新对象
"""

a_lst = [1, 2]

a_lst = a_lst+a_lst
print(a_lst)

c_lst = [4, 5]
c_lst += c_lst
print(c_lst)




