# coding:utf-8
import re
import pymongo


class MongodbSaver(object):

    def __init__(self, mongo_url, mongo_db, mongo_table):
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


def cut_rows(file_name, encoding='utf-8'):

    with open(file_name, 'r', encoding=encoding) as f:
        line = f.readline()

    cut_str = line.split(',')

    return cut_str


def cut_lines(cut_str):

    soh = chr(int('0x01', 16))
    stx = chr(int('0x02', 16))
    etx = chr(int('0x03', 16))
    after_cut_str_list = re.split('{}'.format(soh), cut_str)

    for i in after_cut_str_list:
        single_feature = re.split('{}|{}'.format(stx, etx), i)
        yield {
            'feature_field_id': single_feature[0],
            'feature_id': single_feature[1],
            'feature_value': single_feature[2]}


def data_model(after_handle_list):

    return {'_id': record_id,
            'length': length,
            'feature_list': [item for item in after_handle_list]}


if __name__ == '__main__':

    file_name = r'C:\Users\34853\Documents\WeChat Files\amoswewin\FileStorage\File\2019-04\123.csv'
    record_id, length, lst = cut_rows(file_name)

    after_handle_list = cut_lines(lst)

    mongodb_url = 'localhost'
    mongodb_name = 'user_new'
    mongodb_table = 'sample12'

    demo_dict = data_model(after_handle_list)

    with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
        ms.save(demo_dict)
