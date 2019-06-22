# -*- coding:utf-8 -*-

"""
    2019/4/22 9:42 by young
"""
from contextlib import contextmanager
import pymongo


class MongodbSaver(object):

    def __init__(self, mongodb_url, mongodb_name, mongodb_table):
        self.mongodb_table = mongodb_table
        self.client = pymongo.MongoClient(mongodb_url, connect=False)
        self.db = self.client[mongodb_name]

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


class MongodbSaverWithoutManager(object):
    def __init__(self, mongodb_url, mongodb_name, mongodb_table):
        self.mongodb_table = mongodb_table
        self.client = pymongo.MongoClient(mongodb_url, connect=False)
        self.db = self.client[mongodb_name]

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     pass

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


# 由于这里是不做前处理和后处理，所以可以使用return
@contextmanager
def add_contextmanager(mongodb_url, mongodb_name, mongodb_table):
    yield MongodbSaverWithoutManager(mongodb_url, mongodb_name, mongodb_table)


# 由于我们使用了contextmanager，所以使用return也可以实现上下文管理器
@contextmanager
def add_contextmanager_return(mongodb_url, mongodb_name, mongodb_table):
    return MongodbSaverWithoutManager(mongodb_url, mongodb_name, mongodb_table)


def go(demo_dict):
    mongodb_url = 'localhost'
    mongodb_name = 'test_mongodb'
    mongodb_table = 'object31'

    with MongodbSaver(mongodb_url, mongodb_name, mongodb_table) as ms:
        ms.save(demo_dict)


def go_without_manager(demo_dict):
    mongodb_url = 'localhost'
    mongodb_name = 'test_mongodb'
    mongodb_table = 'object32'

    with add_contextmanager(mongodb_url, mongodb_name, mongodb_table) as ms:
        ms.save(demo_dict)


def go_without_manager_with_return(demo_dict):
    mongodb_url = 'localhost'
    mongodb_name = 'test_mongodb'
    mongodb_table = 'object33'

    with add_contextmanager(mongodb_url, mongodb_name, mongodb_table) as ms:
        ms.save(demo_dict)


if __name__ == "__main__":
    go_without_manager_with_return({'hello': 1})
