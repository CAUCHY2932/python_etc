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
# import pandas as pd
import re
from conn_mongo import MongodbSaver

# def cut_rows(file_name: str, encoding: str='utf-8', items: int=20) -> None:
#     data = pd.read_csv(file_name, nrows=1,header=None)
#     print(data)


def cut_rows_mine(file_name: str, encoding: str = 'utf-8', items: int = 20) -> None:

    with open(file_name, 'r', encoding=encoding) as f:
        line = f.readline()

    cut_str = line.split(',')
    
    waiting_cut_str = cut_str[2]

    soh = chr(int('0x01', 16))
    stx = chr(int('0x02', 16))
    etx = chr(int('0x03', 16))
    # after_cut_str_list = re.split(f'{soh}|{stx}|{etx}', waiting_cut_str) # 按照所有的进行切分
    after_cut_str_list = re.split(f'{soh}', waiting_cut_str) # 按照特征进行切分
    length = len(after_cut_str_list)
    for item in range(length):
        print(after_cut_str_list[item])
    # print(length)
    # print(cut_str[1])


def cut_rows_mine2(file_name: str, encoding: str = 'utf-8') -> None:
    """


    :param file_name: 传入文件名
    :param encoding: 文件默认编码
    :return: 返回生成的字典
    """
    with open(file_name, 'r', encoding=encoding) as f:
        line = f.readline()

    cut_str = line.split(',')
    # print(cut_str[0], cut_str[1])
    waiting_cut_str = cut_str[2]

    soh = chr(int('0x01', 16))
    # stx = chr(int('0x02', 16))
    # etx = chr(int('0x03', 16))
    # after_cut_str_list = re.split(f'{soh}|{stx}|{etx}', waiting_cut_str)
    after_cut_str_list = re.split(f'{soh}', waiting_cut_str)
    # length = len(after_cut_str_list)
    # for item in range(length):
    #     print(after_cut_str_list[item])
    return after_cut_str_list, cut_str[0], cut_str[1]


def cut_lines(after_cut_str_list):
    """


    :param after_cut_str_list: 切分id, length之后的字符串
    :return: 生成器结果，包含所有特征的列表
    """
    stx = chr(int('0x02', 16))
    etx = chr(int('0x03', 16))
    for i in after_cut_str_list:
        single_feature = re.split(f'{stx}|{etx}', i)
        yield {
            'feature_field_id': single_feature[0],
            'feature_id': single_feature[1],
            'feature_value': single_feature[2],
        }
    pass


if __name__ == '__main__':

    lst, record_id, length = cut_rows_mine2(r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv')
    after_handle_list = cut_lines(lst)
    mongo_url = 'localhost'
    mongo_db = 'user_new'
    mongo_table = 'sample11'

    demo_dict = {
        '_id': record_id,
        'length': length,
        # '_id': a['id'],
        # 'length': a['length'],
        'feature_list': [item for item in after_handle_list]
    }

    with MongodbSaver(mongo_url, mongo_db, mongo_table) as ms:
        ms.save(demo_dict)
