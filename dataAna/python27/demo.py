# -*- coding:utf-8 -*-

"""
    2019/4/3 16:08 by young
"""


from recsys import algorithm
algorithm.VERBOSE = True

from recsys.algorithm.factorize import SVD

svd = SVD()


svd.load_data(filename='./data/movielens/ratings.dat',
              sep='::',
              format={'col':0,
                      'row':1,
                      'value':2,
                      'ids': int})





