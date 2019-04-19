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


class Cutter(object):
    """
    改写为处理单行数据的返回内容
    实例化之后，销毁
    """

    __slots__ = ('record_id', 'feature_num', 'feature_str', 'feature_list', 'data', 'raw_record')

    def __init__(self, raw_record):
        self.record_id = None
        self.feature_num = None
        self.feature_str = ''
        self.feature_list = None
        self.data = {}
        self.raw_record = raw_record

    def cut_to_record(self):
        self.__cut_line()
        self.feature_list = self.__cut_feature()
        self.__data_model()

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

    def __cut_line(self):
        self.record_id, self.feature_num, self.feature_str = self.raw_record.split(',')

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
                     'feature_num': self.feature_num,
                     'feature_list': [item for item in self.feature_list]}

    def __del__(self):
        print('del the object')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self


class Reader(object):
    """
    撰写一个上下文管理器用于操作文件的按每行读写
    yield添加''之后出现错误
    如下：
        def read(self):
        k = 0
        with open(self.file_name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while k < self.line_num and line:
                yield line
                k += 1
                line = f.readline()
            yield ''
    正确的写法是：
        def read(self):
        k = 0
        with open(self.file_name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while k < self.line_num and line:
                yield line
                k += 1
                line = f.readline()
    """
    def __init__(self, file_name, line_num):
        self.file_name = file_name
        self.line_num = line_num

    def read(self):
        k = 0
        with open(self.file_name, 'r', encoding='utf-8') as f:
            line = f.readline()
            while k < self.line_num and line:
                yield line
                k += 1
                line = f.readline()

    def __str__(self):
        return 'Reader object to handle some string'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('file reader has been created successfully!')


def go5():
    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv'
    line_num = 10
    mongodb_url = 'localhost'
    mongodb_name = 'user_new'
    mongodb_table = 'object31'

    with Reader(file_name, line_num) as rd:
        rd_gen = rd.read()

    for item in rd_gen:
        with Cutter(item) as ct:
            ct.cut_to_record()
            print(ct.data)
            # with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
            #     ms.save(ct.data)


if __name__ == '__main__':

    go5()
