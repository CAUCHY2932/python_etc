# -*- coding:utf-8 -*-

"""
    2019/4/22 14:52 by young
"""

import os

# os.environ["PYSPARK_PYTHON"] = "D:\Miniconda3\envs\spark\python"

from pyspark import SparkContext

sc = SparkContext()
recs = sc.textFile('dna_seq.txt')
# print(recs.collect())

ones = recs.flatMap(lambda x: [(c, 1) for c in list(x)])
# print(ones.collect())

print(ones.reduceByKey(lambda x, y: x + y).collect())  # lambda x,y : x+y;from operator import add
