# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 11:43
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, orm

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    title = Column(String(256))
    rating_average = Column(String(16))
    subtype = Column(String(128))
    origin_title = Column(String(256))

    genres = Column(String(128))
    image = Column(String(256))

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            # if hasattr(self, k) and k != 'id':
            #     setattr(self, k, v)
            if hasattr(self, k):
                setattr(self, k, v)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'year', 'rating_average',
                       'subtype',
                       'genres',
                       'image',
                       'origin_title']

    def keys(self):
        # return self.fields
        return ['id', 'title', 'year', 'rating_average',
                'subtype',
                'genres',
                'image',
                'origin_title']

    def __getitem__(self, item):
        return getattr(self, item)
