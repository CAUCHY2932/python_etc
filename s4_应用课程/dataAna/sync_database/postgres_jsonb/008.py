# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/4 14:14
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import Column, Table, MetaData, create_engine, Integer
from sqlalchemy.dialects.postgresql import JSONB
import requests
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class NewTable(Base):
    __tablename__ = 'new_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSONB)


# engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres', echo=True)
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres')


Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


new_record = NewTable()
new_record.data = {'j': 45, '89': 'ijoj'}


session.add(new_record)
session.commit()
