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
from sqlalchemy.orm import sessionmaker

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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    address = Column(String(32))
    age = Column(Integer)

# 定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)


# 顶固删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()
init_db()


# 创建会话
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# 新建一个实例
user1 = User(name='aaron', address='chengdu', age=19)
user2 = User(name='john', address='chengdu', age=34)
user3 = User(name='jerry', address='hangzhou', age=14)
user4 = User(name='tom', address='nanjing', age=12)

#
# # 插入记录
# session.add(user1)
#
#
# # 查询记录
# our_user = session.query(User).filter_by(name='aaron').first()
# 如果有结果，会返回一个对象
# 否则会返回None
# 提交
# session.commit()

