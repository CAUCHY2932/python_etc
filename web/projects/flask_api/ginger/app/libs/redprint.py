# -*-encoding:utf-8 -*-
"""
    2019/4/20 4:40
    create by young
"""


class Redprint(object):
    """
    模仿蓝图创造一个红图
    """

    def __init__(self,
                 name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):

        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
