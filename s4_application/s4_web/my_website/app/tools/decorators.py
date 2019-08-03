# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019-08-03 22:59
    :copyright: © 2019 young <haochen2932@foxmail.com>
    :license: None, see LICENSE for more details.
"""
import functools


def permission_required(s):
    def deco(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if not s:
                return None
            return f(*args, **kwargs)
        return wrapper
    return deco





