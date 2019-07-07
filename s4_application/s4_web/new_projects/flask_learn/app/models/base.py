# -*-encoding:utf-8 -*-
"""
    2019/4/19 17:16
    create by young
"""
from sqlalchemy import SmallInteger, Column, Integer
from datetime import datetime
"""
类变量和实例变量
类变量是在类实现时，进行初始化的
实例变量是实例化一个对象时，进行初始化
"""


class Base(object):
    __abstract__ = True

    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=True)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attr(self, attr_dict):
        for key, value in attr_dict:
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
