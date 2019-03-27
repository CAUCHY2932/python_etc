# coding:utf-8


import pymysql


# setting


class SqlSaver(object):
    def __init__(self, database_name, password):
        self.conn = pymysql.connect(
                    port=3306,
                    database=str(database_name),
                    user='root',
                    password=str(password),
                    charset='utf8')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        """
        使用游标进行操作
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def save(self, insert_sql):
        try:
            self.cursor.execute(insert_sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def query(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class Dbb(object):
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
        self.cs1 = self.conn.cursor()

    def __enter__(self):
        return self.cs1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cs1.close()
        self.conn.close()


if __name__ == "__main__":
    with SqlSaver() as ss:
        ss.save()
