# -*- coding:utf-8 -*-
"""
create by young on 2019-03-16 23:06 
"""
from enum import Enum

__author__ = 'young'


def find_run_nian(num):
    """

    :param num:
    :return: true or false
    """
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        return True
    return False


print(find_run_nian(1900))
print(find_run_nian(2008))

# 闰年2月有29天，平年有28天
# enum_month = Enum
run = {
    'Jan': 31,
    'Feb': 29,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'Jun': 30,
    'Jul': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31,
}

ping = {
    'Jan': 31,
    'Feb': 29,
    'Mar': 30,
    'Apr': 30,
    'May': 31,
    'Jun': 30,
    'Jul': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31,
}
def count_days(str):
    """
    :param str:
    :return:
    """
    year = str[:3]
    month = str[3:5]
    day = str[5:]

    if int(month) >=2:
        pass
    if find_run_nian(int(year)):
        pass


    # return days
