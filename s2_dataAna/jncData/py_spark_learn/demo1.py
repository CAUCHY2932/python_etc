# -*- coding:utf-8 -*-

"""
    2019/4/15 11:04 by young
"""


from pyspark.shell import sc


lines = sc.textFile('./data.txt')
s = lines.count()
print(s)
