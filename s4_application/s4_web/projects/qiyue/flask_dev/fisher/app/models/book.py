# -*- coding:utf-8 -*-
"""
    create by young on 2018/12/29 15:36
"""

from app.models.base import *


class Book(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String(50), nullable=False)
    author=Column(String(30), default='未名')
    binding=Column(String(20))
    publisher=Column(String(50))
    price=Column(String(30))
    pages=Column(Integer)
    pubdate=Column(String(20))
    isbn=Column(String(15), nullable=False, unique=True)
    summary=Column(String(1000))
    image=Column(String(50))


    def sample(self):
        pass
