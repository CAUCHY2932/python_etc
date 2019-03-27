# coding:utf-8
__author__ = "young"
import numpy as np


file_name = './presidential_polls.csv'

data_array = np.loadtxt(
    file_name,
    delimiter=',',
    dtype=str,
    usecols=(0, 2, 3)
)


print(data_array, data_array.shape)
