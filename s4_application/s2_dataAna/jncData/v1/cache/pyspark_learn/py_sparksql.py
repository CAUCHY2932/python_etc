# -*- coding:utf-8 -*-

"""
    2019/4/22 14:44 by young
"""
from pyspark import SparkContext as sc
from pyspark.sql import SQLContext


sqlContext = SQLContext(sc)

df = sqlContext.read(source="com.databricks.spark.csv", header="true", path="cars.csv")
df.select("year", "model").save("newcars.csv", "com.databricks.spark.csv")
