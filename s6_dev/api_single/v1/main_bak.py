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

    current_user = Employee.query.filter_by(id=userid).first()
    name = current_user.name
    title = current_user.title
    department_level_one = current_user.department_level_one
    department_level_two = current_user.department_level_two
    department_level_three = current_user.department_level_three
    print(department_level_one, department_level_two, department_level_three)
    if title == '城市经理':
        filter_dict ={
            department_level_one == department_level_one,
            department_level_two == department_level_two,
            department_level_three == department_level_three,
        }
        xiashu = Employee.query.filter_by(department_level_one=department_level_one, department_level_two=department_level_two, department_level_three=department_level_three).all()
        # xiashu = Employee.query.filter_by(*filter_dict).first()
        # print(xiashu)
        # for item in xiashu:
        #     print(item)
    else:
        xiashu = []
    name_list = [x.name for x in xiashu]

    return 'userid is {}'.format(name_list)
