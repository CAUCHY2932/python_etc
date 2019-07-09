# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/7/9 14:55
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""

from flask import Blueprint
from sqlalchemy import and_

from .model import Employee, Activity


main = Blueprint('main', __name__)


# @main.route('/<userid>')
# def index(userid):
#     return 'userid is {}'.format(userid)

@main.route('/<userid>')
def index(userid):

    # 确定当前用户
    current_user = Employee.query.filter_by(id=userid).first()
    # name = current_user.name
    title = current_user.title

    # 确定职位范围
    department_level_one = current_user.department_level_one
    department_level_two = current_user.department_level_two
    department_level_three = current_user.department_level_three
    print(department_level_one, department_level_two, department_level_three)
    if title == '城市经理':
        xiashu = Employee.query.filter_by(
            department_level_one=department_level_one,
            department_level_two=department_level_two,
            department_level_three=department_level_three).all()
    elif title == '办事处主任':
        xiashu = Employee.query.filter_by(
            department_level_one=department_level_one,
            department_level_two=department_level_two).all()
    elif title == '大区营销总监':
        xiashu = Employee.query.filter_by(department_level_one=department_level_one).all()
    else:
        xiashu = []
    # name_list = [x.name for x in xiashu]

    ids = [x.id for x in xiashu]
    random_gen = Employee.query.filter(Employee.id.in_(ids))

    name_list = [x.name for x in random_gen]
    return 'have query {} records, username is \n{}'.format(len(name_list), name_list)


# books = session.query(Book) \
#         .filter(Book.id.in_([1, 3, 5])) \
#         .all()