# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/30 11:42
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
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
