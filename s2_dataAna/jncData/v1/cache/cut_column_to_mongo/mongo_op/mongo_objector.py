# -*- coding:utf-8 -*-

"""
    2019/4/19 14:23 by young
"""


import pymongo


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
