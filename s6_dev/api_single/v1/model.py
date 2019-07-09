# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 15:16
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
from sqlalchemy import Column, String

from v1 import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(8))
    company_range = db.Column(db.String(8))


