# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/24 15:39
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import pandas as pd


def split_csv_read(file_name, usecols=None, chunk_size=20000):
    # item = 10
    item = 1
    for chunk in pd.read_csv(file_name, usecols=usecols, chunksize=chunk_size):
        # chunk.columns = ['banquet_id', 'banquet_addr']  # banquet_id 宴会单号, banquet_addr 宴会地址
        # process(chunk)
        chunk.to_csv('./2018070{}.csv'.format(item), index=False, header=False)
        item = item + 1
        print('-' * 50)


if __name__ == '__main__':
    split_csv_read('./datasets/201807.csv', chunk_size=2000)
