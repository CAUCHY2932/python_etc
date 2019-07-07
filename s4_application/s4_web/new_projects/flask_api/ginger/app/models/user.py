# -*-encoding:utf-8 -*-
"""
    2019/4/21 0:00
    create by young
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        # 在对象内部创建对象本身，有些矛盾，但对于静态方法和类方法是可以的
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
        pass
