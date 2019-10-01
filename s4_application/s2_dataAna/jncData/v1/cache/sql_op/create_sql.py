# -*- coding:utf-8 -*-

"""
    2019/4/22 13:19 by young
    这里不能指定integer的长度
"""
# https://www.cnblogs.com/ccorz/p/5711955.html
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# settings
database_type = 'mysql'
database_driver = 'pymysql'
user_name = 'root'
password = '123456'
host = 'localhost'
port = 3306
database_name = 'feature_skeleton'


# 进行初始化操作
engine = create_engine("{}+{}://{}:{}@{}:{}/{}".format(database_type,
                                                       database_driver,
                                                       user_name,
                                                       password,
                                                       host,
                                                       port,
                                                       database_name),
                       max_overflow=5)
Base = declarative_base()


class CommonFeatureTest(Base):
    __tablename__ = 'common_feature_test2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    common_feature_index = Column(String(32), nullable=False)


# 定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)


# 顶固删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()
init_db()
