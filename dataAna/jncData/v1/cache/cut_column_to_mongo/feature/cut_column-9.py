# coding:utf-8
import re
import pymongo
import os


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


class Cutter(object):
    """
    改写为处理单行数据的返回内容
    """

    __slots__ = ('record_id', 'length', 'feature_str', 'feature_list', 'data', 'raw_record')

    def __init__(self, raw_record):
        self.record_id = None
        self.length = None
        self.feature_str = ''
        self.feature_list = None
        self.data = {}
        self.raw_record = raw_record

    def cut_to_record(self):
        self.__cut_line()
        self.feature_list = self.__cut_feature()
        self.__data_model()
        # return self.data

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

    def __cut_line(self):
        self.record_id, self.length, self.feature_str = self.raw_record.split(',')

    def __cut_feature(self):
        soh = chr(int('0x01', 16))
        stx = chr(int('0x02', 16))
        etx = chr(int('0x03', 16))
        after_cut_str_list = re.split('{}'.format(soh), self.feature_str)

        for i in after_cut_str_list:
            single_feature = re.split('{}|{}'.format(stx, etx), i)
            yield {'feature_field_id': single_feature[0],
                   'feature_id': single_feature[1],
                   'feature_value': single_feature[2]}

    def __data_model(self):
        self.data = {'_id': self.record_id,
                     'length': self.length,
                     'feature_list': [item for item in self.feature_list]}

    @staticmethod
    def split_file(file_name, dist_dir, return_files, chunk_size=100000, encoding='utf-8'):

        if not os.path.exists(dist_dir):
            os.mkdir(dist_dir)
        _, suffix = os.path.splitext(file_name)
        part_num = 0

        with open(file_name, 'r', encoding=encoding) as f:
            while True:
                chunk = ''.join((f.readline() for _ in range(chunk_size)))
                if (part_num >= return_files) or (not chunk):
                    break
                part_num += 1
                target_name = 'part{0:0>12}{1}'.format(part_num, suffix)
                file_part_name = os.path.join(dist_dir, target_name)
                with open(file_part_name, 'w', encoding='utf-8') as f_part:
                    f_part.write(chunk)
                    print('write {} file succesfully!'.format(target_name))


class Reader(object):
    """
    撰写一个上下文管理器用于操作文件的按每行读写
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            yield f.readline()

    def __str__(self):
        return 'Reader object to handle some string'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('file has handle successfully!')


def go():
    file_name = r'C:\Users\34853\Documents\WeChat Files\amoswewin\FileStorage\File\2019-04\123.csv'

    mongodb_url = 'localhost'
    mongodb_name = 'user_new'
    mongodb_table = 'object13'

    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv'
    ct = Cutter(file_name)
    ct.cut_to_record()
    # print(ct.data)
    # demo_dict = ''
    demo_dict = ct.data
    with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
        ms.save(demo_dict)


if __name__ == '__main__':

    go()
