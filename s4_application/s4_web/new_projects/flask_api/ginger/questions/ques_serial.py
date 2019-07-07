# -*-encoding:utf-8 -*-
"""
    2019/4/20 6:50
    create by young
"""


"""
序列化器，
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
secret_key = 'xxxxdfsafe'
s= Serializer(secret_key)
token = s.dumps({'id': 89}).decode('utf-8')
data = s.loads(token.encode('utf-8'))
uid = data.get('id')
"""
