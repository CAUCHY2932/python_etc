# -*- coding:utf-8 -*-
"""
create by young on 2019-03-17 02:51 
"""

__author__ = 'young'


def update(var, stu_infos):
    if var not in stu_infos.keys():
        print('不存在这个用户的信息')
        return None
    return None


def delete(var, stu_infos):
    if var not in stu_infos.keys():
        print('无法删除不存在的信息')
        return None
    stu_collections.pop(var)


def query():
    pass


def create():
    pass


stu_collections = {
    'libai': {
        'id': '',
        'age': '',
        'stu_num': '',

    },
}

print('-' * 20)
print('欢迎来到学生管理系统')
print('-' * 20)

order = input('请输入你需要执行的命令：\n')
print(order.strip())

if order.strip() == '1':
    a = input('请输入你想要删除的学生信息:\n')
    delete(a.strip(), stu_collections)
print(stu_collections)

print('-' * 20)
print('欢迎来到学生管理系统')
print('-' * 20)
