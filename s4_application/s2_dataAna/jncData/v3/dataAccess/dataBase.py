# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/30 12:02
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import pymongo
import pymysql


class MongodbSaver(object):
    """
    建立一个mongodb的对象
    连接到指定的数据库实例
    对集合（表）进行操作

    """
    def __init__(self, mongodb_url, mongodb_name, mongodb_table):
        self.mongodb_table = mongodb_table
        self.client = pymongo.MongoClient(mongodb_url, connect=False)
        self.db = self.client[mongodb_name]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def save_record(self, result):
        """
        把字典数据插入mongodb

        :param result: 字典格式
        :return: bool值，确定是否插入成功
        """
        if self.db[self.mongodb_table].insert(result):
            print('Successfully Saved to Mongodb', result)
            return True
        return False

    def insert_record(self):

        pass

    def update_record(self):

        pass

    def delete_record(self):

        pass


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
