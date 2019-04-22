# -*- coding:utf-8 -*-

"""
    2019/4/22 13:19 by young
"""
# https://www.cnblogs.com/ccorz/p/5711955.html
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:7ujm8ik,@192.168.4.193:3306/testsql", max_overflow=5)
Base = declarative_base()


class CommonFeatureTest(Base):
    __table_name__ = 'common_feature_test'
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
