# coding:utf-8

"""
由于记录中包含了若干非法字符，如

{
    '0x01': 'SOH',# 标题开始
    '0x02': 'STX',# 正文开始
    '0x03': 'ETX',# 正文结束
}
将其进行切分
"""
import pandas as pd 


def cut_rows(file_name: str, encoding: str='utf-8', items: int=20) -> None:
    data = pd.read_csv(file_name, nrows=1, header=None)
    print(data)


def cut_rows_mine(file_name: str, encoding: str= 'utf-8', items: int=20) -> None:
    import re

    with open(file_name, 'r', encoding=encoding) as f:
        line = f.readline()

    cut_str = line.split(',')
    
    waiting_cut_str = cut_str[2]

    soh = chr(int('0x01', 16))
    stx = chr(int('0x02', 16))
    etx = chr(int('0x03', 16))
    after_cut_str_list = re.split(f'{soh}|{stx}|{etx}', waiting_cut_str)
    # after_cut_str_list = re.split(f'{soh}', waiting_cut_str)
    length = len(after_cut_str_list)
    for item in range(length):
        print(after_cut_str_list[item])
    print(length)
    print(cut_str[1])


if __name__ == '__main__':
    cut_rows_mine('./common_features_test.csv')
