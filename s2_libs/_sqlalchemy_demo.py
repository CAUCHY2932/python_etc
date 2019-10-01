from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True, autoincrement=True)
    name = Column(String(20))

link = 'mysql+pysqlconnector://root:password@localhost:3306/test'

engine = create_engine(link)

DBSession = sessionmaker(bind=engine)

# 使用session进行操作
session = DBSession()


def test_sqlalchemy_core():
    # 最快
    session.execute(User.__table__.insert(),
                    [dict(name=str(x)) for x in range(10)])
    session.commit()


def test_sqlalchemy_orm_bulk_insert():
    # 中等
    session.bulk_insert_mappings(User,
                                 [dict(name=str(x))
                                  for x in range(10)])
    session.commit()


def test_insert_save_objects():
    # 最慢
    session.bulk_save_objects([User(name=str(i))
                               for i in range(10000)])
    session.commit()
