# -*-encoding:utf-8 -*-
"""
    2019/4/19 17:14
    create by young
"""

from sqlalchemy import Column, String, Integer, Float
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
    __tablename__ = 'user1'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    send_counter = Column(Integer, default=0)
    _password = Column('password', String(128))
    beans = Column(Float, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
