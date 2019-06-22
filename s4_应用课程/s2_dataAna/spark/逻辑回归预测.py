# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/5/16 9:27
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""



# Every record of this DataFrame contains the label and
# features represented by a vector.
# from pyspark.ml.classification import LogisticRegression
# from pyspark.shell import sqlContext
#
# df = sqlContext.createDataFrame(data, ["label", "features"])
#
# # Set parameters for the algorithm.
# # Here, we limit the number of iterations to 10.
# lr = LogisticRegression(maxIter=10)
#
# # Fit the model to the data.
# model = lr.fit(df)
#
# # Given a dataset, predict each point's label, and show the results.
# model.transform(df).show()
