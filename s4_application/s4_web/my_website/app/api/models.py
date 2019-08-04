# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-08-03 20:58
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import create_engine

from app import db
from door import app


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

#
# class User(db.Model):
#     pass


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    # users = db.relationship('User', backref='role', lazy='dynamic')


# class AnonymousUser(db.Model):
#     pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
