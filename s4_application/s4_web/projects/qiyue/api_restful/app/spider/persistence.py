# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/4/24 14:00
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from app.models.base import Movie, db


class MysqlStorage(object):
    @classmethod
    def is_exist(cls, id):
        """
        :return:
        """
        movie = Movie()
        mv = movie.query.filter_by(id=id).first()
        if mv:
            return mv
        return None

    @classmethod
    def insert_to_mysql(cls, data):
        movie = Movie()
        movie.set_attrs(data)

        db.session.add(movie)
        db.session.commit()

        return movie
