# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/4 9:54
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import Column, Table, MetaData, create_engine, Integer
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

engine = create_engine("postgresql://scott:tiger@localhost/test")
# with engine.connect() as conn:
#     conn.execute("SET search_path TO test_schema, public")
#     meta = MetaData()
#     referring = Table('referring', meta,
#                       autoload=True, autoload_with=conn)

data_table = Table('data_table', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('data', JSONB)
                   )

with engine.connect() as conn:
    conn.execute(
        data_table.insert(),
        data={"key1": "value1", "key2": "value2"}
    )
