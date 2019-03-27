# coding:utf-8
import pymysql
import time


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


def read_line_record(file_name, line_num):
    k = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while k < line_num and line:
            yield line
            k += 1
            line = f.readline()


def cut_line_id(raw_record):
    return raw_record.split(',')[0]


def go5():
    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv'
    line_num = 2 ** 32
    k = 1
    start_time = int(time.time())

    for item in read_line_record(file_name=file_name, line_num=line_num):
        with SqlSaver('feature_skeleton', '123456') as db:
            db.cursor.execute('INSERT INTO feature(feature_id) VALUES(%s)', cut_line_id(item))
            db.conn.commit()
            k += 1
            if k % 10000 == 0:
                print('have cost {} second'.format(int(time.time())-start_time))
            print('insert {0:0>32} th record successfully!'.format(k))


def go6(table_name):
    """

    将上下文管理器更换到循环外可以合理解决这个问题
    :return:
    """
    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv'
    line_num = 2 ** 32
    k = 1
    start_time = int(time.time())

    with SqlSaver('feature_skeleton', '123456') as db:
        for item in read_line_record(file_name=file_name, line_num=line_num):
            db.cursor.execute('INSERT INTO {}(common_feature_index) VALUES(%s)'.format(table_name), cut_line_id(item))
            db.conn.commit()
            if k % 1000 == 0:
                print('have cost {} second'.format(int(time.time())-start_time))
            print('insert {0:0>16} th record successfully!'.format(k))
            k += 1


if __name__ == '__main__':
    go6('common_feature_test')
