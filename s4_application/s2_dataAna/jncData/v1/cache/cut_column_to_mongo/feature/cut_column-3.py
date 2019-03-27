# coding:utf-8
import re
import pymongo


class MongodbSaver(object):
    """

    保存所有的数据到mongodb
    传入一个字典数据
    返回处理结果
    pymongo相关操作
    """

    def __init__(self, mongo_url, mongo_db, mongo_table):
        """

        :param mongo_url:
        :param mongo_db:
        :param mongo_table:
        """
        self.mongo_table = mongo_table
        self.client = pymongo.MongoClient(mongo_url, connect=False)
        self.db = self.client[mongo_db]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def save(self, result):
        """
        把字典数据插入mongodb

        :param result: 字典格式
        :return: bool值，确定是否插入成功
        """
        if self.db[self.mongo_table].insert(result):
            print('Successfully Saved to Mongodb', result)
            return True
        return False


def cut_rows_mine2(file_name: str, encoding: str = 'utf-8'):
    """
    :param file_name: 传入文件名
    :param encoding: 文件默认编码
    :return: 返回生成的字典
    """
    with open(file_name, 'r', encoding=encoding) as f:
        line = f.readline()

    cut_str = line.split(',')
    waiting_cut_str = cut_str[2]

    soh = chr(int('0x01', 16))
    after_cut_str_list = re.split(f'{soh}', waiting_cut_str)
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


if __name__ == '__main__':

    file_name = ''
    lst, record_id, length = cut_rows_mine2(file_name)

    after_handle_list = cut_lines(lst)

    mongo_url = 'localhost'
    mongo_db = 'user_new'
    mongo_table = 'sample11'

    demo_dict = {
        '_id': record_id,
        'length': length,
        'feature_list': [item for item in after_handle_list]
    }

    with MongodbSaver(mongo_url, mongo_db, mongo_table) as ms:
        ms.save(demo_dict)
