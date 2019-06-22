# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/4 14:54
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from contextlib import contextmanager

from sqlalchemy import Column, Table, MetaData, create_engine, Integer
from sqlalchemy.dialects.postgresql import JSONB
import requests
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


@contextmanager
def auto_commit():
    try:
        yield
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


class NewTable(Base):
    __tablename__ = 'new_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSONB)


# engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres', echo=True)
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres', echo=True)


Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


new_record = NewTable()
new_record.data = {'j': 45, '89': 'ijoj'}


with auto_commit():
    session.add(new_record)
# session.commit()



