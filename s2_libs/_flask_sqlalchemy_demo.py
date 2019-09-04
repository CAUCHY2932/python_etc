# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

# 使用flask_sqlalchemy自动回进行配置
db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = '''postgresql+psycopg2://jncreport:jncreport890@jncreport.cotpwdfxy0tl.rds.cn-northwest-1.amazonaws.com.cn:5432/report'''


def create_app():
    app = Flask(__name__)

    return app


app = create_app()


@app.route('/')
def index():
    return 'hello'


class User(db.Model):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True, autoincrement=True)
    name = Column(String(20))


def test_sqlalchemy_core():
    # 最快
    db.session.execute(User.__table__.insert(),
                       [dict(name=str(x)) for x in range(10)])
    db.session.commit()


def test_sqlalchemy_orm_bulk_insert():
    # 中等
    db.session.bulk_insert_mappings(User,
                                    [dict(name=str(x))
                                     for x in range(10)])
    db.session.commit()


def test_insert_save_objects():
    # 最慢
    db.session.bulk_save_objects([User(name=str(i))
                                  for i in range(10000)])
    db.session.commit()


if __name__ == '__main__':
    app.run(port=5010)
