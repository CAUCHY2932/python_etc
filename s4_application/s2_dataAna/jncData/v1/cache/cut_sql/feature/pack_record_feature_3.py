# coding:utf-8
import re
from datetime import datetime

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


def buffer_receive(item, length, lst=[]):
    lst.append(item)

    pass





def go5():
    """

    这种写法对数据库交互太过于频繁，可以尝试一次获取n条，然后插入

    n = 10
    for item in range(n):
        pass

    包装一个list，进行批量插入
    :return:
    """

    file_name = r'C:\Users\LvYangyang\Downloads\sample_test.tar\sample_test\common_features_test.csv'
    line_num = 2 ** 32
    k = 1
    m = 1
    insert_list = []
    insert_num = 1000
    for item in read_line_record(file_name=file_name, line_num=line_num):
        m += 1
        insert_list.append(item)
        if m == insert_num:
            # TODO 写入一千条数据，并将insert_list置空
            pass
        else:
            # TODO 如果最后一段不到一千条，进行处理
            pass

        with SqlSaver('feature_skeleton', '123456') as db:
            db.cursor.execute('INSERT INTO feature(feature_id) VALUES(%s)', cut_line_id(item))
            db.conn.commit()
            k += 1
            print('insert {0:0>32} th record successfully!'.format(k))


def go6():
    # 将初始化一个对象的操作放置到循环之外，可以显著提高插入速率
    pass


if __name__ == '__main__':
    go5()
