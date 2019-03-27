# -*- coding:utf-8 -*-
__author__ = 'bliss'

from flask_cache import Cache
# 新的插件方式已经被采用，是flask_cache 而非flask.ext.cache
# flask-cache 全局引用
cache = Cache()
