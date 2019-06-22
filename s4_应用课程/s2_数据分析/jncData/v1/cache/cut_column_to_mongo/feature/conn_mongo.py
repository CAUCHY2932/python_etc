# -*- coding:utf-8 -*-

"""
    2019/4/18 11:31 by young
"""


import pymongo


# settings


class MongodbSaver(object):
    """

    保存所有的数据到mongodb
    传入一个字典数据
    返回处理结果
    https://blog.csdn.net/wsp_1138886114/article/details/80402039
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

    def query(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":

    mongo_url = 'localhost'
    mongo_db = 'user_new'
    mongo_table = 'sample3'

    demo_dict = {
        '_id': '810d5366057b3f58',
        'length': 1025,
        'feature_list': [
                    {'feature_field_id': '101', 'feature_id': '412797', 'feature_value': '1.0'},
                    {'feature_field_id': '125', 'feature_id': '3438772', 'feature_value': '1.0'},
                    {'feature_field_id': '126', 'feature_id': '3438778', 'feature_value': '1.0'},
                    {'feature_field_id': '127', 'feature_id': '3438782', 'feature_value': '1.0'},
                    {'feature_field_id': '128', 'feature_id': '3864885', 'feature_value': '1.0'},
                    {'feature_field_id': '129', 'feature_id': '3864888', 'feature_value': '1.0'},
                    {'feature_field_id': '150_14', 'feature_id': '3960367', 'feature_value': '0.45932'},]
        }

    with MongodbSaver(mongo_url, mongo_db, mongo_table) as ms:
        ms.save(demo_dict)
