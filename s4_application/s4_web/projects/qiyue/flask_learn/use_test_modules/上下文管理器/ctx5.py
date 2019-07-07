# -*-encoding:utf-8 -*-
"""
    2019/4/20 1:26
    create by young
使用上下文管理器，进行数据库的访问操作
如果我们要对一个类进行子类的操作，我们可以尝试一下改变父类的名字

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

"""

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e
