# -*- coding:utf-8 -*-

"""
    2019/4/18 13:07 by young
"""

from pymysql import *  # 导数据库包


class Dbb(object):
    # 初始化一些数据
    def __init__(self, database_name, password):
        # 创建链接
        self.conn = connect(host='localhost',
                            port=3306,
                            database=str(database_name),
                            user='root',
                            password=str(password),
                            charset='utf8')
        # 获取cursor对象
        self.cs1 = self.conn.cursor()

    def __enter__(self):
        return self.cs1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cs1.close()
        self.conn.close()


def main():
    with Dbb('conn_test', '123456') as db:
        # 数据库执行操作
        db.execute('select * from stu')
        content = db.fetchall()
    print(content)


if __name__ == '__main__':
    main()
