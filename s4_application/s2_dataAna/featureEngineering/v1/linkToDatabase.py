# -*- coding:utf-8 -*-

"""
    2019/4/12 13:06 by young
"""


import sqlalchemy


# settings
"""
参数过多，需要封装，使用上下文管理器
dialect，是数据库类型包括：sqlite, mysql, postgresql, oracle,  mssql等
driver，指定连接数据库的API，如：`psycopg2``, ``pyodbc``, ``cx_oracle``等，为可选关键字。
username，用户名
password，密码
host，网络地址ip
port，数据库端口
database，数据库名称
"""
SETTINGS = {
    'dialect': '',
    'driver': '',
    'username': '',
    'password': '',
    'host': '',
    'port': '',
    'database': '',
}
dialect = ''
driver = ''
username = ''
password = ''
host = ''
port = ''
database = ''
link = f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'
engine = sqlalchemy.create_engine(link, encoding='utf-8', echo=True)

