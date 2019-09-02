# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/14 14:17
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from pyspark.shell import spark

df = spark.read.format("image").option("dropInvalid", True).load("data/mllib/images/origin/kittens")
df.select("image.origin", "image.width", "image.height").show(truncate=False)

