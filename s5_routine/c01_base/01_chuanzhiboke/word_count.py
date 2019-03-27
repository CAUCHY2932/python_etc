# -*- coding:utf-8 -*-


str_demo = 'hello world'
dict_demo = {}
for item in str_demo:
	if item not in dict_demo:
		dict_demo[item]=1
	else:
		dict_demo[item]+=1

print(dict_demo)

