"""
 Created by 七月 on 2018/5/10.
"""

__author__ = '七月'

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
