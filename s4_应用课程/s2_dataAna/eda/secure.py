# -*- coding:utf-8 -*-

"""
    2019/4/17 17:39 by young
"""


# link_setting = {
#     'database_type': '',
#     'driver': '',
#     'user': '',
#     'password': '',
#     'host': '',
#     'port': '',
#     'database': '',
# }

database_type = ''
driver = ''
user = ''
password = ''
host = ''
port = ''
database = ''
SQLALCHEMY_DATABASE_URI = f'{database_type}+{driver}://{user}:{password}@{host}:{port}/{database}'
