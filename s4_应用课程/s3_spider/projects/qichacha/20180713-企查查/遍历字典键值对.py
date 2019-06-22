遍历字典
这里有两种方法

方法1：先获取key，然后通过dic[key]获取value
>>> for key in dic:
...     print 'key is %s,value is %s'%(key,dic[key])
...
key is id,value is 001
key is age,value is 30
key is name,value is zhangsan
key is sex,value is male
1
2
3
4
5
6
7
方法2：对字典items()方法返回的元组列表进行序列解包
>>> for key,value in dic.items():
...     print 'key is %s,value is %s'%(key,value)
...
key is id,value is 001
key is age,value is 30
key is name,value is zhangsan
key is sex,value is male