# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 15:16
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
# from sqlalchemy import Column, String
from v1 import db


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(8))
    company_range = db.Column(db.String(8))
    company_subrange = db.Column(db.String(8))
    employee_group = db.Column(db.String(8))
    employee_subgroup = db.Column(db.String(8))
    employee_status = db.Column(db.String(8))
    salary_range = db.Column(db.String(8))
    department_level_one = db.Column(db.String(8))
    department_level_two = db.Column(db.String(20))
    department_level_three = db.Column(db.String(255))
    title = db.Column(db.String(255))
    department_code = db.Column(db.String(11))
    department = db.Column(db.String(255))
    city_kind = db.Column(db.String(255))
    province = db.Column(db.String(255))
    city = db.Column(db.String(255))
    district = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    # def __repr__(self):
    #     return '雇员表'


class Activity(db.Model):
    __tablename__ = 'activity'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(50))
    user_code = db.Column(db.String(50))
    distributor_code = db.Column(db.String(50))
    policy_id = db.Column(db.BigInteger)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.TIMESTAMP)
    product_group_id = db.Column(db.BigInteger)
    is_deleted = db.Column(db.Integer)
