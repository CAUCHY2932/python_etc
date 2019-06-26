# coding: utf-8


import pandas as pd
import time

def process(chunk):
    # chunk.to_csv(r'D:\0621\new_records.csv', mode='a', header=False)
    for index, item in chunk.iterrows():
        print(item["banquet_addr"], item["banquet_id"])
    # print(chunk)
    pass


def split_chunk_read(file_name, usecols=None,chunk_size=100):
    item = 10
    for chunk in pd.read_csv(file_name, usecols=usecols, header=None,chunksize=chunk_size):
        chunk.columns =['banquet_id', 'banquet_addr'] # banquet_id 宴会单号, banquet_addr 宴会地址
        process(chunk)
        item = item + 1
        if item>10:
            break
        print('-'*12)
        time.sleep(3)


def split_chunk_read_test():
    split_chunk_read(r'D:\0621\addr_2017.csv', usecols=[0, 1])
    pass


if __name__ == "__main__":
    split_chunk_read_test()
    pass
