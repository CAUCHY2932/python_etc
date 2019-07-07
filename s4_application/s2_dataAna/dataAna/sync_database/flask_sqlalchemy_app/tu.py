# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/3 16:09
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('sqlite:///memory.db', echo=True)
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres', echo=True)
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name = {}, fullname= {}, nickname= {})>".format(self.name,
                                                                      self.fullname,
                                                                      self.nickname)


# 建立表
Base.metadata.create_all(engine)
# 建立会话，crud
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

ed_user = User(name='ed2',
               fullname='Ed Jones',
               nickname='edsnickname')


session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
session.commit()
print(our_user)
