# coding:utf-8
import re
import pymongo
import pymysql


class SqlSaver(object):
    # 初始化一些数据
    def __init__(self, database_name, password):
        # 创建链接
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    database=str(database_name),
                                    user='root',
                                    password=str(password),
                                    charset='utf8')
        # 获取cursor对象
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


class MongodbSaver(object):

    def __init__(self, mongodb_url, mongodb_db, mongodb_table):
        self.mongodb_table = mongodb_table
        self.client = pymongo.MongoClient(mongodb_url, connect=False)
        self.db = self.client[mongodb_db]

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
        if self.db[self.mongodb_table].insert(result):
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
        # self.feature_num = None
        # self.feature_str = ''
        # self.feature_list = None
        # self.data = {}
        self.raw_record = raw_record

    def cut_to_record(self):
        self.__cut_line()
        # self.feature_list = self.__cut_feature()
        # self.__data_model()

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

    def __cut_line(self):
        self.record_id = self.raw_record.split(',')[0]

    # def __cut_feature(self):
    #     soh = chr(int('0x01', 16))
    #     stx = chr(int('0x02', 16))
    #     etx = chr(int('0x03', 16))
    #     after_cut_str_list = re.split('{}'.format(soh), self.feature_str)
    #
    #     for i in after_cut_str_list:
    #         single_feature = re.split('{}|{}'.format(stx, etx), i)
    #         yield {'feature_field_id': single_feature[0],
    #                'feature_id': single_feature[1],
    #                'feature_value': single_feature[2]}

    # def __data_model(self):
    #     self.data = {'_id': self.record_id,
    #                  'feature_num': self.feature_num,
    #                  'feature_list': [item for item in self.feature_list]}

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
    line_num = 2 ** 32
    # mongodb_url = 'localhost'
    # mongodb_name = 'user_new'
    # mongodb_table = 'object31'
    k = 1

    with Reader(file_name, line_num) as rd:
        rd_gen = rd.read()

        for item in rd_gen:
            with Cutter(item) as ct:
                ct.cut_to_record()
                # print(ct.record_id)
                with SqlSaver('feature_skeleton', '123456') as db:
                    db.cursor.execute('INSERT INTO feature(feature_id) VALUES(%s)', ct.record_id)
                    db.conn.commit()
                    k += 1
                    print('insert {0:0>32} th record successfully!'.format(k))

            # with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
            #     ms.save(ct.data)


def go_insert():

    for item in range(10):
        with SqlSaver('feature_skeleton', '123456') as db:
            db.cursor.execute('INSERT INTO feature(feature_id) VALUES(%s)', item)
            db.conn.commit()
# def main():
#     with SqlSaver('feature_skeleton', '123456') as db:
#         # 数据库执行操作
#         db.execute('select * from stu')
#         content = db.fetchall()
#     print(content)


if __name__ == '__main__':
    go5()
    # go_insert()
