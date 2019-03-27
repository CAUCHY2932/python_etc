# -*-encoding:utf-8 -*-
"""
    2019/4/20 23:37
    create by young
"""


from enum import Enum


class ClientTypeEnum(Enum):
    # 使用枚举来代表类型
    USER_EMAIL = 100
    USER_MOBIL = 101

    # 微信

    USER_MINA = 200
    USER_WX = 201
