# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 11:43
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    title = Column(String(64))
    rating = Column(String(16))

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)





