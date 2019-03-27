# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/6/3 16:02
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import math
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Table:
    pass

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('postgresql://scott:tiger@localhost/')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

# work with sess
myobject = MyObject('foo', 'bar')
session.add(myobject)
session.commit()






