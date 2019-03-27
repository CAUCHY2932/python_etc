import pymysql
import warnings
import requests
# from conf import *

warnings.filterwarnings("ignore")


class Save_information:
    """建表语句"""

    def __init__(self, host='localhost', port=3306, db='cms', user='root', passwd='1234', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        self.cursor = self.conn.cursor()

    def insert_data(self, i):
        insert_sql = """
            insert ignore into firms(title,date,,content,link,source) values(%s,%s,%s,%s,%s,%s)
        """.format()
        param = self.cursor.execute(insert_sql, i)
        if param != 1:
            # print("已存在")
            pass
        else:
            """通知用户"""
            # requests.get(new_Address)
            print("有新数据啦")
            pass
        # print(param)
        self.conn.commit()
        # #关闭数据库
        # self.cursor.close()
        # self.conn.close()

    # def insert_status(self, userid, login_status, login_time, code_counts, code_time):
    #     insert_sql = """
    #         insert into user_status(userid,login_status,login_time,code_counts,code_time) values(%s,%s,%s,%s,%s)
    #         on duplicate key update login_status=values(login_status),login_time=values(login_time),code_counts=values(code_counts),code_time=values(code_time);
    #     """
    #     self.cursor.execute(insert_sql, (userid, login_status, login_time, code_counts, code_time))
    #     self.conn.commit()
    #     # #关闭数据库
    #     # self.cursor.close()
    #     # self.conn.close()

    # def keep_alive(self):
    #     self.cursor.execute('select * from user_status')


# class Read_user_info:
#     def __init__(self):
#         self.conn = pymysql.connect(host="127.0.0.1", user="root", password='root',
#                                     db="phone", charset='utf8')
#         self.cursor = self.conn.cursor()

#     def read_user_info(self):
#         sql = """
#             select * from user_info
#         """
#         self.cursor.execute(sql)
#         data = self.cursor.fetchall()
#         for i in data:
#             print(i)


# if __name__ == "__main__":
#     r = Read_user_info()
#     r.read_user_info()
