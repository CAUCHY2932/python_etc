# -*- coding:utf-8 -*-

"""
    2019/4/3 10:49 by young
"""
import numpy as np
from sklearn import preprocessing

def data_matrix(file_name):
    """
    将文本转化为matrix
    :param file_name:文件名
    :return: 数据矩阵
    """
    with open(file_name, 'r') as fr:
        array_lines = fr.readlines()
    number_lines = len(array_lines)
    return_mat = np.zeros((number_lines, 3))

    index = 0
    for line in array_lines:
        line = line.strip()
        list_line = line.split('\t')
        return_mat[index, :] = list_line[0:3]
    return return_mat

def data_matrix_mine(file_name):
    """
    自己实现一些更加简洁的写法，使用列表推导式
    :param file_name: 文件名
    :return: 数据矩阵
    """
    with open(file_name, 'r') as fr:
        array_lines = fr.readlines()
    content_lst = [line.strip().split('\t')[0:3]
                   for line in array_lines]
    return np.array(content_lst)

def feature_normal(data_set):
    """
    特征归一化
    :param data_set: 数据集
    :return:
    """
    # 每列最小值
    min_val = data_set.min(0)
    # 每列最大值
    max_val = data_set.max(0)
    ranges = max_val - min_val
    norm_data = np.zeros(np.shape(data_set))
    # 得出行数
    m = data_set.shape[0]
    # 矩阵相减
    norm_data = data_set - np.tile(min_val, (m, 1))
    # 矩阵相除
    norm_data = norm_data/np.tile(ranges, (m, 1))
    return norm_data

def feature_normal_mine(data_set):
    """
    特征归一化的我的版本
    无需构造新的矩阵
    :param data_set: 数据集
    :return:
    """
    min_val = data_set.min(0)
    max_val = data_set.max(0)
    ranges = max_val - min_val
    # min_mat = np.ones(np.shape(data_set)) * min_val
    norm_data = (data_set - min_val)/ranges
    return norm_data

# 利用scikit-learn.preprocessing中的类MinMaxScaler，将数据矩阵缩放到[0,1]之间
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
print(X_train_minmax)
